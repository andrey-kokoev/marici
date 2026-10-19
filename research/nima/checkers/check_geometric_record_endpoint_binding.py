# /// script
# dependencies = ["sympy"]
# ///
"""Join full-path responses to the EXISTING typed record attachment and T9s.

The endpoint/label decorations and flat port frames are explicit input data.
No identification of either candidate with intended T9 is asserted.
"""
from contextlib import redirect_stdout
from fractions import Fraction
from pathlib import Path
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/geometric-record-endpoint-binding.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    geo=runpy.run_path(str(HERE/'check_geometric_fixture_representation.py'))
    flat=runpy.run_path(str(HERE/'check_flat_reference_attachment.py'))
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
check('full-path-representation-fresh',geo['result']['verification_status']=='pass')
check('existing-flat-attachment-fresh',flat['result']['status']=='passed')
m=flat['m']; chain=flat['chain']; inverse=flat['inverse']
rows=m['source']; fs=flat['frames']; changed=flat['changed']
reps=geo['representatives']
def rational_matrix(a):
    return tuple(tuple(Fraction(str(v)) for v in row) for row in a.tolist())
responses={tuple(p['label']):rational_matrix(geo['evaluate'](p['word'])[1]) for p in reps}
packets={row.label:{'label':row.label,'source':row.source,'target':row.target,
                    'word':reps[i]['word'],'mass':row.mass} for i,row in enumerate(rows)}

def attach(row,frames):
    return chain(frames[row.target],responses[row.label],inverse(frames[row.source]))
for row in rows:
    for frames in (fs,changed):
        actual=attach(row,frames)
        check('typed-response-binding/'+str(row.label)+'/'+str(frames is changed),actual==flat['realization'](row,frames)[0])
        check('fixed-reference-decoding/'+str(row.label)+'/'+str(frames is changed),flat['decode'](actual,row.source,row.target,frames)==row.value)

pair_count=0
for family in m['indexed'](rows,'target').values():
    for a in family:
        for b in family:
            # a:s_a->t, return_b:t->s_b, b:s_b->t.
            check('typed-reference-return-port-chain/'+str((a.label,b.label)),a.target==b.target)
            _,_,br=flat['realization'](b,fs)
            actual=chain(attach(b,fs),br,attach(a,fs))
            word=packets[a.label]['word']+packets[b.label]['word']
            rho=rational_matrix(geo['evaluate'](word)[1])
            expected=chain(fs[a.target],rho,inverse(fs[a.source]))
            check('full-path-common-target-operation/'+str((a.label,b.label)),actual==expected)
            check('decoded-operation/'+str((a.label,b.label)),flat['decode'](actual,a.source,a.target,fs)==chain(b.value,flat['r'],a.value))
            pair_count+=1
check('all977-admitted-leaf-pairs-bound',pair_count==977)
# All source representatives are based A loops. A vertex-only functor cannot
# send that same A to every supplied source and target record port.
record_sources={row.source for row in rows}; record_targets={row.target for row in rows}
check('single-seed-vertex-endpoint-map-impossible',len(record_sources)>1 and len(record_targets)>1)
check('decorated-packets-retain137-distinct-labels',len(packets)==137)

profiles={}
for policy in ('inherited','common'):
    first=m['incoming_promotion'](rows,1,policy)
    second=m['incoming_promotion'](first,2,policy)
    retained=m['leaves'](second)
    check('T9-exact-labelled-endpoint-recovery/'+policy,retained==rows)
    check('T9-geometric-packet-recovery/'+policy,tuple(packets[row.label] for row in retained)==tuple(packets[row.label] for row in rows))
    check('T9-original-member-measure/'+policy,sum(row.mass for row in second)==137)
    check('T9-unchanged-J4/'+policy,m['read_at_four'](m['indexed'](second,'target'))==m['read_at_four'](m['indexed'](rows,'target')))
    # Group final leaf labels by generated target. This relation is retained
    # table wiring, not a scalar whose matching could select a constructor.
    blocks=[tuple(row.label for row in m['leaves']((family,))) for family in second]
    supported=sum(len(block)**2 for block in blocks)
    profiles[policy]={'first_rows':len(first),'final_rows':len(second),
                      'final_leaf_blocks':blocks,'supported_ordered_leaf_pairs':supported}
check('candidate-T9s-remain-distinct-after-full-response-binding',profiles['inherited']['final_rows']==32 and profiles['common']['final_rows']==1)
check('candidate-incidence-separation',profiles['inherited']['supported_ordered_leaf_pairs']==977 and profiles['common']['supported_ordered_leaf_pairs']==18769)
# A reproducible witness of a connection common admits and inherited excludes.
a=rows[0]; b=next(row for row in rows if row.target!=a.target)
check('cross-family-T9-selection-witness',a.target!=b.target)
result={
 'schema':'marici.nima.geometric-record-endpoint-binding.v1','verification_status':'pass',
 'checks':checks,'bound_leaf_records':137,'bound_common_target_compositions':pair_count,
 'source_interface':'labelled port-decorated based geometric paths, not bare seed vertices',
 'typed_map':'P_t rho(word) P_s^-1; reference=P_t P_s^-1; decoding=d P_t^-1 M P_s',
 'endpoint_binding_status':'complete conditional binding to supplied fixture ports and existing flat attachments',
 'bare_seed_endpoint_functor_status':'impossible for these all-A representatives and multiple record ports',
 'T9_profiles':profiles,
 'selection_witness':{'left_label':a.label,'right_label':b.label,'left_target':a.target,'right_target':b.target,
                      'inherited_admits':False,'common_admits':True},
 'intended_T9_status':'not selected by current source declarations or response/retention equations',
 'objective_complete':False,
 'remaining_selection':'Declare whether unlike original target fibres may share the next comparison port (or supply a different native constructor and endpoint table).',
 'scope':'Reuses both existing promotions and flat frame contract unchanged; does not derive record labels, weights, flatness or physical generator.',
 'inputs_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'check_geometric_fixture_representation.py',HERE/'check_flat_reference_attachment.py',HERE/'check_rung_transport_diagram.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} typed full-path/record binding checks')
print('137 decorated records and all977 admitted compositions bound; both T9 candidates retain original J4.')
print('Intended T9 remains a wiring selection: preserve32 target fibres or connect them into one.')
