#!/usr/bin/env python3
"""Finite-jet audit: multiplier-linear maps preserve Xi divisibility; derivatives need not."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_xi_ideal_preservation_gate_certificate_20260908.json');a=p.parse_args()
 t=s.symbols('t');checks=0
 for m in range(1,9):
  coeff=s.symbols('a0:'+str(9-m));f=sum(coeff[j]*t**j for j in range(len(coeff)));tau=t**m
  h=s.symbols('h0:'+str(9-m));mulp=sum(h[j]*t**j for j in range(len(h)))
  r=s.expand(tau*f*mulp)
  assert all(s.expand(r).coeff(t,j)==0 for j in range(m));checks+=1
  dr=s.diff(tau*f,t)
  if m>=1:
   assert s.expand(dr).coeff(t,m-1)==m*coeff[0];checks+=1
 out={'schema':'marici.rh.xi-ideal-preservation-gate.v1','status':'filtration_preservation_identified','checks':checks,'jet_orders_tested':[1,8],
 'positive':'multiplication/B-module maps on an ambient source module send tau*f to tau*h and preserve every local multiplicity jet',
 'hostile':'parameter differentiation sends t^m f to m f(0)t^(m-1)+..., lowering divisor order',
 'required_bridge':'identify the Evans source section with the Mellin Xi ideal and prove the complete five-port residual comparison preserves the Xi-adic filtration',
 'consequence':'scalar source-ideal equality alone cannot imply residual divisibility; the comparison must be multiplier-linear or carry an explicit filtration-preserving homotopy'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks}))
if __name__=='__main__':main()
