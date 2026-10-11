"""Audit the induced equation-family four-cell bridge, not a pentagon claim."""
import json
from check_composable_witness_specialization import ROOT, validate

MODULE = "FourSimplexEquationBridge"
RECEIPT = ROOT / f"research/nima/results/agda-{MODULE}.json"
RESULT = ROOT / "research/nima/results/four-simplex-equation-bridge-check.json"


def main():
    try:
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8-sig"))
        failures = validate(receipt, MODULE)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        failures = [f"missing or invalid receipt: {exc}"]
    result = {
        "schema": "marici.nima.four-simplex-equation-bridge-check.v1",
        "status": "pass" if not failures else "fail",
        "classification": "induced_equation_family_fourcell_bridge_checked" if not failures else "unverified",
        "failures": failures,
        "scope": "Fixed-five-tetrahedron four-cell equivalence to an induced equation-family presentation; full package inverse laws and boundary square. Equality with an independently defined pentagon relation is not claimed.",
        "receipt": str(RECEIPT.relative_to(ROOT)).replace("\\", "/"),
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
