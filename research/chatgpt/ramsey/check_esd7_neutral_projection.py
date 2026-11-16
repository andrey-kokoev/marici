"""Exact finite incidence audit of esd_7(Delta^3) with roles R,B,N1,N2.
The geometry is reproduced from Marici's public census builder, with no independent Ramsey claims.
"""
from itertools import combinations, permutations, product
from collections import Counter, defaultdict
from math import comb

R=7
valid=lambda z: 0 <= z[0] <= z[1] <= z[2] <= R
bary=lambda z: (z[0],z[1]-z[0],z[2]-z[1],R-z[2])
q=lambda z:(z[0],z[1]-z[0],R-z[1]) # R,B,N
visible=lambda z:z[:2] # cumulative projection, injective on (R,B,N)
mirror=lambda z:(z[0],z[1],z[1]+R-z[2])

T=set()
for base in product(range(R+1),repeat=3):
  for order in permutations(range(3)):
    w=list(base);vertices=[tuple(w)]
    for axis in order:
      w[axis]+=1;vertices.append(tuple(w))
    if all(valid(z) for z in vertices): T.add(tuple(sorted(vertices)))
V={v for t in T for v in t};E={e for t in T for e in combinations(t,2)};F={f for t in T for f in combinations(t,3)}
assert (len(V),len(E),len(F),len(T))==(120,560,784,343)
Vq={visible(v) for v in V}
Eq={tuple(sorted({visible(v) for v in e})) for e in E}
Fq={tuple(sorted({visible(v) for v in f})) for f in F}
Tq={tuple(sorted({visible(v) for v in t})) for t in T}
# independently build esd_7(Delta^2) (ordered chamber x<=y) triangles
Tr=set()
for x in range(R+1):
 for y in range(R+1):
  for order in permutations(range(2)):
   w=[x,y];verts=[tuple(w)]
   for axis in order:
    w[axis]+=1;verts.append(tuple(w))
   if all(0<=a<=b<=R for a,b in verts):Tr.add(tuple(sorted(verts)))
fr={e for f in Tr for e in combinations(f,2)}
assert len(Vq)==36 and len(Tr)==49 and set(x for e in Tr for x in e)==Vq
assert all(len(t)==3 and t in Tr for t in Tq), 'projection of tet may degenerate further than a triangle?'
assert {tuple(sorted({visible(v) for v in e})) for e in E if visible(e[0]) != visible(e[1])}==fr
assert Tq==Tr

fibers=Counter(visible(z) for z in V)
assert sum(fibers.values())==120 and len(fibers)==36
assert all(fibers[(x,y)]==R-y+1 for x,y in Vq)
vertical=[e for e in E if visible(e[0])==visible(e[1])]
assert len(vertical)==84
byfiber=Counter(visible(e[0]) for e in vertical)
assert all(byfiber.get(q,0)==size-1 for q,size in fibers.items())
assert all(mirror(v) in V for v in V)
mirror_tets=sum(tuple(sorted(mirror(v) for v in t)) in T for t in T)
mirror_edges=sum(tuple(sorted(mirror(v) for v in e)) in E for e in E)

# central tetra: full-coordinate role order R B N1 N2
cent=tuple(sorted([z for z in V if sorted(bary(z))==[1,2,2,2]]))
assert len(cent)==4 and cent in T
role_to_central={bary(v):v for v in cent}
R0=role_to_central[(1,2,2,2)];B0=role_to_central[(2,1,2,2)]
N10=role_to_central[(2,2,1,2)];N20=role_to_central[(2,2,2,1)]
assert cent==(R0,B0,N10,N20)
assert visible(N10)==visible(N20)
assert visible(R0)!=visible(B0)!=visible(N10)

def alternating_boundary(chain):
  result=defaultdict(int)
  for tup,coef in chain.items():
    for i in range(len(tup)):
      face=tup[:i]+tup[i+1:]
      if len(set(face))==len(face):result[face]+=coef*((-1)**i)
  return {a:b for a,b in result.items() if b}

