"""Saved allocation replay is not whole-interface or history authority."""
from pathlib import Path
from threading import RLock
from uuid import uuid4
from fractions import Fraction as Q
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/grothendieck/checkers'))
import verify_active_cap_moment_master as kernel
from moment_column_checkpoints import VerifierSession,encode
if not __debug__:raise RuntimeError('Assertions required')
def digest(x):return hashlib.sha256(encode(x)).hexdigest()
def allocation(payload):
    state=payload['state'];columns=payload['seeds'];weights=list(map(Q,payload['weights']));blocks=[];sources=[]
    assert len(columns)==len(weights) and all(w>0 for w in weights)
    for b,(left,right) in enumerate(state['intervals']):
        selected=[(c,w) for c,w in zip(columns,weights) if c['block']==b]
        assert 1<=len(selected)<=5 and sum(w for c,w in selected)==1
        raw=[sum(w*Q(1+j%3)*Q(c['potential'][j-left]) for c,w in selected) for j in range(left,right+1)]
        observation=(raw[0],raw[-1],sum(raw),sum(Q(1,128**j)*v for j,v in zip(range(left,right+1),raw)))
        blocks.append(list(map(str,observation)));sources.append(raw)
    result={'status':payload['status'],'block_allocations':blocks,
            'scope':'local allocation only; no global lift for an infeasible master'}
    if payload['status']=='OPTIMUM':
        global_source={}
        for (left,right),raw in zip(state['intervals'],sources):
            for j,v in zip(range(left,right+1),raw):
                if j in global_source:assert global_source[j]==v
                global_source[j]=v
        ids=sorted(global_source);values=[global_source[j] for j in ids]
        public=(values[0],values[-1],sum(values),sum(Q(1,128**j)*global_source[j] for j in ids))
        assert all(sum(Q(a)*v for a,v in zip(f['normal'],public))<=Q(f['upper']) for f in state['frames'])
        assert all(sum(Q(a)*Q(v) for a,v in zip(f['normal'],blocks[f['block']]))<=Q(f['upper']) for f in state.get('local_frames',[]))
        if 'point' in state:assert tuple(map(Q,state['point']))==public
        result.update(global_source={str(j):str(global_source[j]) for j in ids},public_allocation=list(map(str,public)),
          objective_value=str(sum(Q(a)*v for a,v in zip(state['objective'],public))),scope='verified current feasible allocation, not the whole interface')
    else:assert payload['status']=='INCONSISTENT'
    return result

class AllocationSession:
    def __init__(self):
        self._lock=RLock();self._engine=None;self._engine_handle=None;self._head=None;self._capsule=None
    def _current(self,handle):
        if handle is None or handle!=self._head:raise ValueError('STALE_OR_FOREIGN_CHECKPOINT')
    def _capture(self):
        payload=self._engine.snapshot(self._engine_handle)
        # Checked local pricing caches are not needed to replay one allocation.
        capsule={k:payload[k] for k in ('state','seeds','weights','status','proof_digest','rule')}
        capsule['allocation']=allocation(capsule);self._capsule=encode(capsule);self._head=uuid4().hex
    def receipt(self):
        with self._lock:
            if self._head is None:raise ValueError('NOT_BOOTSTRAPPED')
            capsule=json.loads(self._capsule)
            return {'handle':self._head,'state':capsule['state'],'capsule_digest':hashlib.sha256(self._capsule).hexdigest(),
              'capabilities':{'replay_current_allocation':True,'new_queries':self._engine is not None,
                              'public_refinement':self._engine is not None,'whole_interface_from_columns':False,'fine_restore':False},
              'retained_columns':len(capsule['seeds']),'bytes':{'allocation_capsule':len(self._capsule),
                'attached_checkpoint':len(self._engine._payload) if self._engine is not None else 0},
              'authority':'No actual-history identity is inferred from these source columns.'}
    def bootstrap(self,expected,answer,compaction):
        with self._lock:
            if self._head is not None:raise ValueError('ALREADY_BOOTSTRAPPED')
            engine=VerifierSession(kernel.verify,kernel.verify_pricing)
            handle,_=engine.bootstrap(expected,answer,compaction)
            self._engine=engine;self._engine_handle=handle;self._capture();return self.receipt()
    def advance(self,handle,expected_before,expected_frame,answer,compaction):
        with self._lock:
            self._current(handle)
            if self._engine is None:raise PermissionError('SOURCE_BACKEND_DETACHED')
            assert expected_before==json.loads(self._capsule)['state']
            self._engine_handle,_=self._engine.advance(self._engine_handle,expected_before,expected_frame,answer,compaction)
            self._capture();return self.receipt()
    def check_new_query(self,handle,expected_query,answer):
        with self._lock:
            self._current(handle)
            if self._engine is None:raise PermissionError('SOURCE_BACKEND_DETACHED')
            current=json.loads(self._capsule)['state'];query=json.loads(encode(expected_query))
            assert {k:v for k,v in current.items() if k!='objective'}=={k:v for k,v in query.items() if k!='objective'}
            self._engine._check_state(query);kernel.verify(query,answer)
            return {'status':answer['status'],'value':answer.get('value'),'state':query,
                    'scope':'Fresh full source/pricing replay; no completeness inferred from retained columns.'}
    def detach(self,handle,expected_before):
        with self._lock:
            self._current(handle);assert expected_before==json.loads(self._capsule)['state']
            self._engine=None;self._engine_handle=None;self._head=uuid4().hex
            return self.receipt()
    def replay_allocation(self,handle):
        with self._lock:
            self._current(handle);capsule=json.loads(self._capsule)
            result=allocation(capsule);assert result==capsule['allocation']
            return {'state':capsule['state'],'allocation':result,'proof_digest':capsule['proof_digest'],
                    'source_admission':'Reused from this session\'s verified bootstrap/advance; no serialized import.'}
    def restore_fine(self,handle,provenance):
        with self._lock:
            self._current(handle);raise PermissionError('OWNING_HISTORY_AUTHORITY_NOT_INTEGRATED')
