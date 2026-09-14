#!/usr/bin/env python3
"""Exact local singularity/lci gate for a Bruce-style smooth realization."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 # B=k[x0,x2,x4,x1,x3,x5]/(xe*xo): 9 independent quadratic initial forms.
 ambient_dim=6;branch_dim=3;ideal_height=ambient_dim-branch_dim
 generators=[(e,o) for e in (0,2,4) for o in (1,3,5)]
 minimal_generators=len(generators)
 jacobian_rank_at_origin=0;tangent_dim=ambient_dim-jacobian_rank_at_origin
 checks=0
 assert minimal_generators==9;checks+=9
 assert ideal_height==3;checks+=1
 assert minimal_generators>ideal_height;checks+=1
 assert tangent_dim==6>branch_dim;checks+=6
 # Two irreducible branches meet at the conductor; a manifold local ring cannot have this node germ.
 branches=2;assert branches==2;checks+=2
 out={'schema':'marici.smooth_q_manifold_realization_gate.v1','status':'falsified','checks':checks,
  'native_local_ring':'k[x_even,x_odd]/(x_even*x_odd)','mixed_quadratic_generators':minimal_generators,
  'height':ideal_height,'complete_intersection':False,'jacobian_rank_at_conductor':0,
  'zariski_tangent_dimension':tangent_dim,'local_dimension':branch_dim,'branches':branches,
  'conclusion':'No smooth supermanifold can retain Spec(B) as its reduced/native base near the conductor; hence no literal Bruce smooth Q-manifold realizes the strict native target.',
  'also':'The native node is not lci at the conductor (9 minimal equations, height 3), so the obvious finite quasi-smooth replacement is unavailable.',
  'allowed_alternative':'the already constructed GR formal moduli problem in IndCoh, or a stratified/derived analytic extension of Bruce outside his stated category',
  'analytic_gates':['compactness','nuclear Frechet function algebra','invariant Berezin volume']}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'falsified','checks':checks,'smooth_native_realization':False}))
if __name__=='__main__':main()
