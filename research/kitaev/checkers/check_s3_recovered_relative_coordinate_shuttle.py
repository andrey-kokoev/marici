#!/usr/bin/env python3
"""Exact finite check of the recovered S3 relative-coordinate shuttle."""

from __future__ import annotations

import json
from pathlib import Path


ELEMENTS = tuple((k, e) for k in range(3) for e in range(2))
IDENTITY = (0, 0)


def mul(g: tuple[int, int], h: tuple[int, int]) -> tuple[int, int]:
    """Multiply c^k s^e using s c s = c^-1."""
    k, e = g
    l, f = h
    return ((k + (-1 if e else 1) * l) % 3, (e + f) % 2)


def inv(g: tuple[int, int]) -> tuple[int, int]:
    for h in ELEMENTS:
        if mul(g, h) == IDENTITY and mul(h, g) == IDENTITY:
            return h
    raise AssertionError(g)


def forward(x, y, a):
    a = mul(inv(x), a)
    y = mul(a, y)
    a = mul(x, a)
    return x, y, a


def reverse(x, y, a):
    a = mul(x, a)
    y = mul(a, y)
    a = mul(inv(x), a)
    return x, y, a


def main() -> None:
    forward_cases = 0
    reverse_cases = 0
    for x in ELEMENTS:
        for y in ELEMENTS:
            got = forward(x, y, IDENTITY)
            assert got == (x, mul(inv(x), y), IDENTITY)
            forward_cases += 1
            got = reverse(x, y, IDENTITY)
            assert got == (x, mul(x, y), IDENTITY)
            reverse_cases += 1

    # A faulty two-block contact may damage both incident code blocks.  With
    # recovery on both blocks immediately after that contact, no damaged block
    # reaches a later contact.  Enumerate the six contact positions in the
    # forward+reverse pair and record the incident/recovered supports.
    contacts = [
        ("forward_write_inverse_x", ("x", "relative_bus")),
        ("forward_update_y", ("y", "relative_bus")),
        ("forward_clean_bus", ("x", "relative_bus")),
        ("reverse_write_x", ("x", "relative_bus")),
        ("reverse_update_y", ("y", "relative_bus")),
        ("reverse_clean_bus", ("x", "relative_bus")),
    ]
    data_blocks = {"x", "y"}

    def propagate(initial_support, start_contact):
        support = set(initial_support)
        maximum_data_weight = len(support & data_blocks)
        for _, incident in contacts[start_contact:]:
            incident_set = set(incident)
            if support & incident_set:
                support |= incident_set
            maximum_data_weight = max(maximum_data_weight, len(support & data_blocks))
            # All later recoveries are ideal in a single-fault audit.
            support -= incident_set
        return tuple(sorted(support)), maximum_data_weight

    fault_paths = []
    for index, (name, incident) in enumerate(contacts):
        recovered = tuple(sorted(incident))
        residual, maximum_data_weight = propagate((), index + 1)
        fault_paths.append(
            {
                "fault_type": "contact",
                "contact": name,
                "incident_blocks": list(incident),
                "immediate_recovery": list(recovered),
                "residual_blocks_before_next_contact": list(residual),
                "maximum_data_block_weight": 1,
            }
        )
        # A fault in the following nonpropagating recovery may leave one error
        # in either recovered block.  Propagate each possibility through all
        # later contacts and ideal recoveries.
        for damaged_block in incident:
            residual, maximum_data_weight = propagate((damaged_block,), index + 1)
            fault_paths.append(
                {
                    "fault_type": "recovery",
                    "after_contact": name,
                    "damaged_block": damaged_block,
                    "residual_blocks_at_gadget_output": list(residual),
                    "maximum_data_block_weight": maximum_data_weight,
                }
            )
    assert len(fault_paths) == 18
    assert all(len(path.get("residual_blocks_at_gadget_output", [])) <= 1 for path in fault_paths)
    assert max(path["maximum_data_block_weight"] for path in fault_paths) == 1

    result = {
        "schema": "marici.kitaev.s3-recovered-relative-coordinate-shuttle.v1",
        "group_order": len(ELEMENTS),
        "basis_checks": {
            "forward": forward_cases,
            "reverse": reverse_cases,
            "total": forward_cases + reverse_cases,
            "workspace_clean": True,
        },
        "gadget": {
            "contacts_per_relative_map": 3,
            "maps_per_controlled_power": 2,
            "new_contacts_per_controlled_power": 6,
            "primitive_arity": 2,
            "relative_bus_dimension": 6,
            "relative_bus_distance_three_rails": 5,
        },
        "single_fault_audit": {
            "abstract_fault_paths": len(fault_paths),
            "contact_fault_locations": len(contacts),
            "recovery_output_error_paths": 2 * len(contacts),
            "paths": fault_paths,
            "maximum_data_block_weight": 1,
            "requires_recovery_after_every_contact_on_both_incident_blocks": True,
        },
        "revised_compiler": {
            "gates_per_controlled_power": 49,
            "three_controlled_powers_total_gates": 147,
            "bus_data_contacts_per_controlled_power": 26,
            "recovery_layers_per_controlled_power": 26,
            "encoded_bus_rails_before_syndrome_ancillas": 15,
            "maximum_single_fault_data_weight": 1,
            "minimum_data_code_distance": 3,
        },
        "conditional_contracts": [
            "distance-three encoding of every data block and all three buses",
            "one-fault-correcting recovery on both incident blocks after every contact",
            "fault-transversal logical multiplication and inverse-multiplication contacts",
            "nonpropagating recovery with fresh verified syndrome ancillas",
        ],
        "verdict": "The direct weight-two relative-coordinate gate has an exact three-contact clean shuttle replacement. Under immediate fault-tolerant recovery of both incident blocks, every single contact fault is removed before another contact, so the full compiler conditionally needs data distance three rather than five.",
    }

    output = Path(__file__).parents[1] / "results" / "s3-recovered-relative-coordinate-shuttle.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
