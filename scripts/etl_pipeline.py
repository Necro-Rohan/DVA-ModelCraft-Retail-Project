"""Starter ETL pipeline for NST DVA Capstone 2.

This script is intentionally lightweight. Teams should adapt it to their own dataset,
but it provides a clean starting point for loading a raw CSV, standardizing columns,
and exporting a processed file for notebook and Tableau use.
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import pandas as pd

# Sensible defaults used by the project notebooks
RAW_DEFAULT = Path("data/raw/RTA_Dataset.csv")
PROCESSED_DEFAULT = Path("data/processed/RTA_cleaned.csv")

# Configure a lightweight logger for CLI visibility
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to a clean snake_case format."""
    cleaned = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    result = df.copy()
    result.columns = cleaned
    return result


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply a few safe default cleaning steps."""
    result = normalize_columns(df)
    result = result.drop_duplicates().reset_index(drop=True)

    for column in result.select_dtypes(include="object").columns:
        result[column] = result[column].astype("string").str.strip()

    return result


def build_clean_dataset(input_path: Path) -> pd.DataFrame:
    """Read a raw CSV file and return a cleaned dataframe."""
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Read with safer defaults to avoid dtype warnings on large CSVs
    try:
        df = pd.read_csv(input_path, encoding="utf-8", low_memory=False, na_values=["", "NA", "N/A"])
    except UnicodeDecodeError:
        # Fallback for differently encoded files
        df = pd.read_csv(input_path, encoding="latin-1", low_memory=False, na_values=["", "NA", "N/A"])

    return basic_clean(df)


def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    """Write the cleaned dataframe to disk, creating the parent folder if needed."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Capstone 2 starter ETL pipeline.")
    parser.add_argument(
        "--input",
        required=False,
        type=Path,
        default=RAW_DEFAULT,
        help=f"Path to the raw CSV file (default: {RAW_DEFAULT}).",
    )
    parser.add_argument(
        "--output",
        required=False,
        type=Path,
        default=PROCESSED_DEFAULT,
        help=f"Path to the cleaned CSV file (default: {PROCESSED_DEFAULT}).",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Load and print the first 5 rows of the cleaned dataset, then exit.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    logger.info("Starting ETL pipeline")
    logger.info(f"Reading raw data from: %s", args.input)
    cleaned_df = build_clean_dataset(args.input)

    if args.preview:
        logger.info("Preview mode: showing top 5 rows of cleaned data")
        print(cleaned_df.head().to_string(index=False))
        return

    save_processed(cleaned_df, args.output)
    logger.info("Processed dataset saved to: %s", args.output)
    logger.info("Rows: %d | Columns: %d", len(cleaned_df), len(cleaned_df.columns))


if __name__ == "__main__":
    main()
