"""Try every legal candidate star on the fixed rooted 22-vertex witness; also restrict to adding a fifth port."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
H=Path(__file__).resolve().parents[1];w=json.loads((H/'results/ramsey_37_root_glue.json').read_text())['witness'];n=22;adj=[0]*n
for i,j in w['plus_edges']:adj[i]|=1<<j;adj[j]|=1<<i
ind=[]
def visit(s,avail):
    ind.append(s)
    while avail:
        b=avail&-avail;avail^=b;visit(s|b,avail&~adj[b.bit_length()-1])
visit(0,(1<<n)-1);assert max(map(int.bit_count,ind))==6
six=[m for m in ind if m.bit_count()==6];ports=sum(1<<v for v in w['ports']);result={}
for name,cand in [('any_vertex',ind),('fifth_port',[s for s in ind if s&1 and not(s&ports)])]:
    hist=Counter(sum(not(s&m) for m in six) for s in cand);best=min(hist);s=next(s for s in cand if sum(not(s&m) for m in six)==best);result[name]=dict(triangle_safe=len(cand),legal=hist[0],min_unhit_sixes=best,example_best_neighbors=[v for v in range(n) if s>>v&1]);assert hist[0]==0
result['minus_sixes']=len(six);print(result);(H/'results/ramsey_37_reglue_one_vertex.json').write_text(json.dumps(result,indent=2)+'\n')
