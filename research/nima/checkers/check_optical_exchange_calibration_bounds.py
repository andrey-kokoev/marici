# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Independent-port calibration design and synthetic held-out regression."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import numpy as np

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/optical-exchange-calibration-bounds.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_optical_plant_endpoint_exchange.py'))
plant=prior['plant']; apply=prior['apply']; U=prior['U']; tol=1e-10
swap=np.array([[0,1],[1,0]],complex)
# Settings and tolerances fixed before generating any validation inputs.
r1=.002; t1=np.sqrt(1-r1*r1); t2=.003; r2=np.sqrt(1-t2*t2)
ell=.004; a=np.sqrt(1-ell*ell); phi=.005
B=plant(r1,t1,r2,t2,a,ell,np.exp(.11j),np.exp(1j*(phi-.11)))
rows=[0,2]; cols=[0,1]; envcols=[2,3]
T=B[np.ix_(rows,cols)]; E=B[np.ix_(rows,envcols)]
rho=a*r2
analytic_retained=np.sqrt(2*(1-t1))+(1-rho)+2*rho*np.sin(abs(phi)/2)
assert np.linalg.norm(T-swap,2)<=analytic_retained+tol
assert abs(np.linalg.norm(E,2)-np.sqrt(1-rho*rho))<tol
# A vacuum environment restores canonical coherent covariance despite loss.
noise=E@E.conj().T/2
assert np.max(np.abs(T@T.conj().T/2+noise-np.eye(2)/2))<tol
assert np.linalg.norm(T@T.conj().T/2-np.eye(2)/2)>1e-6

# Synthetic independent calibration: four known unit port probes, complex
# outputs referenced in both quadratures. Entrywise complex error radius is
# an externally supplied calibration bound, NOT inferred from held-out tests.
entry_radius=1e-4
error=entry_radius*.5*np.exp(1j*np.arange(16).reshape(4,4))
measured=B+error
assert np.max(np.abs(measured-B))<=entry_radius
# For a2x2 complex block, spectral error <= Frobenius error <=2*entry_radius.
That=measured[np.ix_(rows,cols)]; Ehat=measured[np.ix_(rows,envcols)]
router_radius=.0011
certificate_retained=float(np.linalg.norm(That-swap,2)+2*entry_radius+np.sqrt(2)*router_radius)
certificate_environment=float(np.linalg.norm(Ehat,2)+2*entry_radius)
acceptance_limit=.02
assert certificate_retained<acceptance_limit
# Choose an independently specified routing error within that bound.
i=121; u=U[i]; orth=np.eye(16,dtype=complex)[0]-u*np.vdot(u,np.eye(16)[0]); orth/=np.linalg.norm(orth)
v=np.cos(.001)*u+np.sin(.001)*orth
assert np.linalg.norm(v-u)<=router_radius
ideal=prior['ideal']
rng=np.random.default_rng(27137)
max_error=0.
for _ in range(40):
    x=rng.normal(size=153)+1j*rng.normal(size=153); x/=np.linalg.norm(x)
    env=rng.normal(size=2)+1j*rng.normal(size=2); env*=.1/np.linalg.norm(env)
    q,w=x[:16],x[16:]
    qa,wa,_=apply(B,q,w,env,v,i)
    qi,wi,_=apply(ideal,q,w,np.zeros(2),u,i)
    actual=np.linalg.norm(np.r_[qa-qi,wa-wi])
    bound=certificate_retained*np.linalg.norm(x)+certificate_environment*np.linalg.norm(env)
    assert actual<=bound+tol
    max_error=max(max_error,float(actual))
# Intensity-only calibration cannot certify swap signs/phases.
phase_flip=np.diag([-1,1,1,1])@ideal
assert np.max(np.abs(np.abs(phase_flip)**2-np.abs(ideal)**2))<tol
assert np.linalg.norm(phase_flip[np.ix_(rows,cols)]-swap,2)>1
# Frozen prior cavity must be rejected at the SAME predeclared tolerance.
frozen_T=prior['frozen'][np.ix_(rows,cols)]
assert np.linalg.norm(frozen_T-swap,2)>acceptance_limit
# A common endpoint frame rotates u,v together without changing routing error.
phase=np.exp(1j*np.arange(16)/7)
assert abs(np.linalg.norm(phase*v-phase*u)-np.linalg.norm(v-u))<tol

result={
 'status':'passed','classification':'conditional_independent_port_calibration_exchange_error_certificate',
 'tolerance':tol,
 'calibration_evidence':'synthetic four-port coherent-probe data; not laboratory measurements',
 'certificate':{'retained_operator_error_bound':certificate_retained,
                'environment_feedthrough_bound':certificate_environment,
                'router_vector_error_bound':router_radius,'complex_entry_error_radius':entry_radius,
                'predeclared_retained_acceptance_limit':acceptance_limit,
                'analytic_retained_error_bound_without_router':float(analytic_retained)},
 'held_out_validation':{'independent_seed':27137,'states':40,'maximum_observed_error':max_error},
 'checks':{'analytic_loss_phase_mirror_bound':True,'vacuum_injection_required':True,
           'independent_calibration_error_certificate':True,'held_out_state_bound':True,
           'intensity_only_phase_hostile':True,'frozen_cavity_rejected':True,
           'endpoint_frame_routing_bound_invariant':True},
 'conclusion':'Independent complex port tomography plus a separately bounded router error can certify approximate exchange without fitting its validation outputs. The current certificate is synthetic; it requires measured error bounds, environment control and phase-referenced calibration before physical use.',
 'next_falsifier':'Implement the time-dependent endpoint-frame connection and test that calibration/phase-frame transport remains valid during a delayed multi-event experiment.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
