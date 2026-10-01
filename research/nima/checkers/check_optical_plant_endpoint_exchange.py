# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Prior cavity dilation + endpoint-phase adapter; conditional exchange gate."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import numpy as np

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/optical-plant-endpoint-exchange.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    runpy.run_path(str(ROOT/'research/aspect/checkers/reciprocal_lossy_cavity_plant.py'),run_name='__main__')
    prior=runpy.run_path(str(HERE/'check_137_local_phase_covariance.py'))
tol=1e-10

def plant(r1,t1,r2,t2,a,ell,p=1,q=1):
    if a<0 or ell<0 or any(abs(x)>tol for x in (r1*r1+t1*t1-1,r2*r2+t2*t2-1,a*a+ell*ell-1,abs(p)-1,abs(q)-1)):
        raise ValueError('uncalibrated normalization')
    m1=np.array([[-r1,t1,0,0],[t1,r1,0,0],[0,0,1,0],[0,0,0,1]],complex)
    m2=np.array([[1,0,0,0],[0,t2,-r2,0],[0,r2,t2,0],[0,0,0,1]],complex)
    loss=np.array([[1,0,0,0],[0,1,0,0],[0,0,a,ell],[0,0,-ell,a]],complex)
    # Physical order matters: return phase acts on b BEFORE loss mixing,
    # hence it occurs in BOTH x_next and y_environment amplitudes.
    return loss@np.diag([1,1,q,1])@m2@np.diag([1,p,1,1])@m1

frozen=plant(.6,.8,.8,.6,.6,.8)
retained=frozen[np.ix_([0,2],[0,1])]
swap=np.array([[0,1],[1,0]])
assert np.max(np.abs(frozen.conj().T@frozen-np.eye(4)))<tol
singular=np.linalg.svd(retained,compute_uv=False)
assert np.max(np.abs(singular-[1,.48]))<tol
assert np.linalg.norm(retained-swap)>.1
# Predeclared ideal boundary settings; phases specified before test inputs.
p=np.exp(.37j); q=np.exp(-.37j)
ideal=plant(0,1,1,0,1,0,p,q)
assert np.max(np.abs(ideal[np.ix_([0,2],[0,1])]-swap))<tol
assert np.max(np.abs(ideal[np.ix_([0,2],[2,3])]))<tol
# Directly extending the prose's y_e=-ell*b+a*w without return phase is NOT unitary.
a=.6; ell=.8; phase=1j
bad=np.array([[a*phase,ell],[-ell,a]],complex)
good=np.array([[a*phase,ell],[-ell*phase,a]],complex)
assert np.linalg.norm(bad.conj().T@bad-np.eye(2))>.1
assert np.max(np.abs(good.conj().T@good-np.eye(2)))<tol
complex_plant=plant(.6,.8,.8,.6,.6,.8,np.exp(.31j),np.exp(-.52j))
assert np.max(np.abs(complex_plant.conj().T@complex_plant-np.eye(4)))<tol

K=prior['K']; features=prior['features']
evals,evecs=np.linalg.eigh(K)
C=(evecs*np.sqrt(evals))@evecs.conj().T
U=np.array([C@v/np.sqrt(np.vdot(v,K@v).real) for v in features])
rng=np.random.default_rng(7137)
carrier=rng.normal(size=16)+1j*rng.normal(size=16)
records=rng.normal(size=137)+1j*rng.normal(size=137)
env=rng.normal(size=2)+1j*rng.normal(size=2)

def apply(B,carrier,records,env,u,i):
    s=np.vdot(u,carrier)
    ports=B@np.r_[records[i],s,env]
    newq=carrier+u*(ports[2]-s)
    neww=records.copy(); neww[i]=ports[0]
    return newq,neww,ports[[1,3]]

def energy(q,w,e): return np.vdot(q,q).real+np.vdot(w,w).real+np.vdot(e,e).real

for trial in range(3):
    ca=rng.uniform(-np.pi,np.pi,4); cb=rng.uniform(-np.pi,np.pi,4)
    phase=np.exp(1j*(cb[None,:]-ca[:,None])).reshape(16)
    Knew=phase[:,None]*K*phase.conj()[None,:]
    Cnew=phase[:,None]*C*phase.conj()[None,:]
    assert np.max(np.abs(Cnew@Cnew-Knew))<tol
    for i,v in enumerate(features):
        unew=Cnew@(phase*v)/np.sqrt(np.vdot(phase*v,Knew@(phase*v)).real)
        assert np.max(np.abs(unew-phase*U[i]))<tol
        for B in (ideal,complex_plant):
            q1,w1,e1=apply(B,carrier,records,env,U[i],i)
            q2,w2,e2=apply(B,phase*carrier,records,env,unew,i)
            assert np.max(np.abs(q2-phase*q1))<tol
            assert np.max(np.abs(w2-w1))<tol and np.max(np.abs(e2-e1))<tol
            assert abs(energy(q1,w1,e1)-energy(carrier,records,env))<tol
        # Ideal retained outputs agree with the old normalized exchange exactly.
        q1,w1,_=apply(ideal,carrier,records,env,U[i],i)
        delta=records[i]-np.vdot(U[i],carrier)
        expected=records.copy(); expected[i]-=delta
        assert np.max(np.abs(q1-carrier-U[i]*delta))<tol
        assert np.max(np.abs(w1-expected))<tol
        assert np.max(np.abs(q1+U.T@w1-(carrier+U.T@records)))<tol
    # Changing the frame but not the addressed supermode is a different operation.
    i=121
    wrong=apply(ideal,phase*carrier,records,env,U[i],i)
    right=apply(ideal,phase*carrier,records,env,phase*U[i],i)
    assert np.linalg.norm(wrong[0]-right[0])>1e-4

result={
 'status':'passed','classification':'conditional_optical_exchange_boundary_with_endpoint_phase_covariance',
 'tolerance':tol,
 'checks':{'prior_optical_and_phase_checks_rerun':True,'frozen_cavity_not_exchange':True,
           'phase_order_environment_hostile':True,'complete_complex_dilation_unitary':True,
           'all137_ideal_exchange_embeddings':True,'three_endpoint_frames_both_plants':True,
           'untransported_supermode_rejected':True},
 'frozen_retained_singular_values':singular.tolist(),
 'ideal_controls':{'r1':0,'t1':1,'r2':1,'t2':0,'a':1,'ell':0,'forward_phase_radians':.37,'return_phase_radians':-.37},
 'conclusion':'The frozen lossy cavity is not exchange. Its lossless fully transmitting-input/perfectly reflecting-end boundary realizes the exchange on an addressed normalized carrier supermode, provided all record/unused ports and endpoint-dependent mode controls are retained.',
 'calibration_status':'Settings are predeclared theoretical controls, not measured calibrations. Mode routing, storage, delay, common energy normalization and independent phase monitoring remain apparatus obligations.',
 'next_falsifier':'Derive tolerances and an independent port-calibration protocol for deviations from this ideal boundary, including mode-routing error, nonzero loss and round-trip phase drift.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
