"""Contract-preserving substitution need not preserve a selected witness.

Verifier-owned live FullPolygonSession providers, not descriptor imports.
"""
from contextlib import ExitStack,contextmanager
from threading import RLock
from uuid import uuid4
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
from full_polygon_checkpoint import FullPolygonSession,verify_full_polygon,interpolate,intersection
from checked_retirement_interface import freeze
if not __debug__:raise RuntimeError('Assertions required')
ADMISSIBLE='return-some-exact-admissible-fine-lift'
SELECTED='preserve-selected-source-vector'
def digest(x):return hashlib.sha256(freeze(x).encode()).hexdigest()
def copy(x):return json.loads(freeze(x))
@contextmanager
def provider_locks(*providers):
    if any(type(p) is not FullPolygonSession for p in providers):raise TypeError('VERIFIED_LIVE_PROVIDER_REQUIRED')
    with ExitStack() as stack:
        for p in sorted(set(providers),key=id):stack.enter_context(p._lock)
        yield

def capture(provider,handle,section_id,expected_state,scope):
    provider._current(handle)
    assert provider._state.descriptor()==expected_state
    assert expected_state['capabilities']=={'lift':True,'reexpose':False}
    if section_id not in provider._polygon_covers:raise ValueError('UNKNOWN_COVER')
    proof=json.loads(provider._polygon_covers[section_id])
    # Strictly this workload requires both providers to cover the SAME full
    # current polygon. Arbitrary restriction scopes need another admission.
    work=verify_full_polygon(provider._state,scope,proof)
    return {'handle':handle,'section_id':section_id,'state':copy(expected_state),'scope':copy(scope),
            'fine_context_digest':hashlib.sha256(provider._state.lift_json.encode()).hexdigest(),
            'section_digest':digest(proof),'proof':proof,'verification':work}
def map_comparison(left,right):
    def cells(proof):
        vertices=[tuple(map(Q,p)) for p in proof['vertices']];lifts=[tuple(map(Q,t)) for t in proof['source_lifts']]
        return [([vertices[i] for i in ids],[lifts[i] for i in ids]) for ids in proof['triangles']]
    checks=0;counterexample=None
    for p,t in cells(left):
        for q,u in cells(right):
            for point in intersection(p,q):
                a,b=interpolate(p,t,point),interpolate(q,u,point);checks+=1
                if a!=b and counterexample is None:
                    counterexample={'point':list(map(str,point)),'left_lift':list(map(str,a)),'right_lift':list(map(str,b))}
    return {'pointwise_equal':counterexample is None,'intersection_vertex_checks':checks,'counterexample':counterexample}

class ProviderRouter:
    def __init__(self):self._lock=RLock();self._head=None;self._provider=None;self._record=None;self._contract=None
    def _current(self,handle):
        if self._head is None or handle!=self._head:raise ValueError('STALE_ROUTER_HEAD')
    def _live(self):
        r=json.loads(self._record);self._provider._current(r['handle'])
        assert self._provider._state.descriptor()==r['state']
        assert self._provider._polygon_covers.get(r['section_id'])==freeze(r['proof'])
        assert hashlib.sha256(self._provider._state.lift_json.encode()).hexdigest()==r['fine_context_digest']
        return r
    def receipt(self):
        with self._lock:
            if self._provider is None:raise ValueError('NOT_BOOTSTRAPPED')
            with provider_locks(self._provider):
                r=self._live()
                return {'handle':self._head,'contract':self._contract,'migration_binding':r['state']['migration_binding'],
                  'scope_digest':digest(r['scope']),'section_digest':r['section_digest'],
                  'provider_generation':r['handle'],'fine_context_digest':r['fine_context_digest'],
                  'capabilities':{'exact_admissible_lift':True,'archive_reexposure':False,'actual_history_selection':False},
                  'bytes':{'router_record':len(self._record.encode()),
                           'provider_polygon_encodings':sum(len(p.encode()) for p in self._provider._polygon_covers.values()),
                           'provider_fine_context':len(self._provider._state.lift_json.encode())}}
    def bootstrap(self,provider,handle,section_id,expected_state,scope,contract=ADMISSIBLE):
        with self._lock,provider_locks(provider):
            if self._head is not None:raise ValueError('ALREADY_BOOTSTRAPPED')
            if contract not in (ADMISSIBLE,SELECTED):raise ValueError('UNKNOWN_CONTRACT')
            record=capture(provider,handle,section_id,copy(expected_state),copy(scope))
            self._provider=provider;self._record=freeze(record);self._contract=contract;self._head=uuid4().hex
            return self.receipt()
    def substitute(self,handle,expected_before,provider,provider_handle,section_id,expected_state):
        with self._lock:
            self._current(handle)
            with provider_locks(self._provider,provider):
                assert expected_before==self.receipt();old=self._live()
                target=capture(provider,provider_handle,section_id,copy(expected_state),old['scope'])
                assert target['state']==old['state'] and target['fine_context_digest']==old['fine_context_digest']
                comparison=map_comparison(old['proof'],target['proof'])
                certificate={'contract':self._contract,'migration_binding':old['state']['migration_binding'],
                  'scope_digest':digest(old['scope']),'fine_context_digest':old['fine_context_digest'],
                  'source_section':old['section_digest'],'target_section':target['section_digest'],
                  'source_generation':old['handle'],'target_generation':target['handle'],
                  'both_full_domain_sections_verified':True,'map_comparison':comparison}
                if self._contract==SELECTED and not comparison['pointwise_equal']:
                    return {'status':'REFUSED_SELECTED_WITNESS_CHANGE','comparison':certificate,'head_unchanged':True}
                self._provider=provider;self._record=freeze(target);self._head=uuid4().hex
                return {'status':'SUBSTITUTED','comparison':certificate,'receipt':self.receipt()}
    def lift(self,handle,point):
        with self._lock:
            self._current(handle)
            with provider_locks(self._provider):
                record=self._live()
                return self._provider.covered_lift(record['handle'],record['section_id'],point)
    def reexpose(self,handle):
        with self._lock:
            self._current(handle);raise PermissionError('LIFT_SUBSTITUTION_IS_NOT_ARCHIVE_AUTHORITY')
