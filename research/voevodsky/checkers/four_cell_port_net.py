"""Small attributed interaction net. Exact payload arithmetic is a primitive,
not a finite-alphabet encoding. Observation sums both boundary slots per family.
"""
from copy import deepcopy

ARITY = {'EB': ('p', 'o'), 'FB': ('p', 'o'),
         'REM': ('p', 'o'), 'OUT': ('p',)}

class Net:
    def __init__(self):
        self.nodes = {}
        self.wires = {}
        self.serial = 0

    def add(self, kind, payload=None):
        if kind not in ARITY:
            raise ValueError('unknown agent')
        name = self.serial
        self.serial += 1
        self.nodes[name] = (kind, deepcopy(payload))
        return name

    def link(self, a, b):
        if a == b or a in self.wires or b in self.wires:
            raise ValueError('nonlinear or self-connected port')
        for node, port in (a, b):
            if node not in self.nodes or port not in ARITY[self.nodes[node][0]]:
                raise ValueError('unknown port')
        self.wires[a], self.wires[b] = b, a

    def validate(self):
        ports = {(n, p) for n, (kind, _) in self.nodes.items() for p in ARITY[kind]}
        if ports != set(self.wires):
            raise ValueError('dangling or foreign port')
        for a, b in self.wires.items():
            if a == b or self.wires.get(b) != a:
                raise ValueError('asymmetric wiring')
        if self.nodes and self.serial <= max(self.nodes):
            raise ValueError('allocator is not fresh')

    def active(self):
        self.validate()
        return [(n, self.wires[n, 'p'][0]) for n, (kind, _) in self.nodes.items()
                if kind == 'EB' and self.wires[n, 'p'][1] == 'p'
                and self.nodes[self.wires[n, 'p'][0]][0] == 'FB']

    def reduce(self, pair, retain_channels=False):
        if pair not in self.active():
            raise ValueError('not an enabled principal pair')
        a, b = pair
        x, y = self.nodes[a][1], self.nodes[b][1]
        if x['family'] != y['family'] or x['members'] & y['members']:
            raise ValueError('family or ownership mismatch')
        if x['pole'] + y['pole'] != 0:
            raise ValueError('uncancelled pole')
        peers = [self.wires[n, 'o'] for n in pair]
        if any(n in pair for n, _ in peers) or len(set(peers)) != 2:
            raise ValueError('invalid external boundary')
        payload = {'family': x['family'], 'members': x['members'] | y['members'],
                   'pole': x['pole'] + y['pole'],
                   'value': tuple(v+w for v,w in zip(x['value'], y['value']))}
        if retain_channels:
            # Fixed two-slot residual, aligned with the rule's boundary bijection.
            payload['channels'] = {'p': deepcopy(x), 'o': deepcopy(y)}
        for n in pair:
            for port in ARITY[self.nodes[n][0]]:
                endpoint = (n, port)
                if endpoint in self.wires:
                    peer = self.wires.pop(endpoint)
                    del self.wires[peer]
            del self.nodes[n]
        r = self.add('REM', payload)
        for port, peer in zip(ARITY['REM'], peers):
            self.link((r, port), peer)
        self.validate()
        return r

    def observe(self):
        """Joint family observer; counts each reachable remainder once, not twice."""
        self.validate()
        seen = set()
        result = {}
        for n, (kind, label) in self.nodes.items():
            if kind != 'OUT':
                continue
            peer, _ = self.wires[n, 'p']
            agent, payload = self.nodes[peer]
            if agent not in ('EB', 'FB', 'REM') or payload['family'] != label[0]:
                raise ValueError('unsupported observation boundary')
            if peer in seen:
                continue
            seen.add(peer)
            family = payload['family']
            value = result.setdefault(family, [0, 0])
            for i, v in enumerate(payload['value']):
                value[i] += v
        return {k: tuple(v) for k,v in result.items()}

    def observe_channels(self):
        """Read-only named boundary probes; no destructive runtime query is implied."""
        self.validate()
        result = {}
        for n, (kind, label) in self.nodes.items():
            if kind != 'OUT':
                continue
            peer, port = self.wires[n, 'p']
            agent, payload = self.nodes[peer]
            if agent == 'REM':
                if 'channels' not in payload:
                    raise ValueError('joint-only remainder cannot answer channel probes')
                payload = payload['channels'][port]
            elif agent not in ('EB', 'FB'):
                raise ValueError('unsupported channel peer')
            if payload['family'] != label[0] or label in result:
                raise ValueError('ambiguous channel boundary')
            result[label] = (tuple(sorted(payload['members'])), payload['pole'], payload['value'])
        return result

    def boundary_normal_form(self):
        """Name-independent terminal signature, retaining named external endpoints."""
        self.validate()
        if self.active():
            raise ValueError('not terminal')
        rows = []
        for n, (kind, payload) in self.nodes.items():
            if kind == 'OUT':
                continue
            boundary = []
            for port in ARITY[kind]:
                peer, _ = self.wires[n, port]
                if self.nodes[peer][0] != 'OUT':
                    raise ValueError('not a boundary remainder')
                boundary.append((port, self.nodes[peer][1]))
            rows.append((kind, payload['family'], tuple(sorted(payload['members'])),
                         payload['pole'], payload['value'], tuple(boundary),
                         tuple((port, tuple(sorted(v['members'])), v['pole'], v['value'])
                               for port,v in sorted(payload.get('channels', {}).items()))))
        return sorted(rows)

def construct(records):
    net = Net()
    for family in sorted({r['family'] for r in records.values()}):
        agents = []
        for kind, suffix in (('EB', 'E_B'), ('FB', 'F_B')):
            agent = net.add(kind, records[family+'_'+suffix])
            out = net.add('OUT', (family, kind))
            net.link((agent, 'o'), (out, 'p'))
            agents.append(agent)
        net.link((agents[0], 'p'), (agents[1], 'p'))
    net.validate()
    return net
