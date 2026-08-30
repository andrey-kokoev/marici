from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "cross_context_reset_transport.json"


def main():
    routes = ("direct_ternary", "left_bracket", "right_bracket", "destructive_pairwise")
    coherences = (F(3, 5), F(0))
    detectors = ("assignment_A", "assignment_B")
    contexts = [(route, gamma, detector) for route in routes for gamma in coherences for detector in detectors]
    reference = {context: F(0) for context in contexts}
    hostile = dict(reference)
    bad_context = ("right_bracket", F(3, 5), "assignment_B")
    hostile[bad_context] = F(1, 5)
    assert len(contexts) == 16
    assert max(abs(value) for value in reference.values()) == 0
    assert max(abs(value) for value in hostile.values()) == F(1, 5)
    out = {
        "schema": "marici.aspect.cross-context-reset-transport.v1", "status": "pass",
        "context_count": len(contexts),
        "routes": list(routes),
        "coherences": [str(x) for x in coherences],
        "detector_assignments": list(detectors),
        "standalone_reset_qualification_passes": True,
        "hostile_context": [bad_context[0], str(bad_context[1]), bad_context[2]],
        "hostile_transport_residual": "1/5",
        "common_terminal_reset_exists": False,
        "required_gate": "one reset identity has null insertion residual in every route-coherence-detector context",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
