"""Typed diagram grading vs presentation labels and endpoint quotients.

Reuses actual indexing/path/diagram operations. Does not infer dimensions.
"""
import contextlib
import io
import itertools
import json
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(ROOT/'research/strominger/checkers/check_wg_rung_schedule_comparison.py'))
D=prior['diagram']; E=prior['E']; base=prior['base']; total=prior['total']
checks={}
# Positions are typed: six object presentations and three transport views.
objects={(0,0):12,(0,1):11,(0,2):10,(1,0):6,(1,1):5,(1,2):4}
transports={0:9,1:8,2:7}
edges=[]
for col in (0,1):
    for row in (0,1): edges.append(((col,row),(col,row+1),'presentation'))
for row in range(3): edges.append(((0,row),(1,row),'action'))
# Hasse rank for this finite directed object diagram, NOT a carrier dimension.
rank=lambda vertex:3-sum(vertex)
assert all(rank(v)==rank(u)-1 for u,v,_ in edges)
checks['six_object_seven_edge_diagram_has_unit_graph_rank']=True
assert {objects[u]-objects[v] for u,v,k in edges if k=='presentation'}=={1}
assert {objects[u]-objects[v] for u,v,k in edges if k=='action'}=={6}
assert all(objects[(0,r)]-transports[r]==transports[r]-objects[(1,r)]==3 for r in range(3))
checks['numerical_rung_labels_are_not_unit_edge_rank']=True
# All complete paths in the typed object graph, retaining edge kinds.
def paths(u,target):
    if u==target: return ((),)
    return tuple(((u,v,k),)+p for x,v,k in edges if x==u for p in paths(v,target))
routes=paths((0,0),(1,2))
assert len(routes)==3 and all(len(route)==3 for route in routes)
assert {tuple(k for u,v,k in route) for route in routes}=={
    ('action','presentation','presentation'),('presentation','action','presentation'),
    ('presentation','presentation','action')}
checks['three_routes_not_eight_serial_steps']=True

# Two actual four-block quotients on the same twelve endpoint-labelled arrows.
source=prior['indexed'](E,'source'); target=prior['indexed'](E,'target')
assert sorted(map(len,source.values()))==sorted(map(len,target.values()))==[3]*4
assert prior['unindex'](source)==prior['unindex'](target)==E
assert source!=target
# Neither target factors through source nor source through target.
assert all(len({r.target for r in fiber})==3 for fiber in source.values())
assert all(len({r.source for r in fiber})==3 for fiber in target.values())
# The JOINT endpoint map, unlike either projection, recovers each arrow.
assert len({(r.source,r.target) for r in E})==len(E)==12
checks['endpoint_quotients_have_equal_profiles_but_do_not_factor']=True
checks['joint_endpoints_recover_twelve_oriented_arrows']=True
lookup={r.label:r for r in E}
def reverse(r): return lookup[('arrow',r.label[2],r.label[1])]
assert all(reverse(reverse(r))==r and reverse(r).source==r.target and reverse(r).target==r.source for r in E)
# Reversal intertwines s and t, but changes the retained orientation/path.
assert all(reverse(r)!=r and reverse(r).value!=r.value for r in E)
checks['source_target_reversal_is_explicit_not_identity']=True
# Covariance under every endpoint relabelling; it does not choose s over t.
for g in itertools.permutations(range(4)):
    for r in E:
        image=lookup[('arrow',g[r.label[1]],g[r.label[2]])]
        assert image.source==('vertex',g[r.label[1]]) and image.target==('vertex',g[r.label[2]])
        assert reverse(image)==lookup[('arrow',g[r.label[2]],g[r.label[1]])]
checks['all24_endpoint_relabellings_preserve_typed_orientation_laws']=True
# Transitivity forces every S4-invariant scalar on these arrows to be constant.
first=E[0]
orbit={lookup[('arrow',g[first.label[1]],g[first.label[2]])] for g in itertools.permutations(range(4))}
assert orbit==set(E)
# A strict endpoint decrease along every arrow is also impossible: each edge
# and its reverse would require both grade(i)>grade(j) and grade(j)>grade(i).
assert all((r.target,r.source) in {(e.source,e.target) for e in E} for r in E)
checks['transitivity_and_two_cycles_obstruct_intrinsic_arrow_descent']=True

# Retained totals preserve counts and each one-edge word at every depth.
cur=E
for field in ('source','target'):
    cur=total(cur,field)
    assert len(cur)==12 and all(base(r).value==lookup[r.label].value for r in cur)
checks['presentation_indexing_changes_neither_row_count_nor_word_length']=True
# Instantiate all three routes with the EXISTING horizontal action policies.
profiles={}
for policy in ('inherited','common'):
    A=D['source']
    def P(rows): return D['incoming_promotion'](D['incoming_promotion'](rows,1,policy),2,policy)
    B=P(A)
    middle=()
    finals=[]
    for route in routes:
        rows=A; history=[]
        for u,v,kind in route:
            if kind=='action':
                before=rows; rows=P(rows)
                middle=(D['incoming_promotion'](before,1,policy),rows)
                history.append(('action',policy,middle))
            else:
                field=('source','target')[v[1]-1]
                view=D['indexed'](rows,field)
                history.append(('presentation',field,view))
                rows=D['unindex'](view)
        assert rows==B and D['leaves'](rows)==A
        finals.append(tuple(history))
    assert len({tuple(item[:2] for item in history) for history in finals})==3
    profiles[policy]={'initial_rows':len(A),'result_rows':len(B),
                      'retained_leaves':len(D['leaves'](B)),'retained_mass':sum(r.mass for r in B)}
assert profiles=={'inherited':{'initial_rows':137,'result_rows':32,'retained_leaves':137,'retained_mass':137},
                 'common':{'initial_rows':137,'result_rows':1,'retained_leaves':137,'retained_mass':137}}
checks['actual_action_policies_preserve_leaves_not_a_unique_row_grade']=True
checks['equal_route_results_do_not_identify_construction_histories']=True

rejected=[]
def refuse(name,condition):
    assert not condition, 'hostile accepted: '+name
    rejected.append(name)
refuse('rung_number_is_unit_graph_rank',all(objects[u]-objects[v]==1 for u,v,k in edges))
refuse('transport9_is_an_object_vertex',9 in objects.values())
refuse('four_blocks_mean_four_retained_rows',len(total(E,'source'))==4)
refuse('target_is_a_function_of_source',all(len({r.target for r in fiber})==1 for fiber in source.values()))
refuse('equal_profiles_identify_quotient_maps',source==target)
refuse('reverse_orientation_is_identity',all(reverse(r)==r for r in E))
refuse('three_routes_have_identical_traces',len({tuple(k for u,v,k in route) for route in routes})==1)
refuse('presentation_label_is_result_row_count',all(p['result_rows']==6 for p in profiles.values()))
assert all(checks.values())
result={'schema':'marici.wg-grading-orientation.v1','status':'pass','checks':checks,'rejected_hostiles':rejected,
        'object_roles':[{'position':list(pos),'rung_label':label,'finite_graph_rank':rank(pos)} for pos,label in objects.items()],
        'transport_roles':[{'row':r,'transport_label':t,'domain':objects[(0,r)],'codomain':objects[(1,r)]} for r,t in transports.items()],
        'route_words':[[k for u,v,k in route] for route in routes],'actual_profiles':profiles,
        'scope':'finite typed diagram rank, endpoint quotient/orientation and declared action-policy instances; not physical dimension or a grade for every integer12 through4'}
(ROOT/'research/strominger/results/wg-grading-orientation-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
