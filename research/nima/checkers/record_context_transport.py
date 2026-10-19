"""Typed separation of existing comparison transport and context creation.

Connector admission is explicit caller-supplied mathematical data, NOT physical
or publication authority. An available matrix does not imply an admitted edge.
Matrix operations and port attachments are supplied by the existing fixture.
"""
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Connector:
    label: str
    source: tuple
    target: tuple
    value: tuple
    provenance: tuple


@dataclass(frozen=True)
class Composition:
    source: tuple
    target: tuple
    actual: tuple
    decoded: tuple
    operands: tuple
    connector: Connector | None


class ContextTransport:
    def __init__(self, flat):
        self.flat = flat
        self.connectors = {}

    def declare(self, connector):
        """Retain an explicit connector declaration; no all-pairs defaults."""
        if not connector.label or not connector.provenance:
            raise ValueError('Connector needs a label and retained provenance')
        if connector.label in self.connectors:
            raise ValueError('Connector label already declared')
        if connector.source not in self.flat['frames'] or connector.target not in self.flat['frames']:
            raise ValueError('Unknown connector port')
        self.flat['inverse'](connector.value)  # invertible stratum only
        self.connectors[connector.label] = connector

    def compose(self, left: Any, right: Any, connector_label=None):
        """Chronological left, connector if supplied, return_right, right.

        The map is right * return_right * connector * left. Its endpoints are
        left.source -> right.target. No connector is inferred from flat frames.
        """
        connector = None
        if connector_label is None:
            if left.target != right.target:
                raise ValueError('Cross-target composition needs a declared connector')
            bridge = self.flat['I']
        else:
            if connector_label not in self.connectors:
                raise ValueError('Undeclared connector')
            connector = self.connectors[connector_label]
            if (connector.source, connector.target) != (left.target, right.target):
                raise ValueError('Connector endpoints do not match operand targets')
            bridge = connector.value
        left_value, _, _ = self.flat['realization'](left, self.flat['frames'])
        right_value, _, right_return = self.flat['realization'](right, self.flat['frames'])
        actual = self.flat['chain'](right_value, right_return, bridge, left_value)
        decoded = self.flat['decode'](actual, left.source, right.target, self.flat['frames'])
        return Composition(left.source, right.target, actual, decoded,
                           (left.label, right.label), connector)


def T9_exact_domain(rows, fixture):
    """Existing inherited-key candidate, guarded by exact context reflection."""
    middle = fixture['incoming_promotion'](rows, 1, 'inherited')
    old_to_new = {}
    new_to_old = {}
    for family in middle:
        old = family.members[0].target
        if any(member.target != old for member in family.members):
            raise ValueError('Incoming family has inconsistent grouping endpoints')
        if old in old_to_new and old_to_new[old] != family.target:
            raise ValueError('Original fibre split')
        if family.target in new_to_old and new_to_old[family.target] != old:
            raise ValueError('Original fibres merged')
        old_to_new[old] = family.target
        new_to_old[family.target] = old
    return fixture['incoming_promotion'](middle, 2, 'inherited')
