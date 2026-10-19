"""Scoped integration review: conditional target coverage is not physical admission."""
import argparse
import copy
import json
from pathlib import Path
import check_physics_geometric_candidate as G

ROOT=G.ROOT
CONTRACT='research/nima/contracts/physics-conditional-model-assembly.v1.json'
NET='research/conjecture_net/contracts/programme-hierarchy.v18.json'
TARGETS={'reciprocal-lossy-cavity-ordered-response','finite-dead-time-detector-records'}


def validate(c):
    G.require(c['decision']=='accept_conditional_model_assembly_only' and c['source_witness_id']=='passive-port-fock-memory.v1','scope/source')
    G.require(c['physical_realization_admitted'] is False and c['native_source_law_selected'] is False,'physical/source promotion')
    coverage={r['target']:r for r in c['target_coverage']}
    G.require(len(coverage)==len(c['target_coverage']) and set(coverage)==TARGETS,'conditional target coverage')
    G.require(all(r['domain'] and r['map'] and r['premise_status'].startswith('imported_')
                  and r['physical_binding'] is False for r in coverage.values()),'target premise promotion')
    G.require(len(c['blockers'])==4 and len(c['assembly_rules'])==6,'lost assembly boundaries')
    G.require(len(c['packets'])==7 and len({p['result'] for p in c['packets']})==7,'packet coverage')


def graph_guard(net):
    by={n['id']:n for n in net['conjectures']}
    model=by['conditional-model-assembly']
    G.require(model['status']=='resolved' and model['verdict']=='constructed' and model['outcome'] is None,'conditional disposition')
    law=by['dynamics-source-selection']
    G.require(law['status']=='deferred' and law['verdict']=='open' and law['blocker'] and law['reopening_condition'],'native source gap hidden')
    for node in ('carrier-and-geometric-dynamics','instrument-common-source-binding','physical-sector-realizations','same-witness-sector-transport','cross-sector-compatibility'):
        G.require(by[node]['status']=='open','conditional review promoted physical gate: '+node)
    G.require(by['carrier-and-geometric-dynamics']['input_requirements']['dynamics-source-selection']=='witness','native law witness gate weakened')
    G.require(net['target_realization_records']==[] and not any(i['id']=='reviewed-common-witness-assembly' for i in net['available_interfaces']),'physical target/root review fabricated')


def main():
    p=argparse.ArgumentParser();p.add_argument('--pin',action='store_true');args=p.parse_args()
    c=G.load(CONTRACT);validate(c)
    paths={CONTRACT}|set(c['source_evidence'])|{q[k] for q in c['packets'] for k in ('result','checker')}
    pin=ROOT/c['source_pins']
    if args.pin:
        G.require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:G.sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=G.load(c['source_pins']);G.require(set(pins['source_sha256'])==paths,'pin coverage')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source drift: '+path)
    admissions=G.load('research/nima/contracts/physics-interface-geometry-admission.v1.json')
    G.require(admissions['source_register_supplement']['source_instance_id']==c['source_witness_id'],'register supplement mismatch')
    reviewed=[]
    for q in c['packets']:
        receipt=G.load(q['result'])
        G.require(receipt['status']=='pass' and receipt['checker_sha256']==G.sha(q['checker']),'stale/failed packet: '+q['result'])
        for path,h in receipt['source_sha256'].items():G.require(G.sha(path)==h,'packet dependency drift: '+path)
        reviewed.append(q['result'])
    law=G.load('research/nima/contracts/physics-source-law-premise-audit.v1.json')
    G.require(not law['native_source_law_selected'] and all(not p['supplied'] for p in law['required_source_inputs']),'source gaps changed without successor review')
    geometry=G.load(c['packets'][0]['result']);histories=G.load(c['packets'][3]['result']);domain=G.load(c['packets'][4]['result']);complex_routes=G.load(c['packets'][5]['result'])
    G.require(geometry['source_id']==c['source_witness_id'] and geometry['spectator_coherence_preserved'],'carrier geometry')
    G.require(histories['full_detector_histories']==252 and histories['assembly_domain_guard'],'detector coverage/domain guard')
    G.require(domain['maximal_safe_dimension']==52 and domain['independent_schedule_constraints']==3,'candidate schedule domain')
    G.require(complex_routes['complex_operator_basis_size']==242 and complex_routes['imaginary_coherence_preserved'],'complex overlap coverage')
    net=G.load(NET);graph_guard(net)
    rejected=[]
    for name in ('physical-promotion','derived-law-promotion','missing-target','lost-boundaries'):
        bad=copy.deepcopy(c)
        if name=='physical-promotion':bad['physical_realization_admitted']=True
        elif name=='derived-law-promotion':bad['target_coverage'][0]['premise_status']='native_derived'
        elif name=='missing-target':bad['target_coverage'].pop()
        else:bad['blockers']=[]
        try:validate(bad)
        except ValueError:rejected.append(name)
        else:raise AssertionError('accepted '+name)
    for name in ('native-law-gate-bypass','physical-assembly-bypass','fabricated-target-record'):
        bad=copy.deepcopy(net);by={n['id']:n for n in bad['conjectures']}
        if name=='native-law-gate-bypass':by['carrier-and-geometric-dynamics']['input_requirements']['dynamics-source-selection']='knowledge'
        elif name=='physical-assembly-bypass':by['physical-sector-realizations']['status']='resolved'
        else:bad['target_realization_records']=[{'target':'reciprocal-lossy-cavity-ordered-response'}]
        try:graph_guard(bad)
        except ValueError:rejected.append(name)
        else:raise AssertionError('accepted '+name)
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source changed during review')
    out={'schema':c['schema'],'status':'pass','decision':c['decision'],'reviewed_packets':reviewed,
         'conditional_target_coverage':sorted(TARGETS),'source_witness_id':c['source_witness_id'],
         'physical_realization_admitted':False,'native_source_law_selected':False,
         'rejected_promotions':rejected,'source_sha256':pins['source_sha256'],'checker_sha256':G.sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
