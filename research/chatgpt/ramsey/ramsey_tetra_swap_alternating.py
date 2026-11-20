"""Test alternating a Hall transversal and its column-swapped copy. Left labels are complementary duads (equivalently four-set contexts); right labels are perfect matchings on the six tetrahedral edges. Over two steps left positions follow nu^{-1} mu. Count shared incidences as doubled edges of length two. Positive control: disjoint unrelated transversals."""
from ramsey_tetra_frame_matching_action import D,M,action
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
maps=[]
def gen(v,used):
    if len(v)==15:maps.append(tuple(v));return
    for j,m in enumerate(M):
        if D[len(v)] in m and j not in used:gen(v+[j],used|{j})
gen([],set());U=set(maps);a,b=action((0,2,1,3));assert len(U)==288

def profile(m,n):
    p=[n.index(j) for j in m];todo=set(range(15));lens=[]
    while todo:
        x=next(iter(todo));k=0
        while x in todo:todo.remove(x);x=p[x];k+=1
        lens.append(2*k)
    return tuple(sorted(lens))
hist=Counter();other=Counter();bad=Counter()
for m in maps:
    n=tuple(b[m[a[i]]] for i in range(15));assert n in U and n!=m
    if m<n:
        shape=profile(m,n);hist[shape]+=1
        if 22 in shape:
            start=next(i for i in range(15) if m[i]!=n[i]);cycle=[];x=start
            while x not in cycle:cycle.extend([x,15+m[x]]);x=n.index(m[x])
            assert len(cycle)==22
            def flip(v):return a[v] if v<15 else 15+b[v-15]
            poles=[i for i,v in enumerate(cycle) if flip(v)==v];assert len(poles)==2 and poles[1]-poles[0]==11
            assert all(flip(cycle[(poles[0]+j)%22])==cycle[(poles[0]-j)%22] for j in range(12))
for m,n in combinations(maps,2):other[profile(m,n)]+=1
out=dict(swap_pairs=sum(hist.values()),swap_profiles={','.join(map(str,k)):v for k,v in sorted(hist.items())},arbitrary_pairs=sum(other.values()),arbitrary_hamiltonian=other[(30,)],arbitrary_22_component=sum(v for k,v in other.items() if 22 in k));print(out);Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
