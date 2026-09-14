#!/usr/bin/env python3
"""Audit C1: does the sourced BD current specialize to the primitive Cech chain?"""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
three=json.loads((R/'research/benincasa/three-cut-relative-chain-pairing-certificate.json').read_text())
param=json.loads((R/'research/benincasa/parameter-space-thimble-type-gate.json').read_text())
qprov=json.loads((R/'research/benincasa/q_physical_provenance_audit.json').read_text())
cech=json.loads((R/'research/voevodsky/results/BD_oriented_conductor_cech_chain.json').read_text())
cospan=json.loads((R/'research/voevodsky/results/conductor_cospan_boundary_map_gate.json').read_text())
# The source proves a local multiplicity-one Leray residue germ. C1 additionally
# needs its external-E Gauss-Manin specialization/intersection with the Cech
# vanishing chain. The admitted packets explicitly leave that arrow undefined.
checks={'literal_positive_chain_cut_incidence_zero':three['chain_boundary_cut_incidence']==[0,0,0],'analytic_continuation_germ_separate':three['classification']=='literal positive-chain pairing is zero; Cut residues belong to analytic continuation/nearby-cycle data','parameter_space_relative_current_absent':param['primary_source']['parameter_space_relative_current'] is None,'external_exceptional_image_absent':param['exceptional_gate']['exceptional_image'] is None,'physical_Q_variation_undefined':qprov['relative_chain']['Var_Q_Gamma_phys']=='undefined_from_frozen_source_data','geometric_Cech_chain_available':cech['primitive_half_boundary']==[1,-1,1,-1],'relative_pair_missing':cospan['checks']['relative_pair_missing'],'global_direction_required':cospan['checks']['global_direction_required']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.C1-physical-current-specialization-audit.v1','conjecture':'The continued BD residue current specializes with multiplicity one to the primitive conductor half-boundary (1,-1,1,-1).','established':{'local_Leray_boundary_value':'multiplicity one on each generic transverse q_G12 patch','geometric_vanishing_chain':cech['primitive_half_boundary'],'BD_orientation':'common phase combined with sign(g)','conditional_consequences':'unit e6 jump and parity (1,0)'},'missing_arrow':'Sp_E of the source-derived residue current Gamma_res_BD into the degree-one normalization/conductor chain complex','required_computation':['write Gamma_res_BD by explicit transported Cayley-Menger and signed-minor inequalities near E=0','resolve the four XY=E*s^2 points simultaneously','intersect the lifted current with the two oriented node bridges','compute the resulting integer coefficients and Smith index'],'status':'open','C1_confirmed':False,'C1_rejected':False,'effect_on_previous_physical_packets':'They are conditional prediction certificates. Their algebraic, cellular, Picard, and logarithmic tests remain valid under the multiplicity-one comparison hypothesis.','checks':checks,'passed':True}
(R/'research/voevodsky/results/C1_physical_current_specialization_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'audit_passed':True,'C1_status':out['status'],'missing_arrow':out['missing_arrow'],'effect':out['effect_on_previous_physical_packets']}))
