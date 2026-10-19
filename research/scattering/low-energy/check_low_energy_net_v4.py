"""Check the proposition graph and exactly refute its single-step seed conjecture.

This recomputes current exact/source certificates supporting the scoped analytic
results, without replaying source-owner scattering solvers. Historical v3 is
checked, not rewritten.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse
import copy
import hashlib
import json

from check_low_energy_net_v3 import validate as validate_history

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/scattering/low-energy'
CONTRACT=BASE/'contracts/low-energy-scattering-conjectures.v4.json'
RESULT=BASE/'results/low-energy-conjectures.v4.json'


def load(path):return json.loads(path.read_text(encoding='utf-8'))
def identity(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def multiply(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Q(0)) for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a):return list(map(list,zip(*a)))
def tensor(a,b):return [[x*y for x in ar for y in br] for ar in a for br in b]
def determinant(a):
    a=[row[:] for row in a];value=Q(1)
    for i in range(len(a)):
        p=next((p for p in range(i,len(a)) if a[p][i]),None)
        if p is None:return Q(0)
        if p!=i:a[p],a[i]=a[i],a[p];value=-value
        pivot=a[i][i];value*=pivot
        for j in range(i+1,len(a)):
            factor=a[j][i]/pivot
            for k in range(i+1,len(a)):a[j][k]-=factor*a[i][k]
            a[j][i]=Q(0)
    return value

def characteristic(a):
    n=len(a);b=identity(n);coefficients=[Q(1)]
    for k in range(1,n+1):
        b=multiply(a,b);c=-sum(b[i][i] for i in range(n))/k
        coefficients.append(c)
        for i in range(n):b[i][i]+=c
    assert all(not x for row in b for x in row)
    return coefficients


def validate(net):
    if net['schema']!='marici.scattering.low-energy-conjectures.v4':raise ValueError('schema')
    if net['physical_explanation_outcome'] is not None:raise ValueError('physical outcome not established')
    nodes={n['id']:n for n in net['conjectures']}
    if len(nodes)!=len(net['conjectures']):raise ValueError('duplicate proposition')
    required={'rim-threshold-regularity','three-port-asymptotic-completeness','glued-seed-two-factor-carrier'}
    if not required<=nodes.keys():raise ValueError('missing requested conjecture')
    incoming={k:[] for k in nodes};outgoing={k:[] for k in nodes};seen_edges=set()
    for e in net['edges']:
        key=(e['from'],e['to'],e['kind'])
        if key in seen_edges or e['from'] not in nodes or e['to'] not in nodes:raise ValueError('invalid edge')
        if e['kind'] not in ('premise','target_definition','successor_test') or not e['reason']:raise ValueError('untyped edge')
        if e['kind']=='premise' and nodes[e['from']]['status']=='refuted':raise ValueError('refuted assertion used as true premise')
        seen_edges.add(key);incoming[e['to']].append(e);outgoing[e['from']].append(e['to'])
    for n in nodes.values():
        if not all(n.get(k) for k in ('statement','quantifiers','falsifier','sources')):raise ValueError('task without proposition')
        # A quantified proposition may carry an executable test pointer;
        # its statement/quantifiers/falsifier above remain mandatory.
        if 'acceptance' in n:raise ValueError('work-package acceptance substituted for a proposition')
        if n['status'] not in ('open','conditional','refuted','established'):raise ValueError('unsupported resolution needs a mathematical certificate')
        established_certificates={
            'rim-threshold-regularity':'research/scattering/low-energy/results/rim-threshold.v1.json',
            'rim-packet-transmission-vanishes':'research/scattering/low-energy/results/rim-threshold.v1.json',
            'three-port-threshold-householder':'research/scattering/low-energy/results/three-port-threshold.v1.json',
            'no-regular-threshold-channel-intertwiner':'research/scattering/low-energy/results/threshold-comparison.v1.json',
            'three-port-no-singular-continuous-spectrum':'research/scattering/low-energy/results/no-singular-continuous.v1.json',
            'three-port-asymptotic-completeness':'research/scattering/low-energy/results/three-port-completeness.v1.json',
            'no-four-mode-single-excitation-port-embedding':'research/scattering/low-energy/results/channel-rank.v1.json',
            'three-port-bound-retention':'research/scattering/low-energy/results/bound-retention.v1.json'}
        if n['status']=='established' and (n['id'] not in established_certificates or n.get('result',{}).get('certificate')!=established_certificates[n['id']]):
            raise ValueError('unsupported established claim')
        if n['status']=='conditional' and not any(e['kind']=='premise' for e in incoming[n['id']]):raise ValueError('conditional without premises')
        if n['status']=='refuted' and (n['id'] not in ('glued-seed-two-factor-carrier','raw-macro-history-isometric-realization','two-tick-macro-factor-carrier') or not n.get('result')):raise ValueError('unverified refutation')
        if n['id']=='raw-macro-history-isometric-realization' and n['status']=='refuted':
            if n['result']['certificate']!='research/scattering/low-energy/results/raw-macro-readout.v1.json':raise ValueError('unknown C10 certificate')
    active=set();done=set()
    def visit(k):
        if k in active:raise ValueError('cycle')
        if k in done:return
        active.add(k)
        for child in outgoing[k]:visit(child)
        active.remove(k);done.add(k)
    for k in nodes:visit(k)
    # Check weak connectivity, without inventing implications between the
    # three independent starting conjectures.
    reached=set();queue=[next(iter(nodes))]
    while queue:
        k=queue.pop()
        if k in reached:continue
        reached.add(k);queue.extend(outgoing[k]);queue.extend(e['from'] for e in incoming[k])
    if reached!=nodes.keys():raise ValueError('disconnected conjectures')
    return nodes


def audit():
    net=load(CONTRACT);nodes=validate(net)
    from check_rim_threshold import audit as threshold_audit
    threshold=threshold_audit()
    if threshold!=load(BASE/'results/rim-threshold.v1.json'):raise ValueError('stale C1/C4 certificate')
    from check_raw_macro_readout import audit as macro_audit
    macro=macro_audit()
    if macro!=load(BASE/'results/raw-macro-readout.v1.json'):raise ValueError('stale C10 certificate')
    assert nodes['raw-macro-history-isometric-realization']['status']=='refuted'
    from check_macro_carrier import audit as carrier_audit
    carrier=carrier_audit()
    if carrier!=load(BASE/'results/macro-carrier.v1.json'):raise ValueError('stale C8 certificate')
    assert nodes['two-tick-macro-factor-carrier']['status']=='refuted'
    assert nodes['two-tick-macro-factor-carrier']['result']['certificate']=='research/scattering/low-energy/results/macro-carrier.v1.json'
    from check_three_port_threshold import audit as three_port_audit
    three_port=three_port_audit()
    if three_port!=load(BASE/'results/three-port-threshold.v1.json'):raise ValueError('stale C11 certificate')
    assert nodes['three-port-threshold-householder']['status']=='established'
    from check_threshold_comparison import audit as comparison_audit
    comparison=comparison_audit()
    if comparison!=load(BASE/'results/threshold-comparison.v1.json'):raise ValueError('stale C6 certificate')
    assert nodes['no-regular-threshold-channel-intertwiner']['status']=='established'
    from check_no_singular_continuous import audit as sc_audit
    sc=sc_audit()
    if sc!=load(BASE/'results/no-singular-continuous.v1.json'):raise ValueError('stale C9 certificate')
    assert nodes['three-port-no-singular-continuous-spectrum']['status']=='established'
    from check_three_port_completeness import audit as completeness_audit
    completeness=completeness_audit()
    if completeness!=load(BASE/'results/three-port-completeness.v1.json'):raise ValueError('stale C2 certificate')
    assert nodes['three-port-asymptotic-completeness']['status']=='established'
    from check_channel_rank import audit as channel_rank_audit
    channel_rank=channel_rank_audit()
    if channel_rank!=load(BASE/'results/channel-rank.v1.json'):raise ValueError('stale C7 certificate')
    assert nodes['no-four-mode-single-excitation-port-embedding']['status']=='established'
    from check_bound_retention import audit as retention_audit
    retention=retention_audit()
    if retention!=load(BASE/'results/bound-retention.v1.json'):raise ValueError('stale C5 certificate')
    assert nodes['three-port-bound-retention']['status']=='established'
    history=load(ROOT/net['historical_work_plan']);pins=load(ROOT/history['source_pins'])
    validate_history(history,pins)
    for p,h in pins['source_sha256'].items():
        if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h:raise ValueError('historical source changed: '+p)
    model=net['models']['glued_one_step'];candidate=load(ROOT/model['candidate'])
    occurrences=[(cycle[i],cycle[i+1]) for cycle in candidate['primitive_cycles'].values() for i in range(len(cycle)-1)]
    assert len(occurrences)==10 and len(set(occurrences))==10
    K=[[Q(a[1]==b[0]) for a in occurrences] for b in occurrences]
    T=[[Q(x) for x in row] for row in model['T_gamma']];G=[[Q(x) for x in row] for row in model['G_gamma']]
    assert multiply(multiply(T,T),T)==identity(2)
    assert multiply(multiply(transpose(T),G),T)==G and determinant(G)>0 and G[0][0]>0
    U=tensor(T,T);target_metric=tensor(G,G)
    assert multiply(multiply(U,U),U)==identity(4) and determinant(target_metric)>0
    K3=multiply(multiply(K,K),K)
    defect=[[K3[i][j]-Q(i==j) for j in range(10)] for i in range(10)]
    det=determinant(defect);coefficients=characteristic(K)
    assert det==Q(-64) and coefficients==list(map(Q,[1,0,-2,0,0,-2,-1,0,0,0,0]))
    assert nodes['glued-seed-two-factor-carrier']['status']=='refuted'
    # Linear-algebra certificates used by the conditional comparison claims.
    # Householder representatives have the same +/- eigenspaces for any
    # nonzero normalized port zero-mode vector; no source eigenvector is fit.
    householder=[[-1,0,0],[0,1,0],[0,0,1]]
    assert determinant([[Q(x) for x in row] for row in householder])==-1
    assert householder[0][0]!=householder[1][1]
    assert len(target_metric)==4>3
    # Integrity tests specifically reject fake wiring and evidence-as-proof.
    refused=[]
    for name in ('false_premise','work_area','unproved_promotion','cycle','physical_outcome'):
        bad=copy.deepcopy(net)
        if name=='false_premise':
            next(e for e in bad['edges'] if e['kind']=='target_definition')['kind']='premise'
        elif name=='work_area':bad['conjectures'][0].pop('quantifiers')
        elif name=='unproved_promotion':bad['conjectures'][0]['status']='proved'
        elif name=='cycle':bad['edges'].append({'from':'rim-packet-transmission-vanishes','to':'rim-threshold-regularity','kind':'premise','reason':'hostile cycle'})
        else:bad['physical_explanation_outcome']='proved'
        try:validate(bad)
        except ValueError:refused.append(name)
        else:raise AssertionError('invalid graph accepted: '+name)
    paths={p for n in nodes.values() for p in n['sources']}|set(pins['source_sha256'])|set(threshold['source_sha256'])|set(macro['source_sha256'])|set(carrier['source_sha256'])|set(three_port['source_sha256'])|set(comparison['source_sha256'])|set(sc['source_sha256'])|set(completeness['source_sha256'])|set(channel_rank['source_sha256'])|set(retention['source_sha256'])|{
        'research/scattering/low-energy/results/bound-retention.v1.json',
        'research/scattering/low-energy/results/channel-rank.v1.json',
        'research/scattering/low-energy/results/three-port-completeness.v1.json',
        'research/scattering/low-energy/results/no-singular-continuous.v1.json',
        'research/scattering/low-energy/results/threshold-comparison.v1.json',
        'research/scattering/low-energy/results/three-port-threshold.v1.json',
        'research/scattering/low-energy/results/macro-carrier.v1.json',
        'research/scattering/low-energy/results/raw-macro-readout.v1.json',
        'research/scattering/low-energy/results/rim-threshold.v1.json',
        CONTRACT.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix(),
        net['historical_work_plan'],history['source_pins']}
    return {
        'schema':'marici.scattering.low-energy-conjectures-check.v4',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(paths)},
        'conjectures':{n['label']:{'id':n['id'],'status':n['status']} for n in nodes.values()},
        'graph':{'nodes':len(nodes),'edges':len(net['edges']),'weakly_connected':True,'acyclic':True,
                 'target_definition_edge_is_not_a_truth_premise':True,
                 'successor_test_edge_is_not_a_truth_premise':True},
        'C3_exact_refutation':{'model':'pinned ten-occurrence graph, one primitive extension per tick',
                              'primitive_occurrences':[list(e) for e in occurrences],
                              'K':[[str(x) for x in row] for row in K],
                              'characteristic_coefficients_descending':list(map(str,coefficients)),
                              'det_K_cubed_minus_identity':str(det),'target_U_cubed_is_identity':True,
                              'deduction':'KJ=JU implies (K³-I)J=J(U³-I)=0; invertibility forces J=0, contradicting rank four',
                              'metric_independent_obstruction':True,
                              'all_possible_source_operations_refuted':False},
        'conditional_comparison_checks':{'C6_Householder_eigenvalues':[-1,1,1],
                                         'C6_rim_limit_if_C1':'-I4',
                                         'C6_scalar_phase_cannot_match_both_signs':True,
                                         'C7_target_rank':4,'C7_single_excitation_fiber_rank_if_C2':3},
        'open_claims_proved_by_this_checker':False,
        'C1_C4_exact_certificate_recomputed':True,
        'C5_preparation_overlap_certificate_recomputed':True,
        'C7_rank_certificate_recomputed':True,
        'C2_five_mode_and_finite_rank_certificate_recomputed':True,
        'C9_source_polynomial_certificate_recomputed':True,
        'C6_certificate_recomputed':True,
        'C6_limiting_operator_defect_squared_lower_bound':2,
        'C11_exact_certificate_recomputed':True,
        'C11_cyclic_dimension':three_port['cyclic_dimension_under_K_alone'],
        'C8_exact_certificate_recomputed':True,
        'C8_det_D_minus_identity':carrier['det_D_minus_identity'],
        'C10_exact_certificate_recomputed':True,
        'C10_norm_obstruction':macro['witness'],
        'C5_argument_scope':'conditional mathematical consequence, not independent solver replay',
        'source_owner_scattering_suites_replayed':False,
        'historical_v3_and_pinned_sources_unchanged':True,
        'invalid_graphs_refused':refused,
        'physical_explanation_outcome':None
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();result=audit();text=json.dumps(result,indent=2)+'\n'
    if args.check:
        if not RESULT.exists() or RESULT.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale conjecture receipt')
    else:
        RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print(json.dumps({'status':'pass','conjectures':result['graph']['nodes'],'edges':result['graph']['edges'],
                      'exact_result':'C3 refuted in single-step model: det(K³-I)=-64',
                      'C1_C4':'established: exact threshold certificate','C2':result['conjectures']['C2']['status'],'historical_solver_replay':False}))


if __name__=='__main__':main()
