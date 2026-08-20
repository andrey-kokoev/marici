import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
BASE_PATH = Path(__file__).with_name("rank12_u0_v2_exact_primitive_witness.py")
RESULT = ROOT / "research/benincasa/results/rank12-u0-v2-exact-quotient-residues.json"

spec = importlib.util.spec_from_file_location("p_chart_checker", BASE_PATH)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
s, a, b = base.s, base.a, base.b
BASIS_INDICES = [0, 1, 2, 6]
BASIS_LABELS = ["Omega111", "Omega101", "Omega110", "e4"]


def quotient_connection():
    classes, all_columns = base.source_columns()
    basis_columns = [all_columns[index] for index in BASIS_INDICES]
    exact_columns = []
    for sa, sb in [(1, 1), (1, 0), (0, 1), (0, 0)]:
        for exponent in base.monomials(6):
            exact_columns.append(base.exact(sa, sb, exponent, False))
            exact_columns.append(base.exact(sa, sb, exponent, True))
    solving_columns = basis_columns + exact_columns
    dictionaries = [sp.Poly(column, a, b, domain=sp.QQ.frac_field(s)).as_dict()
                    for column in solving_columns]
    connection_rows = []
    solve_metadata = []
    for class_index in BASIS_INDICES:
        rhs_dictionary = sp.Poly(base.target(classes[class_index]), a, b,
                                 domain=sp.QQ.frac_field(s)).as_dict()
        monomials = sorted(set(rhs_dictionary).union(*(dictionary.keys() for dictionary in dictionaries)))
        unknowns = sp.symbols(f"x0:{len(solving_columns)}")
        equations = [
            sum(dictionary.get(monomial, 0) * unknown
                for dictionary, unknown in zip(dictionaries, unknowns))
            - rhs_dictionary.get(monomial, 0)
            for monomial in monomials
        ]
        solution = next(iter(sp.linsolve(equations, unknowns)))
        free = set().union(*(value.free_symbols for value in solution)) - {s}
        specialized = tuple(sp.factor(value.subs({symbol: 0 for symbol in free})) for value in solution)
        residual = sp.Poly(
            sp.together(sum(value * column for value, column in zip(specialized, solving_columns))
                        - base.target(classes[class_index])),
            a, b, domain=sp.QQ.frac_field(s),
        )
        if not residual.is_zero:
            raise AssertionError("quotient reduction residual is nonzero")
        connection_rows.append(list(specialized[:4]))
        solve_metadata.append({"equations": len(monomials), "free_parameter_count": len(free)})
    return sp.Matrix(connection_rows), solve_metadata


def e5_frame(matrix):
    g = -sp.Integer(24) / ((s + 3) * (s**2 + 3))
    transformed = sp.zeros(4)
    for row in range(3):
        for column in range(3):
            transformed[row, column] = matrix[row, column]
        transformed[row, 3] = sp.factor(matrix[row, 3] / g)
    for column in range(3):
        transformed[3, column] = sp.factor(g * matrix[3, column])
    transformed[3, 3] = sp.factor(matrix[3, 3] + sp.diff(g, s) / g)
    return transformed


def residue(matrix, divisor):
    if divisor == s:
        entries = [sp.cancel(s * entry).subs(s, 0) for entry in matrix]
        return sp.Matrix(4, 4, entries), "Q"
    if divisor == s - 1:
        entries = [sp.cancel((s - 1) * entry).subs(s, 1) for entry in matrix]
        return sp.Matrix(4, 4, entries), "Q"
    if divisor == s + 1:
        entries = [sp.cancel((s + 1) * entry).subs(s, -1) for entry in matrix]
        return sp.Matrix(4, 4, entries), "Q"
    derivative = sp.diff(divisor, s)
    entries = []
    for entry in matrix:
        numerator, denominator = sp.fraction(sp.cancel(divisor * entry / derivative))
        inverse = sp.invert(sp.Poly(denominator, s, domain=sp.QQ), sp.Poly(divisor, s, domain=sp.QQ))
        reduced = sp.rem(sp.Poly(numerator, s, domain=sp.QQ) * inverse,
                         sp.Poly(divisor, s, domain=sp.QQ)).as_expr()
        entries.append(sp.factor(reduced))
    return sp.Matrix(4, 4, entries), "Q[s]/(s^2+6s+1)"


def render_matrix(matrix):
    return [[str(sp.factor(matrix[row, column])) for column in range(matrix.cols)]
            for row in range(matrix.rows)]


def divisor_rank(matrix, divisor):
    """Rank after base change to the residue field of an irreducible divisor."""
    if sp.degree(divisor, s) == 1:
        return int(matrix.rank())
    modulus = sp.Poly(divisor, s, domain=sp.QQ)
    for size in range(min(matrix.rows, matrix.cols), 0, -1):
        for rows in itertools.combinations(range(matrix.rows), size):
            for columns in itertools.combinations(range(matrix.cols), size):
                minor = sp.cancel(matrix.extract(rows, columns).det())
                numerator, denominator = sp.fraction(minor)
                if sp.rem(sp.Poly(numerator, s, domain=sp.QQ), modulus) != 0:
                    if sp.rem(sp.Poly(denominator, s, domain=sp.QQ), modulus) == 0:
                        raise AssertionError("residue minor has a denominator on its divisor")
                    return size
    return 0


def main():
    connection_e4, solves = quotient_connection()
    connection = e5_frame(connection_e4)
    expected_line = -2 * (s - 2) / ((s - 1) * (s + 1))
    if sp.factor(connection[3, 3] - expected_line) != 0:
        raise AssertionError("exact scalar line does not reproduce the frozen e5 frame")

    divisors = [("s", s), ("s-1", s - 1), ("s+1", s + 1),
                ("s^2+6s+1", s**2 + 6 * s + 1)]
    residue_packet = []
    for label, divisor in divisors:
        residue_matrix, field = residue(connection, divisor)
        residue_packet.append({
            "divisor": label,
            "field": field,
            "matrix": render_matrix(residue_matrix),
            "rank": divisor_rank(residue_matrix, divisor),
            "rank_square": divisor_rank(residue_matrix**2, divisor),
            "trace": str(sp.factor(sp.trace(residue_matrix))),
            "determinant": str(sp.factor(residue_matrix.det())),
            "characteristic_polynomial": str(sp.factor(residue_matrix.charpoly().as_expr())),
        })

    denominators = sorted({str(factor) for entry in connection for factor, _ in
                           sp.factor_list(sp.denom(sp.cancel(entry)))[1]})
    result = {
        "schema": "marici.benincasa.rank12_u0_v2_exact_quotient_residues.v1",
        "status": "passed",
        "basis": ["Omega111", "Omega101", "Omega110", "e5"],
        "connection_convention": "row i is derivative of basis i in basis columns",
        "source_reduction": solves,
        "connection": render_matrix(connection),
        "denominator_factors": denominators,
        "residues": residue_packet,
        "overlap_homotopies_have_finite_poles": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "schema": result["schema"],
        "status": result["status"],
        "denominator_factors": denominators,
        "residues": [{key: value for key, value in item.items() if key != "matrix"}
                     for item in residue_packet],
    }))


if __name__ == "__main__":
    main()
