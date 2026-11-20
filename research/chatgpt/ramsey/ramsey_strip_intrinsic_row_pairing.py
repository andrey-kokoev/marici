"""Recover row pairing without supplying it as an invariant: center of the full mixed-cube symmetry group. Enumerate type-preserving symmetries as an independent completeness control."""
from itertools import product
from ramsey_strip_unmarked_frame_motion import isos,maps,U,V,E,F,cross,r
verts=U+V;I=tuple(verts);encode=lambda a:tuple(a[x] for x in verts);decode=lambda a:dict(zip(verts,a))
def compose(a,b):
 d=decode(a);return tuple(d[x] for x in b)
G={I};todo=[I];gens=list(map(encode,maps))
while todo:
 a=todo.pop()
 for g in gens:
  b=compose(a,g)
  if b not in G:G.add(b);todo.append(b)
center=[a for a in G if all(compose(a,b)==compose(b,a) for b in G)];z,=[a for a in center if a!=I];assert decode(z)=={x:r[x] for x in verts}
# Every internal cube automorphism is the composition of a fixed cube isometry inverse and another.
base=isos[0];inv={v:u for u,v in base.items()};A=[{x:inv[g[x]] for x in U} for g in isos];B=[{base[x]:g[x] for x in U} for g in isos];pres=[]
for a,b in product(A,B):
 if all(cross(x,y)==cross(a[x],b[y]) for x in U for y in V):pres.append(encode(a|b))
assert len(pres)==4 and G==set(pres)|set(gens)
print('complete symmetry group',len(G),'center size',len(center),'intrinsic nonidentity central action equals row swap',True);print('intrinsic paired states',[(x,decode(z)[x]) for x in sorted(verts) if x<decode(z)[x]])
