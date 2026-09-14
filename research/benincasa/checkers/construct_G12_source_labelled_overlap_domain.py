#!/usr/bin/env python3
"""VC2b1: construct the source-labelled Cech overlap domain of four cubic walls."""
import itertools,json
from pathlib import Path
walls=('g1','g2','s23','s31');vertices=list(walls);edges=list(itertools.combinations(range(4),2));triangles=list(itertools.combinations(range(4),3));tetra=(0,1,2,3)
def boundary(simplex):return [((-1)**k,tuple(simplex[:k]+simplex[k+1:])) for k in range(len(simplex))]
# Matrices d_k: oriented k-simplex to its boundary.
def matrix(high,low):
 idx={x:i for i,x in enumerate(low)};M=[[0]*len(high) for _ in low]
 for j,x in enumerate(high):
  for sign,face in boundary(x):M[idx[face]][j]=sign
 return M
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
verts=[(i,) for i in range(4)];d1=matrix(edges,verts);d2=matrix(triangles,edges);d3=matrix([tetra],triangles)
zero12=mm(d1,d2);zero23=mm(d2,d3)
# Exchange 1<->2 and 23<->31 is permutation (0 1)(2 3), even.
perm={0:1,1:0,2:3,3:2}
def transport(simplex):
 image=[perm[i] for i in simplex];sorted_image=sorted(image);inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)));return (-1)**inversions,tuple(sorted_image)
def equivariant(high,low,D):
 hi={x:i for i,x in enumerate(high)};lo={x:i for i,x in enumerate(low)}
 for x in high:
  sx,tx=transport(x)
  for y in low:
   sy,ty=transport(y)
   if D[lo[ty]][hi[tx]]*sx != sy*D[lo[y]][hi[x]]:return False
 return True
checks={'four_source_walls':vertices==['g1','g2','s23','s31'],'six_pair_overlaps':len(edges)==6,'four_triple_overlaps':len(triangles)==4,'one_quadruple_overlap':len([tetra])==1,'boundary_squared_zero':not any(map(any,zero12)) and not any(map(any,zero23)),'exchange_even':transport(tetra)==(1,tetra),'d1_exchange_equivariant':equivariant(edges,verts,d1),'d2_exchange_equivariant':equivariant(triangles,edges,d2),'d3_exchange_equivariant':equivariant([tetra],triangles,d3)}
assert all(checks.values()),checks
label=lambda x:'|'.join(walls[i] for i in x)
out={'schema':'marici.benincasa.G12-source-labelled-overlap-domain.v1','prospective_action':'VC2b1_construct_overlap_domain','wall_order':list(walls),'cech_modules':{'C0_vertices':[label(x) for x in verts],'C1_pair_overlaps':[label(x) for x in edges],'C2_triple_overlaps':[label(x) for x in triangles],'C3_quadruple_overlap':[label(tetra)]},'differentials':{'d1_edges_to_vertices':d1,'d2_triangles_to_edges':d2,'d3_tetrahedron_to_triangles':d3},'exchange':'(g1 g2)(s23 s31), including induced orientation signs','VC2b1_resolution':'++','interface_added':'overlap_domain','result':'The complete labelled Cech/Koszul overlap domain is constructed integrally, satisfies d^2=0, and is exchange-equivariant.','scope':'Constructs the domain and incidence differentials only; no coefficient map to the 379-dimensional stage-1 quotient is asserted.','next':'VC2b0 reconstruct the characteristic-zero H1 presentation, then VC2b2 compare this overlap domain to H1.','checks':checks,'passed':True}
d=Path(__file__).resolve().parents[1]/'results'/'G12_source_labelled_overlap_domain.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'++','ranks':[4,6,4,1],'interface':'overlap_domain'}))
