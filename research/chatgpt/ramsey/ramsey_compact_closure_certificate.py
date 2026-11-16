"""Compact exact Ramsey R(3,7) local-incidence obstruction certificate.

CONDITIONAL theorem: assuming a 23-vertex (3,7)-admissible coloring is
6-regular in A, its neighborhood support system cannot exist.

Checks all 2,806 normalized support patterns using three universal
integer propagation rules; the 11 remaining patterns are rejected by
stored nonnegative integer Farkas multipliers on degree and Hall demands.
No numerical optimizers, graph catalogs, or third-party libraries required.
The 6-regular reduction is NOT established by this script.
"""
from itertools import combinations, combinations_with_replacement, permutations, product
from collections import Counter, defaultdict
import json
LABELS=tuple(range(6))
PAIRS=tuple(combinations(LABELS,2))
def low_support_cases(n3, n4):
    # The zero-/single-high-support cases have exactly n1 singleton supports.
    assert (n3,n4) in {(0,0),(1,0),(0,1)}
    n1=2+n3+2*n4
    n2=14-2*n3-3*n4
    if (n3,n4)==(0,0): high=[()]
    elif (n3,n4)==(1,0):
        high=[(3,4,5),(0,3,4),(0,1,3),(0,1,2)]
    else: high=[(2,3,4,5),(1,2,3,4),(0,1,2,3)]
    singles=tuple(frozenset((i,)) for i in range(n1))
    repeatable=tuple(p for p in PAIRS if not(set(p)&set(range(n1))))
    other=tuple(p for p in PAIRS if p not in repeatable)
    for Q in high:
        pair_degree=[5-int(i<n1)-int(i in Q) for i in LABELS]
        for bits in product((0,1),repeat=len(other)):
            for multi in product((0,1,2),repeat=len(repeatable)):
                mult=dict(zip(other,bits));mult.update(zip(repeatable,multi))
                if sum(mult.values()) != n2:continue
                if any(sum(mult[p] for p in PAIRS if i in p)!=pair_degree[i] for i in LABELS):continue
                yield (n3,n4), singles+((frozenset(Q),) if Q else ())+tuple(frozenset(p) for p in PAIRS for _ in range(mult[p]))

def high_orbit_representatives(n3,n4):
    # Permuting singleton labels and nonsingleton labels preserves the canonical
    # placement of the n1 distinct singleton-supported vertices.
    n1=2+n3+2*n4
    sing=tuple(range(n1));other=tuple(range(n1,6))
    h3=tuple(combinations_with_replacement(tuple(combinations(LABELS,3)),n3))
    h4=tuple(combinations_with_replacement(tuple(combinations(LABELS,4)),n4))
    ps=tuple(p+q for p,q in product(permutations(sing),permutations(other)))
    seen=set()
    for a in h3:
        for b in h4:
            h=tuple(sorted(tuple(sorted(x)) for x in a+b))
            if h in seen:continue
            orbit={tuple(sorted(tuple(sorted(p[i] for i in x)) for x in h)) for p in ps}
            rep=min(orbit)
            seen.update(orbit)
            yield tuple(frozenset(x) for x in rep)

def pair_tables():
    # All simple pair sets plus the sole potentially doubled pair when n1=4.
    for n1 in (4,5,6):
        table=defaultdict(list)
        for mask in range(1<<len(PAIRS)):
            degrees=[0]*6;pp=[]
            for j,p in enumerate(PAIRS):
                if mask>>j&1:
                    degrees[p[0]]+=1;degrees[p[1]]+=1
                    pp.append(frozenset(p))
            table[tuple(degrees)].append(tuple(pp))
            if n1==4 and mask>>PAIRS.index((4,5))&1:
                d=degrees.copy();d[4]+=1;d[5]+=1
                table[tuple(d)].append(tuple(pp)+(frozenset((4,5)),))
        yield n1,table

def high_support_cases(n3,n4,table):
    n1=2+n3+2*n4;n2=14-2*n3-3*n4
    singles=tuple(frozenset((i,)) for i in range(n1))
    for hs in high_orbit_representatives(n3,n4):
        required=tuple(5-int(i<n1)-sum(i in q for q in hs) for i in LABELS)
        for pp in table.get(required,()):
            if len(pp)!=n2:continue
            yield (n3,n4),singles+hs+pp

