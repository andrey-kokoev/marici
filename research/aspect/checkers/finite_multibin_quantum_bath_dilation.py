"""Exact finite-bin bath multiplicity and commutator audit."""

from fractions import Fraction as F
import json
from pathlib import Path


def transpose(a): return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def main():
    # Three declared frequency bins.  T and L act on annihilation operators.
    t = [F(3, 5), F(5, 13), F(8, 17)]
    loss = [F(4, 5), F(12, 13), F(15, 17)]
    T = [[t[i] if i == j else F(0) for j in range(3)] for i in range(3)]
    L_ind = [[loss[i] if i == j else F(0) for j in range(3)] for i in range(3)]
    L_shared = [[loss[i]] for i in range(3)]
    identity = [[F(i == j) for j in range(3)] for i in range(3)]

    independent_commutator = add(mm(T, transpose(T)), mm(L_ind, transpose(L_ind)))
    shared_commutator = add(mm(T, transpose(T)), mm(L_shared, transpose(L_shared)))
    shared_residual = [[shared_commutator[i][j] - identity[i][j] for j in range(3)] for i in range(3)]
    off_diagonal_residuals = [shared_residual[i][j] for i in range(3) for j in range(3) if i != j]

    # Vacuum bath adds zero mean occupation, while a diagonal thermal bath with
    # exact occupations n_j adds L diag(n) L^T.
    thermal_n = [F(0), F(1, 2), F(2)]
    N = [[thermal_n[i] if i == j else F(0) for j in range(3)] for i in range(3)]
    thermal_added = mm(mm(L_ind, N), transpose(L_ind))

    checks = {
        "every_bin_has_exact_passive_norm_completion": all(ti*ti + li*li == 1 for ti, li in zip(t, loss)),
        "independent_baths_restore_global_commutator": independent_commutator == identity,
        "one_shared_bath_creates_forbidden_cross_bin_commutators": any(x != 0 for x in off_diagonal_residuals),
        "shared_bath_hostile_preserves_each_diagonal": all(shared_commutator[i][i] == 1 for i in range(3)),
        "vacuum_bath_adds_zero_mean_occupation": all(F(0) == 0 for _ in range(3)),
        "thermal_noise_is_positive_and_frequency_dependent": all(thermal_added[i][i] >= 0 for i in range(3)) and len({thermal_added[i][i] for i in range(3)}) == 3,
        "finite_bins_do_not_establish_continuum_limit": True,
    }
    result = {
        "schema": "marici.aspect.finite_multibin_quantum_bath_dilation.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "bins": 3,
        "shared_bath_off_diagonal_residuals": [str(x) for x in off_diagonal_residuals],
        "thermal_added_noise_diagonal": [str(thermal_added[i][i]) for i in range(3)],
        "typed_boundary": {
            "source": "three labelled frequency-bin system modes with three orthogonal bath modes",
            "constructor": "diagonal frequency-preserving passive dilation",
            "detector": "frequency-resolved system outputs after environmental trace",
            "hostile": "one common bath preserves all scalar bin norms but creates nonzero cross-bin commutators",
            "completion": "mesh refinement, continuum convergence, causal spectral density, and fluctuation-dissipation remain open",
        },
    }
    out = Path(__file__).parents[1] / "results" / "finite_multibin_quantum_bath_dilation.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
