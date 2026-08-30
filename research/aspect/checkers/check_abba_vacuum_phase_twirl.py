from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "abba_vacuum_phase_twirl.json"


def moments(signs):
    return tuple(sum(F(s) * F(t) ** degree for t, s in enumerate(signs)) for degree in range(3))


def admissible(signs):
    m0, m1, _ = moments(signs)
    return m0 == 0 and m1 == 0


def main():
    searches = {}
    first = None
    for length in range(1, 5):
        solutions = [s for s in product((1, -1), repeat=length) if admissible(s)]
        searches[str(length)] = ["".join("+" if x == 1 else "-" for x in s) for s in solutions]
        if solutions and first is None:
            first = length

    abba = (1, -1, -1, 1)
    alternating = (1, -1, 1, -1)
    assert first == 4
    assert moments(abba) == (F(0), F(0), F(4))
    assert moments(alternating) == (F(0), F(-2), F(-6))
    assert searches["4"] == ["+--+", "-++-"]

    coupler_cross_multiplier = 2 * F(3, 5) * F(4, 5)
    curvature = F(1, 100)
    abba_signed_average_curvature = moments(abba)[2] * curvature / 4
    residual_visibility = coupler_cross_multiplier * abba_signed_average_curvature
    assert abba_signed_average_curvature == curvature
    assert residual_visibility == F(6, 625)

    out = {
        "schema": "marici.aspect.abba-vacuum-phase-twirl.v1",
        "status": "pass", "shortest_length": first,
        "solutions_at_shortest_length": searches["4"],
        "abba_moments_degrees_0_1_2": [str(x) for x in moments(abba)],
        "alternating_moments_degrees_0_1_2": [str(x) for x in moments(alternating)],
        "cancelled_exactly": ["constant coherent leakage", "linear within-block drift"],
        "quadratic_curvature_fixture": str(curvature),
        "residual_visibility_bound": str(residual_visibility),
        "conclusion": "balanced alternation cancels the mean but ABBA is the shortest binary phase twirl that also cancels linear drift",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
