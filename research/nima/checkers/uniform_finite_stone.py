"""Reconstruction from finite Boolean tables, without supplied atoms or inverse.

Only powerset_fixture knows about bit masks. The construction uses table lookups.
This module is dependency-free. Certificates are exhaustive for a supplied object;
they are not a universally quantified proof in Agda.
"""
from dataclasses import dataclass
from itertools import combinations, product


class InvalidStructure(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise InvalidStructure(message)


@dataclass(frozen=True)
class BooleanTable:
    zero: int
    one: int
    neg: tuple
    meet: tuple
    join: tuple

    @property
    def elements(self):
        return range(len(self.neg))

    def le(self, x, y):
        return self.meet[x][y] == x

    def validate(self):
        xs = self.elements
        n = len(xs)
        require(n > 0, 'empty carrier')
        valid = lambda x: type(x) is int and 0 <= x < n
        require(valid(self.zero) and valid(self.one), 'bounds outside carrier')
        require(all(valid(x) for x in self.neg), 'complement outside carrier')
        for op in (self.meet, self.join):
            require(len(op) == n and all(len(row) == n for row in op), 'table dimensions')
            require(all(valid(x) for row in op for x in row), 'operation outside carrier')
        m, j, c = self.meet, self.join, self.neg
        for a in xs:
            require(m[a][self.one] == a and j[a][self.zero] == a, 'bounded identities')
            require(m[a][a] == a and j[a][a] == a, 'idempotence')
            require(m[a][c[a]] == self.zero and j[a][c[a]] == self.one, 'complement')
            for b in xs:
                require(m[a][b] == m[b][a] and j[a][b] == j[b][a], 'commutativity')
                require(m[a][j[a][b]] == a and j[a][m[a][b]] == a, 'absorption')
                for d in xs:
                    require(m[m[a][b]][d] == m[a][m[b][d]], 'meet associativity')
                    require(j[j[a][b]][d] == j[a][j[b][d]], 'join associativity')
                    require(m[a][j[b][d]] == j[m[a][b]][m[a][d]], 'distributivity')
                    require(j[a][m[b][d]] == m[j[a][b]][j[a][d]], 'dual distributivity')
        return self


def subsets(xs):
    return tuple(frozenset(s) for n in range(len(xs) + 1) for s in combinations(xs, n))


@dataclass(frozen=True)
class Reconstruction:
    algebra: BooleanTable
    atoms: tuple

    def represent(self, x):
        require(type(x) is int and x in self.algebra.elements, 'element outside carrier')
        return frozenset(a for a in self.atoms if self.algebra.le(a, x))

    def reconstruct(self, subset):
        require(set(subset) <= set(self.atoms), 'not a subset of atoms')
        x = self.algebra.zero
        for a in self.atoms:
            if a in subset:
                x = self.algebra.join[x][a]
        return x

    def verify(self):
        b = self.algebra.validate()
        actual = tuple(a for a in b.elements if a != b.zero and all(
            x == b.zero or x == a for x in b.elements if b.le(x, a)))
        require(self.atoms == actual, 'incorrect atom certificate')
        universe = frozenset(self.atoms)
        require(self.represent(b.zero) == frozenset(), 'bottom preservation')
        require(self.represent(b.one) == universe, 'top preservation')
        for x in b.elements:
            require(self.reconstruct(self.represent(x)) == x, 'algebra roundtrip')
            require(self.represent(b.neg[x]) == universe - self.represent(x), 'complement preservation')
            for y in b.elements:
                require(self.represent(b.meet[x][y]) == self.represent(x) & self.represent(y), 'meet preservation')
                require(self.represent(b.join[x][y]) == self.represent(x) | self.represent(y), 'join preservation')
        for s in subsets(self.atoms):
            require(self.represent(self.reconstruct(s)) == s, 'subset roundtrip')
        return self


def derive(b):
    b.validate()
    atoms = tuple(a for a in b.elements if a != b.zero and all(
        x == b.zero or x == a for x in b.elements if b.le(x, a)))
    return Reconstruction(b, atoms).verify()


def is_hom(b, c, h):
    if len(h) != len(b.elements) or any(type(x) is not int or x not in c.elements for x in h):
        return False
    return (h[b.zero] == c.zero and h[b.one] == c.one
        and all(h[b.neg[x]] == c.neg[h[x]] for x in b.elements)
        and all(h[b.meet[x][y]] == c.meet[h[x]][h[y]]
                and h[b.join[x][y]] == c.join[h[x]][h[y]]
                for x, y in product(b.elements, repeat=2)))


def dual_map(source, target, h):
    """h:B→C yields a map of ACTUAL atom labels Atom(C)→Atom(B)."""
    b, c = source.algebra, target.algebra
    require(is_hom(b, c, h), 'not a Boolean homomorphism')
    result = []
    for q in target.atoms:
        candidates = [p for p in source.atoms if c.le(q, h[p])]
        require(len(candidates) == 1, 'nonunique or missing point pullback')
        result.append(candidates[0])
    result = tuple(result)
    verify_dual(source, target, h, result)
    return result


def verify_dual(source, target, h, f):
    require(is_hom(source.algebra, target.algebra, h), 'not a Boolean homomorphism')
    require(len(f) == len(target.atoms) and all(p in source.atoms for p in f), 'point-map type')
    for x in source.algebra.elements:
        pulled = frozenset(q for q, p in zip(target.atoms, f) if p in source.represent(x))
        require(target.represent(h[x]) == pulled, 'naturality')
    return True


def pullback(source, target, f):
    """Build B→C from Atom(C)→Atom(B), using the derived inverse."""
    require(len(f) == len(target.atoms) and all(p in source.atoms for p in f), 'point-map type')
    h = tuple(target.reconstruct(frozenset(q for q, p in zip(target.atoms, f)
        if p in source.represent(x))) for x in source.algebra.elements)
    verify_dual(source, target, h, f)
    return h


def powerset_fixture(n):
    size = 2 ** n
    return BooleanTable(0, size - 1, tuple((size - 1) ^ a for a in range(size)),
        tuple(tuple(a & b for b in range(size)) for a in range(size)),
        tuple(tuple(a | b for b in range(size)) for a in range(size)))


def relabel(b, permutation):
    """permutation[old] = new; transport only tables, never hidden coordinates."""
    n = len(b.elements)
    require(sorted(permutation) == list(range(n)), 'not a permutation')
    inverse = [permutation.index(i) for i in range(n)]
    op = lambda table: tuple(tuple(permutation[table[inverse[i]][inverse[j]]]
        for j in range(n)) for i in range(n))
    return BooleanTable(permutation[b.zero], permutation[b.one],
        tuple(permutation[b.neg[inverse[i]]] for i in range(n)), op(b.meet), op(b.join))
