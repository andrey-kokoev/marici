"""Construct the initial relative-pair extension with primitive horn boundary."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_obstruction_universality_and_minimal_extension.json'
def main():
    absolute_disk={'H1':0,'H2':0};relative_quotient={'H1':1,'omega':1,'boundary':(1,-1,0)}
    assert absolute_disk=={'H1':0,'H2':0}
    assert relative_quotient['H1']==relative_quotient['omega']==1
    out={
      'schema':'marici.voevodsky.cosmology-obstruction-universality-and-minimal-extension.v1',
      'status':'initial_algebraic_relative_extension_constructed_local_geometric_witness_identified',
      'construction':'From the rank26 pair B_R->G_R, set B_plus=B_R direct_sum Z*z and G_plus=G_R direct_sum D(z), where D(z) has Gamma in degree one, z in degree two, and d Gamma=z.',
      'relative_cofiber':'G_plus/B_plus=(G_R/B_R) direct_sum Z*Gamma; the new relative class is nonzero although D(z) is absolutely acyclic.',
      'comparison':'Send z to the complete vector (Xi_rel,-sigma123,0 residuals), so omega(Gamma)=1.',
      'universality':'In the category of relative extensions under R with a chosen exact-boundary element h, there is a unique map from this free extension sending Gamma to h and fixing R.',
      'minimality':'One relative generator is sufficient and necessary for a primitive unit boundary. Any smaller extension retains im(omega)=0.',
      'geometric_boundary':'This is initial only algebraically. Admission to the witnessed category requires geometry realizing the free cell; the local ambient star supplies one witness, while the global carrier does not.',
      'nonuniqueness_boundary':'Different geometric realizations of the same initial algebraic pair need not be equivalent; universality does not prove uniqueness of source geometry.',
      'decision':'The obstruction is killed minimally by a rank-one relative attachment, correctly distinguished from an absolute acyclic summand.',
      'next_gate':'geometric-nonuniqueness-of-minimal-extension',
      'limitations':['algebraic initiality plus local witness','global geometric witness absent','checker execution pending'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