def constraints(D, arity):
    n=len(D)
    edges=tuple(e for e in combinations(range(n),2) if D[e[0]].isdisjoint(D[e[1]]))
    indexes={e:i for i,e in enumerate(edges)}
    cap=tuple(6-len(d) for d in D)
    degm=tuple(sum(1<<i for i,e in enumerate(edges) if u in e) for u in range(n))
    trim=[]
    for tri in combinations(range(n),3):
        ee=[indexes[e] for e in combinations(tri,2) if e in indexes]
        if len(ee)==3:trim.append(sum(1<<i for i in ee))
    hall=[]
    for size in range(2,min(arity,n)+1):
        for C in combinations(range(n),size):
            if len(set().union(*(D[i] for i in C)))>=size:continue
            mask=sum(1<<indexes[e] for e in combinations(C,2) if e in indexes)
            if not mask:return None,('uncoverable Hall set',C)
            hall.append(mask)
    # Remove Hall demands implied by another demand on a subset of edges.
    minimal=[]
    for mask in sorted(set(hall),key=int.bit_count):
        if not any(mask&sm == sm for sm in minimal):minimal.append(mask)
    return (edges,cap,degm,tuple(trim),tuple(minimal)),None

def propagate(system):
    edges, caps, degree_masks, triangle_masks, hall_masks = system
    full = (1<<len(edges))-1
    ones=zeros=0
    while True:
        old=(ones,zeros)
        # Exact vertex-degree completion.
        for mask,k in zip(degree_masks,caps):
            chosen=(mask&ones).bit_count()
            free=mask & (~(ones|zeros)&full)
            if chosen>k or chosen+free.bit_count()<k:return None
            if chosen==k:zeros|=free
            if chosen+free.bit_count()==k:ones|=free
        if ones&zeros:return None
        # Triangle avoidance.
        for mask in triangle_masks:
            chosen=(ones&mask).bit_count()
            if chosen==3:return None
            if chosen==2:zeros|=mask&(~(ones|zeros)&full)
        if ones&zeros:return None
        # Every deficient Hall set needs an A edge.
        for mask in hall_masks:
            if ones&mask:continue
            free=mask&(~(ones|zeros)&full)
            if not free:return None
            if free.bit_count()==1:ones|=free
        if ones&zeros:return None
        if (ones,zeros)==old:return ones,zeros


def residual_rows(system,ones,zeros):
    edges, caps, degree_masks, triangle_masks, hall_masks=system
    free=[j for j in range(len(edges)) if not ((ones|zeros)>>j&1)]
    def row(mask,sign=1):
        return {i:sign for i,j in enumerate(free) if mask>>j&1}
    rows=[]
    for mask,k in zip(degree_masks,caps):
        r=row(mask)
        if not r:continue
        remaining=k-(ones&mask).bit_count()
        rows.append((r,remaining))
        rows.append(({j:-v for j,v in r.items()},-remaining))
    for mask in hall_masks:
        if ones&mask:continue
        rows.append((row(mask,-1),-1))
    for j in range(len(free)):
        rows.append(({j:1},1))
    # No triangle constraints occur in these rational residual certificates:
    # their effects are already reflected in propagated zeros and ones.
    return len(free),rows


def check_exact_dual(system,ones,zeros,cert):
    n,rows=residual_rows(system,ones,zeros)
    y=dict(cert['weights'])
    assert all(0<=i<len(rows) and v>=0 for i,v in y.items())
    rhs=sum(v*rows[i][1] for i,v in y.items())
    assert rhs==cert['rhs'] and rhs<0,('rhs',rhs,cert['rhs'])
    lhs=[sum(v*rows[i][0].get(j,0) for i,v in y.items()) for j in range(n)]
    assert min(lhs,default=0)>=0,('coordinate',min(lhs))
    # If x>=0, rows_i*x<=rhs_i, then 0<= (y*A)*x<= y*b<0.

