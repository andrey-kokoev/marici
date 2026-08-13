"""Vertex-local certificate for the all-arity QTDS contact theorem.

For a quartic vertex with consecutive odd momentum blocks A,B,C,D, write
its boundary indices as a<b<c<d.  In formal planar variables,

    V_+ = X_ac + X_bd - X_ad - X_bc,
    V_- = X_ac + X_bd - X_ab - X_cd.

The positive terms are the two scalar diagonals of the quadrilateral.  The
negative physical sides are exactly those dual edges directed out of that
cell by the alternating coorientation.

Consequently an entire QTDS diagram can cancel every propagator iff its
directed dual tree has a unique sink.  Every non-sink vertex then supplies
its unique outgoing propagator and the sink supplies either scalar diagonal.
Including the global diagram convention, every contact coefficient is -1.

This script checks the local identities and geometric typing on every
quartic presentation through fourteen points.  The proof itself is the
displayed kinematic identity plus the elementary oriented-tree argument.
"""

from __future__ import annotations

from collections import defaultdict
from functools import lru_cache

from check_eight_point_transfer import planar_symbolic_kinematics
from check_j_reconstruction import triangulations
from check_qtds_lift import momentum_dot, odd_three_splits
from check_scalar_catalan_map import (
    alternating_coorientation,
    cell_side,
    physical_core,
    quadrangulation_cells,
)


Order = tuple[int, ...]
Cell = tuple[int, int, int, int]
Diagonal = tuple[int, int]
VertexRecord = tuple[Cell, tuple[Diagonal, Diagonal], bool]


def local_vertex_identity_audit(multiplicity: int) -> int:
    """Check both planar-variable vertex identities on every odd split."""

    _, variables, kinematics = planar_symbolic_kinematics(
        multiplicity
    )
    polynomial_type = type(next(iter(variables.values())))
    zero = polynomial_type.constant(0)

    def planar(first: int, second: int):
        if first == second or second - first in (
            1,
            multiplicity - 1,
        ):
            return zero
        return variables[(first, second)]

    check_count = 0
    for first in range(multiplicity - 1):
        for size in range(3, multiplicity - first, 2):
            block = tuple(range(first, first + size))
            for first_size, second_size, _ in odd_three_splits(
                size
            ):
                second = first + first_size
                third = second + second_size
                fourth = first + size
                first_block = tuple(range(first, second))
                second_block = tuple(range(second, third))
                third_block = tuple(range(third, fourth))

                plus_actual = -2 * momentum_dot(
                    first_block, third_block, kinematics
                )
                plus_expected = (
                    planar(first, third)
                    + planar(second, fourth)
                    - planar(first, fourth)
                    - planar(second, third)
                )
                assert plus_actual == plus_expected

                minus_actual = 2 * momentum_dot(
                    block, second_block, kinematics
                )
                minus_expected = (
                    planar(first, third)
                    + planar(second, fourth)
                    - planar(first, second)
                    - planar(third, fourth)
                )
                assert minus_actual == minus_expected
                check_count += 2
    return check_count


def presentation_records(
    multiplicity: int, *, first_is_plus: bool
) -> tuple[tuple[tuple[Order, ...], tuple[VertexRecord, ...]], ...]:
    """All rooted QTDS presentations with their vertex-local metadata."""

    @lru_cache(None)
    def current(block: Order, starts_plus: bool):
        if len(block) == 1:
            return (((), ()),)
        return tuple(
            ((block,) + propagators, records)
            for propagators, records in vertex(
                block, starts_plus
            )
        )

    @lru_cache(None)
    def vertex(block: Order, starts_plus: bool):
        result = []
        first = block[0]
        for first_size, second_size, _ in odd_three_splits(
            len(block)
        ):
            second = first + first_size
            third = second + second_size
            fourth = first + len(block)
            subblocks = (
                block[:first_size],
                block[first_size : first_size + second_size],
                block[first_size + second_size :],
            )
            subpolarities = (
                starts_plus,
                not starts_plus,
                starts_plus,
            )
            negative_sides = (
                ((first, fourth), (second, third))
                if starts_plus
                else ((first, second), (third, fourth))
            )
            record: VertexRecord = (
                (first, second, third, fourth),
                negative_sides,
                starts_plus,
            )
            for first_data in current(
                subblocks[0], subpolarities[0]
            ):
                for second_data in current(
                    subblocks[1], subpolarities[1]
                ):
                    for third_data in current(
                        subblocks[2], subpolarities[2]
                    ):
                        propagators = (
                            first_data[0]
                            + second_data[0]
                            + third_data[0]
                        )
                        records = (
                            (record,)
                            + first_data[1]
                            + second_data[1]
                            + third_data[1]
                        )
                        result.append((propagators, records))
        return tuple(result)

    return vertex(
        tuple(range(multiplicity - 1)), first_is_plus
    )


