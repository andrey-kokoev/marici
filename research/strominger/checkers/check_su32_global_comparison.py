"""One global comparison carrier, retaining rather than killing route mismatches.

Standard-library exact arithmetic. Uses the existing native support exporter and
Whitney product; does not infer coefficients or phases for native wire payloads.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import subprocess
from check_su32_cochain_transfer import (
    add, scale, faces, differential, parity, oriented, multiply, rank, complex_info)

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'research/strominger/results/su32-global-comparison-v1'
SUPPORT = ROOT / 'research/strominger/results/su32-cochain-transfer-v1/support.json'


def clean(x):
    return {k: F(v) for k, v in x.items() if v}


def value(x, sequence):
    return parity(sequence)*x.get(tuple(sorted(sequence)), F(0))


def nullspace(a):
    a = [[F(x) for x in row] for row in a]
    n = len(a[0]); pivots = []; r = 0
    for j in range(n):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][j]; a[r] = [x/v for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                v = a[i][j]; a[i] = [x-v*y for x, y in zip(a[i], a[r])]
        pivots.append(j); r += 1
        if r == len(a):
            break
    result = []
    for j in range(n):
        if j not in pivots:
            v = [F(0)]*n; v[j] = 1
            for i, p in enumerate(pivots):
                v[p] = -a[i][j]
            result.append(v)
    return result


class GlobalComparison:
    def __init__(self, source):
        self.source = source
        self.charts = sorted((c for c in source['occurrences'] if c['binding'] == [0, 0]),
                             key=lambda c: c['chartId'])
        self.fine = faces(source['facets']); self.fs = set(self.fine)
        self.fb = [[s for s in self.fine if len(s) == k+1] for k in range(3)]
        self.squares = [c['square'] for c in self.charts]
        self.edges = sorted({tuple(sorted((q[j], q[(j+1) % 4])))
                             for q in self.squares for j in range(4)})
        self.es = set(self.edges)
        self.triangles = []
        diagonals = []
        for q in self.squares:
            self.triangles.append([[q[j] for j in t] for t in
                                   [(0, 1, 2), (0, 2, 3), (1, 2, 3), (1, 3, 0)]])
            diagonals.extend([tuple(sorted((q[0], q[2]))), tuple(sorted((q[1], q[3])))])
        assert len(set(diagonals)) == len(diagonals) == 72
        assert not self.es.intersection(diagonals)
        assert self.es | set(diagonals) == set(self.fb[1])
        all_triangles = [tuple(sorted(t)) for ts in self.triangles for t in ts]
        assert len(set(all_triangles)) == len(all_triangles) == 144
        assert set(all_triangles) == set(self.fb[2])
        self.qb = [self.fb[0], self.edges, [('Omega', j) for j in range(len(self.charts))]]
        self.rb = [self.qb[0], self.qb[1], self.qb[2]+[('mu', j) for j in range(len(self.charts))]]
        self.df_basis = {s: differential({s: F(1)}, self.fine) for s in self.fine}

    def df(self, x):
        return add(*(scale(v, self.df_basis[s]) for s, v in x.items()))

    def dr(self, k, x):
        if not x:
            return {}
        if k == 0:
            return {e: v for e in self.edges if (v := x.get((e[1],), 0)-x.get((e[0],), 0))}
        if k == 1:
            return clean({('Omega', j): sum(value(x, [q[t], q[(t+1) % 4]]) for t in range(4))
                          for j, q in enumerate(self.squares)})
        return {}

    def project(self, k, x):
        if k == 0:
            return x.copy()
        if k == 1:
            return {s: v for s, v in x.items() if s in self.es}
        if k != 2:
            return {}
        result = {}
        for j, ts in enumerate(self.triangles):
            a, b, c, d = [value(x, t) for t in ts]
            result['Omega', j] = (a+b+c+d)/2
            result['mu', j] = a+b-c-d
        return clean(result)

    def include(self, k, x):
        if k == 0:
            return x.copy()
        if k == 1:
            terms = [x.copy()]
            for q in self.squares:
                a, b, c, d = [value(x, [q[t], q[(t+1) % 4]]) for t in range(4)]
                terms.extend([scale((a+b-c-d)/2, oriented([q[0], q[2]])),
                              scale((b+c-d-a)/2, oriented([q[1], q[3]]))])
            return add(*terms)
        if k != 2:
            return {}
        terms = []
        for j, ts in enumerate(self.triangles):
            omega, mu = x.get(('Omega', j), F(0)), x.get(('mu', j), F(0))
            for n, t in enumerate(ts):
                terms.append(scale(omega/2+(mu/4 if n < 2 else -mu/4), oriented(t)))
        return add(*terms)

    def homotopy(self, k, x):
        if k != 2:
            return {}
        terms = []
        for q, ts in zip(self.squares, self.triangles):
            a, b, c, d = [value(x, t) for t in ts]
            terms.extend([scale((b-a)/2, oriented([q[0], q[2]])),
                          scale((d-c)/2, oriented([q[1], q[3]]))])
        return add(*terms)

    def operation(self, p, a, q, b):
        """Transfer one whole-complex Whitney product; no route is selected."""
        return self.project(p+q, multiply(self.include(p, a), self.include(q, b), self.fs, 'Whitney'))

    def route(self, k, x, role):
        if k != 2:
            return x.copy()
        sign = 1 if role == 'E' else -1
        return clean({('Omega', j): x.get(('Omega', j), F(0))+sign*x.get(('mu', j), F(0))/2
                      for j in range(len(self.charts))})

    def defect(self, x):
        return {('Omega', j): v for (tag, j), v in x.items() if tag == 'mu' and v}

    def linear(self, j, w, square=None):
        q = self.squares[j] if square is None else square
        return sum((-1)**(t+1)*value(w, [q[t], q[(t+1) % 4]]) for t in range(4))/12

    def higher(self, p, a, q, b):
        if (p, q) == (2, 1):
            return self.higher(1, b, 2, a)
        if (p, q) != (1, 2):
            return {}
        return clean({('Omega', j): self.linear(j, a)*v for (tag, j), v in b.items() if tag == 'Omega'})


def main():
    subprocess.run(['node', 'research/strominger/checkers/export_su32_comparison_support.mjs'],
                   cwd=ROOT, check=True, capture_output=True, text=True)
    source = json.loads(SUPPORT.read_text(encoding='utf8'))
    for p, h in source['sourceHashes'].items():
        assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest() == h
    g = GlobalComparison(source)
    contractions = 0
    for k, basis in enumerate(g.fb):
        for s in basis:
            x = {s: F(1)}; dx = g.df(x)
            assert not g.df(dx)
            assert g.project(k+1, dx) == g.dr(k, g.project(k, x))
            residual = add(g.df(g.homotopy(k, x)), g.homotopy(k+1, dx))
            assert add(g.include(k, g.project(k, x)), residual) == x
            assert not g.homotopy(k-1, g.homotopy(k, x))
            assert not g.project(k-1, g.homotopy(k, x))
            contractions += 1
    for k, basis in enumerate(g.rb):
        for s in basis:
            x = {s: F(1)}
            assert g.project(k, g.include(k, x)) == x
            assert g.df(g.include(k, x)) == g.include(k+1, g.dr(k, x))
            assert not g.homotopy(k, g.include(k, x))
            for role in ['P', 'E']:
                assert g.route(k+1, g.dr(k, x), role) == g.dr(k, g.route(k, x, role))
    # Derive both operations from one global fine Whitney product.
    lifted = {s: g.include(k, {s: F(1)}) for k, bs in enumerate(g.qb) for s in bs}
    higher_checks = 0
    for p, q in product(range(3), repeat=2):
        for a, b in product(g.qb[p], g.qb[q]):
            x, y = {a: F(1)}, {b: F(1)}
            fine_product = multiply(lifted[a], lifted[b], g.fs, 'Whitney')
            result = g.project(p+q, fine_product)
            delta = add(g.route(p+q, result, 'E'), scale(-1, g.route(p+q, result, 'P')))
            assert delta == (g.defect(result) if p+q == 2 else {})
            h = g.higher(p, x, q, y)
            rhs = add(g.dr(p+q-1, h), g.higher(p+1, g.dr(p, x), q, y),
                      scale((-1)**p, g.higher(p, x, q+1, g.dr(q, y))))
            assert delta == rhs, (p, q, a, b, delta, rhs)
            higher_checks += 1
    # Symmetrization removes the previous local H's sign-binding dependence.
    frame_checks = 0
    lookup = {c['chartId']: j for j, c in enumerate(g.charts)}
    for c in source['occurrences']:
        j = lookup[c['chartId']]
        for edge in g.edges:
            assert g.linear(j, {edge: F(1)}, c['square']) == g.linear(j, {edge: F(1)})
            frame_checks += 1
    matrix = [[g.dr(1, {e: F(1)}).get(('Omega', j), 0) for e in g.edges]
              for j in range(len(g.charts))]
    d1rank = rank(matrix)
    cycles = nullspace(list(map(list, zip(*matrix))))
    assert len(cycles) == 7 and d1rank == 29
    for z in cycles:
        assert all(sum(z[j]*matrix[j][e] for j in range(len(z))) == 0 for e in range(len(g.edges)))
    # A nonzero global period with all local route mismatches zero.
    z = cycles[0]; j = next(i for i, v in enumerate(z) if v)
    omega = {('Omega', j): F(1)}
    fine = g.include(2, omega)
    assert g.project(2, fine) == omega and not g.defect(g.project(2, fine))
    assert g.route(2, omega, 'E') == g.route(2, omega, 'P')
    assert z[j] != 0
    # Conversely, a local mismatch is retained, never normalized away.
    mismatch = {('mu', 0): F(1)}
    assert g.project(2, g.include(2, mismatch)) == mismatch
    assert g.route(2, mismatch, 'E') != g.route(2, mismatch, 'P')
    for edge in g.fb[1]:
        assert not g.defect(g.project(2, g.df({edge: F(1)})))
    # Concrete comparison input reproduces the earlier 1/6 discrepancy.
    v = {(g.squares[0][0],): F(1)}; area = {('Omega', 0): F(1)}
    result = g.project(2, multiply(g.include(0, v), g.include(2, area), g.fs, 'Whitney'))
    assert result == {('Omega', 0): F(1, 4), ('mu', 0): F(1, 6)}
    assert g.route(2, result, 'E') == {('Omega', 0): F(1, 3)}
    assert g.route(2, result, 'P') == {('Omega', 0): F(1, 6)}
    # Explain the defect on all four records in every square, not just v0.
    interpolation_checks = 0
    for j, square in enumerate(g.squares):
        for t, vertex in enumerate(square):
            out = g.operation(0, {(vertex,): F(1)}, 2, {('Omega', j): F(1)})
            assert out == {('Omega', j): F(1, 4), ('mu', j): F((-1)**t, 6)}
            interpolation_checks += 1
    # A constant probe produces no route discrepancy; the product retains every
    # mismatch coordinate as well as every ordinary square coordinate.
    unit = {s: F(1) for s in g.rb[0]}
    for k, basis in enumerate(g.rb):
        for s in basis:
            x = {s: F(1)}
            assert g.operation(0, unit, k, x) == x == g.operation(k, x, 0, unit)
    # The seven global periods together with 36 mismatches classify top-degree
    # rational cochains modulo exact ones: rank43 + image(d1)rank29 = 72.
    periods = [z+[F(0)]*36 for z in cycles]
    periods += [[F(0)]*36+[F(i == j) for i in range(36)] for j in range(36)]
    assert rank(periods) == 43 and rank(periods)+d1rank == len(g.rb[2])
    # Each route is a subdivision of the same global square complex.
    route_info = {r: complex_info(faces([t for ts in g.triangles for t in ts[sl]]))
                  for r, sl in [('E', slice(0, 2)), ('P', slice(2, 4))]}
    assert all(v['betti'] == [1, 0, 7] for v in route_info.values())
    packet = {
        'schema': 'su32.global-comparison.v1', 'passed': True,
        'classification': 'global rational-cochain comparison with retained mismatch channels; not native dynamics',
        'fineComplex': complex_info(g.fine), 'routeComplexes': route_info,
        'commonSquareComplex': {'dimensions': list(map(len, g.qb)), 'differentialRanks': [31, d1rank], 'betti': [1, 0, 7]},
        'retainedComparisonCarrier': {'dimensions': list(map(len, g.rb)), 'betti': [1, 0, 43],
            'split': 'ordinary square cochains plus 36 degree-two route-mismatch coordinates'},
        'checks': {'fineBasisContractionsAndRecovery': contractions, 'globalHigherComparisonBasisPairs': higher_checks,
                   'signBindingCovariance': frame_checks, 'globalCycleBasis': len(cycles),
                   'fourRecordInterpolationChecks': interpolation_checks, 'twoSidedUnitChecks': 2*sum(map(len, g.rb)),
                   'independentTopDegreePeriods': 43},
        'example': {'square': g.squares[0], 'input': 'vertex-0 cochain times square face cochain',
                    'mean': '1/4', 'mismatch': '1/6', 'E_readout': '1/3', 'P_readout': '1/6'},
        'hostiles': {'eraseMismatch': 'mu=1 distinguishes E and P while preserving all vertex records',
                     'eraseGlobalPeriods': {'mu': 0, 'faceIndex': j, 'period': str(z[j]), 'cycle': list(map(str, z))},
                     'eraseAcyclicWitnesses': 'recovery requires both Kx and Kdx in addition to the reduced packet'},
        'fourRecordFormula': {'mean': '(f0+f1+f2+f3)*Omega/4',
                              'mismatch': '(f0-f1+f2-f3)*Omega/6',
                              'meaning': 'Different vertex incidence multiplicities in the two triangulations, not an inferred phase'},
        'sourceChoice': 'Symmetric rational interpolation, integrated Whitney product; chart orientations retained, no global static signs assumed',
        'residuals': ['native payload algebra and assignment of edge/face cochains remain unbound',
                      'binary higher comparison constructed; full higher associativity/BV action not constructed',
                      'no native involution lift, phase holonomy or Hopf class inferred'],
        'sources': source['sourceHashes'],
        'checkerHashes': {str(Path(p)): hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in
            ['research/strominger/checkers/check_su32_global_comparison.py',
             'research/strominger/checkers/check_su32_cochain_transfer.py']}}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/'verification.json').write_text(json.dumps(packet, indent=2)+'\n', encoding='utf8')
    (OUT/'square-carrier.json').write_text(json.dumps({'vertices': source['vertices'], 'edges': g.edges,
        'squares': [{'chartId': c['chartId'], 'boundary': q, 'target': c['target']}
                    for c, q in zip(g.charts, g.squares)], 'cycleBasis': [list(map(str, z)) for z in cycles]}, indent=2)+'\n', encoding='utf8')
    print(json.dumps(packet, indent=2))


if __name__ == '__main__':
    main()
