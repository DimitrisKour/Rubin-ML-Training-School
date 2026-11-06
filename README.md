# Rubin ML Training School 2026: Hands-On Anomaly Detection with AppleCiDEr and Hyrax

**Monday November 9 – Wednesday November 11, 2026**
School of Physics and Astronomy, University of Minnesota, John T. Tate Hall, 116 Church St SE, Minneapolis, MN 55455

This repository holds the schedule, setup instructions, and tutorial notebooks of a three-day LINCC Frameworks training school on transient classification, anomaly detection, and similarity search in astronomical alert streams. Participants build each workflow on labeled Zwicky Transient Facility (ZTF) alerts during the first two days, filter live alerts through the BOOM alert broker, and transfer their workflows to Rubin Data Preview 2 (DP2) in Hyrax during a hackathon on the third day. The school website is in [`docs/`](docs/index.html) and is served through GitHub Pages.

The school is supported by the [LSST Discovery Alliance](https://lsstdiscoveryalliance.org/) through the LINCC Frameworks Community Events program.

## Registration

Registration takes place through the [school registration form](https://forms.gle/131QcEVjUtkckCvb8), and selected participants receive logistics and preparation material by email.

## Before the school

Please complete the three steps below before Monday, November 9. Account problems can take several days to resolve, so start as soon as possible and write to [asasli@umn.edu](mailto:asasli@umn.edu) if any step fails. The full instructions are in [`setup/README.md`](setup/README.md).

1. **BOOM alert streams through Babamul.** Create an account at [babamul.caltech.edu](https://babamul.caltech.edu) and keep the Kafka username, Kafka password, and API token from your profile page at hand for the Day 1 activity.
2. **Rubin Science Platform.** Log in at [data.lsst.cloud](https://data.lsst.cloud) with your Rubin data-rights account and start a session in the Notebooks aspect once. Participants without Rubin data rights work on ZTF data or on live Rubin alerts through Babamul during the hackathon.
3. **Software.** Clone this repository, create the `rubin-ml-school` environment, and run [`setup/check_setup.ipynb`](setup/check_setup.ipynb).

```bash
git clone https://github.com/asasli/Rubin-ML-Training-School.git
cd Rubin-ML-Training-School
conda env create -f environment.yml
conda activate rubin-ml-school
python -m ipykernel install --user --name rubin-ml-school
```

## Schedule

All times are Central Time (CT). Every day opens with **Coffee & Pastries, 9:00–9:30 AM** and ends by **4:00 PM**. Sessions on Monday, Tuesday, and Wednesday morning take place in room 401-20, and the Wednesday afternoon hackathon takes place in room B55.

### Day 1, Monday November 9: Alert Brokers and Hyrax

| Time        | Session | Material |
|-------------|---------|----------|
| 9:00–9:30   | Coffee & Pastries | |
| 9:30–9:45   | **Welcome and introduction**: Argyro Sasli & Michael Coughlin | |
| 9:45–10:25  | **Lecture: ZTF and Rubin alert streams with BOOM**: Sushant Sharma Chaudhary | [`day1/01_boom_alert_streams`](day1/01_boom_alert_streams) |
| 10:25–11:05 | **Lecture: Babamul and its features**: Thomas Culino | [`day1/02_babamul`](day1/02_babamul) |
| 11:05–11:15 | Break | |
| 11:15–12:15 | **Lecture and demo: Hyrax, machine learning in the LINCC ecosystem**: Drew Oldag | [`day1/03_hyrax`](day1/03_hyrax) |
| 12:15–1:15  | Lunch | |
| 1:15–2:30   | **Activity: Babamul API usage and alert filtering**: Thomas Culino | [`day1/02_babamul`](day1/02_babamul) |
| 2:30–2:45   | Break | |
| 2:45–3:30   | **Activity: Hyrax hands-on, setting up the ZTF light-curve dataset** | [`day1/03_hyrax`](day1/03_hyrax) |
| 3:30–4:00   | **Activity: Hyrax hands-on, training a light-curve model on ZTF**: Drew Oldag | [`day1/03_hyrax`](day1/03_hyrax) |

### Day 2, Tuesday November 10: Classification, Anomaly Detection, Similarity Search, and MCP Servers

| Time        | Session | Material |
|-------------|---------|----------|
| 9:00–9:30   | Coffee & Pastries | |
| 9:30–10:45  | **Lecture / Activity: AppleCiDEr, multimodal classification of ZTF transients**: Argyro Sasli | [`day2/01_applecider_classification`](day2/01_applecider_classification) |
| 10:45–11:00 | Break | |
| 11:00–12:00 | **Activity: Anomaly detection with AppleCiDEr and LUNA**: Argyro Sasli | [`day2/02_anomaly_detection`](day2/02_anomaly_detection) |
| 12:00–1:00  | Lunch | |
| 1:00–2:30   | **Lecture / Activity: Similarity search in embedding space on ZTF alerts**: Sneha Maharjan | [`day2/03_similarity_search`](day2/03_similarity_search) |
| 2:30–2:45   | Break | |
| 2:45–4:00   | **Lecture / Activity: MCP servers for BOOM and ML models**: Leo Conforti | [`day2/04_mcp_servers`](day2/04_mcp_servers) |

### Day 3, Wednesday November 11: Active Learning and the DP2 Hackathon

| Time        | Session | Material |
|-------------|---------|----------|
| 9:00–9:30   | Coffee & Pastries (401-20) | |
| 9:30–10:45  | **Lecture / Activity: Active learning for classification and follow-up on ZTF**: Dimitrios Kourtesis (401-20) | [`day3/01_active_learning`](day3/01_active_learning) |
| 10:45–11:00 | Break | |
| 11:00–11:30 | **Lecture: From ZTF to Rubin, DP2 on the Rubin Science Platform**: Argyro Sasli (401-20) | [`day3/02_dp2_on_rsp`](day3/02_dp2_on_rsp) |
| 11:30–12:00 | **Hackathon kickoff**: teams and project choice (401-20) | [`day3/03_hackathon`](day3/03_hackathon) |
| 12:00–12:30 | Move to B55 | |
| 12:30–1:15  | Working lunch and hackathon start (B55) | |
| 1:15–3:00   | **Hackathon: porting workflows to DP2 in Hyrax** (B55) | [`day3/03_hackathon`](day3/03_hackathon) |
| 3:00–3:15   | Break | |
| 3:15–3:45   | **Lightning presentations** of hackathon projects (B55) | |
| 3:45–4:00   | **Closing remarks**: Argyro Sasli & Michael Coughlin (B55) | |

## Repository layout

```
Rubin-ML-Training-School/
├── README.md                     schedule and overview
├── environment.yml               conda environment for the school
├── requirements.txt              the same packages for pip
├── setup/                        before-the-school instructions, .env template, setup check
├── day1/
│   ├── 01_boom_alert_streams/    ZTF and Rubin alert streams with BOOM (Sushant Sharma Chaudhary)
│   ├── 02_babamul/               Babamul features, API usage, and alert filtering (Thomas Culino)
│   └── 03_hyrax/                 Hyrax lecture, demo, and hands-on (Drew Oldag)
├── day2/
│   ├── 01_applecider_classification/   AppleCiDEr classification (Argyro Sasli)
│   ├── 02_anomaly_detection/           AppleCiDEr and LUNA anomaly detection (Argyro Sasli)
│   ├── 03_similarity_search/           similarity search (Sneha Maharjan)
│   └── 04_mcp_servers/                 MCP servers for BOOM and ML models (Leo Conforti)
├── day3/
│   ├── 01_active_learning/       active learning (Dimitrios Kourtesis)
│   ├── 02_dp2_on_rsp/            DP2 light curves on the Rubin Science Platform (Argyro Sasli)
│   └── 03_hackathon/             hackathon instructions, project template, team projects
└── docs/                         school website for GitHub Pages
```

Each session folder has a `README.md` with the time, room, speaker, and learning goals of the session, and the speakers add their notebooks to these folders before the school.

## Rubin data rights

DP2 is proprietary to Rubin data-rights holders. DP2 data, including light curves extracted on the Rubin Science Platform, stays on the Rubin Science Platform and is never committed to this repository. The `.gitignore` excludes common data formats, and hackathon teams commit code and notebooks without outputs that contain DP2 data.

## Organizers and contact

The school is organized by Argyro Sasli and Michael Coughlin (University of Minnesota) with Drew Oldag (LINCC Frameworks). Questions go to [asasli@umn.edu](mailto:asasli@umn.edu).

## Acknowledgments

We thank Sushant Sharma Chaudhary, Sneha Maharjan, Sougat Dasgupta, Vaidehi Gupta, Tyler Barna, and Hal Yngve for their help with the organization of the school.

## License

The material in this repository is released under the GNU General Public License v3.0, as described in [`LICENSE`](LICENSE).

## Featured papers and code

### Papers

- Sasli, A., and Coughlin, M. 2026, *Anomaly-ranked confirmation slows new-class learning*, [arXiv:2611.03250](https://arxiv.org/abs/2611.03250)
- Sasli, A., et al. 2026, *Photometric classification and out-of-taxonomy detection of ZTF transients with FLARE*, [arXiv:2610.30656](https://arxiv.org/abs/2610.30656)
- Sasli, A., et al. 2026, *Catching Disguised Transients with ASTRANet: Anomaly-Aware Spectroscopic Classification and Conformal Calibration*, [arXiv:2607.08044](https://arxiv.org/abs/2607.08044)
- Junell, A., Sasli, A., et al. 2025, *Applying multimodal learning to Classify transient Detections Early (AppleCiDEr) I: Data set, methods, and infrastructure*, [arXiv:2507.16088](https://arxiv.org/abs/2507.16088)
- Jegou du Laz, T., et al. 2026, *BOOM and Babamul: a real-time, multi-survey, optical alert broker system operating at scale*, PASP, 138, 064503, [arXiv:2511.00164](https://arxiv.org/abs/2511.00164)
- Ghosh, A., Oldag, D., Tauraso, M., et al. 2026, *Hyrax: An Extensible Framework for Rapid ML Experimentation and Unsupervised Discovery in the Era of Rubin, Roman, and Euclid*, [arXiv:2605.18959](https://arxiv.org/abs/2605.18959)
- Bom, C. R., Mahabal, A., Bianco, F., et al. 2026, *Toward decision-aware AI for LSST-scale time-domain astronomy*, [arXiv:2606.05285](https://arxiv.org/abs/2606.05285)
- Coughlin, M. W., et al. 2023, *A Data Science Platform to Enable Time-domain Astronomy*, ApJS, 267, 31, [arXiv:2305.00108](https://arxiv.org/abs/2305.00108)
- van der Walt, S. J., Crellin-Quick, A., and Bloom, J. S. 2019, *SkyPortal: An Astronomical Data Platform*, JOSS, 4, 1247, [doi:10.21105/joss.01247](https://doi.org/10.21105/joss.01247)

### Code

- [AppleCiDEr](https://github.com/applecider-ml/applecider): multimodal transient classifier and anomaly-detection pipeline developed through the LINCC Incubator
- [FLARE](https://github.com/applecider-ml/flare): photometric classification and anomaly-detection module of AppleCiDEr, running in production on Fritz
- [LUNA](https://github.com/asasli/luna): classifier-agnostic library for novelty and anomaly detection on model embeddings and logits
- [BOOM](https://github.com/boom-astro/boom): multi-survey alert broker for ZTF and Rubin, written in Rust
- [Babamul](https://github.com/boom-astro/babamul): Python client for the public Babamul alert streams built on BOOM
- [SkyPortal](https://github.com/skyportal/skyportal): open-source platform for discovering, following up, and characterizing transients
- [Hyrax](https://github.com/lincc-frameworks/hyrax): LINCC Frameworks framework for training and analyzing machine-learning models on survey data
