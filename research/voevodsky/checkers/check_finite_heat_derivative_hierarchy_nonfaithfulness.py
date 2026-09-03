from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONTRACT = Path("research/voevodsky/finite-heat-derivative-hierarchy-nonfaithfulness-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    truncations_checked = 0
    inequalities_checked = 0
    for cutoff in range(13):
        coefficient = Fraction(3, 2 ** (cutoff + 2))
        assert coefficient > 0  # eta has a genuinely negative atom at lambda=2.
        for order in range(cutoff + 1):
            # For t>=0, exp(-t)<=1, so the bracket
            # 1-c_N*2^k*exp(-t) is bounded below by 1-c_N*2^k.
            uniform_lower_bracket = 1 - coefficient * 2**order
            assert uniform_lower_bracket >= Fraction(1, 4) > 0
            inequalities_checked += 1
        next_order_at_zero = 1 - coefficient * 2 ** (cutoff + 1)
        assert next_order_at_zero == Fraction(-1, 2)
        truncations_checked += 1

    status = contract["status"]
    assert status["finite_k_all_t_faithfulness"] == "refuted"
    assert status["full_two_index_complete_monotonicity"] == "required"
    result = {
        "schema":"marici.voevodsky.finite-heat-derivative-hierarchy-nonfaithfulness-check.v1",
        "status":"uniform_finite_order_nonfaithfulness_verified",
        "derivative_cutoffs_checked":truncations_checked,
        "all_t_inequalities_checked":inequalities_checked,
        "uniform_pass_margin":"1/4",
        "next_order_failure":"-1/2",
        "underlying_measure_positive":False,
        "finite_order_all_t_faithful":False,
        "full_two_index_domain_required":True,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
