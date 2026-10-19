"""Freshness and outcome audit of the completed timing receipts; no rerun of Z3."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
BASE=ROOT/'research/strominger/results/reference-solver-benchmark'
hashes={}
def load(path):
    raw=path.read_bytes();hashes[path.relative_to(ROOT).as_posix()]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
primary=load(BASE/'benchmark-30000ms-seeds-0.json')
assert primary['status']=='complete' and primary['productionSolverUnchanged']
for path,value in primary['sourceHashes'].items():assert digest(ROOT/path)==value
for path,value in primary['inputHashes'].items():assert digest(ROOT/path)==value
checks=load(BASE/'equivalence.json')
assert checks['status']=='pass' and checks['selectionChecks']==3200 and checks['baseline_assertions_match_production']
for name,value in checks['sourceHashes'].items():assert digest(HERE/name)==value
names=[row['resultFile'] for row in primary['rows']]
names+=['mg24-D7-baseline-seed1-30000ms.json','mg24-D7-scc-bv-seed1-30000ms.json','mg24-D8-scc-bv-seed0-120000ms.json','mg24-D9-scc-bv-seed0-120000ms.json']
assert len(names)==29 and len(set(names))==29
results={}
for name in names:
    result=load(BASE/name);results[name]=result
    assert result['solver']=='z3-5.3.1'
    assert digest(ROOT/result['input'])==result['inputSha256']
    for path,value in result['sourceHashes'].items():assert digest(HERE/path)==value
    if result['status']=='sat':assert result['directSelectionValidation']
    if result['status']=='unknown':assert result['unknownReason']=='timeout'
sat_replays=0
for row in primary['rows']:
    result=results[row['resultFile']]
    assert row['status']==result['status'] and row['checkSeconds']==result['checkSeconds']
    if row['status']!='sat':continue
    replay=load(BASE/row['replayFile'])
    assert replay['status']=='native-candidate-replayed'
    assert replay['candidateSha256']==digest(BASE/row['resultFile'])
    assert replay['inputSha256']==result['inputSha256']
    assert replay['checkerSha256']==digest(HERE/'replay_reference_solver_candidate.mjs')
    for path,value in replay['sourceHashes'].items():assert digest((HERE/path).resolve())==value
    sat_replays+=1
assert sat_replays==5
original=load(ROOT/'research/strominger/results/reference-mg24-search/verification.json')
assert next(row['solver']['status'] for row in original['rows'] if row['maxOrigin']==9)=='unknown'
assert results['mg24-D9-scc-bv-seed0-120000ms.json']['status']=='unsat'
report={'schema':'marici.reference-solver-benchmark-audit.v1','status':'pass','timed_runs':len(results),'native_sat_replays':sat_replays,
        'small_selection_equivalence_checks':checks['selectionChecks'],'production_assertions_matched':True,'production_solver_unchanged':True,
        'mg24_origin9':'UNSAT under equivalent SCC bit-vector encoding; original UNKNOWN receipt preserved',
        'formal_unsat_certificate_checked':False,'scope':'Receipt freshness, constraint-equivalence tests and positive replay evidence; timings are not rerun here.'}
for path in (Path(__file__),ROOT/'research/strominger/reference-solver-benchmark-v1.md'):
    hashes[path.relative_to(ROOT).as_posix()]=digest(path)
report['sourceAndReceiptHashes']=hashes
(BASE/'audit-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='sourceAndReceiptHashes'},indent=2))
