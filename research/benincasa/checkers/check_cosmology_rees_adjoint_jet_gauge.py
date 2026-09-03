#!/usr/bin/env python3
"""Verify scalar jet gauge invariance of assembled adjoint closure."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
# Represent pairings p_ij=lambda_i(r_j). Closure coefficients are
# c0=p00, c1=p10+p01, c2=p20+p11+p02.
p={(0,0):F(0),(1,0):F(2),(0,1):F(-2),(2,0):F(5),(1,1):F(-7),(0,2):F(2)};a=F(3);b=F(-4)
# lambda'_0=lambda0; lambda'_1=lambda1+a lambda0; lambda'_2=lambda2+a lambda1+b lambda0.
pp={(0,j):p.get((0,j),0) for j in range(3)}
for j in range(3):pp[(1,j)]=p.get((1,j),0)+a*p.get((0,j),0);pp[(2,j)]=p.get((2,j),0)+a*p.get((1,j),0)+b*p.get((0,j),0)
def cs(x):return [x.get((0,0),0),x.get((1,0),0)+x.get((0,1),0),x.get((2,0),0)+x.get((1,1),0)+x.get((0,2),0)]
assert cs(p)==[0,0,0] and cs(pp)==[0,0,0]
out={'schema':'marici.benincasa.cosmology-rees-adjoint-jet-gauge.v1','rescaling':'lambda(E) maps to (1+aE+bE^2) lambda(E)','jet_action':['lambda0 unchanged','lambda1 maps to lambda1+a lambda0','lambda2 maps to lambda2+a lambda1+b lambda0'],'closure_invariant':True,'normalization_lambda0_tau_invariant':True,'consequence':'assembled adjoint closure and special-fiber normalization cannot determine the first and second scalar jets; they form an intrinsic two-parameter gauge orbit','required_replacement':'either quotient dual jets by invertible scalar 2-jets or supply a connection/parallel-normalization law','uniform_tau_nonvanishing_relevance':'a nonzero lambda0 certificate is gauge-invariant; a canonical jet coordinate is not','passed':True};(R/'cosmology_rees_adjoint_jet_gauge.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
