"""Ablate saturated cliques by excess trace type. If a type has excess multiplicity, mark ALL cliques with that type (no arbitrary tie selection). Compare local and orbit-wide results."""
import json,itertools
from collections import Counter
from pysat.solvers import Solver
from pysat.card import CardEnc
from ramsey_retention_slice import D,decode
P=D.parent;row=next(r for r in json.loads((P/'ramsey_wedge_join_reversal.json').read_text()) if r['reversals']);g=decode(next(z['graph6'] for z in json.loads(D.read_text()) if (z['l'],z['k'])==(3,9)));F={v for z in json.loads((P/'ramsey_square_edge_families.json').read_text()) for v in z[3]};r={int(i):j for i,j in row['rotation'].items()};s,t=row['singles'];Q=set(r);q=sum(1<<i for i in Q);a=min(Q-{s,t});A=[a,r[a],r[r[a]]];B=Q-{s,t}-set(A);counts=Counter(q&z for z in F-{q});local={k:set() for k in (3,5)}
for b in B:
 f={s:t,t:s,**dict(zip(A,[b,r[r[b]],r[b]]))};f.update({j:i for i,j in list(f.items())})
 for z in F-{q}:
  m=z&q;k=m.bit_count();im=sum(1<<f[i] for i in Q if m>>i&1)
  if counts[m]>counts[im]:local[k].add(z)
import igraph as ig
G=ig.Graph(35,[(i,j) for i,j in itertools.combinations(range(35),2) if g[i]>>j&1]);gens=G.automorphism_group()
def close(S):
 S=S.copy();stack=list(S)
 while stack:
  z=stack.pop()
  for p in gens:
   y=sum(1<<p[i] for i in range(35) if z>>i&1)
   if y not in S:S.add(y);stack.append(y)
 assert S<=F;return S
enc={k:CardEnc.atmost(list(range(1,36)),k).clauses for k in range(1,10)}
def hit(S):
 if not S:return []
 cs=[[i+1 for i in range(35) if z>>i&1] for z in S];lo,hi=0,9;w=None
 while hi-lo>1:
  k=(hi+lo)//2
  with Solver(name='g4',bootstrap_with=cs+enc[k]) as sl:
   if sl.solve():w=[i-1 for i in sl.get_model() if 1<=i<=35];hi=len(w)
   else:lo=k
 if w is None:w=json.loads((P/'ramsey_saturated_square_cuts.json').read_text())[-1]['cuts'][0]
 assert len(w)==hi and all(any(z>>i&1 for i in w) for z in S);return w
out=[]
for scope,sets in [('local',local),('all equivalent wedges',{k:close(v) for k,v in local.items()})]:
 for k,S in [(3,sets[3]),(5,sets[5]),('both',sets[3]|sets[5])]:
  u,v=hit(S),hit(F-S);print(scope,k,len(S),len(u),len(v),flush=True);out.append(dict(scope=scope,size=k,marked=len(S),cut=u,complement_cut=v))
(P/'ramsey_reversal_cut.json').write_text(json.dumps(out,indent=1)+'\n')
