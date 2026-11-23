"""Given, not infer, stored named windows and requested staged origins. Compare shared occurrences first by dimension, then by stage modulo 3 with independent local c -> sign*c+offset reindexings. Enumerate all based charts, not stage operators or metric identifications."""
from itertools import product
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1];W=json.loads((D/'results/pne_kind_index_projection.json').read_text())['windows'];phase=[[1,2,0],[1,2,0],[2,0,1]] # R=0 X=1 Y=2
sizes=[[12,3,36],[3,12,36],[2,8,4]];occ={s:[(j,k,sizes[j][k]) for j,row in enumerate(W) for k,v in enumerate(row) if v==s] for s in sum(W,[])};out=[]
for sn,se,cn,ce in product([1,-1],[1,-1],range(3),range(3)):
 vals={};pars=[(1,0),(sn,cn),(se,ce)]
 for row,ph,(a,b) in zip(W,phase,pars):
  for s,v in zip(row,ph):vals.setdefault(s,set()).add((a*v+b)%3)
 if all(len(v)==1 for v in vals.values()):out.append(dict(charts=pars,sites={s:next(iter(v)) for s,v in vals.items()}))
assert len(out)==1 and out[0]['charts'][2][0]==-1;r=dict(requested_stage_origins=['X','X','Y'],dimensions_at_shared_sites={s:[v for _,_,v in o] for s,o in occ.items() if len(o)>1},based_fits=out,forward_only_fits=sum(all(a==1 for a,b in u['charts']) for u in out));print(r);(D/'results/pne_stage_site_gluing.json').write_text(json.dumps(r,indent=2)+'\n')
