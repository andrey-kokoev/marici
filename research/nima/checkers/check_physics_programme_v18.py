"""Central physics research graph: typed ports, live prerequisite and frontier checks."""
import argparse
import copy
import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'research/conjecture_net'))
from graph_metrics import MetricAction, MetricGraph
from admit_structural_overlap import check as check_live_overlap

CONTRACT = 'research/conjecture_net/contracts/programme-hierarchy.v18.json'
CURRENT = 'research/conjecture_net/contracts/physics-programme-current.v1.json'
RESULT = ROOT/'research/nima/results/physics-programme-v18-validation.json'
PORTS = ROOT/'research/nima/results/physics-programme-v18-ports.json'
DASHBOARD = ROOT/'research/conjecture_net/PHYSICS-FRONTIER.md'
PRINCIPAL = {'carrier-and-geometric-dynamics','physical-sector-realizations',
             'cross-sector-compatibility','empirical-recovery','falsifiable-explanatory-constraint'}
PORT_TYPES = {'knowledge':'scoped_research_knowledge','witness':'constructed_witness',
              'counterexample':'scoped_rejection'}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))


def sha(path):
    return sha256((ROOT/path).read_bytes()).hexdigest()


def sources(c):
    catalog = load(c['target_catalog'])
    return ({p for a in c['artifacts'] for p in a['paths']} |
            {c['target_catalog']} | {t['source'] for t in catalog['targets']})


def output_available(n, port):
    return n['status'] == 'resolved' and (port == 'knowledge' or
        (port == 'witness' and n['verdict'] == 'constructed') or
        (port == 'counterexample' and n['verdict'] == 'rejected'))


def blockers(n, by, interfaces):
    return ([f'{dep}:{port}' for dep,port in n['input_requirements'].items()
             if not output_available(by[dep],port)] +
            ['interface:'+x for x in n['requires'] if x not in interfaces] +
            ([n['blocker']] if n['status'] == 'deferred' else []))


def effective_nodes(c, catalog):
    nodes = copy.deepcopy(c['conjectures'])
    by = {n['id']:n for n in nodes}
    targets = {t['id']:t for t in catalog['targets']}
    for target in c['selected_physical_targets']:
        require(target in targets, 'unknown selected target')
        for binding in targets[target]['required_bindings']:
            by['physical-sector-realizations']['input_requirements'][binding] = 'witness'
    return nodes


