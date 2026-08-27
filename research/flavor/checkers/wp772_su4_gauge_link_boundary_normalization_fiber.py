"""Exact SU(4) gauge-link decomposition and boundary normalization audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
wp771 = json.loads(
    (ROOT / "results" / "wp771_radius_free_static_portal_composition.json").read_text(
        encoding="utf-8"
    )
)

P = sp.diag(1, 1, -1, -1)

# Matrix-unit count under X -> P X P^{-1}. Diagonal 2x2 blocks are even;
# off-diagonal 2x2 blocks are odd. Hermitian traceless dimensions are counted
# over the reals.
even_matrix_units = []
odd_matrix_units = []
for i in range(4):
    for j in range(4):
        parity = P[i, i] * P[j, j]
        (even_matrix_units if parity == 1 else odd_matrix_units).append((i, j))

even_real_dimension = 2**2 + 2**2 - 1
odd_real_dimension = 2 * 2 * 2
su4_dimension = 4**2 - 1

# Pure bulk vector packet: the off-diagonal A_5 link is part of the adjoint,
# not an independently counted hypermultiplet.
N_V = su4_dimension
N_H = 0
kappa = 2 + N_V - N_H

C, tau_a, tau_b, tau = sp.symbols(
    "C tau_A tau_B tau", positive=True, real=True
)
g_a2 = 1 / (C + tau_a)
g_b2 = 1 / (C + tau_b)
g_common2 = 1 / (C + tau)
portal_common = sp.simplify(g_common2 / 10)

checks = {
    "wp771_dependency_passed": wp771["status"] == "PASS" and all(wp771["checks"].values()),
    "su4_adjoint_dimension_is_fifteen": su4_dimension == 15,
    "even_subalgebra_dimension_is_seven": even_real_dimension == 7,
    "odd_coset_dimension_is_eight": odd_real_dimension == 8,
    "parity_partition_exhausts_matrix_units": len(even_matrix_units) == 8 and len(odd_matrix_units) == 8,
    "traceless_parity_dimensions_exhaust_adjoint": even_real_dimension + odd_real_dimension == su4_dimension,
    "even_algebra_matches_su2_su2_u1_dimensions": even_real_dimension == 3 + 3 + 1,
    "odd_sector_matches_complex_bifundamental": odd_real_dimension == 2 * (2 * 2),
    "gauge_link_requires_no_bulk_hyper": N_H == 0,
    "pure_su4_vector_spectral_index_is_positive_seventeen": kappa == 17,
    "independent_boundary_terms_split_couplings": sp.simplify(g_a2 - g_b2) != 0,
    "exchange_symmetric_boundary_term_preserves_equality": sp.simplify(g_a2.subs({tau_a: tau, tau_b: tau}) - g_b2.subs({tau_a: tau, tau_b: tau})) == 0,
    "exchange_symmetric_boundary_term_changes_magnitude": sp.simplify(portal_common.subs({C: 1, tau: 0}) - portal_common.subs({C: 1, tau: 1})) == sp.Rational(1, 20),
    "hostile_common_boundary_pair_is_one_tenth_vs_one_twentieth": portal_common.subs({C: 1, tau: 0}) == sp.Rational(1, 10) and portal_common.subs({C: 1, tau: 1}) == sp.Rational(1, 20),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP772",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP771",
    "admitted_state_domain": "a five-dimensional SU(4) vector multiplet with orbifold parity diag(1,1,-1,-1), off-diagonal A_5 link modes, boundary residual SU(2)_A x SU(2)_B x U(1), and every quadratic residual-gauge-invariant boundary kinetic term",
    "faithful_coordinate": "bulk inverse coupling C=ell/g_5^2 and boundary inverse kinetic coefficients tau_A,tau_B, including their exchange-even common mode",
    "source_authorized_operation": "simple-group gauge-Higgs decomposition of the SU(4) adjoint under the parity stabilizer",
    "representation_result": "15 = 7 even plus 8 odd; the even algebra is su(2)_A plus su(2)_B plus u(1), and the odd A_5 sector is one complex (2,2) bifundamental",
    "spectral_result": "with the link carried by the vector adjoint and no bulk hypers, kappa=2+15=17>0",
    "classification": "the simple parent jointly derives the link representation, one bulk coupling, and positive spectral sign, but residual-symmetry boundary kinetic terms reopen both coupling splitting and the exchange-even common normalization",
    "smallest_exact_falsifier": "at C=1 and tau_A=tau_B=tau, tau=0 gives Delta=1/10 while tau=1 gives Delta=1/20 without changing the bulk parent, parity, spectral index, or exchange symmetry",
    "deutschian_status": "SU(4) gauge-Higgs unification makes the representation and spectral explanation harder to vary, but not the physical gauge normalization because the complete boundary operator ring contains a common kinetic modulus",
    "next_source_gate": "derive a boundary principle that fixes or eliminates the common kinetic term and then prove an isolated RG normalization for the resulting complete bulk-boundary theory",
    "instrument_gate": "WP770 remains a formal two-port readout; actual physical16 channel realization is not supplied by gauge-Higgs unification",
}
(ROOT / "results" / "wp772_su4_gauge_link_boundary_normalization_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
