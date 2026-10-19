"""Distinct endpoint roles and the inherited partial index observer.

No physical vertex/state identification or numerical response map is derived.
"""
from contextlib import redirect_stdout
from dataclasses import dataclass
from functools import lru_cache
import io
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[2]
CHECKERS = ROOT / 'research/nima/checkers'


@lru_cache(maxsize=1)
def source_table():
    # The inspected rung/shared-leg/biclique modules write no artifacts.
    previous_path = list(sys.path)
    try:
        sys.path.insert(0, str(CHECKERS))
        with redirect_stdout(io.StringIO()):
            source = runpy.run_path(str(CHECKERS / 'check_rung_transport_diagram.py'))
    finally:
        sys.path[:] = previous_path
    return source


@dataclass(frozen=True)
class AssemblyView:
    parent: object
    path: tuple
    source: tuple = ('assembly', 'A')
    target: tuple = ('assembly', 'B')

    @property
    def label(self):
        return self.parent.label

    @property
    def value(self):
        return self.parent.value

    @property
    def mass(self):
        return self.parent.mass

    @property
    def members(self):
        return (self.parent,)


@dataclass(frozen=True)
class EndpointPacket:
    parent: object
    side: int
    observed_state_key: tuple
    state_record_label: tuple


class MarkedEndpointObserver:
    """Partial discrete metadata observer with parent retention, not a gate."""
    def __init__(self, rows):
        self.rows = tuple(rows)
        self.by_label = {row.label: row for row in self.rows}
        if len(self.by_label) != len(self.rows):
            raise ValueError('duplicate source row label')
        self.states = {row.target: row for row in self.rows if row.target[0] == 's'}

    def observe(self, parent, side):
        if self.by_label.get(parent.label) != parent:
            raise ValueError('foreign or changed parent row')
        if type(side) is not int or side not in (0, 1):
            raise ValueError('side must be source endpoint0 or target endpoint1')
        endpoint = parent.source if side == 0 else parent.target
        if endpoint[0] != 'a':
            raise ValueError('endpoint readout requires an arrow-pair parent')
        if 0 in endpoint[1:]:
            raise ValueError('inherited reference-index0 exclusion')
        key = ('s',) + endpoint[1:]
        if key not in self.states:
            raise ValueError('state index absent from marked table')
        return EndpointPacket(parent, side, key, self.states[key].label)

    def restore_parent(self, packet):
        if self.observe(packet.parent, packet.side) != packet:
            raise ValueError('corrupted endpoint packet')
        return packet.parent

    def state_response(self, packet):
        self.restore_parent(packet)
        raise ValueError('no response-level state transport law supplied')

    def inverse(self, packet):
        self.restore_parent(packet)
        raise ValueError('coarse readout is not an invertible connector')


def assembly_views(source):
    rows = source['source']
    views = []
    ordinal = 0
    for tag, size in (('a', 11), ('s', 4)):
        for i in range(size):
            for j in range(size):
                row = rows[ordinal]
                if row.label != ('leaf', ordinal):
                    raise ValueError('source row ordering changed')
                views.append(AssemblyView(row, (f'{tag}x{i}', f'{tag}y{j}')))
                ordinal += 1
    return tuple(views)
