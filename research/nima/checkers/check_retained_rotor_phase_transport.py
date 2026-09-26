"""Exact phase-space rotor lift and two generating-function charts.
All conclusions are relative to the declared real Clifford defining module
and the specified phase connection; no physical clock/quantization is inferred.
"""
from pathlib import Path
import hashlib
import json
import sympy as s
import check_clifford_retained_order as source

OWNER = Path(__file__).resolve().parents[1]


def main():
    out = OWNER/'results/retained-rotor-phase-transport.json'
    out.unlink(missing_ok=True)
    I,E1,E2,J = [s.Matrix(2,2,x) for x in source.BASIS]
    th,eta = s.symbols('th eta', real=True)
    a,q,p,b,phi = s.symbols('a q p b phi', real=True)
    kappa = s.symbols('kappa', positive=True)
    k = s.symbols('k', real=True)
    x = s.Matrix([a,q,p,b])
    Q = a*I+q*E1+p*E2+b*J
    U = lambda t:s.cos(t)*I+s.sin(t)*J
    def rho(t,e):
        return U(t)*(E1 if e else I)
    def coeff(A):
        return s.Matrix([(A[0,0]+A[1,1])/2,(A[0,0]-A[1,1])/2,
                         (A[0,1]+A[1,0])/2,(A[0,1]-A[1,0])/2])
    def F(v):
        return (v[1]*v[2]+v[0]*v[3])/2
    def beta(v):
        return s.Matrix([0,v[2],0,v[0]])
    def transform(t,e,v):
        A = sum((c*B for c,B in zip(v,(I,E1,E2,J))),s.zeros(2))
        r = rho(t,e)
        return s.simplify(coeff(r*A*r.T))
    def lift(t,e,v,phase,weight=1):
        target = transform(t,e,v)
        return target, (-1)**e*phase+(F(target)-(-1)**e*F(v))/kappa-weight*t

    for e in (0,1):
        target,phase = lift(th,e,x,phi)
        sign = (-1)**e
        # Pull back dphi-beta/kappa; odd transformations reverse this form.
        base_coeff = s.Matrix([s.diff(phase,c) for c in x])-target.jacobian(x).T*beta(target)/kappa
        assert s.simplify(base_coeff+sign*beta(x)/kappa) == s.zeros(4,1)
        assert s.diff(phase,phi) == sign
        invth = -sign*th
        back,backphase = lift(invth,e,target,phase)
        assert s.simplify(back-x) == s.zeros(4,1)
        assert s.simplify(backphase-phi) == 0
        for d in (0,1):
            assert s.simplify(rho(th,e)*rho(eta,d)-rho(th+sign*eta,e^d)) == s.zeros(2)
            inner,innerphase = lift(eta,d,x,phi)
            actual,actualphase = lift(th,e,inner,innerphase)
            expected,expectedphase = lift(th+sign*eta,e^d,x,phi)
            assert s.simplify(actual-expected) == s.zeros(4,1)
            assert s.simplify(actualphase-expectedphase) == 0

    assert rho(0,1) == E1 and rho(-s.pi/2,1) == E2
    for t,expected in ((s.pi/2,J),(-s.pi/2,-J),(s.pi,-I),(2*s.pi,I)):
        assert rho(t,0) == expected
        _,phase = lift(t,0,x,phi)
        assert s.simplify(phase-phi+t) == 0
    # A weight-five character passes ALL finite samples, but not real linearity.
    for n in range(4):
        t = n*s.pi/2
        assert U(5*t) == U(t)
    assert U(5*s.pi/4) == -U(s.pi/4)
    assert U(5*s.pi/4) != s.cos(s.pi/4)*I+s.sin(s.pi/4)*J
    # Existing defining-module action is weight one in w=u+i*v coordinates.
    u,v = s.symbols('u v', real=True)
    w = s.Matrix([u,v])
    rotated = U(th)*w
    assert s.expand(rotated[0]+s.I*rotated[1]-(s.cos(th)-s.I*s.sin(th))*(u+s.I*v)) == 0

    target,phase = lift(th,0,x,phi)
    D = s.diff(target,th).subs(th,0)
    phasedot = s.simplify(s.diff(phase,th).subs(th,0))
    contact_H = s.simplify(-kappa*(phasedot-(beta(x).dot(D))/kappa))
    assert contact_H == q*q+p*p+kappa
    assert phasedot == (p*p-q*q-kappa)/kappa

    # Two charts cover all angular times: sin and cos cannot vanish together.
    qi,pi = s.symbols('qi pi', real=True)
    S0 = ((q*q+qi*qi)*s.cos(2*th)-2*q*qi)/(2*s.sin(2*th))
    G0 = q*pi/s.cos(2*th)-(q*q+pi*pi)*s.tan(2*th)/2
    Sc,Gc = S0-kappa*th,G0-kappa*th
    for action in (Sc,Gc):
        assert s.trigsimp(s.diff(action,th)+s.diff(action,q)**2+q*q+kappa) == 0
    qi_from_q_pi = (q-pi*s.sin(2*th))/s.cos(2*th)
    assert s.trigsimp((Sc+pi*qi).subs(qi,qi_from_q_pi)-Gc) == 0
    assert s.trigsimp(s.diff(Gc,pi)-qi_from_q_pi) == 0
    for n in range(-2,3):
        t = n*s.pi/2
        sign = -1 if n % 2 else 1
        assert s.simplify(Gc.subs(th,t)-(sign*q*pi-kappa*t)) == 0
    # Independent counting-metric control for the source sector (not an
    # assertion that counting norm is the unique physical metric).
    anchor,odd = (1,0,0,0),(0,1,-1,0)
    tensor = lambda u,v:s.Matrix([a*b for a in u for b in v])
    source_basis = (tensor(anchor,anchor),tensor(anchor,odd),tensor(odd,anchor),tensor(odd,odd))
    counting_gram = s.Matrix(4,4,lambda i,j:source_basis[i].dot(source_basis[j]))
    assert counting_gram == s.diag(1,2,2,4)
    left_J = s.Matrix.hstack(*(coeff(J*A) for A in (I,E1,E2,J)))
    assert counting_gram*left_J+(counting_gram*left_J).T != s.zeros(4)
    # One correction can be stored in the action OR the fiber, not both.
    assert s.exp(-s.I*s.pi) == -1
    assert s.exp(-2*s.I*s.pi) == 1

    result = {
        'schema':'marici.nima.retained-rotor-phase-transport.v1',
        'classification':'defining_module_fixes_weight_one_rotor_phase_and_sews_two_hj_charts',
        'phase_transport':'phi -> orientation*phi + (F(target)-orientation*F(source))/kappa - theta; F=(q*p+s*z)/2',
        'connection':'alpha=dphi-(p*dq+s*dz)/kappa',
        'symmetry_checks':'all four parity pairs, arbitrary symbolic angles; inverse and signed connection preservation',
        'source_module':'U(theta) acts on w=u+i*v as exp(-i*theta); e1 conjugates, e2=i times conjugation',
        'classification_boundary':'Continuous rotor characters have integer weight. Exact finite samples fix weight modulo four; real-linear extension of the declared Clifford defining-module action fixes weight one.',
        'contact_hamiltonian':'q^2+p^2+kappa',
        'hj_action':'S0-kappa*theta, or equivalently S0 with a separate exp(-i*theta) module factor',
        'caustic_sewing':'Type-I and type-II generating functions related by the initial-variable Legendre boundary term; covers sin(2theta)=0 without erasing momentum or phase.',
        'hostiles':['weight five matches finite samples but violates real-linearity','double-counting offset and module factor erases the retained full-period minus sign','native counting Gram diag(1,2,2,4) does not equal the supplied Clifford metric'], 
        'scope':'Conditional classical phase-space/contact realization of the specified Clifford module. Neither physical time, kappa=hbar, quantum zero-point energy, position-space propagator amplitude, nor full native higher-witness realization is derived.',
        'input_sha256':{str(path.relative_to(OWNER)):hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in (Path(__file__),Path(source.__file__),OWNER/'retained-rotor-generator.md')}
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
