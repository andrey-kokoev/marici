"""Arbitrary-even-n massless phi4 trees as native three-column DAG tables.

Shared odd-subset currents retain all unordered three-way partitions and child
attachments. No legacy current, history or evaluator is called. Exact rational
non-pole kinematics only; exponential combinatorics, not polynomial complexity.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
from types import MappingProxyType
from native_scalar_fibers import Row, External, norm, momentum_sum, index


@dataclass(frozen=True)
class Boundary:
    coupling: Q
    legs: int
    root: int
    theory: str = 'massless-phi4-tree'


@dataclass(frozen=True)
class Current:
    leaves: tuple
    momentum: tuple
    denominator: Q | None
    amputated: bool


@dataclass(frozen=True)
class Branch:
    children: tuple


def partitions(labels):
    """Each odd three-block partition once, ordered by its block minima."""
    if len(labels) < 3 or len(labels) % 2 == 0:
        return ()
    result = []
    for size in range(1, len(labels)-1, 2):
        for tail in combinations(labels[1:], size-1):
            a = (labels[0],)+tail
            rest = tuple(x for x in labels if x not in a)
            for size_b in range(1, len(rest), 2):
                for tail_b in combinations(rest[1:], size_b-1):
                    b = (rest[0],)+tail_b
                    c = tuple(x for x in rest if x not in b)
                    result.append((a,b,c))
    return tuple(result)


def boundary_check(ps, coupling, root):
    if len(ps) < 4 or len(ps) % 2:
        raise ValueError('even multiplicity >=4 required')
    if type(root) is not int or not 0 <= root < len(ps):
        raise ValueError('invalid external root')
    if not isinstance(coupling, Q):
        raise ValueError('rational coupling required')
    if any(not isinstance(p,tuple) or len(p) != 4 or any(not isinstance(x, Q) for x in p) for p in ps):
        raise ValueError('rational four-momenta required')
    if any(norm(p) != 0 for p in ps):
        raise ValueError('off shell')
    if any(momentum_sum(ps, range(len(ps)))):
        raise ValueError('momentum conservation')


def address(boundary, leaves):
    return (boundary, 'current', leaves)


def construct(ps, coupling, root=0, boundary='b'):
    if not isinstance(boundary,str):
        raise ValueError('text boundary identifier required')
    ps = tuple(tuple(Q(x) for x in p) for p in ps)
    coupling = Q(coupling)
    boundary_check(ps, coupling, root)
    remaining = tuple(i for i in range(len(ps)) if i != root)
    rows = [Row(Boundary(coupling, len(ps), root), boundary, 'declaration')]
    rows.extend(Row(External(p), boundary, ('external',i)) for i,p in enumerate(ps))
    seen = set()
    def build(leaves):
        source = address(boundary, leaves)
        if leaves in seen:
            return source
        seen.add(leaves)
        p = momentum_sum(ps, leaves)
        amputated = leaves == remaining
        denominator = None if amputated or len(leaves) == 1 else norm(p)
        if denominator == 0:
            raise ValueError('internal pole; no rational i0 substitution')
        rows.append(Row(Current(leaves,p,denominator,amputated), source, 'declaration'))
        for blocks in partitions(leaves):
            children = tuple(build(block) for block in blocks)
            rows.append(Row(Branch(children), source, ('partition',blocks)))
        return source
    rows.append(Row(build(remaining), boundary, 'root'))
    return tuple(rows)


class Evaluation:
    """Validated native table plus memoized values/counts, not erased history."""
    def __init__(self, rows, boundary='b'):
        if not isinstance(boundary,str):
            raise ValueError('text boundary identifier required')
        self.rows = tuple(rows)
        idx = index(self.rows)
        local = {target:label for (source,target),label in idx.items() if source == boundary}
        decl = local.get('declaration')
        if not isinstance(decl, Boundary) or decl.theory != 'massless-phi4-tree':
            raise ValueError('missing/unknown boundary declaration')
        if type(decl.legs) is not int or decl.legs < 4 or decl.legs % 2:
            raise ValueError('even multiplicity >=4 required')
        expected = {'declaration','root'} | {('external',i) for i in range(decl.legs)}
        if set(local) != expected:
            raise ValueError('missing/extra boundary port')
        external = tuple(local[('external',i)] for i in range(decl.legs))
        if any(not isinstance(p,External) for p in external):
            raise ValueError('wrong external attachment')
        ps = tuple(p.momentum for p in external)
        boundary_check(ps,decl.coupling,decl.root)
        remaining = tuple(i for i in range(decl.legs) if i != decl.root)
        if local['root'] != address(boundary,remaining):
            raise ValueError('wrong root attachment')
        self.groups = {}
        for (source,target),label in idx.items():
            if isinstance(source,tuple) and len(source)==3 and source[:2] == (boundary,'current'):
                self.groups.setdefault(source[2],{})[target] = label
        visited = set()
        def validate(leaves):
            if leaves in visited:
                return
            visited.add(leaves)
            group = self.groups.get(leaves,{})
            cur = group.get('declaration')
            p = momentum_sum(ps,leaves)
            amputated = leaves == remaining
            d = None if amputated or len(leaves)==1 else norm(p)
            if d == 0:
                raise ValueError('internal pole')
            if (not isinstance(cur,Current) or type(cur.amputated) is not bool
                    or any(not isinstance(x,Q) for x in cur.momentum)
                    or (d is not None and not isinstance(cur.denominator,Q))
                    or cur != Current(leaves,p,d,amputated)):
                raise ValueError('incompatible current declaration')
            choices = partitions(leaves)
            if set(group) != {'declaration'} | {('partition',blocks) for blocks in choices}:
                raise ValueError('missing/extra partition')
            for blocks in choices:
                branch = group[('partition',blocks)]
                if not isinstance(branch,Branch) or branch.children != tuple(address(boundary,b) for b in blocks):
                    raise ValueError('incompatible child attachment')
                # Strictly smaller, disjoint blocks; cycles cannot be admitted.
                for block in blocks:
                    validate(block)
        validate(remaining)
        if visited != set(self.groups):
            raise ValueError('unreachable current declaration')
        # Refuse unexpected source namespaces, while permitting merged boundary tables.
        admitted_sources = {boundary} | {address(boundary,s) for s in visited}
        for source,_ in idx:
            if source == boundary or (isinstance(source,tuple) and source and source[0] == boundary):
                if source not in admitted_sources:
                    raise ValueError('unknown current namespace')
        self.groups = MappingProxyType({s:MappingProxyType(g) for s,g in self.groups.items()})
        self.boundary = boundary
        self.declaration = decl
        self.remaining = remaining
        self._value = lru_cache(None)(self._evaluate)
        self._count = lru_cache(None)(self._count_trees)

    def choices(self, leaves):
        return tuple(label for port,label in self.groups[leaves].items() if port != 'declaration')

    def _evaluate(self, leaves):
        cur = self.groups[leaves]['declaration']
        if len(leaves)==1:
            return Q(1)
        total = sum((multiply(self._value(child[2]) for child in branch.children)
                     for branch in self.choices(leaves)), Q(0))
        if cur.amputated:
            return -self.declaration.coupling * total
        return self.declaration.coupling * total / cur.denominator

    def _count_trees(self, leaves):
        if len(leaves)==1:
            return 1
        return sum(multiply(self._count(child[2]) for child in branch.children)
                   for branch in self.choices(leaves))

    @property
    def amplitude(self):
        return self._value(self.remaining)

    @property
    def diagram_count(self):
        return self._count(self.remaining)

    def diagrams(self, limit=10000):
        """Optional expansion into internal split sets and individual weights.

        Sharing compresses the calculation, not multiplicity. Expansion has an
        explicit budget and refuses rather than silently truncating diagrams.
        """
        if self.diagram_count > limit:
            raise ValueError('diagram expansion budget exceeded')
        n = self.declaration.legs
        def expand(leaves):
            cur = self.groups[leaves]['declaration']
            if len(leaves)==1:
                return (((),Q(1)),)
            if cur.amputated:
                own = ()
                factor = -self.declaration.coupling
            else:
                complement = tuple(i for i in range(n) if i not in leaves)
                own = (min(leaves,complement,key=lambda s:(len(s),s)),)
                factor = self.declaration.coupling/cur.denominator
            result = []
            for branch in self.choices(leaves):
                for terms in product(*(expand(child[2]) for child in branch.children)):
                    edges = tuple(sorted(own+tuple(e for es,_ in terms for e in es)))
                    result.append((edges,factor*multiply(w for _,w in terms)))
            return tuple(result)
        return expand(self.remaining)


def multiply(values):
    result = 1
    for value in values:
        result *= value
    return result


def amplitude(rows, boundary='b'):
    return Evaluation(rows,boundary).amplitude
