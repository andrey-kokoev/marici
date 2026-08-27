"""Exact finite witness separating state energy from observer overlap."""

from math import log


def energy(packet: tuple[complex, complex]) -> float:
    weights = (0.0, log(2.0))
    return 2.0 * sum(abs(value) ** 2 * weight for value, weight in zip(packet, weights))


def readout(packet: tuple[complex, complex]) -> complex:
    return sum(packet)


def main() -> None:
    constructive = (1.0 + 0.0j, 1.0 + 0.0j)
    destructive = (1.0 + 0.0j, -1.0 + 0.0j)

    assert energy(constructive) == energy(destructive)
    assert readout(constructive) == 2.0
    assert readout(destructive) == 0.0

    print("equal_magnitudes_equal_interval_energy=true")
    print("constructive_overlap=2")
    print("destructive_overlap=0")
    print("state_norm_controls_overlap=false")
    print("spectral_height_visible_to_energy=false")
    print("next_gate=mixed_source_observer_kernel")


if __name__ == "__main__":
    main()
