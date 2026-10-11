"""Validate the fresh 4-simplex Agda receipt, without launching a compiler."""
import json
from check_composable_witness_specialization import ROOT, validate

MODULE = "FourSimplexHorn"
RECEIPT = ROOT / f"research/nima/results/agda-{MODULE}.json"
RESULT = ROOT / "research/nima/results/four-simplex-horn-check.json"


def main():
    try:
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8-sig"))
        failures = validate(receipt, MODULE)
        if "fresh closure" not in validate(dict(receipt, ignore_interfaces=False), MODULE):
            failures.append("incremental-receipt negative control failed")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        failures = [f"missing or invalid receipt: {exc}"]
    result = {
        "schema": "marici.nima.four-simplex-horn-check.v1",
        "status": "pass" if not failures else "fail",
        "classification": "cubical_marked_four_simplex_outer_horn_checked" if not failures else "unverified",
        "failures": failures,
        "scope": "Outer horn completion, five tetrahedral boundary restrictions, ten shared triangles; old tetrahedral encoding bridge not proved.",
        "receipt": str(RECEIPT.relative_to(ROOT)).replace("\\", "/"),
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
