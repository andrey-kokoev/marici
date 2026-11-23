"""Exact graph isomorphism by simultaneous color refinement and branching. Count isomorphisms respecting or forgetting the deleted root. Rooted isos restrict to precisely the attachment-preserving residual isos (all neighborhoods distinct)."""
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';load=lambda k:json.loads((D/(k+'.json')).read_text());covers={x['index']:x['contacts'] for x in load('pne_four_cover_realizations')};out=[]
def iso(A,B,root):
 n=len(A);init=[int(i==root) for i in range(n)]
 def go(x,y):
  while True:
   s=[(c[i],tuple(sorted(c[j] for j in G[i]))) for G,c in [(A,x),(B,y)] for i in range(n)];d={v:k for k,v in enumerate(sorted(set(s)))};a,b=([d[t] for t in s[h:h+n]] for h in [0,n]);
   if sorted(a)!=sorted(b):return 0
   done=len(set(a))==len(set(x));x,y=a,b
   if done:break
  if len(set(x))==n:return 1
  k=min((c for c in set(x) if x.count(c)>1),key=lambda c:(x.count(c),c));i=x.index(k);new=max(x)+1;xx=x.copy();xx[i]=new;total=0
  for j in range(n):
   if y[j]==k:
    yy=y.copy();yy[j]=new;total+=go(xx,yy)
  return total
 return go(init,init)
for v in load('pne_lower_six_port_dictionary'):
 cs=covers[v['index']];k=1 if v['root']==20 else 0;off=5*k;graphs=[]
 for sets in [v['actual']]+v['alternativeAttachments']:
  H=sorted(set.union(*map(set,sets)));N=[set() for _ in range(22)]
  def edge(a,b):N[a].add(b);N[b].add(a)
  for i,p in enumerate(cs):
   for s in p[k]:edge(H.index(10+i),H.index(off+int(s)))
   for j in range(i):
    if all(set(a).isdisjoint(b) for a,b in zip(p,cs[j])):edge(H.index(10+i),H.index(10+j))
  for j,t in enumerate(sets):
   edge(21,15+j)
   for h in t:edge(15+j,H.index(h))
  graphs.append(N)
 # Same family four times up to relabeling, but compute each case independently.
 matrices={}
 for key,root in [('rooted',21),('unrooted',None)]:
  M=[[0]*4 for _ in graphs];
  for i in range(4):
   for j in range(i+1):M[i][j]=M[j][i]=iso(graphs[i],graphs[j],root)
  matrices[key]=M
 out.append(dict(index=v['index'],pole=v['root'],**matrices))
print(out[0]);(D/'pne_port_completion_iso.json').write_text(json.dumps(out,indent=2)+'\n')
