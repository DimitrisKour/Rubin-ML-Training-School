"""Your model as a tool for the BOOM MCP server.

The server loads this file with `boom-mcp --plugin my_model.py`. Every function
decorated with `@tool()` becomes a tool the agent can call. `babamul(ctx)`
fetches data from BOOM with the caller's Babamul token.

`color_change` below works as-is. Replace it with your own model, or add yours
next to it; there is a sketch for the LUNA pipeline at the bottom.
"""

from mcp.server.mcpserver import Context

from boom_mcp import summarize as s
from boom_mcp.app import babamul, tool


@tool()
async def color_change(ctx: Context, object_id: str) -> dict:
    """The g - r color of a ZTF object at its first and latest epochs that have both
    bands within half a day. A positive change means it got redder; for a supernova
    that usually means it is cooling after peak."""
    obj = await babamul(ctx).get(f"/surveys/ZTF/objects/{object_id}")
    rows = [
        r for r in s.light_curve_rows(obj, "ZTF", other_survey=False)
        if "mag" in r and not r.get("negative")
    ]
    g = [r for r in rows if r["band"] == "ztfg"]
    r_band = [r for r in rows if r["band"] == "ztfr"]

    pairs = []
    for point in g:
        nearest = min(r_band, key=lambda r: abs(r["jd"] - point["jd"]), default=None)
        if nearest and abs(nearest["jd"] - point["jd"]) < 0.5:
            pairs.append({"time": s.jd_to_iso(point["jd"]), "g_minus_r": round(point["mag"] - nearest["mag"], 3)})

    if len(pairs) < 2:
        return {"object_id": object_id, "verdict": "not enough nights with both g and r detections"}
    change = pairs[-1]["g_minus_r"] - pairs[0]["g_minus_r"]
    verdict = "redder" if change > 0.1 else "bluer" if change < -0.1 else "about the same"
    return {"object_id": object_id, "first": pairs[0], "latest": pairs[-1], "change": round(change, 3), "verdict": verdict}


# A sketch with the LUNA pipeline from this morning. `my_features` is the part
# that depends on your model: it turns a BOOM object into the embeddings and
# logits LUNA expects.
#
# from luna import LUNAPipeline
#
# pipe = LUNAPipeline.load("luna_ztf.pkl")  # load once, when the server starts
#
#
# @tool()
# async def luna_anomaly(ctx: Context, object_id: str) -> dict:
#     """How unusual this object is to the LUNA pipeline trained this morning.
#     A small p-value means anomalous."""
#     obj = await babamul(ctx).get(f"/surveys/ZTF/objects/{object_id}")
#     out = pipe.predict(my_features(obj))
#     return {"object_id": object_id, "p_value": float(out["p_value"][0])}
