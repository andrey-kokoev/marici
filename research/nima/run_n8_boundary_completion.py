#!/usr/bin/env python3
"""Reproduce or quickly validate the complete n=8 boundary programme."""
from pathlib import Path
import argparse,json,subprocess,sys,time
R=Path(__file__).resolve().parents[2];C=R/'research/nima/checkers';D=R/'research/nima/results'
STEPS=[
 ('coordinate_bruhat_coverage','check_n8_coordinate_to_bruhat_boundary_coverage.py','n8-coordinate-to-bruhat-boundary-coverage.json'),
 ('positive_bridge_chains','search_n8_positive_bridge_chains.py','n8-positive-bridge-chain-search.json'),
 ('cyclic_bridge_chains','search_n8_cyclic_positive_bridge_chains.py','n8-cyclic-positive-bridge-chain-search.json'),
 ('symbolic_bridge_charts','check_n8_symbolic_positive_bridge_charts.py','n8-symbolic-positive-bridge-charts.json'),
 ('complete_bridge_atlas','check_n8_complete_cyclic_bcfw_bridge_atlas.py','n8-complete-cyclic-bcfw-bridge-atlas.json'),
 ('polygon_auxiliary_atlas','check_n8_rank2_cyclic_positive_atlas.py','n8-rank2-cyclic-positive-atlas.json'),
 ('hidden_bridge_transitions','check_n8_hidden_bcfw_bridge_transitions.py','n8-hidden-bcfw-bridge-transitions.json'),
 ('polygon_seed_anchors','check_n8_polygon_chart_orientation_anchors.py','n8-polygon-chart-orientation-anchors.json'),
 ('bridge_seed_anchors','check_n8_bcfw_bridge_orientation_anchors.py','n8-bcfw-bridge-orientation-anchors.json'),
 ('oriented_chain','check_n8_complete_oriented_boundary_chain.py','n8-complete-oriented-boundary-chain.json'),
 ('nonphysical_cancellation','check_n8_nonphysical_bcfw_transported_cancellation.py','n8-nonphysical-bcfw-transported-cancellation.json'),
 ('complete_external_pushforward','check_n8_complete_external_pushforward.py','n8-complete-external-pushforward.json'),
 ('second_positive_Z','check_n8_external_pushforward_second_positive_Z.py','n8-external-pushforward-second-positive-Z.json'),
 ('contracted_facets','check_n8_contracted_external_facets.py','n8-contracted-external-facets.json'),
 ('physical_bridge_representatives','prepare_n8_physical_bcfw_residue_representatives.py','n8-physical-bcfw-residue-representatives.json'),
 ('physical_bridge_orientations','check_n8_physical_bcfw_residue_orientations.py','n8-physical-bcfw-residue-orientations.json'),
 ('physical_bridge_polygon_equivalence','check_n8_physical_bcfw_to_polygon_residue_transitions.py','n8-physical-bcfw-to-polygon-residue-transitions.json'),
 ('physical_inverse_fibers','check_n8_physical_facet_inverse_fibers.py','n8-physical-facet-inverse-fibers.json'),
 ('history2_saturation','check_n8_history2_inverse_fiber_saturation.py','n8-history2-inverse-fiber-saturation.json'),
 ('physical_completion','check_n8_physical_boundary_canonical_form_completion.py','n8-physical-boundary-canonical-form-completion.json'),
 ('final_manifest','check_n8_boundary_programme_manifest.py','n8-boundary-programme-manifest.json')]
parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true',help='rerun all checkers; default validates materialized artifacts');args=parser.parse_args();rows=[]
for name,script,result in STEPS:
 t=time.time();status='passed';detail='artifact'
 if args.full:
  try:
   q=subprocess.run(['uv','run','--with','sympy','python',str(C/script)],cwd=R,text=True,capture_output=True,timeout=120)
   status='passed' if q.returncode==0 else 'failed';detail=(q.stdout+q.stderr)[-2000:]
  except subprocess.TimeoutExpired:status='timeout';detail='exceeded 120 seconds'
 else:
  p=D/result
  if not p.exists():status='missing';detail=str(p.relative_to(R))
  else:
   try:
    x=json.loads(p.read_text());status='passed' if x.get('passed') is True else 'failed';detail=x.get('schema','no schema')
   except Exception as e:status='invalid';detail=str(e)
 rows.append({'step':name,'checker':script,'result':result,'status':status,'seconds':round(time.time()-t,3),'detail':detail});print(name,status,flush=True)
passed=all(x['status']=='passed' for x in rows);out={'schema':'marici.nima.n8-boundary-reproduction-run.v1','mode':'full' if args.full else 'artifact-validation','per_process_timeout_seconds':120,'excluded_negative_scouts':['scout_n8_affine_cover_bridge_atlas_failure.py','scout_n8_colored_bridge_reconstruction.py'],'steps':rows,'passed':passed};p=D/'n8-boundary-reproduction-run.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'mode':out['mode'],'step_count':len(rows),'passed':passed,'failures':[x for x in rows if x['status']!='passed']},indent=2));raise SystemExit(0 if passed else 1)
