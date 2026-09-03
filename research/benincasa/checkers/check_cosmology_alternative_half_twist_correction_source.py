#!/usr/bin/env python3
"""Test the proposed antisymmetric half-twist candidate pair against labelled reflection."""
import json
from pathlib import Path
P=Path(__file__).resolve();ROOT=P.parents[3];R=ROOT/'research'/'benincasa'/'results'
s=json.loads((R/'cosmology_half_twist_syzygy_provenance_summary.json').read_text());labels=s['pivot_labels'];families=s['source_families'];pairs=[]
for i,label in enumerate(labels):
 reflected=[*label[:-1],[label[-1][1],label[-1][0]]]
 matches=[j for j,x in enumerate(labels) if x==reflected]
 if matches:pairs.append({'candidate':i,'reflected_label':reflected,'matches':matches})
proposed={'candidates':[2,4],'source_families':[families[2],families[4]],'family_support_reflection_compatible':set(families[2])=={'IBP','K','g1','g3','g23'} and set(families[4])=={'IBP','K','g2','g3','g31'},'pivot_labels':[labels[2],labels[4]],'label_reflection_compatible':labels[4]==[*labels[2][:-1],[labels[2][-1][1],labels[2][-1][0]]]}
assert proposed['family_support_reflection_compatible'];assert not proposed['label_reflection_compatible'];assert not pairs
out={'schema':'marici.benincasa.cosmology-alternative-half-twist-correction-source.v1','required_vertex_correction':[0,-2,2],'candidate_2_minus_4_test':proposed,'exact_reflection_pairs_among_eight':pairs,'decision':'Candidates 2 and 4 have reflected source-family support but are not reflected labelled pivots: (1,7) reflects to (7,1), not (0,8). None of the eight pivots has its reflected label in the candidate set, so source-family symmetry alone cannot authorize an antisymmetric correction.','surviving_route':'test the oriented D2-D3 weighted Gysin principal trace through an explicit face-to-vertex incidence map','limitations':['label reflection uses the declared two-variable monomial swap','does not exclude linear combinations involving non-pivot source rows'],'passed':True};(R/'cosmology_alternative_half_twist_correction_source.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
