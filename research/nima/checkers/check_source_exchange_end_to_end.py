# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Fresh bounded end-to-end audit with actual native matrix-response seeding."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import runpy
import numpy as np
from labelled_exchange_experiment import Experiment

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/source-exchange-end-to-end.json'
out.unlink(missing_ok=True)
support=[
 'check_exchange_feedback_adapter.py',
 'check_source_exchange_contract.py',
 'check_exchange_oscillator_instrument.py',
 'check_matrix_leg_exchange_closure.py',
 'check_witness_record_memory_gate.py',
 'check_exchange_shared_leg_composition.py',
 'check_labelled_exchange_experiment.py',
 'check_exchange_detector_calibration.py']
fresh={}
for name in support:
    with redirect_stdout(io.StringIO()): data=runpy.run_path(str(HERE/name))
    assert data['result']['status']=='passed'
    fresh[name]={'status':'passed','sha256':hashlib.sha256((HERE/name).read_bytes()).hexdigest()}
# Reuse the freshly executed detector check's actual native fixture, not a
# separately declared port-amplitude list.
native=data['native']; moments=data['moments']; detector=data['detector']
_,boundary,_,_,routes=native['build']({'a':(0,0),'s':(0,0)})
values=native['values']; evaluate=native['evaluate']
ex=Experiment(); events=[]; raw=[]
gamma=F(1,4)  # declared trace-to-X preparation gain, not fixed by source labels
for tag,size in (('a',11),('s',4)):
    for i in range(size):
        witness=routes(tag,i,0)[0]  # overwritten per comparison below
        for j in range(size):
            witness=routes(tag,i,j)[0]
            response=evaluate(boundary(witness),values)
            raw.append(response[0][0]+response[1][1])
            events.append(ex.compile(ex.labels[len(events)],witness,boundary,'native-matrix-fixture:roots00'))
seed=np.array([float(gamma*x) for x in raw])
prepared=ex.prepare(np.zeros(16),seed,np.eye(153)/2,'native-trace-times-one-quarter;vacuum-carrier;coherent-quadratures')
# First port(10,10) has positive trace14/3, hence prepared X=7/6.
port=120
assert raw[port]==F(14,3) and abs(seed[port]-7/6)<1e-12
word=[events[k] for k in (120,10,0,110)]
echo=ex.run(prepared,[events[port],events[port]])
rectangle=ex.run(prepared,word)
state0=ex.state(prepared); state_echo=ex.state(echo); state_rect=ex.state(rectangle)
tol=1e-10
assert np.max(np.abs(state0-state_echo))<tol
assert abs(state_rect[16+port])<tol
assert np.max(np.abs(rectangle.anchor-prepared.anchor))<tol
assert abs(state_rect@state_rect-state0@state0)<tol
assert np.max(np.abs(rectangle.covariance-prepared.covariance))<tol
# Seed legs remain provenance. Independent current records retain corrections.
corrections=state_rect[16:]-seed
assert np.linalg.norm(corrections)>0
assert np.max(np.abs(seed+corrections-state_rect[16:]))<tol
observations={
 'prepared_reference':moments(state0[16+port],**detector),
 'exchange_echo':moments(state_echo[16+port],**detector),
 'quarter_turn_echo':moments(-state0[16+port],**detector),
 'exchange_rectangle':moments(state_rect[16+port],**detector)}
b=detector['b']; reference=observations['prepared_reference'][0]-b
ratios={k:(v[0]-b)/reference for k,v in observations.items()}
for key,value in [('exchange_echo',1),('quarter_turn_echo',-1),('exchange_rectangle',0)]:
    assert abs(ratios[key]-value)<tol
# Common preparation rescaling changes physical resources and raw detector means,
# while these normalized discriminators stay unchanged.
scaled=ex.prepare(np.zeros(16),2*seed,np.eye(153)/2,'native-trace-times-one-half;coherent-quadratures')
scaled_echo=ex.run(scaled,[events[port],events[port]])
scaled_m=moments(ex.state(scaled_echo)[16+port],**detector)[0]-b
assert abs(scaled_m/reference-2)<tol
assert abs(np.linalg.norm(ex.state(scaled))**2/state0.dot(state0)-4)<tol

# Serialize actual source values and preparation contract alongside its checksum.
provenance={
 'native_matrix_values':{k:[[str(x) for x in row] for row in matrix] for k,matrix in values.items()},
 'trace_to_X_gain':str(gamma),'carrier_preparation':'zero coherent amplitude',
 'record_preparation':'coherent X means gamma*trace(Y_j X_i-d)',
 'conjugate_quadratures':'independent vacuum; supplied physical assumption',
 'reference':ex.reference,'comparison_count':len(events)}
ledger={
 'state':'conditional trace-seeded instrument map; native seed and independent record corrections retained',
 'operation':'checked event concatenation/reference transport; native shared-leg factorization rejected',
 'observable':'conditional coherent quadrature detector with declared loss/gain/noise/phase parameters',
 'normalization':'preparation gain and detector standards supplied; absolute current-field coupling open',
 'discriminator':'signed echo and first-port rectangle, conditional on monitored phase and preparation'}
result={
 'status':'passed','classification':'native_trace_seed_to_compiled_exchange_and_detector_chain_conditionally_checked',
 'tolerance':tol,'fresh_support_checks':fresh,
 'provenance':provenance,'success_criteria':ledger,
 'detector_parameters':detector,'predicted_detector_moments':observations,'offset_subtracted_mean_ratios':ratios,
 'checks':{'actual137_native_matrix_responses_seed_preparation':True,'full_state_echo':True,
           'rectangle_discriminator':True,'retained_record_corrections':True,
           'anchor_and_covariance_budget':True,'free_preparation_scale_hostile':True},
 'conclusion':'The actual native matrix-response fixture now feeds a declared coherent preparation, boundary-validated exchange compiler and calibrated-model readout. This closes a conditional source-labelled experiment, not source-selected dynamics or absolute physical normalization.',
 'objective_complete':False,
 'open_gates':['native selection of independent record attachment and pulse','independent physical preparation and phase standards',
               'current/field coupling and physical energy normalization'],
 'next_falsifier':'Test preparation and control resource accounting: a passing measurement model must not silently make resetting137 oscillator records and supplying pulse/phase references free.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('provenance','fresh_support_checks')},indent=2))
