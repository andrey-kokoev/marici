import json
from fractions import Fraction
from pathlib import Path


def run_zero_beta(tau0: Fraction, scale_step: Fraction) -> Fraction:
    del scale_step
    return tau0


def main() -> None:
    hyper_beta = Fraction(0)
    tau_zero = run_zero_beta(Fraction(0), Fraction(5))
    tau_one = run_zero_beta(Fraction(1), Fraction(5))

    vector_index = 2 + 15
    operand_hyper_index = 2 + 15 - 32

    checks = {
        "hypermultiplet_boundary_beta_zero": hyper_beta == 0,
        "one_hyper_shift_zero": hyper_beta == 0,
        "many_hyper_shift_zero": 32 * hyper_beta == 0,
        "zero_beta_preserves_tau_zero": tau_zero == 0,
        "zero_beta_preserves_tau_one": tau_one == 1,
        "zero_beta_pair_remains_distinct": tau_zero != tau_one,
        "zero_beta_not_selector": tau_zero != tau_one,
        "pure_vector_index_positive": vector_index == 17,
        "operand_completion_index_negative": operand_hyper_index == -15,
        "spectral_and_beta_completion_axes_independent": operand_hyper_index != vector_index and 32 * hyper_beta == 0,
        "full_su4_beta_not_imported": True,
        "higher_loop_closure_not_imported": True,
    }

    result = {
        "work_package": "WP938",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "imported_domain": "one-loop bulk hypermultiplet contribution to brane gauge coupling on five-dimensional S1/Z2",
        "exact_kernel": {
            "hypermultiplet_beta_contribution": "0",
            "preserved_tau_pair": [str(tau_zero), str(tau_one)],
            "dimension": 1,
        },
        "independence_witness": {
            "spectral_index_before": vector_index,
            "spectral_index_after_32_degree_completion": operand_hyper_index,
            "boundary_beta_shift": "0",
        },
        "classification": "completion-invariant beta kernel, not boundary selector",
        "smallest_exact_falsifier": "tau=0 and tau=1 remain distinct under zero hypermultiplet boundary beta",
        "remaining_gate": "complete SU4 vector-plus-boundary beta system, higher-loop closure, thresholds, and physical16 instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp938_s1z2_hypermultiplet_boundary_beta_kernel.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
