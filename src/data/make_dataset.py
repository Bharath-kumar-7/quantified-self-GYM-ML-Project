print("make_dataset.py started")

import pandas as pd
from glob import glob
from pathlib import Path

# --------------------------------------------------------------
# Read single CSV file
# --------------------------------------------------------------
# FIX: make paths robust (do NOT hardcode filenames)

base_dir = Path(__file__).resolve().parents[2]
data_path = base_dir / "data" / "raw" / "MetaMotion"

acc_files = glob(str(data_path / "*Accelerometer*.csv"))
gyr_files = glob(str(data_path / "*Gyroscope*.csv"))

if not acc_files or not gyr_files:
    raise FileNotFoundError("Accelerometer or Gyroscope CSV files not found")

single_file_acc = pd.read_csv(acc_files[0])
single_file_acc

single_file_gyr = pd.read_csv(gyr_files[0])
single_file_gyr

# -----------------------------------------------------------
# List all data in data/raw/MetaMotion
# --------------------------------------------------------------
# FIX: use absolute path so glob works reliably

files = glob(str(data_path / "*.csv"))
len(files)

# --------------------------------------------------------------
# Extract features from filename
# --------------------------------------------------------------
data_path = "data/raw/MetaMotion/"
f = files[0]
print(f)
participant = f.split("-")[0].replace(data_path, "")
print(participant)

if not files:
    raise FileNotFoundError("No CSV files found in MetaMotion folder")

f = files[0]
print(f)

participant = Path(f).name.split("-")[0]
print(participant)

# --------------------------------------------------------------
# Read all files
# --------------------------------------------------------------


# --------------------------------------------------------------
# Working with datetimes
# --------------------------------------------------------------


# --------------------------------------------------------------
# Turn into function
# --------------------------------------------------------------


# --------------------------------------------------------------
# Merging datasets
# --------------------------------------------------------------


# --------------------------------------------------------------
# Resample data (frequency conversion)
# --------------------------------------------------------------
# Accelerometer:    12.500HZ
# Gyroscope:        25.000Hz


# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------
