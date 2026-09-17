#!/usr/bin/env python3
"""Fail-closed audit of the proposed eight-step uniform Weil proof."""
import json
from pathlib import Path
root=Path(__file__).parents[1];res=root/'results'
def passed(name):
 p=res/name
 if not p.exists():return False
 return bool(json.loads(p.read_text()).get('passed',False))
steps={
 '1_smooth_logarithmic_IMS':{'theorem_written':(root/'smooth-logarithmic-ims-estimate-from-the-digamma-levy-representation.md').exists(),'numerical_constant_check':passed('logarithmic_ims_constants.json'),'closed':True},
 '2_rescaled_edge_model':{'model_written':(root/'rescaled-universal-edge-model-is-endpoint-minus-prime-hankel-discrepancy.md').exists(),'arithmetic_discrepancy_bound_deferred_to_step6':False,'closed':True},
 '3_edge_bulk_schur':{'theorem_written':(root/'edge-bulk-schur-absorption-after-finite-codefect-extraction.md').exists(),'L075_application_unconditional':passed('L075_edge_bulk_schur_application.json'),'closed':True},
 '4_uniform_normalized_complement':{'theorem_written':(root/'uniform-normalized-complement-gap-by-compact-codefect-extraction.md').exists(),'L075_check':passed('L075_uniform_complement_gap.json'),'closed':True},
 '5_interval_chebyshev_continuation':{'pilot_passed':passed('chebyshev_dangerous_block_L055_L065.json'),'directed_adaptive_slabs_complete':False,'closed':False},
 '6_asymptotic_threshold_N0':{'conditional_theorem_written':(root/'asymptotic-threshold-theorem-reduces-to-a-weighted-hankel-discrepancy-bound.md').exists(),'explicit_unconditional_N0':False,'closed':False},
 '7_finite_threshold_certificates':{'L055_unconditional':False,'L075_unconditional':passed('L075_edge_bulk_schur_application.json'),'all_below_N0':False,'closed':False},
 '8_form_core_passage':{'theorem_written':(root/'global-weil-positivity-follows-from-the-fixed-support-family-without-an-arithmetic-limit.md').exists(),'all_L_premise':False,'source_identity_audited':False,'closed':True}}
complete=all(x['closed'] for x in steps.values()) and steps['8_form_core_passage']['all_L_premise'] and steps['8_form_core_passage']['source_identity_audited'];out={'schema':'marici.voevodsky.uniform-weil-proof-gate-audit.v1','steps':steps,'global_weil_positivity_established':complete,'rh_proved':False,'passed':False};p=res/'uniform_weil_proof_gate_audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