# oriented chain pushforward: every degenerate simplex -> 0
push=lambda simplex: tuple(visible(v) for v in simplex) if len(set(visible(v) for v in simplex))==len(simplex) else None
boundary=dict((face,(-1)**i) for i,face in enumerate(cent[:i]+cent[i+1:] for i in range(4)))
pushboundary=defaultdict(int)
for f,c in boundary.items():
  qf=push(f)
  if qf:pushboundary[qf]+=c
assert all(c==0 for c in pushboundary.values())
assert push(cent) is None
# section as N1=0 => z=y maps visible back into full tetra, is simplicial
section=lambda p:(p[0],p[1],p[1])
assert all(tuple(sorted(section(p) for p in t)) in F for t in Tr)

print('ESD7 full f-vector:',[len(V),len(E),len(F),len(T)])
print('Observable triangle quotient: 36 vertices,',len(fr),'edges,',len(Tr),'triangles')
print('Fibers:',sorted(Counter(fibers.values()).items()),'neutral-only edges:',len(vertical))
print('Projection: all 343 tetrahedra project to 49 triangles; section exists')
print('Neutral swap image: ',mirror_tets,'of 343 tetrahedra,',mirror_edges,'of 560 edges are simplices')
print('Central role coordinates:',[(name,bary(v),q(v)) for name,v in [('R',R0),('B',B0),('N1',N10),('N2',N20)]])
print('Central tetra chain projects to zero; signed boundary projects to zero')
print('PASS')

# The 56 presentation-dependent diagonals are exactly simultaneous transfers
# B -> R and N2 -> N1, encoded by cumulative mask 101.
mask=lambda edge:''.join(str(i+1) for i in range(3) if edge[1][i]>edge[0][i])
diagonals=[e for e in E if mask(e)=='13']
assert len(diagonals)==56
assert {e for e in E if tuple(sorted(mirror(z) for z in e)) not in E}==set(diagonals)
assert sum(1 for t in T if any(e in diagonals for e in combinations(t,2)))==224
assert all(sum(e in diagonals for e in combinations(t,2))==1 for t in T if any(e in diagonals for e in combinations(t,2)))
assert all(tuple(sorted(mirror(z) for z in t)) in T for t in T if not any(e in diagonals for e in combinations(t,2)))
assert all(tuple(sorted(mirror(z) for z in t)) not in T for t in T if any(e in diagonals for e in combinations(t,2)))

def add(a,d):return tuple(x+y for x,y in zip(a,d))
root_delta=((1,-1,0,0),(0,0,1,-1),(0,-1,1,0),(1,0,0,-1))
root_faces=set()
for e in diagonals:
    a0,a1=e;source=bary(a0);target=bary(a1)
    assert tuple(x-y for x,y in zip(target,source))==(1,-1,1,-1)
    assert source[1]>0 and source[3]>0
    for d in root_delta:
        m=add(source,d)
        m_cum=(m[0],m[0]+m[1],m[0]+m[1]+m[2])
        assert m_cum in V
        assert tuple(sorted((a0,m_cum))) in E and tuple(sorted((m_cum,a1))) in E
        tri=tuple(sorted((a0,m_cum,a1)))
        assert tri in F
        root_faces.add(tri)
assert len(root_faces)==224
print('Presentation diagonals: 56, each with 4 root routes =',len(root_faces),'actual face comparisons')
print('Neutral reversal preserves all 504 root edges but none of 56 diagonals;')
print('it preserves 119 unsplit tetrahedra, changes all 224 tetrahedra refining octahedra')
print('Exact source role of every diagonal: simultaneous (B -> R) and (N2 -> N1) transfers')
print('Central tetrahedron preserved by neutral swap:',tuple(sorted(mirror(v) for v in cent))==cent)
print('PASS: mismatch is subdivision/presentation dependence, not nonexistence of refinement')
