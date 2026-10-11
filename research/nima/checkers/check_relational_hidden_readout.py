"""Root-relative reference decomposition of the existing hidden return.

This is a readout/attachment audit, not a new state-dependent evolution law.
The actual filled Boolean fixtures have flat edge-action triangles.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
from check_four_packet_cycle import UNIT,E2,J,matrix
from check_four_packet_record_feedback import mm,transpose
ROOT=Path(__file__).resolve().parents[1]
I=matrix(UNIT);X=matrix(E2);j=matrix(J)


def mul(*args):
    out=I
    for a in args:out=mm(out,a)
    return out


def inv(a):
    (p,q),(r,s)=a;det=p*s-q*r
    assert det!=0
    return ((s/det,-q/det),(-r/det,p/det))


def half(a):return tuple(tuple(x/2 for x in row) for row in a)

def trace(a):return a[0][0]+a[1][1]


def rooted(u,v,d,j1,j2):
    a=mul(inv(u),j1,u)
    b=mul(inv(d),j2,d)
    h=mul(inv(d),v,u)
    original=half(mul(inv(d),j2,v,inv(j1),u))
    relative=half(mul(b,h,inv(a)))
    assert original==relative
    return a,b,h,relative


def main():
    fixtures=(('ordinary_fixed_reference',I,I,I,j,j,F(1)),
              ('twisted_fixed_reference',X,X,I,j,j,F(-1)),
              ('twisted_transported_reference',X,X,I,mul(X,j,X),j,F(1)))
    reports=[];checks=0
    for name,u,v,d,j1,j2,expected_trace in fixtures:
        a,b,h,result=rooted(u,v,d,j1,j2)
        assert h==I and trace(result)==expected_trace
        for bits in product((0,1),repeat=3):
            g0,g1,g2=(X if bit else I for bit in bits)
            up=mul(g1,u,inv(g0));vp=mul(g2,v,inv(g1));dp=mul(g2,d,inv(g0))
            jp1=mul(g1,j1,inv(g1));jp2=mul(g2,j2,inv(g2))
            ap,bp,hp,rp=rooted(up,vp,dp,jp1,jp2)
            assert ap==mul(g0,a,inv(g0)) and bp==mul(g0,b,inv(g0))
            assert hp==mul(g0,h,inv(g0)) and rp==mul(g0,result,inv(g0))
            assert trace(rp)==expected_trace
            checks+=1
        reports.append(dict(name=name,root_reference_relation='equal' if a==b else 'opposite',
                            closed_trace=str(trace(result))))
    # Same-root reference attachment, using the same two paths as the readout.
    # For these flat triangles it must give baseline, not a hidden response.
    for u,v,d in ((I,I,I),(X,X,I),(X,I,X),(I,X,X)):
        j1=mul(u,j,inv(u));j2=mul(d,j,inv(d))
        a,b,h,r=rooted(u,v,d,j1,j2)
        assert a==b==j and h==I and r==half(I)
    # Algebraic nonflat control: NOT an admitted filled tetrahedral fixture.
    h=((F(2),F(0)),(F(0),F(1)))
    a,b,H,r=rooted(I,h,I,j,j)
    assert H==h and r==half(mul(j,h,inv(j))) and r!=half(I)
    result=dict(schema='marici.nima.relational-hidden-readout.v1',status='pass',
        definitions={'A':'u01^-1 J1 u01','B':'d02^-1 J2 d02','H':'d02^-1 u12 u01'},
        root_return='b0 = (1/2) B H A^-1',
        frame_law='A,B,H,b0 all conjugate by the root frame G0; trace(b0) is invariant',
        covariance_checks=checks,fixtures=reports,
        same_root_attachment='J1=u01 J0 u01^-1 and J2=d02 J0 d02^-1 imply A=B=J0. Then b0=(1/2)J0 H J0^-1; for flat H=I this is I/2.',
        disposition='The prior +/- responses can be distinguished relationally when references are included in the state: they have equal versus opposite transported root references. Mere passive changes of a complete reference-bearing state do not alter its trace. Same-root attachment along a flat triangle yields no extra hidden signal.',
        limits='References and their preparation/attachment remain supplied data. This does not select independent references, physicalize the trace, prove a higher-filler equivalence or verify budget conservation for a new state-dependent mixer. Nonflat matrix control is not a filled tetrahedral source.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'recovered-reference-return-response-chain.md','co-constructed-seam-reference-hypothesis.md',
            'checkers/check_four_packet_cycle.py','checkers/check_relational_hidden_readout.py')})
    (ROOT/'results/relational-hidden-readout.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
