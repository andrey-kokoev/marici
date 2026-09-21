"""Raw derivative descent and a cross-cut Green isometry obstruction."""
from pathlib import Path
import contextlib
import io
import json
import runpy
ROOT = Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    src = runpy.run_path(str(ROOT/'research/grothendieck/checkers/check_six_prime_derived_block_associativity.py'))
D, relation, multiply = (src[k] for k in ('derivative','relation','multiply'))
p = multiply(relation((0,1),0),relation((2,3),0))
assert p
image = D(p,0)
# With vacuum histories, earlier/later relation routes cancel at every edge.
assert not image
# Raw derivative descent must be tested on mixed products, too.
results = []
for ka in (0,1):
    for kb in (0,1):
        col = multiply(relation((0,1),ka),relation((2,3),kb))
        value = D(col,0)
        results.append({'types':[ka,kb],'derivative_nonzero':bool(value)})
        assert not value
# Different middle cuts share a coarse edge even with vacuum histories.
u = multiply(relation((0,1),0), {((2,3),(False,False)):1})
v = multiply(relation((0,2),0), {((1,3),(False,False)):1})
du,dv = D(u,0),D(v,0)
assert all(not left and letter == 0 and not right
           for x,y,left,letter,right in set(du) | set(dv))
coarse_cross = sum(c*dv.get(key,0) for key,c in du.items())
assert coarse_cross == 1
# Cut-labelled direct sums put these images in different orthogonal blocks.
refined_cross = 0
assert coarse_cross != refined_cross
print(json.dumps({'passed':True,'product_derivative_tests':results,
 'coarse_vacuum_cross_pairing':coarse_cross,
 'orthogonal_cut_target_cross_pairing':refined_cross,
 'scope':'Raw derivative kills tested product relations, but its vacuum Green form is not the orthogonal cut-target pullback. No claim about other independently prescribed coarse forms.'},indent=2))
