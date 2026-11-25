"""Exact one-vertex extension defect for each (3,7;22) catalogue parent.
Count independent six-sets disjoint from the proposed red neighborhood.
Only inclusion-maximal independent neighborhoods need be tested for the minimum.
"""
from collections import Counter
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6'
hist=Counter(); degree_hist=Counter(); best=None
for index,line in enumerate(p.read_bytes().splitlines(),1):
    assert line[0]-63==22
    adj=[0]*22;k=0
    for j in range(22):
        for i in range(j):
            if (line[1+k//6]-63)>>(5-k%6)&1:adj[i]|=1<<j;adj[j]|=1<<i
            k+=1
    assert all(not any(adj[i]&adj[j] for j in range(i) if adj[i]>>j&1) for i in range(22))
    maximal=[];six=[];full=(1<<22)-1
    def walk(a,possible):
        if not possible:
            if not any(not (a>>i&1 or a&adj[i]) for i in range(22)):maximal.append(a)
            return
        while possible:
            b=possible&-possible;possible-=b;v=a|b
            assert v.bit_count()<=6
            if v.bit_count()==6:six.append(v)
            walk(v,possible&~adj[b.bit_length()-1])
    walk(0,full)
    d,a=min((sum(not s&m for s in six),m) for m in maximal)
    hist[d]+=1;degree_hist[a.bit_count()]+=1
    if best is None or d<best[0]:best=(d,index,[i for i in range(22) if a>>i&1],len(six),len(maximal))
print('parents:',hist.total(),'defect histogram:',sorted(hist.items()),'best (defect, record, neighbors, sixes, maximal sets):',best)
