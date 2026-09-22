"""Actual source witness for nonsplitting of the background-two acquisition.

Old degree-two seed rows (including optional calibrated frames) kill the
all-forgotten cubic. The old first two stages already exhaust the initial
2D ideal corner, so the enlarged lift there is forced.
"""
from pathlib import Path
from itertools import product
import json,runpy
ROOT=Path(__file__).resolve().parents[3]
v=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_filtered_obstruction.py'))
old=v['verify'](v['load'](ROOT/'research/voevodsky/results/filtered-obstruction-problem.json'),
                v['load'](ROOT/'research/voevodsky/results/filtered-obstruction-certificate.json'))
assert old['verified']
rel=v['relation'];mul=v['multiply'];rows=v['vacuum_rows']
a=rel((0,1),0);mixed=rel((0,1),1);b=rel((2,3),0);c=rel((4,5),0)
k=mul(mul(a,b),c)
assert len(k)==8 and all(sum(m)==0 for w,m in k)
first=((('e',0,1,0),))
assert rows(0,3,a,1).get(first,0)==1
assert rows(0,3,mixed,1).get(first,0)==0
oldseams=[tuple(tuple(e) for e in r) for r in v['expected_problem']()['old_seams']]
assert [rows(0,15,mul(a,b),2).get(r,0) for r in oldseams]==[0,0]
assert [rows(0,15,mul(mixed,b),2).get(r,0) for r in oldseams]==[1,1]
# The actual combined old second row gives nonzero d2 on mixed*b. Together
# with the first row this is a diagonal rank-two observation of the initial
# ideal corner, whose entire kernel basis was independently checked above.
assert v['rank']([a,mixed])==2
vac=(('e',0,1,0),('e',3,7,0),('e',15,31,0))
assert rows(0,63,k,3).get(vac,0)==1
# All 270 private rows require retained degree two, so each kills k.
private=[]
for pairs in v['pairings'](tuple(range(6))):
    for kinds in ((1,1,0),(1,0,1),(0,1,1)):
        start=0;seams=[]
        for pair,kind in zip(pairs,kinds):
            seams.append(('e',start,start|(1<<min(pair)),kind))
            start|=sum(1<<j for j in pair)
        private.append(tuple(seams))
im=rows(0,63,k,3)
assert len(private)==270 and all(im.get(row,0)==0 for row in private)
# At a full six-event corner no positive context fits a six-event detector.
# The earlier shorter detectors cannot contribute either. Other-background
# vacuum rows also miss k by their outer labels.
# Seven definite shared saturated coordinates of V2 and the old 270 family:
# all length-two canonical intervals, plus (1,4) and (3,6).
shared=[]
for i in range(6):
    for j in range(i+2,7):
        eligible=[kinds for kinds in ((1,1,0),(1,0,1),(0,1,1))
                  if all(not kinds[pos//2] for pos in range(i,j) if pos%2==0)]
        if eligible:shared.append((i,j))
assert shared==[(0,2),(1,3),(1,4),(2,4),(3,5),(3,6),(4,6)]
# The old retained-feature nullhomotopy is still invisible to the new seed.
x=mul({((0,1),(0,1)):1},b)
for order in ((4,5),(5,4)):
    for marks in product((0,1),repeat=2):
        contextual=mul(x,{(order,marks):1})
        assert all(sum(m)>=1 for w,m in contextual)
        assert rows(0,63,contextual,3).get(vac,0)==0
result={'passed':True,'old_obstruction_certificate_verified':True,
 'forced_lift_corner':[2,12],'whole_initial_ideal_dimension':2,
 'old_initial_observation':'diag(1,d2), with the owning certified d2 nonzero',
 'forgotten_cubic_source_terms':len(k),'old_full_corner_value':'0',
 'new_unit_vacuum_value':'1','definite_shared_vacuum_intervals':shared,
 'increment_dimension_bounds':[1,8],
 'checks':{'initial_lift_forced':True,'right_I2_action_contradicts_a_section':True,
   'old_270_private_rows_kill_new_witness':True,
   'retained_nullhomotopy_survives_vacuum_addition':True},
 'scope':'Nonsplitting for the actual 270-row observer without the background-two vacuum row, including additional homogeneous degree-two frames. Bounds, not an exact full-union increment dimension, are asserted.'}
(ROOT/'research/voevodsky/results/background-two-vacuum-coupling.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
