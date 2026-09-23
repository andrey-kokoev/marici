"""Exact graded defect invariant for the historical bounded analytic edge fixture."""
import importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
p=ROOT/'research/voevodsky/checkers/check_degree_four_reciprocal_waldhausen_realization.py'
spec=importlib.util.spec_from_file_location('historical_cones',p);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
assert h.out['all_exact']
profile=[]
for (i,j),(plus,minus) in sorted(h.intervals.items()):
 rank=plus.rank();kernel=plus.cols-rank;cokernel=plus.rows-rank
 assert minus.rank()==rank and minus.shape==plus.shape
 profile.append({'interval':[i,j],'shape':list(plus.shape),'rank':rank,'kernel':kernel,'cokernel':cokernel})
generators=[row for row in profile if row['interval'][1]==row['interval'][0]+1]
assert [(row['cokernel'],row['kernel']) for row in generators]==[(1,0),(0,1),(1,0),(0,1)]
assert len(profile)==10
# A simplex-face cone has zero graded relative homology: first generator's
# nonzero H_0 cannot be sent to it by a homology-preserving equivalence.
assert generators[0]['cokernel']==1
report={'passed':True,'intervals':profile,'generating_edge_defects':'alternating cokernel/kernel of dimension one','first_edge_rejects_acyclic_target':True,'scope':'Bounded historical operator fixture; no role-to-polyhedral functor or analytical completion constructed.'}
(ROOT/'research/voevodsky/results/analytic-interval-defect-profile.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'intervals':len(profile),'generators':generators},indent=2))