def validate(c, pins, catalog):
    nodes = effective_nodes(c, catalog); by = {n['id']:n for n in nodes}
    status_map = {'open':'active','resolved':'resolved','deferred':'pruned'}
    require(all(n['status'] in status_map for n in nodes),'invalid status')
    MetricGraph(tuple(MetricAction(n['id'],frozenset(n['input_requirements']),
        status=status_map[n['status']]) for n in nodes)).validate()
    artifacts = {a['id'] for a in c['artifacts']}
    require(len(artifacts) == len(c['artifacts']),'duplicate artifact')
    definitions = {d['id']:d for d in c['interface_definitions']}
    interfaces = {}
    for i in c['available_interfaces']:
        require(i['id'] in definitions and i['id'] not in interfaces,'unknown/duplicate interface')
        require(i['type'] == definitions[i['id']]['type'] and i['evidence'] and
                set(i['evidence']) <= artifacts and i['review'],'untyped interface admission')
        interfaces[i['id']] = i
    for n in nodes:
        require(n['branch'] in PRINCIPAL|{'root'},'unknown branch')
        require(n['owner'].startswith('marici.') and n['statement'] and n['scope'] and
                n['acceptance'] and n['falsifier'],'missing typed obligation')
        require(set(n['evidence']) <= artifacts,'unknown evidence')
        require(set(n['requires']) <= set(definitions),'unknown external port')
        require(set(n['input_requirements'].values()) <= set(PORT_TYPES),'bad port type')
        if n['status'] == 'resolved':
            require(n['verdict'] in {'constructed','rejected'} and n['evidence'],'unsupported disposition')
            require(not blockers(n,by,interfaces),'resolved with unavailable input')
        else:
            require(n['verdict'] == 'open' and n['next_action'] and n['deliverable'],'unactionable task')
        if n['status'] == 'deferred':
            require(n['blocker'] and n['reopening_condition'],'untyped deferral')
        if n['id'] != 'accepted-finite-overlap':
            require(n['outcome'] is None,'unreviewed formal outcome')
    accepted = by['accepted-finite-overlap']
    require(accepted['outcome'] == '++' and accepted['verdict'] == 'constructed' and
            accepted['evidence'] == ['finite-overlap'],'accepted scope lost')
    require(by['native-source-bridge-obstruction']['verdict'] == 'rejected','lost bridge rejection')
    root = by[c['objective']['target']]
    require(root['id'] == c['root']['id'] == 'relational-carrier-physical-explanation','root id')
    require(c['root']['outcome'] is None and c['objective']['outcome'] is None,'root promotion')
    require(root['input_requirements'] == {p:'witness' for p in PRINCIPAL},'five-obligation root gate')
    require(root['requires'] == ['reviewed-common-witness-assembly'],'root review bypass')
    require(by['physical-sector-realizations']['requires'] == ['reviewed-physical-target-scope'],'target review bypass')
    require(by['held-out-model-comparison']['requires'] == ['calibrated-independent-records'],'data authority bypass')
    require(by['empirical-recovery']['input_requirements'] == {'held-out-model-comparison':'witness'},'empirical bypass')
    require(by['cross-sector-compatibility']['input_requirements']['same-witness-sector-transport'] == 'witness','overlap bypass')
    require(by['falsifiable-explanatory-constraint']['input_requirements']['identifiability-and-robustness-test'] == 'witness','identifiability bypass')
    targets = {t['id']:t for t in catalog['targets']}
    require(len(targets) == len(catalog['targets']),'duplicate target')
    selected = set(c['selected_physical_targets'])
    require(len(selected) == len(c['selected_physical_targets']) and selected <= set(targets),'target selection')
    require(all(targets[t]['class'] == 'physical_target_candidate' for t in selected),'structural result used as physical target')
    if selected:
        require('reviewed-physical-target-scope' in interfaces,'selected targets without scope review')
    if 'reviewed-physical-target-scope' in interfaces:
        review = interfaces['reviewed-physical-target-scope']
        require(selected and set(review['targets']) == selected and
                review['catalog_sha256'] == sha(c['target_catalog']),'target review scope drift')
        expected_digest = sha256(json.dumps(sorted(selected),sort_keys=True,separators=(',',':')).encode()).hexdigest()
        require(review['target_set_sha256'] == expected_digest,'target-set digest drift')
        require(review['charter'] in sources(c) and review['charter_sha256'] == sha(review['charter']),
                'target charter source drift')
        charter = load(review['charter'])
        require(set(charter['selected_physical_targets']) == selected and
                {t['id'] for t in charter['targets']} == selected and
                charter['catalog'] == c['target_catalog'],'charter target coverage')
        require(output_available(by['source-target-charter'],'witness'),'scope admitted before charter disposition')
    for t in targets.values():
        require(set(t['required_bindings']) <= set(by) and (ROOT/t['source']).is_file(),'target binding/source')
    realized = {}
    for record in c['target_realization_records']:
        t = record['target']
        require(t in selected and t not in realized,'unknown/duplicate realization')
        require(record['source_witness_id'] and record['scope'] and record['evidence'] and
                set(record['evidence']) <= artifacts,'untyped target witness')
        require(all(output_available(by[b],'witness') for b in targets[t]['required_bindings']),'target-specific binding bypass')
        realized[t] = record
    if by['physical-sector-realizations']['status'] == 'resolved':
        require(selected and set(realized) == selected,'incomplete physical target coverage')
        require(len({r['source_witness_id'] for r in realized.values()}) == 1,'different physical source witnesses')
    if by['cross-sector-compatibility']['status'] == 'resolved':
        require(c['overlap_records'],'missing overlap records')
        for r in c['overlap_records']:
            require(set(r['targets']) <= selected and r['common_domain'] and r['comparison'] and
                    r['evidence'] and set(r['evidence']) <= artifacts,'untyped overlap record')
    if by['empirical-recovery']['status'] == 'resolved':
        require({r['target'] for r in c['empirical_test_records']} == selected and selected,'empirical coverage')
        for r in c['empirical_test_records']:
            require(r['dataset'] and r['protocol'] and r['uncertainty'] and r['decision'] and
                    r['fitting_validation_disjoint'] is True,'empirical record contract')
    parent = load(c['parent']['contract'])
    require(c['parent']['node'] in {n['id'] for n in parent['conjectures']},'parent attachment')
    for link in c['contribution_nets']:
        require(set(link['consumers']) <= set(by) and link['transport_required'] and
                (ROOT/link['contract']).is_file(),'bad contribution binding')
    frontier = [n['id'] for n in nodes if n['status'] == 'open' and not blockers(n,by,interfaces)]
    require(frontier == c['frontier'] and set(c['priority_order']) == set(frontier),'stale frontier/priority')
    require(set(pins['source_sha256']) == sources(c),'pin coverage')
    for path,digest in pins['source_sha256'].items():
        require((ROOT/path).resolve().is_relative_to(ROOT) and sha(path) == digest,'source drift: '+path)
    legacy = load(c['predecessor'])
    require(legacy['root']['id'] == root['id'] and legacy['root']['outcome'] is None,'legacy root changed')
    return by,interfaces,frontier


