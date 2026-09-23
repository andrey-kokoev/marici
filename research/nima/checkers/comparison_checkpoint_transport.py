"""Transport one verified point result across an authorized comparison cell."""
from pathlib import Path
from fractions import Fraction as Q
from threading import RLock
from uuid import uuid4
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
import continuation_coherence as coherence
from continuation_coherence import root,verify_path,compare,digest,freeze
from verify_scalar_envelope_band import cross
if not __debug__:raise RuntimeError('Assertions required')
POLICY='exact-point-only/no-archive-reexposure/v1'
def clone(x):return json.loads(freeze(x))
def epoch():
    paths=(Path(__file__),Path(coherence.__file__),Path(coherence.expected_archive.__code__.co_filename),
           Path(cross.__code__.co_filename))
    return digest({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
def verify_point(state,point,answer):
    assert type(answer.get('admitted')) is bool
    p=tuple(map(Q,point));assert len(p)==2
    polygon=[tuple(map(Q,v)) for v in state['public_polygon']]
    if not all(cross(a,b,p)>=0 for a,b in zip(polygon,polygon[1:]+polygon[:1])):
        assert answer=={'admitted':False};return
    lower=[];upper=[]
    for r in state['fine_rows']:
        a,b,c=map(Q,r['normal']);rhs=Q(r['upper'])-a*p[0]-b*p[1]
        if c>0:upper.append(rhs/c)
        elif c<0:lower.append(rhs/c)
        elif rhs<0:assert answer=={'admitted':False};return
    lo,hi=max(lower),min(upper)
    if lo>hi:assert answer=={'admitted':False,'interval':list(map(str,(lo,hi)))};return
    assert set(answer)=={'admitted','interval','source_lift'} and answer['admitted'] is True
    assert answer['interval']==list(map(str,(lo,hi)))
    t=list(map(Q,answer['source_lift']));assert len(t)==4 and all(0<=v<=100+2*j for j,v in enumerate(t))
    d=Q(1,128**4);slopes=[Q(1,128**j) for j in range(4)];h=(t[0]-50)/d
    assert t[1]==51 and lo<=h<=hi and sum(t)==206+d*p[0]
    assert sum(a*b for a,b in zip(t,slopes))==sum(a*b for a,b in zip((50,51,52,53),slopes))+d*p[1]
    assert all(sum(a*b for a,b in zip(map(Q,r['normal']),(*p,h)))<=Q(r['upper']) for r in state['fine_rows'])

class TransportSession:
    def __init__(self,vault):
        self._vault=vault;self._lock=RLock();self._head=None;self._record=None;self._epoch=epoch()
        self._work={'point_checks':0,'point_cache_hits':0,'path_checks':0,'authority_checks':0}
    def _descriptor(self,r):
        return {'binding':r['binding'],'path_tip':r['path']['tip'],'semantic_digest':digest(r['semantic']),
                'point':r['point'],'policy':r['policy'],'verifier_epoch':self._epoch}
    def receipt(self):
        with self._lock:
            if self._head is None:raise ValueError('NO_CHECKPOINT')
            r=json.loads(self._record)
            return {'handle':self._head,'state':self._descriptor(r),'answer':r['answer'],'work':dict(self._work),
                    'checkpoint_bytes':len(self._record.encode()),'scope':'One checked point, not a transported whole section.'}
    def _key(self,semantic,point,policy):return digest({'epoch':self._epoch,'semantic':semantic,'point':point,'policy':policy})
    def bootstrap(self,event,context,token,expected_batches,path,point,answer,policy=POLICY):
        with self._lock,self._vault._lock:
            if self._head is not None:raise ValueError('ALREADY_BOOTSTRAPPED')
            if epoch()!=self._epoch or policy!=POLICY:raise ValueError('FRESH_BOOTSTRAP_REQUIRED')
            batches=clone(expected_batches);candidate=clone(path);p=list(map(str,map(Q,point)));a=clone(answer)
            request=digest({'event':event,'context':context,'batches':batches,'point':p,'policy':policy})
            grant=self._vault._authorize(token,event,context,request);assert grant['request_digest']==request and grant['event']==event
            binding=root(grant['archive'],event,context);semantic=verify_path(grant['archive'],binding,batches,candidate)
            verify_point(semantic,p,a)
            record={'binding':binding,'batches':batches,'path':candidate,'semantic':semantic,'point':p,'answer':a,
                    'policy':policy,'dependency':self._key(semantic,p,policy),'authorization_request':request}
            self._record=freeze(record);self._head=uuid4().hex
            self._work.update(point_checks=1,path_checks=1,authority_checks=1)
            return self.receipt()
    def transport(self,handle,expected_before,token,expected_batches,path,point,policy=POLICY):
        with self._lock,self._vault._lock:
            if self._head is None or handle!=self._head:raise ValueError('STALE_OR_FOREIGN')
            old=json.loads(self._record);assert expected_before==self._descriptor(old)
            if epoch()!=self._epoch or policy!=old['policy']:raise ValueError('FRESH_VERIFICATION_REQUIRED')
            p=list(map(str,map(Q,point)))
            if p!=old['point']:raise ValueError('FRESH_POINT_VERIFICATION_REQUIRED')
            batches=clone(expected_batches);candidate=clone(path);binding=old['binding']
            request=digest({'binding':binding,'parent_tip':old['path']['tip'],'batches':batches,
                            'destination_tip':candidate['tip'],'point':p,'policy':policy})
            grant=self._vault._authorize(token,binding['event'],binding['context'],request)
            assert grant['request_digest']==request and grant['event']==binding['event']
            assert root(grant['archive'],binding['event'],binding['context'])==binding
            comparison=compare(grant['archive'],binding,old['batches'],old['path'],batches,candidate)
            semantic=candidate['edges'][-1]['successor'] if candidate['edges'] else old['semantic']
            assert self._key(semantic,p,policy)==old['dependency']
            record={**old,'batches':batches,'path':candidate,'semantic':semantic,'authorization_request':request}
            # No point arithmetic occurs here. Path and authority checks stay fresh.
            self._record=freeze(record);self._head=uuid4().hex
            self._work['point_cache_hits']+=1;self._work['path_checks']+=2;self._work['authority_checks']+=1
            result=self.receipt();result['comparison']=comparison;return result
