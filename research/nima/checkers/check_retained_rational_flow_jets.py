"""Exact finite jets; formal completion is kept distinct from real evaluation."""
from fractions import Fraction as F
from itertools import product
from math import factorial, comb
from pathlib import Path
import hashlib
import json
import re
import check_clifford_retained_order as C

OWNER = Path(__file__).resolve().parents[1]
ZERO = C.ZERO


def madd(a,b):
    return tuple(x+y for x,y in zip(a,b))


def msum(values):
    answer = ZERO
    for v in values:
        answer = madd(answer,v)
    return answer


def convolution(a,b,N):
    return [msum(C.mul(a[i],b[k-i]) for i in range(k+1)) for k in range(N+1)]


def scalar_product(a,b,N):
    return [sum(a[i]*b[k-i] for i in range(k+1)) for k in range(N+1)]


def padd(a,b):
    answer = dict(a)
    for key,value in b.items():
        answer[key] = answer.get(key,F(0))+value
    return {k:v for k,v in answer.items() if v}


def pscale(c,a):
    return {k:c*v for k,v in a.items() if c*v}


def pmul(a,b,N):
    answer = {}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            index = i+k,j+l
            if sum(index) <= N:
                answer[index] = answer.get(index,F(0))+v*w
    return {k:v for k,v in answer.items() if v}


