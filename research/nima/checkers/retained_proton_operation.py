"""Conditional stateful interface for the six already-bound proton requests.

Geometry, spin and exchange remain separate readings. History records request
order, not fresh physical event IDs. Electron exchange is deliberately unbound.
"""
from dataclasses import dataclass
import sympy as S
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'voevodsky/checkers'))
from check_proton_electron_contact_binding import I, act, adj, decode_matrix


@dataclass(frozen=True)
class State:
    geometric: int
    spin: tuple
    mismatch: tuple
    anchor: tuple


@dataclass(frozen=True)
class Execution:
    initial: State
    final: State
    requests: tuple


@dataclass(frozen=True)
class RetainedExecution:
    lift_signs: tuple
    initial: State
    path_record: object


class RetainedProtonOperation:
    def __init__(self, binding, lift_signs):
        if len(lift_signs) != 2 or any(sign not in ('+I', '-I') for sign in lift_signs):
            raise ValueError('Choose a third-power sign for each proton generator')
        self.signs = tuple(lift_signs)
        self.q = binding['quotient']
        self.encoder, self.decoder = binding['encoder'], binding['decoder']
        self.updates = binding['updates']
        self.spin_actions = {}
        for row in binding['spin_variants']:
            if row['third_power'] == self.signs[row['generator']]:
                for label in row['arrows']:
                    self.spin_actions[label] = decode_matrix(row['logical_action'])
        initial = (('A', 'E'), binding['phase']['initial'])
        self.root = self.q.states.index(initial)

    def prepare(self, spin, exchange):
        if len(spin) != 2 or len(exchange) != 22:
            raise ValueError('Expected logical doublet and 22 exchange coordinates')
        encoded = self.encoder*S.Matrix(exchange)
        return State(self.root, tuple(spin), tuple(encoded[16:]), tuple(encoded[:16]))

    def _validate(self, state):
        self.q.observe(state.geometric)
        if len(state.spin) != 2 or len(state.mismatch) != 6 or len(state.anchor) != 16:
            raise ValueError('Malformed state dimensions')

    def _label(self, action):
        if action not in self.q.actions or action[0] != 'proton':
            raise ValueError('Only the six proton requests have an exchange binding')
        return ''.join(action[2:])

    def step(self, state, action):
        self._validate(state)
        label = self._label(action)
        target = self.q.step(state.geometric, action)
        return State(target, act(self.spin_actions[label], state.spin),
                     tuple(self.updates[label]*S.Matrix(state.mismatch)), state.anchor)

    def execute(self, initial, requests):
        self._validate(initial)
        current = initial
        requests = tuple(requests)
        for action in requests:
            current = self.step(current, action)
        return Execution(initial, current, requests)

    def recover(self, execution):
        # Validate forward record before using numerical inverse operations.
        if self.execute(execution.initial, execution.requests) != execution:
            raise ValueError('Altered execution')
        spin, delta = execution.final.spin, S.Matrix(execution.final.mismatch)
        for action in reversed(execution.requests):
            label = self._label(action)
            spin = act(adj(self.spin_actions[label]), spin)
            delta = self.updates[label]*delta
        recovered = State(execution.initial.geometric, spin, tuple(delta), execution.final.anchor)
        if recovered != execution.initial:
            raise ValueError('Inverse failed')
        return recovered

    def exchange_state(self, state):
        self._validate(state)
        return tuple(self.decoder*S.Matrix(state.anchor + state.mismatch))

    def observe(self, state):
        self._validate(state)
        return {'geometry': self.q.observe(state.geometric), 'spin': state.spin,
                'mismatch': state.mismatch, 'anchor': state.anchor}

    def retain(self, execution, policy):
        if execution.initial.geometric != self.root or not execution.requests:
            raise ValueError('Rung binding requires a nonempty history from (A,E)')
        if self.execute(execution.initial, execution.requests) != execution:
            raise ValueError('Altered execution')
        endpoint = ('A', 'E')
        history = ()
        for action in execution.requests:
            edge = next(edge for (edge,) in self.q.bridge['frame']
                        if edge[0] == endpoint and edge[2] == action)
            history += (edge,)
            endpoint = edge[1]
        return RetainedExecution(self.signs, execution.initial, self.q.retain(history, policy))

    def restore(self, retained):
        if retained.lift_signs != self.signs or retained.initial.geometric != self.root:
            raise ValueError('Foreign lift policy or initial state')
        history = self.q.restore(retained.path_record)
        return self.execute(retained.initial, tuple(edge[2] for edge in history))

    def advance_rung(self, retained, action, policy):
        execution = self.restore(retained)
        return self.retain(self.execute(execution.initial, execution.requests + (action,)), policy)
