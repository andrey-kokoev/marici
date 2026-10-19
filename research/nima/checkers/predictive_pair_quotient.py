"""Finite predictive quotient of the checked actual-pair history adapter.

State IDs are local to this constructed table, not persistent physical labels.
The quotient does not store or reconstruct provenance; retain/restore does.
Only nonempty single histories from the registered (A,E) preparation are bound.
"""
from types import MappingProxyType


class PredictivePairQuotient:
    def __init__(self, binding):
        self.bridge = binding['bridge']
        self.states = tuple(binding['states'])
        self._ids = MappingProxyType({state: i for i, state in enumerate(self.states)})
        self.actions = tuple(self.bridge['registry'])
        self.transitions = tuple(MappingProxyType({action: self._ids[target]
                                 for action, target in binding['transitions'][state].items()})
                                 for state in self.states)
        self.outputs = tuple(binding['outputs'][state] for state in self.states)
        self.witnesses = tuple(binding['witnesses'][state] for state in self.states)
        self._path_state = binding['path_state']

    def _state(self, state):
        if type(state) is not int or not 0 <= state < len(self.states):
            raise ValueError('Unknown predictive state ID')
        return state

    def _path(self, history):
        history = tuple(history)
        if not history:
            raise ValueError('Nonempty history required')
        self.bridge['packet']([history])  # validates primitive IDs, root and seams
        return history

    def project(self, history):
        history = self._path(history)
        key = (history[-1][1], self._path_state(history))
        if key not in self._ids:
            raise ValueError('History outside the closed predictive carrier')
        return self._ids[key]

    def admitted(self, state):
        return tuple(self.transitions[self._state(state)])

    def step(self, state, action):
        table = self.transitions[self._state(state)]
        if action not in table:
            raise ValueError('Request not admitted at predictive state')
        return table[action]

    def observe(self, state):
        return self.outputs[self._state(state)]

    def advance_history(self, history, action):
        history = self._path(history)
        # Use actual contextual path extension, independently of quotient table.
        children = self.bridge['extend'](self.bridge['packet']([history]))
        matches = [p for p in children.paths if p[-1][2] == action]
        if len(matches) != 1:
            raise ValueError('Request not admitted at history endpoint')
        return matches[0]

    def retain(self, history, policy):
        if policy not in ('inherited', 'common'):
            raise ValueError('Unknown rung transport policy')
        history = self._path(history)
        return self.bridge['encode'](self.bridge['packet']([history]), policy)

    def restore(self, retained):
        packet = self.bridge['decode'](retained)
        if len(packet.paths) != 1:
            raise ValueError('Single-history contract requires one path')
        return self._path(packet.paths[0])

    def project_rung(self, retained):
        return self.project(self.restore(retained))

    def observe_rung(self, retained):
        return self.observe(self.project_rung(retained))

    def advance_rung(self, retained, action, policy):
        return self.retain(self.advance_history(self.restore(retained), action), policy)
