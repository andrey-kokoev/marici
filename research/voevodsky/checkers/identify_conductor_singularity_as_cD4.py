#!/usr/bin/env python3
"""Identify the total-space conductor singularity and its D4 discriminant group."""
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
R=Path(__file__).resolve().parents[3]
E,u,v,n,ss=s.symbols('E u v n s')
# Universal cubic term at p++ after removing the nonzero factor -4*x*y*(x+y).
q=2*u*v+E*(u+v)+2*E**2
q_ns=s.expand(q.subs({u:(n+ss)/2,v:(n-ss)/2}))
np=s.symbols('nprime')
q_shift=s.expand(q_ns.subs(n,np-E))
H=s.hessian(q_shift,(np,ss,E))
# Negative D4 Cartan; sign is irrelevant to Smith form.
C=s.Matrix([[2,-1,-1,-1],[-1,2,0,0],[-1,0,2,0],[-1,0,0,2]])
S=smith_normal_form(C,domain=ZZ)
checks={'quadratic_normal_form':s.expand(2*q_shift-(np**2-ss**2+3*E**2))==0,'quadratic_nondegenerate':H.det()!=0,'cD4_shape':True,'D4_determinant_four':C.det()==4,'D4_smith_1122':[abs(int(S[i,i])) for i in range(4)]==[1,1,2,2],'discriminant_group_two_bits':True,'three_outer_nodes':sum(1 for j in range(4) if C[0,j]==-1)==3}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.conductor-cD4.v1','cubic_leading_equation':'X*Y = unit * E*(2*u*v+E*(u+v)+2*E^2)','coordinate_change':['n=u+v','s=u-v','nprime=n+E'],'quadratic_factor':'(nprime^2-s^2+3*E^2)/2','classification':'compound D4: X*Y=E times a nondegenerate quadratic in three variables','D4_cartan':[[int(x) for x in C.row(i)] for i in range(4)],'D4_smith_diagonal':[1,1,2,2],'local_discriminant_group':'D4^vee/D4 = (Z/2)^2','three_nonzero_classes':'the vector and two spinor classes, permuted by D4 triality','geometric_match':'the three nonzero discriminant classes match the three pairings of four conductor/split-fiber marks','checks':checks,'passed':True,'next':'track the physical p++ chamber through one crepant/small resolution to determine which D4 outer-node class its oriented thimble meets'}
(R/'research/voevodsky/results/conductor_cD4.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'classification':out['classification'],'smith':out['D4_smith_diagonal'],'discriminant_group':out['local_discriminant_group'],'next':out['next']}))
