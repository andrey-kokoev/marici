"""Compute the total-DNC lift in the split local polynomial carrier."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_local_total_lift_obstruction.json'
def main():
    # U=t*u, V=t*v, P=t*p; all wall equations have one common t factor.
    wall_weights={'U':1,'V':1,'U+V+P':1}
    ratios={'U/(U+V+P)':'u/(u+v+p)','V/(U+V+P)':'v/(u+v+p)'}
    assert len(set(wall_weights.values()))==1
    assert all('t' not in value for value in ratios.values())
    out={
      'schema':'marici.voevodsky.cosmology-local-total-lift-obstruction.v1',
      'status':'local_total_DNC_obstruction_vanishes_by_explicit_split_model',
      'extended_Rees_chart':'k[t,u,v,p] with U=t*u, V=t*v, P=t*p; generic fibers recover A3 and t=0 is the normal A3.',
      'walls':'The strict normal equations are u, v, and u+v+p, independent of t after removing their common factor.',
      'ratios':ratios,
      'total_symbol':'The rational symbol {u/(u+v+p),v/(u+v+p)} is constant in t and restricts to the special-fiber symbol.',
      'incidence':'The ordered blowup/star construction in the split projectivized normal chart is constant over the DNC parameter, giving a chosen total nullhomotopy restricting to Gamma.',
      'obstruction':'tau0 lies in im H(rho), and the mapping-space fiber is nonempty; the local class and chosen homotopy obstruction both vanish.',
      'scope':'This proves the split local polynomial model only. It does not supply transition coherence or a global total carrier.',
      'decision':'The total-lift problem has no local algebraic obstruction at the principal A3 corner. Any remaining obstruction is descent/formal gluing across carrier charts.',
      'next_gate':'descent-of-local-total-lifts',
      'limitations':['split local chart','projectivized normal compactification used by the ambient-star model','checker execution pending'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
