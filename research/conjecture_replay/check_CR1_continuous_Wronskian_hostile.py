#!/usr/bin/env python3
"""Exact rank-3 hostile to the overbroad continuous Wronskian conjecture."""
import json
from fractions import Fraction as F
from pathlib import Path
from evidence_policy import write_result
def det3(m):return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
a=[F(23),F(26),F(36)];x=F(3,23);M=[[(-q/F(2))**j*(q*x-3-2*j) for j in range(3)] for q in a];d=det3(M);assert d>0 # expected reverse-SR3 sign is negative
R=Path(__file__).resolve().parents[2];out={'schema':'marici.conjecture-replay.CR1-continuous-Wronskian-hostile.v1','passed':True,'claim_status':'falsified','evidence':[{'class':'SYMBOLIC','claim':'An exact rational rank-3 reduced Wronskian has the wrong sign at the positivity boundary and therefore on a right neighborhood by continuity.','checker':'research/conjecture_replay/check_CR1_continuous_Wronskian_hostile.py'}],'outcome':'broad continuous-parameter sign conjecture falsified','witness':{'a':[23,26,36],'x':'3/23','reduced_determinant':str(d),'actual_sign':'+','required_reverse_SR3_sign':'-'},'open_neighborhood':'The determinant is nonzero at x=3/23, so it remains positive for some x>3/23 where every ax-3 is positive.','scope_correction':'K(a,x)=a(ax-3)exp(-ax/2) is not reverse sign-regular on the full continuous domain ax>3.','theta_not_falsified':'Actual theta parameters are a=2*pi*n^2 and x=exp(2u)>=1, hence ax>=2*pi*n^2. The hostile lies far outside that lattice half-strip.','revised_target':'Prove or falsify sign regularity only on a_i=2*pi*n_i^2, x>=1. A continuous extension down to ax>3 is too strong.','next':'derive_a_Wronskian_sign_bound_using_the_theta_margin_a_1*x>=2*pi'}
write_result(R/'research/conjecture_replay/results/CR1_continuous_Wronskian_hostile.json',out);print(json.dumps({'passed':True,'claim_status':'falsified','rank':3,'theta_domain_falsified':False,'continuous_extension_falsified':True}))
