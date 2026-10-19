# /// script
# dependencies = ["sympy"]
# ///
"""Executable separation of transport and explicitly witnessed new contexts."""
from contextlib import redirect_stdout
from dataclasses import replace
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
from record_context_transport import Connector, ContextTransport, T9_exact_domain
ROOT=HERE.parent
OUT=ROOT/'results/explicit-context-transport.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    audit=runpy.run_path(str(HERE/'check_geometric_record_endpoint_binding.py'))
flat=audit['flat']; m=audit['m']; rows=m['source']
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def rejects(name,thunk):
    try: thunk()
    except (ValueError,AssertionError): check(name,True)
    else: raise AssertionError(name)
ctx=ContextTransport(flat)
a=rows[0]
b=next(row for row in rows if row.target!=a.target)
fs=flat['frames']; chain=flat['chain']; inv=flat['inverse']
# All old contexts still work without a connector; none is added by flatness.
pair_count=0
for family in m['indexed'](rows,'target').values():
    for left in family:
        for right in family:
            result=ctx.compose(left,right)
            check('old-context-response/'+str((left.label,right.label)),result.decoded==chain(right.value,flat['r'],left.value))
            check('old-context-endpoints/'+str((left.label,right.label)),(result.source,result.target)==(left.source,right.target) and result.connector is None)
            pair_count+=1
check('all977-original-contexts-preserved',pair_count==977)
rejects('flat-frames-do-not-admit-cross-target-context',lambda:ctx.compose(a,b))
rejects('undeclared-connector-rejected',lambda:ctx.compose(a,b,'missing'))
K=chain(fs[b.target],inv(fs[a.target]))
connector=Connector('declared-flat-bridge',a.target,b.target,K,
                    ('explicit-test-declaration','existing-flat-port-frames'))
ctx.declare(connector)
result=ctx.compose(a,b,connector.label)
check('new-context-has-correct-endpoints',(result.source,result.target)==(a.source,b.target))
check('new-context-retains-exact-witness',result.connector==connector)
check('new-context-retains-both-operands',result.operands==(a.label,b.label))
check('declared-flat-bridge-numerical-law',result.decoded==chain(b.value,flat['r'],a.value))
rejects('connector-cannot-be-used-in-reverse-without-declaration',lambda:ctx.compose(b,a,connector.label))
rejects('duplicate-connector-label-rejected',lambda:ctx.declare(connector))
rejects('empty-provenance-rejected',lambda:ctx.declare(replace(connector,label='no-proof',provenance=())))
# Same coordinate effect does not identify separately retained declarations.
other=replace(connector,label='second-history',provenance=('independent-test-declaration',))
ctx.declare(other)
other_result=ctx.compose(a,b,other.label)
check('equal-effects-preserve-distinct-witnesses',other_result.decoded==result.decoded and other_result.connector!=result.connector)
# An active response in the bridge is a DIFFERENT operation, not passive
# transport. This diagnostic verifies it cannot silently retain the old law.
H=flat['H']
active=Connector('active-bridge-control',a.target,b.target,chain(fs[b.target],H,inv(fs[a.target])),('declared-active-control',))
ctx.declare(active)
active_result=ctx.compose(a,b,active.label)
check('active-bridge-changes-fixed-decoded-response',active_result.decoded!=result.decoded)
check('active-bridge-law',active_result.decoded==chain(b.value,flat['r'],H,a.value))
selected=T9_exact_domain(rows,m)
check('transport-candidate-keeps32-families',len(selected)==32)
check('transport-candidate-preserves-original-records',m['leaves'](selected)==rows)
check('transport-candidate-preserves-J4',m['read_at_four'](m['indexed'](selected,'target'))==m['read_at_four'](m['indexed'](rows,'target')))
check('new-context-does-not-mutate-transport-source',rows==m['source'] and m['leaves'](selected)==rows)
# A single target-port bridge admits only its stated directional fibre pair,
# not all137 squared pairs. Two declarations with the same endpoints do not
# create new extensional support beyond that same pair of fibres.
added=[(left.label,right.label) for left in rows for right in rows if (left.target,right.target)==(a.target,b.target)]
check('connector-admission-is-local-not-common-collapse',0<len(added)<18769-977)
result_json={
 'schema':'marici.nima.explicit-context-transport.v1','verification_status':'pass','checks':checks,
 'original_supported_pairs':977,'single_bridge_added_pairs':len(added),
 'witness':{'left':a.label,'right':b.label,'source_target':a.target,'destination_target':b.target},
 'transport_contract':'T9_exact_domain uses existing inherited promotion twice; no cross-target comparison is inferred.',
 'context_creation_contract':'A labelled, endpoint-matching invertible connector with retained provenance must be explicitly declared; output retains operands and witness.',
 'typing':'a:s_a->t_a; connector:t_a->t_b; return_b:t_b->s_b; b:s_b->t_b; composite:s_a->t_b.',
 'flat_bridge_decoding':'C_b r C_a','active_bridge_decoding':'C_b r H C_a',
 'intended_T9_status':'Conservative exact-domain candidate implemented, not operator-confirmed physical T9.',
 'connector_status':'Test declarations only, not source-derived physical instruments or authority.',
 'objective_complete':False,
 'next_operational_input':'An actual source constructor or experimental task must supply connector admission/provenance if context creation is intended.',
 'inputs_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'record_context_transport.py')}}
OUT.write_text(json.dumps(result_json,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} explicit-context transport checks')
print('Original977 comparisons retained; cross-target comparisons require explicit connector witnesses.')
print('Equal effects retain different provenance; active connectors change decoded responses rather than retuning transport.')
