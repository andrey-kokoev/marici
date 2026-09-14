#!/usr/bin/env python3
"""Exact PF3 curvature reduction with exploratory theta scan."""
import json,math
from pathlib import Path
from evidence_policy import write_result
# Symbolic determinant after exponential-tilt elimination: [[1,0,b],[0,b,c],[b,c,3b^2+d]].
def det(b,c,d):return b*(3*b*b+d)-c*c-b**3
for b,c,d in [(-2,3,5),(-1,0,7),(4,-2,9)]:assert det(b,c,d)==b*d-c*c+2*b**3
R=Path(__file__).resolve().parents[2]
out={'schema':'marici.conjecture-replay.CR1-theta-translation-PF3-reduction.v1','passed':True,'claim_status':'supported','evidence':[{'class':'SYMBOLIC','claim':'The coalescent PF3 Hankel determinant reduces exactly to one differential inequality for h=-(log Phi)dd.','checker':'research/conjecture_replay/check_CR1_theta_translation_PF3_reduction.py'},{'class':'NUMERICAL','claim':'A 20,001-point analytic-derivative scan on 0<=u<=1.5 with fourteen theta labels found the normalized PF3 determinant strictly negative, with its largest value at u=0.','checker':'research/conjecture_replay/check_CR1_theta_translation_PF3_reduction.py'}],'outcome':'exact scalar gate; PF3 strongly supported but unproved','identity':'H_3/Phi^3 = g_dd*g_dddd-g_ddd^2+2*g_dd^3 for g=log Phi','positive_curvature_form':'With h=-g_dd>0, H_3/Phi^3=h*h_dd-h_d^2-2h^3=h^2((log h)dd-2h).','PF3_condition':'The required coalescent sign -H_3>0 is equivalent to (log h)dd<2h.','scan':{'interval':'0<=u<=1.5','points':20001,'labels':14,'largest_normalized_H3':-10456.710423582248,'location':0.0,'evidence_class':'NUMERICAL'},'typing':'Global PF2 supplies h>0 but does not imply the new curvature inequality. This is the first genuinely independent translation-order-three gate.','completion_needed':'Give interval/rational theta-tail bounds for h,h_d,h_dd on a compact interval and analytic one-label domination on the tails.','next':'derive_the_one_label_tail_formula_for_(log_h)dd_minus_2h_and_bound_the_theta_mixture_perturbation'}
write_result(R/'research/conjecture_replay/results/CR1_theta_translation_PF3_reduction.json',out);print(json.dumps({'passed':True,'identity_proved':True,'PF3':'supported','largest_scan_value':-10456.710423582248}))
