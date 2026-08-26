"""Exact Kraus, probability, and back-action checks for a finite detector."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def add(*matrices):
    return [[sum(a[i][j] for a in matrices) for j in range(len(matrices[0][0]))]
            for i in range(len(matrices[0]))]


def scale(q, a):
    return [[q * value for value in row] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def apply(k, rho):
    return mm(mm(k, rho), tr(k))


def outer(v):
    return [[v[i] * v[j] for j in range(len(v))] for i in range(len(v))]


def vec(k):
    return [k[i][j] for j in range(len(k[0])) for i in range(len(k))]


def encode_matrix(a):
    return [[str(value) for value in row] for row in a]


def main():
    zero = F(0)
    one = F(1)
    k_vac = [[one, zero], [zero, zero]]
    k_click = [[zero, F(3, 5)], [zero, zero]]
    k_loss = [[zero, F(4, 5)], [zero, zero]]
    identity = [[one, zero], [zero, one]]

    completeness = add(mm(tr(k_vac), k_vac), mm(tr(k_click), k_click), mm(tr(k_loss), k_loss))
    choi_click = outer(vec(k_click))
    choi_no = add(outer(vec(k_vac)), outer(vec(k_loss)))

    rho_vac = [[one, zero], [zero, zero]]
    rho_one = [[zero, zero], [zero, one]]
    rho_plus = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
    rho_minus = [[F(1, 2), F(-1, 2)], [F(-1, 2), F(1, 2)]]

    def outcomes(rho):
        vac = apply(k_vac, rho)
        loss = apply(k_loss, rho)
        click = apply(k_click, rho)
        no_click = add(vac, loss)
        return {
            "vac": vac,
            "loss": loss,
            "click": click,
            "no_click": no_click,
            "unconditional": add(vac, loss, click),
        }

    one_out = outcomes(rho_one)
    vac_out = outcomes(rho_vac)
    plus_out = outcomes(rho_plus)
    minus_out = outcomes(rho_minus)
    vacuum_post = rho_vac

    # Gram-form Choi matrices are positive semidefinite by construction.  The
    # checker also records their nonnegative diagonal and symmetric form.
    choi_gram_certificate = (
        choi_click == tr(choi_click)
        and choi_no == tr(choi_no)
        and all(choi_click[i][i] >= 0 and choi_no[i][i] >= 0 for i in range(4))
    )

    one_click_probability = trace(one_out["click"])
    one_no_probability = trace(one_out["no_click"])
    normalized_one_click = scale(F(1, 1) / one_click_probability, one_out["click"])
    normalized_one_loss = scale(F(1, 1) / trace(one_out["loss"]), one_out["loss"])

    checks = {
        "kraus_completeness_is_exact": completeness == identity,
        "outcome_choi_matrices_have_explicit_gram_certificates": choi_gram_certificate,
        "one_photon_click_probability_is_nine_twenty_fifths": one_click_probability == F(9, 25),
        "one_photon_no_click_probability_is_sixteen_twenty_fifths": one_no_probability == F(16, 25),
        "one_photon_probabilities_normalize": one_click_probability + one_no_probability == 1,
        "vacuum_never_clicks": trace(vac_out["click"]) == 0 and trace(vac_out["no_click"]) == 1,
        "nonzero_click_and_loss_branches_end_in_vacuum": normalized_one_click == vacuum_post and normalized_one_loss == vacuum_post,
        "refined_outcomes_sum_to_coarse_unconditional_channel": one_out["unconditional"] == add(one_out["no_click"], one_out["click"]),
        "opposite_phase_states_have_same_coarse_record": (
            trace(plus_out["click"]) == trace(minus_out["click"])
            and trace(plus_out["no_click"]) == trace(minus_out["no_click"])
            and rho_plus != rho_minus
        ),
        "opposite_phase_states_have_same_unconditional_post_state": plus_out["unconditional"] == minus_out["unconditional"] == vacuum_post,
        "environment_refinement_separates_vacuum_from_loss_route": trace(vac_out["vac"]) == 1 and trace(one_out["loss"]) == F(16, 25),
    }

    result = {
        "schema": "marici.aspect.finite_lossy_photodetection_quantum_instrument.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "probabilities": {
            "one_photon": {"click": str(one_click_probability), "no_click": str(one_no_probability)},
            "vacuum": {"click": str(trace(vac_out["click"])), "no_click": str(trace(vac_out["no_click"]))},
            "plus_minus_click": str(trace(plus_out["click"])),
        },
        "certificates": {
            "kraus_completeness": encode_matrix(completeness),
            "click_choi": encode_matrix(choi_click),
            "no_click_choi": encode_matrix(choi_no),
        },
        "typed_boundary": {
            "instrument": "finite CP trace-preserving sum with destructive back-action",
            "record_kernel": "relative phase and coarse vacuum-versus-loss route",
            "completion_missing": "multiphoton, memory, dark counts, temporal continuum, and stochastic limit",
        },
    }
    out = Path(__file__).parents[1] / "results" / "finite_lossy_photodetection_quantum_instrument.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
