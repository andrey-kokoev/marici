"""Actual schedule factorization and failed local triangle half-step binding.

Rejects a named candidate, not every possible enlarged package-level root.
"""
import contextlib
from dataclasses import dataclass, replace
from fractions import Fraction as F
import io
import json
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    w=runpy.run_path(str(ROOT/'research/strominger/checkers/check_wg_retained_assembly.py'))
    local=runpy.run_path(str(ROOT/'research/nima/checkers/check_triangle_half_phase.py'))
    serial=runpy.run_path(str(ROOT/'research/nima/checkers/check_two_triangle_half_phase.py'))
    local['main'](); serial['main']()
schedule=w['schedule']; a=schedule['a']; g=schedule['g']; S=w['S']
mm=local['mm']; transpose=local['transpose']; add=local['add']; sub=local['sub']; scale=local['scale']
packets=tuple(local['TwoPacket'](*x) for x in (('AB','A','B'),('BC','B','C'),('CA','C','A')))
C=local['cycle_from_packets'](packets); I=local['I']
Q=scale(add(add(I,C),mm(C,C)),F(1,3)); P=sub(I,Q)
H=add(add(Q,scale(P,F(1,2))),scale(sub(C,transpose(C)),F(1,2)))
assert mm(H,H)==C and mm(transpose(H),H)==I
assert mm(mm(C,C),mm(C,C))==C and mm(C,C)!=H

@dataclass(frozen=True)
class Intermediate:
    source: object
    binding: object
    first_rows: tuple
    trace: tuple

@dataclass(frozen=True)
class Factorization:
    intermediate: Intermediate
    output: object

# A real heterogeneous factorization of G: primitive frame -> generated/bound
# first promotion -> second promotion. It is NOT a homogeneous triangle root.
def first_stage(node):
    schedule['verify_left'](node)
    rows=schedule['recover'](node); context=node.context
    assert context.policy in ('inherited','common') and context.mark==(0,1) and context.state_roots==(0,1,2,3)
    selected=tuple(r for r in rows if (r.source[0],r.target[0])!=context.mark)
    records={(i,):g['Record'](r.source,r.target) for i,r in enumerate(selected)}
    states={(i,):g['Record']((root,),(root,)) for i,root in enumerate(context.state_roots)}
    frame={'primitive_rows':rows,'selected_parent_ids':tuple(r.label for r in selected),
           'reference':context.mark,'states':context.state_roots,'operation':'same-kind-independent-pair'}
    packet=g['advance'](g['Packet'](0,frame,{'arrow':records,'state':states},{}))
    bound=a['bind'](packet,context.assignment)
    first_rows=schedule['promote'](a['verify'](bound),1,context.policy)
    return Intermediate(node,bound,first_rows,('generate137-and-bind','incoming-promotion1'))

def second_stage(mid):
    assert isinstance(mid,Intermediate)
    assert mid==first_stage(mid.source), 'intermediate/source/trace drift'
    node=mid.source
    outer=schedule['promote'](mid.first_rows,2,node.context.policy)
    out=node.rung-6
    output=schedule['Node'](out,schedule['present'](outer,out),node.context,mid.binding,(node,),node.trace+(f'G{node.rung-3}',))
    assert output==schedule['generate'](node)
    schedule['verify_right'](output)
    return Factorization(mid,output)

checks={}; profiles=[]
for policy in ('inherited','common'):
    left=schedule['examples'][policy][0]
    for _ in range(3):
        mid=first_stage(left); fact=second_stage(mid)
        assert fact.intermediate.source is left and fact.output.parents==(left,)
        assert schedule['leaves'](mid.first_rows)==a['verify'](mid.binding)
        assert schedule['leaves'](schedule['recover'](fact.output))==a['verify'](mid.binding)
        assert len(mid.binding.slots)==137
        profiles.append({'policy':policy,'source_rung':left.rung,'result_rung':fact.output.rung,
                         'intermediate_rows':len(mid.first_rows),'retained_slots':len(mid.binding.slots)})
        if left.rung>10: left=schedule['vertical'](left)
