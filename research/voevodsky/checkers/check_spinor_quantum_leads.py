"""Exact single-occupation quantization of the already reduced hard-flux model.
Run: uv run --with sympy python THIS_FILE
Conditional choices: hbar=1, periodic lead rotors, operator-square charging.
No microscopic implementation of the hard constraint is asserted.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

BASE=Path(__file__).resolve().parents[1]


def main():
    raw=(BASE/'results/spinor_interacting_construction.json').read_bytes()
    assert json.loads(raw)['verification_passed']
    beta,eta=s.Rational(3,5),s.Rational(1,5)
    v=beta/4
    q=s.I*s.Matrix([[0,1,1,1],[-1,0,1,-1],[-1,-1,0,1],[-1,1,-1,0]])/s.sqrt(3)
    k=s.eye(4)-q
    assert q*q==s.eye(4) and q.H==q
    x=s.symbols('x',real=True)
    energies=[]
    ground_vectors=[]
    rr=(v+s.sqrt(v*v+4))/2
    lam=(2-v-s.sqrt(4+v*v))/2
    constant=3*beta/4+eta/2
    energy=s.simplify(constant+lam)
    # The remaining infinite lattice is excluded analytically: sum ell=-1
    # implies ||ell||^2 is odd; outside -e_i it is >=3. For integer ell,
    # min ell >= -||ell||^2. Since K>=0, H >=3 beta ||ell||^2/8+beta/8+eta/2.
    outside_lower=5*beta/4+eta/2
    assert bool(energy<constant<outside_lower)
    for i in range(4):
        e=s.eye(4)[:,i];projector=e*e.T
        ell=-e
        h=k+v*s.diag(*ell)+(5*beta*(ell.dot(ell))/8+beta/8+eta/2)*s.eye(4)
        low=k-v*projector
        expected=x*(x-2)*(x*x-(2-v)*x-v)
        assert s.simplify((x*s.eye(4)-low).det()-expected)==0
        state=rr*e+q*e
        assert (low*state-lam*state).applyfunc(s.simplify)==s.zeros(4,1)
        norm=s.simplify((state.H*state)[0])
        assert s.simplify(norm-(1+rr*rr))==0
        energies.append(s.simplify((state.H*h*state)[0]/norm))
        assert s.simplify(energies[-1]-energy)==0
        ground_vectors.append(state/s.sqrt(norm))
    # Operator square on the one-occupation subspace is not density square.
    # Sum N_i^2=I follows from N_i=|i><i|; normal-ordered self-quartics vanish.
    ns=[s.diag(*[int(i==j) for j in range(4)]) for i in range(4)]
    assert sum((n*n for n in ns),s.zeros(4))==s.eye(4)
    assert sum((n*(n-s.eye(4)) for n in ns),s.zeros(4))==s.zeros(4)
    for probabilities in ([s.Rational(1,4)]*4,[s.Rational(1,2),s.Rational(1,6),s.Rational(1,6),s.Rational(1,6)]):
        correction=beta*(1-sum(p*p for p in probabilities))/8
        assert correction>0
    # Fixed-flux vector components are not a cutoff: four-dimensional exact
    # matter blocks over every ell in the full integer sum=-1 lattice.
    overlap=s.simplify((ground_vectors[0].H*ground_vectors[1])[0])
    assert overlap!=0
    report={
        'verification_passed':True,'classical_construction_sha256':sha256(raw).hexdigest(),
        'assumptions':['Quantize the reduced model, not a proven parent quantization','hbar=1 in the supplied model units','Periodic untwisted lead angles','One matter occupation in four source modes','Electric energy uses squares of number operators, not normal-ordered quartic replacement'],
        'hilbert_space':'C^4 tensor l2({ell in Z^4 : sum ell=-1}); equivalently C^4 tensor L2(T^3) in a charge-sector trivialization',
        'hamiltonian_block':'K+(beta/4)diag(ell)+(5 beta ||ell||^2/8+beta/8+eta/2)I',
        'domain':'Direct-sum self-adjoint operator; finite Fourier support is a core; quadratic flux growth gives compact resolvent.',
        'ground_fluxes':[-s.eye(4)[:,i] for i in range(4)],
        'ground_energy_exact':str(energy),'ground_energy_decimal':float(energy),
        'outside_four_flux_blocks_lower_bound':str(outside_lower),
        'matter_ratio_exact':str(rr),'selected_face_density':float(rr*rr/(1+rr*rr)),
        'ground_multiplicity':4,'orthogonality':'Different lead Fourier modes are orthogonal, even though their matter vectors overlap.',
        'one_block_characteristic':'x(x-2)[x^2-(2-beta/4)x-beta/4] before scalar electric offset',
        'single_occupation_variance_correction':'<H_quantum>-H_classical(psi,ell)=beta*(1-sum rho_i^2)/8 for a product state with sharp ell',
        'lead_conservation':'Every ell commutes with H. Superpositions of sectors are allowed, but H has no transfer matrix elements between them.',
        'physical_hard_flux_implementation_complete':False,
        'next_gate':'Construct an explicit constrained parent action and audit why finite-stiffness parent quantization is not identical to this reduced Hilbert space.'}
    report['ground_fluxes']=[[int(z) for z in e] for e in report['ground_fluxes']]
    (BASE/'results/spinor_quantum_leads.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
