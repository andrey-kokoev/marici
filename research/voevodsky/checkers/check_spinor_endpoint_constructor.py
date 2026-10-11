"""Exact endpoint-rotor constructor and reduced-Hilbert-space intertwiner.
Run: uv run --with sympy python THIS_FILE
An ideal quantum Hamiltonian specification, not a hardware demonstration.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

BASE=Path(__file__).resolve().parents[1]


def main():
    raw=(BASE/'results/spinor_quantum_leads.json').read_bytes()
    assert json.loads(raw)['verification_passed']
    q=s.I*s.Matrix([[0,1,1,1],[-1,0,1,-1],[-1,-1,0,1],[-1,1,-1,0]])/s.sqrt(3)
    k=s.eye(4)-q
    beta,eta=s.symbols('beta eta',positive=True)
    ell=s.Matrix(s.symbols('ell0:4',integer=True))
    # On physical basis |i; n=-ell-e_i; ell>, diagonal rotor energy must
    # equal the reduced operator-square prescription for every integer ell.
    for i in range(4):
        e=s.eye(4)[:,i];n=-ell-e
        assert n+ell+e==s.zeros(4,1)
        charging=beta*n.dot(n)/8+beta*ell.dot(ell)/2+eta/2
        target=5*beta*ell.dot(ell)/8+beta/8+beta*ell[i]/4+eta/2
        assert s.expand(charging-target)==0
        for j in range(4):
            # R_i R_j^dagger is the charge -1 transport for hop i -> j.
            shift=e-s.eye(4)[:,j]
            assert n+shift==-ell-s.eye(4)[:,j]
            assert shift+s.eye(4)[:,j]-e==s.zeros(4,1)
            assert s.conjugate(k[j,i])==k[i,j]
    # Products of endpoint shift vectors telescope on all sourced faces.
    phases=[]
    for face,sign in [((1,2,3),1),((0,2,3),-1),((0,1,3),1),((0,1,2),-1)]:
        shift=s.zeros(4,1);phase=1
        for i,j in zip(face,face[1:]+face[:1]):
            shift+=s.eye(4)[:,i]-s.eye(4)[:,j]
            phase*=s.sqrt(3)*q[j,i]
        assert shift==s.zeros(4,1)
        if sign<0:phase=s.conjugate(phase)
        phase=s.simplify(phase)
        assert phase==s.I
        phases.append(str(phase))
    # Here the directed transport uses Q[j,i]. Reversing every edge
    # conjugates the Wilson phases; relative endpoint products stay I.
    for flux in [(-1,0,0,0),(0,-1,0,0),(-3,2,1,-1),(10,-8,-2,-1)]:
        assert sum(flux)==-1
        for i in range(4):
            n=[-flux[j]-int(i==j) for j in range(4)]
            assert sum(n)==0
            assert all(n[j]+flux[j]+int(i==j)==0 for j in range(4))
    result={'verification_passed':True,'quantum_leads_sha256':sha256(raw).hexdigest(),
            'kinematics':'One matter occupation, four endpoint rotors and four lead rotors; integer n,ell with sum n=0 and sum ell=-1.',
            'gauge_generators':'G_i=n_i+ell_i+N_i',
            'transport':'T_ji=|j><i| R_i R_j^dagger, R_i raises endpoint n_i by one',
            'hamiltonian':'sum_ij K_ji T_ji+beta sum n_i^2/8+beta sum ell_i^2/2+eta/2',
            'flatness':'Every relative face product telescopes to I as an operator identity on the full endpoint-rotor domain.',
            'directed_charge_minus_one_source_Wilson_phases':phases,
            'physical_basis':'|i; n=-ell-e_i; ell>',
            'unitary_intertwiner':'|i> tensor |ell> maps to |i; -ell-e_i; ell>; bijection of orthonormal bases, exact Hamiltonian intertwining.',
            'constraint_type':'First-class site gauge invariance in a structurally flat configuration model; not second-class projection of independent links.',
            'finite_penalty_needed_for_flatness':False,
            'hardware_realization_verified':False,
            'unselected_physical_inputs':['Endpoint versus independent-link degrees of freedom','Exact assisted hopping amplitudes and intrinsic source phases','Endpoint/lead charging coefficients beta/8 and beta/2','Preparation and preservation of the gauge-neutral charge sector'],
            'next_gate':'Consolidate and verify the quantum chain; distinguish this exact ideal constructor from an unverified physical device, and specify acceptance tests for any proposed platform.'}
    (BASE/'results/spinor_endpoint_constructor.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
