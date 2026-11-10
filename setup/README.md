# Before the school

Please complete the three steps below before Monday, November 9, 2026. Account problems can take several days to resolve, so start as soon as possible and write to [asasli@umn.edu](mailto:asasli@umn.edu) if any step fails.

## 1. BOOM alert streams through Babamul

The Day 1 activities read live ZTF and Rubin alerts from Babamul, the public deployment of the BOOM alert broker.

1. Create an account at [babamul.caltech.edu](https://babamul.caltech.edu).
2. Open your profile page, where you find a Kafka username and password for reading the alert streams and an API token for cross-matches, photometry, object lookups, and cone searches.
3. Copy the template and fill in the three values:

   ```bash
   cp setup/.env.example setup/.env
   ```

A backup deployment runs at [babamul.umn.edu](https://babamul.umn.edu) with its own credentials on its own profile page. To use it, set `BABAMUL_ENV=backup` in your `.env` file and copy the credentials from the backup profile page.

The `.env` file holds personal credentials and is excluded from git by `.gitignore`. Never commit it.

## 2. Rubin Science Platform

The Day 3 hackathon runs on DP2 catalogs on the Rubin Science Platform.

1. Log in at [data.lsst.cloud](https://data.lsst.cloud) with your Rubin data-rights account.
2. Start a session in the Notebooks aspect once. This confirms that your account works and creates your home directory.
3. In a terminal on the Rubin Science Platform, clone this repository into your home directory:

   ```bash
   git clone https://github.com/asasli/Rubin-ML-Training-School.git
   ```

Participants without Rubin data rights work on ZTF data or on live Rubin alerts through Babamul during the hackathon, and do not need this step.

## 3. Software on your laptop

Create the school environment with conda (or mamba) and register it as a Jupyter kernel:

```bash
git clone https://github.com/asasli/Rubin-ML-Training-School.git
cd Rubin-ML-Training-School
conda env create -f environment.yml
conda activate rubin-ml-school
python -m ipykernel install --user --name rubin-ml-school
```

With plain pip in a fresh virtual environment, `pip install -r requirements.txt` installs the same packages.

Bring a laptop with a recent web browser and a terminal.

## 4. Check your setup

Open [`check_setup.ipynb`](check_setup.ipynb) with the `rubin-ml-school` kernel and run all cells. Every check should print `OK`. If a check fails, send the error message to [asasli@umn.edu](mailto:asasli@umn.edu).
