"""Distinguish presentation aliases from fresh retained traversal events.

Event identity is supplied explicitly. Repeated references to one ID do not
create events; a fresh traversal has a new ID even with identical label data.
Compare raw reference sums, unique-event sums, and unique-event averages.
"""
from fractions import Fraction as F
from pathlib import Path
import json

registry = {'a':(1,0,0,0), 'b':(0,1,0,0),
            'a_new':(1,0,0,0), 'b_new':(0,1,0,0)}


def vector(refs, unique=False, average=False):
    ids = list(dict.fromkeys(refs)) if unique else list(refs)
    result = tuple(sum(F(registry[i][j]) for i in ids) for j in range(4))
    return tuple(v/len(ids) for v in result) if average else result


def spatial(v):
    common = sum(v)/4
    return tuple(x-common for x in v)


def difference_squared(a,b):
    # G4=10I+J on spatial contrasts, in squared seed-edge units20.
    d = tuple(x-y for x,y in zip(spatial(a),spatial(b)))
    assert sum(d)==0
    return sum(x*x for x in d)/2


base = ('a','b')
alias = ('a','b','a')  # repeated reference to existing event a
fresh = ('a','b','a_new')
replay = ('a','b','a_new','b_new')  # fresh replay of both events
assert set(alias)==set(base)
assert len(set(fresh))==3 and len(set(replay))==4
assert registry['a']==registry['a_new']

rules = {'raw_reference_sum':{},
         'unique_event_sum':{'unique':True},
         'unique_event_average':{'unique':True,'average':True}}
results = {}
for name, options in rules.items():
    initial = vector(base,**options)
    changes = {case:str(difference_squared(vector(refs,**options),initial))
               for case,refs in [('alias',alias),('fresh_event',fresh),('fresh_full_replay',replay)]}
    results[name] = changes
assert results['raw_reference_sum']['alias']!='0'
assert results['unique_event_sum']['alias']=='0'
assert results['unique_event_average']['alias']=='0'
assert results['unique_event_sum']['fresh_full_replay']!='0'
assert results['unique_event_average']['fresh_full_replay']=='0'
assert vector(replay,unique=True)==tuple(2*x for x in vector(base,unique=True))
assert vector(replay,unique=True,average=True)==vector(base,unique=True,average=True)
# Averaged location plus event count still recovers the additive vector exactly.
for refs in (base,alias,fresh,replay):
    count = len(set(refs))
    assert tuple(count*x for x in vector(refs,unique=True,average=True))==vector(refs,unique=True)

report = {'status':'passed','squared_spatial_readout_changes':results,
          'unique_event_counts':{'base':2,'alias':2,'fresh_event':3,'fresh_full_replay':4},
          'conclusion':'Naive reference summation is presentation-dependent. Both event-aware sum and average ignore aliases. A new full replay changes the sum and event count but leaves the average fixed. Average plus count is lossless for the summed vector; event histories themselves remain retained separately.',
          'scope':'The test distinguishes event identity from presentation multiplicity. It does not force event count to be a physical distance or proper-time scale.'}
HERE = Path(__file__).resolve().parents[1]
(HERE/'results/readout-event-identity.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
