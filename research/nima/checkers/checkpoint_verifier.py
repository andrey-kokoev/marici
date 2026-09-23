"""Process-local verified checkpoints; no untrusted checkpoint import.

Only local arithmetic is memoized. State admission, gain charts, transition
bindings, interface closure and expanded negative cycles are checked afresh.
"""
from dataclasses import dataclass,asdict
from fractions import Fraction as Q
import json,uuid
from threading import RLock
from functools import wraps
from verify_modular_difference_interfaces import check as difference_check,closure_check,digest
from verify_balanced_gain_adapter import check as gain_check
from verify_incremental_difference_interfaces import archived_transition
from verify_incremental_gain_interfaces import transition as gain_transition
if not __debug__:raise RuntimeError('Assertions required')

def encode(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),default=lambda x:str(x) if isinstance(x,Q) else fail_type(x))
def fail_type(x):raise TypeError(type(x).__name__)

@dataclass(frozen=True)
class _Checkpoint:
    handle: str
    kind: str
    state: str
    proof: str
    result: str
    locals: tuple

def _serialized(method):
    @wraps(method)
    def call(self,*args,**kwargs):
        with self._lock:return method(self,*args,**kwargs)
    return call

class VerifierSession:
    """One linear head. Forks/restarts require a fresh full bootstrap.

    Expected states and operations are supplied by the owning caller, not
    extracted as authority from a candidate transition or checkpoint receipt.
    """
    def __init__(self):
        self.__head=None;self._lock=RLock()
    def _run(self,kind,state,proof,old=()):
        entries=[];stats={'local_checks':0,'local_hits':0,'interface_checks':0,
                          'chart_checks':int(kind=='gain'),'hashed_local_proof_bytes':0}
        def local(nodes,edges,p):
            i=len(entries)
            dependency={'epoch':'local-closure-check-v1','language':kind,'m':state['m'],
              'binding':state['binding'],'retention':state['retention'],'raw_block':state['blocks'][i],
              'nodes':nodes,'edges':edges,
              'local_scales':[[v,proof['scales'][v]] for v in nodes] if kind=='gain' else None}
            key=digest(dependency);proof_key=digest(p);stats['hashed_local_proof_bytes']+=len(encode(p).encode())
            if i<len(old) and old[i][:2]==(key,proof_key):
                encoded=old[i][2];data=json.loads(encoded)
                D=None if data is None else [list(map(Q,row)) for row in data];stats['local_hits']+=1
            else:
                D=closure_check(nodes,edges,p);encoded=encode(D);stats['local_checks']+=1
            entries.append((key,proof_key,encoded));return D
        def interface(nodes,edges,p):
            stats['interface_checks']+=1;return closure_check(nodes,edges,p)
        def modular(expected,p):
            return difference_check(expected,p,_local_check=local,_interface_check=interface)
        if kind=='difference':result=modular(state,proof)
        elif kind=='gain':result=gain_check(state,proof,_difference_check=modular)
        else:raise ValueError('UNKNOWN_LANGUAGE')
        return encode(result),tuple(entries),stats
    def _publish(self,kind,state,proof,verified):
        result,entries,stats=verified
        head=_Checkpoint(uuid.uuid4().hex,kind,encode(state),encode(proof),result,entries)
        receipt={'handle':head.handle,'language':kind,'state_digest':digest(state),'proof_digest':digest(proof),
                 'status':proof['status'],'result':json.loads(result),'work':dict(stats),
                 'checkpoint_encoded_bytes':len(encode(asdict(head)).encode())}
        self.__head=head
        return receipt
    @_serialized
    def bootstrap(self,kind,expected,proof):
        if self.__head is not None:raise ValueError('SESSION_ALREADY_ADMITTED')
        # Round-trip inputs before checking so caller mutation cannot change
        # the checked snapshot retained in the checkpoint.
        state=json.loads(encode(expected));packet=json.loads(encode(proof))
        if state['retention']!='archive-backed':raise PermissionError('ARCHIVE_TRANSITIONS_ONLY')
        return self._publish(kind,state,packet,self._run(kind,state,packet))
    @_serialized
    def advance(self,handle,expected_before,expected_operation,candidate):
        head=self.__head
        if head is None or handle!=head.handle:raise ValueError('STALE_OR_FOREIGN_CHECKPOINT')
        before=json.loads(head.state);previous=json.loads(head.proof)
        assert expected_before==before
        operation=json.loads(encode(expected_operation));t=json.loads(encode(candidate));verified=[];calls=0
        def checked(state,packet):
            nonlocal calls
            calls+=1
            if calls==1:
                assert state==before and packet==previous
                return json.loads(head.result)
            assert calls==2
            result=self._run(head.kind,state,packet,head.locals);verified.append(result)
            return json.loads(result[0])
        if head.kind=='difference':after=archived_transition(before,operation,previous,t,_check=checked)
        else:after=gain_transition(before,operation,previous,t,_check=checked)
        assert calls==2 and len(verified)==1
        # Publishing occurs only after all arithmetic AND envelope/cache
        # declarations pass. Failure never advances or poisons the head.
        return self._publish(head.kind,after,t['after'],verified[0])
