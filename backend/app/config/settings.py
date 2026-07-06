from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "data"
RAG_DIR = PROJECT_ROOT / "rag"

DELHI_FEATURES_CSV = DATA_DIR / "delhi" / "geoai_features_100k.csv"
DELHI_PREDICTIONS_CSV = DATA_DIR / "delhi" / "city_scale_predictions.csv"

MODEL_DIR = DATA_DIR / "models"
STACKING_MODEL = MODEL_DIR / "stacking_model.pkl"
RF_MODEL = MODEL_DIR / "rf_central_model.pkl"
QGB10_MODEL = MODEL_DIR / "qgb10_model.pkl"
QGB90_MODEL = MODEL_DIR / "qgb90_model.pkl"
FEATURE_LIST = MODEL_DIR / "feature_list.pkl"

EPW_PATH = DATA_DIR / "epw" / "delhi.epw"
EMISSION_CSV = DATA_DIR / "emission_factors" / "india_grid.csv"

CHROMA_DIR = RAG_DIR / "chroma_db"
THESIS_PDF = RAG_DIR / "docs" / "thesis_multi_city.pdf"

OLLAMA_MODEL = "ollama/qwen2.5:7b"
OLLAMA_BASE_URL = "http://localhost:11434"
EMBEDDING_MODEL = "nomic-embed-text"

DELHI_GRID_EMISSION_FACTOR = 0.82
ECBC_COMMERCIAL = 150.0
BEE_RESIDENTIAL = 45.0