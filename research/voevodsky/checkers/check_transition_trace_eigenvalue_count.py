from __future__ import annotations

import json
from fractions import Fraction


def main() -> None:
    eigenvalues = [Fraction(99,100)]*5 + [Fraction(1,2)]*2 + [Fraction(1,100)]*20
    eta = Fraction(1,10)
    count = sum(value >= eta for value in eigenvalues)
    trace = sum(eigenvalues)
    transition_trace = sum(value*(1-value) for value in eigenvalues)
    bound = trace + transition_trace/eta
    trace_only_bound = trace/eta
    assert Fraction(count) <= bound
    assert bound < trace_only_bound

    result = {
        "schema":"marici.voevodsky.transition-trace-eigenvalue-count-check.v1",
        "status":"transition_trace_count_bound_verified",
        "threshold":str(eta),
        "actual_count":count,
        "trace":str(trace),
        "transition_trace":str(transition_trace),
        "improved_count_bound":str(bound),
        "trace_only_count_bound":str(trace_only_bound),
        "identity":"N_eta <= Tr(T)+Tr(T-T^2)/eta",
        "bad_set_transition_trace_bounded":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
