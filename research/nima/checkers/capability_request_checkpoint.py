"""Fixed-family, fail-closed capability requests. No provenance authority installed."""
from pathlib import Path
from fractions import Fraction as Q
from threading import RLock
from uuid import uuid4
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from verify_fine_refinement_obstruction import verify as verify_obstruction
from verify_scalar_envelope_band import check as verify_band
if not __debug__:raise RuntimeError('Assertions required')
FAMILY='owning-m4-moment-curve-two-history-v1'
def freeze(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def digest(x):return hashlib.sha256(freeze(x).encode()).hexdigest()
def snapshot(x):return json.loads(freeze(x))

class CapabilitySession:
    def __init__(self):
        self._lock=RLock();self._handle=None;self._state=None;self._section=None;self._ambiguity=None
    def _current(self,handle,expected):
        if self._handle is None or handle!=self._handle:raise ValueError('STALE_OR_FOREIGN_CHECKPOINT')
        assert expected==json.loads(self._state)
    def _receipt(self):
        return {'handle':self._handle,'state':json.loads(self._state),
          'bytes':{'live_state':len(self._state.encode()),'section':len(self._section.encode()),
                   'ambiguity_proof':len((self._ambiguity or '').encode()),'actual_history_selector':0},
          'authority':'NO_HISTORY_SELECTION_AUTHORITY'}
    def bootstrap(self,expected,section):
        with self._lock:
            if self._handle is not None:raise ValueError('ALREADY_BOOTSTRAPPED')
            contract=snapshot(expected);packet=snapshot(section)
            assert set(contract)=={'family','n','eta'} and contract['family']==FAMILY
            verify_band({'n':contract['n'],'eta':contract['eta']},packet)
            state={**contract,'section_digest':digest(packet),'actual_history':None,
              'capabilities':['verified-scalar-band','verified-fine-ambiguity'],'archive_reexposure':False}
            self._state=freeze(state);self._section=freeze(packet);self._handle=uuid4().hex
            return self._receipt()
    def tighten(self,handle,expected_before,new_eta,candidate):
        with self._lock:
            self._current(handle,expected_before);before=json.loads(self._state)
            eta=Q(new_eta)
            if not 0<=eta<=Q(before['eta']):raise ValueError('NOT_A_TIGHTENING')
            request={'n':before['n'],'eta':str(eta)};packet=snapshot(candidate)
            try:metrics=verify_band(request,packet)
            except (AssertionError,ValueError,KeyError,IndexError,TypeError,ZeroDivisionError):
                # A failed selector is not an impossibility theorem.
                return {'status':'SECTION_NOT_VERIFIED','history_separation_proved':False,**self._receipt()}
            after={**before,'eta':str(eta),'section_digest':digest(packet)}
            self._state=freeze(after);self._section=freeze(packet);self._ambiguity=None;self._handle=uuid4().hex
            return {'status':'SECTION_VERIFIED','verification':metrics,**self._receipt()}
    def request_fine(self,handle,expected_before,operation,point,certificate):
        with self._lock:
            self._current(handle,expected_before);state=json.loads(self._state)
            op=snapshot(operation);p=list(map(str,map(Q,point)));proof=snapshot(certificate)
            if set(op)!={'kind','h_upper'} or op['kind']!='append-fine-upper-then-exact-point-admission':
                raise PermissionError('UNSUPPORTED_CONTINUATION')
            expected={'family':state['family'],'n':state['n'],'continuation':op['kind'],'h_upper':op['h_upper']}
            assert proof['public_point']==p
            result=verify_obstruction(expected,proof)
            request={'state':state,'operation':op,'point':p}
            ambiguity={'status':'HISTORY_PROVENANCE_REQUIRED','request':request,'request_digest':digest(request),
              'alternatives':{'A':result['A_admits_point'],'B':result['B_admits_point']},
              'actual_history':None,'selected_answer':None,'obstruction':proof,
              'selector_lower_bound_bits':1,'scope':'Displayed fiber only; not whole-domain emptiness.'}
            self._ambiguity=freeze(ambiguity)
            return snapshot(ambiguity)
    def request_history_selection(self,handle,expected_before,request_digest,provenance):
        with self._lock:
            self._current(handle,expected_before)
            if self._ambiguity is None:raise ValueError('NO_VERIFIED_AMBIGUITY')
            request=json.loads(self._ambiguity)['request_digest']
            if request_digest!=request:raise ValueError('STALE_OR_MISMATCHED_REQUEST')
            token=snapshot(provenance)
            if not isinstance(token,dict) or token.get('request_digest')!=request:
                raise ValueError('MISMATCHED_PROVENANCE_CONTEXT')
            # Matching metadata, archive contents, witness choice and even an
            # asserted signature do not constitute an owning authority contract.
            raise NotImplementedError('OWNING_PROVENANCE_AUTHORITY_NOT_INTEGRATED')
    def reexpose(self,handle,expected_before):
        with self._lock:
            self._current(handle,expected_before);raise PermissionError('NO_ARCHIVE_AUTHORITY')
