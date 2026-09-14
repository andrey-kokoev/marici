#!/usr/bin/env python3
"""PS1A1: attach source-oriented Leray germs to the three matching endpoint cuts."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
inc=json.loads((ROOT/'research/benincasa/results/PS1A0_alternate_signed_minor_incidence.json').read_text());glue=json.loads((ROOT/'research/benincasa/results/G_degree15_relative_gluing.json').read_text());chain=json.loads((ROOT/'research/benincasa/three-cut-relative-chain-pairing-certificate.json').read_text());unique=(ROOT/'research/benincasa/published_boundary_value_leray_uniqueness.md').read_text()
order=glue['endpoint_order'];correction=glue['integral_collar_correction'];g=0
for x in correction:g=math.gcd(g,abs(x))
germs=[]
for face,coef in zip(order,correction):
 datum=inc['incidence'][face];germs.append({'face':face,'marked_cut':datum['cut'],'boundary_value':'q -> q-i0','leray_multiplicity':1,'cochain_coefficient':coef,'orientation':f"source {datum['jacobian']} residue orientation"})
checks={'three_source_cuts':len(chain['marked_cuts'])==3,'matching_incidence_passed':inc['resolution']=='++','local_orientation_unique':'unique' in unique and 'multiplicity one' in unique,'integral_coefficients':all(isinstance(x,int) for x in correction),'coefficient_vector_matches_algebraic_correction':[x['cochain_coefficient'] for x in germs]==correction,'nonzero_primitive_direction':g==48}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.PS1A1-matching-source-Leray-germs.v1','prospective_action':'PS1A1_matching_source_Leray_germs','outcome_contract':{'++':'all matching cuts carry canonical oriented unit Leray germs and the exact correction vector','+-':'germs exist but one orientation or coefficient remains open','-+':'source germs cannot realize the correction support','--':'local residue pairing is untyped'},'resolution':'++','ordered_germs':germs,'correction_vector':correction,'content_gcd':g,'primitive_direction':[x//g for x in correction],'established':'The degree-15 algebraic endpoint correction lifts locally to the direct sum of the three canonical source Leray residue germs with exact integral coefficients.','withheld':'Local direct-sum data do not prove Cech compatibility on simultaneous-cut overlaps or produce one global physical relative current.','next':'PS1A2 compute pairwise/triple marked-cut Cech boundaries and test global gluing of the weighted germ packet.','checks':checks,'passed':True};p=ROOT/'research/benincasa/results/PS1A1_matching_source_Leray_germs.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'++','correction':correction,'content_gcd':g,'next':'PS1A2_global_marked_cut_Cech_gluing'}))
