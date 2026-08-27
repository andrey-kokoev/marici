"""Exact audit of primitive occupancy plus valuation excess."""

from math import exp, log, pi


def occupancy(valuation: int) -> int:
    return int(valuation >= 1)


def excess(valuation: int) -> int:
    return 0 if valuation == 0 else valuation - 1


def main() -> None:
    for valuation in range(10):
        assert occupancy(valuation) + excess(valuation) == valuation

    labels = {
        1: {},
        2: {2: 1},
        6: {2: 1, 3: 1},
        12: {2: 2, 3: 1},
        72: {2: 3, 3: 2},
    }
    u = 0.4
    density = 2.0 * exp(-pi * u * u)
    for label, valuations in labels.items():
        coefficient = sum(power * log(prime) for prime, power in valuations.items())
        assert abs(coefficient - log(label)) < 1e-14
        energy = density * coefficient
        assert (energy == 0.0) == (label == 1)

    print("primitive_front_coefficient=occupancy")
    print("excess_front_coefficient=valuation_minus_occupancy")
    print("full_front_coefficient=valuation")
    print("global_coefficient=log(n)")
    print("squarefree_kernel_repaired=true")
    print("remaining_kernel=vacuum_n_equals_1")
    print("next_gate=vacuum_transversality")


if __name__ == "__main__":
    main()
