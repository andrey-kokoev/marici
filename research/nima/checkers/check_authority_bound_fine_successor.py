"""Authority-gated fine successors, exact queries and failed-commit atomicity."""
from pathlib import Path
import copy,json,hashlib
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
from authority_bound_fine_successor import FineSuccessorSession,ArchiveAuthority,fine_state,digest
from approximate_section_checkpoint import initial
from verify_authority_bound_fine_successor import verify_state,verify_answer
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
def main():
    packets=json.loads((OUT/'scalar-envelope-band-packets.json').read_text())
    section=next(p for p in packets if p['request']=={'n':18,'eta':'1/100'})
    obstruction=json.loads((ROOT/'research/voevodsky/results/fine-refinement-obstruction.json').read_text())['obstruction_packet']
    operation={'kind':'fine-upper-point-admission','h_upper':'1/2','point':['1','1']}
    vault=ArchiveAuthority();records=[];rejected=[]
    def setup(history,retain=True):
        s=FineSuccessorSession(vault);boot=s.retire(initial(section['request']),section,owner_history=history,retain_identity=retain)
        candidate={'before_digest':digest(boot['state']),'retirement_event':boot['retirement_event'],
          'after':fine_state(boot['state'],boot['retirement_event'],history,operation)}
        return s,boot,candidate
    def reject(name,action):
        try:action()
        except (AssertionError,ValueError,PermissionError,KeyError,IndexError):rejected.append(name)
        else:raise AssertionError(name+' accepted')
    for history in ('A','B'):
        session,boot,candidate=setup(history);handle=boot['handle'];before=boot['state'];reference=boot['archive_reference']
        old_lift=session.lift(handle,['1','1'])
        _,foreign,_=setup(history)
        for defect in ('foreign-authority','forged-authority','changed-history','missing-fine-row','changed-bound','stale-parent','foreign-event','false-obstruction'):
            bad=copy.deepcopy(candidate);proof=copy.deepcopy(obstruction);token=reference
            if defect=='foreign-authority':token=foreign['archive_reference']
            if defect=='forged-authority':token='forged'
            if defect=='changed-history':bad['after']=fine_state(before,boot['retirement_event'],'B' if history=='A' else 'A',operation)
            if defect=='missing-fine-row':bad['after']['rows'].pop()
            if defect=='changed-bound':bad['after']['rows'][-1]['upper']='1'
            if defect=='stale-parent':bad['before_digest']='foreign'
            if defect=='foreign-event':bad['retirement_event']='foreign'
            if defect=='false-obstruction':proof['A_combined_upper']='0'
            receipt=session.receipt()
            reject(history+':'+defect,lambda:session.commit_fine(handle,before,operation,proof,token,bad))
            assert session.receipt()==receipt
        committed=session.commit_fine(handle,before,operation,obstruction,reference,candidate)
        after=committed['state'];verify_state(before,boot['retirement_event'],history,operation,after)
        answers=[]
        for point in (['1','1'],['1/18','1/324'],['0','0']):
            answer=session.exact_query(committed['handle'],point);verify_answer(after,point,answer);answers.append(answer)
        assert answers[0]['admits']==(history=='B') and answers[1]['admits'] and not answers[2]['admits']
        reject(history+':stale-head',lambda:session.exact_query(handle,['1','1']))
        reject(history+':old-approximate-api',lambda:session.lift(committed['handle'],['1','1']))
        reject(history+':archive-escalation',lambda:session.reexpose(committed['handle']))
        reject(history+':unimplemented-fine-transition',lambda:session.restrict(committed['handle'],after,{'kind':'append-public','normal':['1','0'],'upper':'1'}))
        # The old selected lift at (1,1) has h=1, violating the new fine bound.
        bad_answer=copy.deepcopy(answers[0]);bad_answer['admits']=True;bad_answer['source_lift']=old_lift['source_lift']
        reject(history+':old-lift-as-fine-witness',lambda:verify_answer(after,['1','1'],bad_answer))
        vault.revoke(reference)
        # Revocation is prospective: it does not undo an already authorized
        # fine-state publication or silently revoke that state's query API.
        verify_answer(after,['1/18','1/324'],session.exact_query(committed['handle'],['1/18','1/324']))
        records.append({'owner_history':history,'before':before,'event':boot['retirement_event'],
          'candidate':candidate,'committed':committed,'answers':answers})
    session,boot,candidate=setup('B');vault.revoke(boot['archive_reference']);receipt=session.receipt()
    reject('revoked-authority',lambda:session.commit_fine(boot['handle'],boot['state'],operation,obstruction,boot['archive_reference'],candidate))
    assert session.receipt()==receipt
    session,boot,candidate=setup('A',False)
    reject('forgotten-identity',lambda:session.commit_fine(boot['handle'],boot['state'],operation,obstruction,None,candidate))
    # Concurrent commits with one parent can publish only one successor.
    session,boot,candidate=setup('B');barrier=Barrier(2)
    def competing(_):
        barrier.wait()
        try:session.commit_fine(boot['handle'],boot['state'],operation,obstruction,boot['archive_reference'],candidate)
        except ValueError:return 'stale'
        return 'committed'
    with ThreadPoolExecutor(max_workers=2) as pool:assert sorted(pool.map(competing,range(2)))==['committed','stale']
    session,boot,candidate=setup('A');barrier=Barrier(2)
    def race_commit():
        barrier.wait()
        try:return session.commit_fine(boot['handle'],boot['state'],operation,obstruction,boot['archive_reference'],candidate)
        except PermissionError:return None
    def race_revoke():
        barrier.wait();vault.revoke(boot['archive_reference'])
    with ThreadPoolExecutor(max_workers=2) as pool:
        commit_future=pool.submit(race_commit);revoke_future=pool.submit(race_revoke)
        race_result=commit_future.result();revoke_future.result()
    if race_result is None:assert session.receipt()['handle']==boot['handle'] and session.receipt()['state']==boot['state']
    else:verify_answer(race_result['state'],['1','1'],session.exact_query(race_result['handle'],['1','1']))
    paths=[Path(__file__),Path(__file__).with_name('authority_bound_fine_successor.py'),Path(__file__).with_name('verify_authority_bound_fine_successor.py'),
      ROOT/'research/voevodsky/checkers/authority_aware_upgrade.py',ROOT/'research/voevodsky/checkers/approximate_section_checkpoint.py',
      ROOT/'research/voevodsky/checkers/verify_fine_refinement_obstruction.py',Path(__file__).with_name('verify_scalar_envelope_band.py')]
    result={'passed':True,'successors':records,'rejections':rejected,'concurrent_commit_atomic':True,'revocation_commit_race_linearized':True,
      'authority_vault_encoded_bytes':vault.encoded_bytes(),'old_sections_retained_in_fine_heads':0,
      'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
      'scope':'Trusted fixed-family event authority and exact fine successors; prospective revocation; no arbitrary migration compiler.'}
    (OUT/'authority-bound-fine-successor.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'fine_successors':len(records),'exact_answers_verified':6,'rejections':len(rejected),'concurrent_commit_atomic':True},indent=2))
if __name__=='__main__':main()
