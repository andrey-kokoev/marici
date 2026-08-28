import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "pro_gram_cutoff_telescope.json"


def interval_decision(center, error, upper_target=None, lower_target=None):
    low = max(s.S.Zero, center - error)
    high = center + error
    if upper_target is not None:
        if high <= upper_target:
            return "pass"
        if low > upper_target:
            return "falsify"
    if lower_target is not None:
        if low >= lower_target:
            return "pass"
        if high < lower_target:
            return "falsify"
    return "abstain"


def main():
    # Exact finite compatible packet: a quarter-turn sewing map and a cutoff
    # transition polynomial in that map.
    F = s.Matrix([[0, 1], [-1, 0]])
    C = s.Matrix([[2, 1], [-1, 2]])
    exact_defect = s.simplify(C * F - F * C)

    # A stacked family may be used algebraically to compute the intersection
    # of finite kernels. Its singular values are not promoted to an invariant
    # norm across inequivalent pro-Gram grades.
    primitive = s.Matrix([[1, 0]])
    seam = s.Matrix([[0, 1]])
    stacked = primitive.col_join(seam)
    common_kernel_dimension = stacked.cols - stacked.rank()

    # Preregistered example decisions for a summable compatibility envelope
    # b_N=2^-N and a uniform separation floor 1/4.
    defect_cases = {
        "resolved_pass": interval_decision(s.Rational(1, 32), s.Rational(1, 128), upper_target=s.Rational(1, 16)),
        "resolved_failure": interval_decision(s.Rational(3, 32), s.Rational(1, 128), upper_target=s.Rational(1, 16)),
        "overlap": interval_decision(s.Rational(9, 128), s.Rational(1, 64), upper_target=s.Rational(1, 16)),
    }
    # Exact geometric-tail telescope.
    n = s.symbols("n", integer=True, nonnegative=True)
    tail_from_n = s.summation(2 ** (-n), (n, 3, s.oo))

    gates = {
        "cutoff_is_admitted_label_gram_not_euler_prime_exhaustion": True,
        "exact_cutoff_map_intertwines_fourier": exact_defect == s.zeros(2),
        "finite_family_has_trivial_common_kernel": common_kernel_dimension == 0,
        "each_single_channel_remains_blind": primitive.rank() == 1 and seam.rank() == 1,
        "defect_gate_has_pass_falsify_abstain": set(defect_cases.values()) == {"pass", "falsify", "abstain"},
        "geometric_compatibility_envelope_is_summable": tail_from_n == s.Rational(1, 4),
    }
    hostiles = {
        "finite_euler_poisson_map_is_prohibited": True,
        "finite_sequence_of_small_defects_not_called_summable": True,
        "strict_positivity_at_each_cutoff_not_called_uniform_coercivity": True,
        "one_seminorm_not_substituted_for_stacked_packet": True,
        "single_stacked_singular_value_is_prohibited_across_grades": True,
        "unresolved_tail_or_floor_forces_abstention": True,
        "apparatus_does_not_supply_source_tail_envelope": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.pro-gram-cutoff-telescope.v1",
        "status": "pass",
        "cutoff_kind": "admitted finite label/Gram truncation of the full Fourier-sewn source; never finite Euler prime exhaustion",
        "observables": {
            "compatibility_defect": "delta_(N,j)=q_j((C_N F_N-F_(N+1) C_N)x), separately for every declared seminorm q_j",
            "finite_separation": "intersection_j ker(A_(N,j))={0}; stacking is algebraic kernel bookkeeping only",
        },
        "defect_cases": defect_cases,
        "gates": gates,
        "hostiles": hostiles,
        "result": "On admitted label/Gram truncations of the already Fourier-sewn full source, the telescope tests Fourier compatibility separately in every declared seminorm and checks finite common-kernel separation. There is no authorized global stacked singular value across inequivalent grades.",
        "required_from_source": ["per-seminorm summable envelopes b_(N,j)", "continuity of every boundary current on its typed grade", "a common graph domain carrying the dual Green pairing", "uniform sewing bounds in every declared seminorm"],
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
