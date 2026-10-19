"""Exact reversible cyclic-mode motion on source-generated facet centroids.

For a source isometry R of order m, encode z_k=(1/m) sum_t zeta^(-kt) R^t v,
advance z_k -> zeta^k z_k, and decode v'=sum_k z_k=Rv. Keep k=0 as well.
Admission to the moving-centroid carrier means some k!=0 component is nonzero
for at least one supplied generator. No target geometry is read here.

Workflow map: docs/arrow-assembly.md (repository root). This wraps the common
geometry assembler for proton/electron examples; measures are centroid-cycle
measures, not coefficient-network transfer counts.
"""
from copy import deepcopy
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import argparse
import hashlib
import json

from assemble_relative_geometry import assemble, subtract, dot_metric


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def divide_exact(a, b):
    a, b = trim(a), trim(b)
    quotient = [Q(0)]*max(1, len(a)-len(b)+1)
    while len(a) >= len(b) and any(a):
        shift, scale = len(a)-len(b), a[-1]/b[-1]
        quotient[shift] += scale
        for i, c in enumerate(b):
            a[i+shift] -= scale*c
        a = trim(a)
    assert not any(a)
    return trim(quotient)


@lru_cache(None)
def cyclotomic(n):
    p = [Q(-1)]+[Q(0)]*(n-1)+[Q(1)]
    for d in range(1, n):
        if n % d == 0:
            p = divide_exact(p, cyclotomic(d))
    return tuple(p)


class Cyclotomic:
    def __init__(self, order):
        self.order = order
        self.polynomial = cyclotomic(order)
        self.degree = len(self.polynomial)-1
        self.zero = (Q(0),)*self.degree
        self.one = self.scalar(1)

    def reduce(self, coefficients):
        a = list(map(Q, coefficients))+[Q(0)]*max(0, self.degree-len(coefficients))
        for k in range(len(a)-1, self.degree-1, -1):
            c = a[k]
            for j in range(self.degree+1):
                a[k-self.degree+j] -= c*self.polynomial[j]
        return tuple(a[:self.degree])

    def scalar(self, x):
        return (Q(x),)+(Q(0),)*(self.degree-1)

    def add(self, a, b):
        return tuple(x+y for x, y in zip(a, b))

    def scale(self, x, a):
        return tuple(Q(x)*v for v in a)

    def multiply(self, a, b):
        out = [Q(0)]*(2*self.degree-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] += x*y
        return self.reduce(out)

    def root(self, exponent):
        exponent %= self.order
        return self.reduce([Q(0)]*exponent+[Q(1)])

    def conjugate(self, a):
        out = self.zero
        for i, c in enumerate(a):
            out = self.add(out, self.scale(c, self.root(-i)))
        return out


def identity(d):
    return tuple(tuple(Q(i == j) for j in range(d)) for i in range(d))


def mm(a, b):
    return tuple(tuple(sum(x*y for x, y in zip(row, col)) for col in zip(*b)) for row in a)


def mv(a, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in a)


def matrix_order(a, limit=256):
    current = I = identity(len(a))
    for n in range(1, limit+1):
        current = mm(a, current)
        if current == I:
            return n
    raise ValueError('Generator/word order exceeded the exact finite-motion bound')


def encode(v, matrix, ring):
    samples, current = [], v
    for _ in range(ring.order):
        samples.append(current)
        current = mv(matrix, current)
    assert current == v
    modes = []
    for k in range(ring.order):
        vector = []
        for i in range(len(v)):
            value = ring.zero
            for t, sample in enumerate(samples):
                value = ring.add(value, ring.scale(sample[i]/ring.order, ring.root(-k*t)))
            vector.append(value)
        modes.append(tuple(vector))
    return tuple(modes)


def advance(modes, ring, steps=1):
    return tuple(tuple(ring.multiply(ring.root(k*steps), x) for x in vector)
                 for k, vector in enumerate(modes))


def decode(modes, ring):
    values = []
    for i in range(len(modes[0])):
        total = ring.zero
        for mode in modes:
            total = ring.add(total, mode[i])
        if any(total[1:]):
            raise ValueError('Decoded mode state is not rational/real')
        values.append(total[0])
    return tuple(values)


def inner(a, b, G, ring):
    out = ring.zero
    for i in range(len(G)):
        for j in range(len(G)):
            out = ring.add(out, ring.scale(G[i][j], ring.multiply(ring.conjugate(a[i]), b[j])))
    return out


def serialize_modes(modes):
    return [[[str(x) for x in component] for component in mode] for mode in modes]


