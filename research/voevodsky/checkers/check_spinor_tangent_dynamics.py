"""Numerical tangent Hamiltonian audit; not an exact spectral certificate.
Run: uv run --with numpy --with scipy python THIS_FILE
"""
from pathlib import Path
import hashlib
import json
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import brentq

BASE=Path(__file__).resolve().parents[1]


def main():
    raw=(BASE/'results/spinor_constrained_leads.json').read_bytes()
    assert json.loads(raw)['verification_passed']
    beta,c=0.6,0.06
    r=brentq(lambda x:3*x**4+6*c*x**3-2*c*x-3,0.9,1,xtol=1e-15)
    q=1j*np.array([[0,1,1,1],[-1,0,1,-1],[-1,-1,0,1],[-1,1,-1,0]])/np.sqrt(3)
    k=np.eye(4)-q
    orbit=(r*np.eye(4)+q)/np.sqrt(1+r*r)
    s=np.vstack((np.eye(3),-np.ones((1,3))))
    j=np.block([[np.zeros((3,3)),np.eye(3)],[-np.eye(3),np.zeros((3,3))]])
    results=[]
    for address in range(4):
        p=orbit[:,address];rho=abs(p)**2;ell=-(rho+1)/5
        u=null_space(p.conj()[None,:])
        t=np.hstack((u,1j*u))/np.sqrt(2)
        mu=np.vdot(p,k@p+beta*(rho+ell)*p/4).real
        a=k+np.diag(beta*(2*rho+ell)/4)-mu*np.eye(4)
        d=np.diag(beta*p*p/4)
        h=2*(t.conj().T@a@t+t.conj().T@d@t.conj()).real
        cross=2*(t.conj().T@(beta*p[:,None]*s/4)).real
        lead=5*beta*s.T@s/4
        assert np.max(abs(h-h.T))<1e-13
        assert np.linalg.eigvalsh(h).min()>1e-4
        schur=lead-cross.T@np.linalg.solve(h,cross)
        assert np.linalg.eigvalsh(schur).min()>1e-4
        # Ordering: six matter coordinates, three angles, three momenta.
        full_h=np.zeros((12,12));full_h[:6,:6]=h
        full_h[:6,9:]=cross;full_h[9:,:6]=cross.T;full_h[9:,9:]=lead
        full_j=np.zeros((12,12));full_j[:6,:6]=j
        full_j[6:9,9:]=np.eye(3);full_j[9:,6:9]=-np.eye(3)
        linear=full_j@full_h
        ev=np.linalg.eigvals(j@h)
        assert max(abs(ev.real))<1e-12
        frequencies=sorted(float(x.imag) for x in ev if x.imag>1e-8)
        assert len(frequencies)==3
        assert np.linalg.matrix_rank(linear,tol=1e-10)==9
        assert np.linalg.matrix_rank(linear@linear,tol=1e-10)==6
        # Tangent shifts relax matter; the remaining angle drift is the
        # Schur-complement response to a constant momentum perturbation.
        for i in range(3):
            momentum=np.eye(3)[:,i]
            v=np.r_[-np.linalg.solve(h,cross@momentum),np.zeros(3),momentum]
            assert np.max(abs(linear@v-np.r_[np.zeros(6),schur@momentum,np.zeros(3)]))<1e-13
        # Independent finite-difference Jacobian in a normalized projective
        # chart removes both norm and overall phase, not just one zero mode.
        def rhs(coords):
            z=(coords[:3]+1j*coords[3:6])/np.sqrt(2)
            state=p+u@z;state/=np.linalg.norm(state)
            flux=ell+s@coords[9:]
            dr=-1j*(k@state+beta*(abs(state)**2+flux)*state/4)
            overlap=np.vdot(p,state)
            zdot=(u.conj().T@dr-(u.conj().T@state)*np.vdot(p,dr)/overlap)/overlap
            angle=s.T@(beta*flux+beta*(abs(state)**2+flux)/4)
            return np.r_[np.sqrt(2)*zdot.real,np.sqrt(2)*zdot.imag,angle,np.zeros(3)]
        eps=1e-5
        fd=np.column_stack([(rhs(eps*e)-rhs(-eps*e))/(2*eps) for e in np.eye(12)])
        error=float(np.max(abs(fd-linear)))
        assert error<2e-9
        results.append({'address':address,'matter_hessian_eigenvalues':np.linalg.eigvalsh(h).tolist(),
                        'matter_frequencies':frequencies,'lead_schur_eigenvalues':np.linalg.eigvalsh(schur).tolist(),
                        'jacobian_finite_difference_error':error})
    for row in results[1:]:
        assert np.allclose(row['matter_frequencies'],results[0]['matter_frequencies'],atol=1e-12,rtol=0)
    report={'verification_passed':True,'constrained_result_sha256':hashlib.sha256(raw).hexdigest(),
            'scope':'Double-precision tangent spectrum at the frozen hard-flux fixture; numerical evidence, not exact eigenvalue bounds.',
            'canonical_chart':'delta psi=U*(x+i*y)/sqrt(2), U^dagger U=I, U^dagger psi0=0',
            'tangent_hamiltonian':'(v^T H v)/2+v^T M dell+(dell^T L dell)/2; independent of lead angles',
            'full_linearization':'vdot=J(Hv+M dell), angle_dot=M^T v+L dell, dell_dot=0',
            'rays':results,'zero_eigenvalue_algebraic_multiplicity':6,'zero_eigenvalue_geometric_multiplicity':3,
            'zero_structure':'Three length-two Jordan chains: conserved momentum shifts drive secular cyclic-angle motion.',
            'stability':'Positive matter Hessian in each fixed-lead sector; three oscillatory mode pairs. Full system is neutral along the ground torus, with angle drift for nearby conserved momenta.',
            'next_gate':'Check finite-amplitude trajectories against tangent predictions and define which observables descend to a sector or require lifted lead/phase histories; no inter-sector hopping is generated.'}
    (BASE/'results/spinor_tangent_dynamics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
