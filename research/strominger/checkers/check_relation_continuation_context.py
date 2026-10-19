"""Explicit gain/drift context for the retained source evaluation graph.

The target DG substitution changes WITH a retained context matrix; no fixed
four-leg-image invariance or faithful numerical detector is presumed.
"""
import contextlib
from collections import defaultdict
from dataclasses import dataclass
import io
import json
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    e=runpy.run_path(str(ROOT/'research/strominger/checkers/check_energy_continuation_instance.py'))
    p=runpy.run_path(str(ROOT/'research/strominger/checkers/check_relation_shared_leg_evaluation.py'))
S=e['S']; control=e['control']; a=p['a']; owner=p['owner']; r=p['r']
P=control['P']; Q=control['Q']; D=control['model']['Q']; I=S.eye(11)
assert P+Q==I

def clean(chain): return {k:S.simplify(v) for k,v in chain.items() if v!=0}
def add_scaled(out,chain,c):
    for word,v in chain.items(): out[word]+=c*v

def generator_images(C):
    assert all(sum(C[i,j] for j in range(11))==1 for i in range(11))
    images={}
    for name in a['arrows']:
        if name=='d' or name.startswith('s'):
            images[name]={(name,):S.Integer(1)}
        elif name=='abase':
            out=defaultdict(lambda:S.Integer(0))
            for i in range(11):
                for j in range(11):
                    add_scaled(out,a['routes']('a',i,j)[0],C[0,i]*C[0,j])
            images[name]=clean(out)
        else:
            role=name[1]; i=int(name[2:])
            if role in ('x','y'):
                images[name]=clean({(f'a{role}{j}',):C[i,j] for j in range(11)})
            else:
                assert role in ('h','k')
                images[name]=clean({(f'a{role}{j}',):C[i,j]-C[0,j] for j in range(1,11)})
    return images

def substitute(chain,images):
    out=defaultdict(lambda:S.Integer(0))
    for word,c in chain.items():
        image={():S.Integer(1)}
        for name in word: image=p['multiply'](image,images[name])
        add_scaled(out,image,c)
    return clean(out)

def matrix_for(command):
    kind,q=command
    if kind=='drift':
        assert q is None
        return D
    assert kind=='gain' and q>=0 and q<=1
    return P+q*Q

def assignment(C):
    values=dict(a['values'])
    for role in ('x','y'):
        for i in range(11):
            total=owner['Z']
            for j in range(11): total=owner['add'](total,owner['scale'](C[i,j],a['values'][f'a{role}{j}']))
            values[f'a{role}{i}']=total
    return values

@dataclass(frozen=True)
class ContextPacket:
    source: object
    context: object
    symbolic: dict
    matrix: tuple
    parent: object = None
    command: object = None

def bind(source,C,parent=None,command=None):
    image=substitute(p['four'].apply(source).column(),generator_images(C))
    value=owner['evaluate'](image,a['values'])
    assert value==owner['evaluate'](p['four'].apply(source).column(),assignment(C))
    return ContextPacket(source,S.ImmutableMatrix(C),image,value,parent,command)

def step(packet,command):
    return bind(packet.source,matrix_for(command)*packet.context,packet,command)

checks={}
contexts=[I,P+S.Rational(1,2)*Q,P+S.Rational(1,4)*Q,P,D]
dg_checks=0
for C in contexts:
    images=generator_images(C)
    for name in a['arrows']:
        assert a['delta'](images[name])==substitute(a['delta'](owner['word'](name)),images)
        dg_checks+=1
    # Products and both cuts commute with the updated, multiplicative map.
    for answer in r['answers']:
        r['verify'](answer)
        left=p['five'].apply(answer.left_cut.product).column()
        right=p['five'].apply(answer.right_cut.product).column()
        assert substitute(left,images)==substitute(right,images)
        for cut in (answer.left_cut,answer.right_cut):
            assert substitute(p['five'].apply(cut.product).column(),images)==p['multiply'](
                substitute(p['five'].apply(cut.left).column(),images),
                substitute(p['five'].apply(cut.right).column(),images))
    assert substitute(p['v'].column(),images)==p['multiply'](
        substitute(p['x'].column(),images),substitute(p['y'].column(),images))
