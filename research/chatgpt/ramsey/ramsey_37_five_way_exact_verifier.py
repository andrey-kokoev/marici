"""Exact support-incidence obstruction for hypothetical R(3,7) on 23 nodes.

CONDITIONAL PREMISE: its triangle-free A-graph is 6-regular (the previously
established degree reduction). Fix vertex v, S=N_A(v) (6 directions),
T is the 16-vertex complement of S and {v}. Each u in T has support D(u)=N_A(u)∩S.

Enumerate every support multiset compatible with:
 * all D(u) nonempty and of size at most 4,
 * six row sums equal 5,
 * singleton support multiplicity at most 1,
 * pair support multiplicity at most 2, and no repeated pair touching
   a singleton-supported direction.

Every admissible coloring must also satisfy:
 * A edges inside T only between vertices with disjoint supports;
 * each vertex u has exactly 6-|D(u)| A neighbors inside T;
 * the A graph inside T is triangle-free;
 * every set C of at most five T vertices with |union D(C)|<|C|
   contains at least one A-edge (otherwise C and the S directions outside
   its support union contain a forbidden B-K7).

All arithmetic and feasibility decisions below use Python integer bitsets,
backtracking, and exact finite enumeration. No graph catalogue, floating-point
LP/MIP, SAT package, or external dependencies.

This verifies that all candidate support multisets violate these conditions,
which proves the 6-regular case is impossible. It does NOT independently prove
the prior reduction from (3,7,23) to 6-regularity.
"""
from itertools import combinations, combinations_with_replacement, permutations, product
from collections import Counter, defaultdict

LABELS = tuple(range(6))
PAIRS = tuple(combinations(LABELS,2))


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


def feasible(D,arity=5):
    system,obstruction=constraints(D,arity)
    if obstruction:return False,0
    edges,cap,degs,tris,halls=system
    full=(1<<len(edges))-1
    nodes=0
    def propagate(ones,zeros):
        while True:
            before=(ones,zeros)
            for m,k in zip(degs,cap):
                yes=(ones&m).bit_count()
                unknown=m & (full&~(ones|zeros))
                if yes>k or yes+unknown.bit_count()<k:return None
                if yes==k:zeros|=unknown
                elif yes+unknown.bit_count()==k:ones|=unknown
            if ones&zeros:return None
            for m in tris:
                yes=(ones&m).bit_count()
                if yes==3:return None
                if yes==2:zeros|=m&(full&~(ones|zeros))
            if ones&zeros:return None
            for m in halls:
                if m&ones:continue
                unknown=m&(full&~(ones|zeros))
                if not unknown:return None
                if unknown.bit_count()==1:ones|=unknown
            if ones&zeros:return None
            if (ones,zeros)==before:return ones,zeros
    def search(ones,zeros):
        nonlocal nodes
        nodes+=1
        found=propagate(ones,zeros)
        if found is None:return False
        ones,zeros=found
        unassigned=full&~(ones|zeros)
        if not unassigned:return True
        open_halls=[m&unassigned for m in halls if not(m&ones)]
        if open_halls:
            candidates=min(open_halls,key=int.bit_count)
            previous=0
            while candidates:
                bit=candidates&-candidates
                if search(ones|bit,zeros|previous):return True
                previous|=bit
                candidates-=bit
            return False
        bit=unassigned&-unassigned
        return search(ones|bit,zeros) or search(ones,zeros|bit)
    return search(0,0),nodes


def main():
    profile_order=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(4,0)]
    low={(0,0),(1,0),(0,1)}
    high_tables=dict(pair_tables())
    total=Counter();limits=Counter()
    for profile in profile_order:
        n3,n4=profile
        candidate_cases=low_support_cases(*profile) if profile in low else high_support_cases(n3,n4,high_tables[2+n3+2*n4])
        cnt=Counter()
        for _,D in candidate_cases:
            assert len(D)==16
            assert sum(len(s) for s in D)==30
            assert all(sum(i in s for s in D)==5 for i in range(6))
            sat5,nodes5=feasible(D,arity=5)
            assert not sat5, ('FIVE_WAY_CONTRADICTION_FAILED',profile,D)
            cnt['tested']+=1
            limits[profile]=max(limits[profile],nodes5)
            sat4,_=feasible(D,arity=4)
            if sat4:cnt['four-way-compatible']+=1
        total.update(cnt)
        print('profile',profile,'tested',cnt['tested'],
              'survive arity four',cnt['four-way-compatible'],
              'survive arity five',0,
              'max exact search nodes at arity five',limits[profile],flush=True)
    assert total['tested']==2806,total
    assert total['four-way-compatible']==19,total
    print('VERIFIED: 2806 normalized degree-feasible incidence systems all contradict five-way Hall+triangle+degree constraints.')
    print('Exactly 19 of them satisfy the four-way version. This is conditional on 6-regularity.')

if __name__=='__main__':main()
