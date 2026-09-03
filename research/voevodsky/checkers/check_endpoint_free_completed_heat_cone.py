from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    Hn, Hn1, t, h, n = sp.symbols("Hn Hn1 t h n", real=True)
    Y = sp.exp(h / 4)
    endpoint_at_n = sp.exp(t / 4) * Y**n
    endpoint_at_n1 = sp.exp(t / 4) * Y ** (n + 1)
    HRn = Hn - endpoint_at_n
    HRn1 = Hn1 - endpoint_at_n1
    remainder_difference = sp.expand(HRn - HRn1)
    endpoint_moment = sp.exp(t / 4) * (Y - 1) * Y**n
    completed_difference = Hn - Hn1
    assert sp.simplify(remainder_difference - endpoint_moment - completed_difference) == 0

    result = {
        "schema":"marici.voevodsky.endpoint-free-completed-heat-cone-check.v1",
        "status":"endpoint_subtraction_identity_verified",
        "identity":"Delta H_R(n)=Delta H(n)+c_E Y^n",
        "Y":"exp(h/4)",
        "c_E":"exp(t/4)(exp(h/4)-1)",
        "endpoint_rank_one_positive":True,
        "completed_heat_cone_rh_equivalence":"conditional_on_existing_moment_and_pole_arguments",
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
