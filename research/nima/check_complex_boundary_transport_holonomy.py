#!/usr/bin/env python3
"""Complex spinorial holonomy of a closed alternating boundary-transport cell."""
import cmath,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def add(A,B):return tuple(a+b for a,b in zip(A,B))
def sub(A,B):return tuple(a-b for a,b in zip(A,B))
def mm(A,B):return (A[0]*B[0]+A[1]*B[2],A[0]*B[1]+A[1]*B[3],A[2]*B[0]+A[3]*B[2],A[2]*B[1]+A[3]*B[3])
def det(A):return A[0]*A[3]-A[1]*A[2]
def adj(A):return (A[3],-A[1],-A[2],A[0])
def outer(a,b):return (a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
lam={i:(1+0j,complex(i*i+i+1,i%3-1)) for i in range(1,7)};til={i:(1+0.2j*i,complex(i**3+1,-i)) for i in range(1,5)};M=(0j,0j,0j,0j)
for i in range(1,5):M=add(M,outer(lam[i],til[i]))
L=(lam[5][0],lam[6][0],lam[5][1],lam[6][1]);Li=tuple(v/det(L) for v in adj(L));Y=mm(Li,tuple(-v for v in M));til[5]=(Y[0],Y[1]);til[6]=(Y[2],Y[3]);x={1:(0j,0j,0j,0j)}
for i in range(1,7):x[i+1]=sub(x[i],outer(lam[i],til[i]))
def X(a,b):return sub(x[a],x[b])
vertices=(6,2,5,3,6);H=(1+0j,0j,0j,1+0j)
for k,(a,b) in enumerate(zip(vertices,vertices[1:])):H=mm(H,X(a,b) if k%2==0 else adj(X(a,b)))
d=det(H);root=cmath.sqrt(d);R=tuple(v/root for v in H);tr=R[0]+R[3];disc=cmath.sqrt(tr*tr-4);eig=((tr+disc)/2,(tr-disc)/2);logs=tuple(cmath.log(v) for v in eig)
def z(v):return {'real':v.real,'imag':v.imag}
checks={'momentum_closure':max(abs(v) for v in x[7])<1e-8,'normalized_holonomy_det_one':abs(det(R)-1)<1e-8,'reciprocal_spinor_eigenvalues':abs(eig[0]*eig[1]-1)<1e-8,'genuine_complex_phase':any(abs(v.imag)>1e-6 for v in logs),'not_purely_unitary':any(abs(v.real)>1e-6 for v in logs)}
out={'schema':'marici.nima.complex-boundary-transport-holonomy.v1','loop_vertices':list(vertices),'holonomy_det':z(d),'normalized_holonomy':[z(v) for v in R],'eigenvalues':[z(v) for v in eig],'complex_rapidities':[z(v) for v in logs],'phase_angles':[v.imag for v in logs],'boost_parts':[v.real for v in logs],'checks':checks,'passed':all(checks.values()),'interpretation':'Complex boundary transport yields reciprocal spinor holonomies with both phase and boost. A 4pi phase law requires isolating the unitary part, not using raw transport.'};p=ROOT/'research/nima/results/complex-boundary-transport-holonomy.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
