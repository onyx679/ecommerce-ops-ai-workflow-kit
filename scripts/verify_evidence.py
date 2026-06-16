from pathlib import Path
import argparse
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ecom_ops.evidence import render_pretty, validate_evidence_file


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the public claim-to-evidence matrix.")
    parser.add_argument("--evidence", type=Path, default=ROOT / "EVIDENCE.md")
    args = parser.parse_args(argv)

    result = validate_evidence_file(args.evidence, ROOT)
    print(render_pretty(result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