def port_graph(c,by,interfaces):
    links = []
    for n in by.values():
        for dep,port in n['input_requirements'].items():
            links.append({'from':dep+':'+port,'to':n['id']+':requires:'+dep,
                          'type':PORT_TYPES[port],'available':output_available(by[dep],port),
                          'relation':'research_prerequisite_requires_scoped_transport'})
        for interface in n['requires']:
            links.append({'from':'external:'+interface,'to':n['id']+':requires:'+interface,
                          'type':next(x['type'] for x in c['interface_definitions'] if x['id']==interface),
                          'available':interface in interfaces,'relation':'reviewed_external_witness'})
    return {'schema':'marici.physics-programme.ports.v18','contract':CONTRACT,
        'nodes':[{'id':n['id'],'status':n['status'],'outputs':[
            {'id':p,'type':t,'available':output_available(n,p)} for p,t in PORT_TYPES.items()]} for n in by.values()],
        'connections':links,'contribution_nets':c['contribution_nets']}


def dashboard(c,by,interfaces,live):
    lines = ['# Central physics research frontier','',
        'Generated by `research/nima/checkers/check_physics_programme_v18.py` from the v18 contract. Edit the contract and rerun the checker.','',
        '## Current work','', '| Priority | Task | Suggested lead | Deliverable |','|---|---|---|---|']
    for rank,key in enumerate(c['priority_order'],1):
        n = by[key]; lines.append(f"| {rank} | `{key}` | {n['owner']} | {n['deliverable']} |")
    if c.get('validation_notices'):
        lines += ['', '## Validation notices', ''] + ['- '+notice for notice in c['validation_notices']]
    lines += ['', '## Principal obligations','', '| Obligation | Status | Immediate inputs |','|---|---|---|']
    for n in by.values():
        if n['id'] in PRINCIPAL:
            lines.append(f"| {n['id']} | {n['status']} | {', '.join(n['input_requirements'])} |")
    lines += ['', '## Deferred branches','', '| Task | Missing ingredient | Reopening condition |','|---|---|---|']
    for n in by.values():
        if n['status']=='deferred':
            lines.append(f"| {n['id']} | {n['blocker']} | {n['reopening_condition']} |")
    lines += ['', '## Evidence and scope','',
        '- Accepted finite structural overlap: live admission dependency check passed; existing ++ retained.',
        '- Physical target selection: '+(', '.join(c['selected_physical_targets']) or 'pending reviewed selection from the current target catalog')+'.',
        '- Root outcome: unassigned. Scientific source suites are not replayed by this structural check.',
        '- Exact source snapshot and all typed connections are recorded in the validation and ports results.',
        '', '## Full work inventory','', '| Node | Status/verdict | Lead | Missing prerequisite ports |','|---|---|---|---|']
    for n in by.values():
        lines.append(f"| `{n['id']}` | {n['status']}/{n['verdict']} | {n['owner']} | {'; '.join(blockers(n,by,interfaces)) or 'none'} |")
    return '\n'.join(lines)+'\n'


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--pin',action='store_true'); args=parser.parse_args()
    c=load(CONTRACT); catalog=load(c['target_catalog']); pinpath=ROOT/c['source_pins']
    if args.pin:
        require(not pinpath.exists(),'refusing implicit re-pin')
        data={p:sha(p) for p in sorted(sources(c))}
        pinpath.write_text(json.dumps({'schema':'marici.physics-programme.source-pins.v18','source_sha256':data},indent=2)+'\n',encoding='utf-8')
    pins=load(pinpath); by,interfaces,frontier=validate(c,pins,catalog)
    hostile=[]
    for name in ('cycle','unknown-node','bad-port','rejection-as-witness','lost-rejection','root-bypass',
                 'root-review-bypass','target-review-bypass','data-bypass','empirical-bypass','overlap-bypass',
                 'identifiability-bypass','structural-as-physical','unknown-target-binding','premature-assembly',
                 'stale-frontier','untyped-deferral','accepted-outcome-loss','stale-pin',
                 'target-set-digest','charter-digest','missing-target-review'):
        b,p,t=copy.deepcopy(c),copy.deepcopy(pins),copy.deepcopy(catalog)
        ns={n['id']:n for n in b['conjectures']}
        if name=='cycle':ns['selected-software-source']['input_requirements']={'relational-carrier-physical-explanation':'knowledge'}
        elif name=='unknown-node':ns['source-target-charter']['input_requirements']['absent']='knowledge'
        elif name=='bad-port':ns['source-target-charter']['input_requirements']['source-typed-instrument-models']='physical-proof'
        elif name=='rejection-as-witness':
            ns['source-typed-instrument-models']['input_requirements']={'native-source-bridge-obstruction':'witness'}
        elif name=='lost-rejection':ns['native-source-bridge-obstruction']['verdict']='constructed'
        elif name=='root-bypass':ns['relational-carrier-physical-explanation']['input_requirements'].pop('empirical-recovery')
        elif name=='root-review-bypass':ns['relational-carrier-physical-explanation']['requires']=[]
        elif name=='target-review-bypass':ns['physical-sector-realizations']['requires']=[]
        elif name=='data-bypass':ns['held-out-model-comparison']['requires']=[]
        elif name=='empirical-bypass':ns['empirical-recovery']['input_requirements']={'source-typed-instrument-models':'witness'}
        elif name=='overlap-bypass':ns['cross-sector-compatibility']['input_requirements']['same-witness-sector-transport']='knowledge'
        elif name=='identifiability-bypass':ns['falsifiable-explanatory-constraint']['input_requirements']['identifiability-and-robustness-test']='knowledge'
        elif name=='structural-as-physical':b['selected_physical_targets']=['unitary-local-return-pilot']
        elif name=='unknown-target-binding':t['targets'][0]['required_bindings']=['absent']
        elif name=='premature-assembly':ns['physical-sector-realizations'].update(status='resolved',verdict='constructed',evidence=['instruments'])
        elif name=='stale-frontier':b['frontier']=[]
        elif name=='untyped-deferral':ns['retained-hamiltonian-physical-binding']['blocker']=''
        elif name=='accepted-outcome-loss':ns['accepted-finite-overlap']['outcome']=None
        elif name=='target-set-digest':b['available_interfaces'][0]['target_set_sha256']='0'*64
        elif name=='charter-digest':b['available_interfaces'][0]['charter_sha256']='0'*64
        elif name=='missing-target-review':b['available_interfaces']=[]
        else:p['source_sha256'][next(iter(p['source_sha256']))]='0'*64
        try:validate(b,p,t)
        except ValueError:hostile.append(name)
        else:raise AssertionError('hostile accepted: '+name)
    # Selecting a target activates only its own binding ports.
    trial=copy.deepcopy(c);trial['selected_physical_targets']=['high-energy-scattering']
    effective={n['id']:n for n in effective_nodes(trial,catalog)}
    require(effective['physical-sector-realizations']['input_requirements']['scattering-contribution-review']=='witness', 'target-specific port not activated')
    require('retained-hamiltonian-physical-binding' not in effective['physical-sector-realizations']['input_requirements'], 'unselected target activated')
    require(output_available(by['native-source-bridge-obstruction'],'knowledge') and
            not output_available(by['native-source-bridge-obstruction'],'witness'), 'rejection port availability')
    live=check_live_overlap()
    require(live['outcome']=='++' and live['source_claim']=='finite-structural-same-witness-transport-and-readout-overlap','live prerequisite')
    current=load(CURRENT)
    require(current['contract']==CONTRACT and current['target_catalog']==c['target_catalog'] and current['legacy_checkpoint']==c['predecessor'],'current pointer')
    require(sum(e['contract']==CONTRACT for e in load('research/conjecture_net/registry.json')['nets'])==1,'registry')
    ports=port_graph(c,by,interfaces)
    result={'schema':'marici.physics-programme.validation.v18','status':'pass','node_count':len(by),
        'frontier':frontier,'deferred':[n['id'] for n in by.values() if n['status']=='deferred'],
        'source_pin_count':len(sources(c)),'connection_count':len(ports['connections']),
        'available_connection_count':sum(x['available'] for x in ports['connections']),
        'rejected_hostiles':hostile,'live_accepted_prerequisite':live,'source_suites_rerun':False,
        'root_outcome':None,'selected_physical_targets':c['selected_physical_targets'],
        'validation_notices':c.get('validation_notices',[]),
        'contract_sha256':sha(CONTRACT),'checker_sha256':sha(Path(__file__)),'pins_sha256':sha(pinpath)}
    RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    PORTS.write_text(json.dumps(ports,indent=2)+'\n',encoding='utf-8')
    DASHBOARD.write_text(dashboard(c,by,interfaces,live),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='live_accepted_prerequisite'},indent=2))


if __name__=='__main__':main()