def orientation_typing_audit(
    multiplicity: int, *, first_is_plus: bool
) -> tuple[int, int, int]:
    """Type every negative vertex side as one outgoing dual edge."""

    core_size = multiplicity // 2 - 2
    full_cores = {
        core
        for triangulation in triangulations(
            tuple(range(multiplicity))
        )
        if len(core := physical_core(triangulation))
        == core_size
    }
    presentations = presentation_records(
        multiplicity, first_is_plus=first_is_plus
    )
    assert len(presentations) == len(full_cores)

    unique_sink_count = 0
    contact_count = 0
    seen_cores = set()
    for propagators, records in presentations:
        quadrangulation = tuple(
            sorted(
                (block[0], block[-1] + 1)
                for block in propagators
            )
        )
        assert quadrangulation in full_cores
        assert quadrangulation not in seen_cores
        seen_cores.add(quadrangulation)
        cells = quadrangulation_cells(
            quadrangulation, multiplicity
        )
        assert {record[0] for record in records} == set(cells)

        outgoing = defaultdict(set)
        for diagonal in quadrangulation:
            adjacent = tuple(
                cell
                for cell in cells
                if set(diagonal) <= set(cell)
            )
            assert len(adjacent) == 2
            target_side = alternating_coorientation(
                diagonal, first_is_plus=first_is_plus
            )
            target = next(
                cell
                for cell in adjacent
                if cell_side(diagonal, cell) == target_side
            )
            source = next(
                cell for cell in adjacent if cell != target
            )
            outgoing[source].add(diagonal)

        for cell, negative_sides, _ in records:
            assert (
                set(negative_sides) & set(quadrangulation)
                == outgoing[cell]
            )

        sinks = tuple(
            cell for cell in cells if not outgoing[cell]
        )
        if len(sinks) == 1:
            # A tree with one sink has outdegree one at every other
            # vertex, so every propagator can be selected once.
            assert all(
                len(outgoing[cell]) == 1
                for cell in cells
                if cell != sinks[0]
            )
            unique_sink_count += 1
            contact_count += 2
        else:
            # With more than one sink, the v-1 outgoing incidences force
            # some vertex to have outdegree at least two.  Its linear
            # numerator cannot cancel both propagators.
            assert any(
                len(outgoing[cell]) >= 2 for cell in cells
            )

    assert seen_cores == full_cores
    return len(presentations), unique_sink_count, contact_count


def main() -> None:
    for multiplicity in (6, 8, 10, 12, 14):
        local_checks = local_vertex_identity_audit(multiplicity)
        polarity_results = tuple(
            orientation_typing_audit(
                multiplicity, first_is_plus=polarity
            )
            for polarity in (True, False)
        )
        assert polarity_results[0] == polarity_results[1]
        diagrams, unique_sinks, contacts = polarity_results[0]
        print(
            f"n={multiplicity} vertex cancellation: "
            f"{local_checks} local identities, {diagrams} diagrams, "
            f"{unique_sinks} unique sinks, and {contacts} contacts "
            "per polarity"
        )
    print(
        "all vertex-local QTDS cancellation checks through fourteen "
        "points passed"
    )


if __name__ == "__main__":
    main()
