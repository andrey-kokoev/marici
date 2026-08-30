#!/usr/bin/env python3
"""Exact two-label separation of scalar nullity and exclusion curvature."""


def main():
    c = (1, -1)
    scalar = c[0] + c[1]
    prime_two_exclusion = (c[0], 0)
    prime_three_exclusion = c
    energy_two = sum(value * value for value in prime_two_exclusion)
    energy_three = sum(value * value for value in prime_three_exclusion)

    assert scalar == 0
    assert energy_two == 1
    assert energy_three == 2
    assert energy_two + energy_three == 3

    print("scalar_aggregation=null")
    print("prime_two_exclusion_energy=1")
    print("prime_three_exclusion_energy=2")
    print("missing_rung=zero_state_to_curvature_nullity_Ward_cell")


if __name__ == "__main__":
    main()

