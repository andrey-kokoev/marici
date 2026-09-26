"""Dimensionless angular clock on an explicitly unwrapped rotor-history model."""
from itertools import product
from pathlib import Path
import hashlib
import json
import sympy as s
import check_clifford_retained_order as source

OWNER = Path(__file__).resolve().parents[1]


def multiply(g,h):
    a,e = g
    b,d = h
    return a+(-1)**e*b,e^d


def inverse(g):
    a,e = g
    return -(-1)**e*a,e


def main():
    out = OWNER/'results/retained-rotor-history-clock.json'
    out.unlink(missing_ok=True)
    a,b,c,reading = s.symbols('a b c reading', real=True)
    # Universal real-angle identities; discrete data only select parity.
    for e,d,f in product((0,1),repeat=3):
        g,h,k = (a,e),(b,d),(c,f)
        left,right = multiply(multiply(g,h),k),multiply(g,multiply(h,k))
        assert s.expand(left[0]-right[0]) == 0 and left[1] == right[1]
    for e,d in product((0,1),repeat=2):
        g,h = (a,e),(b,d)
        gh = multiply(g,h)
        assert s.expand(gh[0]-g[0]-(-1)**e*h[0]) == 0
        composed = (-1)**e*((-1)**d*reading+b)+a
        assert s.expand(composed-((-1)**gh[1]*reading+gh[0])) == 0
    for e in (0,1):
        assert multiply((a,e),inverse((a,e))) == (0,0)
    # Reflection conjugates every rotation to its inverse. Any ordinary
    # additive real homomorphism therefore gives x=-x, hence x=0.
    reflection = (0,1)
    assert multiply(multiply(reflection,(a,0)),reflection) == (-a,0)
    value = s.symbols('value', real=True)
    assert s.solve(s.Eq(value,-value),value) == [0]

    # The clock comes from the PREVIOUSLY CONSTRUCTED phase transport.
    q,p,z,scalar,phi = s.symbols('q p z scalar phi', real=True)
    kappa = s.symbols('kappa', positive=True)
    C,theta = s.symbols('C theta', real=True)
    F = (q*p+scalar*z)/2
    clock = F/kappa-phi
    phasedot = (p*p-q*q-C)/kappa
    clockdot = s.simplify(s.diff(clock,q)*2*p+s.diff(clock,p)*(-2*q)
                         +s.diff(clock,phi)*phasedot)
    assert clockdot == C/kappa
    assert clockdot.subs(C,kappa) == 1
    assert clockdot.subs(C,0) == 0
    Fnew = s.symbols('Fnew',real=True)
    for e in (0,1):
        orientation = (-1)**e
        newphase = orientation*phi+(Fnew-orientation*F)/kappa-theta
        newclock = Fnew/kappa-newphase
        assert s.simplify(newclock-(orientation*clock+theta)) == 0
    # Consistent changes of primitive/phase chart cancel out of the reading.
    chi = s.symbols('chi',real=True)
    assert s.simplify((F+kappa*chi)/kappa-(phi+chi)-clock) == 0

    # Exact finite endpoint controls: angles measured in pi/2 units.
    rotors = (source.I,source.J,source.scale(-1,source.I),source.scale(-1,source.J))
    def matrix(g):
        angle,e = g
        return source.mul(rotors[angle%4],source.E1 if e else source.I)
    L,R = (0,1),(-1,1)
    assert matrix(L) == source.E1 and matrix(R) == source.E2
    def evaluate(word,second=R):
        answer = (0,0)
        for letter in word:
            answer = multiply(answer,L if letter == 1 else second)
        return answer
    words = [w for n in range(9) for w in product((1,2),repeat=n)]
    for word in words:
        lifted = evaluate(word)
        assert matrix(lifted) == source.realize(source.evaluate(word))
        assert multiply(lifted,inverse(lifted)) == (0,0)
        assert evaluate(word[::-1]) == inverse(lifted)
    assert evaluate((1,2)*2) == (2,0)  # pi; action identity but lift -I
    assert matrix(evaluate((1,2)*2)) == source.scale(-1,source.I)
    assert evaluate((1,2)*4) == (4,0)  # 2*pi; lift identity, history nonempty
    assert matrix(evaluate((1,2)*4)) == source.I
    assert evaluate(()) == evaluate((1,1)) and () != (1,1)
    # The discrete word does NOT itself select angular paths for its letters.
    alternative_R = (3,1)
    assert matrix(alternative_R) == matrix(R)
    assert evaluate((1,2),alternative_R) == (-3,0)
    assert evaluate((1,2)) == (1,0)

    # Winding over the signed endpoint group is orientation-twisted, not central.
    endpoints = tuple(product(range(4),(0,1)))
    def endpoint_product(g,h):
        angle,e = multiply(g,h)
        return angle%4,e
    def carry(g,h):
        raw,e = multiply(g,h)
        return (raw-(raw%4))//4
    for g,h,k in product(endpoints,repeat=3):
        assert carry(g,h)+carry(endpoint_product(g,h),k) == (
            (-1)**g[1]*carry(h,k)+carry(g,endpoint_product(h,k)))
    assert multiply(multiply(reflection,(4,0)),reflection) == (-4,0)
    # General continuous affine clock cocycles: A*angle+B on odd elements.
    A,B = s.symbols('A B',real=True)
    for e,d in product((0,1),repeat=2):
        g,h = (a,e),(b,d)
        gh = multiply(g,h)
        t = lambda x:A*x[0]+B*x[1]
        assert s.expand(t(gh)-t(g)-(-1)**e*t(h)) == 0

    # Angular variation is a distinct nonnegative PATH readout, not a
    # homomorphism of endpoint transformations. Odd frame changes flip
    # continuous increments but leave this variation invariant.
    variation = lambda increments:sum(abs(v) for v in increments)
    path = (s.Rational(1,2),s.Rational(-1,4),s.Rational(3,4))
    assert variation(path) == variation(tuple(-v for v in path))
    assert variation(path+path) == 2*variation(path)
    assert variation((s.Rational(1,3),s.Rational(2,3))) == variation((s.Integer(1),))
    assert sum((1,-1)) == 0 and variation((1,-1)) == 2
    assert variation(()) == 0

    result = {
        'schema':'marici.nima.retained-rotor-history-clock.v1',
        'classification':'unwrapped_phase_gives_affine_angular_clock_not_endpoint_elapsed_time',
        'reading':'T=F/kappa-phi=-psi on a chosen real lift of the fiber angle',
        'rate':'dT/dtheta=C/kappa; specified defining-module phase fixes C=kappa and rate one',
        'transport':'T -> orientation*T+theta',
        'cocycle':'tau(gh)=tau(g)+orientation(g)*tau(h)',
        'ordinary_clock_obstruction':'reflection conjugacy forces any ordinary additive real homomorphism on the full rotor/reverser group or its cover to vanish',
        'descent_obstruction':'2*pi retained rotation returns the signed matrix to identity but advances the unwrapped reading; it cannot descend to endpoint data',
        'extra_data':'A continuous phase path and starting lift, or explicit angular lifts for primitive letters, are required. A discrete retained word alone does not determine those lifts.',
        'duration_candidate':'Integral of absolute angular increments on supplied continuous rotor paths is additive and reversal-even; it is not invariant under arbitrary endpoint-preserving backtrack deletion, and gives no duration for an unspecified odd operation.',
        'controls':{'source_words':len(words),'twisted_winding_triples':len(endpoints)**3,
                    'symbolic_associativity_parities':8,'symbolic_transport_parities':4},
        'scope':'Conditional angular clock on the declared Clifford rotor/phase realization. It is a history-sensitive signed frame coordinate, not a faithful encoding of histories, nonnegative duration, native-source clock theorem, or calibrated physical time.',
        'input_sha256':{str(path.relative_to(OWNER)):hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in (Path(__file__),Path(source.__file__),OWNER/'retained-rotor-phase-transport.md')}
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
