"""Actual native witnessed partial spans under independently validated full-port inputs."""
from hashlib import sha256
import json,re
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[3];BASE='research/voevodsky/'
def main():
    js=subprocess.run(['node',BASE+'checkers/check_ramsey_native_PN_overlap_span.mjs'],cwd=ROOT,capture_output=True,text=True,timeout=180)
    if js.returncode:raise RuntimeError(js.stdout+'\n'+js.stderr)
    raw=json.loads((ROOT/(BASE+'results/ramsey-native-PN-overlap-span-input-v1.json')).read_text(encoding='utf-8'))
    assert (len(raw['frames']),len(raw['ports']),raw['validatedTransfers'])==(24,48,72)
    assert (raw['pairCells'],raw['emptyPairs'],raw['pairPorts'])==(576,96,576)
    assert (raw['tripleCells'],raw['emptyTriples'],raw['triplePorts'],raw['pairwiseButTripleEmpty'])==(13824,7296,6912,1536)
    assert len(raw['controls'])==6 and raw['policyBeforeOverlapSelection']
    for p in raw['ports']:
        a,b,op=p['source'],p['target'],p['operation']
        assert op['kind']=='PN' and op['permutation']==[3,1,2,0,4] and op['phaseDelta']==0
        assert len(a['packet']['permutation'])==5 and sorted(a['packet']['permutation'])==list(range(5))
        assert b['packet']['permutation']==[a['packet']['permutation'][i] for i in op['permutation']]
        assert op['source']==a['packet']['id'] and op['target']==b['packet']['id']
        assert a['packet']['origin']==b['packet']['origin']
        assert set(a['cell']['vertices'])&set(b['cell']['vertices'])==set(p['faceVertices'])==set(op['face'])
        for n in ['C0','M0','C1','M1','C2']:assert a['chart']['aliases'][n]==b['chart']['aliases'][n]
        assert p['permitMCount']==sum(p['role'][v]=='M' for v in op['face'])==2
        if p['prefix']:
            assert len(p['prefix'])==1 and p['prefix'][0]['kind']=='reader-phase-advance'
            assert p['prefix'][0]['source']==p['base']['packet']['id'] and p['prefix'][0]['target']==op['source']
    ex=raw['example'];assert ex['AB']['target']==ex['BC']['source']==ex['fullSource'][1]
    assert ex['AB']['source']==ex['AC']['source'] and ex['BC']['target']==ex['AC']['target']
    assert not any(raw[k] for k in ['compositionResultSeeded','totalGaugeClaimed','physicalRoleChangeClaimed','globalAssemblyClaimed'])
    text=(ROOT/(BASE+'fixtures/ramsey-native-PN-overlap-span/RamseyPNOverlapExamples.agda')).read_text(encoding='utf-8')
    quoted=re.findall(r'^packet ([ABCD]) (c0|m0|c1|m1) p = (".*")$',text,re.M)
    assert len(quoted)==8
    for c,f,s in quoted:
        port=json.loads(json.loads(s));chart=raw['demoCharts'][c];face=['c0','m0','c1','m1'].index(f)
        assert port==next(p for p in raw['ports'] if p['chart']==chart and p['face']==face)
    ps=subprocess.run(['pwsh','-NoProfile','-File',BASE+'checkers/check_ramsey_native_PN_overlap_span_agda.ps1','-Fresh'],cwd=ROOT,capture_output=True,text=True,timeout=840)
    if ps.returncode:raise RuntimeError('native PN overlap span proof failed\n'+ps.stdout[-7000:]+'\n'+ps.stderr[-1600:])
    f=json.loads((ROOT/(BASE+'results/agda-RamseyNativePNOverlapSpan.json')).read_text(encoding='utf-8-sig'))
    assert f['passed'] and f['ignore_interfaces'] and f['inputs_stable_during_check']
    pins=dict(json.loads((ROOT/(BASE+'results/ramsey-role-domain-transport-v1.json')).read_text(encoding='utf-8'))['source_sha256'])
    for p in ['contracts/ramsey-native-PN-overlap-span-attempt.v1.json','ramsey-native-PN-overlap-span-v1.md','agda/RamseyNativePNOverlapSpan.agda',
              'checkers/check_ramsey_native_PN_overlap_span.mjs','checkers/check_ramsey_native_PN_overlap_span.py','checkers/check_ramsey_native_PN_overlap_span_agda.ps1']:
        pins[BASE+p]=sha256((ROOT/(BASE+p)).read_bytes()).hexdigest()
    for group,prefix in [('native','research/nima/agda/'),('owner',BASE+'agda/'),('fixtures',BASE+'fixtures/ramsey-native-PN-overlap-span/')]:
        for p,h in f['source_inventory'][group].items():pins[prefix+p]=h
    for p,h in pins.items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h
    r={'schema':'marici.ramsey-native-PN-overlap-span.verification.v1','status':'passed','scope_id':'native-shared-PN-domain-span-and-composition-v1','outcome':'++',
      'verification_level':'fresh safe Cubical actual native P/E partial spans, full-port retention and triple-domain composition/seam cells under validated-port input policy; runtime PN binding, not physical role motion or full descent',
      'independent_full_port_input_policy':True,'actual_native_span_and_selection':True,'both_role_domain_certificates_retained':True,
      'middle_full_packet_and_derivation_cell':True,'all_route_and_three_port_histories_retained':True,'composition_on_declared_triple_domain':True,
      'empty_pair_and_pairwise_nonempty_empty_triple_checked':True,
      'kernel_sector_PN_interpretation_proved':False,'total_PN_gauge_proved':False,'physical_role_change_proved':False,'global_occupied_assembly_proved':False,
      'full_four_face_descent_proved':False,'whole_space_admission_proved':False,'root_resolved':False,
      'input_port_records':48,'validated_transfers':72,'pair_cells':576,'empty_pairs':96,'common_pair_ports':576,
      'triple_cells':13824,'empty_triples':7296,'common_triple_ports':6912,'pairwise_nonempty_empty_triples':1536,'controls':6,
      'formal_check':{'receipt':BASE+'results/agda-RamseyNativePNOverlapSpan.json','compiler_sha256':f['compiler_sha256'],'module_source_sha256':f['module_source_sha256'],
        'ignore_interfaces':True,'inputs_stable':True,'library_inventory_sha256':sha256(json.dumps(f['source_inventory']['library'],sort_keys=True).encode()).hexdigest()},
      'witness':raw,'source_sha256':dict(sorted(pins.items()))}
    (ROOT/(BASE+'results/ramsey-native-PN-overlap-span-v1.json')).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('witness','source_sha256')}))
if __name__=='__main__':main()
