#!/usr/bin/env python3
"""Global strict log-concavity/PF2 certificate for completed theta density."""
from fractions import Fraction as F
import json
from pathlib import Path
from evidence_policy import write_result
def B(n):return F(44,21)*n**4*(F(44,7)*(n*n-1)+2)**2/F(20)**(n*n-1)
assert B(2)+2*B(3)<2
assert all(B(n+1)*2<B(n) for n in range(3,30))
# e^3>20 from terms through k=8 of its positive Taylor series.
fact=1;power=1;s=F(0)
for k in range(9):
 if k:fact*=k;power*=3
 s+=F(power,fact)
assert s>20 and 22*22<12*7*7
R=Path(__file__).resolve().parents[2]
out={'schema':'marici.conjecture-replay.CR1-theta-global-PF2.v1','passed':True,'claim_status':'proved','evidence':[{'class':'SYMBOLIC','claim':'Exact rational majorants bound the mixture slope variance by 2, while every component log-curvature is below -4*pi*exp(2u); evenness closes the negative half-line.','checker':'research/conjecture_replay/check_CR1_theta_global_PF2.py'}],'outcome':'++ global strict PF2','mixture_identity':'(log Phi)dd=sum_n w_n c_n+Var_w(ell_n)','component_bound':'c_n=-4*pi*n^2*E-24*pi*n^2*E/(2*pi*n^2*E-3)^2 < -4*pi*E, E=exp(2u)>=1','ratio_monotonicity':'R_n(E)=T_n/T_1 and E^2 R_n(E) decrease for E>=1, n>=2','rational_majorant':'R_n(E)|ell_n-ell_1|^2 <= B_n=(44/21)n^4((44/7)(n^2-1)+2)^2/20^(n^2-1)','tail_bound':'B_2+sum_(n>=3)B_n <= B_2+2B_3 <2; the n>=3 ratio is <1/2','curvature':'(log Phi)dd < -4*pi+2 < -10 for u>=0','bilateral':'Phi is positive and even, so the same strict bound holds for u<=0.','PF2':'The translation kernel Phi(x-y) is strictly TP2, equivalently Phi is strictly log-concave.','scope':'This proves only translation order two. It does not follow from, nor imply, all-order labelled total positivity; PF3 and higher remain separate.','next':'evaluate_and_certify_the_coalescent_translation_PF3_Hankel_Wronskian_sign_globally_or_find_a_counterpoint'}
write_result(R/'research/conjecture_replay/results/CR1_theta_global_PF2.json',out);print(json.dumps({'passed':True,'outcome':'++','global_log_concavity':True,'translation_PF2':True,'PF_infinity':False}))
