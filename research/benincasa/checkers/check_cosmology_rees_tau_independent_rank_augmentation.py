#!/usr/bin/env python3
"""Independent modular rank-augmentation falsifier for the finite tau_p target."""
import contextlib,io,json,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'))
checks=[]
for p in [101,103,107]:
 m=g['configure'](p);low,cols=m.column_packet();width=len(cols);basepoint=(3,6,-3);points=[(basepoint[0],basepoint[1],basepoint[2]+o) for o in m.OFFSETS];gens=[m.raw_relations(pt,cols) for pt in points];w1=m.interpolation_weights(1);w2=m.interpolation_weights(2);pivots={}
 for sampled in zip(*gens,strict=True):
  r0=dict(sampled[m.OFFSETS.index(0)]);r1=m.combine(sampled,w1);r2=m.combine(sampled,w2)
  m.base.add_pivot(m.shifted_row(r0,width,2),pivots);m.base.add_pivot(m.assemble(({},r0,r1),width),pivots);m.base.add_pivot(m.assemble((r0,r1,r2),width),pivots)
 before=len(pivots);label=(0,1,1,1,1,1,(0,0));target={width+cols[label]:3%p};m.base.add_pivot(target,pivots);after=len(pivots);checks.append({'prime':p,'relation_rank':before,'augmented_rank':after,'rank_gain':after-before})
assert all(x['relation_rank']==4146 and x['rank_gain']==1 for x in checks)
out={'schema':'marici.benincasa.cosmology-rees-tau-independent-rank-augmentation.v1','test':'independent modular rank augmentation using the original raw_relations and base.add_pivot implementation','checks':checks,'result':'tau_p increases the assembled relation rank by one at every tested prime','scope':'chosen z-offset ambient-four presentation only; modular independence does not establish slice invariance or cohomological closure','passed':True};(R/'cosmology_rees_tau_independent_rank_augmentation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
