#!/usr/bin/env python3
"""Verify the unique endpoint comparison candidate forced by V_p."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_endpoint_comparison_unique_candidate_certificate_20260908.json');a=p.parse_args()
 r=s.symbols('r',positive=True);V=s.Matrix([[1,r],[r,1]])/2
 Vinv=2*s.Matrix([[1,-r],[-r,1]])/(1-r**2);checks=0
 assert s.simplify(V*Vinv-s.eye(2))==s.zeros(2);checks+=1
 wall=s.Matrix([1,1])/s.sqrt(2);jump=s.Matrix([1,-1])/s.sqrt(2)
 assert s.simplify(V*wall-(1+r)*wall/2)==s.zeros(2,1);checks+=1
 assert s.simplify(V*jump-(1-r)*jump/2)==s.zeros(2,1);checks+=1
 assert s.simplify(Vinv*wall-2*wall/(1+r))==s.zeros(2,1);checks+=1
 assert s.simplify(Vinv*jump-2*jump/(1-r))==s.zeros(2,1);checks+=1
 out={'schema':'marici.rh.endpoint-comparison-unique-candidate.v1','status':'unique_candidate_reduced_to_trace_faithfulness','checks':checks,
 'candidate':'A_p=V_p^{-1} Tr_end T_hist,p J_P','inverse':'2/(1-p^-2) [[1,-p^-1],[-p^-1,1]]',
 'inverse_singular_values':['2/(1+p^-1)','2/(1-p^-1)'],
 'prime_uniform_bounds':'for p>=2, 4/3 <= sigma_min(V_p^-1) <= sigma_max(V_p^-1) <= 4',
 'consequence':'A_p exists uniquely whenever the analytic endpoint trace is typed; its injectivity and lower bound are exactly those of that trace, up to explicit uniform constants',
 'boundary':'this does not prove the analytic endpoint trace is injective on the Adams source relation or that the composition preserves the Green form'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks}))
if __name__=='__main__':main()
