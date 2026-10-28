"""Fresh source replay and exact local field checks in two independent contexts."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[3]
V='research/voevodsky/'
CHECKER='research/strominger/checkers/check_joint_field_assembly_sewing.py'

def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def main():
    inputs=[V+'contracts/ramsey-complementary-sewing-attempt.v1.json',
            V+'checkers/export_ramsey_complementary_sewing.mjs',
            V+'checkers/check_ramsey_complementary_sewing.py',CHECKER,
            'research/strominger/results/channel-assembled-native-fixture.json',
            'research/nima/generative-phase-assembly.mjs']
    before={p:sha(p) for p in inputs}
    subprocess.run(['node',V+'checkers/export_ramsey_complementary_sewing.mjs'],cwd=ROOT,check=True,timeout=120)
    receipts={}; fixtures={}
    for label in ['base','complement']:
        fixture=V+f'results/ramsey-complementary-sewing-{label}-fixture-v1.json'
        output=V+f'results/ramsey-complementary-sewing-{label}-field-v1.json'
        run=subprocess.run([sys.executable,CHECKER,'--fixture',fixture,'--output',output],cwd=ROOT,capture_output=True,text=True,timeout=600)
        (ROOT/(V+f'results/ramsey-complementary-sewing-{label}-field-v1.log')).write_text(run.stdout+'\n'+run.stderr)
        if run.returncode: raise RuntimeError(label+' field check failed: '+run.stdout[-3000:]+'\n'+run.stderr[-3000:])
        r=json.loads((ROOT/output).read_text());f=json.loads((ROOT/fixture).read_text())
        assert r['status']=='passed' and r['check_count']==18
        assert r['counts']['rootFieldDimension']==44 and len(r['interfaces'])==18
        assert f['fullReferenceCovariance'] and f['rootFacets']==([0,2] if label=='base' else [1,3])
        for p,h in r['sourceHashes'].items(): assert sha(p)==h, 'stale local field input: '+p
        receipts[label]={'path':output,'sha256':sha(output),'checks':18}
        fixtures[label]={'path':fixture,'sha256':sha(fixture),'rootFacets':f['rootFacets']}
    assert before=={p:sha(p) for p in inputs}, 'sources changed during replay'
    result={'schema':'marici.ramsey-complementary-sewing.verification.v1','status':'passed',
        'scope_id':'two-complementary-native-contexts-local-field-sewing-v1',
        'independent_contexts':2,'native_packet_occurrences':28,'native_interface_occurrences':36,
        'covered_facets':[0,1,2,3],'full_reference_covariance':True,
        'local_co_moving_field_sewing':True,'field_checks':receipts,'fixtures':fixtures,
        'cross_context_world_field_intertwiner_proved':False,'joint_occupied_assembly_certified':False,
        'geometric_edge_vertex_restriction_proved':False,'native_WG_comparison_proved':False,
        'parent_descent_resolved':False,'source_sha256':before}
    (ROOT/(V+'results/ramsey-complementary-sewing-v1.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
