# /// script
# dependencies = ["sympy"]
# ///
"""Conditional connectors witnessed by actual directed fixture record routes.

Route syntax is source data; its interpretation as connector transport is an
explicit extra role binding. Reference and actual comparison maps are NOT
identified. Neither interpretation is claimed to be a physical instrument.
"""
from collections import defaultdict, deque
from contextlib import redirect_stdout
from dataclasses import replace
from fractions import Fraction
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
from record_context_transport import Connector, ContextTransport
ROOT=HERE.parent
OUT=ROOT/'results/record-route-connector-admission.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    bound=runpy.run_path(str(HERE/'check_geometric_record_endpoint_binding.py'))
flat=bound['flat']; rows=bound['m']['source']; fs=flat['frames']
chain=flat['chain']; inverse=flat['inverse']
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
check('typed-source-records-fresh',bound['result']['verification_status']=='pass')
by_label={row.label:row for row in rows}
adjacency=defaultdict(list)
for row in rows: adjacency[row.source].append(row)
ports={row.target for row in rows}
check('existing-graph-endpoint-set',ports=={row.source for row in rows} and len(ports)==32)

def paths_from(start):
    found={start:()}; queue=deque([start])
    while queue:
        at=queue.popleft()
        for row in adjacency[at]:
            if row.target not in found:
                found[row.target]=found[at]+(row.label,)
                queue.append(row.target)
    return found
routes={(start,end):word for start in sorted(ports,key=repr) for end,word in paths_from(start).items()}
check('route_reachability_272_port_pairs',len(routes)==272)
check('route_reachability_preserves_branch',all(s[0]==t[0] for s,t in routes))
check('arrow_sector_is_strongly_connected',all((s,t) in routes for s in ports for t in ports if s[0]==t[0]=='a'))
check('state_ports_have_no_cross_connectors',all(s==t for s,t in routes if s[0]=='s'))

def realize(word,start):
    at=start; reference=flat['I']; actual=flat['I']
    for label in word:
        row=by_label[label]
        if at!=row.source: raise ValueError('Noncomposable record route')
        comparison,ref,_=flat['realization'](row,fs)
        reference=chain(ref,reference); actual=chain(comparison,actual)
        at=row.target
    return at,reference,actual

ctx=ContextTransport(flat)
for n,((start,end),word) in enumerate(routes.items()):
    at,reference,actual=realize(word,start)
    check('route-endpoints/'+str(n),at==end)
    check('reference-route-flatness/'+str(n),reference==chain(fs[end],inverse(fs[start])))
    if start!=end:
        check('nontrivial-connector-has-actual-directed-provenance/'+str(n),len(word)>0)
        ctx.declare(Connector('route-ref:'+str(n),start,end,reference,
                              ('conditional-reference-route-binding',word)))
        ctx.declare(Connector('route-actual:'+str(n),start,end,actual,
                              ('conditional-actual-comparison-route-binding',word)))
check('240_cross_port_routes_explicitly_declared',len(ctx.connectors)==480)
original={(a.label,b.label) for a in rows for b in rows if a.target==b.target}
admitted={(a.label,b.label) for a in rows for b in rows if (a.target,b.target) in routes}
check('all-original-contexts-preserved',original<=admitted and len(original)==977)
check('route-supported_leaf_pairs',len(admitted)==14657)
check('common_target_pairs_still_not_admitted',137**2-len(admitted)==4112)
check('added_route_supported_pairs',len(admitted-original)==13680)
# A third structural candidate is induced by this graph's route components.
# It does not select which response interpretation of those routes is intended.
m=bound['m']
first=m['incoming_promotion'](rows,1,'inherited')
def component(port): return ('a',) if port[0]=='a' else port
route_first=tuple(replace(family,target=('route-component',component(family.members[0].target))) for family in first)
route_final=m['incoming_promotion'](route_first,2,'inherited')
check('route_component_successor_has17_rows',len(route_final)==17)
check('route_component_successor_retains_original_rows',m['leaves'](route_final)==rows)
check('route_component_successor_preserves_original_J4',m['read_at_four'](m['indexed'](route_final,'target'))==m['read_at_four'](m['indexed'](rows,'target')))
route_support=set()
for family in route_final:
    leaves=m['leaves']((family,))
    route_support.update((a.label,b.label) for a in leaves for b in leaves)
