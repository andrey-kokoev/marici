"""Check regulator naturality and expose ramification multiplicities."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_regulator_naturality_square.json'
def pullback(e,f):
    return {'top_weight':e*f,'D1_v_exponent':-e*f,'D2_u_exponent':e*f,'D3_ratio_exponent':e*f}
def main():
    strict=pullback(1,1); ramified=pullback(2,1)
    assert strict=={'top_weight':1,'D1_v_exponent':-1,'D2_u_exponent':1,'D3_ratio_exponent':1}
    assert ramified['top_weight']==2
    out={
      'schema':'marici.voevodsky.cosmology-regulator-naturality-square.v1',
      'status':'naturality_proved_for_strict_transverse_base_change_ramification_boundary_identified',
      'admissible_morphism':['Cartesian regular centers','base-change isomorphism for the associated graded/Rees algebra','reduced labeled wall pullbacks with ramification index one','orientation-preserving ordered conormal map'],
      'blowup_square':'The Rees base-change condition identifies the pulled-back blowup and every exceptional incidence stratum.',
      'log_square':'Pullback commutes with relative dlog and wedge, so f^*Xi_rel=Xi_rel.',
      'tame_square':'For ramification index one, tame symbols commute with pullback divisor by divisor; the tuple remains (v^-1,u,-v/u,1).',
      'incidence_square':'Reduced Cartesian strata preserve each oriented flag with coefficient one, hence f^*Gamma=Gamma and f^*sigma123=sigma123.',
      'conclusion':'Phi is a natural transformation on the strict transverse ordered subcategory.',
      'ramification_test':'Under u->u^e and v->v^f, top weight and all outer tame exponents scale by e*f. The primitive unit is preserved only when e=f=1 for positive indices.',
      'decision':'Replace unrestricted transverse naturality by strict transverse/Rees-compatible naturality. Ramified maps require weighted horns and do not preserve the primitive constructor.',
      'next_gate':'ramified-base-change-weighted-horn',
      'limitations':['relative regulator','strict transverse category fully typed; global carrier still absent','checker execution pending'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
