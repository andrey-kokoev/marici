"""Bind generated slots to the owner's typed DG legs and rung4 carrier.

No physical values, state roots or rung placement are derived from the count.
Owner scripts are executed unchanged; actual constructors and data are reused.
"""
import contextlib
from dataclasses import dataclass, replace
import io
import json
from pathlib import Path
import runpy
import sys

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
with contextlib.redirect_stdout(io.StringIO()):
    generated=runpy.run_path(str(ROOT/'research/strominger/checkers/check_two_block_leaf_generation.py'))
    diagram=runpy.run_path(str(ROOT/'research/nima/checkers/check_rung_transport_diagram.py'))
owner=diagram['m']
Row=diagram['Row']
indexed,unindex,promote,leaves=(diagram[n] for n in ('indexed','unindex','incoming_promotion','leaves'))
values,mul=owner['values'],owner['mul']
# Explicit source choice: base-path witnesses belong to this supplied DG model.
roots={'a':(0,0),'s':(0,0)}
arrows,delta,bases,rectangles,routes=owner['build'](roots)
first=generated['first']

@dataclass(frozen=True)
class Slot:
    branch: str
    parents: tuple
    left_leg: str
    right_leg: str
    row: object
    witness_first: dict
    witness_second: dict
    filler: dict

@dataclass(frozen=True)
class Bound:
    generated_packet: object
    slots: tuple
    assignment: dict
    direct_name: str
    direct_value: tuple
    root_policy: dict


def bind(packet,assigned,direct='d'):
    assert packet.level==1, 'adapter domain is exactly first generated stage'
    assert arrows[direct]==('A','B',0)
    result=[]
    for block,tag,mid in (('arrow','a','U'),('state','s','V')):
        for rid,record in sorted(packet.blocks[block].items()):
            left,right=record.parents
            assert len(left)==len(right)==1 and rid==left+right
            i,j=left[0],right[0]
            x,y=f'{tag}x{i}',f'{tag}y{j}'
            assert arrows[x]==('A',mid,0) and arrows[y]==(mid,'B',0)
            # Parent labels index roles, NOT a claim that variable endpoints
            # themselves form composable paths. Composition uses A,U/V,B.
            source=(tag,)+record.source
            target=(tag,)+record.target
            row=Row(('leaf',len(result)),source,target,mul(assigned[y],assigned[x]))
            w1,w2,fill=routes(tag,i,j)
            result.append(Slot(tag,record.parents,x,y,row,w1,w2,fill))
    return Bound(packet,tuple(result),dict(assigned),direct,assigned[direct],dict(roots))


def verify(bound):
    assert bound.direct_name=='d' and arrows['d']==('A','B',0)
    assert bound.direct_value==bound.assignment['d']
    expected=bind(bound.generated_packet,bound.assignment,bound.direct_name)
    assert bound==expected, 'leg, endpoint, parent, witness, ordering or reference drift'
    for slot in bound.slots:
        boundary=owner['plus'](owner['word'](slot.left_leg,slot.right_leg),
                               owner['minus'](owner['word'](bound.direct_name)))
        assert delta(slot.witness_first)==delta(slot.witness_second)==boundary
        assert delta(slot.filler)==owner['plus'](slot.witness_second,owner['minus'](slot.witness_first))
    return tuple(s.row for s in bound.slots)

bound=bind(first,values)
rows=verify(bound)
checks={
    'generated_rows_equal_owner_source_field_for_field': rows==diagram['source'],
    'all_generated_slots_have_unique_typed_leg_pairs':len({(s.left_leg,s.right_leg) for s in bound.slots})==len(rows),
    'all_exact_parent_ids_recover':all(
        s.parents==first.blocks['arrow' if s.branch=='a' else 'state'][(s.parents[0]+s.parents[1])].parents
        for s in bound.slots),
    'direct_reference_is_not_reference_mark':bound.direct_name=='d' and generated['reference']==(0,1),
    'original_frame_retained':bound.generated_packet.parent is generated['initial'],
}
assert bound.direct_value==diagram['physical_reference'].value
@dataclass(frozen=True)
class Terminal:
    binding: Bound
    policy: str
    view: dict
    reference: object


