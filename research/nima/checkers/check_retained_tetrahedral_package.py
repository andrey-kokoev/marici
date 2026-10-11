"""Validate the fresh Agda receipt for retained typed boundary recovery."""
import json
from check_composable_witness_specialization import ROOT, validate

MODULE = "RetainedTetrahedralPackage"
RECEIPT = ROOT / f"research/nima/results/agda-{MODULE}.json"
RESULT = ROOT / "research/nima/results/retained-tetrahedral-package-check.json"


def main():
    try:
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8-sig"))
        failures = validate(receipt, MODULE)
        if "fresh closure" not in validate(dict(receipt, ignore_interfaces=False), MODULE):
            failures.append("incremental-receipt negative control failed")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        failures = [f"missing or invalid receipt: {exc}"]
    result = {
        "schema": "marici.nima.retained-tetrahedral-package-check.v1",
        "status": "pass" if not failures else "fail",
        "classification": "retained_path_tetrahedron_boundary_recovery_checked" if not failures else "unverified",
        "failures": failures,
        "scope": "Path-horn completion and retained boundary/type/term extraction; no arbitrary surface filler or diagonal-only recovery.",
        "receipt": str(RECEIPT.relative_to(ROOT)).replace("\\", "/"),
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
