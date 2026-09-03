#!/usr/bin/env python3
"""Census corrected symbol dimensions across homogeneous degrees."""
import contextlib,io,json,runpy,sys
from pathlib import Path
HERE=Path(__file__).resolve();src=HERE.with_name('check_cosmology_rees_residual_nullspace_basis.py');rows=[]
for D in range(20,33):
 old=sys.argv;sys.argv=[str(src),str(D)]
 try:
  with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(src))
 finally:sys.argv=old
 rows.append({'D':D,'domain':len(g['cols']),'symbol_rank':len(g['pivs']),'nullity':len(g['null']),'known_rank':g['knownrank'],'quotient':len(g['residual'])})
checks={'domain_4D_minus_36':all(r['domain']==4*r['D']-36 for r in rows),'rank_D_minus_3':all(r['symbol_rank']==r['D']-3 for r in rows),'nullity_3D_minus_33':all(r['nullity']==3*r['D']-33 for r in rows),'known_3D_minus_43':all(r['known_rank']==3*r['D']-43 for r in rows),'quotient_10':all(r['quotient']==10 for r in rows)}
out={'schema':'marici.benincasa.cosmology-rees-residual-dimension-recurrence.v1','prime':101,'degree_range':[20,32],'rows':rows,'checks':checks};R=HERE.parents[1]/'results';(R/'cosmology_rees_residual_dimension_recurrence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':checks,'first':rows[0],'last':rows[-1]},indent=2))
