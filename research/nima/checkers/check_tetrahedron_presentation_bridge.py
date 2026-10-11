"""Receipt audit for the fixed-boundary tetrahedron presentation bridge."""
import json
from check_composable_witness_specialization import ROOT, validate

MODULE = "TetrahedronPresentationBridge"
RECEIPT = ROOT / f"research/nima/results/agda-{MODULE}.json"
RESULT = ROOT / "research/nima/results/tetrahedron-presentation-bridge-check.json"


def main():
    try:
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8-sig"))
        failures = validate(receipt, MODULE)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        failures = [f"missing or invalid receipt: {exc}"]
    result = {
        "schema": "marici.nima.tetrahedron-presentation-bridge-check.v1",
        "status": "pass" if not failures else "fail",
        "classification": "fixed_boundary_tetrahedron_bridge_checked" if not failures else "unverified",
        "failures": failures,
        "scope": "RouteNaturality and FaceNaturality proved for the original J-based triangle comparison; FixedBoundaryTarget.Goal inhabited. No full 4-dimensional filler comparison or equality with the alternative pasting comparison claimed.",
        "receipt": str(RECEIPT.relative_to(ROOT)).replace("\\", "/"),
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
