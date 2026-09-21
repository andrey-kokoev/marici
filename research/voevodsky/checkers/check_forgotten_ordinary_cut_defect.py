"""Full 90-channel forgotten ordinary cut defect, exact vacuum forms."""
from pathlib import Path
import contextlib
import io
import json
import runpy
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(ROOT/'research/voevodsky/checkers/check_ordinary_coarse_green_grouping_obstruction.py'))
observe,pairing=prior['observe'],prior['pairing']
partitions=list(prior['src']['blocks'](tuple(range(6))))
assert len(partitions)==90
images={g:[observe(*p,g) for p in partitions] for g in ('left','right')}
forms={g:s.Matrix(90,90,lambda i,j:pairing(images[g][i],images[g][j])) for g in images}
L,R=forms['left'],forms['right']
Delta=L-R
assert Delta==Delta.T and all(Delta[i,i]==0 for i in range(90))
# Reversal exchanges the cut groupings. Relation orientations may change;
# derive the signed comparison from actual coordinate images if needed.
eigenvalues=Delta.eigenvals()
assert all(e.is_real and (e.is_positive or e.is_negative or e==0) for e in eigenvalues)
inertia=[sum(m for e,m in eigenvalues.items() if test(e))
         for test in (lambda e:e.is_positive,lambda e:e.is_negative,lambda e:e==0)]
assert sum(inertia)==90
# Relative packets telescope; this does not claim a sewing counterterm.
M=16*s.eye(90)
assert (L-M)-(R-M)==Delta
result={'passed':True,'forgotten_ordinary_channels':90,
 'left_rank':L.rank(),'right_rank':R.rank(),
 'defect_rank':90-inertia[2],'defect_inertia_positive_negative_null':inertia,
 'defect_eigenvalues':{str(e):m for e,m in eigenvalues.items()},
 'nonzero_ordered_cross_entries':sum(1 for v in Delta if v!=0),
 'scope':'Exact unit-vacuum/Omega sector with orthogonal coarse-cut labels. Not the full 2160-coordinate spectral defect or a source-admitted counterterm.'}
out=ROOT/'research/voevodsky/results/forgotten-ordinary-cut-defect.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
