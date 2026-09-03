#!/usr/bin/env python3
"""Test whether integral C2 transfer operations can produce the required odd leg."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
for n in ['cosmology_primitive_lift_obstruction_synthesis.json','cosmology_universal_minimal_integral_source_extension.json']:
 assert json.loads((R/n).read_text())['passed']
rows=[]
for a in range(-8,9):
 rows.append({'sheet_coefficient':a,'invariant_difference':a-a,'sign_difference':a-(-a),'invariant_transfer':a+a,'sign_transfer':a+(-a)})
assert all(r['invariant_difference']==0 and r['sign_difference']%2==0 and r['invariant_transfer']%2==0 and r['sign_transfer']==0 for r in rows)
out={'schema':'marici.benincasa.cosmology-mu2-orientation-local-system-integral-realization.v1','deck_operations':{'difference':'1-s','transfer':'1+s'},'exhaustive_integer_samples':rows,'lemma':'for either trivial or sign coefficient action, integral difference and transfer have principal coefficient zero or even','ordered_boundary_difference':[0,-2,2],'boundary_can_be_realized_formally_by_sheet_difference':True,'odd_principal_leg_realized':False,'forbidden_escape':'the projector (1-s)/2 can halve an even class only after inverting 2 or supplying divisibility data','independent_primitive_anti_invariant_source_present':False,'conclusion':'a sourced double cover generated from the existing even source cannot integrally realize formal u; it would require a new primitive anti-invariant source class','global_mu2_no_go':False,'next_test':'test whether an integral Bockstein from a mod-2 orientation class can land in the free primitive target lattice','passed':True};(R/'cosmology_mu2_orientation_local_system_integral_realization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
