import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".tmp_sympy"))
import mpmath as mp


def kummer_integral(x, y):
    a = x * y
    s = x + y
    n0 = mp.sqrt(2 * s / a)

    def pulled_back(theta):
        n = n0 * mp.sin(theta)
        dn = n0 * mp.cos(theta)
        w = 1j * mp.sqrt(2 * s) * mp.cos(theta)
        return dn / w

    return mp.quad(pulled_back, [-mp.pi / 2, 0, mp.pi / 2])


def periods(x, y):
    a = x * y
    i0 = kummer_integral(x, y)
    c31 = -(3 * x * x + 7 * x * y + 6 * y * y) / (16 * a ** mp.mpf("3.5"))
    c23 = (6 * x * x + 7 * x * y + 3 * y * y) / (16 * a ** mp.mpf("3.5"))
    return i0, c31 * i0, c23 * i0


def sci(z):
    return mp.nstr(z, 30)


def main():
    mp.mp.dps = 100
    cases = [
        ("generic_1_2", mp.mpf(1), mp.mpf(2)),
        ("generic_2_5", mp.mpf(2), mp.mpf(5)),
        ("near_diagonal", mp.mpf(1) + mp.mpf("1e-40"), mp.mpf(1)),
        ("near_soft", mp.mpf("1e-40"), mp.mpf(3)),
    ]
    rows = []
    max_integral_error = mp.mpf(0)
    max_sewing_error = mp.mpf(0)
    for label, x, y in cases:
        i0, p31, p23 = periods(x, y)
        expected_i0 = -1j * mp.pi / mp.sqrt(x * y)
        expected_sum = -3j * mp.pi * (x - y) * (x + y) / (16 * (x * y) ** 4)
        integral_error = abs(i0 - expected_i0) / max(1, abs(expected_i0))
        sewing_error = abs(p31 + p23 - expected_sum) / max(1, abs(expected_sum))
        max_integral_error = max(max_integral_error, integral_error)
        max_sewing_error = max(max_sewing_error, sewing_error)
        rows.append(
            {
                "case": label,
                "x": sci(x),
                "y": sci(y),
                "kummer_integral": sci(i0),
                "p31": sci(p31),
                "p23": sci(p23),
                "sewn": sci(p31 + p23),
                "relative_integral_error": sci(integral_error),
                "relative_sewing_error": sci(sewing_error),
            }
        )
    assert max_integral_error < mp.mpf("1e-90")
    assert max_sewing_error < mp.mpf("1e-90")
    result = {
        "schema": "marici.occurrence-relative-periods-numeric.v1",
        "precision_decimal_digits": mp.mp.dps,
        "cases": rows,
        "max_relative_integral_error": sci(max_integral_error),
        "max_relative_sewing_error": sci(max_sewing_error),
        "scope": "Kummer quotient periods; endpoint-jet evaluation intentionally excluded",
        "new_carrier_incidence": False,
    }
    with open(sys.argv[1], "w", encoding="utf-8", newline="\n") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")


if __name__ == "__main__":
    main()
