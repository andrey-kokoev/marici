"""Certified difference-constraint closure on an owning atom-cap box.
Observer: selected raw atoms, not the moment pair. Anchor node 0 has value 0;
node j+1 represents atom j. Edge (u,v,w) means x_v-x_u<=w.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def edges(m):
 e=[]
 for j in range(m):e.extend([(0,j+1,Q(100+2*j)),(j+1,0,Q(0))])
 for j in range(1,m):e.extend([(j,j+1,Q(1)),(j+1,j,Q(-1,2))])
 return e
def close(m,e,order):
 n=m+1;D=[[None]*n for _ in range(n)];paths=[[None]*n for _ in range(n)]
 for i in range(n):D[i][i]=Q(0);paths[i][i]=[]
 for k,(u,v,w) in enumerate(e):
  if D[u][v] is None or w<D[u][v]:D[u][v]=w;paths[u][v]=[k]
 for k in order:
  for i in range(n):
   for j in range(n):
    if D[i][k] is not None and D[k][j] is not None:
     t=D[i][k]+D[k][j]
     if D[i][j] is None or t<D[i][j]:D[i][j]=t;paths[i][j]=paths[i][k]+paths[k][j]
 return D,paths

def main():
 packets=[]
 for m in (4,8,16,32):
  e=edges(m);D,paths=close(m,e,range(m+1));anchors=[0,1,m]
  # Blocks are eliminated in opposite orders, followed by interface closure.
  hidden=list(range(2,m));order=hidden[::-1]+anchors
  alt,_=close(m,e,order);assert alt==D
  summary=[[a,b,str(D[a][b])] for a in anchors for b in anchors if a!=b]
  samples=[]
  for base in (Q(0),Q(1),Q(50)):
   y={0:Q(0),1:base,m:base+Q(3*(m-1),4)}
   assert all(y[b]-y[a]<=D[a][b] for a in anchors for b in anchors)
   x=[min(y[a]+D[a][v] for a in anchors) for v in range(m+1)]
   assert all(x[a]==y[a] for a in anchors)
   assert all(x[v]-x[u]<=w for u,v,w in e)
   samples.append({'public':[str(y[a]) for a in anchors],'lift':list(map(str,x))})
  p={'m':m,'edges':[[u,v,str(w)] for u,v,w in e],'anchors':anchors,
   'distance':[[str(w) for w in row] for row in D],'paths':paths,'summary':summary,'samples':samples}
  enc=lambda x:len(json.dumps(x,separators=(',',':')).encode())
  p['cost']={'input_rows':len(e),'summary_rows':len(summary),'input_rows_bytes':enc(p['edges']),
    'summary_rows_bytes':enc(summary),'closure_proof_bytes':enc({'distance':p['distance'],'paths':paths}),
    'comparison':'Row payload only; source/schema metadata and archive are not included.'}
  packets.append(p)
 (OUT/'chain-audit-elimination.json').write_text(json.dumps({'packets':packets},indent=2)+'\n')
 print(json.dumps([{'m':p['m'],**p['cost']} for p in packets],indent=2))
if __name__=='__main__':main()
