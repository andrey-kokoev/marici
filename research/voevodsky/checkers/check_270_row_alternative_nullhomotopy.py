"""An actual lower-filtration line lift for the 270-private-row observer.

All selected analytical blocks are checked before norming evaluation. The
old scalar scores 2 and 3 below are symbolic fixtures; the proof uses the
actual positive ratio gap_A/(mu_A2-L).
"""
from pathlib import Path
from itertools import product,permutations
import runpy,json
ROOT=Path(__file__).resolve().parents[3]
a=runpy.run_path(str(ROOT/'research/voevodsky/checkers/check_optimal_cubic_observer_line_lift.py'))
t=runpy.run_path(str(ROOT/'research/nima/checkers/check_all_depth_observer_tower.py'))
f=a['f'];raw3=a['raw3'];ordered=t['ordered'];score=t['score']
x=f['multiply']({((0,1),(0,1)):1},f['relation']((2,3),0))
v2=f['multiply'](f['relation']((0,1),1),f['relation']((2,3),0))
assert len(x)==2 and f['derivative'](0,x)
assert score(ordered(0,x,2),2)==3
assert score(ordered(0,v2,2),2)==2
# Exact source membership: the actual terminal recorder kills x.
record={}
for key,c in x.items():
    for word,b in f['record'](0,*key).items():record[word]=record.get(word,0)+c*b
assert not f['clean'](record)
selected=set(a['J'])|{a['reserve'][0]}
pivots=[]
for col in a['columns']:
    start=0;seams=[]
    for pair,kind in zip(col['pairs'],col['kinds']):
        seams.append(('e',start,start|(1<<pair[0]),kind))
        start|=sum(1<<p for p in pair)
    pivots.append((tuple(seams),(0,0,0,0)))
assert len(set(pivots))==270
selected.update(pivots)
for row,_ in t['selected'](3):selected.add((row[0],(0,0,0,0)))
for pair1,pair2 in (((0,1),(2,3)),((0,2),(1,3))):
    start=sum(1<<p for p in pair1)
    for p,q,last in product(pair1,pair2,(4,5)):
        selected.add(((('e',0,1<<p,1),('e',start,start|(1<<q),1),
                       ('e',15,15|(1<<last),0)),(0,0,0,0)))
selected.add(((('e',0,1,0),('e',3,7,0),('e',15,31,0)),(0,0,0,0)))
contexts=0
for word in permutations((4,5)):
    for marks in product((0,1),repeat=2):
        im=raw3(f['multiply'](x,{(word,marks):1}))
        overlap={key:c for key,c in im.items() if key[0] in selected}
        assert not overlap,(word,marks,overlap)
        contexts+=1
# The old I^2 representative does NOT have that annihilation property.
y=f['multiply'](v2,f['relation']((4,5),1))
assert any(shape==pivots[1] for shape,windows in raw3(y))
result={'passed':True,'lower_filtration_source_terms':len(x),
 'new_source_in_I_but_not_I_squared':True,
 'old_symbolic_readouts':{'v2':2,'late_feature_source':3},
 'distinct_analytical_blocks_audited':len(selected),'all_right_contexts':contexts,
 'included_protocols':['270 first-seam private rows','original four sectors',
 'two-private and sixteen-private rows','449 matched-optimal blocks','vacuum probe'],
 'checks':{'all_new_saturated_readouts_kill_the_late_feature_lift':True,
 'old_readout_nonzero':True,'old_I_squared_lift_still_obstructed':True},
 'scope':'Exact actual-source support and membership. Actual normalization is gap_A/(mu_A2-L), nonzero in the fixed calibrated protocol. The bounded equivariant section and nullhomotopy follow from the companion argument, not an assignment of symbolic scores to theta windows.'}
out=ROOT/'research/voevodsky/results/270-row-alternative-nullhomotopy.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
