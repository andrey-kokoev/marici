from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    L, W, N = sp.symbols("L W N", positive=True, real=True)
    A = W/(2*sp.pi)
    B = N/sp.pi
    t0 = sp.simplify(B/A)
    assert t0 == 2*N/W

    bound_many_bandwidths = sp.simplify(B**2 * (3 + 2*sp.log(2*L/t0)))
    expected_many = N**2/sp.pi**2 * (3 + 2*sp.log(L*W/N))
    assert sp.simplify(bound_many_bandwidths-expected_many) == 0

    bound_few_bandwidths = sp.simplify(8*L*A*B - 4*L**2*A**2)
    expected_few = (4*L*W*N-L**2*W**2)/sp.pi**2
    assert sp.simplify(bound_few_bandwidths-expected_few) == 0

    result = {
        "schema":"marici.voevodsky.component-transition-trace-bound-check.v1",
        "status":"component_sensitive_transition_trace_bound_verified",
        "kernel_bound":"min(W/(2*pi),N/(pi*abs(t)))",
        "crossing_weight":"min(2L,abs(t))",
        "bound_if_LW_ge_N":"N^2/pi^2*[3+2log(LW/N)]",
        "bound_if_LW_lt_N":"[4LWN-L^2W^2]/pi^2",
        "component_count_enclosed":False,
        "bad_set_measure_enclosed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
