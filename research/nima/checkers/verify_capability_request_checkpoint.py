"""Replay semantic claims without importing the capability session."""
from pathlib import Path
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from verify_fine_refinement_obstruction import verify
from verify_scalar_envelope_band import check
if not __debug__:raise RuntimeError('Assertions required')
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
    report=json.loads((OUT/'capability-request-checkpoint.json').read_text())
    for path,h in report['bindings'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==h
    packets=json.loads((OUT/'scalar-envelope-band-packets.json').read_text())
    exact=next(p for p in packets if p['request']=={'n':18,'eta':'0'})
    approximate=next(p for p in packets if p['request']=={'n':18,'eta':'1/100'})
    check(approximate['request'],approximate)
    assert report['exact_attachment']['verification']==check(exact['request'],exact)
    approximate['request']['eta']='0'
    try:check(approximate['request'],approximate)
    except AssertionError:pass
    else:raise AssertionError('supposed invalid tightened selector is valid')
    ambiguity=report['fine_request_ambiguity'];request=ambiguity['request']
    assert request['point']==['1','1'] and request['operation']=={'kind':'append-fine-upper-then-exact-point-admission','h_upper':'1/2'}
    expected={'family':'owning-m4-moment-curve-two-history-v1','n':18,
      'continuation':'append-fine-upper-then-exact-point-admission','h_upper':'1/2'}
    result=verify(expected,ambiguity['obstruction']);assert ambiguity['obstruction']['public_point']==request['point']
    assert ambiguity['alternatives']=={'A':result['A_admits_point'],'B':result['B_admits_point']}
    assert ambiguity['request_digest']==digest(request) and ambiguity['status']=='HISTORY_PROVENANCE_REQUIRED'
    assert request['state']==report['exact_attachment']['state']==report['final_receipt']['state']
    assert request['state']['section_digest']==digest(exact) and request['state']['eta']=='0'
    assert request['state']['family']==expected['family'] and request['state']['n']==18
    assert request['state']['actual_history'] is None and ambiguity['actual_history'] is None and ambiguity['selected_answer'] is None
    assert report['provenance_authority']=='NOT_INTEGRATED' and report['actual_history_selected'] is False
    assert report['failed_tightening']['history_separation_proved'] is False
    result={'passed':True,'exact_common_section_cells':16,'fine_admission_answers':ambiguity['alternatives'],
      'actual_history_selected':False,'scope':'Semantic packet replay only; process-local authority refusals are exercised by the session workload.'}
    (OUT/'capability-request-checkpoint-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
