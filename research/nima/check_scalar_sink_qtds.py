"""Exact QTDS verification of the direct scalar sink map through 14 points.

For each even arity, the expected contact table is built first from the
target-independent alternating unique-sink rule.  The script then expands
every QTDS quartic tree in formal planar kinematics and compares diagram,
marked scalar diagonal, and coefficient.
"""

from __future__ import annotations

from collections import Counter

from check_eight_point_transfer import (
    negative_support,
    planar_symbolic_kinematics,
    select_terms,
)
from check_j_reconstruction import canonical_channel, triangulations
from check_qtds_lift import qtds_raw_terms
from check_scalar_catalan_map import (
    fuss_catalan_quadrangulations,
    physical_core,
    sink_contact_slots,
)


def physical_diagonals(multiplicity: int):
    """All physical diagonals in the fixed cyclic ordering."""

    return tuple(
        diagonal
        for diagonal in (
            (first, second)
            for first in range(multiplicity)
            for second in range(first + 1, multiplicity)
        )
        if (diagonal[1] - diagonal[0])
        not in (1, multiplicity - 1)
        and (diagonal[0] - diagonal[1]) % 2
    )


def full_cores(multiplicity: int):
    """All quadrangulation cores derived from scalar triangulations."""

    core_size = multiplicity // 2 - 2
    result = tuple(
        sorted(
            {
                core
                for triangulation in triangulations(
                    tuple(range(multiplicity))
                )
                if len(
                    core := physical_core(triangulation)
                )
                == core_size
            }
        )
    )
    assert len(result) == fuss_catalan_quadrangulations(
        multiplicity
    )
    return result


def scalar_zero_core_coefficients(multiplicity: int):
    """Marked leading-grade coefficients of all zero-core scalar cells."""

    result = {}
    zero_core_cells = tuple(
        triangulation
        for triangulation in triangulations(
            tuple(range(multiplicity))
        )
        if not physical_core(triangulation)
    )
    for triangulation in zero_core_cells:
        shift_signs = {
            diagonal: (1 if diagonal[0] % 2 else -1)
            for diagonal in triangulation
        }
        base_sign = 1
        for sign in shift_signs.values():
            base_sign *= sign
        for mark, sign in shift_signs.items():
            result[(triangulation, mark)] = -base_sign * sign
    assert set(result.values()) == {-1}
    return result


def scalar_sink_coefficients(
    multiplicity: int, *, first_is_plus: bool
):
    """Target-independent scalar-derived contact occurrence table."""

    result = {}
    for quadrangulation in full_cores(multiplicity):
        for mark in sink_contact_slots(
            quadrangulation,
            multiplicity,
            first_is_plus=first_is_plus,
        ):
            result[(quadrangulation, mark)] = -1
    return result


def qtds_contact_coefficients(
    multiplicity: int, *, first_is_plus: bool
):
    """Polynomial contacts of the independent symbolic QTDS recursion."""

    diagonals, variables, kinematics = planar_symbolic_kinematics(
        multiplicity
    )
    polynomial_type = type(next(iter(variables.values())))
    channel_to_diagonal = {}
    for diagonal in physical_diagonals(multiplicity):
        start, end = diagonal
        channel = canonical_channel(
            tuple(range(start, end)), multiplicity
        )
        assert channel not in channel_to_diagonal
        channel_to_diagonal[channel] = diagonal

    result = {}
    diagram_cores = set()
    convention_sign = (-1) ** (multiplicity // 2 - 1)
    for numerator, propagators in qtds_raw_terms(
        tuple(range(multiplicity)),
        kinematics,
        first_is_plus=first_is_plus,
    ):
        assert len(propagators) == multiplicity // 2 - 2
        denominator = polynomial_type.constant(1)
        diagram_diagonals = []
        for block in propagators:
            diagonal = channel_to_diagonal[
                canonical_channel(block, multiplicity)
            ]
            diagram_diagonals.append(diagonal)
            denominator *= variables[diagonal]
        quadrangulation = tuple(sorted(diagram_diagonals))
        assert quadrangulation not in diagram_cores
        diagram_cores.add(quadrangulation)
        diagram = convention_sign * numerator / denominator
        contact = select_terms(
            diagram, lambda powers: not negative_support(powers)
        )
        for powers, coefficient in contact.terms.items():
            support = tuple(
                index
                for index, exponent in enumerate(powers)
                if exponent
            )
            assert len(support) == 1
            assert powers[support[0]] == 1
            key = (quadrangulation, diagonals[support[0]])
            assert key not in result
            result[key] = coefficient

    assert diagram_cores == set(full_cores(multiplicity))
    assert set(result.values()) == {-1}
    return result


def multiplicity_audit(multiplicity: int):
    """Compare the scalar and QTDS contact tables at one arity."""

    source = scalar_zero_core_coefficients(multiplicity)
    source_multiplicity = Counter(mark for _, mark in source)
    contact_count = None
    for polarity in (True, False):
        scalar = scalar_sink_coefficients(
            multiplicity, first_is_plus=polarity
        )
        qtds = qtds_contact_coefficients(
            multiplicity, first_is_plus=polarity
        )
        assert scalar == qtds
        assert Counter(mark for _, mark in scalar) == source_multiplicity
        contact_count = len(scalar)
    return (
        len(full_cores(multiplicity)),
        len(source),
        contact_count,
    )


def main() -> None:
    for multiplicity in (6, 8, 10, 12, 14):
        diagram_count, source_count, contact_count = multiplicity_audit(
            multiplicity
        )
        assert source_count == contact_count
        print(
            f"n={multiplicity} scalar/QTDS contacts: "
            f"{diagram_count} diagrams and {contact_count} exact "
            "coefficient -1 sink occurrences for each polarity"
        )
    print(
        "all exact scalar-sink/QTDS checks through fourteen points passed"
    )


if __name__ == "__main__":
    main()
