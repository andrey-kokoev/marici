#!/usr/bin/env python3
"""Audit finite geometric cutoff transitions on their declared open-unit-disk chart."""
import argparse,json
from pathlib import Path
import sympy as s

def geom(q,n):return sum(q**k for k in range(n+1))
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_cutoff_transition_unit_hostile_certificate_20260908.json');a=p.parse_args();q=s.symbols('q');rows=[];checks=0
 for coarse,fine in ((2,3),(3,5),(5,10)):
  gc,gf=geom(q,coarse),geom(q,fine)
  # (1-q)g_n=1-q^(n+1).  For |q|<1 neither factor on the right can
  # vanish, so every g_n and every quotient g_f/g_c is a holomorphic unit.
  assert s.expand((1-q)*gc-(1-q**(coarse+1)))==0;checks+=1
  assert s.expand((1-q)*gf-(1-q**(fine+1)))==0;checks+=1
  ratio=s.cancel((gf/gc)**2);raw=gf**2/gc**2
  connection=s.cancel(s.diff(raw,q)/raw-2*s.diff(gf,q)/gf+2*s.diff(gc,q)/gc)
  assert connection==0;checks+=1
  num,den=map(lambda x:s.Poly(x,q),s.fraction(ratio))
  rows.append({'coarse':coarse,'fine':fine,'transition':str(ratio),'numerator_degree':num.degree(),'denominator_degree':den.degree(),'unit_domain':'|q|<1','unit_proof':'(1-q)g_n=1-q^(n+1); roots of g_n lie on |q|=1','log_connection_identity_residual':str(connection)})
 out={'schema':'marici.rh.cutoff-transition-unit-hostile.v2','status':'unit_on_declared_open_disk','checks':checks,'rows':rows,'correction':'nonconstant rational functions can be holomorphic nowhere-zero units on a restricted chart; polynomial units on the affine line were the wrong criterion','claim':'the tested finite cutoff carrier transitions are units on |q|<1','boundary':'does not prove boundary extension to |q|=1, convergence of the section, identification with Xi, or boundary-work conservation'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'pairs':[[x['coarse'],x['fine']] for x in rows]}))
if __name__=='__main__':main()
