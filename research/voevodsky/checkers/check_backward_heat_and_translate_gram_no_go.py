from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONTRACT = Path("research/voevodsky/backward-heat-and-translate-gram-no-go-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    # Let r=b*exp(-tau). In the broad regime r=1/2, k(x)=1-r cos x is nonnegative.
    broad_r = Fraction(1, 2)
    broad_k0 = 1 - broad_r
    broad_kpi = 1 + broad_r
    assert broad_k0 >= 0 and broad_kpi >= 0
    broad_gram_determinant = broad_k0**2 - broad_kpi**2
    assert broad_gram_determinant == -4 * broad_r < 0

    # Backward heat decreases tau and increases r. At r=3/2, pointwise positivity fails at x=0.
    narrow_r = Fraction(3, 2)
    narrow_k0 = 1 - narrow_r
    assert narrow_k0 < 0

    # First-contact sign: Theta_t=-(4t^2)^(-1) Theta_xixi.
    t = Fraction(2, 1)
    spatial_curvature = Fraction(3, 1)
    t_derivative = -spatial_curvature / (4 * t * t)
    assert spatial_curvature >= 0 and t_derivative <= 0

    status = contract["status"]
    assert status["backward_heat_propagation"] == "refuted"
    assert status["pointwise_to_gram_promotion"] == "refuted"
    result = {
        "schema":"marici.voevodsky.backward-heat-and-translate-gram-no-go-check.v1",
        "status":"two_distinct_positivity_promotions_refuted",
        "broad_pointwise_fixture_nonnegative":True,
        "broad_two_translate_gram_determinant":str(broad_gram_determinant),
        "broad_pointwise_implies_gram":False,
        "backward_heat_narrow_value":str(narrow_k0),
        "backward_heat_preserves_pointwise_positivity":False,
        "first_contact_t_derivative":str(t_derivative),
        "all_translate_gram_verified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
