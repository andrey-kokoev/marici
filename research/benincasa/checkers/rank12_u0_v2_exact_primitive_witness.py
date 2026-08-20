import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
WITNESS = ROOT / "research/benincasa/rank12-u0-v2-exceptional-pilot-rational-witness.json"
RESULT = ROOT / "research/benincasa/results/rank12-u0-v2-exceptional-pilot-rational-witness.json"

s, a, b = sp.symbols("s a b")


def monomials(degree):
    return [(i, total - i) for total in range(degree + 1) for i in range(total + 1)]


K = (
    a**4
    + 2 * (1 - s) * a**2 * b
    + (-sp.Rational(5, 2) - s - s**2 / 2) * a**2
    + (1 + s) ** 2 * b**2
    + (-5 + 3 * s + s**2 + s**3) * b / 2
    + (25 - 44 * s + 14 * s**2 + 4 * s**3 + s**4) / 16
)
K1 = 4 * a**2 + 4 * (1 - s) * b - s**2 + 6 * s - 5
L1 = b - 1
L2 = a + (s - 1) / 2


def classes():
    one = sp.Integer(1)

    def double(monomial):
        return (0, 0, 3, -monomial * K1 / 2)

    return [
        (1, 1, 1, one),
        (1, 0, 1, one),
        (0, 1, 1, one),
        (0, 0, 1, a * b),
        (0, 0, 1, a),
        double(a),
        (0, 0, 1, b),
        double(b),
        double(one),
        (0, 0, 1, one),
        (0, 0, 1, a**2),
        (0, 0, 1, b**2),
    ]


def common(cls):
    aa, bb, h, n = cls
    return n * L1 ** (2 - aa) * L2 ** (2 - bb) * K ** ((5 - h) // 2)


def target(cls):
    aa, bb, h, n = cls
    ea, eb, ek = 2 - aa, 2 - bb, (5 - h) // 2
    value = sp.diff(n, s) * L1**ea * L2**eb * K**ek
    if aa:
        value -= n * L1 ** (ea - 1) * L2**eb * K**ek * sp.diff(L1, s) * aa
    if bb:
        value -= n * L1**ea * L2 ** (eb - 1) * K**ek * sp.diff(L2, s) * bb
    value -= n * L1**ea * L2**eb * sp.diff(K, s) * K ** (ek - 1) * sp.Rational(h, 2)
    return sp.expand(value)


def exact(sa, sb, exponents, is_q):
    f = a ** exponents[0] * b ** exponents[1]
    ea, eb = 2 - sa, 2 - sb
    base = L1**ea * L2**eb
    if not is_q:
        value = -sp.diff(f, b) * base * K
        if sa:
            value += f * L1 ** (ea - 1) * L2**eb * K * sa
        value += sp.Rational(3, 2) * f * base * sp.diff(K, b)
    else:
        value = sp.diff(f, a) * base * K
        if sb:
            value -= f * L1**ea * L2 ** (eb - 1) * K * sb
        value -= sp.Rational(3, 2) * f * base * sp.diff(K, a)
    return sp.expand(value)


def source_columns():
    cls = classes()
    columns = [sp.expand(common(item)) for item in cls]
    for sa, sb in [(1, 1), (1, 0), (0, 1), (0, 0)]:
        for exponent in monomials(8):
            columns.append(exact(sa, sb, exponent, False))
            columns.append(exact(sa, sb, exponent, True))
    assert len(columns) == 372
    return cls, columns


def main():
    packet = json.loads(WITNESS.read_text())
    coordinates = {int(column): sp.Rational(value) for column, value in packet["rational_coordinates"]}
    numerator_degree = packet["numerator_degree"]
    numerator = [sp.Integer(0)] * 372
    for column in range(372):
        numerator[column] = sum(
            coordinates.get(column * (numerator_degree + 1) + degree, 0) * s**degree
            for degree in range(numerator_degree + 1)
        )
    denominator = sum(coordinates.get(2604 + degree, 0) * s**degree for degree in range(5))
    cls, columns = source_columns()
    residual = sp.Poly(
        sp.expand(sum(coefficient * column for coefficient, column in zip(numerator, columns))
                  - denominator * target(cls[0])),
        a, b, s,
        domain=sp.QQ,
    )
    result = {
        "schema": "marici.benincasa.rank12_u0_v2_exact_primitive_check.v1",
        "status": "passed" if residual.is_zero else "failed",
        "chart": "p_nonzero",
        "master": 0,
        "source_columns": len(columns),
        "nonzero_numerator_polynomials": sum(value != 0 for value in numerator),
        "denominator": str(sp.factor(denominator)),
        "residual_term_count": 0 if residual.is_zero else len(residual.terms()),
        "residual_zero": residual.is_zero,
        "normalization_is_canonical": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
    if not residual.is_zero:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
