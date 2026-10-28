"""Fresh local template induction gate for the fixed-seed query rival."""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import subprocess
ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/voevodsky/'

def main():
    run = subprocess.run(['node',BASE+'checkers/check_ramsey_single_leaf_query.mjs'],cwd=ROOT,capture_output=True,text=True,check=True,timeout=60)
    raw = json.loads(run.stdout)
    q = [sum(raw['pattern'][i][j] for i in raw['word']) for j in range(3)]
    assert q == raw['query'] == [3,3,0] and sum(q)%2 == 0 and max(map(abs,q)) <= raw['regionRadius'] == 3
    assert q[1] not in raw['allTerminalFirstWindowY'] == [0,1,2]
    assert len(raw['rows']) == 32 and raw['counts']['checkedNativeTransfers'] == 96
    assert raw['queryExcludedByInvariant'] and not raw['depthLimitedSearchUsed'] and not raw['allMariciPoliciesRefuted'] and not raw['rootResolved']
    slab_pairs = [(a,m) for a,m in product(range(3),range(1,3)) if a+m<=2]
    assert slab_pairs == [(0,1),(0,2),(1,1)] and all(a%3 != (a+m)%3 for a,m in slab_pairs)
    region = [p for p in product(range(-3,4),repeat=3) if sum(p)%2==0]
    assert len(region)==171 and tuple(q) in region
    sources = dict(json.loads((ROOT/(BASE+'results/ramsey-native-word-trace-v1.json')).read_text(encoding='utf-8'))['source_sha256'])
    for name in ['contracts/ramsey-single-leaf-query-attempt.v1.json','ramsey-single-leaf-query-obstruction-v1.md',
                 'checkers/check_ramsey_single_leaf_query.mjs','checkers/check_ramsey_single_leaf_query.py']:
        sources[BASE+name] = sha256((ROOT/(BASE+name)).read_bytes()).hexdigest()
    for path,digest in sources.items():
        assert sha256((ROOT/path).read_bytes()).hexdigest()==digest
    result = {'schema':'marici.ramsey-single-leaf-query.verification.v1','status':'passed',
        'scope_id':'canonical-PN-leaf-all-word-first-window-query-v1','outcome':'-+',
        'verification_level':'written exact-integer template-to-path induction and exhaustive native source controls; not all source policies or kernel verified',
        'witness':raw,'source_templates_admitted':96,'planar_templates_checked':32,'native_transfers_checked':96,
        'terminal_exits_checked':16,'query_excluded':[3,3,0],'complete_test_region_points':171,
        'slab_three_color_homothety_vertical_pairs':[list(p) for p in slab_pairs],
        'all_path_argument':'Exact template exhaustion plus integer-translation covariance and origin/permutation-independent availability; induction, not a path-depth cutoff',
        'single_leaf_uniform_query_lift_refuted':True,'uniform_task_package_refuted':False,'root_resolved':False,
        'source_sha256':dict(sorted(sources.items()))}
    (ROOT/(BASE+'results/ramsey-single-leaf-query-v1.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('witness','source_sha256')}))

if __name__=='__main__':
    main()
