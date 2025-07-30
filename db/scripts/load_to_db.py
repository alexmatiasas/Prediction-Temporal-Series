import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL, Engine
from dotenv import load_dotenv
from typing import Final
import logging
from pathlib import Path

# Basic logging configuration (INFO level and format)
logging.basicConfig(level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Constants (type-hinted and marked as Final for immutability)
CSV_PATH: Final[str] = "data/processed/final_features.csv"  # Path to your dataset
SCHEMA_FILE_PATH: Final[str] = "db/sql-queries/db-schema.sql"  # SQL schema file
CHUNK_SIZE: Final[int] = 5000  # Optimal chunk size for batch processing

# Environment variables with default values
DB_USER: Final[str] = os.getenv("SUPABASE_USER", "postgres")
DB_PASSWORD: Final[str] = os.getenv("SUPABASE_PASSWORD", "")
DB_HOST: Final[str] = os.getenv("SUPABASE_HOST", "")
DB_PORT: Final[int] = int(os.getenv("SUPABASE_PORT", "5432"))  # Ensure integer type
DB_NAME: Final[str] = os.getenv("SUPABASE_NAME", "postgres")


def validate_environment() -> None:
    """Validates that required environment variables are set."""
    required_vars = {"SUPABASE_HOST": DB_HOST, "SUPABASE_PASSWORD": DB_PASSWORD}

    missing_vars = [var for var, val in required_vars.items() if not val]
    if missing_vars:
        logger.error(
            "❌ Missing required environment variables: %s", ", ".join(missing_vars)
        )
        exit(1)


def get_engine() -> Engine:
    """Creates and returns a SQLAlchemy database engine configured for Supabase."""
    try:
        url = URL.create(
            drivername="postgresql+psycopg2",
            username=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            query={"sslmode": "require"},  # Enforces SSL encryption
        )
        logger.info("🔌 Connecting to database at host: %s", DB_HOST)
        return create_engine(url, echo=False, pool_pre_ping=True)
    except Exception as e:
        logger.error("❌ Failed to create database engine: %s", str(e))
        exit(1)


def setup_database(engine: Engine) -> None:
    """Executes the SQL schema file to create database structure."""
    try:
        schema_sql = Path(SCHEMA_FILE_PATH).read_text(encoding="utf-8")
        with engine.begin() as conn:
            conn.execute(text(schema_sql))
        logger.info("✅ Database schema loaded successfully")
    except Exception as e:
        logger.error("❌ Failed to load database schema: %s", str(e))
        raise


def load_data(engine: Engine) -> None:
    """Loads data from CSV into the database in optimized chunks."""
    try:
        df = pd.read_csv(CSV_PATH)

        # TODO: validate that required columns exist in the CSV

        if "datetime" in df.columns:
            df["datetime"] = pd.to_datetime(df["datetime"], utc=True)
            # TODO: assert datetime column has timezone-aware dtype (e.g., datetime64[ns, UTC])

        total_rows = len(df)
        logger.info("📊 Total rows to load: %d", total_rows)

        for i in range(0, total_rows, CHUNK_SIZE):
            chunk = df.iloc[i : i + CHUNK_SIZE]
            with engine.begin() as conn:
                chunk.to_sql(
                    name="energy_features",
                    con=conn,
                    schema="energy",
                    if_exists="append",
                    index=False,
                    method="multi",
                )
            logger.info("✅ Loaded chunk %d-%d of %d", i, i + len(chunk), total_rows)

    except Exception as e:
        logger.error("❌ Failed to load data: %s", str(e))
        raise


def main() -> None:
    """Main execution flow for schema setup and data loading."""
    validate_environment()

    engine = get_engine()
    try:
        logger.info("🛠 Setting up database schema...")
        setup_database(engine)

        # TODO: validate that table energy.energy_features exists before truncating

        logger.info("🔄 Truncating existing data...")
        with engine.begin() as conn:
            conn.execute(
                text("TRUNCATE TABLE energy.energy_features CONTINUE IDENTITY;")
            )

        logger.info("📤 Loading data...")
        load_data(engine)

        logger.info("🎉 Data load completed successfully!")
    finally:
        engine.dispose()  # Proper connection cleanup


if __name__ == "__main__":
    main()
