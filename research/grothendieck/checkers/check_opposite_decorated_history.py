"""Exact opposite-category reversal; no source arrow inversion is asserted."""
from pathlib import Path
from itertools import permutations,product
from collections import Counter
from dataclasses import replace
import importlib.util
import sys
import json
ROOT=Path(__file__).resolve().parents[3]
def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'research/grothendieck'/file)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
h=load('endpoint','endpoint_decorated_history.py')
o=load('opposite','opposite_decorated_history.py')
t=load('jets','universal_history.py')
a=load('source','theta_interval_signature.py')

def lift(w):return tuple(replace(w,retained=bits) for bits in product((False,True),repeat=len(w.events)))
def extract(w):return replace(w,retained=(True,)*len(w.events)) if all(w.retained) else None
def coefficient(w):
    out=t.Jet.unit(4)
    for s,z,keep in zip(w.vertices,w.vertices[1:],w.retained):
        if keep:
            lo,hi=(s,z) if w.direction==1 else (z,s)
            out=out*t.Jet(4,{(j,):1 for j in range(a.POSITION[lo],a.POSITION[hi])})
    return out

def dagger(jet):return t.Jet(jet.order,{word[::-1]:c.conjugate() for word,c in jet.terms.items()})

routes=histories=cuts=0
for start in range(16):
    remaining=[j for j in range(4) if not start>>j&1]
    for length in range(len(remaining)+1):
        for word in permutations(remaining,length):
            routes+=1
            w=o.OrientedHistory.from_forward(h.History(start,word,(True,)*length))
            assert Counter(x.reverse() for x in lift(w))==Counter(lift(w.reverse()))
            for x in lift(w):
                histories+=1;y=x.reverse()
                assert y.reverse()==x and y.vertices==x.vertices[::-1]
                assert extract(y)==(extract(x).reverse() if extract(x) is not None else None)
                gaps,events=x.gaps();rgaps,revents=y.gaps()
                assert rgaps==tuple(g.reverse() for g in gaps[::-1])
                assert revents==tuple(e.reverse() for e in events[::-1])
                assert coefficient(y)==dagger(coefficient(x))
                # Gaussian-integer scalar checks the conjugate-linear extension.
                assert dagger(coefficient(x).scale(2+3j))==coefficient(y).scale(2-3j)
                for j in range(length+1):
                    cuts+=1;l,r=x.cut(j)
                    assert y.cut(length-j)==(r.reverse(),l.reverse())
                    assert r.reverse().join(l.reverse())==y
                    # A source cut keeps the same arithmetic vertex after reversal.
                    assert y.vertices[length-j]==x.vertices[j]
# Opposite routes cannot be admitted as forward transitions with the same endpoints.
x=o.OrientedHistory.from_forward(h.History(0,(0,1),(False,True))).reverse()
try:replace(x,direction=1)
except ValueError:pass
else:raise AssertionError('Opposite route silently treated as forward arithmetic')
# Zero-step identities still belong to their declared orientation categories.
try:o.OrientedHistory((0,),(),(),1).join(o.OrientedHistory((0,),(),(),-1))
except ValueError:pass
else:raise AssertionError('Mixed orientation categories composed implicitly')
result={'schema':'marici.grothendieck.opposite-decorated-history.v1','passed':True,
        'source_routes':routes,'marked_histories':histories,'typed_cuts':cuts,
        'checks':{'involution_between_opposite_categories':True,'marks_and_gap_reversal':True,
                  'marked_lift_and_extraction_squares':True,'cut_flip_with_same_vertex':True,
                  'coefficient_dagger_and_conjugate_linearity':True,
                  'wrong_forward_typing_rejected':True},
        'scope':'Structural path/opposite comparison only. No inverse arithmetic arrow, Hilbert adjoint, or analytic source identification.'}
p=ROOT/'research/grothendieck/results/opposite-decorated-history.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
