"""Verify the repaired rank26 aggregate and reject the former semantic mutation."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research'/'voevodsky'/'results'
OUT=V/'cosmology_supported_comparison_to_rank26.json'
def contract_ok(x):
    comparison=x.get('supported_DNC_comparison',{})
    return (x.get('schema','').endswith('.v2') and
            comparison.get('status')=='unverified' and
            'DNC_consequence' not in x and 'horn_obstruction' not in x)
def main():
    full=json.loads((V/'cosmology_full_rank26_characteristic_zero_absorption.json').read_text())
    dnc=json.loads((V/'cosmology_DNC_full_family_factorization_gate.json').read_text())
    assert contract_ok(full)
    assert 'not yet established' in dnc['decision']
    mutated=dict(full);mutated['DNC_consequence']='established by passed=true'
    assert not contract_ok(mutated)  # deliberate-failure mutation must be rejected
    out={
      'schema':'marici.voevodsky.cosmology-supported-comparison-to-rank26.v2',
      'status':'aggregation_gate_repaired_unsupported_DNC_consequences_rejected',
      'relation_absorption':'The v2 aggregate retains exact IBP, K, and q relation-family absorption.',
      'comparison_status':'unverified',
      'required':['named supported target complex','chain map','support localization','differential commutation','factorization'],
      'deliberate_failure':'Injecting the former DNC consequence makes contract_ok false.',
      'decision':'The aggregate no longer promotes diagnostic passed status to geometric theorem truth.',
      'next_gate':'construct-supported-rank26-comparison',
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
