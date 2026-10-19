"""Exact finite policy/guard/phase tests; no cost valuation is inferred."""
from dataclasses import replace
from hashlib import sha256
import json
from itertools import product
from pathlib import Path
import sys
from electron_packet_interface import ROOT,Interface,ACTIONS,E,I,F,G0,G1,act,adj,gmm,sm
from packet_transport_policy import (GRID,CHARTS,EDGES,matrix,admit,cost_token,seed,step,ledger,validate)
CONTRACT=ROOT/'research/strominger/contracts/packet-transport-policy.v1.json'
def digest(p):return sha256(p.read_bytes()).hexdigest()
def reject(action,message):
    try:action()
    except ValueError as e: assert message in str(e),(message,str(e))
    else:raise AssertionError('accepted '+message)
def inner(x,y):
    from electron_packet_interface import gt,gm,gc
    return gt(gm(gc(a),b) for a,b in zip(x,y))
prior_path=ROOT/'research/strominger/results/electron-packet-extraction-v1.json'
prior=json.loads(prior_path.read_text(encoding='utf-8'));assert prior['status']=='pass'
pins=dict(prior['source_sha256']);pins[prior_path.relative_to(ROOT).as_posix()]=digest(prior_path)
for p in (CONTRACT,Path(__file__).resolve(),Path(__file__).with_name('packet_transport_policy.py').resolve(),ROOT/'research/voevodsky/checkers/check_electron_three_direction_trial.py'):
    key=p.relative_to(ROOT).as_posix()
    if key in pins:assert pins[key]==digest(p)
    pins[key]=digest(p)
assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale prerequisite'
f=Interface();contract=json.loads(CONTRACT.read_text(encoding='utf-8'))
assert contract['cost_semantics']['assigned_units'] is None
assert contract['cost_semantics']['primitive_realization']=='not supplied'
assert len(GRID)==27 and len(EDGES)==108
assert sum(c in ACTIONS for c in CHARTS.values())==15
ref=(G1,G0);origin=(F(0),)*3
native_edges=0;edge_records=[]
for u,v in EDGES:
    T=matrix(u,v);is_native=T in ACTIONS
    native_edges+=is_native
    assert gmm(adj(T),T)==I and matrix(v,u)==adj(T)
    W=gmm(gmm(f.K,T),f.D) # image lift, not its primitive implementation
    assert gmm(W,f.K)==gmm(f.K,T) and gmm(f.D,W)==gmm(T,f.D)
    s=seed('supplied_grid',ref,u);s1=step('supplied_grid',s,u,v)
    assert s1.spinor==act(CHARTS[v],ref)
    assert act(W,act(f.K,s.spinor))==act(f.K,s1.spinor)
    validate('supplied_grid',s1)
    if is_native: assert step('native_only',seed('native_only',ref,u),u,v).spinor==s1.spinor
    else:
        reject(lambda:step('native_only',seed('native_only',ref,u),u,v),'nonnative capability')
        reject(lambda:f.packet_step(f.extract(f.seed(ref)),T),'operation unavailable')
    reject(lambda:admit('supplied_grid',v,u,v),'source vertex guard')
    token=cost_token(T);assert token['numeric_primitive_cost'] is None and token['native']==is_native
    edge_records.append({'source':list(map(str,u)),'target':list(map(str,v)),'native':is_native,'cost_token':token['symbol']})
reachable={origin}
while True:
    expanded=reachable|{v for u,v in EDGES if u in reachable and matrix(u,v) in ACTIONS}
    if expanded==reachable:break
    reachable=expanded
