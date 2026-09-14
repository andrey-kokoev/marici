#!/usr/bin/env python3
"""Asymptotic no-go for the proposed finite-vector resolvent realization."""
import json,math
from pathlib import Path

def main():
 # For self-adjoint A and x>0, |2x/(x^2+lambda^2)| <= 2/x pointwise.
 xs=(10,100,1000,10000);rows=[]
 for x in xs:
  resolvent_bound=2/x # unit cyclic vector
  xi_log_derivative_leading=.5*math.log(x/(2*math.pi))
  rows.append({'x':x,'unit_vector_resolvent_bound':resolvent_bound,'xi_log_derivative_Stirling_leading_term':xi_log_derivative_leading})
 assert rows[-1]['xi_log_derivative_Stirling_leading_term']>1
 assert rows[-1]['unit_vector_resolvent_bound']<.001
 result={'schema':'marici.voevodsky.arithmetic-resolvent-asymptotic-no-go.v1','operator_bound':'|<Omega,[(x-iA)^-1+(x+iA)^-1]Omega>| <= 2||Omega||^2/x','target_asymptotic':'Xi prime(x)/Xi(x) = half log(x/(2pi)) + O(1/x) on the positive real axis','rows':rows,'contradiction':'finite-norm vector resolvent tends to zero while target diverges logarithmically','bold_conjecture_as_stated':False,'surviving_repairs':['subtract the full explicit archimedean logarithmic reference before asking for a vector resolvent','replace Omega by a distributional/rigged vector with infinite spectral mass and prove Gaussian regularizations are Hilbert vectors'],'warning':'An affine correction cannot repair logarithmic growth.'}
 out=Path(__file__).parents[1]/'results'/'arithmetic_resolvent_asymptotic_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
