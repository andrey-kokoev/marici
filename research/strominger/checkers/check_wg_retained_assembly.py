"""Final conditional common-witness assembly; reject erasure at its boundary.

All prior source scopes stay explicit. This is not a universal physical WG.
"""
import contextlib
from dataclasses import dataclass, replace
import io
import json
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    f=runpy.run_path(str(ROOT/'research/strominger/checkers/check_context_composition_fillers.py'))
c=f['c']; e=c['e']; p=c['p']; S=c['S']; r=c['r']
schedule=e['interface']['schedule']; a=schedule['a']

@dataclass(frozen=True)
class Assembly:
    policy: str
    relation: object
    cuts: tuple
    right_action: tuple
    energy: object
    rung4: object
    terminal: object
    comparison: object
    parent: object = None
    command: object = None

def presentation(policy,C):
    root=schedule['examples'][policy][0]
    root=replace(root,context=replace(root.context,assignment=c['assignment'](C)))
    n=schedule['vertical'](schedule['vertical'](schedule['generate'](root)))
    return n,schedule['terminal'](n)

def seed(policy):
    n,t=presentation(policy,c['I'])
    return Assembly(policy,c['initial'],p['evaluated_answers'],r['actual_action'],e['initial'],n,t,None)

def advance(state,command):
    coherent=f['advance'](state.relation,command)
    energy=e['source_step'](state.energy,command)
    n,t=presentation(state.policy,coherent.after.context)
    return Assembly(state.policy,coherent.after,state.cuts,state.right_action,energy,n,t,
                    coherent.comparison,state,command)

# Only checked packages are admitted to continuations; validate the entire
# predecessor chain rather than trusting a freshly computed terminal readout.
def validate(state):
    assert state.policy in ('inherited','common')
    assert state.cuts==p['evaluated_answers'] and state.right_action==r['actual_action']
    assert state.relation.source==c['initial'].source
    if state.parent is None:
        assert state.command is None and state.comparison is None
        assert state.relation==c['initial'] and state.energy==e['initial']
    else:
        validate(state.parent)
        assert state.policy==state.parent.policy
        assert state.relation==c['step'](state.parent.relation,state.command)
        assert state.energy==e['source_step'](state.parent.energy,state.command)
        assert state.comparison==f['compare'](state.parent.relation.context,c['matrix_for'](state.command))
        f['validate'](state.comparison)
        # Do not trust equality with a cached mutable Comparison object.
        M=state.parent.relation.context; N=c['matrix_for'](state.command)
        fresh_defect=f['plus'](f['T'](M,f['T'](N,f['base'])),f['minus'](f['T'](N*M,f['base'])))
        assert state.comparison.defect==fresh_defect
        assert f['delta'](state.comparison.filler)==fresh_defect
    assert state.relation==c['bind'](state.relation.source,state.relation.context,
                                   state.relation.parent,state.relation.command)
    expected_n,expected_t=presentation(state.policy,state.relation.context)
    assert state.rung4==expected_n and state.terminal==expected_t
    rows=a['verify'](state.terminal.binding)
    field=S.ImmutableMatrix([list(sum(row.value,())) for row in rows])
    assert field==state.energy.field
    assert state.terminal.binding.direct_value==a['values']['d']
    # Every retained five-event cut also has a checked current-context image.
    for answer in state.cuts:
        r['verify'](answer.source_answer)
        assert f['T'](state.relation.context,answer.left_product.column())==f['T'](state.relation.context,answer.right_product.column())
    # The actual right-b action is preserved in the same symbolic context.
    images=[f['T'](state.relation.context,image.column()) for image in p['images']]
    assert images[2]==p['multiply'](images[0],images[1])
    assert state.relation.symbolic==images[2]
    return True


def observations(state):
    # Deliberately distinct tasks, not one scalar standing in for identity.
    return {'energy':e['summary'](state.energy).energy,
            'comparison_residual':a['verify_terminal'](state.terminal),
            'relation_matrix':state.relation.matrix,
            'relation_source_detector':state.relation.source.terms[0][1]}

