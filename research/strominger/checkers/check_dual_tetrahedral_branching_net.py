"""Net registration/type audit and exact count construction; not physics replay."""
from datetime import datetime,timezone
from hashlib import sha256
from itertools import product,combinations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
NET=ROOT/'research/strominger/contracts/dual-tetrahedral-branching-conjecture-net.v1.json'
PACKET=ROOT/'research/strominger/dual-tetrahedral-branching-conjecture-net.md'
MODEL=ROOT/'research/strominger/scc-models/dual-tetrahedral-branching-net-v1.json'
OUT=ROOT/'research/strominger/results/dual-tetrahedral-branching-net'


def run(report):
    net=json.loads(NET.read_text(encoding='utf-8'))
    checks=report['checks']
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    nodes={n['id']:n for n in net['conjectures']}
    check('node_ids_unique',len(nodes)==len(net['conjectures']))
    check('all_dependency_references_exist',all(d in nodes for n in nodes.values() for d in n['depends_on']))
    visiting=set();seen=set()
    def visit(key):
        if key in visiting:raise AssertionError('dependency cycle')
        if key in seen:return
        visiting.add(key)
        for d in nodes[key]['depends_on']:visit(d)
        visiting.remove(key);seen.add(key)
    for key in nodes:visit(key)
    check('dependency_DAG',len(seen)==len(nodes))
    check('parameter_roles_remain_distinct',set(net['parameters'])=={'d','b','n','r','sigma'})
    check('registration_has_no_physical_or_formal_promotion',net['formal_outcome'] is None and not net['physical_validation'] and not net['objective']['physical_assignment_complete'])
    check('parent_and_all_local_attachments_exist',(ROOT/net['parent_net']).is_file() and all((ROOT/a['contract']).is_file() if 'contract' in a else (ROOT/a['packet']).is_file() for a in net['attachments']))
    frontier=net['frontier']
    check('one_executable_frontier_not_waiting',frontier==['canonical-flag-channel-spectrum'] and all(nodes[k]['status']=='open_executable' and nodes[k]['actionable'] for k in frontier))
    check('all_native_missing_source_branches_nonactionable',all(not n.get('actionable',False) and n['id'] not in frontier for n in nodes.values() if 'first_missing_object' in n))
    evidence={key:ROOT/value for key,value in net['evidence'].items()}
    check('all_evidence_locators_exist',all(path.is_file() for path in evidence.values()))
    history=json.loads(evidence['historical_port_net'].read_text(encoding='utf-8'))
    old_rule=next(n for n in history['conjectures'] if n['id']=='same-codimension-rule')
    check('historical_context_specific_count_rejection_retained',old_rule['disposition']=='rejected' and 'n*2^(n-1)' in old_rule['residual'])
    prior={key:json.loads(evidence[key].read_text(encoding='utf-8')) for key in ('capacity','two_sided','reciprocal')}
    check('cited_prior_receipts_passed_not_replayed',all(r['status']=='pass' and all(r['checks'].values()) for r in prior.values()))
    check('all_cited_direct_source_fingerprints_current',all(sha256((ROOT/path).read_bytes()).hexdigest()==digest for r in prior.values() for path,digest in r['source_sha256'].items()))
    rows=[]
    for d in range(1,7):
        facets=list(product((-1,1),repeat=d))
        vertices=list(product(range(d),(-1,1)))
        flags=[(v,face) for v in vertices for face in facets if face[v[0]]==v[1]]
        formula=2*d*2**(d-1)
        check(f'd{d}_flags_derive_proposed_formula',len(flags)==formula and all(sum(face[v[0]]==v[1] for face in facets)==2**(d-1) for v in vertices))
        rows.append({'space_dimension':d,'facet_dimension':d-1,'vertices':len(vertices),'facets':len(facets),'vertex_facet_flags':len(flags),'shell_capacity_if_index_were_n':2*d*d,'count_difference_under_that_identification':len(flags)-2*d*d})
    source=prior['capacity']['regular_candidates']['16-cell']
    tetra=source['geometry']['tetrahedral_facets']
    flags=[(v,i) for i,face in enumerate(tetra) for v in face]
    check('actual_source_16_cell_has_64_vertex_tetrahedron_flags',len(source['geometry']['vertices'])==8 and len(tetra)==16 and len(flags)==64 and all(sum(v in face for face in tetra)==8 for v in range(8)))
    scalar_modes=sum(b['scalar_rank'] for b in source['spectral_certificate']['bands'])
    check('actual_shared_source_distinguishes_flags_from_modes',scalar_modes==8 and source['capacity_comparison']['all_band_capacities']==[2,8,6] and len(flags)!=2*scalar_modes)
    third=prior['capacity']['regular_candidates']['600-cell']['capacity_comparison']['all_band_capacities'][2]
    check('final_shell_capacity_counterexample_kept',third==18 and rows[2]['vertex_facet_flags']==24 and nodes['binary-count-is-final-shell-capacity']['status'].startswith('rejected'))
    check('failed_atomic_filling_not_erased',all(not a['matches'] for a in prior['capacity']['neutral_filling_test'] if a['element'] in ['Ca','Fe','Pb']) and nodes['same-operator-explains-atoms']['status'].startswith('rejected'))
    graph_edges=[];adj=[set() for _ in flags]
    for a,b in combinations(range(len(flags)),2):
        v,i=flags[a];w,j=flags[b]
        if (i==j and v!=w) or (v==w and len(set(tetra[i])&set(tetra[j]))==3):
            graph_edges.append((a,b));adj[a].add(b);adj[b].add(a)
    reached={0};queue=[0]
    for a in queue:
        for b in adj[a]:
            if b not in reached:reached.add(b);queue.append(b)
    check('queued_operator_source_is_a_connected_64_flag_degree6_graph',len(flags)==64 and len(graph_edges)==192 and all(len(row)==6 for row in adj) and len(reached)==64)
    check('queued_spectral_test_not_misreported_as_done',nodes['canonical-flag-channel-spectrum']['status']=='open_executable')
    graph={'field':'Q','metric':'identity','carrier':'functions on64 labelled vertex-tetrahedron flags, not the old8-vertex carrier',
           'flags':[{'vertex':v,'tetrahedron':i,'tetrahedron_vertices':tetra[i]} for v,i in flags], 'edges':graph_edges,
           'operator':'degree6 I - adjacency','spectrum_evaluated':False,'physical_assignment':False}
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'queued-flag-operator.json').write_text(json.dumps(graph,indent=2)+'\n',encoding='utf-8')
    report.update({'classification':'typed_branching_net_registered_counts_verified_spectrum_pending','nodes':list(nodes),'frontier':frontier,
      'count_table':rows,'source_16_cell_scalar_modes':scalar_modes,'source_16_cell_spin_band_capacities':[2,8,6],
      'queued_source':{'vertices':64,'edges':192,'degree':6,'spectrum_evaluated':False},
      'parent_attachment_sha256':{a.get('contract',a.get('packet')):sha256((ROOT/a.get('contract',a.get('packet'))).read_bytes()).hexdigest() for a in net['attachments']},
      'evidence_sha256':{key:sha256(path.read_bytes()).hexdigest() for key,path in evidence.items()},
      'scientific_replay':False,'physical_validation':False,'formal_outcome':None})


def main():
    report={'schema':'marici.strominger.dual-tetrahedral-branching-net.audit.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'checks':{},
       'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in [HERE,NET,PACKET,MODEL]}}
    try:run(report);report['status']='pass'
    except Exception as error:report.update(status='fail',error=repr(error));raise
    finally:
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'status':report['status'],'classification':report.get('classification','execution_failure'),'checks':len(report['checks']),'frontier':report.get('frontier'),'receipt':(OUT/'verification.json').relative_to(ROOT).as_posix()}))


if __name__=='__main__':main()
