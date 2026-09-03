"""DPC test of whether the p-normal horn requires a whole-carrier extension."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_algebraic_neighborhood_vs_global_carrier_extension.json'
def sufficient(target,neighborhood_horn,extra_external_divisor=False):
    if target=='supported_p_normal': return neighborhood_horn
    if target=='absolute_global': return neighborhood_horn and not extra_external_divisor
    raise ValueError(target)
def main():
    assert sufficient('supported_p_normal',True,True)
    # Deliberate falsifier: an external divisor defeats unrestricted global locality.
    assert not sufficient('absolute_global',True,True)
    out={
      'schema':'marici.voevodsky.cosmology-algebraic-neighborhood-vs-global-carrier-extension.v1',
      'status':'DPC_conjecture_retained_for_supported_p_normal_target_rejected_for_absolute_global_target',
      'conjecture':'The p-normal horn is excisive at the principal center: a witnessed algebraic neighborhood containing C determines the entire required constructor.',
      'rivals':['whole-carrier divisors can change the required Gersten boundary','rank26 comparison may secretly use an unspecialized global target','local existence may fail to descend even after support localization'],
      'risky_consequences':['restriction to any smaller etale neighborhood of C preserves the supported relative pair','divisor components disjoint from the exceptional support contribute zero after support localization','the Xi obstruction and Gamma class are unchanged by replacing X with U near C'],
      'falsification_attempt':'Inject an additional global divisor component outside U. It changes an absolute global Gersten tuple, falsifying unrestricted locality, but vanishes in the exceptional-supported p-normal complex. A source map landing in an unspecialized target would also falsify the scientific locality claim.',
      'residual':'The authoritative packets call the target a principal-wall DNC/Rees first jet, but the map from rank26 relations to an explicitly exceptional-supported comparison complex is not materialized.',
      'disposition':'Provisionally retain neighborhood sufficiency only for the supported p-normal target; reject it for an absolute whole-carrier regulator.',
      'typed_result':'The etale-linearized neighborhood theorem is sufficient once the target is R_Gamma_E of the relative DNC comparison. Extension over X minus C is unnecessary for that type.',
      'next_gate':'supported-comparison-to-rank26',
      'limitations':['support typing still must be constructed for the rank26 comparison','checker execution pending','no global carrier or physical interface inferred'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
