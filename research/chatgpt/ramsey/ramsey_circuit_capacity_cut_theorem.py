"""Self-contained exact combinatorial cut certificate for the conditional
R(3,7) 23-vertex / 6-regular local incidence obstruction.

After deterministic Hall/degree/triangle propagation, a cut is found from
remaining vertex capacities and a disjoint family of Hall demands.
No LP, SAT, external libraries, stored Farkas weights, or graph catalogue.
The prior 6-regularity reduction is an external assumption, not proved here.
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




def find_cut(system,D):
    """Return an exact demand > capacity witness, or None.
    P: positive-budget vertices, Q: competing degree commitments.
    Selected Hall demands have disjoint candidate-edge sets, each candidate
    touches P and avoids Q. A valid completion would imply
    m <= r(P)-r(Q)+2|E[Q]|+|E(Q,R)|.
    """
    edges,caps,degrees,triangles,halls=system
    fixed=propagate(system)
    if fixed is None: return None
    ones,zeros=fixed
    free=[j for j in range(len(edges)) if not (ones|zeros)>>j&1]
    remaining=[caps[u]-(ones&degrees[u]).bit_count() for u in range(16)]
    demands=[frozenset(j for j in free if h>>j&1) for h in halls if not ones&h]
    singletons=tuple(u for u in range(16) if len(D[u])==1)
    other=tuple(u for u in range(16) if len(D[u])>=2)
    P_options=[set(a) for z in range(1,len(singletons)+1)
               for a in combinations(singletons,z)]
    # Allow one pair-supported vertex in a cut alongside all singleton nodes.
    P_options += [set(singletons)|{u} for u in other if len(D[u])==2]
    P_options.sort(key=lambda p:(len(p),tuple(sorted(p))))
    for P in P_options:
        q_candidates=[u for u in other if u not in P]
        Q_options=[set()] + [{u} for u in q_candidates] + [set(q) for q in combinations(q_candidates,2)]
        for Q in Q_options:
            R=set(range(16))-P-Q
            eQR={j for j in free if (edges[j][0] in Q and edges[j][1] in R)
                                     or (edges[j][1] in Q and edges[j][0] in R)}
            eQQ={j for j in free if edges[j][0] in Q and edges[j][1] in Q}
            capacity=(sum(remaining[u] for u in P)-sum(remaining[u] for u in Q)
                      +len(eQR)+2*len(eQQ))
            if capacity>=len(demands):continue
            eligible=[]
            for h in demands:
                if all((edges[j][0] in P or edges[j][1] in P) and
                       (edges[j][0] not in Q and edges[j][1] not in Q) for j in h):
                    eligible.append(h)
            if len(eligible)<=capacity:continue
            used=set(); selected=[]
            for h in sorted(eligible,key=lambda s:(len(s),tuple(sorted(s)))):
                if not used.intersection(h):
                    selected.append(h);used.update(h)
            if len(selected)<=capacity:continue
            # Independently check the combinatorial proof hypotheses.
            assert P.isdisjoint(Q)
            assert sum(map(len,selected))==len(used)
            assert all(all((edges[j][0] in P or edges[j][1] in P)
                           and edges[j][0] not in Q and edges[j][1] not in Q
                           for j in h) for h in selected)
            assert len(selected)>capacity
            return dict(P=sorted(P),Q=sorted(Q), demands=len(selected),
                        capacity=capacity, Q_outside=len(eQR),Q_internal=len(eQQ),
                        candidate_edge_options=len(used))
    return None


def main():
    profiles=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(4,0)]
    low={(0,0),(1,0),(0,1)}
    pair_lookup=dict(pair_tables())
    counts=Counter()
    witnesses=[]
    for profile in profiles:
        gen=(low_support_cases(*profile) if profile in low else
             high_support_cases(*profile,pair_lookup[2+profile[0]+2*profile[1]]))
        for _,D in gen:
            counts['all']+=1
            assert len(D)==16 and sum(map(len,D))==30
            assert all(sum(i in s for s in D)==5 for i in range(6))
            system,obstruction=constraints(D,5)
            if obstruction:
                counts['direct_hall']+=1
                continue
            fixed=propagate(system)
            if fixed is None:
                counts['propagation']+=1
                continue
            result=find_cut(system,D)
            if result is None:
                raise AssertionError(('missing cut',profile,D))
            counts['cut']+=1
            witnesses.append((tuple(''.join(map(str,sorted(d))) for d in D),result))
        print('profile',profile,'running totals',dict(counts),flush=True)
    assert counts==Counter(all=2806,direct_hall=1643,propagation=1152,cut=11)
    print('CERTIFIED 2806 patterns: 1643 direct Hall + 1152 propagation + 11 circuit-capacity cuts')
    print('11 cut witnesses:')
    for k,(D,w) in enumerate(witnesses):
        print(k, 'P=',w['P'],'Q=',w['Q'],
              'demands=',w['demands'],'capacity=',w['capacity'])



# 17-vertex comparison: no-three-witness hypothetical R(3,6) structure.
S5 = tuple(range(5))
PAIRS5 = tuple(combinations(S5,2))
PERM5 = tuple(permutations(S5))

def patterns17():
    seen = set()
    output = []
    for deficit in range(4):
        for missing in combinations(PAIRS5, deficit+1):
            count = Counter(i for pair in missing for i in pair)
            for eps in product((0,1,2),repeat=5):
                if sum(eps)!=deficit: continue
                if any(count[i]-eps[i] not in (0,1) for i in S5): continue
                D = tuple(frozenset(p) for p in PAIRS5 if p not in missing)
                D += tuple(frozenset((i,)) for i in S5 if count[i]-eps[i]==1)
                assert len(D)==11
                canon = min(tuple(sorted(tuple(sorted(p[i] for i in x)) for x in D)) for p in PERM5)
                if canon not in seen:
                    seen.add(canon)
                    output.append((deficit,D))
    return output

def edge_system(D):
    return [(i,j) for i,j in combinations(range(len(D)),2) if D[i].isdisjoint(D[j])]

def fixed_A17(D):
    # Original vertex 0; S vertices 1..5; T vertices 6..16.
    fixed={(0,i+1) for i in range(5)}
    for u,d in enumerate(D):
        for i in d: fixed.add((i+1,6+u))
    return fixed

def hall_deficit(U,D):
    return len(U)-len(set().union(*(D[u] for u in U)))

def hall_circuits(D):
    """Minimal Hall-deficient subsets, from supports alone.
    No monochromatic clique search is involved.
    """
    result=[]
    for size in range(2,min(len(D),len(set().union(*D))+1)+1):
        for U in combinations(range(len(D)),size):
            if hall_deficit(U,D) <= 0: continue
            if all(hall_deficit(W,D)<=0
                   for r in range(1,size) for W in combinations(U,r)):
                assert hall_deficit(U,D)==1
                result.append(U)
    return result

def edge_mask(U,e):
    selected=set(U)
    return sum(1<<i for i,(u,v) in enumerate(e) if u in selected and v in selected)


def analyze17(D):
 n=len(D); edges=edge_system(D); caps=[5-len(z) for z in D]
 dm=[sum(1<<j for j,e in enumerate(edges) if u in e) for u in range(n)]
 idx={e:j for j,e in enumerate(edges)}
 tris=[sum(1<<idx[e] for e in combinations(s,2)) for s in combinations(range(n),3) if all(e in idx for e in combinations(s,2))]
 hs=[edge_mask(U,edges) for U in hall_circuits(D) if len(U)<=4]
 ones=zeros=0; full=(1<<len(edges))-1
 while True:
  old=(ones,zeros)
  for u in range(n):
   yes=(ones&dm[u]).bit_count();free=dm[u]&~(ones|zeros)&full
   if yes>caps[u]:return 'prop'
   if yes==caps[u]: zeros|=free
  if ones&zeros:return 'prop'
  for mask in tris:
   yes=(ones&mask).bit_count()
   if yes==3:return 'prop'
   if yes==2:zeros |= mask&~(ones|zeros)&full
  if ones&zeros:return 'prop'
  for mask in hs:
   if ones&mask:continue
   avail=mask&~(ones|zeros)&full
   if not avail:return 'prop'
   if avail.bit_count()==1:ones|=avail
  if ones&zeros:return 'prop'
  if old==(ones,zeros):break
 free=[j for j in range(len(edges)) if not (ones|zeros)>>j&1]
 hs=[set(j for j in free if h>>j&1) for h in hs if not ones&h]
 rem=[caps[u]-(ones&dm[u]).bit_count() for u in range(n)]
 for s in range(1,1<<n):
  P={u for u in range(n) if s>>u&1}
  budget=sum(rem[u] for u in P)
  elig=[]
  for h in hs:
   if all(any(v in P for v in edges[j]) for j in h):elig.append(h)
  if len(elig)<=budget:continue
  used=set();count=0
  for h in sorted(elig,key=lambda h:(len(h),tuple(sorted(h)))):
   if not(h&used):count+=1;used|=h
  if count>budget:return ('cut',count,budget,sorted(P))
 return 'open'


def verify17():
    count=Counter()
    for deficit,D in patterns17():
        result=analyze17(D)
        mode=result[0] if isinstance(result,tuple) else result
        count[mode]+=1
    assert count==Counter({'prop':9,'cut':2}),count
    print('17-VERTEX COMPARISON: 11 systems: 9 propagation, 2 capacity cuts, 0 survivors.')

if __name__=='__main__':
    verify17()
    main()
