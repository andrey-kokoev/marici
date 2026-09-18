#!/usr/bin/env python3
"""SL(2,C) holonomies from actual diagonal NNMHV boundary-update paths."""
import cmath,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def add(A,B):return tuple(a+b for a,b in zip(A,B))
def sub(A,B):return tuple(a-b for a,b in zip(A,B))
def mm(A,B):return (A[0]*B[0]+A[1]*B[2],A[0]*B[1]+A[1]*B[3],A[2]*B[0]+A[3]*B[2],A[2]*B[1]+A[3]*B[3])
def det(A):return A[0]*A[3]-A[1]*A[2]
def adj(A):return (A[3],-A[1],-A[2],A[0])
def inv(A):return tuple(v/det(A) for v in adj(A))
def outer(a,b):return (a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
def normsl(A):
 r=cmath.sqrt(det(A));return tuple(v/r for v in A)
def z(v):return {'real':v.real,'imag':v.imag}
n=8;lam={i:(1+0j,complex(i*i+i+1,i%3-1)) for i in range(1,n+1)};til={i:(1+.13j*i,complex(i**3+1,-i)) for i in range(1,n-1)};M=(0j,0j,0j,0j)
for i in range(1,n-1):M=add(M,outer(lam[i],til[i]))
L=(lam[n-1][0],lam[n][0],lam[n-1][1],lam[n][1]);Y=mm(inv(L),tuple(-v for v in M));til[n-1]=(Y[0],Y[1]);til[n]=(Y[2],Y[3]);x={1:(0j,0j,0j,0j)}
for i in range(1,n+1):x[i+1]=sub(x[i],outer(lam[i],til[i]))
def X(a,b):return sub(x[a],x[b])
def path(vertices):
 R=(1+0j,0j,0j,1+0j)
 for k,(a,b) in enumerate(zip(vertices,vertices[1:])):R=mm(R,X(a,b) if k%2==0 else adj(X(a,b)))
 return R
hol={}
for b in range(5,n-1):
 xi=path((n,b,2));upper=path((n,2,b));hol[b]=normsl(mm(xi,inv(upper)))
plaquettes=[]
for b in range(5,n-2):
 C=normsl(mm(hol[b+1],inv(hol[b])));tr=C[0]+C[3];disc=cmath.sqrt(tr*tr-4);e=(tr+disc)/2;rap=cmath.log(e);plaquettes.append({'b_to_bplus1':[b,b+1],'trace':z(tr),'rapidity':z(rap),'nontriviality':max(abs(C[i]-(1 if i in (0,3) else 0)) for i in range(4))})
checks={'momentum_closure':max(abs(v) for v in x[n+1])<1e-8,'all_boundary_holonomies_in_sl2':all(abs(det(R)-1)<1e-8 for R in hol.values()),'adjacent_boundary_curvature_nonzero':all(p['nontriviality']>1e-6 for p in plaquettes),'curvature_has_complex_phase':any(abs(p['rapidity']['imag'])>1e-6 for p in plaquettes)}
out={'schema':'marici.nima.nnmhv-boundary-update-holonomy.v1','n':n,'definition':'R_b = normalize(M_(n,b,2) inverse(M_(n,2,b)))','boundary_holonomies':{str(b):[z(v) for v in R] for b,R in hol.items()},'adjacent_plaquette_curvatures':plaquettes,'checks':checks,'passed':all(checks.values()),'scope':'Actual source boundary paths on one complex momentum-conserving eight-point polygon; comparison with scalar insertion cocycle remains open.'};p=ROOT/'research/nima/results/nnmhv-boundary-update-holonomy.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
