"""Explicit conditional binding of a retained reference to fixture boundaries.

The source operator representation is reused. Boundary identifications and
port frames are supplied, not physical/source-derived geometry. Mismatches
are rejected, never rescaled to fit the software reference.
"""
from dataclasses import dataclass
from retained_reference_protocol import inverse_operator


@dataclass(frozen=True)
class BoundaryIdentification:
    source: str
    target: str
    operator_space: str
    source_to_operator: tuple
    target_to_operator: tuple
    provenance: tuple


@dataclass(frozen=True)
class BoundReference:
    reference: tuple
    inverse: tuple
    boundary: BoundaryIdentification
    source_value: tuple
    source_operator: tuple
    readout_mode: str
    readout_policy: str
    depth: int
    events: tuple
    preparation: tuple
    input_carrier: tuple
    input_bank: tuple

    def attach(self, row, frames, flat):
        source, target = frames[row.source], frames[row.target]
        actual = flat['chain'](target, self.inverse, row.value, flat['inverse'](source))
        reference = flat['chain'](target, flat['inverse'](source))
        return actual, reference, flat['inverse'](reference)

    def decode(self, actual, source, target, frames, flat):
        return flat['chain'](self.reference, flat['inverse'](frames[target]), actual, frames[source])


def bind(protocol, mode, boundary, flat, readout_policy='normalized'):
    if (boundary.source, boundary.target) != ('A', 'B'):
        raise ValueError('Expected the declared shared-leg comparison boundary A->B')
    if not boundary.operator_space or not boundary.provenance:
        raise ValueError('Boundary space and identification provenance required')
    record = protocol.interrogate(mode, readout_policy)
    initial = protocol.recover_initial()
    # Both boundary maps must be identifications, even though only the
    # target's inverse occurs in the expression below.
    inverse_operator(boundary.source_to_operator)
    target_inverse = inverse_operator(boundary.target_to_operator)
    reference = flat['chain'](target_inverse, record['operator'], boundary.source_to_operator)
    ret = inverse_operator(reference)
    if reference != flat['d'] or ret != flat['r']:
        raise ValueError('Interrogated/bound reference differs from pinned fixture; rescaling is forbidden')
    return BoundReference(reference, ret, boundary, record['value'], record['operator'],
                          mode, record['readout_policy'], record['depth'], record['events'], record['preparation'],
                          initial.carrier, initial.record)
