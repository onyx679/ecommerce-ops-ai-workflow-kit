from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ecom_ops.report import main


if __name__ == "__main__":
    raise SystemExit(main())
