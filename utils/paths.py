"""
Central path configuration.

Bulk data should live on HPC scratch.
Local development can fall back to repository-relative data directory.
"""

import os
from pathlib import Path


# Shared HPC scratch root
SCRATCH_ROOT = Path(
    "/scratch/antwerpen/grp/ap_vliz_research/PPFC/evie.stergiopoulou/HYDRA-pCO2"
)

# Repository root: config_paths.py is expected in the project root
REPO_ROOT = Path(__file__).resolve().parent
LOCAL_DATA_ROOT = REPO_ROOT / "data"

# Allow override:
# e.g., export HYDRA_PCO2_DATA_ROOT=/scratch/.../HYDRA-pCO2/data
DATA_ROOT = Path(
    os.environ.get(
        "HYDRA_PCO2_DATA_ROOT",
        SCRATCH_ROOT / "data" if SCRATCH_ROOT.exists() else LOCAL_DATA_ROOT,
    )
)

# Main data directories
RAW_DIR = DATA_ROOT / "raw"
PROCESSED_DIR = DATA_ROOT / "processed"
EXTERNAL_DIR = DATA_ROOT / "external"
PREDICTIONS_DIR = DATA_ROOT / "predictions"
EVALUATION_DIR = DATA_ROOT / "evaluation"
PRODUCTS_DIR = DATA_ROOT / "products"

# Raw inputs
SATELLITE_RAW_DIR = RAW_DIR / "satellite"
CMIP6_RAW_DIR = RAW_DIR / "cmip6"
INPUT4MIPS_RAW_DIR = RAW_DIR / "input4mips"
SOCAT_RAW_DIR = RAW_DIR / "socat"
ERA5_RAW_DIR = RAW_DIR / "era5"
NOAA_RAW_DIR = RAW_DIR / "noaa"

# Processed outputs
SATELLITE_PROCESSED_DIR = PROCESSED_DIR / "satellite"
CMIP6_PROCESSED_DIR = PROCESSED_DIR / "cmip6"
INPUT4MIPS_PROCESSED_DIR = PROCESSED_DIR / "input4mips"
SOCAT_PROCESSED_DIR = PROCESSED_DIR / "socat"
XGBOOST_PROCESSED_DIR = PROCESSED_DIR / "xgboost_thermal"
MODEL_PROCESSED_DIR = PROCESSED_DIR / "models"

# Prediction outputs
PRIOR_PREDICTIONS_DIR = PREDICTIONS_DIR / "prior" / "ensemble_members"
POSTERIOR_PREDICTIONS_DIR = PREDICTIONS_DIR / "posterior"

# Evaluation outputs
RESNET_EVALUATION_DIR = EVALUATION_DIR / "resnet_ensemble"
PRODUCT_COMPARISON_DIR = EVALUATION_DIR / "product_comparison"

# Input files
NOAA_MBL_FILE = SATELLITE_RAW_DIR / "co2_GHGreference.1954248230_surface.txt"

SOCAT_FILE = SOCAT_RAW_DIR / "SOCATv2026_tracks_gridded_monthly.nc"

ERA5_FILE = ERA5_RAW_DIR / "era5_msl_full_monthly.nc"
ERA5_TEST_FILE = ERA5_RAW_DIR / "era5_msl_2003_monthly_test.nc"

# Processed products
NOAA_MBL_ZARR = (
    SATELLITE_PROCESSED_DIR
    / "noaa_gml_mbl_co2_1x1_monthly.zarr"
)

SATELLITE_COVARIATES_ZARR = (
    SATELLITE_PROCESSED_DIR
    / "satellite_covariates_1deg_1982_2024.zarr"
)

# Legacy products - keep until satellite pipeline is switched over
MULTIOBS_ZARR = (
    SATELLITE_PROCESSED_DIR
    / "multiobs_1deg_1993_2024.zarr"
)

OCCII_CHL_ZARR = (
    SATELLITE_PROCESSED_DIR
    / "occi_chl_1deg_1997_2024.zarr"
)

