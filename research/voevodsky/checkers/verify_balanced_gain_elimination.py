"""Exact chart, path-closure and source-lift checks; no producer import."""
from pathlib import Path
from fractions import Fraction as Q
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 packets=json.loads((OUT/'balanced-gain-elimination.json').read_text())['packets'];assert len(packets)==3
 count=0
 for m,p in zip((4,8,16),packets):
  assert p['m']==m;s=list(map(Q,p['scales']));assert s==[Q(1+j%3) for j in range(m)]
  rows=[]
  for u,v in [(j,j+1) for j in range(m-1)]+[(0,m-1)]:
   rows.extend([(u,v,s[v]/s[u],s[v]),(v,u,s[u]/s[v],-s[u]/2)])
  rows[-2]=(0,m-1,s[-1]/s[0],s[-1]*m);rows[-1]=(m-1,0,s[0]/s[-1],Q(0))
  assert p['gain_rows']==[[u,v,str(g),str(w)] for u,v,g,w in rows]
  E=[]
  for j in range(m):E.extend([(0,j+1,Q(100+2*j)/s[j]),(j+1,0,Q(0))])
  for u,v,g,w in rows:
   assert s[v]==g*s[u];E.append((u+1,v+1,w/s[v]))
  assert p['normalized_edges']==[[u,v,str(w)] for u,v,w in E]
  D=[[Q(v) for v in row] for row in p['distance']]
  for i in range(m+1):
   assert D[i][i]==0
   for j in range(m+1):
    node=i;weight=Q(0)
    for k in p['paths'][i][j]:
     assert type(k) is int and 0<=k<len(E);u,v,w=E[k];assert node==u;node=v;weight+=w
    assert node==j and weight==D[i][j]
    assert all(D[i][j]<=D[i][k]+D[k][j] for k in range(m+1));count+=1
  assert all(D[u][v]<=w for u,v,w in E)
  for sample in p['samples']:
   a=[0,1,m];y=dict(zip(a,map(Q,sample['scaled_public'])));x=list(map(Q,sample['source_lift']))
   assert y[0]==0 and len(x)==m
   assert all(y[b]-y[c]<=D[c][b] for c in a for b in a)
   assert x==[s[j]*min(y[k]+D[k][j+1] for k in a) for j in range(m)]
   assert all(0<=v<=100+2*j for j,v in enumerate(x)) and all(x[v]<=g*x[u]+w for u,v,g,w in rows)
  # Doubling chord gain disagrees with the product along the chain.
  chain=Q(1)
  for j in range(m-1):chain*=s[j+1]/s[j]
  assert chain!=2*s[-1]/s[0]
 result={'passed':True,'cases':3,'distance_path_checks':count,'lifts':6,
 'scope':'Balanced positive gain systems only. Failure of a scaling chart is not source inconsistency.'}
 (OUT/'balanced-gain-elimination-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
