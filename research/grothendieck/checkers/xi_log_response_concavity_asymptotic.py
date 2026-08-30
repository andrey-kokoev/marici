"""Exact-decimal audit of the coarse s>=100 concavity reduction.

The analytic input proved in the accompanying note is
  v >= 2/(5s),  a <= log(s),  (yv)' <= 3/s^2.
The displayed function is then a lower bound for D.
"""

from decimal import Decimal, ROUND_FLOOR, localcontext


def lower_bound(s: Decimal) -> Decimal:
    with localcontext() as context:
        context.prec = 70
        context.rounding = ROUND_FLOOR
        return (
            Decimal(4) / Decimal(25) * (Decimal(1) - Decimal(1) / (Decimal(2) * s)) ** 2
            - Decimal(3) * s.ln() / s
        )


def main() -> None:
    endpoint = lower_bound(Decimal(100))
    print(f"D_lower_at_s_100={endpoint}")
    print("monotonicity=first term increases; log(s)/s decreases for s>e")
    print(f"certified={endpoint > 0}")


if __name__ == "__main__":
    main()
