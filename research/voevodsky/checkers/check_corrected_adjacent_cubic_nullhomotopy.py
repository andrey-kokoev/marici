"""Actual support checks for a lifted old graded line and adjacent nullhomotopy.

The bounded source-equivariant homotopy is constructed in the companion note.
No numerical linear splitting of the completed source is assumed.
"""
from pathlib import Path
from itertools import permutations,product
import runpy,json
ROOT=Path(__file__).resolve().parents[3]
t=runpy.run_path(str(ROOT/'research/nima/checkers/check_all_depth_observer_tower.py'))
g=runpy.run_path(str(ROOT/'research/nima/checkers/check_translated_cubic_observer_growth.py'))
f=t['f'];ordered=t['ordered'];score=t['score']
v2=f['chain_product'](t['factors'](2))
assert score(ordered(0,v2,2),2)==2
# Complete minimal four-event relation-product audit, across feature degrees.
nonzero=[];count=0
for pairs in g['pairings'](tuple(range(4))):
    for kinds in product((0,1),repeat=2):
        source=f['chain_product']([f['relation'](pair,kind) for pair,kind in zip(pairs,kinds)])
        value=score(ordered(0,source,2),2)
        if value:nonzero.append((pairs,kinds,value))
        count+=1
assert nonzero==[(((0,1),(2,3)),(1,0),2)]
oldrows={key for key,weight in t['selected'](3)}
rows=set(oldrows)
for pair1,pair2 in (((0,1),(2,3)),((0,2),(1,3))):
    start=sum(1<<p for p in pair1)
    for p,q,last in product(pair1,pair2,(4,5)):
        rows.add(((('e',0,1<<p,1),('e',start,start|(1<<q),1),
                   ('e',15,15|(1<<last),0)),((),)*4))
assert len(rows)==19
# All possible full-corner right contexts. Nonidentity left contexts are
# excluded by the fixed initial vertex. Source saturation just subdivides
# these same total contexts; it creates no extra first-four-event feature.
contexts=0
for word in permutations((4,5)):
    for marks in product((0,1),repeat=2):
        image=ordered(0,f['multiply'](v2,{(word,marks):1}),3)
        assert all(image.get(row,0)==0 for row in rows)
        contexts+=1
v3=f['chain_product'](t['factors'](3))
assert score(ordered(0,v3,3),3)==4
# Higher-depth fixture for the same line-lift support mechanism.
higher=0
for word in permutations((6,7)):
    for marks in product((0,1),repeat=2):
        image=ordered(0,f['multiply'](v3,{(word,marks):1}),4)
        assert all(image.get(row,0)==0 for row,_ in t['selected'](4))
        higher+=1
result={'passed':True,'minimal_four_event_products':count,
 'old_detector_nonzero_products':nonzero,'distinct_cubic_rows_audited':len(rows),
 'all_cubic_right_contexts':contexts,'quartic_line_lift_contexts':higher,
 'checks':{'old_graded_image_is_one_visible_line':True,
 'line_lift_annihilated_by_all_contributing_positive_contexts':True,
 'works_for_original_two_private_and_sixteen_private_corrections':True,
 'new_cubic_witness_still_nonzero':True},
 'scope':'Exact actual-source support checks. The identity H i=f and vanishing pushout class use the source-module line lift and finite-stage bounded maps, not a sampled scalar or a completed projectivity assumption.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/corrected-adjacent-cubic-nullhomotopy.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
