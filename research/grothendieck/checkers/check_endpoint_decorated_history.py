"""Exact faithful marked lift, source coproduct, and coefficient projection."""
from pathlib import Path
from itertools import permutations
from collections import Counter
import importlib.util
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
def load(name,filename):
    spec=importlib.util.spec_from_file_location(name,ROOT/'research/grothendieck'/filename)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    return module
h=load('decorated','endpoint_decorated_history.py')
t=load('universal','universal_history.py')
a=load('signature','theta_interval_signature.py')

def coefficient(history):
    out=t.Jet.unit(4)
    for index,keep in enumerate(history.retained):
        if keep:
            left,right=history.vertices[index:index+2]
            out=out*t.Jet(4,{(j,):1 for j in range(a.POSITION[left],a.POSITION[right])})
    return out

route_count=history_count=cut_count=0
for start in range(16):
    unused=[j for j in range(4) if not start>>j&1]
    for length in range(len(unused)+1):
        for word in permutations(unused,length):
            route_count+=1
            lift=h.marked_lift(start,word)
            # All-retained projection is a linear left inverse of the lift.
            assert [(x.start,x.word) for x in lift if all(x.retained)]==[(start,word)]
            total=t.Jet(4,{})
            lhs=Counter();rhs=Counter()
            for x in lift:
                history_count+=1
                assert h.History.from_gaps(*x.gap_normal_form())==x
                assert x.labels[0]==a.LABELS[start]
                total=total+coefficient(x)
                for j in range(length+1):
                    left,right=x.cut(j);cut_count+=1
                    assert left.end==right.start and left.join(right)==x
                    lhs[(left,right)]+=1
                # Coassociativity with complete intermediate endpoints retained.
                dleft=Counter();dright=Counter()
                for j in range(length+1):
                    l,r=x.cut(j)
                    for i in range(j+1):
                        ll,lr=l.cut(i);dleft[(ll,lr,r)]+=1
                    for i in range(length-j+1):
                        rl,rr=r.cut(i);dright[(l,rl,rr)]+=1
                assert dleft==dright
            route=h.History(start,word,(True,)*length)
            for j in range(length+1):
                l,r=route.cut(j)
                left_lift=h.marked_lift(l.start,l.word)
                right_lift=h.marked_lift(r.start,r.word)
                assert Counter(x.join(y) for x in left_lift for y in right_lift)==Counter(lift)
                for x in left_lift:
                    for y in right_lift:rhs[(x,y)]+=1
            # Delta decorated(lift w) = (lift tensor lift) Delta source(w).
            assert lhs==rhs
            expected={word:c for row in a.observe_route(word,start) for word,c in row.items()}
            assert total==t.Jet(4,expected)
# Full forgotten paths with the same terminal integer are still distinct.
x=h.History(0,(0,1),(False,False));y=h.History(0,(1,0),(False,False))
assert x!=y and x.end==y.end and x.labels[-1]==12
assert x.labels==(2,4,12) and y.labels==(2,6,12)
assert coefficient(x)==coefficient(y)==t.Jet.unit(4)
assert x.gap_normal_form()!=y.gap_normal_form()
try:h.History(0,(),()).join(h.History(1,(),()))
except ValueError:pass
else:raise AssertionError('Mismatched endpoints accepted')
result={'schema':'marici.grothendieck.endpoint-decorated-history.v1','passed':True,
        'source_routes':route_count,'marked_histories':history_count,'typed_cuts':cut_count,
        'checks':{'gap_normal_form_roundtrip':True,'typed_cut_join':True,
                  'coassociative_typed_cuts':True,'marked_lift_preserves_composition':True,
                  'marked_lift_preserves_source_coproduct':True,
                  'all_retained_left_inverse':True,'coefficient_projection_matches_existing_signature':True,
                  'forgotten_routes_to_twelve_remain_distinct':True,'invalid_attachment_rejected':True},
        'scope':'Finite typed source and marked path coalgebra. Coefficient projection alone is not a source-coalgebra equivalence.'}
p=ROOT/'research/grothendieck/results/endpoint-decorated-history.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
