"""Fixed-family atomic authority + exact fine-state publication."""
from pathlib import Path
from fractions import Fraction as Q
from uuid import uuid4
import sys,json
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from authority_aware_upgrade import UpgradeSession,ArchiveAuthority
from approximate_section_checkpoint import copy,encode,digest,source
from verify_scalar_envelope_band import domain,envelopes
if not __debug__:raise RuntimeError('Assertions required')

def fine_state(before,event,history,operation):
    assert history in ('A','B')
    n=before['request']['n'];polygon=domain(n);lower,upper=envelopes(n);rows=[]
    for a,b in zip(polygon,polygon[1:]+polygon[:1]):
        normal=[b[1]-a[1],a[0]-b[0],Q(0)]
        rows.append((normal,normal[0]*a[0]+normal[1]*a[1]))
    rows += [([Q(0),Q(0),Q(-1)],Q(0)),([Q(0),Q(0),Q(1)],Q(1))]
    if history=='A':rows += [([a,b,Q(-1)],-c) for a,b,c in lower]
    else:rows += [([-a,-b,Q(1)],c) for a,b,c in upper]
    rows += [([*map(Q,r['normal']),Q(0)],Q(r['upper'])) for r in before['frames']]
    rows.append(([Q(0),Q(0),Q(1)],Q(operation['h_upper'])))
    return {'family':before['family'],'n':n,'history':history,'retirement_event':event,
      'parent_digest':digest(before),'operation':copy(operation),
      'rows':[{'normal':list(map(str,a)),'upper':str(b)} for a,b in rows],
      'capabilities':{'exact_point_admission':True,'exact_lift':True,'approximate_lift':False,'archive':False}}

class FineSuccessorSession(UpgradeSession):
    def __init__(self,authority):super().__init__(authority);self._fine=False
    def receipt(self):
        with self._lock:
            if not self._fine:return super().receipt()
            return {'handle':self._handle,'state':copy(self._state),'mode':'exact-fine-successor',
              'bytes':{'fine_state':len(encode(self._state).encode()),'section':0,'replacement_section':0},
              'scope':'Exact pointwise fine queries; no retained approximate section or re-exposure.'}
    def commit_fine(self,handle,expected_before,operation,obstruction,archive_reference,candidate):
        with self._lock:
            self.current(handle);assert expected_before==self._state
            if self._fine:raise PermissionError('ALREADY_FINE')
            op,_=self._obstruction(operation,obstruction);packet=copy(candidate)
            # The vault lock spans authority validation through publication:
            # concurrent revocation cannot race between check and commit.
            with self._authority._lock:
                history=self._authority._resolve(archive_reference,self._event,self._context)
                expected=fine_state(self._state,self._event,history,op)
                assert set(packet)=={'before_digest','retirement_event','after'}
                assert packet['before_digest']==digest(self._state) and packet['retirement_event']==self._event
                assert packet['after']==expected
                self._state=expected;self._proof=None;self._metrics=None;self._resolution=None
                self._fine=True;self._handle=uuid4().hex
                return self.receipt()
    def lift(self,handle,point):
        with self._lock:
            self.current(handle)
            if self._fine:raise PermissionError('USE_EXACT_FINE_QUERY')
            return super().lift(handle,point)
    def restrict(self,handle,expected_before,operation):
        with self._lock:
            self.current(handle)
            if self._fine:raise PermissionError('FINE_TRANSITIONS_NOT_IMPLEMENTED')
            return super().restrict(handle,expected_before,operation)
    def request_upgrade(self,handle,expected_before,operation,obstruction):
        with self._lock:
            self.current(handle)
            if self._fine:raise PermissionError('ALREADY_FINE')
            return super().request_upgrade(handle,expected_before,operation,obstruction)
    def resolve(self,*args,**kwargs):raise PermissionError('USE_ATOMIC_FINE_COMMIT')
    def exact_query(self,handle,point):
        with self._lock:
            self.current(handle)
            if not self._fine:raise PermissionError('NO_EXACT_FINE_CAPABILITY')
            p=tuple(map(Q,point))
            if len(p)!=2:raise ValueError('NONPUBLIC_POINT')
            lows=[];highs=[]
            for i,row in enumerate(self._state['rows']):
                a,b,c=map(Q,row['normal']);rhs=Q(row['upper'])-a*p[0]-b*p[1]
                if c==0:
                    if rhs<0:return {'state':copy(self._state),'point':list(map(str,p)),'admits':False,'violated_public_row':i}
                elif c<0:lows.append((rhs/c,i))
                else:highs.append((rhs/c,i))
            lo,li=max(lows);hi,ui=min(highs)
            answer={'state':copy(self._state),'point':list(map(str,p)),'admits':lo<=hi,
                    'interval':[str(lo),str(hi)],'bound_rows':[li,ui]}
            if lo<=hi:answer['source_lift']=list(map(str,source(*p,(lo+hi)/2)))
            return answer
