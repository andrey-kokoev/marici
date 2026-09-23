"""Check exact path witnesses, closure and source-relative extensions independently."""
from pathlib import Path
from fractions import Fraction as Q
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 packets=json.loads((OUT/'chain-audit-elimination.json').read_text())['packets'];assert len(packets)==4
 path_checks=0;lift_checks=0
 for m,p in zip((4,8,16,32),packets):
  assert p['m']==m;E=[]
  for j in range(m):E.extend([(0,j+1,Q(100+2*j)),(j+1,0,Q(0))])
  for j in range(1,m):E.extend([(j,j+1,Q(1)),(j+1,j,Q(-1,2))])
  assert p['edges']==[[u,v,str(w)] for u,v,w in E]
  D=[[Q(w) for w in row] for row in p['distance']];assert len(D)==m+1 and all(len(row)==m+1 for row in D)
  for i in range(m+1):
   assert D[i][i]==0
   for j in range(m+1):
    node=i;weight=Q(0)
    for k in p['paths'][i][j]:
     assert type(k) is int and 0<=k<len(E)
     u,v,w=E[k];assert u==node;node=v;weight+=w
    assert node==j and weight==D[i][j];path_checks+=1
    for k in range(m+1):assert D[i][j]<=D[i][k]+D[k][j]
  for u,v,w in E:assert D[u][v]<=w
  # Triangle + domination of original edges gives D <= every path length.
  # Exhibited paths give the reverse inequality, so D is exact closure.
  A=[0,1,m];assert p['anchors']==A
  assert p['summary']==[[a,b,str(D[a][b])] for a in A for b in A if a!=b]
  for sample in p['samples']:
   y=dict(zip(A,map(Q,sample['public'])));x=list(map(Q,sample['lift']))
   assert y[0]==0 and len(x)==m+1
   assert all(y[b]-y[a]<=D[a][b] for a in A for b in A)
   assert x==[min(y[a]+D[a][v] for a in A) for v in range(m+1)]
   assert all(x[a]==y[a] for a in A) and all(x[v]-x[u]<=w for u,v,w in E)
   lift_checks+=1
 result={'passed':True,'cases':4,'exact_distance_path_checks':path_checks,'source_lifts':lift_checks,
 'scope':'Difference constraints with raw-atom observer. Not arbitrary linear moment/audit evidence; full closure proof retains hidden information.'}
 (OUT/'chain-audit-elimination-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
