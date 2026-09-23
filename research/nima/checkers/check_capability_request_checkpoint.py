"""Fail-closed escalation, selector replacement and provenance refusals."""
from pathlib import Path
import json,copy,hashlib
from capability_request_checkpoint import CapabilitySession,FAMILY,digest
from verify_fine_refinement_obstruction import verify
from verify_scalar_envelope_band import check
OUT=Path(__file__).resolve().parents[1]/'results';ROOT=Path(__file__).resolve().parents[3]
def main():
    packets=json.loads((OUT/'scalar-envelope-band-packets.json').read_text())
    approximate=next(p for p in packets if p['request']=={'n':18,'eta':'1/100'})
    exact=next(p for p in packets if p['request']=={'n':18,'eta':'0'})
    artifact=ROOT/'research/voevodsky/results/fine-refinement-obstruction.json'
    proof=json.loads(artifact.read_text())['obstruction_packet']
    operation={'kind':'append-fine-upper-then-exact-point-admission','h_upper':'1/2'};point=['1','1']
    expected_proof={'family':FAMILY,'n':18,'continuation':operation['kind'],'h_upper':'1/2'}
    verify(expected_proof,proof)
    session=CapabilitySession();candidate=copy.deepcopy(approximate)
    boot=session.bootstrap({'family':FAMILY,'n':18,'eta':'1/100'},candidate)
    state=copy.deepcopy(boot['state']);handle=boot['handle']
    candidate['cells'][0]['formula'][0]='999';boot['state']['actual_history']='A'
    # Same affine candidate at zero tolerance is actually invalid, not just
    # rejected because its old requested tolerance was left in its header.
    tighter=copy.deepcopy(approximate);tighter['request']['eta']='0'
    failed=session.tighten(handle,state,'0',tighter)
    assert failed['status']=='SECTION_NOT_VERIFIED' and not failed['history_separation_proved']
    assert failed['handle']==handle and failed['state']==state
    ambiguity=session.request_fine(handle,state,operation,point,proof)
    assert ambiguity['alternatives']=={'A':False,'B':True}
    assert ambiguity['actual_history'] is None and ambiguity['selected_answer'] is None
    assert ambiguity['request_digest']==digest({'state':state,'operation':operation,'point':point})
    rejected=[]
    def reject(name,action):
        try:action()
        except (AssertionError,ValueError,PermissionError,NotImplementedError,KeyError):rejected.append(name)
        else:raise AssertionError(name+' accepted')
    for defect in ('wrong-point','wrong-operation','false-contradiction','foreign-family'):
        bad=copy.deepcopy(proof);p=point;op=operation
        if defect=='wrong-point':p=['1/2','1/2']
        if defect=='wrong-operation':op={**operation,'h_upper':'1'}
        if defect=='false-contradiction':bad['A_combined_upper']='0'
        if defect=='foreign-family':bad['expected']['n']=6
        reject(defect,lambda:session.request_fine(handle,state,op,p,bad))
    request=ambiguity['request_digest']
    reject('mismatched-provenance',lambda:session.request_history_selection(handle,state,request,{'request_digest':'foreign','history':'A'}))
    for name,token in (
      ('self-declared-history',{'history':'A'}),
      ('both-history-archive',{'histories':['A','B']}),
      ('chosen-positive-witness',{'source_witness':proof['B_source_witness'],'history':'B'}),
      ('unadmitted-signer',{'history':'A','issuer':'claimed-owner','signature':'not-an-authority-contract'})):
        token['request_digest']=request
        reject(name,lambda:session.request_history_selection(handle,state,request,token))
    reject('archive-escalation',lambda:session.reexpose(handle,state))
    # Even zero-tolerance common lifting leaves actual-history admission
    # ambiguous under the stronger fine continuation.
    accepted=session.tighten(handle,state,'0',exact)
    assert accepted['status']=='SECTION_VERIFIED' and accepted['verification']==check({'n':18,'eta':'0'},exact)
    reject('stale-checkpoint',lambda:session.request_fine(handle,state,operation,point,proof))
    head=accepted['handle'];after=accepted['state']
    reject('old-provenance-before-new-request',lambda:session.request_history_selection(head,after,request,{'request_digest':request}))
    after_ambiguity=session.request_fine(head,after,operation,point,proof)
    assert after_ambiguity['alternatives']==ambiguity['alternatives'] and after_ambiguity['request_digest']!=request
    reject('stale-provenance-request',lambda:session.request_history_selection(head,after,request,{'request_digest':request,'history':'B'}))
    # Receipt mutation cannot install history identity in the trusted state.
    after_ambiguity['actual_history']='B';after_ambiguity['selected_answer']=True
    final_ambiguity=session.request_fine(head,after,operation,point,proof)
    assert final_ambiguity['actual_history'] is None and final_ambiguity['selected_answer'] is None
    receipt=session._receipt();assert receipt['bytes']['actual_history_selector']==0
    paths=[Path(__file__),Path(__file__).with_name('capability_request_checkpoint.py'),
      Path(__file__).with_name('verify_scalar_envelope_band.py'),ROOT/'research/voevodsky/checkers/verify_fine_refinement_obstruction.py',
      OUT/'scalar-envelope-band-packets.json',artifact]
    result={'passed':True,'failed_tightening_is_not_separation':True,'exact_common_section_cells':accepted['verification']['cells'],
      'fine_request_ambiguity':final_ambiguity,'actual_history_selected':False,'provenance_authority':'NOT_INTEGRATED',
      'failed_tightening':failed,'exact_attachment':accepted,'final_receipt':receipt,'rejections':rejected,
      'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
      'scope':'Fixed two-history request gate. Verified ambiguity, not an authenticated split, selected branch, or new fine capability.'}
    (OUT/'capability-request-checkpoint.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('passed','failed_tightening_is_not_separation','exact_common_section_cells','actual_history_selected','provenance_authority','rejections')},indent=2))
if __name__=='__main__':main()