def reusable_task_signature(state):
    # Full history is NOT asserted recoverable from this declared task view.
    return (state.policy,state.relation.context,state.relation.source,state.cuts,
            state.right_action,state.energy.field,state.terminal.view,
            state.terminal.reference,state.relation.symbolic)

checks={}; examples={}
for policy in ('inherited','common'):
    start=seed(policy); validate(start)
    first=advance(start,('gain',S.Rational(1,2)))
    second=advance(first,('drift',None)); validate(second)
    assert second.comparison.defect and len(second.comparison.filler)==18
    assert second.parent is first and first.parent is start
    assert second.relation.source is start.relation.source
    checks[policy+'_full_common_witness_package_and_continuation']=True
    examples[policy]=(start,first,second)

start=examples['inherited'][0]
x=advance(advance(start,('gain',S.Rational(2,3))),('gain',S.Rational(3,5)))
y=advance(start,('gain',S.Rational(2,5)))
validate(x); validate(y)
assert reusable_task_signature(x)==reusable_task_signature(y) and x!=y
for command in (('drift',None),('gain',S.Rational(1,4))):
    xx=advance(x,command); yy=advance(y,command)
    validate(xx); validate(yy)
    assert reusable_task_signature(xx)==reusable_task_signature(yy)
    assert observations(xx)==observations(yy)
checks['task_agreement_transports_next_commands_without_erasing_history']=True
quarter=advance(start,('gain',S.Rational(1,4))); validate(quarter)
assert quarter.relation.matrix==c['owner']['Z'] and quarter.relation.symbolic and quarter.relation.source.terms
checks['numerical_cancellation_keeps_full_symbolic_source_witness']=True

controls={}
def rejects(name,bad):
    try: validate(bad)
    except (AssertionError,AttributeError,KeyError,TypeError): controls[name]=True
    else: raise AssertionError('Accepted erased/stale assembly: '+name)

_,first,last=examples['inherited']
rejects('erased_composition_filler',replace(last,comparison=replace(last.comparison,filler={})))
rejects('stale_pre_gain_energy_field',replace(last,energy=start.energy))
rejects('disconnected_relation_action',replace(last,right_action=r['graded_action']))
rejects('lost_source_cut_witnesses',replace(last,cuts=()))
rejects('relabelled_grouping_policy',replace(last,policy='common'))
rejects('lost_predecessor_history',replace(last,parent=None))
rejects('zero_symbolic_attachment_after_matrix_cancellation',replace(quarter,relation=replace(quarter.relation,symbolic={})))
rejects('reference_replaced_by_local_mean',replace(last,terminal=replace(last.terminal,
    reference=a['diagram']['Reference'](4,a['diagram']['mean'](a['verify'](last.terminal.binding))))))
saved_defect=dict(last.comparison.defect); saved_filler=dict(last.comparison.filler)
try:
    last.comparison.defect.clear(); last.comparison.filler.clear()
    rejects('in_place_cached_comparison_corruption',last)
finally:
    last.comparison.defect.update(saved_defect); last.comparison.filler.update(saved_filler)
assert all(checks.values()) and all(controls.values())
out={'schema':'marici.wg-retained-assembly.v1','status':'pass','checks':checks,
     'rejected_hostiles':controls,
     'scope':'one conditional retained joint source, two fixed grouping-policy instances, declared gain/drift continuations and separate observers',
     'retained':['original relation and cuts','actual source action','context/predecessor/command','DG comparison defect and filler','native-compatible generated terminal fields','energy source field and history','policy and independent reference'],
     'not_claimed':['universal WG or physical realization','faithful numerical detector','inverse of task quotient','identification of recorder seam complex with target DG','Feedback.run identification'],
     'verification':'exact executable assembly and earlier kernel structural/continuation theorems; root assembly is not itself a new Agda theorem'}
(ROOT/'research/strominger/results/wg-retained-assembly-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
