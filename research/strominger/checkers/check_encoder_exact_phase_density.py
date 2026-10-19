"""Exact arithmetic controls for a dense software bank-phase vocabulary.

The density/completion argument is written in the companion note; finite samples
are regression tests, not the proof of density. Uses the source arithmetic field
Q(sqrt(2), i sqrt(3)) through its existing operations, restricted to rational t.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_witnessed_interface_compiler import ROOT, BASE, rat, mm, tr, blockdiag, enc, rank
from check_coupled_six_piece_belt import R, Z, ONE, add, mul, conj, scale, norm


def phase(t):
    d = 1+3*t*t
    return (R((1-3*t*t)/d), R(2*t/d))


def main():
    paths = {
        'source':BASE/'results/neutron-seam-control-transport.json',
        'memory':BASE/'results/neutron-comparison-memory.json',
        'orbit':BASE/'results/encoder-conjugated-bank-controls.json',
        'lie':BASE/'results/encoder-rank-one-controllability.json',
    }
    raw = {k:p.read_bytes() for k,p in paths.items()}
    data = {k:json.loads(v) for k,v in raw.items()}
    for key in ('orbit','lie'):
        assert data[key]['status']=='pass'
        for p,digest in data[key]['source_hashes'].items():
            assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest,p
    source = data['source']
    item = next(x for x in source['source_pulses'] if x['frame']==0)
    P = blockdiag(rat(item['projector']),[[F(0)]*21 for _ in range(21)])
    metric = blockdiag(rat(source['metric']),rat(data['memory']['memory_metric']))
    assert mm(P,P)==P and mm(tr(P),metric)==mm(metric,P) and rank(P)==1
    def action(state,z):
        alpha = add(z,scale(-1,ONE))
        image = []
        for row in P:
            q = Z
            for a,x in zip(row,state):
                if a:
                    q = add(q,scale(a,x))
            image.append(q)
        return [add(x,mul(alpha,y)) for x,y in zip(state,image)]
    ts = sorted({F(m,2**n) for n in range(5) for m in range(-8,9)})
    phases = [phase(t) for t in ts]+[(R(-1),R())]
    for z in phases:
        assert norm(z)==R(1)
        alpha=add(z,scale(-1,ONE))
        # Coefficient of P in U^sharp U-I, valid on every complex input.
        assert add(add(alpha,conj(alpha)),(norm(alpha),R()))==Z
        for j in range(45):
            v=[Z]*45
            v[j]=ONE
            assert action(action(v,z),conj(z))==v
    for t in ts:
        assert phase(-t)==conj(phase(t))
    for t in ts:
        for s in (F(0),F(1,3),F(-2),F(7,8)):
            delta=add(phase(t),scale(-1,phase(s)))
            exact=12*(t-s)**2/((1+3*t*t)*(1+3*s*s))
            assert norm(delta)==R(exact)
            assert exact<=16*(t-s)**2
    # Exact arbitrary-n polynomial identity certificate: the numerator of
    # |z(t)-z(s)|^2 reduces to 12(t-s)^2(1+3t^2)(1+3s^2).
    # Implement sparse bivariate polynomials with rational coefficients.
    def plus(a,b):
        out=dict(a)
        for k,v in b.items():out[k]=out.get(k,F(0))+v
        return {k:v for k,v in out.items() if v}
    def times(a,b):
        out={}
        for (i,j),x in a.items():
            for (k,l),y in b.items():
                key=(i+k,j+l);out[key]=out.get(key,F(0))+x*y
        return {k:v for k,v in out.items() if v}
    def scaled(c,a):return {k:c*v for k,v in a.items() if c*v}
    dt={(0,0):F(1),(2,0):F(3)}
    ds={(0,0):F(1),(0,2):F(3)}
    realdiff=plus(times({(0,0):F(1),(2,0):F(-3)},ds),scaled(-1,times({(0,0):F(1),(0,2):F(-3)},dt)))
    imagdiff=plus(times({(1,0):F(2)},ds),scaled(-1,times({(0,1):F(2)},dt)))
    lhs=plus(times(realdiff,realdiff),scaled(3,times(imagdiff,imagdiff)))
    diff={(1,0):F(1),(0,1):F(-1)}
    rhs=scaled(12,times(times(diff,diff),times(dt,ds)))
    assert lhs==rhs
    # A bounded-parameter vocabulary is NOT dense as SINGLE phases: |t|<=1 stays distance >=1
    # from -1, since |z(t)+1|^2=4/(1+3t^2). Appending -1 alone does not fill
    # the omitted open arcs. This hostile concerns direct phase approximation,
    # NOT products: products of phases from the arc can cover the circle.
    for t in ts:
        if abs(t)<=1:
            assert norm(add(phase(t),ONE))==R(4/(1+3*t*t))
            assert 4/(1+3*t*t)>=1
    hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(raw[k]).hexdigest() for k,p in paths.items()}
    own=Path(__file__).resolve()
    hashes[own.relative_to(ROOT).as_posix()]=hashlib.sha256(own.read_bytes()).hexdigest()
    for p,digest in hashes.items():
        assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest
    report={
        'status':'pass','bank_label':item['label'],'frame':0,
        'phase_formula':'(1-3t^2)/(1+3t^2) + i sqrt(3) 2t/(1+3t^2)',
        'parameter_vocabulary':'all dyadic rationals, plus the exact phase -1',
        'tested_phases':len(phases),'basis_inverse_tests':45*len(phases),
        'general_polynomial_distance_identity_verified':True,
        'distance_bound':'|z(t)-z(s)| <= 4|t-s|',
        'unitarity':'exact on all inputs by projector algebra and exact phase norm',
        'dense_word_enumeration':'At stage n>=1: |m|<=n*2^n, t=m/2^n, and all primitive words of length<=n over those bank phases, -1, seam/write reflections, R and R^-1.',
        'bounded_single_phase_parameter_hostile_detected':True,
        'source_hashes':hashes,
        'scope':'Exact phase arithmetic and source-projector tests plus the written density theorem. Not a polar evaluator, compiler, formal kernel theorem, gate-count bound, or hardware control admission.'}
    (BASE/'results/encoder-exact-phase-density.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','tested_phases','basis_inverse_tests','general_polynomial_distance_identity_verified']}))


if __name__=='__main__':
    main()
