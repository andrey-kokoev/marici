"""Scoped single-frame full-face rejection; not a whole-space no-go."""
from hashlib import sha256
from itertools import permutations,combinations
import json
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[3];BASE='research/voevodsky/'
def main():
    js=subprocess.run(['node',BASE+'checkers/check_ramsey_single_frame_faces.mjs'],cwd=ROOT,capture_output=True,text=True,timeout=120)
    if js.returncode:raise RuntimeError(js.stdout+'\n'+js.stderr)
    raw=json.loads((ROOT/(BASE+'results/ramsey-single-frame-faces-input-v1.json')).read_text(encoding='utf-8'))
    assert (len(raw['cases']),raw['transfers'],raw['neighbors'],len(raw['controls']))==(4,288,16,12)
    for case in raw['cases']:
        vertices=case['vertices'];faces={frozenset(f) for f in case['faces']}
        assert len(vertices)==4 and faces=={frozenset(c) for c in combinations(vertices,3)}
        assert len(case['frames'])==24 and len(case['groups'])==6
        markings={tuple(f['aliases'][n] for n in ['C0','M0','C1','M1']) for f in case['frames']}
        assert markings==set(permutations(vertices))
        for g in case['groups']:
            assert g['frameCount']==4 and len(g['faces'])==2
            expected={f for f in faces if sum(g['roles'][v]=='M' for v in f)==2}
            assert {frozenset(s.split('|')) for s in g['faces']}==expected
        for f in case['frames']:
            roles={v:n[0] for n,v in f['aliases'].items() if n in ('C0','M0','C1','M1')}
            assert sorted(sum(roles[v]=='M' for v in face) for face in faces)==[1,1,2,2]
            for name in ('pn','readerPN'):
                op=f[name];assert op['kind']=='PN' and op['permutation']==[3,1,2,0,4] and op['phaseDelta']==0
                assert sum(roles[v]=='M' for v in op['face'])==2
        w=case['counterexample'];assert not w['joint']['valid'] and w['joint']['reason']=='global-CM-role-conflict'
        assert frozenset(w['alternativeOperation']['face'])==frozenset(w['blockedFace'])
        assert w['sourceOperation']['source']==w['source']['packet']['id']
    assert raw['singleRoleFrameAllFourFacesRefuted'] and not any(raw[k] for k in ['allPerFaceChartsUnavailable','spaceAdmissionRefuted','WGChartTaskPackageRefuted','rootResolved'])
    ps=subprocess.run(['pwsh','-NoProfile','-File',BASE+'checkers/check_ramsey_single_frame_faces_agda.ps1','-Fresh'],cwd=ROOT,capture_output=True,text=True,timeout=840)
    if ps.returncode:raise RuntimeError('single-frame finite obstruction failed\n'+ps.stdout[-6500:]+'\n'+ps.stderr[-1500:])
    f=json.loads((ROOT/(BASE+'results/agda-RamseySingleFrameFaces.json')).read_text(encoding='utf-8-sig'))
    assert f['passed'] and f['ignore_interfaces'] and f['inputs_stable_during_check']
    pins=dict(json.loads((ROOT/(BASE+'results/ramsey-uniform-task-package-v1.json')).read_text(encoding='utf-8'))['source_sha256'])
    for p in ['contracts/ramsey-single-frame-face-attempt.v1.json','ramsey-single-frame-faces-v1.md','agda/RamseySingleFrameFaces.agda',
              'checkers/check_ramsey_single_frame_faces.mjs','checkers/check_ramsey_single_frame_faces.py','checkers/check_ramsey_single_frame_faces_agda.ps1']:
        pins[BASE+p]=sha256((ROOT/(BASE+p)).read_bytes()).hexdigest()
    for group,prefix in [('native','research/nima/agda/'),('owner',BASE+'agda/'),('fixtures',BASE+'fixtures/ramsey-single-frame-faces/')]:
        for p,h in f['source_inventory'][group].items():pins[prefix+p]=h
    for p,h in pins.items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h
    r={'schema':'marici.ramsey-single-frame-faces.verification.v1','status':'passed','scope_id':'one-role-coherent-P-frame-four-PN-faces-v1','outcome':'-+',
      'verification_level':'fresh safe Cubical universal finite C/M face-count obstruction and actual PN/reader/full-reference controls; rejects one role-coherent particle-port interpretation, not all source policies',
      'single_role_frame_full_face_policy_refuted':True,'all_markings_grouped_by_roles':True,'all_geometric_faces_have_neighbors':True,
      'source_valid_incompatible_per_face_port_retained':True,'global_role_sewing_rejects_counterexample':True,
      'all_native_interpretations_refuted':False,'space_admission_refuted':False,'WG_chart_task_package_refuted':False,'root_resolved':False,
      'source_regular_cells':4,'native_markings':96,'role_groups':24,'validated_transfers':288,'geometric_neighbors':16,'controls':12,
      'formal_check':{'receipt':BASE+'results/agda-RamseySingleFrameFaces.json','compiler_sha256':f['compiler_sha256'],'module_source_sha256':f['module_source_sha256'],
        'ignore_interfaces':True,'inputs_stable':True,'library_inventory_sha256':sha256(json.dumps(f['source_inventory']['library'],sort_keys=True).encode()).hexdigest()},
      'witness':raw,'source_sha256':dict(sorted(pins.items()))}
    (ROOT/(BASE+'results/ramsey-single-frame-faces-v1.json')).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('witness','source_sha256')}))
if __name__=='__main__':main()
