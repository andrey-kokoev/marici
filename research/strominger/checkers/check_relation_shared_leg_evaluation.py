"""Explicit collapsed-quiver evaluation into the actual shared-leg algebra.

The free marked source is retained. This map does NOT factor through its
terminal recorder and does not assert a map of recorder-balanced seam complexes.
"""
import contextlib
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
import io
import json
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    a=runpy.run_path(str(ROOT/'research/strominger/checkers/check_generated_rung4_adapter.py'))
    r=runpy.run_path(str(ROOT/'research/strominger/checkers/check_relation_wg_packets.py'))
owner=a['owner']; arrows=a['arrows']; delta=a['delta']

def clean(d): return {k:v for k,v in d.items() if v}
def multiply(x,y):
    out=defaultdict(F)
    for u,c in x.items():
        for v,d in y.items(): out[u+v]+=c*d
    return clean(out)

@dataclass(frozen=True)
class Image:
    start: str
    end: str
    terms: tuple
    def column(self): return dict(self.terms)

class Evaluation:
    def __init__(self,events,left,right):
        self.events=tuple(events); self.left=tuple(left); self.right=tuple(right)
        assert set(left).isdisjoint(right) and len(left)==len(right)==2
        self.lmask=sum(1<<i for i in left); self.rmask=sum(1<<i for i in right)
    def obj(self,mask):
        if mask&self.lmask!=self.lmask: return 'A'
        return 'B' if mask&self.rmask==self.rmask else 'U'
    def generator(self,mask,event,marked):
        assert event in self.events and not mask&(1<<event)
        start,end=self.obj(mask),self.obj(mask|(1<<event))
        if start==end: path=()
        elif (start,end)==('A','U'): path=(f'ax{self.left.index(event)}',)
        elif (start,end)==('U','B'): path=(f'ay{self.right.index(event)}',)
        else:
            assert (start,end)==('A','B')
            path=('d',)
        if path:
            assert arrows[path[0]][:2]==(start,end)
        return {path:F(1,2) if marked else F(1)}
    def path(self,start,word,marks):
        image={():F(1)}; mask=start
        for event,marked in zip(word,marks):
            image=multiply(image,self.generator(mask,event,marked))
            mask|=1<<event
        return mask,image
    def apply(self,arrow):
        out=defaultdict(F)
        for (word,marks),c in arrow.terms:
            assert len(word)==len(marks)
            end,image=self.path(arrow.start,word,marks)
            assert end==arrow.end
            for path,d in image.items(): out[path]+=c*d
        result=Image(self.obj(arrow.start),self.obj(arrow.end),tuple(sorted(clean(out).items())))
        for path,c in result.terms:
            if not path: assert result.start==result.end
            else:
                assert arrows[path[0]][0]==result.start and arrows[path[-1]][1]==result.end
                assert all(arrows[x][1]==arrows[y][0] for x,y in zip(path,path[1:]))
        return result
    def product_law(self,x,y):
        assert x.end==y.start
        px,py=self.apply(x),self.apply(y)
        actual=self.apply(r['mul'](x,y))
        assert px.end==py.start
        assert actual.column()==multiply(px.column(),py.column())
        return actual

four=Evaluation(range(4),(0,1),(2,3))
x=four.apply(r['a4']); y=four.apply(r['b4']); v=four.product_law(r['a4'],r['b4'])
expected={('ax1','ay1'):F(1),('ax1','ay0'):F(-1),('ax0','ay1'):F(-1),('ax0','ay0'):F(1)}
checks={
    'left_relation_maps_to_actual_leg_difference':x.column()==delta(owner['word']('ah1')),
    'right_relation_maps_to_actual_leg_difference':y.column()==delta(owner['word']('ak1')),
    'actual_product_maps_to_nonzero_shared_leg_rectangle':v.column()==expected,
}
rectangle=next(rect for tag,i,j,fill,rect in a['rectangles'] if (tag,i,j)==('a',1,1))
checks['product_is_actual_DG_rectangle_boundary']=delta(rectangle)==v.column()
value=owner['evaluate'](v.column(),a['values'])
checks['displayed_matrix_detector_is_nonzero']=value==owner['scale'](F(1,15),owner['mul'](owner['K'],owner['H'])) and value!=owner['Z']
# Hence evaluation cannot factor through the old terminal recorder.
checks['evaluation_does_not_factor_terminal_observation']=not r['observe'](r['p4'].product) and bool(v.terms)

