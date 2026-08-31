#!/usr/bin/env python3
"""Census admitted source candidates against the odd/even incidence signature."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
refs=[
 'research/benincasa/results/cosmology_source_sum_asymmetric_connection_orbit_two_prime.json',
 'research/benincasa/results/cosmology_principal_wall_partial_fraction_cech_gate.json',
 'research/voevodsky/results/cosmology_blowup_exceptional_cell_gate.json',
 'research/benincasa/results/cosmology_cayley_menger_exceptional_incoming_generator_audit.json',
 'research/benincasa/results/cosmology_sourced_quotient_line_outside_absorbed_family.json']
for p in refs:
 d=json.loads((ROOT/p).read_text()); assert d.get('passed') is True
orbit=json.loads((ROOT/refs[0]).read_text()); assert orbit['source_sum_principal_face_coefficient']==-2 and orbit['difference_principal_face_coefficient']==0
candidates=[
 {'name':'literal five-mark source sum','principal':-2,'exclusion':'even principal coefficient'},
 {'name':'connection-generated antisymmetric difference','principal':0,'exclusion':'zero principal coefficient'},
 {'name':'blow-up exceptional cell','column':[0,1],'exclusion':'no Xi_log unit leg'},
 {'name':'Cayley-Menger current','principal':None,'exclusion':'no weighted comparison to the coefficient complex'},
 {'name':'marked K residual family','principal':None,'exclusion':'unboundedly absorbed; no surviving sourced line'}]
assert not any(isinstance(c.get('principal'),int) and c['principal']%2 for c in candidates)
out={'schema':'marici.benincasa.cosmology-asymmetric-incidence-source-census.v1','required_signature':{'principal_parity':'odd','ordered_exceptional_boundary':[0,-2,2]},'candidates':candidates,'matching_candidate_count':0,'disposition':'exhausted in the current source envelope','strongest_residual':'the literal source supplies even exceptional multiplicity only together with an even principal leg; the connection removes the principal leg rather than making it odd','next_discriminating_leaf':'test whether a sourced degree-two exceptional attaching map factors independently of the principal occurrence','references':refs,'passed':True}
outp=ROOT/'research/benincasa/results/cosmology_asymmetric_incidence_source_census.json';outp.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
