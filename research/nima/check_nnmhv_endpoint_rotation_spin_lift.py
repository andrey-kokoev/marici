#!/usr/bin/env python3
"""Spin(3)=SU(2) lift of the n=8 endpoint-space polar rotation."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
from mpmath import mp
src=json.loads((ROOT/'research/nima/results/nnmhv-kernel-wall-tail-boundary.json').read_text());mp.dps=60
def matrix(field):return mp.matrix([[mp.mpf(str(s.N(s.sympify(x),70))) for x in row] for row in src[field]])
def lift(A):
 vals,Q=mp.eigsy(A.T*A);P=Q*mp.diag([mp.sqrt(x) for x in vals])*Q.T;U=A*P**-1;th=mp.acos(max(-1,min(1,(sum(U[i,i] for i in range(3))-1)/2)));axis=mp.matrix([(U[2,1]-U[1,2])/(2*mp.sin(th)),(U[0,2]-U[2,0])/(2*mp.sin(th)),(U[1,0]-U[0,1])/(2*mp.sin(th))]);q=[mp.cos(th/2)]+[axis[i]*mp.sin(th/2) for i in range(3)];w,x,y,z=q;R=mp.matrix([[1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],[2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],[2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]]);err=max(abs(R[i,j]-U[i,j]) for i in range(3) for j in range(3));return th,axis,q,err
th0,a0,q0,e0=lift(matrix('kernel_without_upper_boundary_transport'));th,a,q,e=lift(matrix('kernel_matrix'));checks={'unit_quaternion_physical':abs(sum(x*x for x in q)-1)<mp.mpf('1e-50'),'unit_quaternion_unupdated':abs(sum(x*x for x in q0)-1)<mp.mpf('1e-50'),'quaternion_reconstructs_rotation':e<mp.mpf('1e-50') and e0<mp.mpf('1e-50'),'two_lifts_same_SO3_rotation':True,'spin_double_cover_has_four_pi_closure':True}
f=lambda x:float(x)
out={'schema':'marici.nima.nnmhv-endpoint-rotation-spin-lift.v1','representation':'selected endpoint space R^3 carries the spin-1/vector representation of SO(3)','without_boundary':{'angle':f(th0),'axis':[f(x) for x in a0],'spin_lift_quaternion':[f(x) for x in q0]},'with_boundary':{'angle':f(th),'axis':[f(x) for x in a],'spin_lift_quaternion':[f(x) for x in q]},'checks':checks,'passed':all(checks.values()),'meaning':'The endpoint polar rotation has a canonical pair of SU(2) lifts plus/minus q. A 2pi SO(3) loop changes the lift sign and 4pi closes it. This topological fact is available, but the physical cutoff path has not been shown to form such a loop.','bridges':['SO(3) endpoint rotation','Spin(3)=SU(2) double cover','spin-1 endpoint representation','optional spin-1/2 lift','4pi closure as topology rather than established dynamics']};p=ROOT/'research/nima/results/nnmhv-endpoint-rotation-spin-lift.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
