"""Exact combinatorial obstruction for a hypothetical (3,7;23) graph.

Assumptions: G triangle-free, alpha(G)<=6, 6-regular.
Fix vertex v, S=N(v), X=V\\(S U {v}).  F_x=N(x) intersect S.
The program proves no configuration with |F_x|<=2 for all x in X.
This is a small incidence enumeration, NOT an enumeration of 23-node graphs.
"""
from itertools import combinations, permutations

S = tuple(range(6))
pairs = tuple(combinations(S,2))
edge_index = {p:i for i,p in enumerate(pairs)}
permutation_of_pairs = [tuple(edge_index[tuple(sorted((p[i],p[j])))] for i,j in pairs)
                        for p in permutations(S)]

# If |F_x| <=2, there must be exactly two singleton columns
# and fourteen 2-element columns. For s,t in S, the pair column
# multiplicity m_st <=2, because c(s,t)=1+m_st<=3.
# The B-group constraint applied to Q_s=N(s) intersect X shows
# that each s has at most one t with m_st=0.
# Thus the missing-pair graph is a matching, a stronger restriction
# than just at most three missing pairs.
# We intentionally enumerate a superset (all <=3 missing pairs).
classes = {}
for r in (1,2,3):
    for missing in combinations(range(15),r):
        for doubled in combinations([i for i in range(15) if i not in missing],r-1):
            w=[1]*15
            for i in missing:w[i]=0
            for i in doubled:w[i]=2
            # Each of six S nodes has exactly five neighbours in X.
            singletons=[5]*6
            for (i,j),wt in zip(pairs,w):
                singletons[i]-=wt
                singletons[j]-=wt
            if min(singletons)<0 or max(singletons)>2 or sum(singletons)!=2:
                continue
            # Additional necessary condition: missing-pair graph matching.
            if any(sum(w[k]==0 for k,(a,b) in enumerate(pairs) if s in (a,b))>1 for s in S):
                continue
            canonical=min(tuple(w[j] for j in pp) for pp in permutation_of_pairs)
            classes[canonical]=True

print('Incidence types after missing-pair matching test:',len(classes))
exclusions=0
for idx,w in enumerate(sorted(classes)):
    F=[frozenset(p) for p,weight in zip(pairs,w) for _ in range(weight)]
    deficit=[5]*6
    for f in F:
        for s in f:deficit[s]-=1
    F.extend(frozenset((s,)) for s in S for _ in range(deficit[s]))
    assert len(F)==16 and sum(map(len,F))==30
    assert all(sum(s in f for f in F)==5 for s in S)
    # A subset I of X with pairwise overlapping F_i cannot contain any A-edge.
    # If |I| > |union F_i|, I together with unused S labels is a forbidden B7.
    witness=None
    for k in (2,3,4):
        for I in combinations(range(16),k):
            U=set().union(*(F[i] for i in I))
            if len(U)<len(I) and all(F[i]&F[j] for i,j in combinations(I,2)):
                witness=I
                break
        if witness is not None:break
    if witness is not None:
        assert len(witness) + 6 - len(set().union(*(F[i] for i in witness))) >=7
        print(f'type {idx}: excluded by B7, supports:',[sorted(F[i]) for i in witness])
        exclusions+=1
        continue
    # Unique residual type: exactly K6 minus one missing pair, plus a
    # singleton at each endpoint of that missing pair.  For its singleton
    # x at endpoint s, the four-node set {x,sa,sb,ab} for each a,b among
    # the other four labels must contain an A-edge. The ONLY possible
    # A-edge is x-ab, forcing six such edges, while d_X(x)=5.
    missing=[p for p,weight in zip(pairs,w) if weight==0]
    doubled=[p for p,weight in zip(pairs,w) if weight==2]
    assert len(missing)==1 and len(doubled)==0 and len(deficit)==6
    s,t=missing[0]
    assert deficit[s]==deficit[t]==1 and sum(deficit)==2
    remaining=[x for x in S if x not in (s,t)]
    forced=[]
    for a,b in combinations(remaining,2):
        support=frozenset((s,a,b))
        witnesses=[frozenset((s,)),frozenset((s,a)),frozenset((s,b)),frozenset((a,b))]
        assert all(witnesses.count(f)==1 for f in witnesses)
        assert all(f in F for f in witnesses)
        possible_A=[(i,j) for i,j in combinations(range(4),2) if not witnesses[i]&witnesses[j]]
        assert possible_A==[(0,3)]
        forced.append((a,b))
    assert len(forced)==6 and len(set(forced))==6
    assert 6 > 5  # d_X of singleton x = 6-|F_x| = 5
    print(f'type {idx}: excluded by six forced neighbours of singleton {s} (capacity five)')
    exclusions+=1
assert exclusions==len(classes)
print('PASS: no 23-node example can have all composition multiplicities <=2.')
print('CONSEQUENCE: every vertex requires at least one B-neighbour with 3 A-path completions.')
