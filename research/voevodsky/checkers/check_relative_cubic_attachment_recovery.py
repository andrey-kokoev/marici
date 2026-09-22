"""Exact cone signs, relative recovery and nullhomotopy ambiguity.

Fixture: nonsplit k[t]-extension k -> k[t]/t^2 -> k. Actual source
nonvanishing and the bounded H are the companion source theorems.
"""
from pathlib import Path
import json
import sympy as s
# B -> A -> G; K=A, H=id, f=i. Original scalar target is k with t=0.
i=s.Matrix([[0],[1]]);q=s.Matrix([[1,0]]);J=i*q
H=s.eye(2);f=i;ell=s.eye(1)
assert q*i==s.zeros(1,1) and H*i==f
# P=[B -> A], R[1]=[B --(-f)--> K].
lift_m=s.eye(1);lift_0=-H
assert (-f)*lift_m==lift_0*i
# Homotopy pushout Z=Cone((ell,-f):B[1]->k[1]+K[1]).
dZ=ell.col_join(-f)
original=s.Matrix([[1],[0],[0]])
null_m=s.eye(1);null_0=s.zeros(1,2).col_join(H)
assert dZ*null_m+null_0*i==original
# Fib(k[1] -> Z) retracts onto R[1].
dFib=s.Matrix([[1,-1],[0,0],[0,1]])
u_m=s.Matrix([[1],[1]])
u_0=s.Matrix([[0,0],[-1,0],[0,-1]])
v_m=s.Matrix([[0,1]])
v_0=s.Matrix([[0,-1,0],[0,0,-1]])
assert dFib*u_m==u_0*(-f)
assert v_0*dFib==(-f)*v_m
assert v_m*u_m==s.eye(1) and v_0*u_0==s.eye(2)
h=s.Matrix([[1,0,0],[0,0,0]])
assert h*dFib==s.eye(2)-u_m*v_m
assert dFib*h==s.eye(3)-u_0*v_0
# The recovered extension is 0 -> im(f) -> K -> coker(f) -> 0.
barH=q*H
assert barH==q
assert J==i*q
# No equivariant section: q*s=1 and J*s=0 are incompatible.
constraints=q.col_join(J);rhs=s.Matrix([1,0,0])
assert constraints.rank()<constraints.row_join(rhs).rank()
# Two equivariant choices of H differ through G; their relative lifts differ
# by the K[0] inclusion in R[1], and receiver projection kills that ambiguity.
c=s.symbols('c')
u=s.Matrix([[0],[c]])
Hp=H+u*q
assert Hp*i==f and Hp*J==J*Hp
assert -Hp-(-H)==-u*q
# Frame isomorphism K -> K' transports all source-relative maps exactly.
W=s.diag(2,3);Wi=W.inv();fp=W*f;Hframe=W*H
assert Hframe*i==fp
assert W*(-H)==-Hframe
assert W*(-f)==-fp
assert (Wi*Hframe)==H
result={'passed':True,'checks':{
 'relative_lift_chain_map_signs':True,
 'original_receiver_class_null_in_homotopy_pushout':True,
 'receiver_fiber_retracts_to_source_observer_fiber':True,
 'image_cokernel_extension_is_nonsplit':True,
 'nullhomotopy_ambiguity_factors_through_K':True,
 'frame_transport_is_natural':True},
 'scope':'Exact module/cone fixtures. Actual relative nonvanishing follows by projection to the already nonzero original cubic roof, and the scalar quotient detector by the actual retained cubic functional. No recovery by functorial application to a zero class is claimed.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/relative-cubic-attachment-recovery.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
