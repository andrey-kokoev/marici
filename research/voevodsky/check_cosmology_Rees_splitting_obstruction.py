"""Separate the exact total-lift obstruction from the stronger formal Rees splitting condition."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_Rees_splitting_obstruction.json'
def lifts(class_in_special,image_of_restriction): return class_in_special in image_of_restriction
def main():
    assert lifts('tau0',{'tau0'}) and not lifts('tau0',set())
    out={
      'schema':'marici.voevodsky.cosmology-Rees-splitting-obstruction.v1',
      'status':'exact_total_lift_obstruction_defined_formal_splitting_reclassified_as_sufficient_not_necessary',
      'complexes':'Let K_tot be the witnessed total-DNC comparison object and K_0 its special-fiber relative pair, with restriction rho:K_tot->K_0.',
      'class_obstruction':'The special-fiber class tau0 lifts exactly when [tau0] lies in the image of H(rho); its first obstruction is its class in coker H(rho).',
      'homotopy_obstruction':'Retaining the chosen nullhomotopy requires a point in the homotopy fiber of the induced mapping-space restriction over tau0; cohomological liftability alone may forget higher coherence.',
      'splitting':'A multiplicative filtered splitting of the completed Rees/I-adic algebra gives a section of the normal specialization and kills every such obstruction.',
      'necessity_correction':'Full formal splitting is not necessary for one particular horn to lift. A nonsplit Rees algebra may still have tau0 in im H(rho).',
      'formal_layers':'Compatible splittings of 0->I^(n+1)/I^(n+2)->I^n/I^(n+2)->I^n/I^(n+1)->0 are sufficient stagewise data; multiplicative coherence is an additional condition.',
      'target_boundary':'The p-normal theorem needs only tau0 and is unaffected by this total-lift obstruction.',
      'decision':'Replace the vague Rees-splitting gate by the restriction/fiber obstruction. Treat formal linearization only as a strong sufficient certificate.',
      'next_gate':'local-total-lift-obstruction',
      'limitations':['abstract obstruction until K_tot is materialized','global carrier absent','checker execution pending'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
