# From ZTF to Rubin, DP2 on the Rubin Science Platform

**Wednesday November 11, 11:00–11:30** · Room 401-20 · Argyro Sasli

This short lecture prepares the hackathon. It covers the DP2 catalogs on the Rubin Science Platform and the differences between ZTF and Rubin light curves that matter when a model moves from one survey to the other: the six *ugrizy* bands against the ZTF *g*, *r*, and *i* bands, difference fluxes in nJy against magnitudes, forced photometry with negative fluxes, and the change in cadence.

[`dp2_light_curves.ipynb`](dp2_light_curves.ipynb) runs on the Rubin Science Platform only. It queries DP2 for DiaObjects and their forced-photometry light curves, converts them into the format of the Day 1 Hyrax dataset, and saves them in your Rubin Science Platform home directory.

DP2 data stays on the Rubin Science Platform. Do not download it to your laptop or commit it to this repository.
