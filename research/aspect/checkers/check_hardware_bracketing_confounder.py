from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "hardware_bracketing_confounder.json"


def crossed(associator, hardware):
    # Logical effects are +/-A/2 and hardware effects +/-D/2.
    L1 = (associator + hardware) / 2
    R2 = -(associator + hardware) / 2
    L2 = (associator - hardware) / 2
    R1 = -(associator - hardware) / 2
    difference_12 = L1 - R2
    difference_21 = L2 - R1
    return {
        "L_on_H1": L1, "R_on_H2": R2, "L_on_H2": L2, "R_on_H1": R1,
        "difference_assignment_12": difference_12,
        "difference_assignment_21": difference_21,
        "recovered_associator": (difference_12 + difference_21) / 2,
        "recovered_hardware_phase": (difference_12 - difference_21) / 2,
    }


def strings(record):
    return {key: str(value) for key, value in record.items()}


def main():
    pure_hardware = crossed(F(0), F(3, 5))
    mixed = crossed(F(1, 5), F(3, 5))
    assert pure_hardware["difference_assignment_12"] == F(3, 5)
    assert pure_hardware["recovered_associator"] == 0
    assert pure_hardware["recovered_hardware_phase"] == F(3, 5)
    assert mixed["difference_assignment_12"] == F(4, 5)
    assert mixed["difference_assignment_21"] == F(-2, 5)
    assert mixed["recovered_associator"] == F(1, 5)
    assert mixed["recovered_hardware_phase"] == F(3, 5)

    out = {
        "schema": "marici.aspect.hardware-bracketing-confounder.v1",
        "status": "pass", "pure_hardware_hostile": strings(pure_hardware),
        "mixed_fixture": strings(mixed),
        "failure": "a fixed logical-to-hardware assignment identifies only associator plus hardware phase",
        "repair": "each physical three-body circuit must implement both logical bracketings; average opposite assignment differences to recover the associator and difference them to recover hardware phase",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
