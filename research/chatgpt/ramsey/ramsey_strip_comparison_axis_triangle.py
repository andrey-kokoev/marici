"""Compare original and transported row involutions on a fixed matching. Determine their generated group and the third conjugate involution."""
from ramsey_strip_short_long_root_transport import long,r,rprime,moved
I=tuple(range(30));a=tuple(r);b=tuple(rprime);comp=lambda x,y:tuple(x[v] for v in y);c=comp(a,comp(b,a));q=comp(a,b)
assert comp(q,comp(q,q))==I and q!=I;assert c==comp(b,comp(a,b)) and comp(c,c)==I
G={I};todo=[I]
while todo:
 x=todo.pop()
 for g in (a,b):
  z=comp(g,x)
  if z not in G:G.add(z);todo.append(z)
assert len(G)==6
for name,g in [('original',a),('transported',b),('third',c)]:
 d=long^moved(long,g);adj={}
 for x,y in d:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
 todo=set(adj);sizes=[]
 while todo:
  stack=[min(todo)];seen=set()
  while stack:
   x=stack.pop()
   if x in seen:continue
   seen.add(x);stack.extend(adj[x]-seen)
  todo-=seen;sizes.append(len(seen))
 print(name,'shared matching links',len(long&moved(long,g)),'alternating components',sorted(sizes))
print('comparison involutions generate S3; product has order three')
