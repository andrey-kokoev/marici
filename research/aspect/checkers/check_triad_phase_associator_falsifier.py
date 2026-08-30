from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "triad_phase_associator_falsifier.json"


def gram_case(cos_triad):
    r = F(1, 2)
    pairwise_hom = r * r
    bargmann_real = r ** 3 * cos_triad
    determinant = 1 - 3 * r * r + 2 * bargmann_real
    cyclic_term = 2 * bargmann_real
    return {
        "pairwise_overlap_magnitude": str(r),
        "pairwise_HOM_visibility": str(pairwise_hom),
        "real_Bargmann_invariant": str(bargmann_real),
        "Gram_determinant": str(determinant),
        "cyclic_three_photon_term": str(cyclic_term),
        "positive_semidefinite": determinant >= 0 and 1 - r * r >= 0,
    }


def main():
    phase_zero = gram_case(F(1))
    phase_pi = gram_case(F(-1))
    assert phase_zero["pairwise_HOM_visibility"] == phase_pi["pairwise_HOM_visibility"] == "1/4"
    assert phase_zero["real_Bargmann_invariant"] == "1/8"
    assert phase_pi["real_Bargmann_invariant"] == "-1/8"
    assert phase_zero["Gram_determinant"] == "1/2"
    assert phase_pi["Gram_determinant"] == "0"
    assert phase_zero["positive_semidefinite"] and phase_pi["positive_semidefinite"]
    cyclic_difference = F(1, 4) - F(-1, 4)
    assert cyclic_difference == F(1, 2)

    out = {
        "schema": "marici.aspect.triad-phase-associator-falsifier.v1",
        "status": "pass", "phase_zero": phase_zero, "phase_pi": phase_pi,
        "cyclic_term_difference": str(cyclic_difference),
        "hostile": "all three pairwise HOM visibilities agree while the three-photon cyclic term differs by one half",
        "repair": "measure the complex Bargmann triad invariant in each bracketing route and epoch; pairwise mode matching is not an associator control",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
