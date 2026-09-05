#!/usr/bin/env python3
"""Exact finite-poset nerve with faces, degeneracies, Segal and Rezk checks."""
from itertools import product
import json
from pathlib import Path

class FinitePosetNerve:
    def __init__(self, objects, leq):
        self.objects = tuple(objects)
        self.leq = leq
        for x in self.objects:
            assert leq(x, x)
        for x, y in product(self.objects, repeat=2):
            assert not (leq(x, y) and leq(y, x)) or x == y
        for x, y, z in product(self.objects, repeat=3):
            assert not (leq(x, y) and leq(y, z)) or leq(x, z)

    def simplices(self, n):
        return tuple(xs for xs in product(self.objects, repeat=n + 1)
                     if all(self.leq(xs[i], xs[i + 1]) for i in range(n)))

    @staticmethod
    def face(simplex, i):
        return simplex[:i] + simplex[i + 1:]

    @staticmethod
    def degeneracy(simplex, i):
        return simplex[:i + 1] + (simplex[i],) + simplex[i + 1:]

    def verify_simplicial_identities(self, max_degree=4):
        checks = 0
        # d_i d_j = d_{j-1} d_i for i < j
        for n in range(2, max_degree + 1):
            for x in self.simplices(n):
                for i in range(n):
                    for j in range(i + 1, n + 1):
                        assert self.face(self.face(x, j), i) == self.face(self.face(x, i), j - 1)
                        checks += 1
        # s_i s_j = s_{j+1} s_i for i <= j
        for n in range(max_degree):
            for x in self.simplices(n):
                for i in range(n + 1):
                    for j in range(i, n + 1):
                        assert self.degeneracy(self.degeneracy(x, j), i) == self.degeneracy(self.degeneracy(x, i), j + 1)
                        checks += 1
        # d_i s_j identities, checked directly by the three standard cases.
        for n in range(max_degree):
            for x in self.simplices(n):
                for j in range(n + 1):
                    sx = self.degeneracy(x, j)
                    for i in range(n + 2):
                        lhs = self.face(sx, i)
                        if i < j:
                            rhs = self.degeneracy(self.face(x, i), j - 1)
                        elif i == j or i == j + 1:
                            rhs = x
                        else:
                            rhs = self.degeneracy(self.face(x, i - 1), j)
                        assert lhs == rhs
                        checks += 1
        return checks

    def verify_segal(self, max_degree=4):
        checks = 0
        for n in range(2, max_degree + 1):
            spines = tuple(edges for edges in product(self.simplices(1), repeat=n)
                           if all(edges[i][1] == edges[i + 1][0] for i in range(n - 1)))
            image = tuple(tuple((x[i], x[i + 1]) for i in range(n)) for x in self.simplices(n))
            assert len(image) == len(set(image))
            assert set(image) == set(spines)
            checks += len(image)
        return checks

    def verify_rezk_completeness(self):
        arrows = self.simplices(1)
        invertible = tuple((x, y) for x, y in arrows if self.leq(y, x))
        identities = tuple((x, x) for x in self.objects)
        assert invertible == identities
        return len(arrows), len(invertible)

def fact5_nerve():
    ds = ('13', '14', '24', '25', '35')
    crossing = {frozenset(('13', '24')), frozenset(('13', '25')),
                frozenset(('14', '25')), frozenset(('14', '35')),
                frozenset(('24', '35'))}
    objs = [frozenset()]
    objs += [frozenset((d,)) for d in ds]
    objs += [frozenset(pair) for pair in product(ds, repeat=2)
             if pair[0] < pair[1] and frozenset(pair) not in crossing]
    return FinitePosetNerve(objs, lambda x, y: x <= y)

def audit(name, nerve):
    return {
        'name': name,
        'objects': len(nerve.objects),
        'simplices_by_degree_0_to_4': [len(nerve.simplices(n)) for n in range(5)],
        'simplicial_identity_instances': nerve.verify_simplicial_identities(),
        'segal_simplex_instances': nerve.verify_segal(),
        'arrows_and_invertible_arrows': nerve.verify_rezk_completeness(),
        'status': 'passed'
    }

result = {
    'schema': 'marici.finite-poset-nerve-check.v1',
    'scope': 'exact external simplicial-set nerve; no Rzk internalization asserted',
    'tests': [
        audit('walking-arrow-chain-2', FinitePosetNerve((0, 1), lambda x, y: x <= y)),
        audit('fact5-refinement-poset', fact5_nerve())
    ]
}
out = Path('research/nima/results/finite_poset_nerve.json')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, sort_keys=True))
