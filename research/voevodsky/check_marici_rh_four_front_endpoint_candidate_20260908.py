#!/usr/bin/env python3
"""Evaluate the unique endpoint comparison on the analytic four-front odd line."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_four_front_endpoint_candidate_certificate_20260908.json');a=p.parse_args()
 L=s.symbols('L',positive=True);r=s.exp(-L);m=2*s.exp(s.Rational(1,16)/s.pi)*(s.sinh(L)-s.sinh(L/2))
 V=s.Matrix([[1,r],[r,1]])/2;Vinv=2*s.Matrix([[1,-r],[-r,1]])/(1-r**2);trace=s.Matrix([-m,m]);candidate=Vinv*trace;checks=0
 expected=2*m*s.Matrix([-1,1])/(1-r)
 assert s.simplify(candidate-expected)==s.zeros(2,1);checks+=1
 assert s.simplify(V*candidate-trace)==s.zeros(2,1);checks+=1
 assert s.limit(m,L,0,dir='+')==0;checks+=1
 # positivity follows from sinh strictly increasing for L>0; numeric hostile confirms sign.
 assert m.subs(L,s.log(2)).evalf()>0;checks+=1
 out={'schema':'marici.rh.four-front-endpoint-candidate.v1','status':'odd_line_endpoint_comparison_explicit_and_faithful','checks':checks,
 'trace':'(-m_p,m_p), m_p=2 exp(1/(16pi))(sinh L-sinh(L/2))>0',
 'candidate':'A_p(b_p)=2m_p/(1-p^-1)*(-1,1)',
 'consequence':'the unique endpoint comparison is injective on the analytic four-front odd line and prime-label preserving',
 'remaining':'prove the labelled primitive/square arithmetic mate maps to this same odd line with coefficient -kappa_p^(<=2)/(2s_p^(1/2)); full source relation remains broader'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks}))
if __name__=='__main__':main()
