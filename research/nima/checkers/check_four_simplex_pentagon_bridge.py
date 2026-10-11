"""Audit the independent pentagon construction and its still-conditional bridge."""
import json
from check_composable_witness_specialization import ROOT, validate

MODULES = ("MarkedFourSimplexCoherence", "FourSimplexPentagonBridge")
RESULT = ROOT / "research/nima/results/four-simplex-pentagon-bridge-check.json"


def main():
    failures = []
    for module in MODULES:
        path = ROOT / f"research/nima/results/agda-{module}.json"
        try:
            receipt = json.loads(path.read_text(encoding="utf-8-sig"))
            failures.extend(f"{module}: {f}" for f in validate(receipt, module))
            for changed, diagnostic in [
                (dict(receipt, ignore_interfaces=False), "fresh closure"),
                (dict(receipt, module="WrongModule"), "receipt module"),
            ]:
                if diagnostic not in validate(changed, module):
                    failures.append(f"{module}: negative control failed: {diagnostic}")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            failures.append(f"{module}: missing or invalid receipt: {exc}")
    result = {
        "schema": "marici.nima.four-simplex-pentagon-bridge-check.v1",
        "status": "pass" if not failures else "fail",
        "classification": "independent_pentagon_checked_comparison_coherence_open" if not failures else "unverified",
        "failures": failures,
        "scope": "Independent five-tetrahedron pentagon and unique missing-face completion; necessary and sufficient center-coherence condition for comparison with the induced equation family. Neither CenterCoherence nor the fixed-boundary comparison Goal is inhabited here.",
        "receipts": [f"research/nima/results/agda-{module}.json" for module in MODULES],
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
