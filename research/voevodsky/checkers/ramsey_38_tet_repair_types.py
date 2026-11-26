"""Test three equal-profile repair edges. Orient each from J to C. Keep the three opposite edge readings together, quotient only by swapping the two auxiliary vertices. Compare with actual marked graph-edge orbits."""
import itertools,json,collections,igraph as ig
from ramsey_retention_slice import D,decode
P=D.parent;z=json.loads((P/'ramsey_38_reverse_seed.json').read_text());g=decode(next(s['graph6'] for s in json.loads(D.read_text()) if (s['l'],s['k'])==(3,8)));g.append(z['best'][1]['red_core']|1<<22|1<<26)
for i in range(27):
 if g[-1]>>i&1:g[i]|=1<<27
for i,j in [(5,22),(21,26)]:g[i]^=1<<j;g[j]^=1<<i
V=range(28);role=lambda i:'root' if i==z['root'] else 'new' if i==27 else 'J' if z['neighbor_mask']>>i&1 else 'C';color=lambda i,j:'R' if g[i]>>j&1 else 'B';G=ig.Graph(28,[(i,j) for i,j in itertools.combinations(V,2) if color(i,j)=='R']);marks=[['root','new','J','C'].index(role(i)) for i in V];autos=G.automorphism_group(color=marks);order=G.count_automorphisms(color=marks);pairs=[(4,24),(13,7),(14,7)];rows=[]
for u,v in pairs:
 assert (role(u),role(v))==('J','C');one=collections.Counter();plain=collections.Counter();marked=collections.Counter();anch=collections.Counter()
 def sig(w,b):return (color(u,v)+color(w,b),color(u,w)+color(v,b),color(u,b)+color(v,w))
 for w in set(V)-{u,v}:one[role(w)+':'+color(u,w)+color(v,w)]+=1
 for w,b in itertools.combinations(set(V)-{u,v},2):
  s=min(sig(w,b),sig(b,w));plain['|'.join(s)]+=1;marked[min('|'.join((role(h),role(j))+sig(h,j)) for h,j in [(w,b),(b,w)])]+=1
  if {role(w),role(b)}=={'root','new'}:anch['|'.join(sig(z['root'],27))]+=1
 seen={(u,v)};stack=list(seen)
 while stack:
  i,j=stack.pop()
  for p in autos:
   t=p[i],p[j]
   if t not in seen:seen.add(t);stack.append(t)
 rows.append(dict(edge=(u,v),one=one,plain=plain,marked=marked,anchor=anch,orbit=sorted(seen)))
print('group',order,'orbits',[r['orbit'] for r in rows]);
for field in ['one','plain','marked','anchor']:
 d=[r[field] for r in rows];print(field,'equal',[(i,j) for i,j in itertools.combinations(range(3),2) if d[i]==d[j]],'example',next(((k,[v[k] for v in d]) for k in sorted(set.union(*(set(v) for v in d))) if len({v[k] for v in d})==3),None));
(P/'ramsey_38_tet_repair_types.json').write_text(json.dumps(dict(group_order=order,rows=rows),indent=1)+'\n')
