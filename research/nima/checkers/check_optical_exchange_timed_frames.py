# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Delayed optical events in time-dependent endpoint coordinates."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import numpy as np

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/optical-exchange-timed-frames.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    calibration=runpy.run_path(str(HERE/'check_optical_exchange_calibration_bounds.py'))
prior=calibration['prior']; U=prior['U']; ideal=prior['ideal']; actual=calibration['B']
n=155; tol=1e-10
# Carrier16, records137, and TWO RETAINED environment modes. They are reused
# coherently here, not reset or treated as fresh independent noise at each event.
def operator(B,u,i):
    A=np.zeros((4,n),complex)
    A[0,16+i]=1; A[1,:16]=u.conj(); A[2,153]=1; A[3,154]=1
    V=A.conj().T[:,[0,2,1,3]]
    return np.eye(n)-A.conj().T@A+V@B@A
ra=np.array([.1,-.2,.3,-.1]); rb=np.array([-.15,.25,.05,-.3])
aa=np.array([.02,.01,-.03,.04]); ab=np.array([-.01,.03,.02,-.02])
def frame(t):
    ca=ra*t+aa*t*t/2; cb=rb*t+ab*t*t/2
    phase=np.exp(1j*(cb[None,:]-ca[:,None])).reshape(16)
    rate=((rb+ab*t)[None,:]-(ra+aa*t)[:,None]).reshape(16)
    return np.r_[phase,np.ones(139)],np.r_[rate,np.zeros(139)]
def timed(F,tin,tout):
    if tout<=tin: raise ValueError('round-trip delay must be positive')
    si,_=frame(tin); so,_=frame(tout)
    return so[:,None]*F*si.conj()[None,:]

rng=np.random.default_rng(37137)
x=rng.normal(size=n)+1j*rng.normal(size=n); x/=np.linalg.norm(x)
z=rng.normal(size=(n,3))+1j*rng.normal(size=(n,3))
C=z@z.conj().T/1000  # full Hermitian complex-amplitude covariance
history=[(121,0.,.7),(0,.7,1.5),(136,1.5,2.6),(11,2.6,3.4)]
for B in (ideal,actual):
    lab=x.copy(); cov=C.copy(); s0,_=frame(history[0][1])
    moving=s0*x; moving_cov=s0[:,None]*C*s0.conj()[None,:]
    accumulated=np.eye(n,dtype=complex); lab_total=np.eye(n,dtype=complex)
    for i,tin,tout in history:
        F=operator(B,U[i],i); Ft=timed(F,tin,tout)
        assert np.max(np.abs(F.conj().T@F-np.eye(n)))<tol
        lab=F@lab; cov=F@cov@F.conj().T
        moving=Ft@moving; moving_cov=Ft@moving_cov@Ft.conj().T
        accumulated=Ft@accumulated; lab_total=F@lab_total
        so,_=frame(tout)
        assert np.max(np.abs(moving-so*lab))<tol
        assert np.max(np.abs(moving_cov-so[:,None]*cov*so.conj()[None,:]))<tol
        assert abs(np.vdot(moving,moving).real+np.trace(moving_cov).real-(np.vdot(x,x).real+np.trace(C).real))<tol
    assert np.max(np.abs(accumulated-timed(lab_total,0.,3.4)))<tol
    # A static conjugation at the input does not describe the delayed output frame.
    i,tin,tout=history[0]; F=operator(B,U[i],i); si,_=frame(tin)
    wrong=si[:,None]*F*si.conj()[None,:]
    assert np.linalg.norm((wrong-timed(F,tin,tout))@x)>1e-3

# Ideal anchors are transported, not numerically frozen in the moving frame.
lab=x.copy(); anchor0=lab[:16]+U.T@lab[16:153]
for i,tin,tout in history:
    lab=operator(ideal,U[i],i)@lab
    assert np.max(np.abs(lab[:16]+U.T@lab[16:153]-anchor0))<tol
    s,_=frame(tout); u_new=U*s[:16][None,:]
    framed=s*lab
    assert np.max(np.abs(framed[:16]+u_new.T@framed[16:153]-s[:16]*anchor0))<tol

# Continuous connection test uses the prior ideal rank-one Hamiltonian pulse.
# It is an interpolation check, NOT a derivation of internal cavity trajectories.
i=121; duration=.7
normal=np.r_[U[i],-np.eye(137)[i],np.zeros(2)]/np.sqrt(2)
e=np.eye(n,dtype=complex)[153]
P=np.outer(normal,normal.conj())+np.outer(e,e.conj())
H=np.pi/duration*P
for t in (.1,.3,.6):
    y=x+(np.exp(-1j*np.pi*t/duration)-1)*(P@x)
    dy=-1j*H@y
    s,rate=frame(t); sy=s*y
    dsy=1j*rate*sy+s*dy
    transformed=s[:,None]*H*s.conj()[None,:]-np.diag(rate)
    assert np.max(np.abs(1j*dsy-transformed@sy))<tol
    without_connection=s[:,None]*H*s.conj()[None,:]
    assert np.linalg.norm(1j*dsy-without_connection@sy)>1e-3
# Operator-error norms are invariant under TWO-ENDPOINT frame transport.
F=operator(actual,U[i],i); F0=operator(ideal,U[i],i)
assert abs(np.linalg.norm(timed(F,0.,duration)-timed(F0,0.,duration),2)-np.linalg.norm(F-F0,2))<tol
# Timestamp error is an extra calibration error, not a free gauge correction.
dt=.02; right=timed(F0,0.,duration); wrong=timed(F0,0.,duration+dt)
_,r0=frame(duration); _,r1=frame(duration+dt)
clock_bound=dt*max(np.max(np.abs(r0)),np.max(np.abs(r1)))
clock_error=np.linalg.norm(wrong-right,2)
assert 1e-5<clock_error<=clock_bound+tol
try: timed(F0,1.,1.)
except ValueError: pass
else: raise AssertionError('zero-delay event accepted')

result={
 'status':'passed','classification':'two_endpoint_timed_frame_transport_preserves_optical_exchange_contract',
 'tolerance':tol,
 'checks':{'calibration_chain_fresh':True,'four_delayed_events_two_plants':True,
           'full_retained_environment_covariance':True,'temporal_composition_telescopes':True,
           'input_only_static_frame_hostile':True,'transported_anchor':True,
           'continuous_connection_term_required':True,'operator_error_certificate_frame_invariant':True,
           'timestamp_error_bound':True,'zero_delay_rejected':True},
 'clock_control':{'timestamp_error':dt,'operator_error':float(clock_error),'bound':float(clock_bound)},
 'conclusion':'Delayed events require S(t_out) F S(t_in)^dagger. The continuous ideal pulse requires i dot(S) S^dagger as well. With those terms, state, covariance, anchors and calibration error bounds transport consistently; frame drift is not an added physical force.',
 'scope':'Prescribed known endpoint frames and stored event-boundary ports. Retained environment modes are reused coherently; independent fresh-environment channel composition is a different model. No clock or phase trace has been measured.',
 'next_falsifier':'Combine port/router/time calibration bounds into a multi-event error budget with explicit environment access or reset assumptions; reject histories whose calibration/frame evidence is missing.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
