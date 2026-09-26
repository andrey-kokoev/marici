"""Tree-port flattening prototype. Rewrites inspect one principal-principal pair."""
from dataclasses import dataclass
from copy import copy
from admission import validate as admit
from reference import Admission, Seed, Step

@dataclass(frozen=True)
class Agent:
    kind: str
    payload: object
    arity: int
    level: int

class Net:
    def __init__(self, history):
        if history.level < 1:
            raise ValueError('a flattening net requires nested resolution seeds')
        self.agents = {}
        self.wires = {}
        self.next_id = 1
        root = self.compile(history)
        f = self.allocate(Agent('flatten', None, 1, history.level))
        self.connect((f, 0), root)
        self.connect((0, 0), (f, 1))  # unique external result port
        self.validate()

    def allocate(self, agent):
        i = self.next_id
        self.next_id += 1
        self.agents[i] = agent
        return i

    def connect(self, a, b):
        if a == b or a in self.wires or b in self.wires:
            raise ValueError('wire requires two distinct unoccupied ports')
        self.wires[a] = b
        self.wires[b] = a

    def compile(self, history):
        # Compilation copies occurrences, not graph aliases. No runtime copier.
        if isinstance(history, Seed):
            nested = not isinstance(history.evidence, Admission)
            i = self.allocate(Agent('seed', history.evidence if not nested else history.package,
                                    int(nested), history.level))
            if nested:
                self.connect((i, 1), self.compile(history.evidence))
        else:
            i = self.allocate(Agent('step', history.rule, len(history.premises), history.level))
            for slot, premise in enumerate(history.premises, 1):
                self.connect((i, slot), self.compile(premise))
        return (i, 0)

    def active(self):
        pairs = []
        for i, agent in self.agents.items():
            if agent.kind == 'flatten':
                j, slot = self.wires[i, 0]
                if slot == 0 and j and self.agents[j].kind in ('seed', 'step'):
                    pairs.append((i, j))
        return pairs

    def rewrite(self, pair):
        self.validate()
        if type(pair) is not tuple or len(pair) != 2 or not all(type(i) is int for i in pair):
            raise ValueError('invalid active-pair identifier')
        if pair not in self.active():
            raise ValueError('requested pair is not active')
        candidate = copy(self)
        candidate.agents = self.agents.copy()
        candidate.wires = self.wires.copy()
        candidate._rewrite_in_place(pair)
        candidate.validate()
        self.agents, self.wires, self.next_id = candidate.agents, candidate.wires, candidate.next_id

    def _rewrite_in_place(self, pair):
        f, d = pair
        F, D = self.agents[f], self.agents[d]
        if F.kind != 'flatten' or self.wires[f, 0] != (d, 0):
            raise ValueError('not a flatten/data active pair')
        if F.level != D.level or D.level < 1:
            raise ValueError('invalid flattening layer')
        if D.kind not in ('seed', 'step') or (D.kind == 'seed' and D.arity != 1):
            raise ValueError('invalid data signature')
        result = self.wires[f, 1]
        children = [self.wires[d, k] for k in range(1, D.arity + 1)]
        # Cut precisely the active pair and preserve its exterior interface.
        for node in (f, d):
            for k in range(self.agents[node].arity + 1):
                port = (node, k)
                if port in self.wires:
                    peer = self.wires.pop(port)
                    self.wires.pop(peer)
            del self.agents[node]
        if D.kind == 'seed':
            self.connect(result, children[0])
        else:
            rebuilt = self.allocate(Agent('step', D.payload, D.arity, D.level - 1))
            self.connect(result, (rebuilt, 0))
            for k, child in enumerate(children, 1):
                pending = self.allocate(Agent('flatten', None, 1, D.level))
                self.connect((rebuilt, k), (pending, 1))
                self.connect((pending, 0), child)
        self.validate()

    def validate(self):
        return admit(self)

    def readback(self):
        self.validate()
        if any(a.kind == 'flatten' for a in self.agents.values()):
            raise ValueError('normal-form readback only')
        visited = set()
        def read(port):
            i, slot = port
            assert slot == 0 and i not in visited
            visited.add(i);a = self.agents[i]
            if a.kind == 'seed':
                if a.arity == 0:return Seed(a.payload.package, a.payload)
                return Seed(a.payload, read(self.wires[i, 1]))
            return Step(a.payload, tuple(read(self.wires[i, k]) for k in range(1, a.arity + 1)))
        history = read(self.wires[0, 0])
        assert visited == set(self.agents)
        return history
