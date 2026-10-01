# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Conditional full-history calibration bound with explicit retained environment."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import numpy as np

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/optical-exchange-history-certificate.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    timed=runpy.run_path(str(HERE/'check_optical_exchange_timed_frames.py'))
cal=timed['calibration']; op=timed['operator']; transport=timed['timed']; frame=timed['frame']
U=timed['U']; actual=timed['actual']; ideal=timed['ideal']; n=155; tol=1e-10
nominal=np.array([.1,.8,1.6,2.7,3.5]); slots=[121,0,136,11]
clock_radius=.002
certificate={
 'port_evidence':'synthetic-four-complex-port-probes',
 'router_evidence':'synthetic-separate-complex-supermode-probes',
 'frame_evidence':'prescribed-endpoint-phase-and-clock-trace',
 'evidence_kind':'synthetic','environment_policy':'retained-two-modes',
 'valid_interval':[0.,4.], 'entry_radius':cal['entry_radius'],
 'router_radius':cal['router_radius'],'clock_radius':clock_radius,
 'history_tolerance':.08}

def validate(cert,times):
    for key in ('port_evidence','router_evidence','frame_evidence'):
        if not cert.get(key): raise ValueError('missing '+key)
    if cert.get('evidence_kind') not in ('synthetic','measured'): raise ValueError('evidence kind')
    if cert.get('environment_policy')!='retained-two-modes': raise ValueError('different environment model')
    if np.any(np.diff(times)<=2*cert['clock_radius']): raise ValueError('uncertain event ordering')
    lo,hi=cert['valid_interval']
    if times[0]-cert['clock_radius']<lo or times[-1]+cert['clock_radius']>hi:
        raise ValueError('stale calibration interval')
    for key in ('entry_radius','router_radius','clock_radius','history_tolerance'):
        if not np.isfinite(cert[key]) or cert[key]<0: raise ValueError('invalid bound')

validate(certificate,nominal)
# Full4x4 calibration has spectral uncertainty <= Frobenius <=4*entry radius.
event_bound=float(np.linalg.norm(cal['measured']-ideal,2)+4*certificate['entry_radius']+np.sqrt(2)*certificate['router_radius'])
def frame_uncertainty(t):
    _,left=frame(t-clock_radius); _,right=frame(t+clock_radius)
    return clock_radius*max(np.max(np.abs(left)),np.max(np.abs(right)))
# Shared boundary timestamps telescope: only initial/final coordinate error
# remains. Physical phase/control errors are already in the event bound.
clock_bound=float(frame_uncertainty(nominal[0])+frame_uncertainty(nominal[-1]))
history_bound=min(2.,len(slots)*event_bound+clock_bound)
assert history_bound<certificate['history_tolerance']

jitter=np.array([.001,-.0015,.0012,-.0007,.0018])
assert np.max(np.abs(jitter))<=clock_radius
true_times=nominal+jitter
Fa=np.eye(n,dtype=complex); Fi=np.eye(n,dtype=complex)
for k,i in enumerate(slots):
    u=U[i]
    # Independently bounded phase-sensitive mode-router error.
    axis=np.eye(16,dtype=complex)[(i+1)%16]
    orth=axis-u*np.vdot(u,axis); orth/=np.linalg.norm(orth)
    v=np.cos(.001)*u+np.sin(.001)*orth
    assert np.linalg.norm(v-u)<=certificate['router_radius']
    A=op(actual,v,i); I=op(ideal,u,i)
    assert np.linalg.norm(A-I,2)<=event_bound+tol
    Fa=transport(A,true_times[k],true_times[k+1])@Fa
    Fi=transport(I,nominal[k],nominal[k+1])@Fi
actual_error=float(np.linalg.norm(Fa-Fi,2))
assert actual_error<=history_bound+tol
rng=np.random.default_rng(47137)
mu=rng.normal(size=n)+1j*rng.normal(size=n); mu/=np.linalg.norm(mu)
Z=rng.normal(size=(n,4))+1j*rng.normal(size=(n,4)); C=Z@Z.conj().T/1000
mean_error=float(np.linalg.norm((Fa-Fi)@mu))
cov_error=float(np.linalg.norm(Fa@C@Fa.conj().T-Fi@C@Fi.conj().T,2))
cov_bound=float(2*history_bound*np.linalg.norm(C,2))
assert mean_error<=history_bound*np.linalg.norm(mu)+tol
assert cov_error<=cov_bound+tol
# A silent fresh-environment replacement changes even the record mean after
# repeated events. These are different physical memory policies, not gauges.
F=op(actual,U[121],121)
x=np.zeros(n,complex); x[16+121]=1
retained=x.copy(); reset=x.copy()
for _ in range(3):
    retained=F@retained
    reset=F@reset; reset[153:]=0
memory_record_difference=abs(retained[16+121]-reset[16+121])
assert memory_record_difference>1e-6

def rejects(change,times=nominal):
    bad=dict(certificate); bad.update(change)
    try: validate(bad,times)
    except ValueError: return
    raise AssertionError('invalid history certificate accepted')
rejects({'frame_evidence':''}); rejects({'router_evidence':''}); rejects({'port_evidence':''})
rejects({'environment_policy':'fresh-vacuum-each-event'})
rejects({'valid_interval':[0.,3.]})
rejects({},np.array([.1,.101,.8,1.6,3.5]))

result={
 'status':'passed','classification':'conditional_retained_environment_history_error_certificate',
 'tolerance':tol,'certificate_contract':certificate,
 'bounds':{'full_event_error':event_bound,'endpoint_clock_error':clock_bound,
           'four_event_operator_error':history_bound,'actual_operator_error':actual_error,
           'actual_mean_error':mean_error,'covariance_bound':cov_bound,'actual_covariance_error':cov_error},
 'environment_hostile_record_difference':float(memory_record_difference),
 'checks':{'prior_chain_fresh':True,'telescoping_operator_bound':True,'mean_and_covariance_bounds':True,
           'environment_memory_policy_hostile':True,'missing_evidence_rejected':True,
           'stale_calibration_rejected':True,'uncertain_order_rejected':True},
 'conclusion':'Full-port calibration and independently bounded router/timestamp errors certify a delayed event history under an explicit retained-environment model. Replacing that environment by fresh vacuum changes the prediction and is rejected by this contract.',
 'measurement_status':'synthetic only; identifiers validate contract completeness, not empirical authenticity',
 'next_falsifier':'Package a final decision gate that distinguishes exact exchange, certified approximate exchange, rejected plant and missing measured calibration; do not report synthetic evidence as measured independent controls.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
