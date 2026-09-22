"""Clock-free operation and rational refinement invariance.

Exact finite tensor-series model. A/B are noncommuting generator directions.
A unit source operation is exp(A) or exp(B); splitting an operation into
exp(A/n)^n preserves it. Degree-four truncation bounds retained information,
not time. No physical minimum time or action quantum is assumed.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
DEGREE=4

def clean(x):return {w:c for w,c in x.items() if c}
def multiply(x,y):
    out={}
    for u,a in x.items():
        for v,b in y.items():
            if len(u)+len(v)<=DEGREE:out[u+v]=out.get(u+v,Q(0))+a*b
    return clean(out)
def segment(event,amount=Q(1)):
    return {(event,)*k:amount**k/Q(factorial(k)) for k in range(DEGREE+1) if amount**k}
def signature(events):
    out={():Q(1)}
    for event,amount in events:out=multiply(out,segment(event,amount))
    return out
def coarse(x,depth):return {w:c for w,c in x.items() if len(w)<=depth}
def residual(x,depth):return {w:c for w,c in x.items() if len(w)>depth}
def restore(view,tail):
    assert not set(view)&set(tail)
    return dict(view)|tail

def emit(word,n):return [(event,Q(1,n)) for event in word for _ in range(n)]
def action(events):return sum((abs(amount) for event,amount in events),Q(0))
def frozen(sig):return tuple(sorted(sig.items()))
words=[''.join(w) for length in range(5) for w in product('AB',repeat=length)]
# No time coordinate enters any source, composition, observation or residual.
seen={};roundtrips=0
for word in words:
    sig=signature(emit(word,1))
    assert frozen(sig) not in seen;seen[frozen(sig)]=word
    for depth in range(DEGREE+1):
        assert restore(coarse(sig,depth),residual(sig,depth))==sig
        roundtrips+=1
composition=0
for u in words:
    for v in words:
        assert multiply(signature(emit(u,1)),signature(emit(v,1)))==signature(emit(u+v,1))
        composition+=1
# Positive charges are additive in operation amount, not charged once per
# arbitrary microstep. Refinement therefore does not secretly add action.
refinement=0
for word in words:
    original=signature(emit(word,1))
    for n in (2,4,8,16):
        refined=emit(word,n)
        assert signature(refined)==original
        assert action(refined)==action(emit(word,1))
        for depth in range(DEGREE+1):
            assert coarse(signature(refined),depth)==coarse(original,depth)
        refinement+=1
# Nonuniform rational subdivision also preserves a single operation.
for event in 'AB':
    assert signature([(event,Q(1,7)),(event,Q(2,7)),(event,Q(4,7))])==segment(event)
# Cycle boundaries remain boundaries of the declared source protocol, not
# a count of implementation microsteps.
for word in ('AB','BA'):
    expected=signature(emit(word,1));elapsed_action=Q(0)
    refined=[]
    for event in word:
        refined.extend([(event,Q(1,8))]*8)
        elapsed_action+=1
        assert action(refined)==elapsed_action
        assert signature(refined)==signature(emit(word[:len(refined)//8],1))
    assert signature(refined)==expected
# Negative controls: changing order is NOT a refinement of the same source.
ab=signature(emit('AB',1));ba=signature(emit('BA',1))
assert coarse(ab,1)==coarse(ba,1) and ab!=ba
assert ab.get(('A','B'),0)-ab.get(('B','A'),0)==1
assert ba.get(('A','B'),0)-ba.get(('B','A'),0)==-1
interleaved=signature([('A',Q(1,2)),('B',Q(1,2)),('A',Q(1,2)),('B',Q(1,2))])
assert interleaved!=ab
# Recording raw microstep counts creates an artificial refinement failure.
assert len(emit('AB',1))==2 and len(emit('AB',8))==16
# Charging a fixed positive action per microstep likewise breaks invariance.
assert Q(1,2)*len(emit('AB',1))!=Q(1,2)*len(emit('AB',8))

report={'passed':True,'model':'degree-four noncommutative tensor series; source operations exp(A), exp(B)',
 'clock_free':{'timestamps_used':False,'histories_separated_up_to_length':4,
               'distinct_bounded_histories':len(seen),'residual_roundtrips':roundtrips,
               'composition_checks':composition},
 'refinement':{'uniform_factors':[2,4,8,16],'uniform_checks':refinement,
               'nonuniform_partition':['1/7','2/7','4/7'],
               'same_operation_same_action_same_observer_records':True},
 'negative_controls':{'reordering_changes_source':True,'interleaving_not_mistaken_for_subdivision':True,
                      'microstep_count_is_not_refinement_invariant':True,
                      'fixed_charge_per_microstep_is_not_refinement_invariant':True},
 'conclusion':'This finite algebraic system operates without timestamps or a minimum tick. Arbitrarily fine rational subdivision is compatible with composition and retained order when it represents the same operation.',
 'limits':['Algebraic countermodel, not a physical clock or receiver implementation.',
           'Order-four records are not asserted faithful for unrestricted histories.',
           'No finite-resource or noisy discrimination claim.',
           'No conclusion about whether physical spacetime is discrete or about Planck time.']}
(ROOT/'research/voevodsky/results/clock-free-refinement.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
