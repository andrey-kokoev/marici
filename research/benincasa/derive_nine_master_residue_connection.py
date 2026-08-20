"""Exact nine-master Cayley--Menger residue connection.

This is a deliberately self-contained symbolic prototype for the homogeneous
three-site slice used below equation (58) of arXiv:2408.16386v2.  It works
over the rational-function field QQ(a1, lambda); ``a`` and ``b`` are fibre
coordinates.  Every reduction is certified after clearing its highest pole
(K0**(3/2) or K0**(5/2)), so the final check is an ordinary polynomial
identity in a,b.

Run, for example, with

    uv run --with sympy python research/benincasa/derive_nine_master_residue_connection.py

The adjacent JSON file is replaced only after every fail-closed assertion
has passed.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import sympy as sp
from sympy.polys.matrices import DomainMatrix


SCHEMA = "marici.benincasa.nine_master_residue_connection.v1"
DEFAULT_RESULT = Path(__file__).with_suffix(".result.json")


@dataclass(frozen=True)
class Master:
    name: str
    source_numerator: sp.Expr
    pole: str
    numerator: sp.Expr
    parity: tuple[int, int]


@dataclass
class Reduction:
    coefficients: list[sp.Expr]
    primitives: dict[str, sp.Expr]
    attempts: list[dict[str, object]]
    cleared_residual: sp.Expr


def canonical(expr: sp.Expr) -> sp.Expr:
    """Canonical rational-function representative without heuristic floats."""

    return sp.cancel(expr)


def expression_string(expr: sp.Expr) -> str:
    # All connection entries have already passed through the fraction-field
    # RREF.  Re-cancelling every entry here is expensive and adds no proof.
    return sp.sstr(expr, order="lex")


def matrix_strings(matrix: sp.MatrixBase) -> list[list[str]]:
    return [
        [expression_string(matrix[row, col]) for col in range(matrix.cols)]
        for row in range(matrix.rows)
    ]


def total_degree_monomials(
    aa: sp.Symbol,
    bb: sp.Symbol,
    degree: int,
    parity: tuple[int, int],
) -> list[sp.Expr]:
    if degree < 0:
        return []
    answer: list[sp.Expr] = []
    for total in range(degree + 1):
        for degree_a in range(total + 1):
            degree_b = total - degree_a
            if (degree_a % 2, degree_b % 2) == parity:
                answer.append(aa**degree_a * bb**degree_b)
    return answer


class ExactReducer:
    """Solve polynomial Griffiths--Dwork identities over QQ(a1,lambda)."""

    # Bounds are (degree at s=1/2, degree at s=3/2).  A simple-pole
    # derivative is cleared only to K0^(3/2), so it never needs s=3/2.
    # Double-pole derivatives are cleared to K0^(5/2).  These finite
    # schedules are fixed before inspecting the connection coefficients.
    SIMPLE_BOUNDS = ((0, -1), (1, -1), (2, -1), (3, -1))
    DOUBLE_BOUNDS = ((0, 0), (1, 1), (2, 3), (3, 5), (3, 7))

    def __init__(
        self,
        aa: sp.Symbol,
        bb: sp.Symbol,
        parameter_field,
        polynomial: sp.Expr,
        masters: list[Master],
    ) -> None:
        self.a = aa
        self.b = bb
        self.field = parameter_field
        self.K = sp.Poly(polynomial, aa, bb, domain=parameter_field).as_expr()
        self.Ka = sp.diff(self.K, aa)
        self.Kb = sp.diff(self.K, bb)
        self.masters = masters
        self.basis_common = {
            clearing_level: [
                master.numerator
                * self.K
                ** (
                    clearing_level
                    - (0 if master.pole == "simple" else 1)
                )
                for master in masters
            ]
            for clearing_level in (1, 2)
        }

    def polynomial_dict(self, expr: sp.Expr) -> dict[tuple[int, int], object]:
        poly = sp.Poly(sp.expand(expr), self.a, self.b, domain=self.field)
        return dict(poly.terms())

    def exact_column(
        self,
        monomial: sp.Expr,
        axis: str,
        s: sp.Rational,
        clearing_level: int,
    ) -> sp.Expr:
        if axis == "U":
            numerator = self.K * sp.diff(monomial, self.a) - s * monomial * self.Ka
        else:
            # d(V da/K^s) = (-K V_b + s V K_b) da db/K^(s+1).
            numerator = -self.K * sp.diff(monomial, self.b) + s * monomial * self.Kb
        output_level = int(s + sp.Rational(1, 2))
        return sp.expand(numerator * self.K ** (clearing_level - output_level))

    def candidates(
        self,
        target_parity: tuple[int, int],
        bounds: tuple[int, int],
        clearing_level: int,
    ) -> tuple[list[sp.Expr], list[tuple[str, sp.Expr]]]:
        candidates: list[sp.Expr] = []
        labels: list[tuple[str, sp.Expr]] = []

        for index, master in enumerate(self.masters):
            if master.parity == target_parity:
                candidates.append(self.basis_common[clearing_level][index])
                labels.append((f"basis:{index}", sp.Integer(1)))

        for s, degree, tag in zip(
            (sp.Rational(1, 2), sp.Rational(3, 2)),
            bounds,
            ("half", "three_half"),
        ):
            if degree < 0:
                continue
            u_parity = (target_parity[0] ^ 1, target_parity[1])
            v_parity = (target_parity[0], target_parity[1] ^ 1)
            for monomial in total_degree_monomials(self.a, self.b, degree, u_parity):
                candidates.append(self.exact_column(monomial, "U", s, clearing_level))
                labels.append((f"U:{tag}", monomial))
            for monomial in total_degree_monomials(self.a, self.b, degree, v_parity):
                candidates.append(self.exact_column(monomial, "V", s, clearing_level))
                labels.append((f"V:{tag}", monomial))
        return candidates, labels

    def linear_system(
        self, candidates: list[sp.Expr], target: sp.Expr
    ) -> tuple[DomainMatrix, list[tuple[int, int]]]:
        column_dicts = [self.polynomial_dict(candidate) for candidate in candidates]
        target_dict = self.polynomial_dict(target)
        monomials = sorted(
            set(target_dict).union(*(set(column) for column in column_dicts)),
            key=lambda item: (sum(item), item),
        )
        zero = self.field.zero
        rows = [
            [column.get(monomial, zero) for column in column_dicts]
            + [target_dict.get(monomial, zero)]
            for monomial in monomials
        ]
        return DomainMatrix.from_list(rows, self.field), monomials

    def solve(
        self,
        target: sp.Expr,
        target_parity: tuple[int, int],
        target_name: str,
        clearing_level: int,
    ) -> Reduction:
        attempts: list[dict[str, object]] = []
        schedule = self.SIMPLE_BOUNDS if clearing_level == 1 else self.DOUBLE_BOUNDS
        for bounds in schedule:
            print(f"reduce {target_name}: trying bounds {bounds}", flush=True)
            candidates, labels = self.candidates(target_parity, bounds, clearing_level)
            augmented, monomials = self.linear_system(candidates, target)
            rref, pivots = augmented.rref()
            inconsistent = bool(pivots and pivots[-1] == len(candidates))
            rank_augmented = len(pivots)
            rank_coefficient = rank_augmented - int(inconsistent)
            attempt = {
                "primitive_degree_bounds": {
                    "s=1/2": bounds[0],
                    "s=3/2": bounds[1],
                },
                "equations": len(monomials),
                "unknowns": len(candidates),
                "rank_coefficient": rank_coefficient,
                "rank_augmented": rank_augmented,
                "consistent": not inconsistent,
            }
            attempts.append(attempt)
            print(
                f"reduce {target_name}: rank {rank_coefficient}/{rank_augmented} "
                f"({'closed' if not inconsistent else 'obstructed'})",
                flush=True,
            )
            if inconsistent:
                continue

            rref_matrix = rref.to_Matrix()
            solution = [sp.Integer(0)] * len(candidates)
            for row, pivot in enumerate(pivots):
                if pivot < len(candidates):
                    # DomainMatrix.rref has already normalized this element in
                    # QQ(a1,lambda); a second generic ``cancel`` can dominate
                    # the entire runtime for the even-even block.
                    solution[pivot] = rref_matrix[row, -1]

            coefficients = [sp.Integer(0)] * len(self.masters)
            primitives = {
                "U_s=1/2": sp.Integer(0),
                "V_s=1/2": sp.Integer(0),
                "U_s=3/2": sp.Integer(0),
                "V_s=3/2": sp.Integer(0),
            }
            reconstructed = sp.Integer(0)
            for value, candidate, (label, monomial) in zip(
                solution, candidates, labels
            ):
                if value == 0:
                    continue
                reconstructed += value * candidate
                if label.startswith("basis:"):
                    coefficients[int(label.split(":", 1)[1])] += value
                else:
                    axis, tag = label.split(":", 1)
                    exponent = {
                        "half": "1/2",
                        "three_half": "3/2",
                    }[tag]
                    primitives[f"{axis}_s={exponent}"] += value * monomial
            residual = sp.Poly(
                sp.expand(target - reconstructed),
                self.a,
                self.b,
                domain=self.field,
            ).as_expr()
            if residual != 0:
                raise AssertionError("RREF solution failed its cleared polynomial identity")
            return Reduction(coefficients, primitives, attempts, residual)

        last = attempts[-1]
        raise RuntimeError(
            "bounded Griffiths--Dwork closure obstruction: "
            f"rank(A)={last['rank_coefficient']} < "
            f"rank([A|b])={last['rank_augmented']} at {schedule[-1]}"
        )


def build_geometry():
    a1, lam, c, aa, bb = sp.symbols("a1 lambda c a b")
    x = a1 * lam
    y = lam
    z = sp.Integer(1)
    E = x + y + z
    q = E + c
    cayley_menger = sp.Matrix(
        [
            [0, 1, 1, 1, 1],
            [1, 0, c**2, aa**2, bb**2],
            [1, c**2, 0, y**2, x**2],
            [1, aa**2, y**2, 0, z**2],
            [1, bb**2, x**2, z**2, 0],
        ]
    )
    K = sp.expand(cayley_menger.det())
    K0 = sp.expand(K.subs(c, -E))
    K1 = sp.expand(sp.diff(K, c).subs(c, -E))
    return a1, lam, c, aa, bb, x, y, z, E, q, K, K0, K1


def build_masters(aa: sp.Symbol, bb: sp.Symbol, K1: sp.Expr) -> list[Master]:
    specifications = [
        ("e1", aa * bb, "simple"),
        ("e2", aa, "simple"),
        ("e3", aa, "double"),
        ("e4", bb, "simple"),
        ("e5", bb, "double"),
        ("e6", sp.Integer(1), "double"),
        ("e7", sp.Integer(1), "simple"),
        ("e8", aa**2, "simple"),
        ("e9", bb**2, "simple"),
    ]
    masters: list[Master] = []
    for name, source_numerator, pole in specifications:
        numerator = (
            source_numerator
            if pole == "simple"
            else -sp.Rational(1, 2) * source_numerator * K1
        )
        poly = sp.Poly(source_numerator, aa, bb)
        monomial = poly.monoms()[0]
        masters.append(
            Master(
                name,
                source_numerator,
                pole,
                sp.expand(numerator),
                (monomial[0] % 2, monomial[1] % 2),
            )
        )
    return masters


def derivative_common_numerator(
    master: Master, K0: sp.Expr, K1: sp.Expr, lam: sp.Symbol
) -> tuple[int, sp.Expr]:
    K_lambda = sp.diff(K0, lam)
    if master.pole == "simple":
        # d(N/sqrt(K))/dlam = -.5 N K_lam/K^(3/2).
        return 1, sp.expand(-sp.Rational(1, 2) * master.source_numerator * K_lambda)
    D = -sp.Rational(1, 2) * master.source_numerator * K1
    # d(D/K^(3/2)) = D_lam/K^(3/2) - 3 D K_lam/(2 K^(5/2)).
    return 2, sp.expand(
        sp.diff(D, lam) * K0 - sp.Rational(3, 2) * D * K_lambda
    )


def exact_gysin_data(
    a1: sp.Symbol,
    lam: sp.Symbol,
    x: sp.Expr,
    y: sp.Expr,
    E: sp.Expr,
):
    R = sp.Matrix(
        [
            [
                0,
                1,
                (E**2 + y**2) / 2,
                (E**2 + x**2) / 2,
            ],
            [
                0,
                0,
                -(E**2 + x**2) / 2,
                -x**2 * (E**2 + y**2) / (2 * y**2),
            ],
        ]
    ).applyfunc(canonical)
    c7 = (x**2 - y**2) * (x**2 * y**2 - E**4)
    c8 = 2 * x**2 * (E**2 + y**2)
    c9 = -2 * y**2 * (E**2 + x**2)
    v = sp.Matrix([0, c7, c8, c9]).applyfunc(canonical)
    kernel_basis = sp.Matrix.hstack(sp.Matrix([1, 0, 0, 0]), v)
    assert (R * kernel_basis).applyfunc(canonical) == sp.zeros(2, 2)
    assert R.rank() == 2
    assert kernel_basis.rank() == 2
    # The displayed vectors span the generic kernel because both dimensions are two.
    return R, v, kernel_basis


def induced_plane_connection(
    final_block: sp.Matrix,
    kernel_basis: sp.Matrix,
    lam: sp.Symbol,
) -> tuple[bool, sp.Matrix, sp.Matrix]:
    differentiated = (final_block * kernel_basis + kernel_basis.diff(lam)).applyfunc(
        canonical
    )
    induced = sp.zeros(2, 2)
    residual = sp.zeros(4, 2)
    # B=(e6,v_alg), and the e8 coefficient of v_alg is generically nonzero.
    pivot = canonical(kernel_basis[2, 1])
    for column in range(2):
        beta = canonical(differentiated[2, column] / pivot)
        alpha = canonical(differentiated[0, column])
        induced[:, column] = sp.Matrix([alpha, beta])
        residual[:, column] = (differentiated[:, column] - kernel_basis * induced[:, column]).applyfunc(
            canonical
        )
    invariant = residual == sp.zeros(4, 2)
    return invariant, induced.applyfunc(canonical), residual


def polynomial_valuation(poly: sp.Poly, divisor: sp.Poly) -> tuple[int, sp.Poly]:
    valuation = 0
    quotient = poly
    while quotient.rem(divisor).is_zero:
        quotient = quotient.exquo(divisor)
        valuation += 1
    return valuation, quotient


def residue_mod_irreducible(
    coefficient: sp.Expr, variable: sp.Symbol, divisor_expr: sp.Expr
) -> dict[str, object]:
    coefficient = sp.cancel(coefficient)
    if coefficient == 0:
        return {"pole_order": 0, "residue_mod_Q": "0"}
    numerator_expr, denominator_expr = sp.fraction(coefficient)
    divisor = sp.Poly(divisor_expr, variable, domain=sp.QQ)
    numerator = sp.Poly(numerator_expr, variable, domain=sp.QQ)
    denominator = sp.Poly(denominator_expr, variable, domain=sp.QQ)
    numerator_order, numerator_unit = polynomial_valuation(numerator, divisor)
    denominator_order, denominator_unit = polynomial_valuation(denominator, divisor)
    pole_order = denominator_order - numerator_order
    if pole_order <= 0:
        return {"pole_order": 0, "residue_mod_Q": "0"}
    if pole_order != 1:
        return {"pole_order": pole_order, "residue_mod_Q": None}
    modulus = divisor
    derivative = sp.Poly(sp.diff(divisor.as_expr(), variable), variable, domain=sp.QQ)
    denominator_inverse = sp.invert(denominator_unit, modulus)
    derivative_inverse = sp.invert(derivative, modulus)
    residue = (numerator_unit * denominator_inverse * derivative_inverse).rem(modulus)
    return {
        "pole_order": 1,
        "residue_mod_Q": expression_string(residue.as_expr()),
    }


def common_denominator(expressions: Iterable[sp.Expr]) -> sp.Expr:
    answer = sp.Integer(1)
    for expression in expressions:
        answer = sp.lcm(answer, sp.fraction(sp.cancel(expression))[1])
    return sp.factor(answer)


def derive() -> dict[str, object]:
    (
        a1,
        lam,
        c,
        aa,
        bb,
        x,
        y,
        z,
        E,
        q,
        K,
        K0,
        K1,
    ) = build_geometry()
    field = sp.QQ.frac_field(a1, lam)
    masters = build_masters(aa, bb, K1)
    reducer = ExactReducer(aa, bb, field, K0, masters)

    reductions: list[Reduction] = []
    connection = sp.zeros(9, 9)
    for column, master in enumerate(masters):
        clearing_level, target = derivative_common_numerator(master, K0, K1, lam)
        reduction = reducer.solve(
            target, master.parity, master.name, clearing_level
        )
        reductions.append(reduction)
        connection[:, column] = sp.Matrix(reduction.coefficients)

    print("all nine reductions found; starting independent verification", flush=True)
    # Recheck every identity independently from the stored primitives.
    verification: list[dict[str, object]] = []
    for column, (master, reduction) in enumerate(zip(masters, reductions)):
        clearing_level, target = derivative_common_numerator(master, K0, K1, lam)
        reconstructed = sum(
            connection[row, column]
            * reducer.basis_common[clearing_level][row]
            for row in range(9)
        )
        for s, label in (
            (sp.Rational(1, 2), "1/2"),
            (sp.Rational(3, 2), "3/2"),
        ):
            for axis in ("U", "V"):
                primitive = reduction.primitives[f"{axis}_s={label}"]
                if primitive != 0:
                    reconstructed += reducer.exact_column(
                        primitive, axis, s, clearing_level
                    )
        residual_poly = sp.Poly(
            sp.expand(target - reconstructed), aa, bb, domain=field
        )
        assert residual_poly.is_zero
        verification.append(
            {
                "master": master.name,
                "clearing_power": f"K0^({clearing_level}+1/2)",
                "polynomial_ring": "QQ(a1,lambda)[a,b]",
                "residual": "0",
                "verified": True,
            }
        )
        print(f"verified {master.name}: cleared residual is zero", flush=True)

    print("checking character blocks", flush=True)
    block_ranges = ((0, 1), (1, 3), (3, 5), (5, 9))
    off_block_entries: list[tuple[int, int]] = []
    for row in range(9):
        for column in range(9):
            same_block = any(
                start <= row < stop and start <= column < stop
                for start, stop in block_ranges
            )
            if not same_block and connection[row, column] != 0:
                off_block_entries.append((row + 1, column + 1))
    assert not off_block_entries
    final_block = connection[5:9, 5:9]

    print("checking infinity-Gysin kernel", flush=True)
    R, v_alg, kernel_basis = exact_gysin_data(a1, lam, x, y, E)
    print("computing induced algebraic-plane connection", flush=True)
    invariant, algebraic_connection, algebraic_residual = induced_plane_connection(
        final_block, kernel_basis, lam
    )

    Aell = sp.expand((x - y) ** 2 - z**2)
    Bell = sp.expand((x + y) ** 2 - z**2)
    Q = sp.factor(4 * Aell * Bell - (Aell + Bell - E**2) ** 2)
    print("computing exact transverse Q residue", flush=True)
    rational_slice = {a1: sp.Integer(2)}
    Q_slice = sp.factor(Q.subs(rational_slice))
    assert sp.gcd(Q_slice, sp.diff(Q_slice, lam)) == 1

    algebraic_slice = algebraic_connection.subs(rational_slice).applyfunc(canonical)
    residue_matrix = [
        [residue_mod_irreducible(algebraic_slice[i, j], lam, Q_slice) for j in range(2)]
        for i in range(2)
    ]
    denominator_slice = common_denominator(list(algebraic_slice))
    q_denominator_gcd = sp.factor(sp.gcd(Q_slice, denominator_slice))

    e6_line_invariant = canonical(algebraic_connection[1, 0]) == 0
    valg_line_invariant = canonical(algebraic_connection[0, 1]) == 0
    selected_rank_one = None
    selected_coefficient = None
    if e6_line_invariant:
        selected_rank_one = "quotient span(e6,v_alg)/span(e6), represented by v_alg"
        selected_coefficient = algebraic_connection[1, 1]
    elif valg_line_invariant:
        selected_rank_one = "subline span(v_alg)"
        selected_coefficient = algebraic_connection[1, 1]

    selected_residue = (
        residue_mod_irreducible(
            canonical(selected_coefficient.subs(rational_slice)), lam, Q_slice
        )
        if selected_coefficient is not None
        else None
    )

    status = "exact_connection_found"
    if not invariant:
        status = "exact_connection_found_algebraic_plane_not_invariant"

    result: dict[str, object] = {
        "schema": SCHEMA,
        "status": status,
        "conventions": {
            "field": "QQ(a1,lambda)",
            "fiber_polynomial_ring": "QQ(a1,lambda)[a,b]",
            "connection": "d(e_j)/dlambda = sum_i connection[i][j] e_i modulo exact two-forms",
            "orientation": "da wedge db",
            "cayley_menger": "literal 5x5 determinant; no fitted rescaling",
            "q": "E+c",
        },
        "slice": {
            "X1": expression_string(x),
            "X2": expression_string(y),
            "X3": expression_string(z),
            "E": expression_string(E),
        },
        "geometry": {
            "K": expression_string(sp.factor(K)),
            "q": expression_string(q),
            "K0": expression_string(sp.factor(K0)),
            "K1": expression_string(sp.factor(K1)),
            "degree_ab_K0": sp.Poly(K0, aa, bb).total_degree(),
            "degree_ab_K1": sp.Poly(K1, aa, bb).total_degree(),
        },
        "basis": [
            {
                "name": master.name,
                "source_numerator": expression_string(master.source_numerator),
                "representative_numerator": expression_string(master.numerator),
                "denominator": "K0^(1/2)" if master.pole == "simple" else "K0^(3/2)",
                "pole": master.pole,
            }
            for master in masters
        ],
        "griffiths_dwork": {
            "identities": [
                "d(U db/K0^s) = (K0*d_a(U)-s*U*d_a(K0)) da db/K0^(s+1)",
                "d(V da/K0^s) = (-K0*d_b(V)+s*V*d_b(K0)) da db/K0^(s+1)",
            ],
            "s_values": ["1/2", "3/2"],
            "bounded_ansatz_schedule": {
                "simple_targets": [list(bounds) for bounds in ExactReducer.SIMPLE_BOUNDS],
                "double_targets": [list(bounds) for bounds in ExactReducer.DOUBLE_BOUNDS],
            },
            "reductions": [
                {
                    "master": master.name,
                    "attempts": reduction.attempts,
                    "connection_coefficients_e1_to_e9": [
                        expression_string(value) for value in reduction.coefficients
                    ],
                    "primitive_certificate": {
                        key: expression_string(value)
                        for key, value in reduction.primitives.items()
                    },
                }
                for master, reduction in zip(masters, reductions)
            ],
            "verification": verification,
        },
        "connection_9x9": matrix_strings(connection),
        "block_structure": {
            "ordered_blocks": [["e1"], ["e2", "e3"], ["e4", "e5"], ["e6", "e7", "e8", "e9"]],
            "all_off_block_entries_zero": not off_block_entries,
            "nonzero_off_block_entries": off_block_entries,
            "final_4x4_order": ["e6", "e7", "e8", "e9"],
            "final_4x4": matrix_strings(final_block),
        },
        "gysin": {
            "target_order": ["omega0", "omega2"],
            "source_order": ["e6", "e7", "e8", "e9"],
            "matrix": matrix_strings(R),
            "generic_rank": 2,
            "v_alg_coefficients": [expression_string(value) for value in v_alg],
            "kernel_basis_columns": matrix_strings(kernel_basis),
            "kernel": "span(e6,v_alg)",
            "verified_R_times_kernel_zero": True,
        },
        "algebraic_plane": {
            "basis": ["e6", "v_alg"],
            "invariant": invariant,
            "induced_connection": matrix_strings(algebraic_connection),
            "cleared_leakage": matrix_strings(algebraic_residual),
            "e6_subline_invariant": e6_line_invariant,
            "v_alg_subline_invariant": valg_line_invariant,
            "selected_rank_one_subquotient": selected_rank_one,
            "selected_connection_coefficient": (
                expression_string(selected_coefficient)
                if selected_coefficient is not None
                else None
            ),
        },
        "Q_transverse_slice": {
            "Q": expression_string(Q),
            "slice": "a1=2",
            "Q_slice": expression_string(Q_slice),
            "square_free": True,
            "algebraic_plane_common_denominator": expression_string(denominator_slice),
            "gcd_Q_with_denominator": expression_string(q_denominator_gcd),
            "residue_matrix_entries": residue_matrix,
            "selected_rank_one_residue": selected_residue,
            "interpretation": (
                "regular with zero residue at generic Q=0"
                if q_denominator_gcd == 1
                else "see exact residue entries"
            ),
        },
    }
    print("assembled machine-readable result", flush=True)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_RESULT)
    arguments = parser.parse_args()
    result = derive()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    arguments.output.write_text(payload, encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {
                "schema": result["schema"],
                "status": result["status"],
                "output": str(arguments.output),
                "all_reductions_verified": all(
                    item["verified"]
                    for item in result["griffiths_dwork"]["verification"]
                ),
                "algebraic_plane_invariant": result["algebraic_plane"]["invariant"],
                "Q_slice_interpretation": result["Q_transverse_slice"]["interpretation"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
