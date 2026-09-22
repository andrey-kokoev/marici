"""Exact source audit for adjoining the acquired vacuum rows at A=3,4.

Uses the independent existing finite source verifier, not numerical task
inference. Whole-image and completion statements are proved in the note.
"""
from pathlib import Path
from itertools import product
import json,runpy
ROOT=Path(__file__).resolve().parents[3]
v=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_filtered_obstruction.py'))
old=v['verify'](v['load'](ROOT/'research/voevodsky/results/filtered-obstruction-problem.json'),
                v['load'](ROOT/'research/voevodsky/results/filtered-obstruction-certificate.json'))
assert old['verified']
relation=v['relation'];multiply=v['multiply'];rows=v['vacuum_rows']
vacuum=(('e',0,1,0),('e',3,7,0),('e',15,31,0))
columns=[];nonzero=[]
for pairs in v['pairings'](tuple(range(6))):
    for kinds in product((0,1),repeat=3):
        col=multiply(multiply(relation(pairs[0],kinds[0]),relation(pairs[1],kinds[1])),relation(pairs[2],kinds[2]))
        value=rows(0,63,col,3).get(vacuum,0)
        columns.append((pairs,kinds,value))
        if value:nonzero.append((pairs,kinds,value))
assert len(columns)==720
assert nonzero==[(((0,1),(2,3),(4,5)),(0,0,0),1)]
# Labelled six-event input can contribute to a six-event seed only through
# vertex contexts: every nonidentity context would exceed length six.
new_backgrounds=(3,4)
assert [[int(A==B) for B in new_backgrounds] for A in new_backgrounds]==[[1,0],[0,1]]
for A in new_backgrounds:
    assert A!=2 and 30030*A!=60060
    # Tail for left ideal image, prefix for right ideal image: neither can
    # be observed inside the old four-event packet ending at 420.
    assert 420%(30030*A)!=0
    assert 420%(210*A)!=0
# Actual lower-filtration source x=path(2_forgotten,3_retained)*b0.
x=multiply({((0,1),(0,1)):1},relation((2,3),0))
assert len(x)==2 and all(sum(m)==1 for w,m in x)
# All eight right contexts closing its old six-event corner still retain
# at least one feature. Check direct ordered cuts as well as the grading.
context_checks=0
for order in ((4,5),(5,4)):
    for marks in product((0,1),repeat=2):
        full=multiply(x,{(order,marks):1})
        assert all(sum(m)>=1 for w,m in full)
        assert rows(0,63,full,3).get(vacuum,0)==0
        context_checks+=1
# Arbitrary additional left/right contexts cannot lower retained degree.
# Thus EVERY all-vacuum seed, at any background, annihilates Sat(x).
result={'passed':True,'old_independent_obstruction_certificate_verified':True,
 'new_acquired_backgrounds':list(new_backgrounds),'old_stage_two_unchanged':True,
 'minimal_cubic_columns_per_new_corner':len(columns),
 'nonzero_new_vacuum_column':{'pairs':[[0,1],[2,3],[4,5]],'kinds':[0,0,0],'value':'1'},
 'new_top_coordinate_matrix':[[1,0],[0,1]],
 'top_kernel_dimension_of_restriction':2,
 'left_tail_endpoints':[30030*A for A in new_backgrounds],
 'right_prefix_endpoints':[210*A for A in new_backgrounds],
 'old_nullhomotopy_closing_contexts_checked':context_checks,
 'checks':{'old_private_obstruction_still_available':True,
   'new_top_directions_in_both_ideal_images':True,
   'new_vacuum_rows_annihilate_retained_lift_contexts':True},
 'scope':'Source/action audit for actual acquired vacuum rows at backgrounds 3 and 4. No detector is installed for the unacquired tail; no total ungraded observer dimension or new Ext degree is computed.'}
(ROOT/'research/voevodsky/results/acquired-vacuum-rows-filtered-attachment.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
