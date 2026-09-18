#!/usr/bin/env python3
"""Factor the scalar mismatch in R_{6;25}=[6,1,2,4,5]."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r,theta_coefficients
from dual_spinor_kinematics import momentum_conserving_kinematics
from momentum_twistor_constructors import four_bracket
from momentum_twistor_super import SuperTwistor
lams=[(1,1),(1,2),(2,1),(1,3),(3,2),(2,5)];tildes=[(1,0),(0,1),(1,2),(2,-1)];lam,til,x=momentum_conserving_kinematics(lams,tildes);theta=theta_coefficients(lam,6);eps=s.Matrix([[0,1],[-1,0]])
_,meta=generalized_r(lam,x,6,(),(2,5),lam[1].T,lam[5].T);labels=(6,1,2,4,5);S={}
for i in range(1,7):
 li=eps*lam[i];mu=x[i].T*li;chi={j:s.simplify((li.T*v)[0]) for j,v in theta[i].items()};S[i]=SuperTwistor(lam[i].col_join(mu),{j:v for j,v in chi.items() if v!=0})
V=tuple(S[i] for i in labels);qs=[]
for i in range(5):qs.append(four_bracket(V[(i+1)%5].z,V[(i+2)%5].z,V[(i+3)%5].z,V[(i+4)%5].z))
five_delta={}
for q,v in zip(qs,V):
 for label,c in v.chi.items():five_delta[label]=s.simplify(five_delta.get(label,0)+q*c)
five_delta={i:v for i,v in five_delta.items() if v!=0};common=set(meta['xi_coefficients'])&set(five_delta);scales={s.factor(meta['xi_coefficients'][i]/five_delta[i]) for i in common};scale=next(iter(scales));five_prefactor=s.factor(1/s.prod(qs));predicted=s.factor(meta['prefactor']*scale**4/five_prefactor)
checks={'fermionic_forms_have_one_scale':len(scales)==1,'predicted_ratio_is_observed_mismatch':predicted==s.Rational(-22,181),'all_prefactor_factors_nonzero':meta['prefactor']!=0 and five_prefactor!=0 and scale!=0}
out={'schema':'marici.nima.dual-r-scalar-normalization-diagnostic.v1','identity':'R_{6;25}=[6,1,2,4,5]','xi_scale_dual_over_twistor':str(scale),'dual_r_prefactor':str(meta['prefactor']),'five_bracket_prefactor':str(five_prefactor),'dual_denominator_factors':[str(v) for v in meta['denominator_factors']],'five_cyclic_four_brackets':[str(v) for v in qs],'reconstructed_ratio':str(predicted),'checks':checks,'passed':all(checks.values()),'scope':'Exact scalar factorization of the convention mismatch at one rational dual polygon.'}
p=ROOT/'research/nima/results/dual-r-scalar-normalization-diagnostic.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
