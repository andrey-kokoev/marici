#!/usr/bin/env python3
"""Exact type no-go: a weighted unilateral Adams shift is not a positive self-adjoint contraction."""
import json
from fractions import Fraction
from pathlib import Path

def main():
 rho=Fraction(1,2)
 # Two-grade truncation: primitive grade maps forward, terminal grade maps out of truncation.
 A=[[Fraction(0),Fraction(0)],[rho,Fraction(0)]]
 At=[list(x) for x in zip(*A)];assert A!=At
 x=[1,-1];quad=sum(x[i]*A[i][j]*x[j] for i in range(2) for j in range(2));assert quad<0
 # Norm contraction follows from A* A <= I despite failure of order positivity.
 AtA=[[sum(At[i][k]*A[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
 result={'schema':'marici.voevodsky.Adams-contraction-not-Hausdorff-positive-filter.v1','weighted_shift':[[str(v) for v in row] for row in A],'A_star_A':[[str(v) for v in row] for row in AtA],'operator_norm_at_most_one':True,'self_adjoint':False,'quadratic_witness':x,'quadratic_value':str(quad),'order_positive':False,'theorem':'A weighted grade-raising shift may be a strict norm contraction while failing self-adjointness and operator positivity.','source_mismatch':['Adams acts by multiplicative integer grade reindexing k->rk','Hausdorff Y_h acts on one fixed moment carrier for every additive real h','Adams has a proper closed divisible-grade range','Y_h=e^(-hL) must be self-adjoint positive'],'conclusion':'The existing weighted Adams semigroup cannot be identified directly with the Hausdorff binary filter Y_h.'}
 out=Path(__file__).parents[1]/'results'/'Adams_contraction_not_Hausdorff_positive_filter.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
