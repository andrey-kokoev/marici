import importlib.util
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
BASE_PATH = Path(__file__).with_name("rank12_u0_v2_exact_primitive_witness.py")
SUPPORT = ROOT / "research/benincasa/rank12-u0-v2-exceptional-q-restricted-support.json"
WITNESS = ROOT / "research/benincasa/rank12-u0-v2-exceptional-q-pilot-rational-witness.json"
RESULT = ROOT / "research/benincasa/results/rank12-u0-v2-exceptional-q-pilot-rational-witness.json"

spec = importlib.util.spec_from_file_location("p_chart_checker", BASE_PATH)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
s, a, b = base.s, base.a, base.b

# Here s denotes the q-chart coordinate r=p/q.  Rebinding the source geometry
# reuses only the typed class/exact formulas from the p-chart checker.
base.K = (
    a**4
    + 2 * (s - 1) * a**2 * b
    + (-s - sp.Rational(5, 2) * s**2 - sp.Rational(1, 2)) * a**2
    + (s + 1) ** 2 * b**2
    + (sp.Rational(1, 2) + s / 2 + 3 * s**2 / 2 - 5 * s**3 / 2) * b
    + s / 4 + 7 * s**2 / 8 - 11 * s**3 / 4 + 25 * s**4 / 16 + sp.Rational(1, 16)
)
base.K1 = 4 * s * a**2 + 4 * s * (s - 1) * b + s * (-1 + 6 * s - 5 * s**2)
base.L1 = b - s
base.L2 = a + (1 - s) / 2


def polynomial_for_coordinate(index, columns, target):
    if index < 2604:
        column, degree = divmod(index, 7)
        return sp.expand(s**degree * columns[column])
    degree = index - 2604
    return sp.expand(-s**degree * target)


def main():
    support = json.loads(SUPPORT.read_text())
    normalization = support["normalization_column"]
    unknown_coordinates = [index for index in support["coordinates"] if index != normalization]
    classes, columns = base.source_columns()
    target = base.target(classes[0])
    polynomials = [polynomial_for_coordinate(index, columns, target) for index in unknown_coordinates]
    normalized = polynomial_for_coordinate(normalization, columns, target)

    dictionaries = [sp.Poly(poly, a, b, s, domain=sp.QQ).as_dict() for poly in polynomials]
    rhs_dictionary = sp.Poly(-normalized, a, b, s, domain=sp.QQ).as_dict()
    monomials = sorted(set(rhs_dictionary).union(*(dictionary.keys() for dictionary in dictionaries)))
    row_index = {monomial: row for row, monomial in enumerate(monomials)}
    entries = {}
    for column, dictionary in enumerate(dictionaries):
        for monomial, coefficient in dictionary.items():
            entries[(row_index[monomial], column)] = coefficient
    matrix = sp.MutableSparseMatrix(len(monomials), len(unknown_coordinates), entries)
    rhs = sp.MutableSparseMatrix(
        len(monomials), 1,
        {(row_index[monomial], 0): coefficient for monomial, coefficient in rhs_dictionary.items()},
    )
    solution, parameters = sp.linsolve((matrix, rhs)).args[0], None
    free_symbols = set().union(*(value.free_symbols for value in solution)) - {s, a, b}
    if free_symbols:
        solution = tuple(value.subs({symbol: 0 for symbol in free_symbols}) for value in solution)

    coordinates = {normalization: sp.Integer(1)}
    coordinates.update({index: value for index, value in zip(unknown_coordinates, solution) if value != 0})
    residual = sp.Poly(
        sp.expand(sum(coordinates[index] * polynomial_for_coordinate(index, columns, target)
                      for index in coordinates)),
        a, b, s,
        domain=sp.QQ,
    )
    witness = {
        "schema": "marici.benincasa.rank12_u0_v2_exceptional_q_pilot_rational_witness.v2",
        "status": "characteristic_zero_identity_verified" if residual.is_zero else "failed",
        "chart": "q_nonzero",
        "coordinate": "r=p/q",
        "master": 0,
        "numerator_degree": 6,
        "denominator_degree": 5,
        "normalization": {"column": normalization, "value": "1/1", "canonical": False},
        "restricted_support_coordinates": len(support["coordinates"]),
        "nonzero_coordinate_count": len(coordinates),
        "rational_coordinates": [[index, str(value)] for index, value in sorted(coordinates.items())],
        "exact_characteristic_zero_verification": residual.is_zero,
    }
    denominator = sum(coordinates.get(2604 + degree, 0) * s**degree for degree in range(6))
    result = {
        "schema": "marici.benincasa.rank12_u0_v2_exact_q_primitive_check.v1",
        "status": "passed" if residual.is_zero else "failed",
        "equations": len(monomials),
        "unknown_coordinates": len(unknown_coordinates),
        "free_parameter_count": len(free_symbols),
        "nonzero_coordinate_count": len(coordinates),
        "denominator": str(sp.factor(denominator)),
        "residual_term_count": 0 if residual.is_zero else len(residual.terms()),
        "residual_zero": residual.is_zero,
        "normalization_is_canonical": False,
    }
    WITNESS.write_text(json.dumps(witness, indent=2) + "\n")
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
    if not residual.is_zero:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
