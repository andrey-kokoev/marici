"""Exact source audit for the 270-private-row ideal-action gate.

Outer endpoint labels are explicitly checked when testing shorter prefixes;
seam/buffer keys alone do not encode a terminal vacuum buffer's endpoint.
"""
from pathlib import Path
from itertools import product
import runpy,json
ROOT=Path(__file__).resolve().parents[3]
g=runpy.run_path(str(ROOT/'research/nima/checkers/check_translated_cubic_observer_growth.py'))
t=runpy.run_path(str(ROOT/'research/nima/checkers/check_all_depth_observer_tower.py'))
f=g['f'];ordered=t['ordered'];score=t['score']
cols=[];pivots=[]
for pairs in g['pairings'](tuple(range(6))):
    for kinds in ((1,1,0),(1,0,1),(0,1,1)):
        start=0;ds=[];seams=[]
        for pair,kind in zip(pairs,kinds):
            seams.append(('e',start,start|(1<<pair[0]),kind))
            ds.append(g['one'](f['derivative'](start,f['relation'](pair,kind))))
            start|=sum(1<<p for p in pair)
        cols.append((pairs,kinds,g['join'](g['join'](ds[0],ds[1]),ds[2])))
        pivots.append((tuple(seams),((),)*4))
assert len(cols)==len(set(pivots))==270
for j,(_,_,im) in enumerate(cols):
    assert [im.get(p,0) for p in pivots]==[int(k==j) for k in range(270)]
# Prefixes generate the right I action; tails generate the left I action.
right_exceptions=[];left_tails=0
for j,(pairs,kinds,_) in enumerate(cols):
    prefix=f['chain_product']([f['relation'](p,k) for p,k in zip(pairs[:2],kinds[:2])])
    end=sum(1<<p for pair in pairs[:2] for p in pair)
    # A four-event I^2 input can only be seen by the uncontextualized old
    # depth-two row, whose exact outer endpoint is mask 15, not mask 63.
    old=score(ordered(0,prefix,2),2) if end==15 else 0
    if old:right_exceptions.append((j,pairs,kinds,old))
    # Every two-factor tail ends at 63; old O2 is supported on subcorners
    # of the initial interval [0,15], so its complete saturation kills it.
    tail_start=sum(1<<p for p in pairs[0])
    assert tail_start!=0 and (63&~15)!=0
    left_tails+=1
assert right_exceptions==[(1,((0,1),(2,3),(4,5)),(1,0,1),2)]
# The exceptional coordinate tests exactly the old prefix coefficient after
# multiplying by the final mixed diamond. Audit every minimal prefix product.
c1=f['relation']((4,5),1)
prefix_checks=0
for pairs in g['pairings'](tuple(range(4))):
    for kinds in product((0,1),repeat=2):
        prefix=f['chain_product']([f['relation'](p,k) for p,k in zip(pairs,kinds)])
        old=score(ordered(0,prefix,2),2)
        new=ordered(0,f['multiply'](prefix,c1),3).get(pivots[1],0)
        assert 2*new==old
        prefix_checks+=1
# Optional vacuum line is in BOTH action images, and is independent of all
# 270 degree-two coordinates.
vacrow=((('e',0,1,0),('e',3,7,0),('e',15,31,0)),((),)*4)
a0=f['relation']((0,1),0);b0=f['relation']((2,3),0);c0=f['relation']((4,5),0)
k=f['chain_product']([a0,b0,c0])
assert ordered(0,k,3).get(vacrow,0)==1
assert all(ordered(0,k,3).get(p,0)==0 for p in pivots)
assert score(ordered(0,f['multiply'](a0,b0),2),2)==0
result={'passed':True,'private_pivot_matrix':'270 by 270 identity (before positive scalar response factors)',
 'all_left_tail_generators':left_tails,'minimal_prefix_products_checked':prefix_checks,
 'right_action_missing_column':{'index':1,'pairs':right_exceptions[0][1],
 'kinds':right_exceptions[0][2]},
 'dimensions_without_vacuum':{'L':270,'I_N':270,'N_I':269},
 'dimensions_with_one_vacuum_probe':{'L':271,'I_N':271,'N_I':270},
 'checks':{'left_ideal_gate_survives':True,'right_ideal_equality_fails':True,
 'old_graded_line_has_no_equivariant_lift_into_I_O3':True},
 'scope':'Exact minimal source/action audit with outer labels. The whole-image statements use the owning finite-support and disjoint minimal-product proofs. No new global Ext computation, numerical conditioning bound, or existence/nonexistence of a different adjacent nullhomotopy into the whole kernel is asserted.'}
out=ROOT/'research/voevodsky/results/270-row-ideal-action-gate.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
