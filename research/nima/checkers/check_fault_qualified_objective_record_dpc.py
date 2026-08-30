from fractions import Fraction
import json
from pathlib import Path


def zero_matrix(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def ghz_density(sign):
    rho = zero_matrix(8)
    rho[0][0] = rho[7][7] = Fraction(1, 2)
    rho[0][7] = rho[7][0] = Fraction(sign, 2)
    return rho


def partial_trace_keep(rho, keep):
    keep = tuple(sorted(keep))
    drop = tuple(i for i in range(3) if i not in keep)
    dim = 1 << len(keep)
    out = zero_matrix(dim)
    for a in range(8):
        bits_a = ((a >> 2) & 1, (a >> 1) & 1, a & 1)
        for b in range(8):
            bits_b = ((b >> 2) & 1, (b >> 1) & 1, b & 1)
            if any(bits_a[i] != bits_b[i] for i in drop):
                continue
            ia = sum(bits_a[i] << (len(keep) - 1 - j) for j, i in enumerate(keep))
            ib = sum(bits_b[i] << (len(keep) - 1 - j) for j, i in enumerate(keep))
            out[ia][ib] += rho[a][b]
    return out


def quorum_safe(n, q, f):
    overlap = max(0, 2 * q - n)
    return overlap, overlap > f


plus = ghz_density(1)
minus = ghz_density(-1)
global_difference = [[plus[i][j] - minus[i][j] for j in range(8)] for i in range(8)]
assert any(x != 0 for row in global_difference for x in row)

proper_subsets = ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2))
proper_equal = {str(k): partial_trace_keep(plus, k) == partial_trace_keep(minus, k) for k in proper_subsets}
assert all(proper_equal.values())

unsafe_overlap, unsafe = quorum_safe(3, 2, 1)
safe_overlap, safe = quorum_safe(4, 3, 1)
assert not unsafe
assert safe

# Three identical readouts share one common-cause failure domain. Counting
# copies cannot make their failure domains independent.
failure_domains = ({"shared_sensor"}, {"shared_sensor"}, {"shared_sensor"})
independent_witnesses = all(
    failure_domains[i].isdisjoint(failure_domains[j])
    for i in range(3) for j in range(i + 1, 3)
)
assert not independent_witnesses

finite_cutoffs = tuple(range(1, 9))
lower_bounds = {n: Fraction(1, n * n) for n in finite_cutoffs}
assert all(bound > 0 for bound in lower_bounds.values())
assert lower_bounds[8] < lower_bounds[1]
# Exact hostile family: for every proposed positive uniform lower bound 1/K,
# choosing N > sqrt(K) violates it.
for k in (1, 2, 5, 17, 101):
    n = k + 1
    assert Fraction(1, n * n) < Fraction(1, k)

result = {
    "schema": "marici.fault-qualified-objective-record-dpc.v1",
    "ghz": {
        "global_states_distinct": True,
        "all_proper_marginals_equal": all(proper_equal.values()),
        "proper_subsets_checked": len(proper_subsets),
        "disposition": "descent_exists_but_is_not_separated",
    },
    "fault_model": {
        "correlated_witnesses_independent": independent_witnesses,
        "byzantine_3_2_1": {"minimum_overlap": unsafe_overlap, "safe": unsafe},
        "byzantine_4_3_1": {"minimum_overlap": safe_overlap, "safe": safe},
    },
    "completion": {
        "every_tested_cutoff_injective": True,
        "lower_bound_formula": "1/N^2",
        "uniform_positive_lower_bound": False,
    },
    "claim_boundary": "objective quotient does not imply global-state reconstruction",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "fault-qualified-objective-record-dpc.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
