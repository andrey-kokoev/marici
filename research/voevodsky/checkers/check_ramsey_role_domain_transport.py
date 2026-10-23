"""Successful geometric cocycles; failed total fixed-face PN law-domain transport."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[3];BASE='research/voevodsky/'
def main():
    js=subprocess.run(['node',BASE+'checkers/check_ramsey_role_domain_transport.mjs'],cwd=ROOT,capture_output=True,text=True,timeout=120)
    if js.returncode:raise RuntimeError(js.stdout+'\n'+js.stderr)
    raw=json.loads((ROOT/(BASE+'results/ramsey-role-domain-transport-input-v1.json')).read_text(encoding='utf-8'))
    assert (len(raw['frames']),raw['pairCells'],raw['changedRolePairs'],raw['oneLost'],raw['twoLost'])==(24,576,480,384,96)
    assert (raw['sameFaceFiveReferenceChangedPairs'],raw['cocycles'],raw['fullCocycles'],raw['validatedTransfers'],len(raw['controls']))==(96,13824,864,72,5)
    for f in raw['frames']:
        assert sorted(f['p'])==list(range(4)) and len(f['eligible'])==2
        for op in [f['pn'],f['readerPN']]:assert op['kind']=='PN' and op['permutation']==[3,1,2,0,4]
    c=raw['counterexample'];a=c['source']['chart']['aliases'];b=c['target']['chart']['aliases']
    assert set(a.values())==set(b.values()) and a['C0']==b['C0'] and a['C2']==b['C2']
    assert set(c['sourcePN']['face'])==set(c['targetPN']['face'])
    sourceRole={v:n[0] for n,v in a.items()};targetRole={v:n[0] for n,v in b.items()}
    assert sum(sourceRole[v]=='M' for v in c['lostFace'])==2 and sum(targetRole[v]=='M' for v in c['lostFace'])==1
    assert len(c['sharedFaces'])==1
    assert raw['totalFixedFacePNDomainTransportRefuted'] and not any(raw[k] for k in ['geometricCocycleFailed','allPartialTransitionsRefuted','faceChartDescentRefuted','WGTaskPackageRefuted','rootResolved'])
    ps=subprocess.run(['pwsh','-NoProfile','-File',BASE+'checkers/check_ramsey_role_domain_transport_agda.ps1','-Fresh'],cwd=ROOT,capture_output=True,text=True,timeout=840)
    if ps.returncode:raise RuntimeError('PN-domain transition proof failed\n'+ps.stdout[-6500:]+'\n'+ps.stderr[-1500:])
    f=json.loads((ROOT/(BASE+'results/agda-RamseyRoleDomainTransport.json')).read_text(encoding='utf-8-sig'))
    assert f['passed'] and f['ignore_interfaces'] and f['inputs_stable_during_check']
    pins=dict(json.loads((ROOT/(BASE+'results/ramsey-single-frame-faces-v1.json')).read_text(encoding='utf-8'))['source_sha256'])
    for p in ['contracts/ramsey-role-domain-transport-attempt.v1.json','ramsey-role-domain-transport-v1.md','agda/RamseyRoleDomainTransport.agda',
              'checkers/check_ramsey_role_domain_transport.mjs','checkers/check_ramsey_role_domain_transport.py','checkers/check_ramsey_role_domain_transport_agda.ps1']:
        pins[BASE+p]=sha256((ROOT/(BASE+p)).read_bytes()).hexdigest()
    for group,prefix in [('native','research/nima/agda/'),('owner',BASE+'agda/'),('fixtures',BASE+'fixtures/ramsey-role-domain-transport/')]:
        for p,h in f['source_inventory'][group].items():pins[prefix+p]=h
    for p,h in pins.items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h
    r={'schema':'marici.ramsey-role-domain-transport.verification.v1','status':'passed','scope_id':'same-face-five-reference-total-PN-domain-transport-v1','outcome':'-+',
      'verification_level':'fresh safe Cubical geometric chart cocycle and no-total-fixed-face PN-domain map, with actual same-face full-reference source controls; not all partial/chart transitions refuted',
      'geometric_cocycle_proved':True,'same_face_full_reference_lower_gate_passed':True,'total_geometry_fixed_PN_domain_map_refuted':True,
      'shared_domain_partial_span_constructed':True,'partial_span_native_admission_proved':False,'all_role_transitions_refuted':False,
      'face_chart_descent_refuted':False,'WG_task_package_refuted':False,'root_resolved':False,
      'native_frames':24,'validated_transfers':72,'pair_cells':576,'changed_role_pairs':480,'triple_cocycles':13824,'full_reference_cocycles':864,'same_face_changed_role_pairs':96,'controls':5,
      'formal_check':{'receipt':BASE+'results/agda-RamseyRoleDomainTransport.json','compiler_sha256':f['compiler_sha256'],'module_source_sha256':f['module_source_sha256'],
        'ignore_interfaces':True,'inputs_stable':True,'library_inventory_sha256':sha256(json.dumps(f['source_inventory']['library'],sort_keys=True).encode()).hexdigest()},
      'witness':raw,'source_sha256':dict(sorted(pins.items()))}
    (ROOT/(BASE+'results/ramsey-role-domain-transport-v1.json')).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('witness','source_sha256')}))
if __name__=='__main__':main()
