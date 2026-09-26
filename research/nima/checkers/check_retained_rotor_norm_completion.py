"""Rational certificates for the selected rotor packet's declared norm completion.
The all-order convergence argument is in the companion note, not inferred from
these bounded tests. No arbitrary formal-series evaluation is used.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import re
import check_clifford_retained_order as C

OWNER = Path(__file__).resolve().parents[1]


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def partial(x,N):
    result = C.I
    term = C.I
    for n in range(1,N+1):
        term = C.scale(x/F(n),C.mul(term,C.J))
        result = add(result,term)
    return result


def tail(R,N):
    R = F(R)
    assert R >= 0 and N+2 > R
    return R**(N+1)/F(factorial(N+1))/(1-R/F(N+2))


def clock_partial(t,M):
    return sum((F(2*(-1)**n,2*n+1)*t**(2*n+1) for n in range(M+1)),F(0))


def clock_tail(t,M):
    assert 0 <= t <= 1
    return F(2,2*M+3)*t**(2*M+3)


def main():
    out = OWNER/'results/retained-rotor-norm-completion.json'
    out.unlink(missing_ok=True)
    block_checks = 0
    for R in (F(0),F(1,2),F(1),F(2),F(4),F(8)):
        for N in (8,12,20,32):
            bound = tail(R,N)
            ratio = R/F(N+2)
            for k in range(N+1,N+30):
                term = R**k/F(factorial(k))
                geometric = R**(N+1)/F(factorial(N+1))*ratio**(k-N-1)
                assert term <= geometric
            block = sum((R**k/F(factorial(k)) for k in range(N+1,N+31)),F(0))
            assert block <= bound
            for x in (-R,F(0),R):
                difference = C.subtract(partial(x,N+8),partial(x,N))
                assert C.norm(difference) <= bound*bound
                derivative_difference = C.mul(C.J,C.subtract(partial(x,N+7),partial(x,N-1)))
                derivative_bound = tail(R,N-1)
                assert C.norm(derivative_difference) <= derivative_bound**2
                block_checks += 1

    # Actual evaluated polynomial defects are bounded, not declared zero.
    points = tuple(map(F,(-2,-1,0,1,2)))+(F(-1,2),F(1,2))
    N = 16
    signed_checks = 0
    units = [(C.realize((sign,a,b)),(-1)**(a+b))
             for sign in (1,-1) for a in (0,1) for b in (0,1)]
    for x in points:
        X = partial(x,N)
        dx = tail(abs(x),N)
        assert C.norm(C.subtract(C.mul(C.reverse(X),X),C.I)) <= (2*dx+dx*dx)**2
        ode_error = C.subtract(C.mul(C.J,partial(x,N-1)),C.mul(C.J,X))
        assert C.norm(ode_error) == (x**N/F(factorial(N)))**2
        for y in points:
            Y = partial(y,N)
            dy = tail(abs(y),N)
            for G,orientation in units:
                for H,_ in units:
                    endpoint = x+orientation*y
                    lhs = C.mul(C.mul(X,G),C.mul(Y,H))
                    rhs = C.mul(partial(endpoint,N),C.mul(G,H))
                    bound = dx+dy+dx*dy+tail(abs(endpoint),N)
                    assert C.norm(C.subtract(lhs,rhs)) <= bound**2
                    signed_checks += 1

    # Alternating clock values converge uniformly up to t=1. Their
    # differentiated polynomials at that endpoint alternate between 0 and 2.
    for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        for M in (0,1,2,4,8,16,32):
            approximate = clock_partial(t,M)
            bound = clock_tail(t,M)
            for bigger in (M+1,M+4,M+9):
                assert abs(clock_partial(t,bigger)-approximate) <= bound
    boundary_derivatives = [sum(2*(-1)**n for n in range(M+1)) for M in range(20)]
    assert set(boundary_derivatives) == {0,2}
    assert 1 not in boundary_derivatives

    # Recover the quarter-turn and its signed returns without using pi or a
    # floating-point trigonometric function as input to the checker.
    source_targets = {1:C.J,2:C.scale(-1,C.I),3:C.scale(-1,C.J),4:C.I}
    return_checks = 0
    certificate = None
    for M in (0,1,2,4,8,16,32,64):
        aM = clock_partial(F(1),M)
        assert F(4,3) <= aM <= 2
        da = clock_tail(F(1),M)
        for k,target in source_targets.items():
            polynomial = partial(k*aM,40)
            bound = tail(F(2*k),40)+k*da
            assert C.norm(C.subtract(polynomial,target)) <= bound**2
            return_checks += 1
            if M == 64 and k == 1:
                certificate = {'clock_terms':M+1,'rotor_order':40,
                               'quarter_turn_error_upper_bound':str(bound)}
    assert C.norm(C.subtract(C.J,C.scale(-1,C.J))) == 4
    assert C.norm(C.subtract(C.I,C.scale(-1,C.I))) == 4
    assert C.evaluate((1,2)*4) == C.evaluate(()) and (1,2)*4 != ()

    coefficient_proof = OWNER/'agda/FormalRotorCoefficients.agda'
    proof_receipt = OWNER/'results/agda-FormalRotorCoefficients.json'
    receipt = json.loads(proof_receipt.read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces']
    assert hashlib.sha256(coefficient_proof.read_bytes()).hexdigest() == receipt['source_sha256'].lower()
    visited = set()
    def audit_imports(module):
        path = OWNER/'agda'/(module.replace('.','/')+'.agda')
        if not path.exists() or module in visited:
            return
        visited.add(module)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == receipt['owner_source_inventory_sha256'][path.name].lower()
        for dep in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)',path.read_text(encoding='utf-8'),re.M):
            audit_imports(dep)
    audit_imports('FormalRotorCoefficients')
    result = {
        'schema':'marici.nima.retained-rotor-norm-completion.v1',
        'classification':'selected_rational_rotor_packet_converges_in_declared_norm_and_recovers_retained_finite_signs',
        'topology':'Archimedean coefficient/reversion norm completion of the chosen rational even Clifford algebra; not the x-adic formal completion and not a newly established native physical topology.',
        'uniform_tail':'B_N(R)=R^(N+1)/(N+1)! / (1-R/(N+2)), for N+2>R',
        'derivative_tail':'B_(N-1)(R), with N+1>R; derivative passage is uniform on compact real parameter intervals',
        'clock_value_tail':'2*t^(2M+3)/(2M+3), uniform for 0<=t<=1',
        'clock_boundary_hostile':'ell_Mprime(1) alternates between 0 and 2; boundary derivative must come from the rational integral kernel, not this divergent derivative sequence',
        'source_return':'a=lim ell_M(1) gives E(a)=J, E(2a)=-I, E(4a)=I; histories and winding stay separate from endpoint matrices',
        'controls':{'tail_blocks':block_checks,'signed_composition_bounds':signed_checks,'return_bounds':return_checks},
        'certificate':certificate,
        'scope':'General analytic proof under an explicitly declared norm completion, supported by exact rational finite certificates. No universal formal-series evaluation, native product/readout admission, physical time unit, or quantum dynamical interpretation is derived.',
        'input_sha256':{str(path.relative_to(OWNER)):hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in (Path(__file__),Path(C.__file__),coefficient_proof,proof_receipt,
                                     OWNER/'retained-rational-flow-jets.md')}
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
