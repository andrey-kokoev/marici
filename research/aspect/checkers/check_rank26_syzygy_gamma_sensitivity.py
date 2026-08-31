#!/usr/bin/env python3
"""Separate gamma-dependent image rank from gamma-robust normal/tangent equality."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results';A=ROOT/'research/aspect/results'
def main():
 runs=[]
 for d in (8,10,12,14):
  for p in (32003,32009):
   integer=json.loads((N/f'cosmology_p_normal_rank26_syzygy_bockstein_a{d}_p{p}.json').read_text());half=json.loads((N/f'cosmology_p_normal_rank26_syzygy_bockstein_half_a{d}_p{p}.json').read_text())
   ir=integer['directions']['nx']['bockstein_image_rank'];hr=half['directions']['nx']['bockstein_image_rank'];assert integer['combined_image_ranks']['all']==ir and half['combined_image_ranks']['all']==hr;assert integer['normal_images_equal'] and half['normal_images_equal'];assert integer['tangent_image_contained_in_normal_image'] and half['tangent_image_contained_in_normal_image']
   runs.append({'ambient':d,'prime':p,'integer_gamma_rank':ir,'half_gamma_rank':hr,'rank_delta':hr-ir,'normal_tangent_equality_both_modes':True})
 deltas=sorted({r['rank_delta'] for r in runs});out={'schema':'marici.aspect.rank26-syzygy-gamma-sensitivity.v1','runs':runs,'rank_deltas_observed':deltas,'image_rank_gamma_invariant':all(r['rank_delta']==0 for r in runs),'normal_tangent_equality_gamma_robust_on_tested_modes':True,'consequence':'rank-growth extrapolation is normalization-sensitive; zero intrinsic normal quotient is the robust observation','degree16_rank19_prediction_universal':False,'tau_p_map_constructed':False,'passed':True};A.mkdir(exist_ok=True);(A/'rank26_syzygy_gamma_sensitivity.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','rank_deltas':deltas,'rank_invariant':out['image_rank_gamma_invariant']}))
if __name__=='__main__':main()
