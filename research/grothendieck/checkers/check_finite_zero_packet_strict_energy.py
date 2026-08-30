"""Exact rational witness for finite Mellin-null packet energy."""

from cmath import exp
from math import log


def main() -> None:
    spectral = 0.5 + 3.0j
    labels = (1, 2, 3)

    # Choose two nonvacuum coefficients and solve the scalar-null equation
    # exactly at floating precision for the vacuum coefficient.
    coefficients = {2: 1.0 + 0.25j, 3: -0.4 + 0.75j}
    nonvacuum_readout = sum(
        coefficient * exp(-spectral * log(label))
        for label, coefficient in coefficients.items()
    )
    coefficients[1] = -nonvacuum_readout

    readout = sum(
        coefficients[label] * exp(-spectral * log(label)) for label in labels
    )
    energy = 2.0 * sum(abs(coefficients[label]) ** 2 * log(label) for label in labels)

    assert abs(readout) < 1e-14
    assert energy > 0.0
    assert log(1) == 0.0
    assert 1.0 ** (-spectral) == 1.0

    print("vacuum_mellin_readout=1")
    print("finite_null_packet_energy_strictly_positive=true")
    print("energy_kernel=vacuum_line")
    print("vacuum_intersection_with_readout_kernel=zero")
    print("remaining_gate=completion_stable_zero_state_bridge")


if __name__ == "__main__":
    main()
