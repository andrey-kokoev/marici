"""Hide all site names. Conditional local gluing: type-preserving consecutive two-slot interfaces on distinct N legs, no other identifications. Compare slot dimension preference and independent ordered-window trace hypothesis; not a derivation of the extra trace premise."""
from itertools import product
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1];T=['CMC','MCM','MCC'];dim=[[12,3,36],[3,12,36],[2,8,4]];rows=[]
for p,n in product(range(2),repeat=2):
 u=list(range(9))
 def root(x):return x if u[x]==x else root(u[x])
 def glue(a,b):
  for x in a:
   y,=[j for j in b if T[x//3][x%3]==T[j//3][j%3]];u[root(x)]=root(y)
 glue(range(p,p+2),range(3+n,5+n));glue(range(4-n,6-n),range(6,8));W=[[root(3*k+i) for i in range(3)] for k in range(3)];flags=[W[0][p:p+2]==W[1][n:n+2],W[1][1-n:3-n]==W[2][:2]];fits=[]
 for a,b in product((1,2),repeat=2): # each next window starts later and overlaps its predecessor; no inserted jump
  starts=(0,a,a+b);words={};ok=True
  for st,row in zip(starts,W):
   for k,s in enumerate(row,st):
    if words.setdefault(k,s)!=s:ok=False
  if ok:fits.append(starts)
 common=set(W[0])&set(W[1]);eq=sum(dim[0][W[0].index(i)]==dim[1][W[1].index(i)] for i in common);rows.append(dict(P_leg=p+1,N_leg_for_P=n+1,outer_same=flags,PN_equal_dimensions=eq,contiguous_ordered_trace=fits))
o=dict(rows=rows);print(rows);assert len({tuple(r['outer_same']) for r in rows})==4 and sum(bool(r['contiguous_ordered_trace']) for r in rows)==1;(D/'results/pne_unlabelled_stage_gluing.json').write_text(json.dumps(o,indent=2)+'\n')