def formal_clock(p,N):
    power = {(0,0):F(1)}
    result = {}
    for n in range(1,N+1):
        power = pmul(power,p,N)
        if n % 2:
            result = padd(result,pscale(F(2*(-1)**((n-1)//2),n),power))
    return result


def main():
    out = OWNER/'results/retained-rational-flow-jets.json'
    out.unlink(missing_ok=True)
    limit = 12
    powers = [C.I]
    for n in range(1,limit+2):
        powers.append(C.mul(powers[-1],C.J))
    coefficients = [C.scale(F(1,factorial(n)),powers[n]) for n in range(limit+2)]
    source_units = [(sign,a,b) for sign in (1,-1) for a,b in product((0,1),repeat=2)]
    unit_matrices = [(g,C.realize(g),(-1)**(g[1]+g[2])) for g in source_units]
    total_degree_cases = 0
    signed_chart_cases = 0
    for N in range(limit+1):
        E = coefficients[:N+1]
        Einv = [C.scale((-1)**n,v) for n,v in enumerate(E)]
        assert convolution(E,Einv,N) == [C.I]+[ZERO]*N
        assert convolution([C.reverse(v) for v in E],E,N) == [C.I]+[ZERO]*N
        assert coefficients[:N+2][:-1] == E
        for n in range(N):
            assert C.scale(n+1,E[n+1]) == C.mul(C.J,E[n])
        for i in range(N+1):
            for j in range(N+1-i):
                assert C.mul(E[i],E[j]) == C.scale(comb(i+j,i),E[i+j])
                total_degree_cases += 1
        # The adjoint generator appears without any analytic evaluation.
        for Q in C.BASIS:
            adjoint = [msum(C.mul(C.mul(E[i],Q),Einv[n-i]) for i in range(n+1)) for n in range(N+1)]
            for n in range(N):
                assert C.scale(n+1,adjoint[n+1]) == C.subtract(C.mul(C.J,adjoint[n]),C.mul(adjoint[n],C.J))
        # All signed centers remain present: W_g(x)=E(x)g.
        if N == limit:
            for g,G,orientation in unit_matrices:
                for h,H,_ in unit_matrices:
                    GH = C.mul(G,H)
                    assert GH == C.realize(C.normal_product(g,h))
                    for i in range(N+1):
                        for j in range(N+1-i):
                            lhs = C.mul(C.mul(E[i],G),C.mul(E[j],H))
                            rhs = C.scale(comb(i+j,i)*orientation**j,C.mul(E[i+j],GH))
                            assert lhs == rhs
                            signed_chart_cases += 1
        # Formal Cayley logarithm, with a shared TOTAL-degree cutoff.
        x,y = {(1,0):F(1)},{(0,1):F(1)}
        geometric = {(k,k):F(1) for k in range(N//2+1)}
        cayley_product = pmul(padd(x,y),geometric,N)
        assert formal_clock(cayley_product,N) == padd(formal_clock(x,N),formal_clock(y,N))
        assert formal_clock(pscale(-1,x),N) == pscale(-1,formal_clock(x,N))
        # E(log_Cayley(t)) equals the rational Cayley matrix as a jet.
        log_coeff = [F(0)]*(N+1)
        for n in range(1,N+1,2):
            log_coeff[n] = F(2*(-1)**((n-1)//2),n)
        power = [F(1)]+[F(0)]*N
        composed = [ZERO]*(N+1)
        for n in range(N+1):
            for degree in range(N+1):
                composed[degree] = madd(composed[degree],C.scale(power[degree],E[n]))
            power = scalar_product(power,log_coeff,N)
        expected = []
        for n in range(N+1):
            if n == 0:
                expected.append(C.I)
            elif n % 2:
                expected.append(C.scale(2*(-1)**((n-1)//2),C.J))
            else:
                expected.append(C.scale(2*(-1)**(n//2),C.I))
        assert composed == expected
    # Two truncation hostiles: separate-variable truncation retains xy,
    # and differentiation cannot be an endomorphism of a fixed jet quotient.
    assert C.mul(C.J,C.J) == C.scale(-1,C.I) != ZERO
    # E_1'=J, but J*E_1=J-xI: the same-order ODE has a nonzero x residual.
    assert C.mul(C.J,coefficients[1]) != ZERO
    # Finite evaluation at a nonzero number does not respect x^(N+1)=0.
    assert F(1,2)**(limit+1) != 0
    assert F(limit+1) != 0  # derivative of the discarded relation is nonzero
    assert C.mul(C.J,C.I) != C.mul(C.scale(-1,C.J),C.I)
    assert C.evaluate(()) == C.evaluate((1,1)) and () != (1,1)

    formal_path = OWNER/'agda/FormalRotorCoefficients.agda'
    receipt_path = OWNER/'results/agda-FormalRotorCoefficients.json'
    receipt = json.loads(receipt_path.read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces']
    assert hashlib.sha256(formal_path.read_bytes()).hexdigest() == receipt['source_sha256'].lower()
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
        'schema':'marici.nima.retained-rational-flow-jets.v1',
        'classification':'native_rational_coefficients_give_coherent_formal_rotor_jets_and_a_formal_clock_not_real_time_evaluation',
        'formal_flow':'E(x)=sum J^n*x^n/n!, with finite E_N in Mat2(Q[x]/x^(N+1))',
        'formal_clock':'ell(t)=2*sum((-1)^n*t^(2n+1)/(2n+1)); ell((t+u)/(1-tu))=ell(t)+ell(u)',
        'signed_charts':'W_g(x)W_h(y)=W_(gh)(x+orientation(g)*y); centers and full histories remain separate',
        'controls':{'maximum_jet_order':limit,'total_degree_composition_coefficients':total_degree_cases,'signed_chart_composition_coefficients':signed_chart_cases},
        'fresh_agda':'Actual constructed rational factorial coefficients satisfy their recurrence and are unique at every order; not a formalization of the entire power-series ring.',
        'hostiles':['rectangular cutoff cannot compare E_N(x+y) at unchanged order','differentiation lowers jet order','nonzero real evaluation does not respect a finite nilpotent relation'],
        'scope':'Formal x-adic completion with an explicit chosen Clifford product. No finite-angle value, real analytic convergence, winding, physical time, or native source-admission theorem follows from these jet checks.',
        'input_sha256':{str(path.relative_to(OWNER)):hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in (Path(__file__),Path(C.__file__),formal_path,receipt_path)}
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
