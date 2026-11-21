"""Explain one-move safety by exact endpoint-link independence numbers."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
from ramsey_mutual_repair_conjecture import decode,apply
from ramsey_defect_link_constructor import independent_sets
D=Path(__file__).parent
for row in json.loads((D/'ramsey_hall_center_conjecture.json').read_text())['regular']:
    A=decode(row['graph6'].encode())
    for r in {187:[1,2],188:[10,17]}.get(row['record'],[]):
        V=[v for v in range(22) if v!=r and not A[r]>>v&1];E=[e for e in combinations(V,2) if A[e[0]]>>e[1]&1];hist=Counter()
        for (a,b),(c,d) in combinations(E,2):
            S={a,b,c,d}
            if len(S)!=4:continue
            for added in (((a,c),(b,d)),((a,d),(b,c))):
                if any(A[u]>>v&1 for u,v in added):continue
                B=apply(A,((a,b),(c,d)),added)
                if any(B[u]&B[v] for u,v in added):continue
                vals=[];links=[]
                for u,v in [(a,b),(c,d)]:
                    L=((1<<22)-1)&~(A[u]|A[v]|sum(1<<x for x in S));alpha=next(k for k in range(L.bit_count(),-1,-1) if next(independent_sets(A,L,k),None) is not None);vals.append(alpha);links.append([i for i in range(22) if L>>i&1])
                hist[tuple(sorted(vals))]+=1
                if max(vals)<5:print(row['record'],r,'safe links',links)
        print(row['record'],r,hist)
