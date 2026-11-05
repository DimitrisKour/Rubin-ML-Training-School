# Hackathon: porting workflows to DP2 in Hyrax

**Wednesday November 11** · kickoff 11:30–12:00 in room 401-20 · hackathon 12:30–3:00 in room B55 · lightning presentations 3:15–3:45 in room B55

Teams of two to four participants take one of the workflows built on ZTF during Days 1 and 2 and make it run on Rubin DP2 light curves in Hyrax. The starting point is the light-curve file produced by [`../02_dp2_on_rsp/dp2_light_curves.ipynb`](../02_dp2_on_rsp/dp2_light_curves.ipynb) on the Rubin Science Platform.

## Project ideas

1. **Classification on DP2.** Apply the Day 1 Hyrax light-curve model to DP2, measure how its predictions change between ZTF and Rubin bands, and fine-tune it on a small labeled DP2 sample built from cross-matches with known transients and variable stars.
2. **Anomaly detection on DP2.** Compute LUNA scores on DP2 embeddings, calibrate a threshold at a target false-alarm rate, and inspect the most anomalous DiaObjects.
3. **Similarity search across surveys.** Embed ZTF and DP2 light curves with the same model and search DP2 for analogs of known ZTF transients.
4. **Active learning on DP2.** Use a query strategy from the morning session to choose which DP2 objects would be most informative to label.
5. **Alerts and archive.** Write a Babamul filter on live Rubin alerts and compare the selected objects with their DP2 light curves.

Participants without Rubin data rights choose a project on ZTF data or on live Rubin alerts through Babamul.

## Adding your project

1. Copy [`PROJECT_TEMPLATE.md`](PROJECT_TEMPLATE.md) to `projects/<team-name>/README.md` and fill it in.
2. Add your code and notebooks to `projects/<team-name>/`. Clear all notebook outputs that contain DP2 data before committing.
3. Open a pull request to this repository by the end of the day.

## Lightning presentations

Each team presents for three minutes, with at most two slides: what you tried on DP2, what changed with respect to ZTF, and what you would do next.
