"""Audit the toroidal space evaluation net, not its open scientific hypotheses."""
from pathlib import Path
import copy,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
NET=ROOT/'research/strominger/contracts/toroidal-space-evaluation-net.v1.json'
NOTE=ROOT/'research/strominger/toroidal-space-evaluation-net-v1.md'
PARENT_NOTE=ROOT/'research/strominger/field-realization-instrument-conjecture-net-v1.md'
NEGATIVES={'rival-surface-isomorphism','rival-cube-B','rival-dual-endpoints','import-fixed-N','import-strict-PN','rival-FCC-fixed-refinement','rival-FCC-fixed-frame','rival-FCC-center-star-native','rival-refinement-average-only','rival-refinement-face-pair-locality'}

def pointer(value,path):
    for part in path.strip('/').split('/'):
        part=part.replace('~1','/').replace('~0','~')
        value=value[int(part)] if isinstance(value,list) else value[part]
    return value

def audit(net):
    assert net['schema']=='marici.toroidal-space-evaluation-conjecture-net.v1'
    assert net['owner']=='marici.Strominger'
    assert net['excluded_objectives']==['physical-double-helix','double-helix-separator']
    assert net['semantics']['spatial_quotient']=='Only lattice addresses are reduced modulo two. Absolute realization origin and full coefficient history are retained.'
    assert (ROOT/net['parent_net']).is_file()
    assert 'contracts/toroidal-space-evaluation-net.v1.json' in PARENT_NOTE.read_text(encoding='utf8')
    nodes={n['id']:n for n in net['conjectures']};assert len(nodes)==len(net['conjectures'])
    paths={net['parent_net'],NET.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),PARENT_NOTE.relative_to(ROOT).as_posix()}
    reports={};direct_hashes=0
    for name,evidence in net['evidence'].items():
        for key in ('report','checker','note','document'):
            if key in evidence:
                path=ROOT/evidence[key];assert path.is_file(),path;paths.add(evidence[key])
        if 'report' in evidence:
            report=json.loads((ROOT/evidence['report']).read_text(encoding='utf8'));assert report.get('status')
            reports[name]=report
            assert report.get('sourceHashes'),('Receipt has no direct fingerprints',name)
            for source,digest in report['sourceHashes'].items():
                assert hashlib.sha256((ROOT/source).read_bytes()).hexdigest()==digest,('Stale evidence',name,source)
                paths.add(source);direct_hashes+=1
    visited=set();visiting=set()
    def visit(key):
        assert key in nodes and key not in visiting,('Missing or cyclic prerequisite',key)
        if key in visited:return
        visiting.add(key)
        for dep,verdict in nodes[key]['requires'].items():
            assert verdict in ('supported','rejected');visit(dep)
        visiting.remove(key);visited.add(key)
    for key in nodes:visit(key)
    observations=0
    for key,n in nodes.items():
        assert n['status'] in ('supported','rejected','open')
        assert all(n.get(field) for field in ('statement','scope','reopen'))
        for reference in n.get('references',[]):
            assert reference['evidence'] in net['evidence'] and reference.get('location'),'Invalid conjecture source reference'
        if key in NEGATIVES:assert n['status']=='rejected','A scoped obstruction was silently revived'
        if n['status']=='open':
            assert not n['checks'],'Open proposition silently decorated as a checked outcome'
            assert all(n.get(field) for field in ('next_test','acceptance','falsifier'))
        else:
            assert n['checks'],'Resolved claim without a decisive observation'
            assert all(nodes[d]['status']==v for d,v in n['requires'].items())
        for check in n['checks']:
            value=pointer(reports[check['evidence']],check['path'])
            if 'all_field' in check:
                assert isinstance(value,list) and value
                assert all(item[check['all_field']]==check['equals'] for item in value)
            elif 'length' in check:assert len(value)==check['length']
            else:assert value==check['equals'],(key,check,value)
            observations+=1
    ready=[key for key,n in nodes.items() if n['status']=='open' and all(nodes[d]['status']==v for d,v in n['requires'].items())]
    choices=net['continuations'];assert len({c['node'] for c in choices})==len(choices)
    assert {c['node'] for c in choices}==set(ready)
    assert sorted(c['priority'] for c in choices)==list(range(1,len(choices)+1))
    for c in choices:
        assert all(c.get(key) for key in ('effort','information_gain','reason','if_positive','if_negative'))
        assert c['node'] not in net['excluded_objectives']
    frontier=[c['node'] for c in sorted(choices,key=lambda c:c['priority'])]
    assert net['frontier']==frontier and net['recommended_start']==frontier[0]
    for event in net['decision_trail']:
        assert event['result'] and event['consequence'] and set(event['evidence'])<=set(net['evidence'])
    assert [e['step'] for e in net['decision_trail']]==list(range(1,len(net['decision_trail'])+1))
    blocked={key:{d:{'required':v,'actual':nodes[d]['status']} for d,v in n['requires'].items() if nodes[d]['status']!=v}
             for key,n in nodes.items() if n['status']=='open' and key not in ready}
    return {'nodes':len(nodes),'supported':sum(n['status']=='supported' for n in nodes.values()),
            'rejected':sum(n['status']=='rejected' for n in nodes.values()),'open':sum(n['status']=='open' for n in nodes.values()),
            'frontier':frontier,'recommended_start':net['recommended_start'],'blocked':blocked,
            'evidence_observations_checked':observations,'direct_receipt_hashes_checked':direct_hashes},paths

