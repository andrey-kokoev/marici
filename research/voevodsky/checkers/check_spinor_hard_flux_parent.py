"""Exact classical second-class reduction of internal source face constraints.
Run: uv run --with sympy python THIS_FILE
Multiplier action is an ideal model, not a laboratory implementation.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

BASE=Path(__file__).resolve().parents[1]


def main():
    raw=(BASE/'results/spinor_quantum_leads.json').read_bytes()
    assert json.loads(raw)['verification_passed']
    edges=[(i,j) for i in range(4) for j in range(i+1,4)]
    b=s.zeros(4,6)
    for n,(i,j) in enumerate(edges):b[i,n]=-1;b[j,n]=1
    c=s.Matrix([[0,0,0,1,-1,1],[0,-1,1,0,0,-1],
                [1,0,-1,0,1,0],[-1,1,0,-1,0,0]])
    d=c[:3,:]
    w=d*d.T
    assert d.rank()==3 and c.rank()==3 and w.det()==16
    assert b*d.T==s.zeros(4,3)
    omega=s.BlockMatrix([[s.zeros(3),w],[-w,s.zeros(3)]]).as_explicit()
    assert omega.det()==256
    # Canonical coordinates ordered A_6,E_6. Constraint functions D A,D E.
    j=s.BlockMatrix([[s.zeros(6),s.eye(6)],[-s.eye(6),s.zeros(6)]]).as_explicit()
    f=s.diag(d,d)
    assert f*j*f.T==omega
    jd=s.simplify(j-j*f.T*omega.inv()*f*j)
    projector=s.eye(6)-d.T*w.inv()*d
    assert projector==b.T*b/4
    assert projector*projector==projector and projector.rank()==3
    assert jd==s.BlockMatrix([[s.zeros(6),projector],[-projector,s.zeros(6)]]).as_explicit()
    assert f*jd==s.zeros(6,12)
    # Reaction supplies exact tangency for any internal current, not only
    # the previously studied coherent circulation.
    current=s.Matrix(s.symbols('j0:6'))
    reaction=w.inv()*d*current
    edot=current-d.T*reaction
    assert d*edot==s.zeros(3,1) and b*edot==b*current
    assert edot==projector*current
    # Eliminate internal field at fixed leads using Gauss.
    rho=s.Matrix(s.symbols('rho0:4'))
    ell=s.Matrix(s.symbols('ell0:4'))
    substitute={rho[3]:1-sum(rho[:3]),ell[3]:-1-sum(ell[:3])}
    residual=(-rho-ell).subs(substitute,simultaneous=True)
    electric=b.T*residual/4
    assert s.simplify(b*electric-residual)==s.zeros(4,1)
    assert d*electric==s.zeros(3,1)
    assert s.simplify(electric.dot(electric)-residual.dot(residual)/4)==0
    # Structural implementation in classical configuration space A=B^T u:
    # every relative Wilson product is identically one, not merely low energy.
    u=s.Matrix(s.symbols('u0:4'))
    assert c*b.T*u==s.zeros(4,1)
    # In local unwrapped quantum coordinates, chi and tangency are conjugate:
    # [D A,D E]=i hbar W. Any single diagonal entry already obstructs
    # annihilating a normalized state with both constraints.
    assert all(w[i,i]==3 for i in range(3))
    result={
        'verification_passed':True,'quantum_leads_sha256':sha256(raw).hexdigest(),
        'independent_face_matrix':[[int(x) for x in row] for row in d.tolist()],
        'constraint_gram':[[int(x) for x in row] for row in w.tolist()],
        'constraint_poisson_determinant':str(omega.det()),
        'classification':'Three coordinate constraints plus three secondary electric constraints are second class; site Gauss constraints remain first class.',
        'dirac_internal_bracket':'{A,E}_D=P=B_internal^T B_internal/4',
        'reaction':'lambda=(D D^T)^(-1) D J for charge -1; E_dot=P J',
        'structural_flatness':'A_internal=B_internal^T u modulo 2*pi retains source phases and removes independent cycle coordinates.',
        'reduced_electric_energy':'beta ||ell||^2/2+beta ||rho+ell||^2/8',
        'quantum_constraint_obstruction':'Locally [D A,D E]=i hbar D D^T; no normalized vector is annihilated by both. Globally exact flat-holonomy support has Haar measure zero in the unconstrained U(1) edge configuration space.',
        'reduction_quantization_status':'Consistent reduced model exists. It is not an ordinary common-kernel subspace of the unreduced continuous-link Hilbert space.',
        'physical_implementation_status':'Ideal multiplier or structurally restricted configuration model only; no finite-resource physical constructor supplied.',
        'next_gate':'Quantify a finite-stiffness parent: flux variance, electric cost and zero-point energy, and determine what limiting/subtraction prescription could approach the reduced model.'}
    (BASE/'results/spinor_hard_flux_parent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