checks['actual_DG_generator_differentials_commute']=True
checks['updated_products_and_all_balanced_cases_commute']=True

half=generator_images(contexts[1])
outside={name for path in substitute(p['x'].column(),half) for name in path}-{'ax0','ax1'}
assert outside
checks['fixed_four_leg_image_is_not_gain_stable']=True

initial=bind(r['p4'].product,I)
commands=(('gain',S.Rational(1,2)),('drift',None),('gain',S.Rational(2,3)))
packet=initial; energy_state=e['initial']; running=I
for command in commands:
    previous=packet
    packet=step(packet,command)
    running=matrix_for(command)*running
    assert packet.context==running and packet.parent is previous and packet.source is initial.source
    energy_state=e['source_step'](energy_state,command)
    # Regenerate the actual schedule from the SAME updated leg assignment.
    schedule=e['interface']['schedule']
    from dataclasses import replace
    for policy,nodes in schedule['examples'].items():
        root=nodes[0]
        root=replace(root,context=replace(root.context,assignment=assignment(running)))
        terminal=schedule['terminal'](schedule['vertical'](schedule['vertical'](schedule['generate'](root))))
        rows=schedule['a']['verify'](terminal.binding)
        field=S.ImmutableMatrix([list(sum(row.value,())) for row in rows])
        assert field==energy_state.field
        assert terminal.binding.direct_value==a['values']['d']
checks['context_update_lifts_same_schedule_energy_commands']=True
checks['complete_source_and_context_predecessors_retained']=True

# Pullback order is explicit: T_M(T_N(path)) = T_(N M)(path).
M=contexts[1]; N=D
for name,(_,_,degree) in a['arrows'].items():
    if degree==0:
        assert substitute(substitute(owner['word'](name),generator_images(N)),generator_images(M))==substitute(owner['word'](name),generator_images(N*M))
checks['degree_zero_context_substitution_composes_in_declared_order']=True
# The chosen gain/drift contexts commute; this does NOT assume all matrices do.
assert M*N==N*M
checks['admitted_gain_drift_contexts_commute']=True

# Critical detector distinction: numerical cancellation at an admitted gain
# does not erase the formal path or the retained original source product.
quarter=step(initial,('gain',S.Rational(1,4)))
assert quarter.matrix==owner['Z'] and quarter.symbolic and quarter.source.terms
checks['quarter_gain_annihilates_matrix_not_retained_symbolic_detector']=True

# Base-witness lifts are chosen, not assumed strictly functorial on all DG
# witnesses. Record their degree-one composition defect and its boundary.
sequential=substitute(substitute(owner['word']('abase'),generator_images(N)),generator_images(M))
direct=substitute(owner['word']('abase'),generator_images(N*M))
defect=defaultdict(lambda:S.Integer(0)); add_scaled(defect,sequential,1); add_scaled(defect,direct,-1)
defect=clean(defect)
assert not a['delta'](defect)
checks['base_witness_composition_defect_is_a_cycle']=True
assert all(checks.values())
out={'schema':'marici.relation-continuation-context.v1','status':'pass','checks':checks,
     'DG_generator_checks':dg_checks,'escaped_arrow_generators':sorted(outside),
     'context_law':'C -> M_command C; Phi_C = T_C Phi; direct d fixed',
     'matrix_detector_zero_at_gain':'1/4',
     'base_witness_composition_defect_terms':len(defect),
     'remaining_obligation':'if the degree-one base-witness defect is nonzero, retain a degree-two filler for context composition before claiming coherent whole-witness assembly'}
(ROOT/'research/strominger/results/relation-continuation-context-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
