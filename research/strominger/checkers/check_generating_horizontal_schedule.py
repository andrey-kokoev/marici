"""A declared generating horizontal schedule, not the old137-row transport.

Left12/11/10 retain twelve primitive arrows. G9/G8/G7 introduce ordered
comparison plus supplied states internally. Right6/5/4 retain137 slots.
"""
import contextlib
from dataclasses import dataclass, replace
import io
import json
from pathlib import Path
import runpy

ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    a=runpy.run_path(str(ROOT/'research/strominger/checkers/check_generated_rung4_adapter.py'))
g=a['generated']
indexed,unindex,promote,leaves=(a[k] for k in ('indexed','unindex','promote','leaves'))

@dataclass(frozen=True)
class Primitive:
    label: tuple
    source: tuple
    target: tuple

@dataclass(frozen=True)
class Context:
    mark: tuple
    state_roots: tuple
    assignment: dict
    policy: str

@dataclass(frozen=True)
class Node:
    rung: int
    view: object
    context: Context
    binding: object = None
    parents: tuple = ()
    trace: tuple = ()

PHASE={12:'raw',11:'source',10:'target',6:'raw',5:'source',4:'target'}
primitive_rows=tuple(Primitive(('primitive',i),(u,),(v,))
                     for i,(u,v) in enumerate(g['full_edges']))

def recover(node):
    assert node.rung in PHASE
    if PHASE[node.rung]=='raw':
        assert isinstance(node.view,tuple)
        rows=node.view
    else:
        assert isinstance(node.view,dict)
        rows=unindex(node.view)
        assert node.view==indexed(rows,PHASE[node.rung]), 'wrong selector phase'
    if node.rung>=10:
        assert rows==primitive_rows and node.binding is None
    else:
        assert node.binding is not None
        assert leaves(rows)==a['verify'](node.binding)
    return rows


def present(rows,rung):
    return rows if PHASE[rung]=='raw' else indexed(rows,PHASE[rung])


def vertical(node):
    assert node.rung in (12,11,6,5)
    rows=recover(node)
    out=node.rung-1
    return Node(out,present(rows,out),node.context,node.binding,(node,),node.trace+(f'P{node.rung}-{out}',))


def verify_left(node):
    assert node.rung in (12,11,10)
    recover(node)
    if node.rung==12:
        assert not node.parents and node.trace==('start12',)
    else:
        assert len(node.parents)==1 and node.parents[0].rung==node.rung+1
        verify_left(node.parents[0])
        assert node==vertical(node.parents[0])


def generate(node):
    assert node.rung in (12,11,10), 'horizontal source phase'
    verify_left(node)
    rows=recover(node)
    c=node.context
    assert c.policy in ('inherited','common')
    assert c.mark==(0,1) and c.state_roots==(0,1,2,3), 'fixed displayed adapter domain'
    selected=tuple(r for r in rows if (r.source[0],r.target[0])!=c.mark)
    assert len(selected)==11
    # Generation happens HERE, inside G, not before the diagram's rung12.
    records={(i,):g['Record'](r.source,r.target) for i,r in enumerate(selected)}
    states={(i,):g['Record']((root,),(root,)) for i,root in enumerate(c.state_roots)}
    frame={'primitive_rows':rows,'selected_parent_ids':tuple(r.label for r in selected),
           'reference':c.mark,'states':c.state_roots,'operation':'same-kind-independent-pair'}
    seed=g['Packet'](0,frame,{'arrow':records,'state':states},{})
    created=g['advance'](seed)
    binding=a['bind'](created,c.assignment)
    r=a['verify'](binding)
    outer=promote(promote(r,1,c.policy),2,c.policy)
    out=node.rung-6
    return Node(out,present(outer,out),c,binding,(node,),node.trace+(f'G{node.rung-3}',))


def verify_right(node):
    assert node.rung in (6,5,4)
    r=recover(node)
    assert node.parents
    parent=node.parents[0]
    if parent.rung<10:
        verify_right(parent)
    expected=generate(parent) if parent.rung>=10 else vertical(parent)
    assert node==expected, 'history, binding, policy or generated-view drift'
    return r


def snapshot(node):
    # Route equality compares semantic fields, not erasing construction paths.
    return node.rung,node.view,node.context,node.binding