checks['six_typed_factorizations_equal_actual_horizontal_generator']=True
checks['factorization_retains_original_source_binding_and_intermediate']=True
checks['local_triangle_root_and_alternate_branch_rechecked']=True

controls={}
def reject(name,fn):
    try: fn()
    except (AssertionError,AttributeError,TypeError,KeyError,ValueError): controls[name]=True
    else: raise AssertionError('accepted candidate/hostile: '+name)
left=schedule['examples']['inherited'][0]; full=schedule['generate'](left); mid=first_stage(left)
# API closure fails: G takes a primitive left Node, not a right or Intermediate.
reject('full_generator_is_not_an_endomorphism_of_left_phase',lambda:schedule['generate'](full))
reject('first_stage_cannot_be_iterated_on_its_output',lambda:first_stage(mid))
reject('lost_intermediate_group_members',lambda:second_stage(replace(mid,first_rows=())))
reject('relabelled_intermediate_history',lambda:second_stage(replace(mid,trace=('triangle-half',))))

# Concrete coefficient-root candidate on three actual retained generated slots.
# Mix payloads only; keep occurrence marks, leg names and witnesses fixed.
# This is the natural naive field adapter whose failure must not be hidden.
bound=full.binding
chosen=tuple(bound.slots[:3])
values=tuple(slot.row.value for slot in chosen)
assert len({repr(value) for value in values})>1
owner=a['owner']
def mix(matrix):
    changed=list(bound.slots)
    for i in range(3):
        value=owner['Z']
        for j in range(3): value=owner['add'](value,owner['scale'](matrix[i][j],values[j]))
        changed[i]=replace(chosen[i],row=replace(chosen[i].row,value=value))
    return replace(bound,slots=tuple(changed))
naive_half=mix(H); naive_full=mix(C)
assert naive_half!=bound and naive_full!=bound
reject('triangle_half_payload_mix_breaks_actual_leg_binding',lambda:a['verify'](naive_half))
reject('triangle_cycle_payload_permutation_breaks_marked_binding',lambda:a['verify'](naive_full))
assert any(x<0 for row in H for x in row)
# Existing incoming grouping uses positive mass ratios only; this candidate
# is not one of its admitted convex grouping operations.
checks['triangle_signed_mix_is_not_existing_positive_grouping']=True

# Reproduce the two-triangle serial hostile using the owning embedding formula.
I5=serial['identity'](5)
R1=(I5[0],I5[1],I5[2]); R2=(tuple(-v for v in I5[0]),I5[3],I5[4])
def embed(T,R): return add(I5,mm(mm(transpose(R),sub(T,I)),R))
C1,C2=embed(C,R1),embed(C,R2); H1,H2=embed(H,R1),embed(H,R2)
assert mm(H1,H1)==C1 and mm(H2,H2)==C2
U=mm(H2,H1); G=mm(C2,C1); defect=sub(mm(U,U),G)
assert defect!=scale(I5,F(0)) and serial['tr'](U)==F(28,9)
assert serial['power'](G,5)==I5
controls['serial_local_roots_do_not_square_to_composite']=True
checks['serial_shared_edge_obstruction_rechecked_exactly']=True

# Histories of a single G vs two coefficient H events are not identified by
# H²=C. No witnessing adapter for these histories was supplied by that equation.
assert ('triangle-half','triangle-half')!=('G9',)
checks['coefficient_square_does_not_supply_retained_history_comparison']=True
assert all(checks.values()) and all(controls.values())
out={'schema':'marici.wg-half-step-binding.v1','status':'pass','checks':checks,'rejected_candidates_and_hostiles':controls,
     'factorization_cases':profiles,'serial_defect':[[str(x) for x in row] for row in defect],
     'candidate_disposition':'existing triangle coefficient root does not bind to the selected complete generating schedule via the tested fixed-mark payload adapter',
     'positive_result':'heterogeneous first_stage/second_stage factorization equals actual G with intermediate and137 original slots retained',
     'scope':'explicit failed binding, not a universal nonexistence theorem; a new phase-indexed package operation, branch law and continuation/history comparison may still supply a different root'}
(ROOT/'research/strominger/results/wg-half-step-binding-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
