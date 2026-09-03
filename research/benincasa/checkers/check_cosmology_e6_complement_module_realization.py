#!/usr/bin/env python3
"""Test the primitive complement on the established A2-to-e6 relational grade."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
fac=json.loads((R/'cosmology_complement_incidence_factorization_gate.json').read_text());e6=json.loads((R/'clifford_e6_cyclic_equivariance.json').read_text());gate=json.loads((R/'cosmology_e6_rank12_triangular_transport_gate.json').read_text());census=json.loads((R/'cosmology_rank12_shear_artifact_census.json').read_text())
assert fac['passed'] and gate['passed'] and census['passed']
C=((0,0,1),(1,0,0),(0,1,0));I=tuple(tuple(x for x in r) for r in e6['realization']);P=tuple(tuple(x for x in r) for r in e6['cyclic_permutation'])
assert I==((1,0,0),(0,1,0),(0,0,1)) and P==C
roots=[tuple(v) for v in e6['source_bivector_orbit']]
def mv(M,v):return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))
assert all(sum(v)==0 and math.gcd(*map(abs,v))==1 for v in roots)
assert mv(C,roots[2])==roots[0]
out={'schema':'marici.benincasa.cosmology-e6-complement-module-realization.v2','correction_of_v1':'common weight -2 is a homogeneity grade, not scalar multiplication by -2','required_complement_C':[list(r) for r in C],'established_A2_realization':[list(r) for r in I],'established_cyclic_transport':[list(r) for r in P],'C_equals_established_cyclic_transport':True,'source_A2_roots_primitive':True,'associated_grade_complement_realized_primitively':True,'integral_division_by_two_required':False,'remaining_blockers':['literal five-mark complex lacks the full q_g12 edge object','associated A2 grade does not determine off-diagonal extension shear','no full rank-twelve connection or connector naturality components'],'full_module_level_C_realized':False,'conclusion':'the complement is already primitive on the A2 occurrence-difference grade; only its lift to the full source and rank-twelve extension remains','passed':True};(R/'cosmology_e6_complement_module_realization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
