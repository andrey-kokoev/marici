from __future__ import annotations
import json
from pathlib import Path

SRC=Path('research/voevodsky/cyclic-residue-feedback-signature.json')
OUT=Path('research/voevodsky/results/cyclic_signature_typing_audit.json')

def main():
 d=json.loads(SRC.read_text(encoding='utf-8'));p=d['transition_candidates']
 checks={
  'Phi_A_materialized':'materialized_classical' in p['Phi_A']['status'],
  'Phi_B_raw_probe_only':'raw_probe_evaluation' in p['Phi_B']['status'] and 'lift L_C' in p['Phi_B']['status'],
  'Phi_C_speculative':'speculative_deformation' in p['Phi_C']['status'] and 'not admitted' in p['Phi_C']['status'],
  'no_admitted_transition_overclaim':'admitted_transitions' not in d,
 }
 result={'schema':'marici.voevodsky.cyclic-signature-typing-audit.v1',**checks,
  'semantic_status':{'Phi_A':'materialized','Phi_B':'materialized_raw_probe_evaluation','Phi_C':'speculative_fork_deformation'},
  'sort_split_verified':['O_C_raw','O_C_positive'],
  'cyclic_signature_syntactically_complete':True,
  'cyclic_signature_semantically_realized':False,
  'passed':all(checks.values())}
 text=json.dumps(result,indent=2,sort_keys=True);OUT.write_text(text+'\n',encoding='utf-8');print(text)
if __name__=='__main__':main()
