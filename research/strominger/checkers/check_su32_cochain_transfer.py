"""Exact support-cochain construction; no physical field or BV action inferred."""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'research/strominger/results/su32-cochain-transfer-v1'


def add(*xs):
    out = {}
    for x in xs:
        for s, v in x.items():
            out[s] = out.get(s, F(0)) + v
    return {s: v for s, v in out.items() if v}


def scale(c, x):
    return {s: c*v for s, v in x.items() if c*v}


def faces(facets):
    return sorted({s for t in facets for n in range(1, len(t)+1)
                   for s in combinations(sorted(t), n)}, key=lambda s: (len(s), s))


def differential(x, basis):
    return {t: v for t in basis if len(t) > 1
            if (v := sum((-1)**j * x.get(t[:j]+t[j+1:], F(0))
                         for j in range(len(t))))}


def parity(seq):
    return (-1)**sum(a > b for i, a in enumerate(seq) for b in seq[i+1:])


def oriented(seq):
    return {tuple(sorted(seq)): F(parity(seq))}


def boundary(chain):
    return add(*({s[:j]+s[j+1:]: (-1)**j*v}
                 for s, v in chain.items() for j in range(len(s))))


def multiply(x, y, basis_set, mode):
    out = {}
    for a, av in x.items():
        for b, bv in y.items():
            t = tuple(sorted(set(a) | set(b)))
            if t not in basis_set or len(t) != len(a)+len(b)-1:
                continue
            if mode == 'AW':
                c = F(int(a[-1] == b[0] and a+b[1:] == t))
            else:
                common = set(a) & set(b)
                if len(common) != 1:
                    continue
                v = next(iter(common))
                seq = tuple(w for w in a if w != v)+(v,)+tuple(w for w in b if w != v)
                sign = (-1)**(len(a)-1-a.index(v)+b.index(v))*parity(seq)
                c = F(sign*factorial(len(a)-1)*factorial(len(b)-1), factorial(len(t)))
            out[t] = out.get(t, F(0)) + c*av*bv
    return {s: v for s, v in out.items() if v}


