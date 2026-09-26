"""Independent finite weighted-table evaluator for massless phi^4 trees.

Only four/six external legs, exact rational non-pole kinematics. Physics is
supplied: vertex -i*lambda, propagator i/q^2, delta-stripped contribution i*M.
For these trees M_h = -lambda**V / product(q_e**2). No legacy evaluator import.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations

@dataclass(frozen=True)
class Row:
    label: object
    source: object
    target: object

@dataclass(frozen=True)
class Declaration:
    coupling: Q
    legs: int
    theory: str = 'massless-phi4-tree'

@dataclass(frozen=True)
class External:
    momentum: tuple

@dataclass(frozen=True)
class Vertex:
    coupling: Q

@dataclass(frozen=True)
class Propagator:
    split: tuple
    momentum: tuple
    denominator: Q

@dataclass(frozen=True)
class Channel:
    rows: tuple


def index(rows):
    result = {}
    for row in rows:
        key = (row.source, row.target)
        if key in result:
            raise ValueError('duplicate endpoints')
        result[key] = row.label
    return result


def norm(p):
    return p[0]*p[0] - p[1]*p[1] - p[2]*p[2] - p[3]*p[3]


def momentum_sum(ps, labels):
    return tuple(sum((ps[i][mu] for i in labels), Q(0)) for mu in range(4))


def check_boundary(ps):
    if len(ps) not in (4, 6):
        raise ValueError('only four/six-point boundary supported')
    if any(len(p) != 4 or any(not isinstance(x, Q) for x in p) for p in ps):
        raise ValueError('exact rational four-momenta required')
    if any(norm(p) != 0 for p in ps):
        raise ValueError('off shell')
    if any(momentum_sum(ps, range(len(ps)))):
        raise ValueError('momentum conservation')


def splits(n, anchor=0):
    if not 0 <= anchor < n:
        raise ValueError('invalid anchor')
    if n == 4:
        return ((),)
    return tuple(sorted({tuple(sorted((tuple(sorted((anchor,)+other)),
                                      tuple(i for i in range(n) if i not in (anchor,)+other))))
                         for other in combinations(tuple(i for i in range(n) if i != anchor), 2)}))


def construct(ps, coupling, boundary='b', anchor=0):
    """Construct diagram tables from external data, not from old histories."""
    ps = tuple(tuple(Q(x) for x in p) for p in ps)
    coupling = Q(coupling)
    check_boundary(ps)
    rows = [Row(Declaration(coupling, len(ps)), boundary, 'declaration')]
    rows.extend(Row(External(p), boundary, ('external', i)) for i, p in enumerate(ps))
    for split in splits(len(ps), anchor):
        sub = [Row(Vertex(coupling), 'diagram', ('vertex', i))
               for i in range(1 if len(ps) == 4 else 2)]
        if split:
            p = momentum_sum(ps, split[0])
            denominator = norm(p)
            if denominator == 0:
                raise ValueError('internal pole; rational i0 replacement forbidden')
            sub.append(Row(Propagator(split, p, denominator), 'diagram', 'propagator'))
        rows.append(Row(Channel(tuple(sub)), boundary, ('channel', split)))
    return tuple(rows)


def fiber(rows, boundary):
    """The from-column fiber. Rows at other boundaries are not discarded globally."""
    return tuple(row for row in rows if row.source == boundary)


def contributions(rows, boundary='b'):
    """Interpret native fields, validating all declarations and attachments."""
    index(rows)  # Global uniqueness, including rows outside the selected fiber.
    local = {row.target: row.label for row in fiber(rows, boundary)}
    decl = local.get('declaration')
    if not isinstance(decl, Declaration) or decl.theory != 'massless-phi4-tree':
        raise ValueError('missing/unknown declaration')
    if not isinstance(decl.coupling, Q) or decl.legs not in (4, 6):
        raise ValueError('invalid declaration')
    expected = {'declaration'} | {('external', i) for i in range(decl.legs)}
    channels = splits(decl.legs)
    expected |= {('channel', s) for s in channels}
    if set(local) != expected:
        raise ValueError('missing/extra channel or external port')
    external = tuple(local[('external', i)] for i in range(decl.legs))
    if any(not isinstance(p, External) for p in external):
        raise ValueError('wrong external attachment')
    ps = tuple(p.momentum for p in external)
    check_boundary(ps)
    result = []
    for split in channels:
        channel = local[('channel', split)]
        if not isinstance(channel, Channel):
            raise ValueError('wrong channel attachment')
        sub = index(channel.rows)
        ports = {('diagram', ('vertex', i)) for i in range(1 if decl.legs == 4 else 2)}
        if split:
            ports.add(('diagram', 'propagator'))
        if set(sub) != ports:
            raise ValueError('missing/extra vertex or propagator')
        weight = Q(-1)
        for i in range(1 if decl.legs == 4 else 2):
            v = sub[('diagram', ('vertex', i))]
            if not isinstance(v, Vertex) or not isinstance(v.coupling, Q) or v.coupling != decl.coupling:
                raise ValueError('incompatible vertex weight')
            weight *= v.coupling
        if split:
            edge = sub[('diagram', 'propagator')]
            p = momentum_sum(ps, split[0])
            d = norm(p)
            if d == 0:
                raise ValueError('internal pole')
            if (not isinstance(edge, Propagator) or not isinstance(edge.denominator, Q)
                    or any(not isinstance(x, Q) for x in edge.momentum)
                    or (edge.split, edge.momentum, edge.denominator) != (split, p, d)):
                raise ValueError('incompatible propagator attachment')
            weight /= edge.denominator
        result.append((split, weight))
    return tuple(result)


def amplitude(rows, boundary='b'):
    return sum((weight for _, weight in contributions(rows, boundary)), Q(0))