assert len(reachable)==7 and native_edges==12
sectors=[]
for omitted in range(3):
    axes=[a for a in range(3) if a!=omitted]
    for signs in product((-1,1),repeat=2):
        A,B=(sm(s,E[a]) for a,s in zip(axes,signs))
        ab=gmm(A,B);ba=gmm(B,A)
        assert ab==sm(-1,ba) and gmm(adj(ab),ba)==sm(-1,I)
        za=act(ab,ref);zb=act(ba,ref)
        assert inner(za,za)==G1 and inner(za,zb)==(-F(1),F(0))
        routes=[]
        for order in (tuple(zip(axes,signs)),tuple(reversed(tuple(zip(axes,signs))))):
            s=seed('supplied_grid',ref,origin)
            for a,sign in order:
                v=list(s.vertex);v[a]=F(sign);v=tuple(v)
                s=step('supplied_grid',s,s.vertex,v)
            validate('supplied_grid',s);routes.append(s)
            u,v=s.edge_word[-1]
            assert CHARTS[v] not in ACTIONS and matrix(u,v) not in ACTIONS
            reject(lambda:admit('native_only',u,u,v),'nonnative capability')
        assert routes[0].spinor==routes[1].spinor and routes[0].vertex==routes[1].vertex
        assert routes[0].edge_word!=routes[1].edge_word
        assert len(ledger(routes[0].edge_word))==2
        assert any(not t['native'] for t in ledger(routes[0].edge_word))
        s=routes[0]
        for u,v in reversed(s.edge_word):s=step('supplied_grid',s,v,u)
        assert s.vertex==origin and s.spinor==ref and len(s.edge_word)==4 and len(ledger(s.edge_word))==4
        sectors.append({'omitted_axis':omitted,'signs':signs,'native_comparison':'-I','native_reference_pairing':['1','-1'],
                        'supplied_endpoints_agree':True,'supplied_histories_identified':False,'inverse_route_token_occurrences':4})
reject(lambda:admit('supplied_grid',origin,origin,origin),'edge domain')
reject(lambda:admit('unknown',origin,*EDGES[0]),'unknown policy')
base=seed('supplied_grid',ref,origin)
reject(lambda:validate('supplied_grid',replace(base,spinor=(G0,G1))),'chart state/history')
# Native closure means a nonnative corner cannot be produced by ANY finite native word.
assert all(gmm(a,b) in ACTIONS for a in ACTIONS for b in ACTIONS)
assert all(digest(ROOT/p)==h for p,h in pins.items())
checks={'policy_and_all_source_pins_frozen':True,'27_vertices_split15_native12_nonnative':True,
 'all108_edges_unitary_with_raw_logical_squares':True,'native_and_supplied_enabled_domains_are_distinct':True,
 'source_vertex_and_forged_state_guards_enforced':True,'all12_native_sectors_retain_minus_identity_reference_hostile':True,
 'all12_chart_sectors_agree_only_with_supplied_edge_task':True,'native_group_closure_excludes_nonnative_corner_words':True,
 'native_grid_reachability_from_origin_is_only7_of27_vertices':True,
 'inverse_restores_value_not_archive_or_execution_token_count':True,'all_edge_costs_symbolic_and_unvalued':True,
 'upstream_inputs_unchanged_no_native_producers_executed':True}
report={'schema':'marici.packet-transport-policy-check.v1','status':'pass','checks':checks,
 'grid_vertices':27,'directed_edges':108,'native_edges':native_edges,'supplied_nonnative_edges':108-native_edges,'native_reachable_grid_vertices_from_origin':len(reachable),
 'sectors':sectors,'edge_dictionary':edge_records,'source_sha256':pins,
 'resolution':'Native-only task retains the -I comparison. Supplied finite-grid branch is separate and conditional; it is not imported as a native or costed realization.',
 'cost_units':None,'primitive_cost_valuation':None,'native_protocol_transfers':144,
 'cost_boundary':'144 is the stored L/G/N support, not the cost of any one logical action or edge.',
 'formal_proof_recompiled':False,'physical_realization':False}
(ROOT/'research/strominger/results/packet-transport-policy-v1.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ('sectors','edge_dictionary','source_sha256')},indent=2))
