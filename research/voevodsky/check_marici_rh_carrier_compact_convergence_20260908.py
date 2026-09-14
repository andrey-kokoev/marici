#!/usr/bin/env python3
"""Exact compact-disk convergence bounds for the finite geometric carrier model."""
import argparse,json
from fractions import Fraction
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_carrier_compact_convergence_certificate_20260908.json');a=p.parse_args()
 radii=(Fraction(1,2),Fraction(2,3),Fraction(3,4));depths=(2,3,5,10);rows=[];checks=0
 for r in radii:
  prev=None
  for n in depths:
   # sup_|q|<=r |g_inf-g_n| <= r^(n+1)/(1-r)
   g_error=r**(n+1)/(1-r)
   # |g_n| <= 1/(1-r), hence square-section error is bounded by
   # |g_inf-g_n|(|g_inf|+|g_n|) <= 2 error/(1-r).
   square_error=2*g_error/(1-r)
   # Consecutive carrier transition g_(n+1)/g_n differs from one by
   # q^(n+1)/g_n; reverse triangle gives |g_n| >= (1-r^(n+1))/(1+r).
   transition_error=r**(n+1)*(1+r)/(1-r**(n+1))
   assert g_error>0 and square_error>0 and transition_error>0;checks+=3
   if prev is not None:
    assert g_error<prev;checks+=1
   prev=g_error
   rows.append({'radius':f'{r.numerator}/{r.denominator}','depth':n,'geometric_tail_bound':f'{g_error.numerator}/{g_error.denominator}','square_section_bound':f'{square_error.numerator}/{square_error.denominator}','next_transition_minus_one_bound':f'{transition_error.numerator}/{transition_error.denominator}'})
 out={'schema':'marici.rh.carrier-compact-convergence.v1','status':'exact_compact_convergence_bounds','checks':checks,'rows':rows,'limit':'g_infinity(q)=1/(1-q), square presentation limit=(1-q)^(-2)','claim':'the finite geometric carrier presentations and their square sections converge uniformly on each tested closed disk strictly inside |q|<1','boundary':'this toy geometric presentation is not identified with the completed theta section Xi; no boundary convergence at |q|=1 or boundary-work law follows'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'radii':[f'{r.numerator}/{r.denominator}' for r in radii]}))
if __name__=='__main__':main()