check('route_component_successor_exact_reachability_support',route_support==admitted)

# Actual route response is not passive reference transport. Pick a genuine
# source route and existing operand records that exhibit that distinction.
witness=None
for n,((start,end),word) in enumerate(routes.items()):
    if start==end: continue
    a=next(row for row in rows if row.target==start)
    b=next(row for row in rows if row.target==end)
    passive=ctx.compose(a,b,'route-ref:'+str(n))
    active=ctx.compose(a,b,'route-actual:'+str(n))
    if active.decoded!=passive.decoded:
        witness={'left':a.label,'right':b.label,'start':start,'end':end,'word':word,
                 'reference_decoded':passive.decoded,'actual_decoded':active.decoded}
        check('source-route-comparison-is-not-reference-transport',True)
        check('both-interpretations-retain-directed-route',passive.connector.provenance[1]==active.connector.provenance[1]==word)
        break
check('actual-reference-response-separation-witness-found',witness is not None)
# Use an EXISTING carrier two-cycle to expose history invisible to flat
# reference endpoints. Reuse, do not perturb, its actual comparison maps.
a=next(row for row in rows if row.source==('a',0,0) and row.target==('a',2,2))
b=next(row for row in rows if row.source==a.target and row.target==a.source)
loop=(a.label,b.label)
at,reference,actual=realize(loop,a.source)
check('actual_record_loop_reference_identity',at==a.source and reference==flat['I'])
check('actual_record_loop_comparison_not_identity',actual!=flat['I'])
check('route_history_cannot_be_replaced_by_endpoints',realize((),a.source)[2]!=actual)
# No directed route exists between state and arrow sectors, nor between
# distinct isolated state ports. Empty-frame coordinates are not route proof.
missing=next((s,t) for s in ports for t in ports if (s,t) not in routes)
check('missing_route_is_not_supplied_by_flat_frames',missing[0] in fs and missing[1] in fs)

def stringify(value):
    if isinstance(value,tuple): return [stringify(x) for x in value]
    if isinstance(value,dict): return {k:stringify(v) for k,v in value.items()}
    if isinstance(value,Fraction): return str(value)
    return value
result={
 'schema':'marici.nima.record-route-connector-admission.v1','verification_status':'pass','checks':checks,
 'port_count':32,'reachable_ordered_port_pairs':272,'cross_port_route_witnesses':240,
 'original_leaf_pair_support':977,'route_supported_leaf_pair_support':14657,
 'added_leaf_pairs':13680,'still_missing_from_common_target':4112,
 'route_component_successor_rows':17,'route_component_successor_J4_unchanged':True,
 'reachability_components':'One strongly connected16-port arrow component;16 isolated state ports.',
 'response_separation_witness':stringify(witness),
 'existing_loop':{'labels':loop,'reference_holonomy_identity':True,'actual_response_identity':False},
 'missing_connector_port_pair':missing,
 'conditional_positive_result':'Actual directed record routes supply retained connector syntax within reachability components.',
 'role_binding_boundary':'Interpreting record references or actual comparison maps as connectors is explicit conditional data. Graph reachability does not authorize a physical pulse or identify either with intended T9.',
 'common_target_status':'Not generated by this existing record-route graph:4112 leaf pairs lack a route witness.',
 'intended_T9_identified':False,'objective_complete':False,
 'next_input':'If common collapse is intended, supply cross-component/state-port connector events and choose actual versus reference transport, retaining route history.',
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'record_context_transport.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} existing-record route connector checks')
print('Route support=14657 leaf pairs; common collapse still needs4112 unsupported pairs.')
print('Reference routes telescope; actual comparison route responses and loop histories do not disappear.')