LEGACY_SATELLITE_COVARIATES_ZARR = (
    SATELLITE_PROCESSED_DIR
    / "satellite_covariates_1deg_1970_2024.zarr"
)

SOCAT_ZARR = (
    SOCAT_PROCESSED_DIR
    / "SOCATv2026_gridded_monthly.zarr"
)

INPUT4MIPS_CO2_ZARR = (
    INPUT4MIPS_PROCESSED_DIR
    / "atmCO2_1850_2100_regridded.zarr"
)

XGBOOST_THERMAL_ZARR = (
    XGBOOST_PROCESSED_DIR
    / "pco2_thermal_xgboost_1993_2024_1deg_monthly.zarr"
)

POSTERIOR_ZARR = (
    POSTERIOR_PREDICTIONS_DIR
    / "assimilated_pco2_1993_2024.zarr"
)

POSTERIOR_DIAGNOSTICS_ZARR = (
    POSTERIOR_PREDICTIONS_DIR
    / "posterior_diagnostics.zarr"
)

# Figures
FIGURES_DIR = (
    SCRATCH_ROOT / "figures"
    if SCRATCH_ROOT.exists()
    else REPO_ROOT / "figures"
)

CMIP6_FIGURES_DIR = FIGURES_DIR / "cmip6_processing"
SATELLITE_FIGURES_DIR = FIGURES_DIR / "satellite_processing"
SOCAT_FIGURES_DIR = FIGURES_DIR / "socat_processing"
ASSIMILATION_FIGURES_DIR = FIGURES_DIR / "data_assimilation"
PRODUCT_COMPARISON_FIGURES_DIR = FIGURES_DIR / "product_comparison"
DEMO_FIGURES_DIR = FIGURES_DIR / "demo"

# Checkpoints
CHECKPOINTS_DIR = (
    SCRATCH_ROOT / "checkpoints"
    if SCRATCH_ROOT.exists()
    else REPO_ROOT / "checkpoints"
)


def ensure_project_dirs():
    """ Create standard project directories if they don't exist """

    directories = [
        DATA_ROOT,
        RAW_DIR,
        PROCESSED_DIR,
        EXTERNAL_DIR,
        PREDICTIONS_DIR,
        EVALUATION_DIR,
        PRODUCTS_DIR,

        SATELLITE_RAW_DIR,
        CMIP6_RAW_DIR,
        INPUT4MIPS_RAW_DIR,
        SOCAT_RAW_DIR,
        ERA5_RAW_DIR,
        NOAA_RAW_DIR,

        SATELLITE_PROCESSED_DIR,
        CMIP6_PROCESSED_DIR,
        INPUT4MIPS_PROCESSED_DIR,
        SOCAT_PROCESSED_DIR,
        XGBOOST_PROCESSED_DIR,
        MODEL_PROCESSED_DIR,

        PRIOR_PREDICTIONS_DIR,
        POSTERIOR_PREDICTIONS_DIR,
        RESNET_EVALUATION_DIR,
        PRODUCT_COMPARISON_DIR,

        FIGURES_DIR,
        CMIP6_FIGURES_DIR,
        SATELLITE_FIGURES_DIR,
        SOCAT_FIGURES_DIR,
        ASSIMILATION_FIGURES_DIR,
        PRODUCT_COMPARISON_FIGURES_DIR,
        DEMO_FIGURES_DIR,

        CHECKPOINTS_DIR,
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def print_paths():
    """ Quick diagnostic for notebooks """

    print(f"DATA_ROOT: {DATA_ROOT}")
    print(f"RAW_DIR: {RAW_DIR}")
    print(f"PROCESSED_DIR: {PROCESSED_DIR}")
    print(f"PREDICTIONS_DIR: {PREDICTIONS_DIR}")
    print(f"EVALUATION_DIR: {EVALUATION_DIR}")
    print(f"PRODUCTS_DIR: {PRODUCTS_DIR}")
    print(f"FIGURES_DIR: {FIGURES_DIR}")
    print(f"CHECKPOINTS_DIR: {CHECKPOINTS_DIR}")