"""Finite-amplitude checks in a normalized projective chart.
Run: uv run --with numpy --with scipy python THIS_FILE
"""
from pathlib import Path
import hashlib
import json
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import null_space, expm
from scipy.optimize import brentq

BASE=Path(__file__).resolve().parents[1]


def main():
    raw=(BASE/'results/spinor_tangent_dynamics.json').read_bytes()
    prior=json.loads(raw)
    assert prior['verification_passed']
    beta,c=0.6,0.06
    r=brentq(lambda x:3*x**4+6*c*x**3-2*c*x-3,0.9,1,xtol=1e-15)
    q=1j*np.array([[0,1,1,1],[-1,0,1,-1],[-1,-1,0,1],[-1,1,-1,0]])/np.sqrt(3)
    k=np.eye(4)-q
    p=(r*np.eye(4)+q)[:,0]/np.sqrt(1+r*r)
    ell=-(abs(p)**2+1)/5
    s=np.vstack((np.eye(3),-np.ones((1,3))))
    u=null_space(p.conj()[None,:]);t=np.hstack((u,1j*u))/np.sqrt(2)
    mu=np.vdot(p,k@p+beta*(abs(p)**2+ell)*p/4).real
    a=k+np.diag(beta*(2*abs(p)**2+ell)/4)-mu*np.eye(4)
    d=np.diag(beta*p*p/4)
    h=2*(t.conj().T@a@t+t.conj().T@d@t.conj()).real
    m=2*(t.conj().T@(beta*p[:,None]*s/4)).real
    l=5*beta*s.T@s/4
    j=np.block([[np.zeros((3,3)),np.eye(3)],[-np.eye(3),np.zeros((3,3))]])
    linear=np.zeros((12,12));linear[:6,:6]=j@h;linear[:6,9:]=j@m
    linear[6:9,:6]=m.T;linear[6:9,9:]=l
    eig,vec=np.linalg.eig(j@h)
    index=min((i for i in range(6) if eig[i].imag>1e-8),key=lambda i:eig[i].imag)
    omega=eig[index].imag
    assert abs(omega-prior['rays'][0]['matter_frequencies'][0])<1e-12
    slow=vec[:,index].real;slow/=np.linalg.norm(slow)
    momentum=np.array([1.,-0.4,0.2]);momentum/=np.linalg.norm(momentum)
    center=-np.linalg.solve(h,m@momentum)
    directions={'slow_mode':np.r_[slow,np.zeros(6)],
                'lead_drift':np.r_[center,np.zeros(3),momentum]}
    def state(coords):
        z=(coords[:3]+1j*coords[3:6])/np.sqrt(2)
        psi=p+u@z
        return psi/np.linalg.norm(psi)
    def rhs(time,coords):
        psi=state(coords);flux=ell+s@coords[9:]
        dr=-1j*(k@psi+beta*(abs(psi)**2+flux)*psi/4)
        overlap=np.vdot(p,psi)
        zdot=(u.conj().T@dr-(u.conj().T@psi)*np.vdot(p,dr)/overlap)/overlap
        angles=s.T@(beta*flux+beta*(abs(psi)**2+flux)/4)
        return np.r_[np.sqrt(2)*zdot.real,np.sqrt(2)*zdot.imag,angles,np.zeros(3)]
    def energy(coords):
        psi=state(coords);flux=ell+s@coords[9:]
        return float(np.vdot(psi,k@psi).real+beta*np.dot(flux,flux)/2
                     +beta*np.sum((abs(psi)**2+flux)**2)/8+0.1)
    results={}
    for name,direction in directions.items():
        duration=2*np.pi/omega if name=='slow_mode' else 100.
        times=np.linspace(0,duration,201)
        # Reused matrix exponential predictions are independent of amplitude.
        prediction=np.array([expm(linear*time)@direction for time in times])
        runs=[]
        for amplitude in (0.002,0.001):
            initial=amplitude*direction
            sol=solve_ivp(rhs,(0,duration),initial,t_eval=times,method='DOP853',rtol=2e-11,atol=2e-13)
            assert sol.success
            errors=np.linalg.norm(sol.y.T-amplitude*prediction,axis=1)
            e0=energy(initial)
            energy_error=max(abs(energy(v)-e0) for v in sol.y.T)
            chart_overlap=min(abs(np.vdot(p,state(v))) for v in sol.y.T)
            assert energy_error<1e-10 and chart_overlap>0.99
            assert np.max(abs(sol.y[9:]-initial[9:,None]))<1e-15
            runs.append({'amplitude':amplitude,'duration':float(duration),
                         'maximum_tangent_error':float(max(errors)),
                         'maximum_energy_error':energy_error,'minimum_chart_overlap':float(chart_overlap),
                         'final_angle_displacement':sol.y[6:9,-1].tolist(),
                         'predicted_final_angle_displacement':(amplitude*prediction[-1,6:9]).tolist()})
        refined=solve_ivp(rhs,(0,duration),initial,t_eval=times,method='DOP853',rtol=2e-12,atol=2e-14)
        assert refined.success
        refinement_error=float(np.max(np.linalg.norm(refined.y.T-sol.y.T,axis=1)))
        assert refinement_error<1e-8
        ratio=runs[0]['maximum_tangent_error']/runs[1]['maximum_tangent_error']
        assert 3.7<ratio<4.3
        results[name]={'runs':runs,'error_halving_ratio':ratio,'tighter_tolerance_discrepancy':refinement_error}
    report={'verification_passed':True,'tangent_result_sha256':hashlib.sha256(raw).hexdigest(),
            'scope':'Numerical finite-amplitude validation at address zero; source symmetry relates the other ground sectors. No quantization or transition coupling added.',
            'slow_period':float(2*np.pi/omega),'fixtures':results,
            'interpretation':'Nonlinear deviation scales quadratically with amplitude; conserved momenta remain fixed and drive the predicted cyclic-angle drift.',
            'next_gate':'Consolidate the classical state/observable contract and validate the full checker chain; any inter-sector transition or quantization requires explicit additional input.'}
    (BASE/'results/spinor_finite_dynamics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
