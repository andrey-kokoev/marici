"""Exact candidate 36-component -> 137 pair-valued slot refibration.
Not a derivation of a reference, numerical DG legs, d, or physical foliation.
"""
from pathlib import Path
from dataclasses import replace
from itertools import permutations
import contextlib,io,runpy,json,hashlib,sys
from field_refibration import EDGES,encode,recover,present,unpresent,relabel,Foliation
ROOT=Path(__file__).resolve().parents[3]
log=io.StringIO()
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
try:
    with contextlib.redirect_stdout(log):
        schedule=runpy.run_path(str(Path(__file__).with_name('check_generating_horizontal_schedule.py')))
finally:sys.path.pop(0)
with contextlib.redirect_stdout(log):
    import check_rotation_realization_square as rotation
owner=schedule['g'];A,ZERO=rotation.A,rotation.ZERO
labels=rotation.r.labels
field={edge:tuple(A(tuple((k+1 if mask==0 else 2*k+1 if mask==8 else 0) for mask in range(16))) for k in range(3*i,3*i+3)) for i,edge in enumerate(EDGES)}
packet=encode(field,(0,1),owner)
assert len(packet.slots)==137
assert sum(s.branch=='arrow' for s in packet.slots)==121
assert sum(s.branch=='state' for s in packet.slots)==16
assert recover(packet,owner)==field
# Match actual generator support and ordered parent occurrence domains exactly.
selected=tuple(edge for edge in EDGES if edge!=(0,1))
for slot in packet.slots:
    rid=tuple(selected.index(e) for e in slot.parents) if slot.branch=='arrow' else slot.parents
    original=owner['first'].blocks[slot.branch][rid]
    assert (slot.source,slot.target)==(original.source,original.target)
    assert original.parents==tuple((i,) for i in rid)
# All 36 basis fields recover; this encoding is linear duplication in a fixed chart.
for k in range(36):
    basis={edge:tuple(A(int(3*i+j==k)) for j in range(3)) for i,edge in enumerate(EDGES)}
    assert recover(encode(basis,(0,1),owner),owner)==basis
# Every marked reference choice retains the omitted arrow via its source-state fiber.
for reference in EDGES:
    test=encode(field,reference,owner)
    assert recover(test,owner)==field
    assert not any(reference in s.parents for s in test.slots if s.branch=='arrow')
    assert any(reference==edge for s in test.slots if s.branch=='state' for bundle in s.payloads for edge,_ in bundle)
# Full support relabelling (not a claim of 24 physical proper rotations).
for p in permutations(range(4)):
    transformed={tuple(p[x] for x in edge):value for edge,value in field.items()}
    assert relabel(packet,p)==encode(transformed,(p[0],p[1]),owner)
# Actual independent native proper rotations: rotate vectors AND their patch labels.
for p,U in rotation.targetActions.items():
    geometric=rotation.r.geo.rotation(p)
    def vector_action(value):
        return tuple(sum((A(geometric[i][j])*value[j] for j in range(3)),ZERO) for i in range(3))
    independently={tuple(p[x] for x in edge):vector_action(value) for edge,value in field.items()}
    flat=tuple(field[tuple('ABCD'.index(c) for c in label.split(':')[0])]['xyz'.index(label.split(':')[1])] for label in labels)
    moved=[ZERO for _ in range(36)]
    for (i,j),v in U.items():moved[i]=moved[i]+v*flat[j]
    for i,label in enumerate(labels):
        edge=tuple('ABCD'.index(c) for c in label.split(':')[0]);axis='xyz'.index(label.split(':')[1])
        assert independently[edge][axis]==moved[i]
    assert relabel(packet,p,vector_action)==encode(independently,(p[0],p[1]),owner)
    if p!=(0,1,2,3):assert relabel(packet,p)!=encode(independently,(p[0],p[1]),owner)
# Both input and output may be represented raw/by-source/by-target without loss.
view_counts={}
for phase in ('raw','source','target'):
    view=present(packet,phase)
    assert unpresent(view,phase)==packet.slots
    assert recover(Foliation(packet.reference,unpresent(view,phase)),owner)==field
    view_counts[phase]=len(view)
controls={}
def rejects(name,call):
    try:call()
    except (ValueError,KeyError,TypeError,AssertionError):controls[name]=True
    else:raise AssertionError('Accepted hostile '+name)
rejects('drop_slot',lambda:recover(replace(packet,slots=packet.slots[:-1]),owner))
rejects('relabel_reference_without_payloads',lambda:recover(replace(packet,reference=(1,0)),owner))
s=packet.slots[0];bundle=list(s.payloads[0]);edge,value=bundle[0];bundle[0]=(edge,(value[0]+A(1),*value[1:]));bad=replace(s,payloads=(tuple(bundle),s.payloads[1]))
rejects('inconsistent_duplicate',lambda:recover(replace(packet,slots=(bad,)+packet.slots[1:]),owner))
rejects('missing_field_component',lambda:encode({**field,EDGES[0]:field[EDGES[0]][:2]},(0,1),owner))
rejects('invented_reference',lambda:encode(field,(0,0),owner))
wrong={('arrow',(99,99)):packet.slots}
rejects('wrong_family_key',lambda:unpresent(wrong,'source'))
# The new output really depends on field values, unlike a bare support projection.
changed={**field,EDGES[0]:(field[EDGES[0]][0]+A(1),*field[EDGES[0]][1:])}
assert set(changed)==set(field) and encode(changed,(0,1),owner)!=packet
sources=[Path(__file__),Path(__file__).with_name('field_refibration.py'),Path(__file__).with_name('check_generating_horizontal_schedule.py'),Path(rotation.__file__),ROOT/'research/strominger/field-36-to-137-refibration-v1.md']
report={'schema':'marici.field-36-to-137-refibration.v1','status':'pass',
 'construction':'pair-valued decoration of the existing two-block generator; state payload = full outgoing source fiber',
 'counts':{'field_components':36,'arrow_slots':121,'state_slots':16,'total_slots':137},
 'independent_field_basis_vectors_recovered':36,'reference_choices_checked':12,'support_relabellings':24,'proper_field_rotations':12,
 'presentation_family_counts':view_counts,'rejected_hostiles':controls,
 'reference_policy':'supplied directed arrow; omitted only from counted arrow branch',
 'retention':'all field values recovered solely from slot payloads; no hidden original-field copy',
 'not_established':['selection of reference or same-kind policy','identification of source fibers with independently supplied physical state roots','numerical/DG leg assignment and direct reference d','physical rung identification or differential-geometric foliation','137 independent modes or a numerical coupling constant'],
 'prior_schedule_and_rotation_replay':log.getvalue(),
 'direct_source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
out=ROOT/'research/strominger/results/field-36-to-137-refibration';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:report[k] for k in ['status','counts','independent_field_basis_vectors_recovered','reference_choices_checked','support_relabellings','proper_field_rotations','presentation_family_counts','rejected_hostiles']},indent=2))
