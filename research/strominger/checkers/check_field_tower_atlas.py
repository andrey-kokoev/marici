"""Populate/check all nine positions of the candidate field-slot tower.
This does not identify pair-valued slots with the old numerical/DG payloads.
"""
from pathlib import Path
from dataclasses import replace
import contextlib,io,json,hashlib
from field_refibration import EDGES
from field_refibration_tower import PHASE,make_node,recover_field,vertical,horizontal,semantic,geometric_action,induced_action
ROOT=Path(__file__).resolve().parents[3]
log=io.StringIO()
with contextlib.redirect_stdout(log):
    import check_field_36_to_137_refibration as previous
    import check_simplex_interface_algebra as group
owner=previous.owner;rotation=previous.rotation;A,ZERO=rotation.A,rotation.ZERO
field=previous.field;labels=rotation.r.labels
atlas_path=ROOT/'research/strominger/rung-symmetry-atlas-v2.json'
atlas=json.loads(atlas_path.read_text(encoding='utf8'))
assert atlas['schema']=='marici.rung-symmetry-atlas.v2'
assert sorted(r['rung'] for r in atlas['rungs'])==list(range(4,13))
assert all((ROOT/p).is_file() for p in atlas['evidence_sources'])

def tower(values,reference=(0,1)):
    n12=make_node(values,reference,12,owner,('start12',))
    n11=vertical(n12,owner);n10=vertical(n11,owner)
    n6=horizontal(n12,owner);n5=vertical(n6,owner);n4=vertical(n5,owner)
    n5other=horizontal(n11,owner);n4other=horizontal(n10,owner)
    assert semantic(n5other)==semantic(n5)
    assert semantic(vertical(n5other,owner))==semantic(n4other)==semantic(n4)
    assert n4.history!=n4other.history
    nodes={n.rung:n for n in (n12,n11,n10,n6,n5,n4)}
    for node in nodes.values():assert recover_field(node,owner)==values
    return nodes
nodes=tower(field)
# Recover all basis components through every state and both complete routes.
for k in range(36):
    basis={edge:tuple(A(int(3*i+j==k)) for j in range(3)) for i,edge in enumerate(EDGES)}
    tower(basis)
for reference in EDGES:tower(field,reference)
profiles={}
for entry in atlas['rungs']:
    rung=entry['rung']
    if entry['role']=='state':
        node=nodes[rung]
        assert entry['outer_entries']==len(node.view)
        assert entry['phase']==PHASE[rung]
        assert entry['independent_field_components']==36
        leaves=0 if rung>=10 else len(node.view) if PHASE[rung]=='raw' else sum(map(len,node.view.values()))
        assert entry['comparison_leaves']==leaves
        profiles[str(rung)]={'role':'state','outer_entries':len(node.view),'comparison_leaves':leaves,'recovered_components':36}
    else:
        assert rung in (9,8,7) and [entry['source'],entry['target']]==atlas['diagram']['horizontal_roles'][str(rung)]
        assert semantic(horizontal(nodes[entry['source']],owner))==semantic(nodes[entry['target']])
        assert entry['generated_total_leaves']==137
        profiles[str(rung)]={'role':'transport','source':entry['source'],'target':entry['target'],'generated_leaves':137,'inverse_on_image':True}
# A full action exists on each constrained image by exact recovery/encoding.
# This is explicitly an INDUCED action, not independent local slot dynamics.
full_covariance=0
for (p,a,b),matrix in group.matrices.items():
    acted={r:induced_action(node,matrix,labels,p,ZERO,owner) for r,node in nodes.items()}
    for left,right in ((12,11),(11,10),(6,5),(5,4)):
        assert semantic(vertical(acted[left],owner))==semantic(acted[right]);full_covariance+=1
    for left,right in ((12,6),(11,5),(10,4)):
        assert semantic(horizontal(acted[left],owner))==semantic(acted[right]);full_covariance+=1
