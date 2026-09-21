"""Exact jet-tower, inverse, and universal-evaluation regressions."""
import importlib.util
from pathlib import Path
from fractions import Fraction as F
from math import prod
import json
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('universal_history',ROOT/'research/grothendieck/universal_history.py')
h=importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name]=h;spec.loader.exec_module(h)
# Noncommuting two-generator histories, checked independently at each order.
windows=[{0:1,1:F(1,2)},{1:1},{0:-1}]
for n in range(9):
    x=h.record(n,windows)
    inv=x.inverse()
    assert x*inv==inv*x==h.Jet.unit(n)
    if n:
        assert x.project(n-1)==h.record(n-1,windows)
        assert inv.project(n-1)==h.record(n-1,windows).inverse()
    a=h.record(n,[{0:1}]);b=h.record(n,[{1:1}]);c=h.record(n,[{0:1,1:1}])
    assert (a*b)*c==a*(b*c)
    assert (a.inverse()*b)*(b.inverse()*c)==a.inverse()*c
# Infinite inverse is not silently truncated at degree four.
x=h.record(8,[{0:1}]).inverse()
assert x.terms[(0,)*8]==1 and x.terms[(0,)*5]==-1
# A commutative formal-series target: send each letter j to coefficient a_j*t.
# At jet order n this evaluation is finite and multiplication must commute.
def eval_series(jet,coefficients):
    out=[F(0)]*(jet.order+1)
    for word,c in jet.terms.items():out[len(word)]+=c*prod(coefficients[j] for j in word)
    return out

def conv(a,b):return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(len(a))]
for n in range(9):
    a=h.record(n,windows[:2]);b=h.record(n,windows[2:])
    assert eval_series(a*b,{0:F(2),1:F(-3)})==conv(eval_series(a,{0:F(2),1:F(-3)}),eval_series(b,{0:F(2),1:F(-3)}))
# Universal receiver retains order that a commutative target forgets.
ab=h.record(2,[{0:1},{1:1}]);ba=h.record(2,[{1:1},{0:1}])
assert ab!=ba and eval_series(ab,{0:F(2),1:F(3)})==eval_series(ba,{0:F(2),1:F(3)})
# Deconcatenation is coassociative; its mixed law counts the join once.
def cuts(word):return {(word[:j],word[j:]):F(1) for j in range(len(word)+1)}
u,v=(0,1),(1,0)
joined=cuts(u+v)
rhs={}
for (a,b),c in cuts(v).items():rhs[(u+a,b)]=rhs.get((u+a,b),0)+c
for (a,b),c in cuts(u).items():rhs[(a,b+v)]=rhs.get((a,b+v),0)+c
rhs[(u,v)]-=1
assert {k:v for k,v in rhs.items() if v}==joined
left={};right={}
for (a,b),c in joined.items():
    for (x,y),d in cuts(a).items():left[(x,y,b)]=left.get((x,y,b),0)+c*d
    for (x,y),d in cuts(b).items():right[(a,x,y)]=right.get((a,x,y),0)+c*d
assert left==right
# Long histories are handled by the same construction, without four-step bound.
assert h.record(6,[{0:1}]*6).terms[(0,)*6]==1
try:h.Jet.unit(2).project(3)
except ValueError:pass
else:raise AssertionError('projection invented higher data')
result={'schema':'marici.grothendieck.full-universal-history.v1','passed':True,
        'tested_orders':list(range(9)),
        'checks':{'associativity':True,'two_sided_inverse':True,'jet_projection':True,
                  'inverse_projection':True,'comparison_cocycle':True,
                  'formal_series_universal_evaluation':True,'higher_inverse_terms_retained':True,
                  'commutative_receiver_can_lose_order':True,'six_event_history':True,
                  'coassociative_record_cuts':True,'cut_join_compatibility':True},
        'scope':'Exact finite jets through eight. All-order universal property is proved in the companion note.'}
p=ROOT/'research/grothendieck/results/full-universal-history.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
