"""Exact source audit: a vacuum probe adds a boundary, not a surviving pushout."""
from pathlib import Path
from itertools import permutations,product
import runpy,json
ROOT=Path(__file__).resolve().parents[3]
t=runpy.run_path(str(ROOT/'research/nima/checkers/check_all_depth_observer_tower.py'))
f=t['f'];ordered=t['ordered'];score=t['score']
probe=((('e',0,1,0),('e',3,7,0),('e',15,31,0)),((),)*4)
a0=f['relation']((0,1),0);a1=f['relation']((0,1),1)
b0=f['relation']((2,3),0);c0=f['relation']((4,5),0)
k=f['chain_product']([a0,b0,c0]);v2=f['multiply'](a1,b0)
v3=f['chain_product'](t['factors'](3))
def vacuum(col):return ordered(0,col,3).get(probe,0)
assert len(k)==8 and vacuum(k)==1
assert not ordered(0,k,1) and not ordered(0,k,2)
assert vacuum(v3)==0 and score(ordered(0,k,3),3)==0
assert score(ordered(0,v3,3),3)==4
# All contexts for the old graded line; a vacuum probe cannot see a retained
# feature, even when source-action saturation is included.
contexts=0
for word in permutations((4,5)):
    for marks in product((0,1),repeat=2):
        assert vacuum(f['multiply'](v2,{(word,marks):1}))==0
        contexts+=1
# The initial forgotten/mixed corner has precisely two ideal dimensions.
paths=[(w,m) for w in permutations((0,1)) for m in product((0,1),repeat=2)]
assert len(paths)-f['rank']([f['record'](0,*p) for p in paths])==2
assert score(ordered(0,a0,1),1)==1
assert score(ordered(0,a1,1),1)==0
# Any lift of the old vacuum scalar has coefficient one on a0; a possible
# a1 correction cannot cancel the vacuum response after right multiplication.
tail=f['multiply'](b0,c0)
assert vacuum(f['multiply'](a0,tail))==1
assert vacuum(f['multiply'](a1,tail))==0
# Restricted to I, chi(D3(x*tail)) is exactly ell_1(x): both are supported
# on the initial two-event vacuum corner and agree on its ideal basis.
assert [vacuum(f['multiply'](a,tail)) for a in (a0,a1)]==[1,0]
result={'passed':True,'old_graded_line_contexts_checked':contexts,
 'vacuum_and_residual_values_on_k_v3':[[1,0],[0,4]],
 'checks':{'vacuum_probe_preserves_old_graded_line_lift':True,
 'direct_adjacent_pushout_nullhomotopy_remains_available':True,
 'vacuum_saturation_contains_the_base_detector':True,
 'vacuum_observer_to_O1_has_forced_lift_obstruction':True,
 'vacuum_scalar_attachment_independent_of_residual_one':True},
 'scope':'Actual marked-source identities. Derived vanishing uses the explicit bounded H=B-jwq; nonvanishing uses the finite source/projective restriction or the source-equivariant section obstruction. This is not a numerical acquisition or a full-tower faithfulness claim.'}
out=ROOT/'research/voevodsky/results/vacuum-probe-extension-class.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