# The geometric part also has an independently occurrence-wise realization.
geometric_checks=0
for p,matrix in rotation.targetActions.items():
    rot=rotation.r.geo.rotation(p)
    def vector_action(value):return tuple(sum((A(rot[i][j])*value[j] for j in range(3)),ZERO) for i in range(3))
    direct={r:geometric_action(node,p,vector_action,owner) for r,node in nodes.items()}
    for rung in nodes:
        induced=induced_action(nodes[rung],matrix,labels,p,ZERO,owner)
        assert semantic(direct[rung])==semantic(induced);geometric_checks+=1
    for left,right in ((12,11),(11,10),(6,5),(5,4)):
        assert semantic(vertical(direct[left],owner))==semantic(direct[right])
    for left,right in ((12,6),(11,5),(10,4)):
        assert semantic(horizontal(direct[left],owner))==semantic(direct[right])
# Verify all internal V4 composition pairs explicitly at every presentation.
internal_compositions=0
identity=(0,1,2,3)
for rung,node in nodes.items():
    for (a,b),X in group.refs.items():
        for (c,d),Y in group.refs.items():
            lhs=induced_action(induced_action(node,Y,labels,identity,ZERO,owner),X,labels,identity,ZERO,owner)
            rhs=induced_action(node,group.refs[a^c,b^d],labels,identity,ZERO,owner)
            assert semantic(lhs)==semantic(rhs);internal_compositions+=1
# Domain stabilizers fix the marked reference, not the field's pointwise values.
reference=(0,1)
proper_fixed=sum(tuple(p[i] for i in reference)==reference for p in rotation.targetActions)
full_fixed=sum(tuple(p[i] for i in reference)==reference for p,a,b in group.matrices)
assert proper_fixed==atlas['actions']['proper_A4']['fixed_reference_domain_order']==1
assert full_fixed==atlas['actions']['full_48_induced']['fixed_reference_domain_order']==4
assert len(group.matrices)==atlas['actions']['full_48_induced']['order']==48
controls={}
def rejects(name,call):
    try:call()
    except (ValueError,KeyError,TypeError,AssertionError):controls[name]=True
    else:raise AssertionError('Accepted hostile '+name)
rejects('rung9_is_not_state',lambda:make_node(field,reference,9,owner))
rejects('horizontal_on_output',lambda:horizontal(nodes[6],owner))
rejects('vertical_after4',lambda:vertical(nodes[4],owner))
rejects('source_view_as_target',lambda:recover_field(replace(nodes[10],view=nodes[11].view),owner))
rejects('missing_comparison_leaf',lambda:recover_field(replace(nodes[6],view=nodes[6].view[:-1]),owner))
rejects('reference_changed_without_slots',lambda:recover_field(replace(nodes[6],reference=(1,0)),owner))
report={'schema':'marici.field-tower-atlas-check.v2','status':'pass','rungs':profiles,
 'basis_fields_checked':36,'reference_choices_checked':12,'field_components_recovered_at_each_state':36,
 'generated_group_order':48,'induced_action_map_squares':full_covariance,'independent_geometric_action_comparisons':geometric_checks,'internal_composition_checks':internal_compositions,
 'fixed_reference_domain_stabilizers':{'proper_rotations':proper_fixed,'full_generated_action':full_fixed},
 'route_histories_distinct':True,'rejected_hostiles':controls,
 'scope':'Complete candidate field-slot diagram. Induced full-group covariance follows from faithful reconstruction; only the proper geometric subgroup has an independently checked occurrence-wise slot action. Numerical/DG binding, physical identification and preferred reference remain open.',
 'prerequisite_replay':log.getvalue()}
sources=[Path(__file__),Path(__file__).with_name('field_refibration_tower.py'),Path(__file__).with_name('field_refibration.py'),atlas_path,ROOT/'research/strominger/rung-symmetry-atlas-v2.md']
report['direct_source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
out=ROOT/'research/strominger/results/field-tower-atlas';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('prerequisite_replay','direct_source_hashes')},indent=2))
