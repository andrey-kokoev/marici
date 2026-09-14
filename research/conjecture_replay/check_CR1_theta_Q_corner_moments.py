#!/usr/bin/env python3
"""Moment representation and exact rank-100 test of theta corner polynomials."""
import json,math
from pathlib import Path
from evidence_policy import write_result
def odd(m):
 q=1
 for j in range(1,m+1):q*=2*j+1
 return q
E=[1];rows=[]
for r in range(1,101):
 y=6*r*r;E.append(0)
 for k in range(r,0,-1):E[k]+=y*E[k-1]
 q=sum((-1)**(r-k)*odd(r-k)*E[k] for k in range(r+1));assert q>0
 if r in {2,3,4,5,10,20,50,100}:rows.append({'rank':r,'Q_positive':True,'digits':len(str(q))})
R=Path(__file__).resolve().parents[2];out={'schema':'marici.conjecture-replay.CR1-theta-Q-corner-moments.v1','passed':True,'claim_status':'supported','evidence':[{'class':'SYMBOLIC','claim':'The odd-double-factorial coefficients are exactly moments of a chi-square variable with three degrees of freedom, giving the finite-product expectation formula.','checker':'research/conjecture_replay/check_CR1_theta_Q_corner_moments.py'},{'class':'NUMERICAL','claim':'Exact integer arithmetic verifies positive theta lower-corner polynomials for every rank 1 through 100.','checker':'research/conjecture_replay/check_CR1_theta_Q_corner_moments.py'}],'outcome':'all-rank positivity strongly supported; proof reduced to one expectation inequality','moment_formula':'Q_r(y)/prod_i y_i = E[prod_i(1-T/y_i)] for T distributed chi-square(3), since E[T^m]=(2m+1)!!','theta_corner':'y_i=6i^2','Euler_limit':'prod_(i>=1)(1-T/(6i^2))=sin(pi sqrt(T/6))/(pi sqrt(T/6))','limit_expectation':'For T=|G|^2 with G a standard three-dimensional Gaussian, spherical averaging identifies E[sinc(pi|G|/sqrt(6))]=exp(-pi^2/12)>0.','exact_tests':rows,'induction_bridge':'If corner positivity holds at every rank, derivative recursion and induction imply Q_r>0 on every ordered theta tuple, hence all-rank reverse sign regularity.','remaining_lemma':'Prove every finite expectation E[prod_(i=1)^r(1-T/(6i^2))] is positive. Positivity of its limit alone does not imply positivity of every partial expectation.','next':'seek_a_monotone_or_positive_integral_representation_for_the_finite_chi_square_expectations'}
write_result(R/'research/conjecture_replay/results/CR1_theta_Q_corner_moments.json',out);print(json.dumps({'passed':True,'status':'supported','exact_ranks':'1..100','positive_limit':'exp(-pi^2/12)','all_rank_proof':False}))
