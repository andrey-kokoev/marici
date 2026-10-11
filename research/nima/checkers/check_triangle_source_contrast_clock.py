"""Test source-generated cross contrast under registered full-seed extension."""
from contextlib import redirect_stdout
from pathlib import Path
import io
import hashlib
import json
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_triangle_endpoint_spatial_reader.py'))
c=prior['composition']; ledger=c['ledger']; X=prior['X']
vertices='ABCD'
M=S.zeros(4)
for label,source,target in c['PACKETS']:
    M[vertices.index(target),vertices.index(source)]+=1
whole=ledger.retain_payload(ledger.root,(1,)*6)
left=ledger.compose_payloads(c['L'],c['R'])
right=ledger.compose_payloads(c['R'],c['L'])

def targets(payload):
    return S.Matrix([sum(value for path,value in zip(payload.paths,payload.values) if path[-1][1]==v)
                     for v in vertices])

checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

initial=targets(left)-targets(right)
check('actual-source-contrast',initial==S.Matrix([1,-1,-1,1]))
check('primitive-third-root-sector',(M*M+M+S.eye(4))*initial==S.zeros(4,1))
check('nontrivial-period',M*initial!=initial and M*M*initial!=initial)
check('exact-third-return',M**3*initial==initial)
check('two-dimensional-closed-contrast-space',S.Matrix.hstack(initial,M*initial).rank()==2)
check('aggregate-blind-throughout-cycle',all(sum(M**k*initial)==0 for k in range(3)))

observations=[]
a,b=2,3
initial_centroid_difference=X*initial/2
frame=c['child']
for tick in range(7):
    lc,rc=targets(left),targets(right)
    detail=lc-rc
    check('registered-count-evolution/'+str(tick),detail==M**tick*initial)
    check('equal-growing-channel-counts/'+str(tick),sum(lc)==sum(rc)==a)
    check('exact-three-phase-readout/'+str(tick),detail==M**(tick%3)*initial)
    q=X*detail/a
    observations.append({'tick':tick,'word_length':left.word_length,'each_channel_count':int(a),
                         'raw_endpoint_contrast':list(map(str,detail)),
                         'raw_spatial_contrast':list(map(str,X*detail)),
                         'centroid_difference':list(map(str,q))})
    if tick==3:
        check('normalized-position-does-not-return',q==initial_centroid_difference/4 and q!=initial_centroid_difference)
        check('whole-history-does-not-return',left.word_length==5 and len(left.paths)==8)
    # Independently compare registered stage extension to retained composition
    # for the first full period, preserving exact word/parent bindings.
    if tick<3:
        next_frame=ledger.successor(frame)
    new_left=ledger.compose_payloads(left,whole)
    new_right=ledger.compose_payloads(right,whole)
    for name,old,new in [('LR',left,new_left),('RL',right,new_right)]:
        parents,slots=ledger.deconstruct_payload(new)
        check('both-operand-histories/'+name+'/'+str(tick),parents[0] is old and parents[1] is whole)
        check('actual-endpoint-incidence/'+name+'/'+str(tick),targets(new)==M*targets(old))
        if tick<3:
            check('same-registered-successor-domain/'+name+'/'+str(tick),set(new.paths)<=set(next_frame.paths))
    if tick<3:frame=next_frame
    left,right=new_left,new_right
    a,b=b,a+b
norms=[(X*M**k*initial).dot(X*M**k*initial) for k in range(3)]
check('not-euclidean-rigid-rotation',norms==[16,40,40])
proof_path=ROOT/'results/agda-TriangleSourceContrastClock.json'
proof=json.loads(proof_path.read_text(encoding='utf-8-sig'))
check('fresh-formal-clock-proof',proof['passed'] and proof['ignore_interfaces'] and proof['inputs_stable_during_check'])
check('formal-source-current',proof['source_sha256']==hashlib.sha256((ROOT/'agda/TriangleSourceContrastClock.agda').read_bytes()).hexdigest())
# CONDITIONAL scheduling control: one sequential unit-duration event per
# newly extended child word, not an event emission claimed by the constructor.
first_cycle=sum(2*r['each_channel_count'] for r in observations[1:4])
second_cycle=sum(2*r['each_channel_count'] for r in observations[4:7])
check('sequential-event-count-not-isochronous',(first_cycle,second_cycle)==(32,136))
result={
    'schema':'marici.nima.triangle-source-contrast-clock.v1','status':'pass','checks':checks,
    'operation':'existing compose_payloads(current, full_original_seed), retaining both inputs; agrees with registered successor word domain',
    'incidence_matrix':[[int(v) for v in M.row(i)] for i in range(4)],
    'observations':observations,
    'exact_result':'the actual LR-RL count contrast occupies the primitive cube-root sector of source incidence and has least period three',
    'whole_boundary':'each channel grows with Fibonacci counts; complete path histories do not return',
    'readout_boundary':'raw endpoint contrast recurs; normalized centroid difference contracts; aggregate reader stays blind to the role difference',
    'metric_boundary':'spatial squared norms are 16,40,40, so this is not a rigid Euclidean oscillator or a constant kinetic-energy proof',
    'time_boundary':'three source-extension phases give a combinatorial phase counter; no physical duration, execution frequency or autonomous scheduling selected',
    'conditional_sequential_unit_event_cycles':[first_cycle,second_cycle],
    'formal_scope':'all-n least-three-period theorem for actual source incidence and initial native word-count contrast; arbitrary-length word-extension/reader intertwining remains tested rather than formally proved',
    'formal_receipt_sha256':hashlib.sha256(proof_path.read_bytes()).hexdigest(),
}
(ROOT/'results/triangle-source-contrast-clock.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact source-contrast recurrence checks')
print('Actual LR-RL contrast has least period THREE under existing full-seed continuation.')
print('Full histories grow; normalized spatial contrast does not return; no physical time scale inferred.')
