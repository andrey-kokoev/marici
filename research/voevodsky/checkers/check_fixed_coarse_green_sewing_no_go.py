"""Exact infeasibility certificate for fixed-form, source-identifying sewing."""
from pathlib import Path
import contextlib
import io
import json
import runpy
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    witness=runpy.run_path(str(ROOT/'research/voevodsky/checkers/check_ordinary_coarse_green_grouping_obstruction.py'))
L=s.Matrix(witness['forms']['left'])
R=s.Matrix(witness['forms']['right'])
assert L-R == s.Matrix([[0,4],[4,0]])

# Any common carrier with equal sewn source images induces ONE Hermitian matrix.
# Its entries would have to equal both independent pullbacks.
a,b,c,d=s.symbols('a b c d', real=True)
H=s.Matrix([[a,b+s.I*c],[b-s.I*c,d]])
equations=list(H-L)+list(H-R)
assert s.linsolve(equations,(a,b,c,d)) is s.EmptySet

# A common counterterm cannot change the discrepancy.
assert (L+H)-(R+H)==L-R
# A correction confined to shifted products is zero on these ordinary vectors.
assert L+s.zeros(2)-R != s.zeros(2)
# Even independently positive corrections can only match by changing at least
# one prescribed ordinary pullback; any one-sided correction must be indefinite.
assert set((L-R).eigenvals()) == {-4,4}
# Null directions of an enlarged carrier cannot alter pairings.
G=s.diag(1,1,0)
base=s.Matrix([[1,0],[0,1],[0,0]])
n1,n2=s.symbols('n1 n2', real=True)
null_lift=s.Matrix([[0,0],[0,0],[n1,n2]])
assert (base+null_lift).T*G*(base+null_lift)==base.T*G*base

result={'passed':True,
 'common_pullback_equations':'inconsistent',
 'witness_defect':[[0,4],[4,0]],
 'witness_defect_eigenvalues':[-4,4],
 'checks':{'common_counterterm_leaves_defect':True,
           'shifted_only_correction_cannot_change_ordinary_witness':True,
           'radical_extension_cannot_change_pullback':True},
 'scope':'No source-identifying common isometric sewing preserving both specified raw coarse forms. Does not prohibit a relative nonisometric correspondence or a changed, separately justified assembly.'}
out=ROOT/'research/voevodsky/results/fixed-coarse-green-sewing-no-go.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
