"""Exact audit of valuation excess times oriented Gaussian density."""

from math import exp, log, pi


def valuation_excess(valuation: int) -> int:
    return 0 if valuation == 0 else valuation - 1


def energy(prime: int, valuation: int, u: float) -> float:
    return 2.0 * log(prime) * valuation_excess(valuation) * exp(-pi * u * u)


def main() -> None:
    for prime in (2, 3, 5, 43):
        for valuation in range(8):
            for u in (-3.0, -0.5, 0.0, 0.5, 3.0):
                value = energy(prime, valuation, u)
                assert value >= 0.0
                assert (value == 0.0) == (valuation in (0, 1))

    print("coupled_bulk_nonnegative=true")
    print("strict_support=valuation_at_least_2")
    print("global_kernel=squarefree_sector")
    print("coefficient=2*(r-1)*log(p)")
    print("density=exp(-pi*u^2)")
    print("remaining_gate=squarefree_transversality")


if __name__ == "__main__":
    main()
