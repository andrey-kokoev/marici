"""Hard internal flux reduction with conserved exterior lead electric fields.
Run: uv run --with numpy --with scipy python THIS_FILE
Exact incidence checks plus separately labelled numerical dynamical checks.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
from scipy.optimize import brentq

BASE = Path(__file__).resolve().parents[1]


def main():
    raw = (BASE/'results/spinor_ground_orbit.json').read_bytes()
    old = json.loads(raw)
    assert old['verification_passed']
    edges = [(i,j) for i in range(4) for j in range(i+1,4)]
    b = np.zeros((4,6),dtype=int)
    for e,(i,j) in enumerate(edges):
        b[i,e],b[j,e] = -1,1
    faces = np.array([[0,0,0,1,-1,1],[0,-1,1,0,0,-1],
                      [1,0,-1,0,1,0],[-1,1,0,-1,0,0]])
    assert np.array_equal(b@faces.T,np.zeros((4,4),dtype=int))
    assert np.array_equal(b@b.T,4*np.eye(4,dtype=int)-np.ones((4,4),dtype=int))
    assert np.array_equal(b.T@b+faces.T@faces,4*np.eye(6,dtype=int))
    beta,eta,c = 0.6,0.2,0.06
    r = brentq(lambda x:3*x**4+6*c*x**3-2*c*x-3,0.9,1,xtol=1e-15)
    q = 1j*np.array([[0,1,1,1],[-1,0,1,-1],[-1,-1,0,1],[-1,1,-1,0]])/np.sqrt(3)
    k = np.eye(4)-q
    orbit = (r*np.eye(4)+q)/np.sqrt(1+r*r)
    def density(p):return abs(p)**2
    def optimum_leads(p):return -(density(p)+1)/5
    def field(p,leads):return b.T@(-density(p)-leads)/4
    def energy(p,leads):
        return float(np.vdot(p,k@p).real+beta*np.sum(leads**2)/2
                     +beta*np.sum((density(p)+leads)**2)/8+eta/2)
    def grad(p,leads):return k@p+beta*(density(p)+leads)*p/4
    def rhs(p,leads):return -1j*grad(p,leads)
    leads = optimum_leads(orbit[:,0])
    stationary=[]
    sector_energies=[]
    for i in range(4):
        p=orbit[:,i]
        own=optimum_leads(p)
        mu=np.vdot(p,grad(p,own)).real
        stationary.append(float(np.linalg.norm(grad(p,own)-mu*p)))
        assert stationary[-1]<1e-12
        assert abs(energy(p,own)-old['global_minimum_interval_decimal'][0])<1e-13
        sector_energies.append(energy(p,leads))
    assert min(sector_energies[1:])>sector_energies[0]+1e-4
    rng=np.random.default_rng(191)
    for _ in range(20):
        p=rng.normal(size=4)+1j*rng.normal(size=4)
        p/=np.linalg.norm(p)
        e=field(p,leads)
        assert np.max(abs(b@e+leads+density(p)))<1e-14
        assert np.max(abs(faces@e))<1e-14
        assert abs(np.dot(e,e)-np.sum((density(p)+leads)**2)/4)<1e-14
        # Completing the square separates the static optimum and the
        # extra cost of a conserved, nonoptimal lead assignment.
        electrostatic=np.vdot(p,k@p).real+beta*(1+np.sum(density(p)**2))/10+eta/2
        assert abs(energy(p,leads)-electrostatic-5*beta*np.sum((leads-optimum_leads(p))**2)/8)<1e-13
        drho=2*(p.conj()*rhs(p,leads)).real
        # Internal current orientation follows rho_dot=-b J.
        j=np.array([2*np.imag(p[i].conjugate()*k[i,j]*p[j]) for i,j in edges])
        assert np.max(abs(drho+b@j))<1e-13
        # E_dot=J-C^T C J/4 for charge -1; leads_dot=0.
        assert np.max(abs(-b.T@drho/4-(j-faces.T@faces@j/4)))<1e-13
    p0=orbit[:,0]+0.17j*orbit[:,1]+0.08*orbit[:,2]
    p0/=np.linalg.norm(p0)
    moving_optimum_rate=np.linalg.norm(-2*(p0.conj()*rhs(p0,leads)).real/5)
    assert moving_optimum_rate>1e-6
    def step(p,h):
        p=np.exp(-1j*h*beta*(density(p)+leads)/8)*p
        p=np.exp(-1j*h)*(np.cos(h)*p+1j*np.sin(h)*(q@p))
        return np.exp(-1j*h*beta*(density(p)+leads)/8)*p
    runs=[]
    for h in (0.02,0.01):
        p=p0.copy();error=0.0
        for _ in range(round(2/h)):
            p=step(p,h)
            error=max(error,abs(energy(p,leads)-energy(p0,leads)))
        norm_error=abs(np.vdot(p,p).real-1)
        for _ in range(round(2/h)):p=step(p,-h)
        reversal=np.linalg.norm(p-p0)
        assert norm_error<1e-12 and reversal<1e-12
        runs.append({'dt':h,'energy_error':error,'norm_error':float(norm_error),'reversal_error':float(reversal)})
    assert 3.8<runs[0]['energy_error']/runs[1]['energy_error']<4.2
    report={
        'verification_passed':True,'ground_orbit_sha256':hashlib.sha256(raw).hexdigest(),
        'scope':'Hard constraints only on the internal source faces, no matter hopping on exterior leads, equal beta electric weights; fixed-norm negative charge.',
        'internal_cycle_rank':3,'total_electron_block_cycle_rank':6,'remaining_cyclic_coordinates':3,
        'lead_law':'ell_dot=0, sum ell=-1',
        'internal_field':'E_internal=B_internal^T*(-rho-ell)/4',
        'fixed_lead_hamiltonian':'<psi,K psi>+beta*||ell||^2/2+beta*||rho+ell||^2/8+eta/2',
        'matter_equation':'i psi_dot=K psi+(beta/4) diag(rho+ell) psi, modulo common phase',
        'static_elimination_gap':'H_ell-H_electrostatic=(5 beta/8)*||ell+(rho+1)/5||^2',
        'own_sector_stationarity_residuals':stationary,
        'four_orbit_energies_in_sector_zero':sector_energies,
        'nonzero_rate_of_instantaneous_optimal_leads':float(moving_optimum_rate),
        'numerical_feedback':runs,
        'conclusion':'Four statically minimizing matter rays carry four distinct conserved lead assignments. Rotations permute these sectors; the four rays are not four dynamically interchangeable minima in one fixed-lead sector.',
        'next_gate':'Compute tangent stability in each fixed-lead sector and account for cyclic lead holonomies; inter-sector transitions require explicitly added boundary or lead-loop dynamics.'
    }
    (BASE/'results/spinor_constrained_leads.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
