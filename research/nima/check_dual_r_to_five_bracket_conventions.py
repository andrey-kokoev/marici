#!/usr/bin/env python3
"""Calibrate dual-spinor conventions against R_{n;st}=[n,s-1,s,t-1,t]."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r,theta_coefficients
from dual_spinor_kinematics import momentum_conserving_kinematics
from momentum_twistor_super import SuperTwistor,super_five_bracket
lams=[(1,1),(1,2),(2,1),(1,3),(3,2),(2,5)];tildes=[(1,0),(0,1),(1,2),(2,-1)];lam,til,x=momentum_conserving_kinematics(lams,tildes);theta=theta_coefficients(lam,6);eps=s.Matrix([[0,1],[-1,0]])
rpoly,_=generalized_r(lam,x,6,(),(2,5),lam[1].T*eps,lam[5].T*eps);labels=(6,1,2,4,5);rows=[]
for lower in (False,True):
 for shift in (0,1):
  S={}
  for i in range(1,7):
   li=eps*lam[i] if lower else lam[i];xi=x[i+shift];mu=xi.T*li;chi={j:s.simplify((li.T*v)[0]) for j,v in theta[i+shift].items()};chi={j:v for j,v in chi.items() if v!=0};S[i]=SuperTwistor(lam[i].col_join(mu),chi)
  try:fpoly=super_five_bracket(tuple(S[i] for i in labels));common=set(rpoly)&set(fpoly);ratios={s.factor(rpoly[m]/fpoly[m]) for m in common if fpoly[m]!=0};supports=set(rpoly)==set(fpoly);rows.append({'lower_lambda_in_incidence':lower,'dual_point_shift':shift,'support_equal':supports,'common_coefficients':len(common),'distinct_nonzero_ratios':len(ratios),'ratios':[str(v) for v in list(ratios)[:5]],'exact_equal':supports and ratios=={s.Integer(1)}})
  except Exception as exc:rows.append({'lower_lambda_in_incidence':lower,'dual_point_shift':shift,'error':str(exc)})
checks={'four_incidence_conventions_tested':len(rows)==4,'at_least_one_coefficientwise_proportional':any(r.get('support_equal') and r.get('distinct_nonzero_ratios')==1 for r in rows),'exact_convention_identified':any(r.get('exact_equal') for r in rows)}
out={'schema':'marici.nima.dual-r-to-five-bracket-conventions.v1','identity':'R_{6;25}=[6,1,2,4,5]','conventions':rows,'checks':checks,'passed':all(checks.values()),'scope':'Exact all-coefficient convention calibration at one rational dual polygon.'}
p=ROOT/'research/nima/results/dual-r-to-five-bracket-conventions.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
