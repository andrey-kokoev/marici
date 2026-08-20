"""Exact Griffiths--Dwork certificate for the equation-(58) nine-master sector.

This checker freezes arXiv:2408.16386v2 and the normalization used in ledger
entries 149, 150, 152, 155, and the Benincasa entry 161.  It works at d=3 on
the printed homogeneous slice

    X1 = rho*lambda,  X2 = lambda,  X3 = 1.

The q_G12 coordinate is q=y12+E, with no inserted factor of two.  Taking the
q=0 residue gives six K^(-1/2) forms and three literal double-pole residues
-P*K1/(2*K^(3/2)).  Every connection row is solved modulo exact forms and is
then checked as a cleared polynomial identity in (a,b,rho,lambda).

The output deliberately distinguishes this absolute residue connection from
the source-underdetermined log/relative connection and physical chain.

Dependency: sympy==1.14.0 (see requirements-griffiths-dwork.txt).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations
from pathlib import Path

try:
    import sympy as sp
except ModuleNotFoundError as error:  # pragma: no cover - environment guard
    raise SystemExit(
        "SymPy is required; install research/benincasa/"
        "requirements-griffiths-dwork.txt"
    ) from error


SCHEMA = "marici.benincasa.nine-master-gd.v1"
SOURCE_HASHES = {
    "temp/arxiv-2408.16386-source.tar": (
        "7f165dc14c4243a88dbca9185f136c37b4a6af5b540247b6292d4086440aaf9f"
    ),
    "temp/arxiv-2408.16386-source/sections/applications.tex": (
        "3e92460fe2e34dc21a537c784dab3b2fbcd9b7cfee9e7372f06971b50d8b6f9b"
    ),
    "src/ledger/20260815-149 Polarized Binary-Quartic Embedding and Rank-One Extension Problem.md": (
        "2aa6cbdBC59ea26a0baa8b69412ab73b82ffb26ab1a69f31a59dee9ca2ec2881".lower()
    ),
    "src/ledger/20260815-150 Explicit Infinity-Gysin Projection and the Rank-Seven Algebraic Kernel.md": (
        "ea96a85a3dfe3981b3e0a0423cd8e83df64c71688b43ea6d7a2d5b64d4af7efb"
    ),
    "src/ledger/20260815-152 Deutsch-Popperian Algebraic-Kernel Flat-Lift Conjecture.md": (
        "b5ab61aba1ecc6e31f542014bf6ba3239d20b5aea5807af58a2a22925c6302a5"
    ),
    "src/ledger/20260815-155 Absolute Q-Smoothness Falsifies the M2.25 Sign Line.md": (
        "216c5e48e4adf527f52807d79a0bd0ab91dac5c496984476a92b017ed20cd6d1"
    ),
    "src/ledger/20260815-161 Marked-Residue Surface Typing and the Missing Q Projection.md": (
        "f0d852e70fed771178c6ca3f9be348cefab16139777f207804c44585cad234af"
    ),
}


# a,b are the residue-surface coordinates y23,y31.  rho is the fixed X1/X2
# ratio; lambda is the only moving homogeneous-slice coordinate.
a, b, rho, lam = sp.symbols("a b rho lambda")
x = rho * lam
y = lam
z = sp.Integer(1)
E = x + y + z
h = x**2 + y**2 - z**2

A_ell = (x - y) ** 2 - z**2
B_ell = (x + y) ** 2 - z**2
C_mark = E**2 - x * y
D_mark = E**2 + x * y

F = x**2 * a**4 - h * a**2 * b**2 + y**2 * b**4
G_a = h * (x**2 + E**2) - 2 * x**2 * (y**2 + E**2)
G_b = h * (y**2 + E**2) - 2 * y**2 * (x**2 + E**2)
H = z**2 * ((E**2 - y**2) * (E**2 - x**2) + E**2 * z**2)
K = sp.expand(F + G_a * a**2 + G_b * b**2 + H)

# K1=dK_general/dq at q=0, where y12=q-E.  This is the numerator forced by
# the literal residue of dq/q^2 * K(q)^(-1/2).
K1 = sp.expand(
    2 * E * (x**2 - y**2 + z**2) * a**2
    + 2 * E * (y**2 - x**2 + z**2) * b**2
    - 2 * E * z**2 * (2 * E**2 - x**2 - y**2 + z**2)
)

K_a = sp.diff(K, a)
K_b = sp.diff(K, b)
K_lam = sp.diff(K, lam)


# A basis item is stored as its numerator and its K exponent.  These are
# exactly the residues of equation (58), not a post-hoc gauge rotation.
BASIS = [
    (a * b, sp.Rational(1, 2)),
    (a, sp.Rational(1, 2)),
    (-a * K1 / 2, sp.Rational(3, 2)),
    (b, sp.Rational(1, 2)),
    (-b * K1 / 2, sp.Rational(3, 2)),
    (-K1 / 2, sp.Rational(3, 2)),
    (sp.Integer(1), sp.Rational(1, 2)),
    (a**2, sp.Rational(1, 2)),
    (b**2, sp.Rational(1, 2)),
]

BLOCKS = {
    "odd_odd": [0],
    "odd_even": [1, 2],
    "even_odd": [3, 4],
    "even_even": [5, 6, 7, 8],
}
PARITIES = {
    "odd_odd": (1, 1),
    "odd_even": (1, 0),
    "even_odd": (0, 1),
    "even_even": (0, 0),
}
TARGET_CONFIG = {
    0: ("odd_odd", 0, 3),
    1: ("odd_even", 0, 3),
    2: ("odd_even", 4, 2),
    3: ("even_odd", 0, 3),
    4: ("even_odd", 4, 2),
    5: ("even_even", 5, 3),
    6: ("even_even", 0, 3),
    7: ("even_even", 0, 3),
    8: ("even_even", 0, 3),
}


def canonical(expression):
    return sp.cancel(expression)


def expression_record(expression):
    expression = canonical(expression)
    numerator, denominator = expression.as_numer_denom()
    return {
        "factor": sp.sstr(sp.factor(expression)),
        "numerator": sp.sstr(sp.factor(numerator)),
        "denominator": sp.sstr(sp.factor(denominator)),
    }


def monomials(max_degree, parity):
    answer = []
    for degree_a in range(max_degree + 1):
        for degree_b in range(max_degree + 1 - degree_a):
            if degree_a % 2 == parity[0] and degree_b % 2 == parity[1]:
                answer.append(a**degree_a * b**degree_b)
    return answer


def vector_field(prefix, max_degree, target_parity):
    parity_a, parity_b = target_parity
    monomials_a = monomials(max_degree, (1 - parity_a, parity_b))
    monomials_b = monomials(max_degree, (parity_a, 1 - parity_b))
    coefficients_a = sp.symbols(f"{prefix}_a0:{len(monomials_a)}")
    coefficients_b = sp.symbols(f"{prefix}_b0:{len(monomials_b)}")
    field_a = sum(
        (coefficient * monomial for coefficient, monomial in zip(coefficients_a, monomials_a)),
        sp.Integer(0),
    )
    field_b = sum(
        (coefficient * monomial for coefficient, monomial in zip(coefficients_b, monomials_b)),
        sp.Integer(0),
    )
    return field_a, field_b, list(coefficients_a) + list(coefficients_b)


def exact_numerator(field_a, field_b, exponent):
    """Numerator of d((-V_b da+V_a db)/K^exponent), one K cleared."""

    return sp.expand(
        (sp.diff(field_a, a) + sp.diff(field_b, b)) * K
        - exponent * (field_a * K_a + field_b * K_b)
    )


def derivative_numerators(target):
    """Return pole-5/2 and pole-3/2 numerators of d/dlambda(e_target)."""

    numerator, exponent = BASIS[target]
    if exponent == sp.Rational(1, 2):
        return sp.Integer(0), sp.expand(-numerator * K_lam / 2)
    assert exponent == sp.Rational(3, 2)
    return (
        sp.expand(-sp.Rational(3, 2) * numerator * K_lam),
        sp.expand(sp.diff(numerator, lam)),
    )


def solve_reduction(target):
    block_name, degree_u, degree_v = TARGET_CONFIG[target]
    block_indices = BLOCKS[block_name]
    target_parity = PARITIES[block_name]
    connection_symbols = sp.symbols(f"c_{target + 1}_0:{len(block_indices)}")
    field_v_a, field_v_b, v_symbols = vector_field(
        f"v_{target + 1}", degree_v, target_parity
    )
    pole_five, pole_three = derivative_numerators(target)

    if BASIS[target][1] == sp.Rational(1, 2):
        field_u_a = field_u_b = sp.Integer(0)
        u_symbols = []
        left = pole_three
        for coefficient, basis_index in zip(connection_symbols, block_indices):
            basis_numerator, basis_exponent = BASIS[basis_index]
            if basis_exponent == sp.Rational(1, 2):
                left -= coefficient * basis_numerator * K
            else:
                left -= coefficient * basis_numerator
        right = exact_numerator(field_v_a, field_v_b, sp.Rational(1, 2))
        cleared_pole = "K^(3/2)"
    else:
        field_u_a, field_u_b, u_symbols = vector_field(
            f"u_{target + 1}", degree_u, target_parity
        )
        left = pole_five + pole_three * K
        for coefficient, basis_index in zip(connection_symbols, block_indices):
            basis_numerator, basis_exponent = BASIS[basis_index]
            if basis_exponent == sp.Rational(1, 2):
                left -= coefficient * basis_numerator * K**2
            else:
                left -= coefficient * basis_numerator * K
        right = exact_numerator(field_u_a, field_u_b, sp.Rational(3, 2))
        right += exact_numerator(field_v_a, field_v_b, sp.Rational(1, 2)) * K
        cleared_pole = "K^(5/2)"

    identity = sp.Poly(sp.expand(left - right), a, b)
    equations = [coefficient for _, coefficient in identity.terms()]
    unknowns = list(connection_symbols) + u_symbols + v_symbols
    matrix, vector = sp.linear_eq_to_matrix(equations, unknowns)
    solution_set = sp.linsolve((matrix, vector), unknowns)
    if solution_set is sp.EmptySet:
        raise AssertionError(f"no reduction for e{target + 1}")
    solution_tuple = next(iter(solution_set))

    # linsolve uses some original unknowns as free parameters.  Setting only
    # those certificate-gauge parameters to zero selects a deterministic
    # primitive; it cannot affect the unique cohomology coefficients.
    parameter_symbols = set().union(
        *(expression.free_symbols for expression in solution_tuple)
    ) - {rho, lam}
    zero_parameters = {symbol: 0 for symbol in parameter_symbols}
    chosen = [canonical(expression.subs(zero_parameters)) for expression in solution_tuple]
    substitution = dict(zip(unknowns, chosen))

    connection_local = chosen[: len(connection_symbols)]
    if any(expression.free_symbols - {rho, lam} for expression in connection_local):
        raise AssertionError(f"nonunique connection coefficient for e{target + 1}")

    # This is the requested fail-closed verification: every coefficient of
    # the cleared polynomial identity is reduced to a rational function of
    # (rho,lambda), its denominator is cleared, and its numerator must be the
    # zero polynomial.  No numerical sampling is used here.
    cleared_checks = []
    for monomial, coefficient in identity.terms():
        residual = sp.together(
            coefficient.subs(substitution, simultaneous=True)
        )
        residual_numerator, residual_denominator = residual.as_numer_denom()
        residual_numerator = sp.Poly(sp.expand(residual_numerator), rho, lam)
        if not residual_numerator.is_zero:
            raise AssertionError(
                f"cleared identity failed for e{target + 1}, monomial {monomial}"
            )
        cleared_checks.append(
            {
                "a_b_exponents": list(monomial),
                "clearing_denominator": sp.sstr(sp.factor(residual_denominator)),
                "cleared_numerator_terms": 0,
            }
        )

    primitive = {
        "U_a": canonical(field_u_a.subs(substitution, simultaneous=True)),
        "U_b": canonical(field_u_b.subs(substitution, simultaneous=True)),
        "V_a": canonical(field_v_a.subs(substitution, simultaneous=True)),
        "V_b": canonical(field_v_b.subs(substitution, simultaneous=True)),
    }
    primitive_text = "\n".join(
        f"{name}={sp.sstr(value)}" for name, value in primitive.items()
    )
    primitive_digest = hashlib.sha256(primitive_text.encode("utf-8")).hexdigest()

    full_row = [sp.Integer(0)] * 9
    for coefficient, basis_index in zip(connection_local, block_indices):
        full_row[basis_index] = canonical(coefficient)

    return full_row, {
        "target": f"e{target + 1}",
        "block": block_name,
        "input_pole_order": str(BASIS[target][1]),
        "cleared_to": cleared_pole,
        "ansatz_degrees": {"U": degree_u, "V": degree_v},
        "linear_equations": matrix.rows,
        "linear_unknowns": matrix.cols,
        "certificate_gauge_parameters_set_to_zero": len(parameter_symbols),
        "coefficient_identities": cleared_checks,
        "all_cleared_numerators_zero": True,
        "primitive_sha256": primitive_digest,
        "primitive": {
            name: sp.sstr(value) for name, value in primitive.items()
        },
    }


def derive_connection():
    rows = []
    certificates = []
    for target in range(9):
        row, certificate = solve_reduction(target)
        rows.append(row)
        certificates.append(certificate)
    matrix = sp.Matrix(rows)

    expected_sparse = {
        (0, 0): (rho + 1) / E,
        (1, 2): 1 / lam,
        (2, 2): -1 / lam,
        (3, 4): 1 / lam,
        (4, 4): -1 / lam,
    }
    for (row, column), expected in expected_sparse.items():
        assert sp.factor(matrix[row, column] - expected) == 0
    for row in range(5):
        for column in range(9):
            if (row, column) not in expected_sparse:
                assert matrix[row, column] == 0
    return matrix, certificates


def final_block_checks(matrix):
    final = matrix[5:9, 5:9]
    assert sp.factor(final[0, 0] + sp.diff(H, lam) / (2 * H)) == 0
    assert all(final[0, column] == 0 for column in range(1, 4))

    coefficient_7 = sp.expand((x**2 - y**2) * (x**2 * y**2 - E**4))
    coefficient_8 = sp.expand(2 * x**2 * (E**2 + y**2))
    coefficient_9 = sp.expand(-2 * y**2 * (E**2 + x**2))
    kernel_vector = sp.Matrix([[0, coefficient_7, coefficient_8, coefficient_9]])
    transported = (
        kernel_vector.applyfunc(lambda entry: sp.diff(entry, lam))
        + kernel_vector * final
    ).applyfunc(canonical)
    kappa = canonical(transported[0, 1] / coefficient_7)
    mu = canonical(transported[0, 0])
    assert sp.factor(kappa - sp.diff(C_mark * D_mark, lam) / (C_mark * D_mark)) == 0
    assert sp.factor(transported[0, 2] - kappa * coefficient_8) == 0
    assert sp.factor(transported[0, 3] - kappa * coefficient_9) == 0

    # Entry-150 infinity-Gysin matrix, now checked as a horizontal quotient.
    gysin = sp.Matrix(
        [
            [0, 0],
            [1, 0],
            [(E**2 + y**2) / 2, -(E**2 + x**2) / 2],
            [
                (E**2 + x**2) / 2,
                -x**2 * (E**2 + y**2) / (2 * y**2),
            ],
        ]
    )
    rhs = final * gysin - gysin.applyfunc(lambda entry: sp.diff(entry, lam))
    selected = gysin[1:3, :]
    quotient = (selected.inv() * rhs[1:3, :]).applyfunc(canonical)
    compatibility = (gysin * quotient - rhs).applyfunc(sp.factor)
    assert compatibility == sp.zeros(4, 2)

    g00, g01, g10, g11 = (
        quotient[0, 0],
        quotient[0, 1],
        quotient[1, 0],
        quotient[1, 1],
    )
    second_derivative_f = sp.diff(g00, lam) + g00**2 + g01 * g10
    second_derivative_g = g00 * g01 + sp.diff(g01, lam) + g01 * g11
    pf_p = canonical(-second_derivative_g / g01)
    pf_q = canonical(
        -(second_derivative_f - second_derivative_g * g00 / g01)
    )
    published_p = canonical(
        (5 * A_ell * B_ell + 2 * (A_ell + B_ell))
        / (lam * A_ell * B_ell)
    )
    published_q = canonical(
        (3 * (rho**2 - 1) ** 2 * lam**2 - 2 * (rho**2 + 1))
        / (A_ell * B_ell)
    )
    assert sp.factor(pf_p - published_p) == 0
    assert sp.factor(pf_q - published_q) == 0

    return {
        "basis": ["e6", "e7", "e8", "e9"],
        "matrix": [
            [expression_record(final[row, column]) for column in range(4)]
            for row in range(4)
        ],
        "e6_line": {
            "connection": expression_record(final[0, 0]),
            "identity": "conn(e6) = -(1/2) d_lambda log(H)",
            "H": sp.sstr(sp.factor(H)),
        },
        "entry_150_kernel_vector": {
            "coefficients_in_e6_e7_e8_e9": [
                "0",
                sp.sstr(sp.factor(coefficient_7)),
                sp.sstr(sp.factor(coefficient_8)),
                sp.sstr(sp.factor(coefficient_9)),
            ],
            "transport": "d(v_alg) = mu*e6 + kappa*v_alg",
            "kappa": expression_record(kappa),
            "kappa_identity": "kappa = d_lambda log((E^2-x*y)*(E^2+x*y))",
            "mu": expression_record(mu),
            "rationally_normalized_quotient_line": (
                "v_alg/((E^2-x*y)*(E^2+x*y)) has zero diagonal connection modulo e6"
            ),
        },
        "infinity_gysin": {
            "matrix_rows_e6_e7_e8_e9_to_omega0_omega2": [
                [expression_record(gysin[row, column]) for column in range(2)]
                for row in range(4)
            ],
            "horizontal_compatibility_residual": [["0", "0"]] * 4,
            "elliptic_quotient_connection": [
                [expression_record(quotient[row, column]) for column in range(2)]
                for row in range(2)
            ],
            "printed_L2": {
                "p": expression_record(pf_p),
                "q": expression_record(pf_q),
                "matches_equation_59": True,
            },
        },
    }


def q_zero_checks(matrix, final_report):
    Q = sp.expand(4 * A_ell * B_ell - (A_ell + B_ell - E**2) ** 2)
    allowed_pole_product = sp.expand(
        lam * E * A_ell * B_ell * C_mark * D_mark * H
    )
    denominators = []
    for expression in matrix:
        denominator = canonical(expression).as_numer_denom()[1]
        if denominator != 1:
            quotient_denominator = canonical(allowed_pole_product / denominator).as_numer_denom()[1]
            assert sp.Poly(quotient_denominator, rho, lam).total_degree() == 0
            denominators.append(sp.factor(denominator))

    q_gcd = sp.gcd(sp.Poly(Q, rho, lam), sp.Poly(allowed_pole_product, rho, lam))
    assert q_gcd.total_degree() == 0

    q_slice = sp.Poly(sp.expand(Q.subs(rho, 2)), lam)
    q_slice_expected = sp.Poly(
        35 * lam**4 + 12 * lam**3 - 70 * lam**2 - 36 * lam - 5,
        lam,
    )
    assert q_slice == q_slice_expected
    resultant = sp.resultant(q_slice.as_expr(), sp.diff(q_slice.as_expr(), lam), lam)
    # The conventional resultant retains the leading-coefficient factor -7.
    # Entry 161's custom certificate reports its positive primitive part.
    assert resultant == -(2**24) * 5 * 7 * 283
    primitive_resultant = abs(resultant) // 7
    assert primitive_resultant == 2**24 * 5 * 283

    # The matrix is holomorphic at the generic point of Q=0.  Pullback to a
    # transverse parameter t=Q therefore has zero logarithmic residue.
    zero_residue = [["0" for _ in range(9)] for _ in range(9)]
    return {
        "Q": sp.sstr(sp.factor(Q)),
        "allowed_connection_pole_product": sp.sstr(sp.factor(allowed_pole_product)),
        "every_matrix_denominator_divides_allowed_product": True,
        "gcd_Q_with_allowed_pole_product": sp.sstr(q_gcd.as_expr()),
        "rho_2_transverse_slice": {
            "Q": sp.sstr(q_slice.as_expr()),
            "resultant_Q_dQ": str(resultant),
            "primitive_absolute_resultant": str(primitive_resultant),
            "simple_real_root_interval": [1, 2],
        },
        "absolute_residue_at_generic_Q0": zero_residue,
        "absolute_local_monodromy_at_generic_Q0": "I_9",
        "algebraic_kernel_Q_behavior": {
            "e6_line": "holomorphic at generic Q=0 because gcd(Q,H)=1",
            "v_alg_mod_e6": (
                "holomorphic and rationally trivial at generic Q=0 because "
                "gcd(Q,(E^2-x*y)*(E^2+x*y))=1"
            ),
            "off_diagonal_extension": (
                "mu is holomorphic at generic Q=0; no Q-supported residue"
            ),
        },
        "scope": "absolute equation-(58) q_G12 residue connection only",
    }


def proportional(left, right):
    return sp.Matrix(left).cross(sp.Matrix(right)) == sp.zeros(3, 1)


def reduced_line_groups(lines):
    groups = []
    used = set()
    for name in lines:
        if name in used:
            continue
        group = [other for other in lines if proportional(lines[name], lines[other])]
        used.update(group)
        groups.append(group)
    return groups


def infinity_direction_counts(lines):
    groups = reduced_line_groups(lines)
    counts = {}
    for group in groups:
        alpha, beta, _ = lines[group[0]]
        if alpha == 0 and beta == 0:
            continue
        direction = (int(alpha), int(beta))
        if direction[0] < 0 or (direction[0] == 0 and direction[1] < 0):
            direction = (-direction[0], -direction[1])
        counts[direction] = counts.get(direction, 0) + 1
    return counts


def log_smoothness_audit():
    # Homogeneous base-line convention: alpha*a+beta*b+constant*s=0.
    source = {
        "q_g1": (0, 1, -y - z),
        "q_g2": (1, 0, -x - z),
        "q_g3": (1, 1, z),
        "q_g12": (1, 1, x + y),
        "q_g23": (0, 1, -x),
        "q_g31": (1, 0, -y),
        "q_G23": (1, 0, E),
        "q_G31": (0, 1, E),
    }
    minor = {
        "ca--": (1, 0, -E - y),
        "ca-+": (1, 0, -E + y),
        "ca+-": (1, 0, E - y),
        "ca++": (1, 0, E + y),
        "cb--": (0, 1, -E - x),
        "cb-+": (0, 1, -E + x),
        "cb+-": (0, 1, E - x),
        "cb++": (0, 1, E + x),
        "ab--": (1, 1, -z),
        "ab-+": (1, 1, z),
        "ab+-": (1, -1, -z),
        "ab++": (1, -1, z),
    }
    edges = {"a=0": (1, 0, 0), "b=0": (0, 1, 0)}
    infinity = {"D_infinity": (0, 0, 1)}
    active_names = ["q_g1", "q_g2", "q_g3", "q_g23", "q_g31"]

    full_lines = source | minor | edges | infinity
    duplicate_groups = [
        sorted(group)
        for group in reduced_line_groups(full_lines)
        if len(group) > 1
    ]
    expected_duplicates = sorted(
        [
            sorted(["q_g1", "cb-+"]),
            sorted(["q_g2", "ca-+"]),
            sorted(["q_g3", "ab-+"]),
        ]
    )
    assert sorted(duplicate_groups) == expected_duplicates

    active_pair_lines = (
        {name: source[name] for name in active_names} | minor | edges | infinity
    )
    active_without_infinity = {
        name: value for name, value in active_pair_lines.items() if name != "D_infinity"
    }
    full_without_infinity = {
        name: value for name, value in full_lines.items() if name != "D_infinity"
    }
    active_counts = infinity_direction_counts(active_without_infinity)
    full_counts = infinity_direction_counts(full_without_infinity)
    assert active_counts == {(0, 1): 6, (1, 0): 6, (1, 1): 2, (1, -1): 2}
    assert full_counts == {(0, 1): 7, (1, 0): 7, (1, 1): 3, (1, -1): 2}

    infinity_branch_values = {
        "vertical_[0:1:0]": sp.factor(F.subs({a: 0, b: 1})),
        "horizontal_[1:0:0]": sp.factor(F.subs({a: 1, b: 0})),
        "a+b_[1:-1:0]": sp.factor(F.subs({a: 1, b: -1})),
        "a-b_[1:1:0]": sp.factor(F.subs({a: 1, b: 1})),
    }
    assert infinity_branch_values == {
        "vertical_[0:1:0]": y**2,
        "horizontal_[1:0:0]": x**2,
        "a+b_[1:-1:0]": z**2,
        "a-b_[1:1:0]": z**2,
    }

    # Independent local check at the pole/minor coincidence q_g2=ca-+.
    line_value = x + z
    square_root = sp.factor(
        b**2 * y
        + x**3
        - x**2 * y
        + x**2 * z
        - x * y**2
        - 2 * x * y * z
        - x * z**2
        - y**2 * z
        - 2 * y * z**2
        - z**3
    )
    assert sp.factor(K.subs(a, line_value) - square_root**2) == 0
    constant_term = sp.factor(square_root.subs(b, 0))
    normal_derivative_at_branch = sp.factor(
        sp.diff(K, a).subs(a, line_value).subs(b**2, -constant_term / y)
    )
    expected_normal = sp.factor(
        2
        * (x + z)
        * (x - y - z)
        * (x - y + z)
        * (x + y - z)
        * (x + y + z) ** 2
        / y
    )
    assert sp.factor(normal_derivative_at_branch - expected_normal) == 0

    Q = sp.expand(4 * A_ell * B_ell - (A_ell + B_ell - E**2) ** 2)
    q_slice = sp.Poly(Q.subs(rho, 2), lam)
    tangency_exclusion = sp.Poly(
        lam
        * (lam - 1)
        * (lam + 1)
        * (2 * lam + 1)
        * (3 * lam - 1)
        * (3 * lam + 1)
        * (2 * lam**2 - 3 * lam - 1),
        lam,
    )
    assert sp.gcd(q_slice, tangency_exclusion).degree() == 0

    # At nonsoft Q=0 the four infinity directions are unramified, hence each
    # has two points upstairs.  At either point the number of active frozen
    # boundary branches is line-count + D_infinity, already >2 on a surface.
    active_upstairs_branch_counts = {
        str(direction): count + 1 for direction, count in active_counts.items()
    }
    full_upstairs_branch_counts = {
        str(direction): count + 1 for direction, count in full_counts.items()
    }
    assert min(active_upstairs_branch_counts.values()) >= 3

    return {
        "surface_at_generic_Q0": (
            "smooth on the entry-155 nonsoft locus; Q is not an absolute discriminant"
        ),
        "reduced_full_surface_divisor_domain_pair_log_smooth": False,
        "duplicate_labeled_components": duplicate_groups,
        "infinity_arrangement": {
            "branch_values": {
                name: sp.sstr(value) for name, value in infinity_branch_values.items()
            },
            "active_five_plus_minor_edge_line_counts_before_D_infinity": {
                str(direction): count for direction, count in active_counts.items()
            },
            "active_five_upstairs_branches_including_D_infinity": active_upstairs_branch_counts,
            "full_eight_plus_minor_edge_line_counts_before_D_infinity": {
                str(direction): count for direction, count in full_counts.items()
            },
            "full_eight_upstairs_branches_including_D_infinity": full_upstairs_branch_counts,
            "failure": (
                "at each unramified lift, at least three reduced boundary branches "
                "meet on a smooth surface; simple normal crossings allows at most two"
            ),
        },
        "ramification_face_local_model": {
            "tested_component": "q_g2 = ca-+ = {a-x-z=0}",
            "K_restriction": f"({sp.sstr(square_root)})^2",
            "normal_derivative_at_square_root_zero": sp.sstr(expected_normal),
            "generic_Q0_exclusion_gcd": "1 on rho=2, lambda in (1,2)",
            "failure": (
                "the two pullback branches W=+R and W=-R and the domain "
                "ramification branch W=0 meet in an ordinary triple point"
            ),
        },
        "conclusion": (
            "a log resolution is required before a log-smooth relative "
            "Gauss-Manin object can be formed; none is added here"
        ),
        "physical_chain_incidence": (
            "undetermined because the source does not give the lifted complex/Borel-Moore "
            "chain, sheets, orientations, or multiplicities"
        ),
    }


def verify_source_hashes(repository_root):
    checks = {}
    for relative_path, expected in SOURCE_HASHES.items():
        path = repository_root / relative_path
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise AssertionError(
                f"frozen input hash mismatch for {relative_path}: {actual} != {expected}"
            )
        checks[relative_path] = actual
    return checks


def build_packet(repository_root):
    source_checks = verify_source_hashes(repository_root)
    matrix, certificates = derive_connection()
    final_report = final_block_checks(matrix)
    q_report = q_zero_checks(matrix, final_report)
    log_report = log_smoothness_audit()

    return {
        "schema": SCHEMA,
        "status": "proved_absolute_reduction_relative_chain_underdetermined",
        "frozen_inputs_sha256": source_checks,
        "normalization": {
            "dimension": "d=3 (gamma=-1/2)",
            "slice": "X1=rho*lambda, X2=lambda, X3=1",
            "q_coordinate": "q_G12=E+y12; q=y12+E; dq/dy12=1",
            "residue_surface": "w^2=K(a,b)",
            "K": sp.sstr(K),
            "K1": sp.sstr(K1),
            "basis": [
                "e1=a*b/K^(1/2)",
                "e2=a/K^(1/2)",
                "e3=-a*K1/(2*K^(3/2))",
                "e4=b/K^(1/2)",
                "e5=-b*K1/(2*K^(3/2))",
                "e6=-K1/(2*K^(3/2))",
                "e7=1/K^(1/2)",
                "e8=a^2/K^(1/2)",
                "e9=b^2/K^(1/2)",
            ],
        },
        "griffiths_dwork_identity": (
            "d((-V_b da+V_a db)/K^s) = "
            "(div(V)*K-s*(V_a*K_a+V_b*K_b))*da*db/K^(s+1)"
        ),
        "connection": {
            "convention": "d_lambda e_i = sum_j A[i,j] e_j",
            "basis": [f"e{index}" for index in range(1, 10)],
            "block_sizes": [1, 2, 2, 4],
            "matrix": [
                [expression_record(matrix[row, column]) for column in range(9)]
                for row in range(9)
            ],
            "reduction_certificates": certificates,
        },
        "final_block_and_kernel": final_report,
        "generic_transverse_Q0": q_report,
        "log_smoothness_audit": log_report,
        "exact_limitations": [
            "The computation determines the absolute homogeneous d=3 q_G12-residue connection, not a generic-d epsilon connection.",
            "The full frozen divisor arrangement is not log-smooth before resolution.",
            "The source supplies no log resolution, relative/Borel-Moore chain lift, sheet labels, orientations, or multiplicities.",
            "Therefore no physical relative-chain connection or physical Q=0 monodromy is mathematically determined by the frozen source.",
            "The zero Q residue and I_9 monodromy proved here apply only to the absolute equation-(58) residue module.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        help="optional JSON result path (stdout is always concise)",
    )
    parser.add_argument(
        "--repository-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
    )
    args = parser.parse_args()
    packet = build_packet(args.repository_root.resolve())
    if args.output:
        args.output.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    summary = {
        "schema": packet["schema"],
        "status": packet["status"],
        "cleared_reductions": len(
            packet["connection"]["reduction_certificates"]
        ),
        "all_cleared_identities": all(
            certificate["all_cleared_numerators_zero"]
            for certificate in packet["connection"]["reduction_certificates"]
        ),
        "L2_match": packet["final_block_and_kernel"]["infinity_gysin"]
        ["printed_L2"]["matches_equation_59"],
        "generic_Q0_absolute_residue": "zero_9x9",
        "generic_Q0_absolute_monodromy": "I_9",
        "full_frozen_pair_log_smooth": packet["log_smoothness_audit"]
        ["reduced_full_surface_divisor_domain_pair_log_smooth"],
        "physical_relative_connection": "underdetermined_by_source",
        "output": str(args.output) if args.output else None,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
