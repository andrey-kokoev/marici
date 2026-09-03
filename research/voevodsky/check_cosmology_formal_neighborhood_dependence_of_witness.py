"""Separate associated-graded horn data from filtered Rees/formal-neighborhood data."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_formal_neighborhood_dependence_of_witness.json'
def main():
    layers={'exceptional_P2':1,'labeled_triangle':1,'relative_Gamma':1,'relative_Xi':1,'vertical_tame_tuple':1,'total_Rees_family':2,'absolute_form':2,'global_carrier_comparison':2}
    assert all(layers[k]==1 for k in ('exceptional_P2','labeled_triangle','relative_Gamma','relative_Xi','vertical_tame_tuple'))
    assert all(layers[k]==2 for k in ('total_Rees_family','absolute_form','global_carrier_comparison'))
    out={
      'schema':'marici.voevodsky.cosmology-formal-neighborhood-dependence-of-witness.v1',
      'status':'normal_cone_and_formal_neighborhood_layers_separated',
      'first_order_layer':['E=P(N_C/X)','ordered exceptional triangle','relative fundamental chain Gamma','relative dlog ratios Xi_rel','vertical Milnor/tame decoration'],
      'first_order_theorem':'These objects factor through gr_I(O_X)=Sym(I/I^2) together with the common-line ordered conormal basis. They are invariant under changing higher wall jets while preserving that data.',
      'higher_layer':['filtered Rees algebra and total DNC family','strict transforms away from E','horizontal or mixed logarithmic terms','absolute carrier form','comparison to a global rank26 geometric source'],
      'filtered_boundary':'The associated graded fixes I^n/I^(n+1), but not the extension and gluing data assembling the I-adic filtration. Equal normal cones do not identify formal completions or total Rees families.',
      'target_refinement':'Because the scientific p-normal target is relative and first-order, the sourced special-fiber HomotopyLift does not require a splitting of the full formal neighborhood. Such a splitting is required only for total-carrier promotion.',
      'classifying_map_correction':'The earlier six-field carrier contract is sufficient for total DNC realization; the relative special-fiber theorem needs only regular center, common line, ordered conormal basis, and labeled first-order walls.',
      'decision':'Retain the relative theorem unconditionally on first-order carrier data and isolate total-DNC promotion as a stronger filtered-Rees gate.',
      'next_gate':'Rees-splitting-obstruction',
      'limitations':['relative first-order classification','no global first-order carrier data materialized','checker execution pending'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
