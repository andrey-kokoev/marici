#!/usr/bin/env python3
"""Polar decomposition of complex boundary holonomy into boost and SU(2) phase."""
import cmath,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];src=json.loads((ROOT/'research/nima/results/complex-boundary-transport-holonomy.json').read_text());z=lambda d:complex(d['real'],d['imag']);R=tuple(z(v) for v in src['normalized_holonomy'])
def mm(A,B):return (A[0]*B[0]+A[1]*B[2],A[0]*B[1]+A[1]*B[3],A[2]*B[0]+A[3]*B[2],A[2]*B[1]+A[3]*B[3])
def adj(A):return (A[3],-A[1],-A[2],A[0])
def det(A):return A[0]*A[3]-A[1]*A[2]
def dagger(A):return (A[0].conjugate(),A[2].conjugate(),A[1].conjugate(),A[3].conjugate())
def scale(c,A):return tuple(c*v for v in A)
def add(A,B):return tuple(a+b for a,b in zip(A,B))
def inv(A):return scale(1/det(A),adj(A))
def out(A):return [{'real':v.real,'imag':v.imag} for v in A]
H=mm(dagger(R),R);sd=cmath.sqrt(det(H));den=cmath.sqrt(H[0]+H[3]+2*sd);P=scale(1/den,add(H,(sd,0j,0j,sd)));U=mm(R,inv(P));tr=U[0]+U[3];theta=math.acos(max(-1,min(1,tr.real/2)));recon=mm(U,P);err=max(abs(a-b) for a,b in zip(recon,R));unit=mm(dagger(U),U);I=(1+0j,0j,0j,1+0j)
checks={'polar_reconstruction':err<1e-10,'boost_positive_hermitian':max(abs(a-b) for a,b in zip(P,dagger(P)))<1e-10,'rotation_unitary':max(abs(a-b) for a,b in zip(unit,I))<1e-8,'rotation_special_unitary':abs(det(U)-1)<1e-8,'spinor_requires_4pi_for_identity':abs(cmath.exp(1j*2*math.pi)-1)<1e-12 and abs(cmath.exp(1j*math.pi)+1)<1e-12}
outj={'schema':'marici.nima.boundary-holonomy-polar-decomposition.v1','boost_P':out(P),'rotation_U':out(U),'spinor_eigenangle_theta':theta,'physical_rotation_angle_2theta':2*theta,'reconstruction_error':err,'checks':checks,'passed':all(checks.values()),'interpretation':'Boundary holonomy factors as R=UP with positive boost P and SU(2) rotation U. The spinor phase belongs to U; physical rotation is twice its eigenangle.'};p=ROOT/'research/nima/results/boundary-holonomy-polar-decomposition.json';p.write_text(json.dumps(outj,indent=2)+'\n');print(json.dumps(outj,indent=2));raise SystemExit(0 if outj['passed'] else 1)
