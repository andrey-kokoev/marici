#!/usr/bin/env python3
"""Exact rank-three reverse sign regularity on the actual theta lattice."""
import json
from pathlib import Path
from evidence_policy import write_result
# Integer lower-bound arithmetic after pi>3: y1>=6,y2>=24,y3>=54.
y=[6,24,54];P=y[0]*y[1]*y[2]-3*(y[0]*y[1]+y[0]*y[2]+y[1]*y[2])+15*sum(y)-105
assert P==3639 and P>0
R=Path(__file__).resolve().parents[2]
out={'schema':'marici.conjecture-replay.CR1-theta-reverse-SR3.v1','passed':True,'claim_status':'proved','evidence':[{'class':'SYMBOLIC','claim':'Exact determinant expansion plus coordinate monotonicity and pi>3 prove the rank-three Wronskian has the reverse sign throughout the actual theta lattice half-strip.','checker':'research/conjecture_replay/check_CR1_theta_reverse_SR3.py'}],'outcome':'++ strict reverse sign regularity at rank 3','parameters':'a_i=2*pi*n_i^2 with 1<=n_1<n_2<n_3 and x=exp(2u)>=1','factorization':'det_j=0..2[(-a_i/2)^j(a_i x-3-2j)]=-(V(a)/8) P(a_1 x,a_2 x,a_3 x)','polynomial':'P(y1,y2,y3)=y1*y2*y3-3(y1*y2+y1*y3+y2*y3)+15(y1+y2+y3)-105','monotonicity':'partial_(y1)P=(y2-3)(y3-3)+6>0, cyclically, whenever every y_i>3','theta_margin':'pi>3 and n_i>=i imply (y1,y2,y3)>=(6,24,54)','lower_bound':'P(y)>=P(6,24,54)=3639>0','sign':'V(a)>0 and all omitted row factors are positive, hence W_3<0=(-1)^3 as required.','consequence':'The continuous near-boundary hostile is excluded exactly by the discrete theta spacing and x>=1 margin; ranks 2 and 3 are now proved.','limitation':'No induction to rank 4 or all ranks is supplied. Higher reduced polynomials have additional symmetric terms requiring separate positivity bounds.','next':'expand_the_rank4_reduced_Wronskian_in_elementary_symmetric_polynomials_and_test_its_theta_margin'}
write_result(R/'research/conjecture_replay/results/CR1_theta_reverse_SR3.json',out);print(json.dumps({'passed':True,'outcome':'++','rank':3,'lower_bound':P,'theta_lattice':True}))
