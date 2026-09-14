#!/usr/bin/env python3
"""High-precision numerical scout of the p=2 Gaussian Stieltjes endpoint Gram."""
import argparse,json
from pathlib import Path
import mpmath as mp

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_p2_stieltjes_pauli_scout_20260908.json');args=p.parse_args();mp.mp.dps=60;L=mp.log(2);checks=0
 rho=lambda q:mp.e**(-mp.pi*q*q)
 H=lambda q:mp.erfc(mp.sqrt(mp.pi)*q)/2
 W=lambda t,q:H(q+t)-H(q-t)
 inner=lambda f,g:mp.quad(lambda q:f(q)*g(q)*rho(q),[-mp.inf,mp.inf])
 a=inner(lambda q:W(L,q),lambda q:W(L,q));b=inner(lambda q:W(2*L,q),lambda q:W(2*L,q));c=inner(lambda q:W(L,q),lambda q:W(2*L,q));d2=a+b-2*c
 assert a>0 and b>0 and a*b-c*c>0;checks+=1
 assert b>a and c>0 and d2>0;checks+=1
 h=L*(2**-.5)/(1-2**-.5);margin=4-h*h;assert 0<h<2 and margin>0;checks+=1
 out={'schema':'marici.rh.p2-stieltjes-pauli-scout.v1','status':'numerical_scout_passed','precision_digits':60,'p':2,'a':mp.nstr(a,30),'b':mp.nstr(b,30),'c':mp.nstr(c,30),'raw_determinant':mp.nstr(a*b-c*c,30),'difference_energy':mp.nstr(d2,30),'pauli_sum_diagonal':[mp.nstr(2*b,30),mp.nstr(2*a,30)],'all_grade_h':mp.nstr(h,30),'oriented_auxiliary_margin':mp.nstr(margin,30),'claim':'the actual p=2 Gaussian endpoint Gram is prime-dependent with nonzero real cross-correlation, while its Pauli sum is a positive diagonal pair','consequence':'the p=2 comparison must map diag(2b,2a) into the separately oriented auxiliary cell; it cannot use the constant 2I identification','boundary':'high-precision quadrature is a scout, not a directed-rounding certificate or proof of the quadratic representation'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'a':out['a'],'b':out['b'],'c':out['c']}))
if __name__=='__main__':main()