def terminal(node):
    assert node.rung==4
    verify_right(node)
    t=a['Terminal'](node.binding,node.context.policy,node.view,
                    a['diagram']['Reference'](4,node.binding.direct_value))
    a['verify_terminal'](t)
    return t

checks={}
profiles={}
examples={}
for policy in ('inherited','common'):
    c=Context((0,1),(0,1,2,3),dict(a['values']),policy)
    n12=Node(12,primitive_rows,c,trace=('start12',))
    n11=vertical(n12); n10=vertical(n11)
    n6=generate(n12); n5=vertical(n6); n4=vertical(n5)
    g8=generate(n11); g7=generate(n10)
    assert snapshot(g8)==snapshot(n5)
    assert snapshot(g7)==snapshot(vertical(g8))==snapshot(n4)
    assert g7.trace!=n4.trace and g7.parents!=n4.parents
    for node in (n6,n5,n4,g8,g7): verify_right(node)
    t=terminal(n4); bottom=terminal(g7)
    assert t==bottom
    assert t.view==a['terminals'][policy].view
    assert len(recover(n12))==len(recover(n11))==len(recover(n10))==12
    assert len(leaves(recover(n6)))==len(leaves(recover(n5)))==len(leaves(recover(n4)))==137
    assert n4.binding.generated_packet.parent.parent['primitive_rows']==primitive_rows
    assert n4.binding.generated_packet.parent.parent['reference']==c.mark
    assert len(n4.binding.generated_packet.parent.parent['selected_parent_ids'])==11
    # Recover each arrow-role parent back to the ORIGINAL twelve-arrow frame.
    frame=n4.binding.generated_packet.parent.parent
    for slot in n4.binding.slots:
        if slot.branch=='a':
            for rid in slot.parents:
                original=next(r for r in primitive_rows if r.label==frame['selected_parent_ids'][rid[0]])
                selected_record=n4.binding.generated_packet.parent.blocks['arrow'][rid]
                assert (original.source,original.target)==(selected_record.source,selected_record.target)
    checks[policy+'_squares_routes_and_retained_histories']=True
    checks[policy+'_generated_terminal_matches_adapter']=True
    checks[policy+'_original_primitive_parents_recover']=True
    profiles[policy]={str(n.rung):{'outer_rows':len(recover(n)),
         'primitive_rows' if n.rung>=10 else 'comparison_leaves':len(recover(n)) if n.rung>=10 else len(leaves(recover(n))),
         'selector':PHASE[n.rung],
         'view_keys':None if PHASE[n.rung]=='raw' else len(n.view)} for n in (n12,n11,n10,n6,n5,n4)}
    examples[policy]=(n12,n11,n10,n6,n5,n4)

controls={}
def rejects(name,call):
    try: call()
    except (AssertionError,TypeError,AttributeError,KeyError): controls[name]=True
    else: raise AssertionError('Accepted hostile: '+name)

n12,n11,n10,n6,n5,n4=examples['inherited']
rejects('already137_rows_at_start',lambda:generate(replace(n12,view=a['rows'])))
rejects('wrong_index_phase',lambda:generate(replace(n10,view=n11.view)))
rejects('omit_supplied_state_roots',lambda:generate(replace(n12,context=replace(n12.context,state_roots=()))))
rejects('constant_primitive_row_horizontal',lambda:verify_right(replace(n6,view=primitive_rows)))
rejects('drop_generation_parent',lambda:verify_right(replace(n6,parents=())))
rejects('relabel_horizontal_policy',lambda:verify_right(replace(n4,context=replace(n4.context,policy='common'))))
rejects('erase_route_history',lambda:verify_right(replace(n4,trace=())))
assert all(checks.values()) and all(controls.values())
out={'schema':'marici.generating-horizontal-schedule.v1','status':'pass','checks':checks,
     'rejected_hostiles':controls,'rung_tables':profiles,
     'horizontal_operations':{'9':'primitive raw -> generated raw','8':'primitive source view -> generated source view','7':'primitive target view -> generated target view'},
     'generation_pipeline':['retain twelve-arrow frame','select eleven arrow roles','supply four state roots and separate d','ordered same-kind comparison','typed-DG binding','two retained incoming promotions'],
     'scope':'Explicit candidate placement for supplied source/role/reference policies; not unique operator selection or native Feedback.run realization.'}
(ROOT/'research/strominger/results/generating-horizontal-schedule-v1.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
