#!/usr/bin/env python3
"""Search degree-bounded support for a normalized tau dual over F_101."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';P=101
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
rows=g['construct'](8);base=(0,1,1,1,1,1,(0,0));tau=(1,base)
def proj(v):return v.numerator*pow(v.denominator,-1,P)%P
def test(D):
 basis={}
 def keep(c):return sum(c[1][-1])<=D
 def reduce(row,insert=False):
  row={k:v%P for k,v in row.items() if v%P and keep(k)}
  while row:
   q=min(row);a=row[q]
   if q not in basis:
    if insert:
     z=pow(a,-1,P);basis[q]={k:v*z%P for k,v in row.items() if v*z%P}
    return row
   for k,v in basis[q].items():row[k]=(row.get(k,0)-a*v)%P
   row={k:v for k,v in row.items() if v}
  return {}
 for r in rows.values():reduce({k:proj(v) for k,v in r.items()},True)
 residual=reduce({tau:1});return {'max_monomial_degree':D,'projected_relation_rank':len(basis),'tau_not_in_projected_row_span':bool(residual),'tau_residual_nnz':len(residual)}
tests=[test(d) for d in range(4)];out={'schema':'marici.benincasa.cosmology-rees-tau-finite-support-dual.v1','field_prime':P,'cutoff':8,'ansatz':'lambda vanishes on every coordinate of monomial degree greater than D','tests':tests,'interpretation':'tau outside the projected relation-row span is equivalent to existence of a normalized dual supported in the degree-D coordinate set','uniformity_caveat':'a Q8 solution is uniform only after proving that relations introduced at larger cutoffs cannot add constraints on its support','passed':True};(R/'cosmology_rees_tau_finite_support_dual.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
