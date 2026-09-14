#!/usr/bin/env python3
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];P=ROOT/'research/aspect/contracts/theta-rh-interaction-net-state.v3.json'
def check(c):
 v=c.get('versioning',{});i=c.get('interface',{});s=c.get('sewing',{});m=c.get('real_metric_typing',{});l=c.get('loading',{});by={x.get('id'):x for x in c.get('constructors',[])}
 required_rejections={'drop_seam_flux_without_proved_quotient','primitive_current_as_fixed_green_hilbert_vector','connected_tail_as_boundary_current','oriented_cocycle_as_mellin_character_only','loading_selected_by_convergence','bounded_inverse_from_algebraic_or_pro_faithfulness','determinant_compiler_folded_into_interface','quarter_turn_identified_with_radial_swap','bare_conjugation_preserves_arbitrary_phase_wall','graph_adjoint_identified_with_ambient_adjoint'}
 checks={
 'versioned_successor':v.get('relation')=='refines_without_rewriting' and v.get('predecessor','').endswith('.v2.json'),
 'radial_amendment_named':v.get('radial_amendment','').endswith('theta-rh-g4-radial-interface.v1.json'),
 'four_ports_no_quotient':i.get('boundary_trace')==['P','Q','M','J'] and i.get('seam_flux_retained') and not i.get('undeclared_quotient'),
 'function_valued_response':i.get('response')==['K','H_K','compatible_J_K_family'] and i.get('oriented_laplace_cocycle_required'),
 'quarter_half_turn_separated':s.get('source_half_turn')=='R=F^2' and s.get('quarter_turn_equals_radial_swap') is False,
 'phase_is_gauge':s.get('phase_is_isolated_interface_invariant') is False,
 'twisted_real_structure':s and m.get('radial_real_structure')=='J_u=diag(1,u^2)K',
 'metrics_separated':m.get('cross_metric_equality_forbidden') and 'G_D^-1' in m.get('ambient_adjoint',''),
 'loading_constructed_internally':l.get('internal_arrow_constructed') is True and 'c_p=' in l.get('coefficient',''),
 'owner_readback_open':l.get('g4_owner_readback_constructed') is False and by.get('g4_radial_carrier_and_loading_readback',{}).get('status')=='open' and by.get('g4_half_turn_sewing_readback',{}).get('status')=='open',
 'downstream_open':by.get('downstream_evans_green_rh_chain',{}).get('status')=='open',
 'rejection_basis_complete':set(c.get('rejections',[]))==required_rejections,
 'rh_not_promoted':c.get('rh_implication') is False}
 return checks
c=json.loads(P.read_text());checks=check(c)
# Ten hostile mutations must each break at least one named invariant.
mut=[]
def hostile(fn):x=copy.deepcopy(c);fn(x);mut.append(not all(check(x).values()))
hostile(lambda x:x['interface'].__setitem__('boundary_trace',['P','Q','M']))
hostile(lambda x:x['interface'].__setitem__('response',['H_K']))
hostile(lambda x:x['sewing'].__setitem__('quarter_turn_equals_radial_swap',True))
hostile(lambda x:x['sewing'].__setitem__('phase_is_isolated_interface_invariant',True))
hostile(lambda x:x['real_metric_typing'].__setitem__('radial_real_structure','K'))
hostile(lambda x:x['real_metric_typing'].__setitem__('cross_metric_equality_forbidden',False))
hostile(lambda x:x['loading'].__setitem__('internal_arrow_constructed',False))
hostile(lambda x:x['loading'].__setitem__('g4_owner_readback_constructed',True))
hostile(lambda x:[n.__setitem__('status','constructed') for n in x['constructors'] if n['id']=='downstream_evans_green_rh_chain'])
hostile(lambda x:x.__setitem__('rh_implication',True))
checks['ten_hostiles_rejected']=all(mut) and len(mut)==10
out={'schema':'marici.aspect.theta-rh-g4-v3-successor-check.v1','passed':all(checks.values()),'checks':checks,'constructed_internal_cells':12,'open_owner_readbacks':['g4_radial_carrier_and_loading_readback','g4_half_turn_sewing_readback'],'downstream_open':True,'rh_implication':False}
R=ROOT/'research/aspect/results/theta_rh_g4_v3_successor.json';R.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
