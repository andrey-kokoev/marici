# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Conditional coherent homodyne detector moments; no experimental data."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from math import cos, exp, sqrt, pi
from pathlib import Path
import io
import json
import runpy
import numpy as np
from labelled_exchange_experiment import Experiment

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/exchange-detector-calibration.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    native=runpy.run_path(str(HERE/'check_shared_leg_dg_realization.py'))
_,boundary,_,_,routes=native['build']({'a':(0,0),'s':(0,0)})
ex=Experiment()
def event(i,j):
    k=11*i+j
    return ex.compile(ex.labels[k],routes('a',i,j)[0],boundary,'native-DG-roots00')

# Detector assumptions: coherent state, real displacement, independent Gaussian
# LO phase on each trial, constant gain/loss, independent electronics noise.
def moments(m,g,eta,b,ve,phase=0.,spread=0.):
    if g<=0 or not 0<=eta<=1 or ve<0 or spread<0: raise ValueError('detector parameters')
    c=exp(-spread**2/2)*cos(phase)
    c2=(1+exp(-2*spread**2)*cos(2*phase))/2
    return b+g*sqrt(eta)*m*c, g*g*(.5+eta*m*m*(c2-c*c))+ve

def observed(packet,port,**detector):
    if np.max(np.abs(packet.covariance-np.eye(153)/2))>1e-10:
        raise ValueError('this endpoint readout requires coherent covariance and supplied vacuum P quadratures')
    return moments(ex.state(packet)[16+port],**detector)

amp=2.; w=np.zeros(137); w[11]=sqrt(2)*amp
prepared=ex.prepare(np.zeros(16),w,np.eye(153)/2,'declared-coherent-preparation-X')
echo=ex.run(prepared,[event(1,0),event(1,0)])
rectangle=ex.run(prepared,[event(1,0),event(0,0),event(0,1),event(1,1)])
detector=dict(g=3.,eta=.64,b=.2,ve=.09,phase=.15,spread=.2)
ref=observed(prepared,11,**detector)
echo_obs=observed(echo,11,**detector)
rect_obs=observed(rectangle,11,**detector)
other= moments(-sqrt(2)*amp,**detector)
b=detector['b']; tol=1e-10
assert abs((echo_obs[0]-b)/(ref[0]-b)-1)<tol
assert abs((other[0]-b)/(ref[0]-b)+1)<tol
assert abs((rect_obs[0]-b)/(ref[0]-b))<tol
assert abs(echo_obs[1]-other[1])<tol
# Calibration recovery from ideal population moments, not noisy estimated data.
dark_mean=b; dark_variance=detector['ve']
vac= moments(0,**detector)
g=sqrt(2*(vac[1]-dark_variance))
c=exp(-detector['spread']**2/2)*cos(detector['phase'])
eta=((ref[0]-dark_mean)/(g*sqrt(2)*amp*c))**2
assert abs(g-detector['g'])<tol and abs(eta-detector['eta'])<tol
# Without independently known amplitude, loss and amplitude are not identifiable.
a=moments(sqrt(2),g=3,eta=.64,b=.2,ve=.09,phase=.15,spread=.2)
z=moments(2*sqrt(2),g=3,eta=.16,b=.2,ve=.09,phase=.15,spread=.2)
assert np.max(np.abs(np.array(a)-z))<tol
# A pi phase jump of the echo LO mimics the competing operation, even in variance.
shifted=dict(detector); shifted['phase']+=pi
fake=observed(echo,11,**shifted)
assert np.max(np.abs(np.array(fake)-other))<tol
# Blind controls: complete loss or phase quadrature at pi/2 removes signed means.
blind=dict(detector); blind['eta']=0
assert abs(moments(sqrt(2)*amp,**blind)[0]-moments(-sqrt(2)*amp,**blind)[0])<tol
blind=dict(detector); blind['phase']=pi/2
assert abs(moments(sqrt(2)*amp,**blind)[0]-moments(-sqrt(2)*amp,**blind)[0])<tol
# Noncoherent supplied covariance is not silently treated as vacuum noise.
noncoherent=ex.prepare(np.zeros(16),w,np.eye(153),'noncoherent-control')
try: observed(noncoherent,11,**detector)
except ValueError: pass
else: raise AssertionError('unsupported covariance accepted')

result={
 'status':'passed','classification':'conditional_detector_calibration_with_phase_and_loss_identifiability_hostiles',
 'tolerance':tol,
 'checks':{'native_compiled_echo_and_rectangle':True,'loss_gain_noise_phase_moments':True,
           'independent_calibration_population_recovery':True,'unknown_amplitude_loss_degeneracy':True,
           'phase_jump_mimics_opposite_echo':True,'blind_detector_controls':True,
           'unsupported_covariance_rejected':True},
 'predicted_detector_moments':{'reference':ref,'exchange_echo':echo_obs,'quarter_turn_echo':other,'rectangle':rect_obs},
 'conclusion':'The conditional compiled experiment gives calibrated detector moments and signed ratios, but needs a stable phase reference and independently known preparation amplitude to separate loss from source strength. Neither requirement is supplied by1/137.',
 'next_falsifier':'Integrate these assumptions and gates into one end-to-end claim ledger, separating checked source-labelled experiments from the still-unproved native selection and absolute physical coupling.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
