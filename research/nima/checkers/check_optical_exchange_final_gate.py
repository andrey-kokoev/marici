# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Final bounded optical realization decision; no measured evidence is invented."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import math
import runpy
import numpy as np

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/optical-exchange-final-gate.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    history=runpy.run_path(str(HERE/'check_optical_exchange_history_certificate.py'))
packet=history['result']; assert packet['status']=='passed'

def decide(lower,upper,tolerance,evidence_kind):
    if not all(math.isfinite(x) for x in (lower,upper,tolerance)) or not 0<=lower<=upper or tolerance<0:
        raise ValueError('invalid error interval')
    if evidence_kind not in ('analytic','synthetic','measured'): raise ValueError('unknown evidence kind')
    if lower>tolerance: return 'rejected_by_error_lower_bound'
    if upper>tolerance: return 'inconclusive_bound_requires_refinement'
    if evidence_kind=='analytic': return 'conditional_model_bound_passes'
    if evidence_kind=='synthetic': return 'synthetic_certificate_passes_not_measured'
    # A metadata label is NOT an empirical provenance/uncertainty review.
    return 'numerical_bound_passes_empirical_evidence_review_required'

bound=packet['bounds']['four_event_operator_error']
limit=packet['certificate_contract']['history_tolerance']
synthetic=decide(0,bound,limit,'synthetic')
assert synthetic=='synthetic_certificate_passes_not_measured'
# The actual synthetic error is below.03, while its conservative bound exceeds
# .03: calling the plant disproved in this case would be a false inference.
assert packet['bounds']['actual_operator_error']<.03<bound
assert decide(0,bound,.03,'synthetic')=='inconclusive_bound_requires_refinement'
# A stricter physical label alone cannot promote the same numerical evidence.
assert decide(0,bound,limit,'measured')=='numerical_bound_passes_empirical_evidence_review_required'
prior=history['timed']['calibration']['prior']
error=float(np.linalg.norm(prior['frozen']-prior['ideal'],2))
uncertainty=4e-4
frozen=decide(max(0,error-uncertainty),error+uncertainty,.02,'analytic')
assert frozen=='rejected_by_error_lower_bound'
assert decide(0,0,0,'analytic')=='conditional_model_bound_passes'
try: decide(float('nan'),bound,limit,'synthetic')
except ValueError: pass
else: raise AssertionError('nonfinite certificate accepted')

support=[
 'check_optical_plant_endpoint_exchange.py',
 'check_optical_exchange_calibration_bounds.py',
 'check_optical_exchange_timed_frames.py',
 'check_optical_exchange_history_certificate.py']
result={
 'status':'passed','classification':'optical_endpoint_synthesis_model_complete_measured_calibration_missing',
 'fresh_dependency_hashes':{p:hashlib.sha256((HERE/p).read_bytes()).hexdigest() for p in support},
 'decisions':{
   'ideal_boundary':'exact_exchange_in_declared_model_with_all137_embeddings_checked',
   'frozen_cavity':frozen,
   'near_ideal_four_event_history':synthetic,
   'tighter_uncertified_tolerance':'inconclusive_not_disproved',
   'physical_apparatus':'unverified_missing_independently_measured_calibration'},
 'history_operator_bound':bound,'predeclared_history_tolerance':limit,
 'checks':{'full_prior_optical_and_phase_chain_fresh':True,'lower_vs_upper_bound_logic':True,
           'synthetic_not_promoted_to_measured':True,'nonfinite_certificate_rejected':True},
 'required_measured_packet':[
   'complex four-port probe records and input standards with independently justified uncertainty bounds',
   'phase-sensitive16-mode router characterization for each used slot',
   'time-stamped endpoint phase reference and synchronization uncertainty',
   'calibration validity interval and predeclared tolerance before validation inputs',
   'environment access/reuse/reset contract and stored-port timing',
   'held-out exchange or echo/rectangle data with preparation and detector calibration'],
 'conclusion':'The optical plant and endpoint-phase adapter combine consistently, and approximate exchange is certifiable from independent control bounds in the declared model. The frozen lossy plant fails; a synthetic near-ideal history passes. No measured physical realization has been established.',
 'model_test_complete':True,'measured_realization_established':False,
 'next_required_input':'Independently acquired calibration and held-out apparatus records; further synthetic passes cannot substitute for them.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
