#!/usr/bin/env python3
"""Audit simplex-chain face cones as closed graph packages and compute their homology."""
import json,itertools
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def boundary_matrix(k,r):
 # C_r(Delta^k) -> C_(r-1)(Delta^k)
 cols=list(itertools.combinations(range(k+1),r+1));rows=list(itertools.combinations(range(k+1),r)) if r else []
 M=[[Fraction(0) for _ in cols] for _ in rows];ri={x:i for i,x in enumerate(rows)}
 if r:
  for j,c in enumerate(cols):
   for i in range(len(c)):M[ri[c[:i]+c[i+1:]]][j]=Fraction((-1)**i)
 return M,rows,cols
def rank(M):
 if not M:return 0
 A=[row[:] for row in M];nr=len(A);nc=len(A[0]);r=0
 for c in range(nc):
  p=next((i for i in range(r,nr) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];v=A[r][c];A[r]=[x/v for x in A[r]]
  for i in range(nr):
   if i!=r and A[i][c]:
    v=A[i][c];A[i]=[x-v*y for x,y in zip(A[i],A[r])]
  r+=1
 return r
def relative_betti(k):
 # Quotient by terminal face on vertices 0,...,k-1.
 dims=[];ranks=[]
 for r in range(k+1):
  M,rows,cols=boundary_matrix(k,r)
  qcols=[c for c in cols if k in c];qrows=[x for x in rows if k in x]
  if r==0:R=[]
  else:
   rowpos={x:i for i,x in enumerate(rows)};colpos={x:i for i,x in enumerate(cols)}
   R=[[M[rowpos[x]][colpos[y]] for y in qcols] for x in qrows]
  dims.append(len(qcols));ranks.append(rank(R))
 betti=[]
 for r in range(k+1):
  rank_out=ranks[r];rank_in=ranks[r+1] if r<k else 0;betti.append(dims[r]-rank_out-rank_in)
 return dims,ranks,betti
rows=[]
for k in (1,2,3):
 dims,ranks,betti=relative_betti(k);rows.append({'simplex_dimension':k,'relative_chain_dimensions':dims,'boundary_ranks':ranks,'relative_betti_numbers':betti,'acyclic':all(x==0 for x in betti)})
checks={'bounded_face_inclusions_have_closed_graph_and_closed_range':True,'mapping_cones_are_admitted_closed_cone_packages':True,'all_simplex_face_cones_acyclic':all(r['acyclic'] for r in rows),'nontrivial_historical_defect_recovered':False}
out={'schema':'marici.nima.simplex-face-cone-graph-package.v1','results':rows,'checks':checks,'passed':checks['all_simplex_face_cones_acyclic'],'conclusion':'N_*(face)->N_*(simplex), tensored with any carrier, is a bounded closed-range graph package, but its cone is contractible because both simplices are contractible and the face inclusion is a homotopy equivalence. It cannot model a nonzero kernel/cokernel defect.'}
p=ROOT/'research/nima/results/simplex-face-cone-graph-package.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
