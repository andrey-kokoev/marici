"""Positive-gain constraints with a certified global difference-coordinate chart."""
from fractions import Fraction as Q
from pathlib import Path
import json
from check_chain_audit_elimination import close
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def chart(n,relations):
 adj=[[] for _ in range(n)]
 for u,v,g in relations:
  assert g>0
  adj[u].append((v,g));adj[v].append((u,1/g))
 scale=[None]*n
 for root in range(n):
  if scale[root] is not None:continue
  scale[root]=Q(1);todo=[root]
  while todo:
   u=todo.pop()
   for v,g in adj[u]:
    candidate=scale[u]*g
    if scale[v] is None:scale[v]=candidate;todo.append(v)
    elif scale[v]!=candidate:return None
 return scale

def main():
 packets=[]
 for m in (4,8,16):
  desired=[Q(1+j%3) for j in range(m)]
  rel=[(j,j+1,desired[j+1]/desired[j]) for j in range(m-1)]
  # Additional chord closes a nontrivial gain cycle.
  rel.append((0,m-1,desired[-1]/desired[0]));s=chart(m,rel);assert s==desired
  # Node 0 is the zero anchor, node j+1 is x_j/s_j.
  normalized=[];source_rows=[]
  for j in range(m):
   normalized.extend([(0,j+1,Q(100+2*j)/s[j]),(j+1,0,Q(0))])
  for u,v,g in rel:
   source_rows.extend([(u,v,g,s[v]),(v,u,1/g,-s[u]/2)])
   normalized.extend([(u+1,v+1,Q(1)),(v+1,u+1,Q(-1,2))])
  # Chord plus chain lower steps would be inconsistent for large m; use
  # its broader compatible bounds instead of the local edge constants.
  u,v,g=rel[-1]
  source_rows[-2]=(u,v,g,s[v]*m);source_rows[-1]=(v,u,1/g,Q(0))
  normalized[-2]=(u+1,v+1,Q(m));normalized[-1]=(v+1,u+1,Q(0))
  D,paths=close(m,normalized,range(m+1));assert all(D[i][i]==0 for i in range(m+1))
  anchors=[0,1,m];samples=[]
  for t in (Q(0),Q(1)):
   y={0:Q(0),1:t,m:t+Q(3*(m-1),4)}
   assert all(y[b]-y[a]<=D[a][b] for a in anchors for b in anchors)
   z=[min(y[a]+D[a][v] for a in anchors) for v in range(m+1)]
   x=[s[j]*z[j+1] for j in range(m)]
   assert all(0<=v<=100+2*j for j,v in enumerate(x))
   assert all(x[v]<=g*x[u]+w for u,v,g,w in source_rows)
   samples.append({'scaled_public':list(map(str,[y[a] for a in anchors])),'source_lift':list(map(str,x))})
  inconsistent=list(rel);u,v,g=inconsistent[-1];inconsistent[-1]=(u,v,2*g)
  assert chart(m,inconsistent) is None
  packets.append({'m':m,'scales':list(map(str,s)),
   'gain_rows':[[u,v,str(g),str(w)] for u,v,g,w in source_rows],
   'normalized_edges':[[u,v,str(w)] for u,v,w in normalized],
   'distance':[[str(v) for v in row] for row in D],'paths':paths,'samples':samples,
   'incompatible_chart_rejected':True})
 (OUT/'balanced-gain-elimination.json').write_text(json.dumps({'packets':packets},indent=2)+'\n')
 print(json.dumps({'passed':True,'cases':len(packets),'gain_cycle_mismatch_controls':len(packets)}))
if __name__=='__main__':main()
