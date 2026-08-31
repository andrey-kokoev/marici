#!/usr/bin/env python3
"""Audit the basis interface required for full CM 7x7 connection matrices."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
t=json.loads((R/'cm-normal-tower-rank.json').read_text());h=json.loads((R/'cm-cyclic-transverse-horizontality.json').read_text())
assert t['status']==h['status']=='pass'
assert t['checks']['all_cm_cohomology_rank_7'] and t['checks']['all_labelled_tower_rank_4']
missing=7-4;assert missing==3
assert all(r['labels'][:4]==['nu1','nu2','nu3','nu1^2'] for r in t['runs'])
out={'schema':'marici.benincasa.cosmology-cm-full-matrix-basis-interface-gate.v1','ambient_CM_quotient_rank':7,'source_labelled_normal_tower_rank':4,'labelled_basis':['nu1','nu2','nu3','nu1^2'],'unlabelled_complement_dimension':missing,'available_relations':'six kernels among ten normal-tower labels at each tested presentation','full_source_labelled_basis_constructed':False,'connection_matrix_shape_required':[3,7,7],'typed_coefficient_functions_required':147,'current_derivative_result':'derivatives of the cyclic port reduce only inside the labelled rank-four image','obstruction':'row reduction can choose three complementary quotient pivots, but no receipt identifies them as source classes or matches them across points and primes','minimal_next_interface':['serialize the seven standard quotient monomials with provenance','identify the rank-four normal subspace embedding','source-label a three-dimensional complement','differentiate and reduce every basis element in three directions','prove cross-point and cross-prime basis transport'],'passed':True};(R/'cosmology_cm_full_matrix_basis_interface_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