def finish(binding,policy):
    assert policy in ('inherited','common')
    r=verify(binding)
    middle=promote(r,1,policy)
    right6=promote(middle,2,policy)
    view=indexed(unindex(indexed(right6,'source')),'target')
    return Terminal(binding,policy,view,diagram['Reference'](4,binding.direct_value))


def verify_terminal(terminal):
    assert terminal==finish(terminal.binding,terminal.policy)
    assert leaves(unindex(terminal.view))==verify(terminal.binding)
    return diagram['read_at_four'](terminal.view,terminal.reference)

profiles={}
terminals={}
for policy in ('inherited','common'):
    terminal=finish(bound,policy)
    terminals[policy]=terminal
    right4=terminal.view
    right6=unindex(right4)
    assert verify_terminal(terminal)==owner['add'](diagram['mean'](rows),owner['scale'](-1,bound.direct_value))
    # Compare the actual owner terminal construction, not only the137 total.
    owner_right4=indexed(promote(promote(diagram['source'],1,policy),2,policy),'target')
    assert right4==owner_right4
    profiles[policy]={'outer_rows':len(right6),'mass':sum(r.mass for r in right6),
                      'exact_terminal_equality':True}
checks['both_owner_terminal_carriers_match_exactly']=True
checks['all_symbolic_comparison_boundaries_and_fillers_verified']=True

controls={}
def rejects(name,mutation):
    try: verify(mutation)
    except (AssertionError,KeyError): controls[name]=True
    else: raise AssertionError('Accepted hostile: '+name)

slots=list(bound.slots)
# Reversing the composition may have the same untyped matrix dimensions.
k=next(i for i,s in enumerate(slots) if mul(values[s.left_leg],values[s.right_leg])!=s.row.value)
s=slots[k]
slots[k]=replace(s,row=replace(s.row,value=mul(values[s.left_leg],values[s.right_leg])))
rejects('reversed_noncommuting_composition',replace(bound,slots=tuple(slots)))
slots=list(bound.slots); slots[0]=replace(slots[0],right_leg='sy0')
rejects('cross_branch_intermediate_type',replace(bound,slots=tuple(slots)))
slots=list(bound.slots); slots[0]=replace(slots[0],parents=((1,),(0,)))
rejects('lost_parent_identity',replace(bound,slots=tuple(slots)))
rejects('reference_replaced_by_local_mean',replace(bound,direct_value=diagram['mean'](rows)))
slots=list(bound.slots); slots[0]=replace(slots[0],witness_first={})
rejects('erased_base_path_witness',replace(bound,slots=tuple(slots)))

# Supplied reference change leaves all indirect slots unchanged but alters
# their rung4 comparison. The adapter cannot infer d from those slots.
changed=dict(values); changed['d']=owner['add'](values['d'],owner['H'])
shifted=bind(first,changed)
assert verify(shifted)==rows
residual=lambda b:owner['add'](diagram['mean'](verify(b)),owner['scale'](-1,b.direct_value))
assert residual(shifted)==owner['add'](residual(bound),owner['scale'](-1,owner['H']))
checks['independent_reference_change_detected_without_changing_slots']=True
for policy in terminals:
    shifted_terminal=finish(shifted,policy)
    assert shifted_terminal.view==terminals[policy].view
    assert verify_terminal(shifted_terminal)==residual(shifted)

for name,bad in (
    ('wrong_reference_rung',replace(terminals['inherited'],reference=diagram['Reference'](5,bound.direct_value))),
    ('lost_terminal_binding',replace(terminals['inherited'],binding=shifted)),
):
    try: verify_terminal(bad)
    except AssertionError: controls[name]=True
    else: raise AssertionError('Accepted terminal hostile: '+name)
checks['terminal_package_retains_binding_policy_and_reference']=True
assert all(checks.values()) and all(controls.values())
out={'schema':'marici.generated-rung4-adapter.v1','status':'pass','checks':checks,
     'rejected_hostiles':controls,'terminal_profiles':profiles,
     'slots':len(rows),'primitive_leg_roles':30,'direct_reference':'d:A->B',
     'scope':'Exact generated-slot/typed-DG/owner-rung4 bridge for supplied roles, roots and matrices; no generative rung placement or physical adapter inferred.'}
(ROOT/'research/strominger/results/generated-rung4-adapter-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
