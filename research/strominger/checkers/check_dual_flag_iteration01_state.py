"""Administrative versioned-net progress audit; does not rerun scientific tests."""
from datetime import datetime,timezone
from hashlib import sha256
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
BASE=ROOT/'research/strominger/contracts/dual-tetrahedral-branching-conjecture-net.v1.json'
NET=ROOT/'research/strominger/contracts/dual-tetrahedral-branching-conjecture-net.v2.json'
POINTER=ROOT/'research/strominger/contracts/dual-tetrahedral-branching-conjecture-net.current.json'
RECEIPT=ROOT/'research/strominger/results/dual-flag-spectrum-walsh/verification.json'
OUT=ROOT/'research/strominger/results/dual-flag-spectrum-walsh'


def main():
    base=json.loads(BASE.read_text(encoding='utf-8'));net=json.loads(NET.read_text(encoding='utf-8'));pointer=json.loads(POINTER.read_text(encoding='utf-8'));r=json.loads(RECEIPT.read_text(encoding='utf-8'))
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    check('predecessor_exact_bytes_retained',sha256(BASE.read_bytes()).hexdigest()==net['base_sha256'])
    check('science_passed_and_all_source_pins_current',r['status']=='pass' and all(r['checks'].values()) and all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in r['source_sha256'].items()))
    nodes={n['id']:dict(n) for n in base['conjectures']}
    for update in net['node_updates']:
        check('update_existing_'+update['id'],update['id'] in nodes);nodes[update['id']].update(update)
    for node in net['added_nodes']:
        check('new_node_'+node['id'],node['id'] not in nodes);nodes[node['id']]=node
    check('all_resolved_dependencies_exist',all(d in nodes for n in nodes.values() for d in n['depends_on']))
    visiting=set();done=set()
    def visit(key):
        if key in visiting:raise AssertionError('cycle')
        if key in done:return
        visiting.add(key)
        for d in nodes[key]['depends_on']:visit(d)
        visiting.remove(key);done.add(key)
    for key in nodes:visit(key)
    check('effective_net_DAG',len(done)==len(nodes))
    check('old_leaf_disposed_not_actionable',not nodes['canonical-flag-channel-spectrum']['actionable'] and nodes['canonical-flag-channel-spectrum']['status']=='resolved_scoped_exact_result')
    check('one_nonredundant_executable_successor',net['frontier']==['flag-family-reconstruction-scaling'] and all(nodes[k]['actionable'] and nodes[k]['status']=='open_executable' for k in net['frontier']))
    check('missing_authority_branches_not_frontier',all(not n.get('actionable',False) and n['id'] not in net['frontier'] for n in nodes.values() if 'first_missing_object' in n))
    check('pointer_and_iteration_budget_match',pointer['current_contract']==str(NET.relative_to(ROOT)).replace('\\','/') and pointer['completed_iteration']==net['iteration']['completed']==1 and net['iteration']['next']==2 and pointer['iteration_budget']==10)
    check('actual_spectrum_and_composition_residual_retained',r['scalar_band_ranks']==[1,4,6,3,4,4,15,6,14,4,3] and r['composition_residual_rank']==4 and r['minimal_closure']['dimension']==12)
    check('coarse_failure_full_retained_success_not_confused',not r['compiled_cells']['coarse']['passed'] and r['compiled_cells']['retained']['passed'])
    check('no_physical_or_formal_promotion',not net['physical_validation'] and net['formal_outcome'] is None and not net['objective']['physical_assignment_complete'])
    report={'schema':'marici.strominger.dual-flag-iteration01.state-audit.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'status':'pass','checks':checks,'effective_node_count':len(nodes),'frontier':net['frontier'],'iteration':net['iteration'],'scientific_replay':False,'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in [HERE,BASE,NET,POINTER,RECEIPT]}}
    OUT.mkdir(parents=True,exist_ok=True);(OUT/'state-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','classification':'iteration1_disposed_frontier_v2_verified','checks':len(checks),'nodes':len(nodes),'frontier':net['frontier']}))

if __name__=='__main__':main()
