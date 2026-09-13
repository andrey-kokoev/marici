#!/usr/bin/env python3
"""Structural audit of the expanded Green/Pfaffian constructor alphabet."""
import json
from pathlib import Path
p=Path(__file__).with_name('boundary-pfaffian-constructor-alphabet.v2.json');d=json.loads(p.read_text())
ids=[x['id'] for x in d['constructors']];assert len(ids)==len(set(ids))
required={'refine_seam','massive_apply','green_resolve','endpoint_moments','include_contexts','project_contexts','green_determinant_transition','paired_pfaffian_correspondence','paired_pfaffian_transition'}
assert required<=set(ids)
cofiber=next(x for x in d['constructors'] if x['id']=='refine_seam')['cofiber'];assert 'value_jump_line_odd' in cofiber and 'flux_jump_line_even' in cofiber
forbidden=set(d['forbidden_collapses']);assert 'identify_green_determinant_line_with_pfaffian_line' in forbidden
rids={x['id'] for x in d['relations']};assert {'massive_green_factorization','ind_pro_triangle','determinant_cocycle','paired_pfaffian_correspondence','paired_pfaffian_transition','moment_kernel_stability'}<=rids
for relation in d['relations']:
 assert 'evidence' in relation and (p.parent/relation['evidence']).exists(), relation['id']
 if 'formal_evidence' in relation: assert (p.parent/relation['formal_evidence']).exists(), relation['id']
 if 'coefficient_obstruction_evidence' in relation: assert (p.parent/relation['coefficient_obstruction_evidence']).exists(), relation['id']
 if 'obstruction_evidence' in relation: assert (p.parent/relation['obstruction_evidence']).exists(), relation['id']
regimes=set(d['coefficient_regimes'])
for constructor in d['constructors']:
 if 'coefficient_regime' in constructor: assert constructor['coefficient_regime'] in regimes
assert next(x for x in d['constructors'] if x['id']=='green_resolve')['coefficient_regime']=='green_normalized'
assert next(x for x in d['constructors'] if x['id']=='paired_pfaffian_correspondence')['coefficient_regime']=='ring_generic'
assert next(x for x in d['constructors'] if x['id']=='paired_pfaffian_transition')['coefficient_regime']=='localized_selected_gaps'
out={'schema':'marici.coherence.boundary-pfaffian-constructor-alphabet-v2-check.v1','constructors':len(ids),'relations':len(rids),'protocols':len(d['protocols']),'coefficient_regimes':len(regimes),'two_seam_channels':True,'green_pfaffian_lines_distinct':True,'all_required_relations_present':True,'all_relations_have_existing_evidence':True,'coefficient_requirements_typed':True}
Path(__file__).with_name('boundary-pfaffian-constructor-alphabet-v2-check.v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
