#!/usr/bin/env python3
"""Exact Fourier-symbol formula for the log-scale theta Dirichlet kernel."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_sech_kernel_fourier_symbol_certificate_20260908.json');args=p.parse_args();w=s.symbols('w',real=True);a=s.Rational(5,2);checks=0
 left=(a-s.I*w)/2;right=(a+s.I*w)/2
 beta_symbol=2**(a-1)*s.beta(left,right)
 gamma_symbol=2**(a-1)*s.gamma(left)*s.gamma(right)/s.gamma(a)
 assert s.simplify(s.expand_func(beta_symbol)-gamma_symbol)==0;checks+=1
 at_zero=s.simplify(gamma_symbol.subs(w,0))
 classical=s.sqrt(s.pi)*s.gamma(a/2)/s.gamma((a+1)/2)
 zero_residual=s.expand_func(at_zero-classical)
 zero_residual=zero_residual.subs(s.gamma(s.Rational(3,4)),s.pi*s.sqrt(2)/s.gamma(s.Rational(1,4)))
 assert s.simplify(zero_residual)==0;checks+=1
 assert s.simplify(right-s.conjugate(left))==0;checks+=1
 # Gamma has no zeros and no poles at Re((a+iw)/2)=5/4>0; therefore the
 # conjugate product is strictly positive for every real frequency.
 real_part=s.re(right);assert real_part==s.Rational(5,4);checks+=1
 out={'schema':'marici.rh.sech-kernel-fourier-symbol.v1','status':'strict_positive_fourier_symbol','checks':checks,'kernel':'K(t)=sech(t)^(5/2)','fourier_symbol':'2^(3/2)*Gamma(5/4-iw/2)*Gamma(5/4+iw/2)/Gamma(5/2)','beta_form':'2^(3/2)*Beta(5/4-iw/2,5/4+iw/2)','positivity_reason':'the numerator is |Gamma(5/4+iw/2)|^2; Gamma has no zeros and no poles in Re(z)>0','claim':'the log-scale Dirichlet kernel is strictly positive definite, so every nonzero finite coefficient packet has positive quadratic form','boundary':'the symbol approaches zero at high frequency, so strict positivity does not imply a uniform L2 lower bound or boundary-work conservation'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'real_gamma_argument':'5/4'}))
if __name__=='__main__':main()
