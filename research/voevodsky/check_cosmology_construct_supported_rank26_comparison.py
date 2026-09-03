"""DPC interface audit for constructing the supported rank26 comparison."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research'/'voevodsky'/'results'
OUT=V/'cosmology_construct_supported_rank26_comparison.json'
REQUIRED={'source_basis','source_differential','supported_target_basis','supported_target_differential','generator_map','support_localization','chain_residual'}
def main():
    rank=json.loads((V/'cosmology_full_rank26_characteristic_zero_absorption.json').read_text())
    exc=json.loads((V/'cosmology_exceptional_triangle_relative_localization.json').read_text())
    available=set(rank)|set(exc);missing=sorted(REQUIRED-available)
    assert missing==sorted(REQUIRED)
    zero_candidate={'generator_map':'zero'}
    zero_admissible=REQUIRED.issubset(zero_candidate)
    assert not zero_admissible  # deliberate failure: an unsourced zero map is refused
    out={
      'schema':'marici.voevodsky.cosmology-construct-supported-rank26-comparison.v1',
      'status':'DPC_conjecture_rejected_existing_artifacts_do_not_construct_supported_comparison',
      'conjecture':'The exact rank26 row-module artifacts and exceptional-triangle localization determine a canonical supported chain map.',
      'rivals':['row modules lack geometric generator semantics','the exceptional complex is an independent three-edge model with no shared interface','absorption permits an abstract zero quotient map but does not source a geometric comparison'],
      'risky_consequences':sorted(REQUIRED),
      'falsification':'The aggregate exposes counts, seed families, and absorption classes; the exceptional checker exposes a 3x3 incidence boundary. They share no basis identifiers, differential contract, support map, or generator images. The deliberate zero-map candidate fails the provenance contract.',
      'missing_contract':missing,
      'residual':'No comparison can be constructed without geometrizing the rank26 generators or adding a separately sourced bridge. Dimension counts and zero quotient classes cannot define it.',
      'disposition':'Reject construction from current artifacts. Retain relation absorption, exceptional localization, and geometric horn as separate typed results.',
      'next_gate':'source-geometrization-contract',
      'limitations':['interface audit, not proof that no comparison exists'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