def evolve(source):
    unprotected = deepcopy(source)
    for seed in unprotected['seeds']:
        if seed['role'] == 'external_interface':
            seed['role'] = 'carrier'
    geometry = assemble(unprotected)
    d = geometry['dimension']
    center = tuple(map(Q, geometry['center']))
    points = [tuple(map(Q, p)) for p in geometry['vertices']]
    G = [[Q(x) for x in row] for row in source['metric']]
    matrices = [tuple(tuple(Q(x) for x in row) for row in g['matrix']) for g in source['generators']]
    if not matrices:
        raise ValueError('Mode motion requires a supplied generator')
    for raw, A in zip(source['generators'], matrices):
        assert tuple(x+Q(t) for x, t in zip(mv(A, center), raw['translation'])) == center
    orders = [matrix_order(A) for A in matrices]
    rings = [Cyclotomic(m) for m in orders]
    facet_states, moving, fixed, all_initial = [], [], [], []
    for facet in geometry['carrier_facets']:
        absolute = tuple(sum(points[i][k] for i in facet)/len(facet) for k in range(d))
        v = subtract(absolute, center)
        all_initial.append(v)
        records, active = [], False
        for A, m, ring in zip(matrices, orders, rings):
            modes = encode(v, A, ring)
            assert decode(modes, ring) == v
            assert decode(advance(modes, ring), ring) == mv(A, v)
            assert advance(advance(modes, ring), ring, -1) == modes
            assert advance(modes, ring, m) == modes
            energy = ring.zero
            for i, zi in enumerate(modes):
                for j, zj in enumerate(modes):
                    value = inner(zi, zj, G, ring)
                    if i == j:
                        energy = ring.add(energy, value)
                    else:
                        assert value == ring.zero
                assert tuple(ring.conjugate(x) for x in zi) == modes[(-i) % m]
            assert energy == ring.scalar(dot_metric(v, v, G))
            nonzero = [k for k, vector in enumerate(modes) if any(x != ring.zero for x in vector)]
            active |= any(k != 0 for k in nonzero)
            records.append({'order': m, 'cyclotomic_polynomial': list(map(str, ring.polynomial)),
                            'nonzero_modes': nonzero, 'encoded_modes': serialize_modes(modes),
                            'exact_inverse_and_phase_step': True, 'orthogonality_and_energy_preserved': True})
        (moving if active else fixed).append(facet)
        corners_move = any(mv(A, subtract(points[i], center)) != subtract(points[i], center)
                           for A in matrices for i in facet)
        facet_states.append({'facet': facet, 'centered_centroid': list(map(str, v)),
                             'moving_centroid': active, 'some_corner_moves': corners_move,
                             'generator_modes': records})
    # Compose the supplied generators in order. Re-encode at each generator;
    # different generators need not share an eigenbasis.
    word = identity(d)
    for A in matrices:
        word = mm(A, word)
    word_order = matrix_order(word)
    steps = word_order*len(matrices)
    current = list(all_initial)
    trace = []
    for step in range(steps):
        index = step % len(matrices)
        A, ring = matrices[index], rings[index]
        updated = []
        for v in current:
            following = decode(advance(encode(v, A, ring), ring), ring)
            assert following == mv(A, v)
            assert dot_metric(following, following, G) == dot_metric(v, v, G)
            updated.append(following)
        current = updated
        trace.append({'generator_index': index,
                      'centroids': [list(map(str, v)) for v in current],
                      'all_labelled_centroids_returned': current == all_initial})
    assert current == all_initial
    # Reverse the actual encoded history without throwing away the fixed modes.
    for step in range(len(trace)-1, -1, -1):
        index = trace[step]['generator_index']
        A, ring = matrices[index], rings[index]
        current = [decode(advance(encode(v, A, ring), ring, -1), ring) for v in current]
        expected = all_initial if step == 0 else [tuple(map(Q, v)) for v in trace[step-1]['centroids']]
        assert current == expected
    assert current == all_initial
    selected = deepcopy(geometry)
    selected['carrier_facets'] = moving
    selected['external_interfaces'] = [sorted(f) for f in fixed]
    selected['cone_cells'] = [[geometry['center_vertex_id']]+f for f in moving]
    selected['positive_cone_determinants_in_source_coordinates'] = [value for f, value in zip(
        geometry['carrier_facets'], geometry['positive_cone_determinants_in_source_coordinates']) if f in moving]
    selected['counts'].update(carrier_facets=len(moving), cone_cells=len(moving), external_interfaces=len(fixed))
    return {'geometry': selected, 'facet_states': facet_states, 'generator_orders': orders,
            'scheduled_word_order': word_order, 'scheduled_atomic_steps_to_word_return': steps,
            'centroid_motion_trace': trace, 'reverse_history_recovers_every_centroid': True,
            'fixed_modes_retained': True,
            'scope': 'Reversible source-isometry dynamics on centroid channels. Active facets are selected by nontrivial mode support; stationary centroids do not imply stationary corners or deletion of caps.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    raw = Path(args.source).read_bytes()
    result = evolve(json.loads(raw))
    result['source_sha256'] = hashlib.sha256(raw).hexdigest()
    result['constructor_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    dest = Path(args.output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'counts': result['geometry']['counts'], 'generator_orders': result['generator_orders'],
                      'scheduled_steps': result['scheduled_atomic_steps_to_word_return']}))


if __name__ == '__main__':
    main()
