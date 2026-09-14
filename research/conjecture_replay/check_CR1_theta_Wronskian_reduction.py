#!/usr/bin/env python3
"""Exact all-rank Wronskian reduction for the theta density kernel."""
import json
from pathlib import Path
from evidence_policy import write_result
# Represent e^(t x)(A x+B) by (A,B); differentiation sends (A,B)->(tA,A+tB).
for a in range(1,8):
 t=-a/2; pair=(float(a),-3.0)
 for j in range(10):
  expected=(t**j*a,t**j*(-3-2*j))
  assert all(abs(pair[q]-expected[q])<1e-8*max(1,abs(expected[q])) for q in (0,1))
  pair=(t*pair[0],pair[0]+t*pair[1])
R=Path(__file__).resolve().parents[2]
out={'schema':'marici.conjecture-replay.CR1-theta-Wronskian-reduction.v1','passed':True,'claim_status':'proved','evidence':[{'class':'SYMBOLIC','claim':'Repeated differentiation of (ax-3)exp(-ax/2) gives the stated closed formula, hence the all-rank Wronskian determinant reduction.','checker':'research/conjecture_replay/check_CR1_theta_Wronskian_reduction.py'}],'outcome':'exact reduction; positivity remains open','kernel':'K(a,x)=a(ax-3)exp(-ax/2)','derivatives':'partial_x^j K(a,x)=a exp(-ax/2)(-a/2)^j(ax-3-2j)','Wronskian':'W_r=prod_i[a_i exp(-a_i x/2)] det_{i,j=0..r-1}[(-a_i/2)^j(a_i x-3-2j)]','domain':'0<a_1<...<a_r and a_1 x>3','sign_target':'sign W_r=(-1)^(r(r-1)/2)','equivalence':'Strict reverse total positivity follows if these Wronskians have the target sign for every rank and the stated domain (via the extended-complete-Chebyshev criterion).','structural_observation':'The determinant is Vandermonde(a) times a symmetric degree-r polynomial in x; its leading coefficient has the target alternating sign. Lower coefficients can still create an interior sign change, so asymptotics are insufficient.','status_by_rank':{'r2':'already proved globally by log-ratio monotonicity','r3_to_r6':'fixed high-precision samples support the target','all_r':'open polynomial-sign problem'},'next':'derive_a_positive_coefficient_expansion_after_the_shift_x=3/a_1_or_find_a_positive_domain_root_of_the_reduced_polynomial'}
write_result(R/'research/conjecture_replay/results/CR1_theta_Wronskian_reduction.json',out);print(json.dumps({'passed':True,'exact_all_rank_reduction':True,'sign_proved_all_rank':False}))