def zero(r, c):
    return [[F(0) for _ in range(c)] for _ in range(r)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def mm(a, b):
    assert len(a[0]) == len(b)
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def ma(a, b, sign=1):
    return [[x+sign*y for x, y in zip(r, s)] for r, s in zip(a, b)]


def rank(a):
    a = [[F(x) for x in row] for row in a]
    if not a:
        return 0
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][col]
        a[r] = [x/q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col]:
                q = a[i][col]
                a[i] = [x-q*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def complex_info(basis):
    levels = [[s for s in basis if len(s) == k+1] for k in range(3)]
    ds = [[[sum((-1)**j for j in range(len(t)) if t[:j]+t[j+1:] == s)
            for s in levels[k]] for t in levels[k+1]] for k in range(2)]
    ranks = list(map(rank, ds))
    dims = list(map(len, levels))
    return {'dimensions': dims, 'differentialRanks': ranks,
            'betti': [dims[k] - ([0]+ranks)[k] - (ranks+[0])[k] for k in range(3)]}


def contraction(start, lam):
    # Oriented square edges 01,12,23,30; diagonal start -> start+2.
    d0 = zero(4, 4)
    for j in range(4):
        d0[j][j], d0[j][(j+1) % 4] = -F(1), F(1)
    coarse = [d0, [[F(1)]*4]]
    fd0 = [r[:] for r in d0] + [[F(j == (start+2) % 4)-F(j == start) for j in range(4)]]
    fd1 = zero(2, 5)
    for j in [start, (start+1) % 4]:
        fd1[0][j] = 1
    for j in [(start+2) % 4, (start+3) % 4]:
        fd1[1][j] = 1
    fd1[0][4], fd1[1][4] = -F(1), F(1)
    fine = [fd0, fd1]
    inclusion1 = eye(4)+[[F(0)]*4]
    for j in range(4):
        inclusion1[4][j] = 1-lam if j in [start, (start+1) % 4] else -lam
    inc = [eye(4), inclusion1, [[lam], [1-lam]]]
    proj = [eye(4), [r+[F(0)] for r in eye(4)], [[F(1), F(1)]]]
    h = [None, zero(4, 5), zero(5, 2)]
    h[2][4] = [-(1-lam), lam]
    assert mm(coarse[1], coarse[0]) == zero(1, 4)
    assert mm(fine[1], fine[0]) == zero(2, 4)
    for k in range(2):
        assert mm(fine[k], inc[k]) == mm(inc[k+1], coarse[k])
        assert mm(coarse[k], proj[k]) == mm(proj[k+1], fine[k])
    for k, n in enumerate([4, 4, 1]):
        assert mm(proj[k], inc[k]) == eye(n)
    for k, n in enumerate([4, 5, 2]):
        lhs = zero(n, n)
        if k:
            lhs = ma(lhs, mm(fine[k-1], h[k]))
        if k < 2:
            lhs = ma(lhs, mm(h[k+1], fine[k]))
        assert lhs == ma(eye(n), mm(inc[k], proj[k]), -1)
    assert mm(h[1], h[2]) == zero(4, 2)
    assert mm(proj[1], h[2]) == zero(4, 2)
    assert mm(h[2], inc[2]) == zero(5, 1)
    # Deleting the homotopy fails on the contractible internal mode.
    assert ma(eye(2), mm(inc[2], proj[2]), -1) != zero(2, 2)
    return inc, proj, h


def main():
    subprocess.run(['node', 'research/strominger/checkers/export_su32_comparison_support.mjs'],
                   cwd=ROOT, check=True, capture_output=True, text=True)
    src = json.loads((OUT/'support.json').read_text(encoding='utf8'))
    for p, h in src['sourceHashes'].items():
        assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest() == h
    basis = faces(src['facets'])
    bs = set(basis)
    # Cache the sparse basis differential; repeatedly scanning every coface for
    # zero products makes the exhaustive bilinear test needlessly cubic.
    db = {s: differential({s: F(1)}, basis) for s in basis}
    d = lambda x: add(*(scale(v, db[s]) for s, v in x.items()))
    mul = lambda a, b, mode: multiply(a, b, bs, mode)
    units = [{s: F(1)} for s in basis]
    unit = {(v,): F(1) for v in src['vertices']}
    leibniz = 0
    for a, x in zip(basis, units):
        assert not d(d(x))
        for mode in ['AW', 'Whitney']:
            assert mul(unit, x, mode) == x == mul(x, unit, mode)
            for y in units:
                assert d(mul(x, y, mode)) == add(mul(d(x), y, mode), scale((-1)**(len(a)-1), mul(x, d(y), mode)))
                leibniz += 1
    # Products only use faces of the output simplex. These local basis triples
    # exhaust all potentially nonzero global associativity coefficients.
    associativity = 0
    for t in src['facets']:
        local = faces([t])
        for a, b, c in product(local, repeat=3):
            x, y, z = ({s: F(1)} for s in [a, b, c])
            assert mul(mul(x, y, 'AW'), z, 'AW') == mul(x, mul(y, z, 'AW'), 'AW')
            associativity += 1
    restriction_checks = 0
    for occurrence in src['occurrences']:
        local = faces([s['refs'] for s in occurrence['supports']])
        ls = set(local)
        restrict = lambda x: {s: v for s, v in x.items() if s in ls}
        assert len(local) == 14  # 4 vertices, 6 edges, 4 triangles.
        # One global rational vertex field, not separately fitted local values.
        field = {(v,): F(value) for v, value in src['globalField'].items()}
        assert restrict(d(field)) == differential(restrict(field), local)
        for a in local:
            x = {a: F(1)}
            assert restrict(d(x)) == differential(x, local)
            for b in local:
                y = {b: F(1)}
                for mode in ['AW', 'Whitney']:
                    assert restrict(mul(x, y, mode)) == multiply(x, y, ls, mode)
                    restriction_checks += 1
    # Compare the actual two route-disks as chains, retaining their difference.
    cycles = {}
    for occurrence in src['occurrences']:
        q = occurrence['square']
        disk_e = add(oriented([q[i] for i in [0, 1, 2]]), oriented([q[i] for i in [0, 2, 3]]))
        disk_p = add(oriented([q[i] for i in [0, 1, 3]]), oriented([q[i] for i in [1, 2, 3]]))
        assert boundary(disk_e) == boundary(disk_p)
        cycle = add(disk_e, scale(-1, disk_p))
        assert len(cycle) == 4 and not boundary(cycle)
        first = min(cycle)
        cycle = scale(1/cycle[first], cycle)
        cycles[tuple(sorted(cycle.items()))] = cycle
    triangles = [s for s in basis if len(s) == 3]
    cycle_rank = rank([[z.get(s, F(0)) for z in cycles.values()] for s in triangles])
    global_info = complex_info(basis)
    assert cycle_rank == len(cycles)
    residual_h2 = global_info['betti'][2] - cycle_rank
    assert residual_h2 >= 0
    edge = next(s for s in basis if len(s) == 2)
    v, e = {(edge[0],): F(1)}, {edge: F(1)}
    assert mul(v, e, 'AW') == e
    assert not mul(e, v, 'AW')
    assert mul(v, e, 'Whitney') == scale(F(1, 2), e)
    associator = add(mul(mul(v, v, 'Whitney'), e, 'Whitney'),
                     scale(-1, mul(v, mul(v, e, 'Whitney'), 'Whitney')))
    assert associator == scale(F(1, 4), e)
    params = [F(0), F(1, 3), F(1, 2), F(2, 3), F(1)]
    packages = {(r, a): contraction(r, a) for r in [0, 1] for a in params}
    for a, b in product(params, repeat=2):
        ie, pe, _ = packages[0, a]
        ip, pp, _ = packages[1, b]
        for k in range(3):
            ep, back = mm(ip[k], pe[k]), mm(ie[k], pp[k])
            assert mm(back, ep) == mm(ie[k], pe[k])
            assert mm(ep, back) == mm(ip[k], pp[k])
    # Transfer the Whitney binary product through each diagonal at lambda=1/2.
    # The products differ, but an explicit boundary-relative bilinear homotopy
    # compares them. This is a first higher comparison, not a full BV action.
    dims = [4, 4, 1]
    def zeros(k):
        return [F(0)] * (dims[k] if 0 <= k <= 2 else 0)
    def cd(k, x):
        if k == 0:
            return [x[(j+1) % 4]-x[j] for j in range(4)]
        return [sum(x)] if k == 1 else []
    def transferred(start, p, x, q, y):
        if p+q > 2:
            return []
        inc, proj, _ = packages[start, F(1, 2)]
        r = lambda j: (start+j) % 4
        cells = [[(j,) for j in range(4)],
                 [(0, 1), (1, 2), (2, 3), (3, 0), (r(0), r(2))],
                 [(r(0), r(1), r(2)), (r(0), r(2), r(3))]]
        fb = set(faces(cells[2]))
        def encode(k, v):
            return add(*(scale(c, oriented(s)) for s, c in zip(cells[k], v)))
        value = multiply(encode(p, mv(inc[p], x)), encode(q, mv(inc[q], y)), fb, 'Whitney')
        fine = [parity(s)*value.get(tuple(sorted(s)), F(0)) for s in cells[p+q]]
        return mv(proj[p+q], fine)
    def homotopy(p, x, q, y):
        linear = lambda w: -(w[0]+w[2])/6
        if (p, q) == (1, 2):
            return [linear(x)*y[0]]
        if (p, q) == (2, 1):
            return [x[0]*linear(y)]
        return zeros(p+q-1)
    higher_checks = 0
    for p, q in product(range(3), repeat=2):
        for x, y in product(eye(dims[p]), eye(dims[q])):
            left = transferred(0, p, x, q, y)
            right = transferred(1, p, x, q, y)
            delta = [a-b for a, b in zip(left, right)]
            dh = cd(p+q-1, homotopy(p, x, q, y)) if p+q else zeros(0)
            hd1 = homotopy(p+1, cd(p, x), q, y)
            hd2 = homotopy(p, x, q+1, cd(q, y))
            rhs = [a+b+(-1)**p*c for a, b, c in zip(dh, hd1, hd2)]
            assert delta == rhs, (p, q, x, y, delta, rhs)
            higher_checks += 1
    f0, omega = eye(4)[0], [F(1)]
    assert transferred(0, 0, f0, 2, omega) == [F(1, 3)]
    assert transferred(1, 0, f0, 2, omega) == [F(1, 6)]
    assert homotopy(1, cd(0, f0), 2, omega) == [F(1, 6)]
    # H has only face-valued outputs: it restricts to zero on every boundary edge.
    assert homotopy(1, eye(4)[0], 2, omega) == [F(-1, 6)]
    # The same native support and differential admit distinct contraction choices.
    assert packages[0, F(0)][0][1] != packages[0, F(1, 2)][0][1]
    sphere = complex_info(faces(list(combinations(range(4), 3))))
    circle = complex_info(faces([(0, 1), (1, 2), (2, 3), (0, 3)]))
    assert sphere['betti'] == [1, 0, 1] and circle['betti'] == [1, 1, 0]
    # A corrupted orientation must spoil d^2 on this actual support triangle.
    t = tuple(src['facets'][0]); local = faces([t])
    cob = differential({(t[0],): F(1)}, local)
    assert cob[(t[0], t[1])] != 0
    wrong_second_d = differential(cob, local).get(t, F(0)) + 2*cob[(t[0], t[1])]
    assert wrong_second_d != 0
    paths = ['research/strominger/checkers/check_su32_cochain_transfer.py',
             'research/strominger/checkers/export_su32_comparison_support.mjs',
             'references/Towards_simplicial_CS.pdf']
    report = {
        'passed': True, 'schema': 'su32.cochain-transfer.v1',
        'classification': 'exact global support cochains and conditional two-route contractions; not native BV dynamics',
        'globalComplex': global_info, 'sourceOccurrences': len(src['occurrences']),
        'routeDifferenceCycles': {'uniqueUpToSign': len(cycles), 'rank': cycle_rank,
                                 'globalH2ModuloTheirSpan': residual_h2,
                                 'interpretation': 'Support-complex classes only. Killing local cycles by hypothetical 3-cell attachments still leaves this many H2 classes; no native fillers attached.'},
        'globalField': 'one rational value per reference-cell identity, then restricted',
        'leibnizBasisChecks': leibniz, 'AWAssociativityLocalBasisChecks': associativity,
        'restrictionProductChecks': restriction_checks,
        'contractionParametersTested': list(map(str, params)), 'contractionPackages': len(packages),
        'twoRouteParameterPairs': len(params)**2,
        'transferredWhitneyComparison': {'basisHomotopyChecks': higher_checks,
            'vertex0TimesFace': {'E': '1/3', 'P': '1/6', 'difference': '1/6'},
            'identity': 'mE-mP = dH + H(d tensor 1 + 1 tensor d), with Koszul signs',
            'H': 'H(w,Omega)=L(w)Omega; H(Omega,w)=Omega L(w); L(w)=-(w01+w23)/6; zero otherwise',
            'boundaryRelative': True, 'scope': 'binary-product comparison at symmetric lambda=1/2; not full higher coherence'},

        'hostiles': {'WhitneyStrictAssociativity': {'edge': edge, 'residual': '1/4 times edge cochain'},
                     'AWEqualsWhitney': {'AWVertexEdge': '1', 'WhitneyVertexEdge': '1/2'},
                     'deletedHomotopy': 'nonzero id-iI on internal face mode',
                     'uniqueContractionFromIncidence': 'lambda=0 and lambda=1/2 differ with identical boundary data',
                     'orientationCorruption': str(wrong_second_d),
                     'sphereToFilledSquareContraction': 'H2 dimensions 1 versus 0',
                     'diskToUnfilledBoundaryContraction': 'H1 dimensions 0 versus 1'},
        'localSphere': sphere, 'localBoundaryCircle': circle,
        'chosenData': ['rational linearization', 'global reference-ID order for AW',
                       'Whitney interpolation rule for alternative product',
                       'common filled-square comparison target and contraction parameter'],
        'residuals': ['support complex is not identified with spatial vertex-link triangulation',
                      'no source-selected product or contraction parameter',
                      'no simultaneously sewn cross-cone contraction',
                      'Whitney higher associativity products and BV quantum action not implemented',
                      'no phase connection or native Hopf class derived'],
        'sourceHashes': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    (OUT/'verification.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
