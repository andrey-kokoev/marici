#!/usr/bin/env python3
"""Resolve whether common homogeneity -2 imposes integral divisibility."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
e6=json.loads((R/'clifford_e6_cyclic_equivariance.json').read_text());corr=json.loads((R/'cosmology_e6_complement_module_realization.json').read_text())
assert corr['passed'] and corr['associated_grade_complement_realized_primitively']
assert e6['source_homogeneity']==e6['target_homogeneity']==-2 and e6['realization']==[[1,0,0],[0,1,0],[0,0,1]]
roots=e6['source_bivector_orbit'];assert all(math.gcd(*map(abs,r))==1 for r in roots)
out={'schema':'marici.benincasa.cosmology-e6-common-weight-divisibility-gate.v1','common_weight':-2,'weight_type':'homogeneity grade','map_scalar':1,'realization_matrix':e6['realization'],'source_roots_primitive':True,'source_labelled_halves_required':False,'divisibility_obstruction_present':False,'corrected_error':'the prior -2C interpretation conflated grading with scalar multiplication','positive_result':'the required complement C is established cyclic transport on the primitive A2 occurrence-difference grade','promotion_limit':'associated-grade realization does not supply the literal q_g12 source object or full rank-twelve extension','next_test':'lift the primitive A2 complement through the rank-twelve extension and test the two shear classes against connector naturality','passed':True};(R/'cosmology_e6_common_weight_divisibility_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
