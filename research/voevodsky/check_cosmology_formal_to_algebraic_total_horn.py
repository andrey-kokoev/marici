"""Type the effectivity obstruction from a formal total horn to an algebraic one."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_formal_to_algebraic_total_horn.json'
def effective(formal_class,algebraic_image): return formal_class in algebraic_image
def main():
    assert effective('tau_hat',{'tau_hat'}) and not effective('tau_hat',set())
    out={
      'schema':'marici.voevodsky.cosmology-formal-to-algebraic-total-horn.v1',
      'status':'algebraization_obstruction_and_strong_effectivity_certificates_defined',
      'exact_gate':'Let completion map the algebraic total comparison mapping space to its formal completion. The formal horn algebraizes exactly when tau_hat lies in its essential image, including the chosen nullhomotopy coherence.',
      'class_obstruction':'At the class level the first obstruction is tau_hat modulo the image on pi0/cohomology; mapping-space fibers retain higher effectivity data.',
      'certificate_etale':'An algebraic neighborhood U of C with a wall-preserving etale map U->Tot(N_C/X) inducing the formal linearization pulls back the universal algebraic normal-model horn.',
      'certificate_Rees':'An algebraic finite-type multiplicative splitting of the Rees family with algebraic ordered wall coordinates directly supplies the ratios, symbol, incidence star, and regulator.',
      'formal_boundary':'A formal isomorphism alone need not extend to either certificate. Approximation to finite order does not equal exact algebraization of the symbol and chosen homotopy.',
      'proper_boundary':'Formal GAGA-style effectivity can be used only after its properness and coherence hypotheses are proved for the actual comparison object; none are materialized here.',
      'materialized_state':'The local polynomial chart is algebraic and passes. The intended global carrier supplies no algebraic effectivity certificate.',
      'decision':'Formal total existence cannot be promoted silently. Algebraization requires an explicit completion-preimage or a stronger etale/Rees certificate.',
      'next_gate':'etale-linearized-carrier-theorem',
      'limitations':['effectivity classification, not global construction','checker execution pending','no rank26 or physical promotion'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
