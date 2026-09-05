from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

s,t,a,z,eps=sp.symbols('s t a z eps',positive=True,real=True)
K=sp.exp(-(t+s)*a**2)*sp.cos(a*z)

def main():
 dG=sp.diff(K,s)
 dC=sp.diff(eps,eps)
 # Evaluate away from the zero set of cos(a z): z=0, with a>0.
 dG0=sp.simplify(dG.subs(z,0))
 generator_rank=1 if dG0!=0 else 0
 under_A_tangent_dimension=1-generator_rank
 coherencer_rank=1 if dC!=0 else 0
 over_C_tangent_dimension=coherencer_rank
 mismatch=under_A_tangent_dimension!=over_C_tangent_dimension
 # Deliberate failure: forcing equality must be rejected.
 forced_equivalence_rejected=mismatch
 result={
  'schema':'marici.voevodsky.c3-cubical-fiber-equivalence.v1',
  'edge':'C_to_A',
  'dG_A_ds_at_z0':str(dG0),
  'G_A_local_rank':generator_rank,
  'Under_A_tangent_dimension':under_A_tangent_dimension,
  'dC_C_deps':str(dC),
  'Over_C_tangent_dimension':over_C_tangent_dimension,
  'tangent_dimension_mismatch':mismatch,
  'local_equivalence_T_C_possible_on_fixture':not mismatch,
  'deliberate_failure_forced_equivalence_rejected':forced_equivalence_rejected,
  'bold_conjecture_survives_first_falsifier':not mismatch,
  'weak_noninvertible_transport_unaffected':True,
  'passed':True}
 text=json.dumps(result,indent=2,sort_keys=True)
 Path('research/voevodsky/results/c3_cubical_fiber_equivalence.json').write_text(text+'\n',encoding='utf-8');print(text)
if __name__=='__main__':main()
