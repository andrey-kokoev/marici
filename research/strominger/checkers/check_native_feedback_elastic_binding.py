"""Conditional action/face binding, not a new native theorem or physical law.
Native premise: NativeFeedbackRouteReadout.intertwines on actual comparisons.
Tests the independently existing elastic swap against a declared count reader.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[3]


def main():
    u,v=s.symbols('u v',real=True)
    gain=s.symbols('gain',positive=True,real=True)
    a,b=s.symbols('a b',positive=True,real=True) # square roots of supplied masses
    m1,m2=a*a,b*b
    M=m1+m2
    swap=s.Matrix([[0,1],[1,0]])
    eplus=s.Matrix([1,1])/s.sqrt(2)
    eminus=s.Matrix([1,-1])/s.sqrt(2)
    center=s.Matrix([a,b])/s.sqrt(M)
    relative=s.Matrix([b,-a])/s.sqrt(M)
    orthogonal=center*eplus.T+relative*eminus.T
    mechanical=s.diag(a,b)*orthogonal
    elastic=s.Matrix([[m1-m2,2*m1],[2*m2,m2-m1]])/M
    simplify=lambda x:x.applyfunc(s.simplify)
    assert simplify(orthogonal.T*orthogonal)==s.eye(2)
    assert s.simplify(mechanical.det())==a*b
    assert simplify(elastic*mechanical-mechanical*swap)==s.zeros(2)
    assert simplify(elastic*elastic)==s.eye(2)
    metric=s.diag(1/m1,1/m2)
    assert simplify(elastic.T*metric*elastic)==metric
    assert simplify(s.ones(1,2)*elastic)==s.ones(1,2)
    reader=gain*s.Matrix([u,v])
    assert simplify(elastic*mechanical*reader-mechanical*gain*s.Matrix([v,u]))==s.zeros(2,1)
    assert simplify(elastic**2*mechanical*reader-mechanical*reader)==s.zeros(2,1)
    # The actual native fixture reads (1,2), then (2,1), not free seed routes.
    fixture=mechanical.subs({a:1,b:1})
    assert simplify(fixture)==s.eye(2)
    initial=s.Matrix([1,2])
    final=swap*initial
    assert final==s.Matrix([2,1]) and final!=initial
    assert (initial.T*initial)[0]/2==(final.T*final)[0]/2==s.Rational(5,2)
    assert sum(initial)==sum(final)==3
    # Unequal calibration of the two roles does not intertwine the same swap.
    unequal=s.diag(1,2)
    assert swap*unequal*initial!=unequal*swap*initial
    # Energy preservation alone would also accept identity; the native reading
    # distinguishes identity from the required nontrivial exchange.
    assert initial!=final
    # Calibration is not selected: two common gains satisfy covariance while
    # scaling momenta and preparation energy. Nothing creates this energy.
    for k in (s.Integer(1),s.Integer(2)):
        assert swap*(k*initial)==k*final
    assert ((2*initial).T*(2*initial))[0]==4*(initial.T*initial)[0]
    paths=['research/nima/agda/NativeFeedbackRouteReadout.agda',
           'research/nima/agda/TriangleComparisonFeedbackRegression.agda',
           'research/nima/native-feedback-change-permission.md',
           'research/nima/exchange-to-mechanical-recoil.md',
           'research/nima/seed-port-exchange-binding.md',
           str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','disposition':'conditional_native_observer_action_and_involution_face_binding',
            'native_premise':'reading(exchange(c))=swap(reading(c)); existing actual native source theorem, not rerun',
            'attachment':'Phi(c)=mechanical_mass_map * gain * reading(c), gain>0',
            'general_symbolic_intertwining':True,'twice_exchange_face_preserved':True,
            'fixture':{'initial':[1,2],'after_exchange':[2,1],'after_two':[1,2],
                       'mass_pair':[1,1],'gain':1,'momentum_sum':3,'kinetic_energy':'5/2'},
            'controls':['unequal role calibration rejected','identity effect differs from native source reading',
                        'common gain freedom retained; energy scales quadratically'],
            'scope':'Observation-level conditional attachment to one exchange port. Full native histories stay in the existing Observed record; counts are not faithful histories. No six-port schedule, laboratory units, source-selected coupling or universal domain theorem.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/strominger/results/native-feedback-elastic-binding/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
