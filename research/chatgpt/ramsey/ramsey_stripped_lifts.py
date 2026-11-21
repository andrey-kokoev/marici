"""Lift the degree-reduced cores, and separate the role of triangles and sevens."""
from itertools import product,combinations
from collections import Counter
from ramsey_stripped_core import T,V,E,bits,models,seed,base
from ramsey_point_witness_ablation import minimal
S=list(models(seed,0));stats=Counter();hist=Counter();legal=[]
for s in S:
    counts=[0,0,0]
    for z in product(range(2),repeat=3):
        m=s|bits[10,14]|bits[11,14]
        for i in range(6):m|=bits[i,10+(z[i//2]^(i%2))]
        if any((m&ms).bit_count()>h for ms,_,h in base):continue
        counts[0]+=1;legal.append(m)
        if any((m&ms).bit_count()<l for ms,l,_ in base):continue
        counts[1]+=1
        if all(any(m&bits.get(e,0) for e in combinations(U,2)) for U in combinations(range(15),6)):counts[2]+=1
    hist[tuple(counts)]+=1
print('core histogram (triangle-free, point-valid, fully valid lifts):',hist)
# Minimum extra point clauses to reduce triangle-free lifts to the point survivors.
cs=list({ms for ms,l,h in base if l==1 and any(not m&ms for m in legal)});target={m for m in legal if all(m&c for c in cs)}
# Candidates with identical rejection patterns are equivalent on this reduced domain.
patterns={frozenset(m for m in legal if not m&c):c for c in cs};goal=set(legal)-target
for k in range(len(patterns)+1):
    hit=next((sub for sub in combinations(patterns,k) if set().union(*sub)==goal),None)
    if hit is not None:break
print('minimum extra point clauses',k,[[(T[i],T[j]) for (i,j),b in bits.items() if patterns[r]&b] for r in hit])
