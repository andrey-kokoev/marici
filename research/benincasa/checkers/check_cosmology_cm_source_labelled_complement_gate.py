#!/usr/bin/env python3
"""Gate source-labelling of the three-dimensional complement in CM cohomology."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
t=json.loads((R/'cm-normal-tower-rank.json').read_text());src=(B/'marici-gm/src/bin/cm_normal_tower_rank.rs').read_text()
assert t['checks']['all_cm_cohomology_rank_7'] and t['checks']['all_labelled_tower_rank_4']
assert 'fn standard_monomials' in src and 'let rank = standard_monomial_count(&basis);' in src
assert 'STANDARD_MONOMIALS=' not in src
runs=t['runs'];assert all(r['labels'][:4]==['nu1','nu2','nu3','nu1^2'] for r in runs)
out={'schema':'marici.benincasa.cosmology-cm-source-labelled-complement-gate.v1','rank_decomposition':{'CM_quotient':7,'normal_tower_image':4,'complement':3},'backend_capability':{'computes_standard_monomial_set_internally':True,'returns_only_standard_monomial_count':True,'serializes_standard_monomials':False},'source_label_status':{'normal_rank4':['nu1','nu2','nu3','nu1^2'],'complement_rank3':None},'transport_status':{'cross_point_source_labels':False,'cross_prime_source_labels':False},'nonpromotion':'standard monomials would be Groebner presentation coordinates even if serialized; a separate source map is required to label the complement','disposition':'no source-labelled complement exists in the current backend or receipts','next_route':'return to the independent weighted relative homology-de Rham pairing route; CM presentation coordinates cannot supply source authority','passed':True};(R/'cosmology_cm_source_labelled_complement_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