net=json.loads(NET.read_text(encoding='utf8'));summary,paths=audit(net)
mutations=[]
for kind in ('cycle','missing_dependency','unsupported_promotion','revived_obstruction','wrong_frontier','history_erasure','removed_falsifier','revived_excluded_objective','revived_average_only','revived_face_pair_locality','missing_source_reference'):
    bad=copy.deepcopy(net);nodes={n['id']:n for n in bad['conjectures']}
    if kind=='cycle':nodes['channels']['requires']['channels']='supported'
    elif kind=='missing_dependency':nodes['P-reader-lift']['requires']['missing']='supported'
    elif kind=='unsupported_promotion':nodes['P-reader-lift']['status']='supported'
    elif kind=='revived_obstruction':nodes['rival-dual-endpoints']['status']='supported'
    elif kind=='wrong_frontier':bad['frontier'].append('PN-lift')
    elif kind=='history_erasure':bad['semantics']['spatial_quotient']='All history is reduced modulo two.'
    elif kind=='removed_falsifier':nodes['N-reader-lift']['falsifier']=''
    elif kind=='revived_excluded_objective':bad['excluded_objectives']=[]
    elif kind=='revived_average_only':nodes['rival-refinement-average-only']['status']='supported'
    elif kind=='revived_face_pair_locality':nodes['rival-refinement-face-pair-locality']['status']='supported'
    elif kind=='missing_source_reference':nodes['Chamon-FCC-benchmark']['references'][0]['evidence']='missing-paper'
    try:audit(bad)
    except AssertionError:mutations.append(kind)
    else:raise AssertionError('Mutation accepted: '+kind)
sys.path.insert(0,str(ROOT/'research/conjecture_net'))
from collect import registry
entry=next(e for e in registry({NET.relative_to(ROOT).as_posix():'owner-local branch'})['nets'] if e['contract']==NET.relative_to(ROOT).as_posix())
assert entry['classification']=='conjecture-net contract'
paths.add('research/conjecture_net/collect.py')
paths.add(Path(__file__).relative_to(ROOT).as_posix())
report={'schema':'marici.toroidal-space-evaluation-net-audit.v1','status':'pass',**summary,
        'mutation_controls_rejected':mutations,'collector_recognizes_net':True,'fresh_scientific_replay':False,'open_frontier_tests_executed':False,
        'scope':'Owner-local conjecture-net registration, direct evidence freshness and dependency/frontier audit; no new scientific outcome or parent-net promotion.',
        'sourceHashes':{path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in sorted(paths)}}
out=ROOT/'research/strominger/results/toroidal-space-evaluation-net';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k!='sourceHashes'},indent=2))
