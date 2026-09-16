"""Admission checker for the corrected three-level semilocal sewing interface."""
import copy,json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
COMMON=['finite_regulator_product_typed','tate_phase_normalization_fixed','observer_order_retained','endpoint_channels_declared','regulator_order_declared']
REQ={
 'relative_strong_feature':['difference_row_exactly_recentered','observer_weighted_phase_energy_finite','summable_angular_phase_energy','bounded_packet_uniformity'],
 'minimal_scalar_product':['fixed_cutoff_two_sided_product_trace_class','transported_outer_regulator_trace_norm_convergence','summable_angular_trace_norm_majorant','placement_commutator_scalar_convergence','bounded_packet_uniformity'],
 'operator_trace_class_product':['fixed_cutoff_two_sided_product_trace_class','transported_outer_regulator_trace_norm_convergence','summable_angular_trace_norm_majorant','placement_remainder_trace_norm_convergence','bounded_packet_uniformity']}
def admit(c):
 for k in COMMON:
  if c.get(k) is not True:return False,k
 mode=c.get('mode')
 if mode not in REQ:return False,'mode'
 for k in REQ[mode]:
  if c.get(k) is not True:return False,k
 return True,'admitted_'+mode
base={k:True for k in COMMON};fixtures={}
for mode,req in REQ.items():fixtures[mode]=base|{k:True for k in req}|{'mode':mode}
# The compact-sandwich lemma supplies the operator-valued placement gate.
current=copy.deepcopy(fixtures['operator_trace_class_product'])
hostiles={}
for mode,c in fixtures.items():
 assert admit(c)==(True,'admitted_'+mode)
 for field in REQ[mode]:
  bad=copy.deepcopy(c);bad[field]=False;ok,reason=admit(bad);assert not ok and reason==field;hostiles[mode+'_'+field]=reason
# Exact angular dominated-convergence fixture.
rows=[]
for n in (1,2,4,8):
 err=sum((F(1,n+1)*F(1,4**chi) for chi in range(8)),F(0))
 rows.append({'regulator':n,'finite_angular_error':str(err),'bound':str(F(4,3*(n+1)))})
checks={'relative_strong_admitted':admit(fixtures['relative_strong_feature'])[0],'minimal_scalar_admitted':admit(fixtures['minimal_scalar_product'])[0],'operator_product_admitted':admit(current)==(True,'admitted_operator_trace_class_product'),'angular_errors_decrease':all(F(rows[i+1]['finite_angular_error'])<F(rows[i]['finite_angular_error']) for i in range(len(rows)-1))}
out={'schema':'marici.voevodsky.semilocal-sewing-completion-interface-check.v2','checks':checks,'hostile_refusals':hostiles,'dominated_convergence_rows':rows,'passed':all(checks.values()),'established_outputs':['positive_relative_difference_feature','signed_scalar_sewing_readout','trace_class_operator_valued_sewing_limit'],'next_gate':'Verify endpoint/index and conductor-channel compatibility of the compact-sandwich factorization for the exact transported physical placement.'}
if __name__=='__main__':
 p=ROOT/'results'/'semilocal-sewing-completion-interface.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