five=Evaluation(range(5),(0,1),(3,4))
for answer in r['answers']:
    r['verify'](answer)
    left=five.product_law(answer.left_cut.left,answer.left_cut.right)
    right=five.product_law(answer.right_cut.left,answer.right_cut.right)
    assert left==right and left.terms
    assert answer.left_cut.balanced==answer.right_cut.balanced
    assert answer.left_cut.raw!=answer.right_cut.raw
checks['eight_balanced_source_cases_have_equal_nonzero_target_products']=True

@dataclass(frozen=True)
class EvaluatedAnswer:
    source_answer: object
    left_product: Image
    right_product: Image

def bind_answer(answer):
    r['verify'](answer)
    left=five.product_law(answer.left_cut.left,answer.left_cut.right)
    right=five.product_law(answer.right_cut.left,answer.right_cut.right)
    assert left==right
    return EvaluatedAnswer(answer,left,right)
evaluated_answers=tuple(bind_answer(answer) for answer in r['answers'])
checks['evaluated_answers_retain_both_source_cuts_and_seams']=all(
    result.source_answer is original and result==bind_answer(result.source_answer)
    for result,original in zip(evaluated_answers,r['answers']))

images=(x,y,v)
for j,image in enumerate(images):
    mapped_action=defaultdict(F)
    for i,basis_image in enumerate(images):
        for path,c in basis_image.terms:
            mapped_action[path]+=r['actual_action'][i][j]*c
    target_action=multiply(image.column(),y.column()) if image.end==y.start else {}
    assert clean(mapped_action)==target_action
checks['actual_cross_layer_right_action_intertwines']=True

# Exhaustive length-two composability checks on both small source cubes.
local_checks=0
for evaluator in (four,five):
    for mask in range(1<<len(evaluator.events)):
        for i in evaluator.events:
            if mask&(1<<i): continue
            for j in evaluator.events:
                if j==i or mask&(1<<j): continue
                for mi in (0,1):
                    for mj in (0,1):
                        left=r['arrow'](mask,{((i,),(mi,)):1})
                        right=r['arrow'](mask|(1<<i),{((j,),(mj,)):1})
                        evaluator.product_law(left,right); local_checks+=1
checks['typed_generator_composition_checks']=local_checks>0

# Strict positive-path candidate fails for structural reasons: J^3=0.
positive=[(name,) for name,(_,_,degree) in arrows.items() if degree==0]
length_two=[p+q for p in positive for q in positive if arrows[p[-1]][1]==arrows[q[0]][0]]
length_three=[p+q for p in length_two for q in positive if arrows[p[-1]][1]==arrows[q[0]][0]]
checks['strict_positive_path_evaluation_cannot_preserve_four_event_product']=bool(length_two) and not length_three

# A graph-of-evaluation packet is tied by an equation, not an unrelated tuple.
@dataclass(frozen=True)
class Bound:
    source: object
    image: Image
    matrix: tuple

def bind(source,evaluator):
    image=evaluator.apply(source)
    return Bound(source,image,owner['evaluate'](image.column(),a['values']))
def verify(packet,evaluator): assert packet==bind(packet.source,evaluator)
packet=bind(r['p4'].product,four); verify(packet,four)
try: verify(Bound(packet.source,Image('A','B',()),owner['Z']),four)
except AssertionError: checks['unrelated_or_zero_target_attachment_rejected']=True
else: raise AssertionError('erasing target passed')
assert all(checks.values())
out={'schema':'marici.relation-shared-leg-evaluation.v1','status':'pass','checks':checks,
     'local_generator_composition_cases':local_checks,
     'generator_policy':{'objects':'A until left pair complete; U until right pair complete; B thereafter',
        'same_object_edges':'identity path','crossings':'ax0/ax1, ay0/ay1, or d for A->B',
        'mark0_coefficient':'1','mark1_coefficient':'1/2','middle_event':'scalar identity'},
     'actual_product_image':{','.join(k):str(c) for k,c in v.terms},
     'matrix_image':[[str(c) for c in row] for row in value],
     'remaining_scope':'retained free-path evaluation and product balancing, not yet induced recorder-balanced seam-complex map or whole continuation-policy assembly'}
(ROOT/'research/strominger/results/relation-shared-leg-evaluation-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
