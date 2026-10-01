# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Conditional passive oscillator realization of the existing complex pulse."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import numpy as np

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/exchange-oscillator-instrument.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    old=runpy.run_path(str(Path(__file__).with_name('check_137_closed_record_stationarity.py')))
U=old['U']; n=153; tol=1e-10
D=np.vstack((U.T,-np.eye(137)))/np.sqrt(2)
W=np.vstack((np.eye(16),U))
I=np.eye(n)
J=np.block([[np.zeros((n,n)),I],[-I,np.zeros((n,n))]])

def pulse(i,theta):
    return I+(np.exp(-1j*theta)-1)*np.outer(D[:,i],D[:,i])

def quadrature(S):
    return np.block([[S.real,-S.imag],[S.imag,S.real]])

for i in range(137):
    H=I-2*np.outer(D[:,i],D[:,i])
    assert np.max(np.abs(pulse(i,np.pi)-H))<tol
    # Every pulse fixes matched amplitude vectors, including between endpoints.
    # Equal means alone do not imply a general quantum state is unchanged.
    assert np.max(np.abs(D[:,i]@W))<tol

for i in (0,121,136):
    for theta in (np.pi/3,np.pi,2*np.pi):
        S=pulse(i,theta); T=quadrature(S)
        assert np.max(np.abs(S.conj().T@S-I))<tol
        assert np.max(np.abs(T@J@T.T-J))<tol
        assert np.max(np.abs(T@T.T-np.eye(2*n)))<tol
        assert np.max(np.abs(W.T@S-W.T))<tol
        # Coherent-state quadrature covariance V=I/2 is unchanged.
        assert np.max(np.abs(T@(np.eye(2*n)/2)@T.T-np.eye(2*n)/2))<tol

amp=2.; i=121
alpha=np.zeros(n,dtype=complex); alpha[16+i]=amp
one=pulse(i,np.pi)@alpha
assert np.max(np.abs(one[:16]-amp*U[i]))<tol
assert abs(one[16+i])<tol
two=pulse(i,np.pi)@one
assert np.max(np.abs(two-alpha))<tol
# Competing quarter-turn agrees on first pulse but gives opposite signed echo.
def rotation(z):
    s=U[i]@z[:16]; r=z[16+i]
    z=z.copy(); z[:16]+=U[i]*(r-s); z[16+i]=-s
    return z
assert np.max(np.abs(rotation(alpha)-one))<tol
other=rotation(rotation(alpha))
assert abs(other[16+i]+amp)<tol
assert abs(np.vdot(other,other).real-np.vdot(alpha,alpha).real)<tol
# [X,P]=i, X=(a+a^dagger)/sqrt(2): coherent mean and vacuum variance.
echo_mean=np.sqrt(2)*two[16+i].real
other_mean=np.sqrt(2)*other[16+i].real
vacuum_variance=.5
assert abs(echo_mean+other_mean)<tol
# Detuning/control calibration: theta=int kappa dt. Endpoint alone does not fix time.
for duration in (1.,3.,7.):
    kappa=np.pi/duration
    assert np.max(np.abs(pulse(i,kappa*duration)-pulse(i,np.pi)))<tol
# Two equal imperfect pulses: record amplitude=A(1+exp(-2i theta))/2.
for error in (-.2,.1):
    theta=np.pi+error
    imperfect=pulse(i,theta)@pulse(i,theta)@alpha
    predicted=amp*(1+np.exp(-2j*theta))/2
    assert abs(imperfect[16+i]-predicted)<tol
    assert abs(imperfect[16+i].real/amp-np.cos(error)**2)<tol
# Even vacuum supplies identical mismatch variances, without an excitation budget.
L=np.hstack((-U,np.eye(137)))
vac_mismatch=.5*np.sum(L*L,axis=1)
assert np.max(np.abs(vac_mismatch-1))<tol
assert np.max(np.abs(vac_mismatch/vac_mismatch.sum()-1/137))<tol
assert np.max(np.abs(vac_mismatch-1))<tol  # vacuum-subtracted variances vanish

result={
 'status':'passed',
 'classification':'conditional_passive_oscillator_exchange_and_homodyne_contract',
 'tolerance':tol,
 'checks':{'all137_pulse_endpoints':True,'canonical_quadrature_transport':True,
           'matched_amplitude_nondisturbance_during_pulse':True,'coherent_covariance_retained':True,
           'signed_echo_discriminator':True,'pulse_area_calibration_freedom':True,
           'pulse_area_error_response':True,'vacuum_share_not_coupling':True},
 'coherent_echo':{'prepared_amplitude':amp,'exchange_X_mean':float(echo_mean),
                  'quarter_turn_X_mean':float(other_mean),'X_variance':vacuum_variance},
 'conclusion':'The prior complex pulse has a passive bosonic-mode realization with coherent preparation and quadrature readout, conditional on supplied mode addressing, phase reference and Hamiltonian control. Vacuum alone has equal1/137 normalized mismatch variance; that fraction is not an interaction strength.',
 'missing':['native_rung_to_mode_map','physical_mode_and_control_selection',
            'preparation_and_detector_resource_model','absolute_current_field_normalization'],
 'next_falsifier':'Find a source-authorized mode/control realization and test its signed echo, pulse-area error curve and calibrated vacuum subtraction.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
