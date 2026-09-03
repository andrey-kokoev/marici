from __future__ import annotations

import json
import math
import sympy as sp


def main() -> None:
    # Exact checks for several degrees: the Hankel Rayleigh form for
    # p(y)=(1-y)^m is the (2m+1)-st forward difference of H.
    for m in range(1, 8):
        H = sp.symbols(f"H0:{2*m+2}")
        c = [(-1) ** i * math.comb(m, i) for i in range(m + 1)]
        q = sum(c[i] * c[j] * (H[i + j] - H[i + j + 1])
                for i in range(m + 1) for j in range(m + 1))
        expected = sum((-1) ** k * math.comb(2 * m + 1, k) * H[k]
                       for k in range(2 * m + 2))
        assert sp.expand(q - expected) == 0

    # The coefficient convolution is Vandermonde's identity.
    m, k = sp.symbols("m k", integer=True, nonnegative=True)
    # Numeric hostile fixture shows cancellation hidden by the l1 bound 4^m.
    degree = 10
    coefficients = [(-1) ** i * math.comb(degree, i) for i in range(degree + 1)]
    assert sum(abs(v) for v in coefficients) ** 2 == 4**degree
    assert sum(coefficients) == 0

    result = {
        "schema":"marici.voevodsky.near-null-high-difference-observer-check.v1",
        "status":"exact_high_difference_identity_verified",
        "degrees_checked":"1..7",
        "identity":"Q_H((1-y)^m)=Delta_h^(2m+1) H(t)",
        "coefficientwise_l1_square":"4^m",
        "exact_cancellation_at_constant_kernel":True,
        "prime_sign_proved":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
