#!/usr/bin/env python3
"""Explain sampled tangent-path rank drops by source degeneracy strata."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/aspect/results';receipts=[json.loads((R/f'rank26_xy_tangent_path_rank_flatness_p{p}.json').read_text()) for p in (32003,32009)];assert receipts[0]['runs']==receipts[1]['runs'];runs=receipts[0]['runs'];classified=[]
for run in runs:
 x,y,z=run['point'];collisions=[]
 if x==-2*z:collisions.append('g2=g31')
 if y==-2*z:collisions.append('g1=g23')
 coordinate_vanishing=[]
 if x==0:coordinate_vanishing.append('x=0')
 if y==0:coordinate_vanishing.append('y=0')
 expected=4275 if collisions else 4285 if coordinate_vanishing else 4289
 assert run['rank']==expected
 classified.append({'s':run['s'],'point':run['point'],'rank':run['rank'],'marked_divisor_collisions':collisions,'coordinate_vanishing':coordinate_vanishing,'stratum':'collision' if collisions else 'coordinate_vanishing' if coordinate_vanishing else 'sampled_generic'})
out={'schema':'marici.aspect.rank26-xy-tangent-path-rank-strata.v1','gamma_mode':'half','ambient':8,'primes':[32003,32009],'classified_runs':classified,'generic_sampled_rank':4289,'coordinate_vanishing_rank':4285,'marked_divisor_collision_rank':4275,'rank_drop_explained_on_sample':True,'swapped_audit_endpoints_lie_on_distinct_marked_divisor_collision_strata':True,'naive_transport_obstruction':'the proposed path leaves one collision stratum, crosses the generic stratum, and specializes to the swapped collision stratum','nearby_specialization_constructed':False,'same_point_normal_image_equality_derived':False,'passed':True};(R/'rank26_xy_tangent_path_rank_strata.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'passed','strata':3,'runs':len(runs)}))
