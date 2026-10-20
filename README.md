# HYDRA-pCO₂: A Hybrid Machine Learning and Data Assimilation Framework for Monthly Global Surface Ocean pCO₂ Reconstruction

This GitHub repository contains the code developed for the MSc thesis _"HYDRA-pCO₂: A Hybrid Machine Learning and Data Assimilation Framework for Monthly Global Surface Ocean pCO₂ Reconstruction"_ by Evie Stergiopoulou (2026).

The thesis was completed as part of the MSc Environmental Data Science and Machine Learning at Imperial College London, in collaboration with the Flanders Marine Institute (VLIZ).

![HYDRA-pCO₂ Demo](figures/demos/HYDRA-pco2_rotating_globe.gif)

[Click here](https://zenodo.org/records/22126123) to download the HYDRA-pCO₂ product.


## Setup

Clone the repository:

```bash
git clone https://github.com/ese-ada-lovelace-2025/irp-efs25.git
cd irp-efs25
```

Create and activate the Conda environment:

```bash
conda env create -f environment.yml
conda activate irp-efs25
```

The notebooks use paths relative to the repository root, so the repository can be cloned to a different location or under a different name without changing the paths.

> **Note:** The ResNet training and data assimilation workflows use CUDA-enabled PyTorch and were developed for Linux with NVIDIA GPUs. The provided environment is therefore not intended for direct use on macOS/Apple Silicon; use an HPC system or a suitable Linux environment instead.

## Data

The raw and intermediate data are omitted from the repository due to their size. Some datasets are downloaded automatically by the notebooks, but for datasets that are not, they must be downloaded separately before running the workflow.

### 1. SOCAT

SOCAT data must be downloaded separately from the [Surface Ocean CO₂ Atlas v2026](https://socat.info/index.php/version-2026/), specifically the monthly gridded (nc) version from the main source (NCEI).

The SOCAT data should be placed under:

```text
data/raw/socat/
```

> **Note:** The SOCAT processing notebook also downloads ERA5 data automatically from the Copernicus Climate Data Store (CDS). This requires a configured CDS API key (`.cdsapirc`). If you have not configured one, follow the [CDS API setup instructions](https://cds.climate.copernicus.eu/how-to-api) before running the notebook. You will need to create/log in to a CDS account and add your personal API token to `~/.cdsapirc`.

### 2. NOAA Marine Boundary Layer xCO₂

The NOAA Marine Boundary Layer Reference data must be downloaded separately from the [NOAA Global Monitoring Laboratory](https://gml.noaa.gov/ccgg/mbl/data.php) (Carbon Cycle Greenhouse Gases > Marine Boundary Layer Reference) with the following selections:

- **Parameter:** `CO2`
- **Reference Type:** `Surface`
- **Zonal References:** `Global (90°S to 90°N)`
- **Start Date:** `1993-01`
- **End Date:** `2024-12`

After pressing "Submit" and "Download", the resulting `.txt` file should be placed under:

```text
data/raw/satellite/
```

### 3. Input4MIPs Boundary Forcing

The Input4MIPs Atmospheric CO₂ Boundary Forcing data must be downloaded separately from the [Earth System Grid Federation (ESGF)](https://metagrid.esgf-west.org/search/input4mips/). On the ESGF search page, use the following selections:

- **Variable ID:** `mole-fraction-of-carbon-dioxide-in-air`
- **Grid Label:** `gn-15x360deg`
- **Source ID:**
  - Historical: `UoM-CMIP-1-2-0`
  - SSP2-4.5: `UoM-MESSAGE-GLOBIOM-ssp245-1-2-0`

Both the historical and SSP2-4.5 datasets are required. After selecting the appropriate files, download the generated `.sh` scripts and run them from the command line using `bash`. For example:

```bash
bash <download_script>.sh
```

The downloaded files should be placed under:

```
data/raw/input4mips/
```

> Tip: Use ls -lh to check the downloaded file sizes and confirm that the files have been downloaded correctly

### 4. Existing pCO₂ Reconstruction Products (Optional)

To run the evaluation notebook `08_pco2_product_comparison` to produce the comparison plots with our product (`data/predictions/posterior/assimilated_pco2_1993_2024.zarr`) vs existing reconstruction approaches:

### i. SOM-FFN

The SOM-FFN data product can be downloaded from the [NOAA NCEI Ocean Carbon Acidification Data System](https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0160558/MPI_SOM-FFN_v2025/). After downloading, the resulting `MPI_SOM-FFN_v2025/SOM-FFN_v2025_CLIM_NCEI_OCADS.nc` file should be placed under:

```text
data/products/
```

### ii. SJTU-AViT

The SJTU-AViT data product can be downloaded from [Zenodo](https://zenodo.org/records/15331978).After downloading, the resulting `.nc` file should be placed under:

```text
data/products/
```

## Running the notebooks

The notebooks are numbered in the order in which the workflow should be run:

1. `01_cmip6_data`
2. `02_socat_data`
3. `03_satellite_data`
4. `04_xco2_data`
5. `05_xgboost_climatology`
6. `06_resnet_model`
7. `07_resnet_ensemble_evaluation`
7. `08_data_assimilation`
8. `09_product_comparison`
9. `10_product_demo`

> **Note:** Run the notebooks in this order, as later stages depend on outputs generated by earlier stages.

## HPC scripts

GPU acceleration is recommended for the computationally intensive stages of the workflow (e.g., model training).

The scripts in the `scripts/` directory are provided as examples for running these stages on an HPC system; they contain user- and system-specific paths and settings and therefore require adaptation before use.

## ResNet ensemble

The ResNet is trained as an ensemble of models. When running the ResNet workflow, a `MEMBER_ID` must be specified.

The `MEMBER_ID` is used to dynamically set the random seed:

```python
SEED = 42 + MEMBER_ID
```

For example:

```text
MEMBER_ID = 0  → SEED = 42
MEMBER_ID = 1  → SEED = 43
...
MEMBER_ID = 4  → SEED = 46
```

For full reproducibility, use `MEMBER_ID`s 0, 1, 2, 3, and 4.

## Repository structure
The final repository structure with the data files should therefore be:

```
irp-efs25/
├── data/
│   ├── raw/             # Downloaded source datasets
│   ├── processed/       # Processed intermediate datasets
│   ├── predictions/     # Model prior and assimilated posterior
│   └── products/        # Established pCO₂ reconstruction products
├── figures/             # Figures and product demonstrations
├── notebooks/           # Main workflow notebooks
├── scripts/             # HPC job submission scripts
├── logbook/             # Log of supervisor meetings
├── deliverables/        # Project plan and final report
├── environment.yml      # Conda environment
└── README.md
```

## Licence

This project is released under the MIT License.
