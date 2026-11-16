#!/usr/bin/env python3
"""An exact, independently checkable finite certificate of R(3,7) <= 23,
conditional only on the standard e(3,6,17)>=40 bound used to deduce
6-regularity of any hypothetical (3,7)-graph of order 23.

Graph-theoretic constraints (all NECESSARY):
  S = N(v), |S|=6, T=other 16, sigma(t)=N(t) cap S.
  1 <= |sigma(t)| <= 3 (upper bound from R(3,5)=14 and R(3,4)=9).
  Each s in S occurs in five supports, with 6-regularity.
  A red edge tu is allowed only when supports are disjoint.
  Each t needs 6-|sigma(t)| red neighbors in T.
  For |U|<=5 and |union sigma(U)|<|U|, U needs a red edge.
  Any triangle of available red edges must have >=1 missing edge.

An actual graph would give x_e in {0,1}. The certificate proves that
these conditions are impossible even over REAL 0<=x_e<=1.

The records are rational LP dual witnesses, verified using only Python's
standard library. Generation ('--generate') uses SciPy HiGHS; verification
('--verify', default) does not use a numerical solver.

This is a finite, independently reconstructible upper-bound certificate,
NOT a new source-derived connection to the original Ramsey symplectic
cloning conjecture and NOT a short classification-free mathematical proof.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations
import argparse
import gzip
import json
from pathlib import Path

S = tuple(range(6))
PAIRS = tuple(combinations(S, 2))
TRIPLES = tuple(combinations(S, 3))
PAIR_MASKS = tuple(sum(1 << x for x in pair) for pair in PAIRS)
TRIPLE_MASKS = tuple(sum(1 << x for x in tri) for tri in TRIPLES)
HERE = Path(__file__).resolve().parent
CERT_FILE = HERE / 'ramsey_fractional_witness_certificates.json.gz'
EXPECTED = [79, 922, 6028, 27690, 103975]


def change_mask(m, p):
    return sum(1 << p[j] for j in S if (m >> j) & 1)


def permutations_preserving_singletons(r):
    k = r + 2
    return [p + q for p in permutations(range(k))
                  for q in permutations(range(k, 6))]


def pair_multisets(degrees, singleton_set):
    caps = tuple(1 if a in singleton_set or b in singleton_set else 2
                 for a, b in PAIRS)
    remaining = list(degrees)
    counts = [0] * len(PAIRS)
    def rec(j):
        if j == len(PAIRS):
            if not any(remaining):
                yield tuple(counts)
            return
        a, b = PAIRS[j]
        for k in range(min(caps[j], remaining[a], remaining[b]) + 1):
            remaining[a] -= k
            remaining[b] -= k
            counts[j] = k
            if all(remaining[i] <= sum(caps[l] for l in range(j+1, len(PAIRS))
                                       if i in PAIRS[l]) for i in S):
                yield from rec(j+1)
            remaining[a] += k
            remaining[b] += k
    yield from rec(0)


def support_classes(r):
    """One representative per orbit under permutations preserving singleton sites.
    No selection is made by checking whether a resulting red graph succeeds.
    """
    ps = permutations_preserving_singletons(r)
    singletons = set(range(r + 2))
    triple_multisets = {tuple(sorted(seq))
                        for seq in combinations_with_replacement(TRIPLE_MASKS, r)}
    classes = set()
    triple_orbits = 0
    while triple_multisets:
        trio = min(triple_multisets)
        orbit = {tuple(sorted(change_mask(t, p) for t in trio)) for p in ps}
        triple_multisets.difference_update(orbit)
        stabilizer = [p for p in ps
                      if tuple(sorted(change_mask(t, p) for t in trio)) == trio]
        triple_orbits += 1
        degrees = [5 - int(i in singletons)
                   - sum((t >> i) & 1 for t in trio) for i in S]
        if min(degrees) < 0:
            continue
        seen_pairs = set()
        for mult in pair_multisets(degrees, singletons):
            pairm = tuple(sorted(mask for mask, count in zip(PAIR_MASKS, mult)
                                 for _ in range(count)))
            if pairm in seen_pairs:
                continue
            seen_pairs.update(tuple(sorted(change_mask(t, p) for t in pairm))
                              for p in stabilizer)
            support = tuple(sorted([1 << i for i in singletons]
                                   + list(pairm) + list(trio)))
            assert len(support) == 16
            assert all(sum((t >> i) & 1 for t in support) == 5 for i in S)
            classes.add(support)
    return sorted(classes), triple_orbits


def constraints(masks):
    """Construct the relaxation, as row tags and source-derived edge IDs.

    H: -sum_{e subset U} x_e - z <= -1, for bad small U.
    T:  sum_{e in triangle} x_e <= 2, for candidate triangles.
    E:  sum_{e incident i} x_e = 6-|sigma_i|.
    0 <= x_e <=1, z >=0.
    """
    edges = tuple(e for e in combinations(range(16), 2)
                  if not (masks[e[0]] & masks[e[1]]))
    eindex = {e: i for i, e in enumerate(edges)}
    hall = []
    for k in (2, 3, 4, 5):
        for subset in combinations(range(16), k):
            union = 0
            for j in subset:
                union |= masks[j]
            if union.bit_count() < k:
                hall.append((subset, tuple(eindex[e] for e in combinations(subset, 2)
                                           if e in eindex)))
    triangle = []
    for subset in combinations(range(16), 3):
        if all(e in eindex for e in combinations(subset, 2)):
            triangle.append((subset, tuple(eindex[e] for e in combinations(subset, 2))))
    return edges, hall, triangle


def rational(s):
    return Fraction(s)


def verify_entry(record):
    """Check the complete dual lower bound over Q, with no LP solver."""
    r = record['r']
    m = tuple(record['supports'])
    assert len(m) == 16
    assert all(sum(t.bit_count() == k for t in m) == expected
               for k,expected in ((1,2+r),(2,14-2*r),(3,r))), (r,m)
    assert set(t for t in m if t.bit_count() == 1) == set(1 << i for i in range(r+2))
    assert all(sum((t >> j) & 1 for t in m) == 5 for j in S)
    edges, hall, triangle = constraints(m)
    eindex = {e:j for j,e in enumerate(edges)}
    hmap = {t: idx for t,idx in hall}
    tmap = {t: idx for t,idx in triangle}
    M = len(edges)
    # c_j - sum(y_i * A_ij) - sum(t_i * E_ij) - upper_j = lower_j >= 0.
    left = [Fraction(0) for _ in range(M)] + [Fraction(1)]
    degree_duals = [rational(x) for x in record['degree_duals']]
    assert len(degree_duals) == 16
    for j, (a,b) in enumerate(edges):
        left[j] -= degree_duals[a] + degree_duals[b]
    bound = sum(degree_duals[j] * (6 - m[j].bit_count()) for j in range(16))
    for typ, subset, val in record['inequality_duals']:
        y = rational(val)
        assert y <= 0
        subset = tuple(subset)
        if typ == 'H':
            idx = hmap[subset]
            # A row is -sum(x_e) - z <= -1.
            for j in idx:
                left[j] += y
            left[-1] += y
            bound -= y
        elif typ == 'T':
            idx = tmap[subset]
            for j in idx:
                left[j] -= y
            bound += 2*y
        else:
            raise ValueError('unknown constraint')
    for e, val in record['upper_duals']:
        e = tuple(e)
        assert e in eindex
        y = rational(val)
        assert y <= 0
        left[eindex[e]] -= y
        bound += y
    assert all(val >= 0 for val in left), (r, m, 'invalid dual stationarity')
    assert bound > 0, (r, m, 'no positive contradiction')
    assert bound == rational(record['bound']), (r,m,'incorrect bound')
    return bound


def derive_dual_certificate(masks):
    """Use a numerical LP only to DISCOVER a rational dual; exact verify is mandatory."""
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import lil_matrix
    edges, hall, triangle = constraints(masks)
    M = len(edges)
    numrows = len(hall) + len(triangle)
    A = lil_matrix((numrows, M+1), dtype=float)
    b = np.zeros(numrows)
    for i, (U, indices) in enumerate(hall):
        b[i] = -1
        A[i,M] = -1
        for j in indices:
            A[i,j] = -1
    for k, (U,indices) in enumerate(triangle):
        i = len(hall) + k
        b[i] = 2
        for j in indices:
            A[i,j] = 1
    E = lil_matrix((16,M+1),dtype=float)
    for j,(a,bb) in enumerate(edges):
        E[a,j]=1
        E[bb,j]=1
    d = [6-x.bit_count() for x in masks]
    c=np.zeros(M+1);c[-1]=1
    ans=linprog(c, A_ub=A.tocsr(), b_ub=b, A_eq=E.tocsr(), b_eq=d,
                bounds=[(0,1)]*M+[(0,None)], method='highs')
    if ans.status != 0:
        raise RuntimeError(f'LP did not solve: {ans.status} {ans.message}')
    fraction=lambda f: str(Fraction(float(f)).limit_denominator(1000000))
    inequalities = []
    for i,y in enumerate(ans.ineqlin.marginals):
        if abs(y) < 1e-9:continue
        typ = 'H' if i < len(hall) else 'T'
        subset = hall[i][0] if typ == 'H' else triangle[i-len(hall)][0]
        inequalities.append([typ, list(subset), fraction(y)])
    record = {
        'supports':list(masks),
        'degree_duals':[fraction(v) for v in ans.eqlin.marginals],
        'inequality_duals':inequalities,
        'upper_duals':[[list(edges[j]),fraction(v)]
                       for j,v in enumerate(ans.upper.marginals[:M]) if abs(v)>1e-9]
    }
    # Deduce the right-hand side EXACTLY, then check the dual with no floating arithmetic.
    temp = dict(record, bound='1')
    # The following 'bound' recomputes from the signed coefficients directly.
    bound = sum(Fraction(temp['degree_duals'][j]) * (6 - masks[j].bit_count()) for j in range(16))
    for typ, U, y in inequalities:
        bound += (-Fraction(y) if typ == 'H' else 2*Fraction(y))
    for e,y in record['upper_duals']:
        bound+=Fraction(y)
    record['bound']=str(bound)
    return record


def orbit_weight(masks, permutations_):
    return len({tuple(sorted(change_mask(t,p) for t in masks)) for p in permutations_})


def generate(path):
    from time import perf_counter
    start=perf_counter()
    records=[]
    profile_counts=[]
    stats=[]
    for r in range(5):
        classes, triple_orbits = support_classes(r)
        perms = permutations_preserving_singletons(r)
        weight_sum=sum(orbit_weight(m,perms) for m in classes)
        assert weight_sum == EXPECTED[r], (r,weight_sum)
        num_with_triangle=0
        for masks in classes:
            rec = derive_dual_certificate(masks)
            rec['r']=r
            bound=verify_entry(rec)
            num_with_triangle += any(x[0]=='T' for x in rec['inequality_duals'])
            records.append(rec)
        profile_counts.append(len(classes))
        stats.append({'r':r,'triple_orbits':triple_orbits,'support_classes':len(classes),
                      'labelled_support_multisets':weight_sum,
                      'dual_uses_triangle':num_with_triangle})
        print('r=',r,'classes=',len(classes),'labelled=',weight_sum,
              'dual_uses_triangle=',num_with_triangle,'elapsed_s=',round(perf_counter()-start,1),flush=True)
    result={'schema':'ramsey.3-7.fractional-support-obstruction.v1',
            'hypothesis':'Any hypothetical counterexample has 23 vertices, red K3 free, blue K7 free, all vertices degree 6.',
            'labelled_support_multisets_by_r':EXPECTED,
            'classes_by_r':profile_counts,
            'stats':stats,'certificates':records}
    with gzip.open(path,'wt',encoding='utf-8',compresslevel=9) as fp:
        json.dump(result,fp,sort_keys=True,separators=(',',':'))
    print('Generated',path,'certificates=',len(records),'bytes=',path.stat().st_size)
    return result


def verify(path):
    with gzip.open(path,'rt',encoding='utf-8') as fp:
        data=json.load(fp)
    assert data['schema']=='ramsey.3-7.fractional-support-obstruction.v1'
    all_classes=[]
    counts=[]
    for r in range(5):
        classes,triple_orbits=support_classes(r)
        assert sum(orbit_weight(m,permutations_preserving_singletons(r)) for m in classes)==EXPECTED[r]
        counts.append(len(classes))
        all_classes += [(r,m) for m in classes]
    assert data['classes_by_r']==counts
    assert data['labelled_support_multisets_by_r']==EXPECTED
    certificates={(rec['r'],tuple(rec['supports'])):rec for rec in data['certificates']}
    assert len(certificates)==len(all_classes)
    assert set(certificates)==set(all_classes)
    bounds=[]
    for key in all_classes:
        bounds.append(verify_entry(certificates[key]))
    assert min(bounds)>0
    print('VERIFIED: 5 profiles,',len(all_classes), 'isomorphism classes,',
          sum(EXPECTED),'labelled support multisets;')
    print('Every class has an exact rational linear inequality forcing a positive slack.')
    print('Minimum dual bound:',min(bounds),'Maximum:',max(bounds))
    print('This rules out the hypothetical 6-regular 23-vertex (3,7)-graph.')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--generate',action='store_true',help='Generate LP candidates, then verify rational duals (requires SciPy).')
    parser.add_argument('--file',type=Path,default=CERT_FILE)
    args=parser.parse_args()
    if args.generate:generate(args.file)
    verify(args.file)
