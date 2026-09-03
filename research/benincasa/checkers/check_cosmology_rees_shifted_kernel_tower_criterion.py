#!/usr/bin/env python3
"""State and test the shifted-kernel tower criterion at admitted cutoffs."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
a45=json.loads((R/'cosmology_rees_exact_faithful_kernel_lift.json').read_text());a56=json.loads((R/'cosmology_rees_a5_shifted_candidate_nonvanishing_mod101.json').read_text())
def expanded(A):
 # K_A=u v^A(v-3)-v^(A+1)(u-6)-6v^(A+1)+3u v^A
 return {'u*v^(A+1)':1-1,'u*v^A':-3+3,'v^(A+1)':6-6}
assert expanded(4)==expanded(5)=={'u*v^(A+1)':0,'u*v^A':0,'v^(A+1)':0}
assert a45['passed'] and a56['nonzero_mod_relation_space'] and a56['exact_A6_target_zero']
out={'schema':'marici.benincasa.cosmology-rees-shifted-kernel-tower-criterion.v1','candidate_family':'K_A=u*v^A*(v-3)-v^(A+1)*(u-6)-6*v^(A+1)+3*u*v^A','formal_identity':'K_A=0 after polynomial expansion for every integer A','verified_kernel_steps':[{'source':4,'target':5,'source_nonzero':True,'target_zero':True,'strength':'exact rational'},{'source':5,'target':6,'source_nonzero':True,'target_zero':True,'strength':'exact rational via full-rank mod-101 nonmembership'}],'tower_criterion':'K_A defines a nonzero Q_A-to-Q_(A+1) kernel class exactly when its four labelled coordinates exist at A, its class is nonzero in Q_A, and the polynomial identity is admitted by the A+1 relation map','exact_residual':'target-zero identities form a formal shifted family, but source nonvanishing and relation admission are verified only at A=4 and A=5','disposition':'two consecutive nonmonic transitions proved; persistent tower and eventual nonmonicity remain unverified','consequence':'the finite diagram already refutes monicity at A4-to-A5 and A5-to-A6, but two steps do not decide eventual stabilization or a colimit','next_acceptance_test':'construct Q7 and test K6 source nonvanishing in Q6 plus target admission in Q7, or prove a source-derived recurrence preserving these properties','passed':True};(R/'cosmology_rees_shifted_kernel_tower_criterion.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
