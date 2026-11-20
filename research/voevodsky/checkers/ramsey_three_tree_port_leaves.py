"""Depth-two incidence trees in three fixed rooted witnesses. The observations are core vertices; questions are signs to two distinct + neighbors of root zero. C2^2 translates sign words, not necessarily vertices."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results';words=['++','+-','-+','--'];out={}
for n,file in [(22,'ramsey_37_root_glue'),(27,'ramsey_38_root_glue'),(35,'ramsey_39_glue_vs_circle')]:
    obj=json.loads((D/(file+'.json')).read_text());E=set(map(tuple,obj.get('witness',obj)['plus_edges']));P=lambda i,j:tuple(sorted((i,j))) in E;ports=[v for v in range(1,n) if P(0,v)];core=[v for v in range(1,n) if not P(0,v)];rows=[]
    for a,b in combinations(ports,2):
        leaves={w:[] for w in words}
        for v in core:leaves[('+' if P(v,a) else '-')+('+' if P(v,b) else '-')].append(v)
        rows.append(dict(ports=[a,b],counts=[len(leaves[w]) for w in words],leaves=leaves))
    out[n]=dict(words=words,core=core,rows=rows);print(n,rows[0],Counter(tuple(r['counts']) for r in rows),sum(min(r['counts'])>0 for r in rows))
(D/'ramsey_three_tree_port_leaves.json').write_text(json.dumps(out,indent=2)+'\n')
