"""Numerical checks of the electrostatic Hamiltonian in ground-orbit coordinates.
Run: uv run --with numpy --with scipy python THIS_FILE
Not a quantization or a dynamical elimination of the full gauge field.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
from scipy.optimize import brentq

BASE = Path(__file__).resolve().parents[1]


def main():
    source = BASE / 'results/spinor_ground_orbit.json'
    raw = source.read_bytes()
    previous = json.loads(raw)
    assert previous['verification_passed'] and previous['ground_state_rays'] == 4
    c, eta = 0.06, 0.2
    r = brentq(lambda x: 3*x**4+6*c*x**3-2*c*x-3, 0.9, 1, xtol=1e-15)
    q = 1j*np.array([[0,1,1,1],[-1,0,1,-1],[-1,-1,0,1],[-1,1,-1,0]])/np.sqrt(3)
    k = np.eye(4)-q
    b = (r*np.eye(4)+q)/np.sqrt(1+r*r)
    g = b.conj().T@b
    assert np.allclose(g, np.eye(4)+2*r*q/(1+r*r))
    assert np.linalg.eigvalsh(g).min() > 0
    def energy(p):
        return float(np.vdot(p,k@p).real+c*(1+np.sum(abs(p)**4))+eta/2)
    def gradient(p):
        return k@p+2*c*abs(p)**2*p
    def velocity(a):
        return -1j*np.linalg.solve(g,b.conj().T@gradient(b@a))
    stationary = []
    for i in range(4):
        p = b[:,i]
        mu = np.vdot(p,gradient(p)).real
        stationary.append(float(np.linalg.norm(gradient(p)-mu*p)))
        assert stationary[-1] < 1e-12
        assert abs(energy(p)-previous['global_minimum_interval_decimal'][0]) < 1e-13
    rng = np.random.default_rng(731)
    residuals = []
    for _ in range(20):
        p = rng.normal(size=4)+1j*rng.normal(size=4)
        p /= np.linalg.norm(p)
        a = np.linalg.solve(b,p)
        da = velocity(a)
        residuals.append(float(np.linalg.norm(b@da+1j*gradient(p))))
        assert abs(2*np.vdot(a,g@da).real) < 1e-10
        assert abs(2*np.vdot(gradient(p),b@da).real) < 1e-10
    assert max(residuals) < 1e-10
    # Exact kinetic and onsite subflows; symmetric Strang composition.
    def step(p,h):
        p = np.exp(-1j*c*h*abs(p)**2)*p
        p = np.exp(-1j*h)*(np.cos(h)*p+1j*np.sin(h)*(q@p))
        return np.exp(-1j*c*h*abs(p)**2)*p
    p0 = b[:,0]+0.17j*b[:,1]+0.08*b[:,2]
    p0 /= np.linalg.norm(p0)
    runs = []
    for h in (0.02,0.01):
        p = p0.copy()
        error = 0.0
        count = round(2/h)
        for _ in range(count):
            p = step(p,h)
            error = max(error,abs(energy(p)-energy(p0)))
        norm_error = abs(np.vdot(p,p).real-1)
        for _ in range(count):
            p = step(p,-h)
        reversal = np.linalg.norm(p-p0)
        assert norm_error < 1e-12 and reversal < 1e-12
        runs.append({'dt':h,'maximum_energy_error':error,'norm_error':float(norm_error),'reversal_error':float(reversal)})
    assert 3.8 < runs[0]['maximum_energy_error']/runs[1]['maximum_energy_error'] < 4.2
    superposition = b[:,0]+b[:,1]
    superposition /= np.linalg.norm(superposition)
    assert energy(superposition) > energy(b[:,0])+1e-6
    report = {
        'verification_passed':True,
        'ground_orbit_result_sha256':hashlib.sha256(raw).hexdigest(),
        'scope':'Numerical verification of a classical electrostatic reduced Hamiltonian; no full gauge-field reduction or quantization claimed.',
        'state_space':'a in C^4, a^dagger G a=1; ray quotient CP^3; retain U(1) lifts for phase histories',
        'basis':'B=(r I+Q)/sqrt(1+r^2), psi=B a',
        'gram':'G=I+2r Q/(1+r^2)',
        'gram_eigenvalues':np.linalg.eigvalsh(g).tolist(),
        'gram_condition_number':float(np.linalg.cond(g)),
        'hamiltonian':'a^dagger B^dagger K B a+c sum_i |(B a)_i|^4+c+eta/2',
        'equation':'i G adot=B^dagger[K B a+2c diag(|B a|^2) B a]',
        'stationary_ray_residuals':stationary,
        'maximum_coordinate_dynamics_residual':max(residuals),
        'equal_two_ray_superposition_energy':energy(superposition),
        'ground_energy':energy(b[:,0]),
        'numerical_feedback':runs,
        'orbit_only_dynamics':'Each ground ray is fixed projectively; its lift evolves by a common chemical-potential phase. No autonomous inter-ray hopping is derived.',
        'next_gate':'Derive constrained symplectic reduction with longitudinal electric variables, or explicitly adopt the electrostatic approximation; then compute tangent stability and distinguish quantization from classical superposition.'
    }
    (BASE/'results/spinor_orbit_dynamics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
