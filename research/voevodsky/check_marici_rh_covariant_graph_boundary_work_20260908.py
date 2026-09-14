#!/usr/bin/env python3
"""Exact boundary-work identity from the two half-density covariant graph legs."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_covariant_graph_boundary_work_certificate_20260908.json');args=p.parse_args();u=s.symbols('u',real=True);h=s.Function('h')(u);checks=0
 Dminus=s.diff(h,u)-h/2;Dplus=s.diff(h,u)+h/2
 difference=s.expand(Dminus**2-Dplus**2)
 assert s.simplify(difference+s.diff(h*h,u))==0;checks+=1
 # Polarized bilinear version, needed before imposing a real/Hermitian slice.
 f=s.Function('f')(u);g=s.Function('g')(u)
 polarized=s.expand((s.diff(f,u)-f/2)*(s.diff(g,u)-g/2)-(s.diff(f,u)+f/2)*(s.diff(g,u)+g/2))
 assert s.simplify(polarized+s.diff(f*g,u))==0;checks+=1
 # Concrete theta half-density verifies the identity without abstract functions.
 hu=s.exp(u/2)*s.exp(-s.pi*s.exp(2*u));concrete=s.simplify((s.diff(hu,u)-hu/2)**2-(s.diff(hu,u)+hu/2)**2+s.diff(hu**2,u))
 assert concrete==0;checks+=1
 out={'schema':'marici.rh.covariant-graph-boundary-work.v1','status':'oriented_boundary_identity_exact','checks':checks,'identity':'|D_- h|^2-|D_+ h|^2=-d_u(h^2) on the real slice','polarized_identity':'D_-f D_-g-D_+f D_+g=-d_u(fg)','interval_form':'integral[q0,q1](|D_-h|^2-|D_+h|^2)du=h(q0)^2-h(q1)^2','claim':'the oriented difference of the two reciprocal covariant graph energies is exactly endpoint boundary work','consequence':'the same half-density construction supplies both a positive symmetric bulk sum and an oriented boundary difference','boundary':'the complex Hermitian extension, two-sheet theta source domain, and equality with the previously normalized D_bw convention remain to be checked'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'identity':'D_-^2-D_+^2=-d(h^2)'}))
if __name__=='__main__':main()