CERTIFICATES = [{'D': ['0', '1', '2', '3', '4', '0125', '345', '03', '04', '05', '13', '14', '15', '23', '24', '25'], 'weights': [[6, 1], [28, 1], [30, 1], [36, 1]], 'rhs': -2}, {'D': ['0', '1', '2', '3', '4', '5', '0123', '0145', '04', '05', '12', '13', '24', '25', '34', '35'], 'weights': [[0, 1], [4, 1], [6, 1], [28, 1], [29, 1], [30, 1], [31, 1], [32, 1], [37, 1], [41, 1], [42, 1]], 'rhs': -3}, {'D': ['0', '1', '2', '3', '4', '5', '0123', '0145', '02', '03', '14', '15', '24', '25', '34', '35'], 'weights': [[0, 1], [8, 1], [10, 1], [35, 1], [37, 1], [38, 1], [39, 1], [40, 1], [42, 1], [68, 1], [69, 1]], 'rhs': -3}, {'D': ['0', '1', '2', '3', '4', '5', '0123', '0145', '03', '05', '12', '14', '23', '25', '34', '45'], 'weights': [[0, 1], [2, 1], [4, 1], [6, 1], [8, 1], [10, 1], [13, 1], [15, 1], [36, 1], [37, 1], [38, 1], [40, 1], [41, 1], [42, 1], [43, 1], [44, 1], [46, 1], [47, 1], [48, 1], [49, 1], [50, 1], [55, 1], [123, 1], [124, 1]], 'rhs': -2}, {'D': ['0', '1', '2', '3', '4', '5', '0123', '0145', '02', '04', '13', '15', '23', '25', '34', '45'], 'weights': [[0, 1], [2, 1], [4, 1], [6, 1], [8, 1], [10, 1], [13, 1], [15, 1], [36, 1], [37, 1], [39, 1], [40, 1], [41, 1], [42, 1], [43, 1], [46, 1], [48, 1], [49, 1], [50, 1], [54, 1], [56, 1], [57, 1], [123, 1], [124, 1]], 'rhs': -2}, {'D': ['0', '1', '2', '3', '4', '5', '0123', '0145', '02', '05', '13', '14', '23', '24', '35', '45'], 'weights': [[0, 1], [2, 1], [4, 1], [6, 1], [8, 1], [10, 1], [13, 1], [15, 1], [36, 1], [37, 1], [38, 1], [40, 1], [43, 1], [44, 1], [45, 1], [46, 1], [48, 1], [49, 1], [50, 1], [54, 1], [56, 1], [57, 1], [123, 1], [124, 1]], 'rhs': -2}, {'D': ['0', '1', '2', '3', '4', '5', '0123', '0145', '03', '04', '12', '15', '23', '24', '35', '45'], 'weights': [[0, 1], [2, 1], [4, 1], [6, 1], [8, 1], [10, 1], [13, 1], [15, 1], [36, 1], [37, 1], [38, 1], [40, 1], [41, 1], [43, 1], [44, 1], [46, 1], [47, 1], [48, 1], [49, 1], [50, 1], [53, 1], [57, 1], [123, 1], [124, 1]], 'rhs': -2}, {'D': ['0', '1', '2', '3', '4', '5', '012', '013', '0245', '03', '14', '15', '24', '25', '34', '35'], 'weights': [[2, 1], [4, 1], [6, 1], [32, 1], [37, 1], [38, 1], [39, 1], [40, 1], [41, 1], [42, 1], [64, 1]], 'rhs': -3}, {'D': ['0', '1', '2', '3', '4', '5', '012', '013', '2345', '01', '05', '14', '24', '25', '34', '35'], 'weights': [[0, 1], [2, 1], [4, 1], [6, 1], [8, 1], [10, 1], [17, 1], [18, 1], [47, 1], [48, 1], [49, 1], [52, 1], [53, 1], [54, 1], [55, 1], [56, 1], [57, 1], [58, 1], [59, 1], [60, 1], [61, 1]], 'rhs': -1}, {'D': ['0', '1', '2', '3', '4', '5', '012', '013', '2345', '01', '04', '15', '24', '25', '34', '35'], 'weights': [[0, 1], [2, 1], [4, 1], [6, 1], [8, 1], [10, 1], [17, 1], [18, 1], [47, 1], [48, 1], [49, 1], [52, 1], [53, 1], [54, 1], [55, 1], [56, 1], [57, 1], [58, 1], [59, 1], [60, 1], [61, 1]], 'rhs': -1}, {'D': ['0', '1', '2', '3', '4', '5', '012', '013', '023', '045', '14', '15', '24', '25', '34', '35'], 'weights': [[2, 1], [4, 1], [6, 1], [31, 1], [33, 1], [40, 1], [41, 1], [42, 1], [43, 1], [44, 1], [45, 1], [47, 1]], 'rhs': -3}]

def main():
    target={tuple(obj['D']):obj for obj in CERTIFICATES}
    profiles=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),
              (3,0),(2,1),(4,0)]
    low={(0,0),(1,0),(0,1)}
    pair_lookup=dict(pair_tables())
    total=Counter(); used=set()
    for profile in profiles:
        cases=(low_support_cases(*profile) if profile in low else
               high_support_cases(*profile,pair_lookup[2+profile[0]+2*profile[1]]))
        for _,D in cases:
            total['all']+=1
            assert len(D)==16 and sum(map(len,D))==30
            assert all(sum(i in s for s in D)==5 for i in range(6))
            st,ob=constraints(D,5)
            if ob:
                total['direct_hall']+=1
                continue
            fixed=propagate(st)
            if fixed is None:
                total['propagation']+=1
                continue
            k=tuple(''.join(str(i) for i in sorted(s)) for s in D)
            assert k in target, ('UNEXPECTED_RESIDUAL',profile,k)
            assert k not in used
            used.add(k)
            check_exact_dual(st,*fixed,target[k])
            total['dual']+=1
        print('profile',profile, 'cumulative',dict(total),flush=True)
    assert total==Counter({'all':2806,'direct_hall':1643,
                           'propagation':1152,'dual':11}),total
    assert len(used)==len(target)==11
    print('CERTIFIED: 2806 support systems excluded; 1643 immediate Hall, '
          '1152 propagation, 11 exact integer duals.')

if __name__=='__main__':main()
