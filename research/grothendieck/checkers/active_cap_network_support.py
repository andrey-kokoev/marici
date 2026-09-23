"""Exact transshipment by residual shortest augmenting paths, no LP import.
Finite for rational demands; no polynomial augmentation-count claim.
"""
from fractions import Fraction as Q

def potentials(n,edges):
 d=[Q(0)]*n;pred=[None]*n;last=None
 for _ in range(n):
  last=None
  for i,(u,v,w) in enumerate(edges):
   if d[v]>d[u]+w:d[v]=d[u]+w;pred[v]=i;last=v
  if last is None:return d,None
 v=last
 for _ in range(n):v=edges[pred[v]][0]
 start=v;cycle=[]
 while True:
  i=pred[v];cycle.append(i);v=edges[i][0]
  if v==start:break
 cycle.reverse();assert sum(edges[i][2] for i in cycle)<0
 assert all(edges[cycle[i]][1]==edges[cycle[(i+1)%len(cycle)]][0] for i in range(len(cycle)))
 return None,cycle

def support(edges,demand):
 demand=tuple(map(Q,demand));n=len(demand);assert sum(demand)==0
 edges=[(u,v,Q(w)) for u,v,w in edges]
 _,cycle=potentials(n,edges)
 if cycle is not None:return {'status':'INCONSISTENT','cycle_edges':cycle}
 S=n;T=n+1;arcs=[(u,v,w,None) for u,v,w in edges]
 for j,q in enumerate(demand):
  if q<0:arcs.append((S,j,Q(0),-q))
  elif q>0:arcs.append((j,T,Q(0),q))
 f=[Q(0)]*len(arcs);required=sum(q for q in demand if q>0);sent=Q(0);iterations=0
 while sent<required:
  residual=[]
  for i,(u,v,w,cap) in enumerate(arcs):
   if cap is None or f[i]<cap:residual.append((u,v,w,i,1,None if cap is None else cap-f[i]))
   if f[i]>0:residual.append((v,u,-w,i,-1,f[i]))
  dist=[None]*(n+2);pred=[None]*(n+2);dist[S]=Q(0)
  for _ in range(n+1):
   changed=False
   for ri,(u,v,w,i,sign,cap) in enumerate(residual):
    if dist[u] is not None and (dist[v] is None or dist[v]>dist[u]+w):dist[v]=dist[u]+w;pred[v]=ri;changed=True
   if not changed:break
  if dist[T] is None:raise RuntimeError('UNROUTABLE_DEMAND')
  path=[];v=T;seen=set()
  while v!=S:
   if v in seen or pred[v] is None:raise RuntimeError('INVALID_SHORTEST_PATH')
   seen.add(v);edge=residual[pred[v]];path.append(edge);v=edge[0]
  amount=min(edge[5] for edge in path if edge[5] is not None);assert amount>0
  for u,v,w,i,sign,cap in path:f[i]+=sign*amount
  sent+=amount;iterations+=1
 flow=f[:len(edges)];balance=[Q(0)]*n
 for amount,(u,v,w) in zip(flow,edges):balance[v]+=amount;balance[u]-=amount
 assert tuple(balance)==demand and all(v>=0 for v in flow)
 residual_edges=list(edges)+[(v,u,-w) for amount,(u,v,w) in zip(flow,edges) if amount>0]
 d,cycle=potentials(n,residual_edges)
 if cycle is not None:raise RuntimeError('UNCERTIFIED_RESIDUAL_OPTIMUM')
 z=tuple(v-d[0] for v in d);cost=sum(amount*w for amount,(u,v,w) in zip(flow,edges))
 assert all(z[v]-z[u]<=w for u,v,w in edges) and sum(q*v for q,v in zip(demand,z))==cost
 return {'status':'OPTIMUM','potential':list(map(str,z)),'flow':list(map(str,flow)),'value':str(cost),'augmentations':iterations}
