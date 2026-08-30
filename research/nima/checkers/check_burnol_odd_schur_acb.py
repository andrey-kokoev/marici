"""Directed acb_calc certificate for the odd level-44 Schur barrier."""

import os

from sage.all import ComplexBallField, RealBallField


PRECISION = int(os.environ.get("BURNOL_PRECISION", "192"))
X_BOXES = int(os.environ.get("BURNOL_X_BOXES", "512"))
START_BOX = int(os.environ.get("BURNOL_START_BOX", "1"))
MAX_DEPTH = int(os.environ.get("BURNOL_MAX_DEPTH", "14"))
R = RealBallField(PRECISION)
C = ComplexBallField(PRECISION)
LENGTH = R(2).log()
HALF_LENGTH = LENGTH / 2
RATES = [R(2 * n) + R(1) / 2 for n in range(1, 44)]
D44 = (
    -R.pi().log()
    - R.euler_constant()
    - R.pi() / 2
    - 3 * LENGTH
    + sum(2 / (R(2 * n) + R(1) / 2) for n in range(44))
)


def interval(left, right):
    return ((left + right) / 2).add_error((right - left).upper() / 2)


def exponent(value):
    return -7 * value**2 - 32 * value**4


def kernel(value):
    return (value / 2).exp() - sum((-rate * value).exp() for rate in RATES)


K_AT_LENGTH = kernel(C(LENGTH))


def constant_b_rayleigh():
    integral = C.integral(
        lambda t, _analytic: (C(LENGTH) - t) * (K_AT_LENGTH - kernel(t)),
        0,
        LENGTH,
        abs_tol=R(2) ** -140,
        use_heap=True,
    )
    return 2 * integral.real() / LENGTH


def quotient_away_from_zero(x):
    x_complex = C(x)
    half = C(HALF_LENGTH)

    def lower(u, _analytic):
        y = x_complex * u
        difference = kernel(x_complex + y) - kernel(x_complex - y)
        return x_complex * u * (exponent(y) - exponent(x_complex)).exp() * difference

    def upper(u, _analytic):
        y = x_complex + (half - x_complex) * u
        difference_over_x = (
            kernel(y + x_complex) - kernel(y - x_complex)
        ) / x_complex
        return (
            (half - x_complex)
            * y
            * (exponent(y) - exponent(x_complex)).exp()
            * difference_over_x
        )

    value = C.integral(lower, 0, 1, abs_tol=R(2) ** -140, use_heap=True)
    value += C.integral(upper, 0, 1, abs_tol=R(2) ** -140, use_heap=True)
    return value.real()


def quotient_including_zero(x):
    """Desingularized fixed-cube quotient for an x-ball containing zero."""
    x_complex = C(x)
    half = C(HALF_LENGTH)

    def z_integral(center, radius):
        return C.integral(
            lambda z, _analytic: (
                R(1) / 2 * ((center + radius * z) / 2).exp()
                + sum(
                    rate * (-rate * (center + radius * z)).exp()
                    for rate in RATES
                )
            ),
            -1,
            1,
            abs_tol=R(2) ** -130,
            use_heap=True,
        )

    def lower(u, _analytic):
        y = x_complex * u
        return x_complex**2 * u**2 * exponent(y).exp() * z_integral(x_complex, y)

    def upper(u, _analytic):
        y = x_complex + (half - x_complex) * u
        return (
            (half - x_complex)
            * y
            * exponent(y).exp()
            * z_integral(y, x_complex)
        )

    value = C.integral(lower, 0, 1, abs_tol=R(2) ** -120, use_heap=True)
    value += C.integral(upper, 0, 1, abs_tol=R(2) ** -120, use_heap=True)
    return ((-exponent(x_complex)).exp() * value).real()


def main():
    endpoint = HALF_LENGTH / 2048
    endpoint_value = quotient_including_zero(interval(R(0), endpoint))
    width = (HALF_LENGTH - endpoint) / X_BOXES
    maximum = None
    maximum_index = None
    failures = []
    certified_boxes = 0
    unresolved = []
    stack = [
        (endpoint + index * width, endpoint + (index + 1) * width, 0, index)
        for index in range(START_BOX, X_BOXES)
    ]
    while stack:
        left, right, depth, index = stack.pop()
        x = interval(left, right)
        value = quotient_away_from_zero(x)
        if not value.is_finite():
            failures.append(index)
            continue
        upper = value.upper()
        if upper < D44.lower():
            certified_boxes += 1
            if maximum is None or upper > maximum:
                maximum = upper
                maximum_index = index
        elif depth < MAX_DEPTH:
            middle = (left + right) / 2
            stack.append((left, middle, depth + 1, index))
            stack.append((middle, right, depth + 1, index))
        else:
            unresolved.append((left, right, upper, index))
    print("schema=marici.burnol-odd-schur-acb.v1")
    print(f"precision={PRECISION} x_boxes={X_BOXES} start_box={START_BOX}")
    print(f"maximum_upper={maximum}")
    print(f"maximum_index={maximum_index}")
    print(f"d44_lower={D44.lower()}")
    print(f"margin_away_from_zero={D44.lower()-maximum}")
    print(f"failures={failures[:20]} count={len(failures)}")
    print(f"certified_boxes={certified_boxes}")
    print(f"unresolved={unresolved[:10]} count={len(unresolved)}")
    print(f"endpoint=[0,{endpoint}] value={endpoint_value}")
    endpoint_certified = endpoint_value.upper() < D44.lower()
    print(f"endpoint_certified={endpoint_certified}")
    constant_rayleigh = constant_b_rayleigh()
    print(f"constant_b_rayleigh={constant_rayleigh}")
    print(f"constant_direction_negative={(constant_rayleigh-D44).lower() > 0}")
    print(
        f"away_from_zero_certified={not failures and not unresolved and endpoint_certified}"
    )


if __name__ == "__main__":
    main()
