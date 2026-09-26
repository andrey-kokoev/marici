"""Continuous enlargement of the declared real Clifford model, not of the finite group alone."""
from pathlib import Path
import hashlib
import json
import sympy as s
import check_clifford_retained_order as source

OWNER = Path(__file__).resolve().parents[1]


def main():
    out = OWNER/'results/retained-rotor-generator.json'
    out.unlink(missing_ok=True)
    I, E1, E2, J = [s.Matrix(2,2,x) for x in source.BASIS]
    basis = (I,E1,E2,J)
    angle, other = s.symbols('angle other', real=True)
    scalar, q, p, bivector = s.symbols('scalar q p bivector', real=True)
    Q = scalar*I+q*E1+p*E2+bivector*J
    coordinates = s.Matrix([scalar,q,p,bivector])
    U = lambda a: s.cos(a)*I+s.sin(a)*J
    zero = s.zeros(2)
    assert J*J == -I and J.T == -J
    assert s.simplify(U(angle).T*U(angle)-I) == zero
    assert s.simplify(U(angle)*U(other)-U(angle+other)) == zero
    assert s.simplify(s.diff(U(angle),angle)-J*U(angle)) == zero
    assert U(s.pi/2) == J and U(-s.pi/2) == -J
    assert U(s.pi) == -I and U(2*s.pi) == I
    assert E1.det() == E2.det() == -1 and I.det() == 1
    for E in (E1,E2):
        assert s.simplify(E*U(angle)*E-U(-angle)) == zero

    def coeff(A):
        return s.Matrix([(A[0,0]+A[1,1])/2,(A[0,0]-A[1,1])/2,
                         (A[0,1]+A[1,0])/2,(A[0,1]-A[1,0])/2])
    G = s.Matrix(4,4,lambda i,j:s.trace(basis[i].T*basis[j])/2)
    assert G == s.eye(4)
    # Omega(A,B)=g(A,JB), constructed from the declared g and oriented J.
    Omega = s.Matrix.hstack(*(coeff(J*A) for A in basis))
    assert Omega.T == -Omega and Omega.det() == 1
    D = s.Matrix.hstack(*(coeff(J*A-A*J) for A in basis))
    assert D*coordinates == s.Matrix([0,2*p,-2*q,0])
    assert D.T*Omega+Omega*D == s.zeros(4)
    H0 = q*q+p*p
    gradient = s.Matrix([s.diff(H0,x) for x in coordinates])
    assert (D*coordinates).T*Omega == gradient.T
    action = coeff(U(angle)*Q*U(-angle))
    expected = s.Matrix([scalar,q*s.cos(2*angle)+p*s.sin(2*angle),
                         -q*s.sin(2*angle)+p*s.cos(2*angle),bivector])
    assert s.simplify(action-expected) == s.zeros(4,1)
    for E in (E1,E2):
        reflection = s.Matrix.hstack(*(coeff(E*A*E) for A in basis))
        assert reflection.T*Omega*reflection == -Omega
        assert reflection*D*reflection == -D

    # Local principal action on the active canonical plane, sin(2*angle) != 0.
    q0,p0 = s.symbols('q0 p0', real=True)
    principal = ((q*q+q0*q0)*s.cos(2*angle)-2*q*q0)/(2*s.sin(2*angle))
    hj = s.diff(principal,angle)+s.diff(principal,q)**2+q*q
    assert s.trigsimp(hj) == 0
    qpath = q0*s.cos(2*angle)+p0*s.sin(2*angle)
    ppath = -q0*s.sin(2*angle)+p0*s.cos(2*angle)
    assert s.simplify(s.diff(qpath,angle)-2*ppath) == 0
    assert s.simplify(s.diff(ppath,angle)+2*qpath) == 0
    energy = s.trigsimp(qpath*qpath+ppath*ppath)
    assert energy == q0*q0+p0*p0
    lagrangian = s.expand(ppath*s.diff(qpath,angle)-energy)
    closed_action = s.simplify(s.integrate(lagrangian,(angle,0,s.pi)))
    assert closed_action == 0
    assert s.simplify(lagrangian-s.diff(qpath*ppath/2,angle)) == 0
    # A central constant leaves trajectories fixed but changes action holonomy.
    C = s.symbols('C', real=True)
    kappa = s.symbols('kappa', positive=True)
    shifted_action = closed_action-s.pi*C
    assert s.exp(s.I*shifted_action.subs(C,0)/kappa) == 1
    for n in range(-3,4):
        assert s.simplify(s.exp(s.I*shifted_action.subs(C,(2*n+1)*kappa)/kappa)) == -1

    result = {
        'schema':'marici.nima.retained-rotor-generator.v1',
        'classification':'ambient_even_rotor_flow_has_quadratic_generator_but_zero_offset_action_misses_retained_minus_sign',
        'source_boundary':'Finite signed group has no nonconstant continuous real-parameter subgroup in its inherited topology; exponentiation enlarges the group inside the already declared real Clifford algebra.',
        'rotor':'U(angle)=cos(angle)I+sin(angle)J',
        'generator':'D(Q)=[J,Q]; scalar/bivector fixed; qdot=2p, pdot=-2q',
        'symplectic_form':'Omega(A,B)=g(A,JB)=dq wedge dp - dscalar wedge dbivector',
        'hamiltonian':'H_angle=q^2+p^2+C',
        'odd_developments':'Both elementary adjoint involutions are anti-symplectic reversers; they are not members of this Hamiltonian flow.',
        'principal_action':'((q^2+q0^2)*cos(2*angle)-2*q*q0)/(2*sin(2*angle)), away from caustics',
        'full_period_angle':'pi', 'retained_full_period_lift':-1,
        'zero_offset_closed_action':0, 'zero_offset_action_phase':1,
        'constant_offset_matching':'C/kappa must be an odd integer to match the single full-period sign by an action-phase shift; not a uniquely selected offset or a full witness realization.',
        'scope':'Exact symbolic matrix/ODE/HJ/integral checks plus an elementary connectedness argument. Metric, real Clifford realization and exponential enlargement are explicit assumptions. No physical clock, energy unit, source-selected analytic completion, quantization or full native witness realization is derived.',
        'input_sha256':{str(path.relative_to(OWNER)):hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in (Path(__file__),Path(source.__file__))}
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
