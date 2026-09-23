"""Direct/staged/permuted point reuse with fresh archive authority."""
from pathlib import Path
from uuid import uuid4
import json,copy,hashlib
import comparison_checkpoint_transport as service
from comparison_checkpoint_transport import TransportSession,POLICY,verify_point
from atomic_fine_restoration import Vault
from continuation_coherence import root,make_path,point_query,digest,verify_path
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
def main():
    f={'normal':['0','0','1'],'upper':'1/2'};g={'normal':['0','0','-1'],'upper':'-1/4'}
    vault=Vault();cases=[];rejections=[]
    def reject(name,session,call):
        before=session.receipt()
        try:call()
        except (AssertionError,ValueError,PermissionError,KeyError):rejections.append(name)
        else:raise AssertionError(name+' accepted')
        assert session.receipt()==before
    for history in ('A','B'):
        event=uuid4().hex;context=digest({'family':'owning-m4-moment-curve-two-history-v1','n':18,'retirement':'shared'})
        token=vault._admit(event,context,18,history);archive=vault._authorize(token,event,context,'owner-admission')['archive'];binding=root(archive,event,context)
        direct=make_path(archive,binding,[[f,g]]);staged=make_path(archive,binding,[[f],[g]]);permuted=make_path(archive,binding,[[g],[f]])
        for point in (['1','1'],['1/18','1/324']):
            semantic=verify_path(archive,binding,[[f,g]],direct);answer=point_query(semantic,point)
            session=TransportSession(vault);boot=session.bootstrap(event,context,token,[[f,g]],direct,point,answer)
            for defect in ('missing-row','omitted-operation','wrong-parent','source-chart','cross-history','self-asserted-authority','changed-point','changed-policy','changed-epoch'):
                bad=copy.deepcopy(staged);batches=[[f],[g]];authority=token;p=point;policy=POLICY
                if defect=='missing-row':bad['edges'][-1]['successor']['fine_rows'].pop()
                if defect=='omitted-operation':batches=[[f]];bad=make_path(archive,binding,batches)
                if defect=='wrong-parent':bad['edges'][-1]['parent']='foreign'
                if defect=='source-chart':bad['edges'][-1]['successor']['source_chart']='foreign'
                if defect=='cross-history':authority=vault._admit(event,context,18,'B' if history=='A' else 'A')
                if defect=='self-asserted-authority':authority={'history':history}
                if defect=='changed-point':p=['1/2','1/4']
                if defect=='changed-policy':policy='whole-section-and-archive'
                previous_epoch=service.epoch
                try:
                    if defect=='changed-epoch':service.epoch=lambda:'foreign-rule-epoch'
                    reject(history+':'+defect,session,lambda:session.transport(boot['handle'],boot['state'],authority,batches,bad,p,policy))
                finally:service.epoch=previous_epoch
            # Point verifier disabled: valid transport must reuse its trusted
            # result rather than silently perform another arithmetic check.
            original=service.verify_point
            def forbidden(*args):raise RuntimeError('POINT_ARITHMETIC_REPLAYED')
            try:
                service.verify_point=forbidden
                first=session.transport(boot['handle'],boot['state'],token,[[f],[g]],staged,point)
                second=session.transport(first['handle'],first['state'],token,[[g],[f]],permuted,point)
            finally:service.verify_point=original
            for receipt,path,batches in ((first,staged,[[f],[g]]),(second,permuted,[[g],[f]])):
                fresh=verify_path(archive,binding,batches,path);verify_point(fresh,point,receipt['answer'])
                assert receipt['answer']==point_query(fresh,point)==answer
                assert receipt['state']['path_tip']==path['tip'] and not receipt['comparison']['proof_paths_identical']
            assert second['work']=={'point_checks':1,'point_cache_hits':2,'path_checks':5,'authority_checks':3}
            reject(history+':stale-head',session,lambda:session.transport(first['handle'],first['state'],token,[[f,g]],direct,point))
            mutated=copy.deepcopy(second);mutated['answer']['admitted']=not answer['admitted']
            assert session.receipt()['answer']==answer
            cases.append({'history':history,'archive':archive,'binding':binding,'point':point,'direct':direct,'staged':staged,
                          'permuted':permuted,'bootstrap':boot,'staged_receipt':first,'permuted_receipt':second})
        # Revocation refuses transport even though all semantic dependencies
        # and the previously checked point answer still match.
        vault.revoke(token)
        reject(history+':revoked-authority',session,lambda:session.transport(second['handle'],second['state'],token,[[f,g]],direct,point))
    paths=[Path(__file__),Path(service.__file__),ROOT/'research/voevodsky/checkers/continuation_coherence.py',
      ROOT/'research/voevodsky/checkers/atomic_fine_restoration.py',ROOT/'research/voevodsky/checkers/verify_fine_successor.py',
      Path(__file__).with_name('verify_scalar_envelope_band.py')]
    result={'passed':True,'cases':cases,'point_bootstraps':len(cases),'transported_results':2*len(cases),
      'fresh_transport_point_checks':0,'fresh_transport_path_checks':4*len(cases),'fresh_transport_authority_checks':2*len(cases),
      'rejections':rejections,'vault_encoded_bytes':vault.bytes(),
      'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
      'scope':'One point across equal canonical fine relations; linear heads and fresh root authority, not section or authority transport.'}
    (OUT/'comparison-checkpoint-transport.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('passed','point_bootstraps','transported_results','fresh_transport_point_checks','fresh_transport_path_checks','fresh_transport_authority_checks')},indent=2))
if __name__=='__main__':main()
