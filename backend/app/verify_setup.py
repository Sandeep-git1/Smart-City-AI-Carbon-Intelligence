import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config.settings import (
    DELHI_FEATURES_CSV, DELHI_PREDICTIONS_CSV,
    STACKING_MODEL, RF_MODEL, QGB10_MODEL, QGB90_MODEL,
    FEATURE_LIST, EPW_PATH, EMISSION_CSV, THESIS_PDF
)

checks = {
    "Features CSV":     DELHI_FEATURES_CSV,
    "Predictions CSV":  DELHI_PREDICTIONS_CSV,
    "Stacking model":   STACKING_MODEL,
    "RF model":         RF_MODEL,
    "QGB10 model":      QGB10_MODEL,
    "QGB90 model":      QGB90_MODEL,
    "Feature list":     FEATURE_LIST,
    "EPW file":         EPW_PATH,
    "Emission factors": EMISSION_CSV,
    "Thesis PDF":       THESIS_PDF,
}

print("=" * 70)
print("Verifying thesis artifacts")
print("=" * 70)

all_good = True
for name, path in checks.items():
    exists = path.exists()
    size_mb = path.stat().st_size / 1e6 if exists else 0
    status = "OK  " if exists else "MISS"
    print(f"[{status}] {name:20} {size_mb:8.2f} MB   {path}")
    if not exists:
        all_good = False

print("=" * 70)
if all_good:
    print("All files present. Ready for the next step.")
else:
    print("Some files missing. Report back which ones before continuing.")