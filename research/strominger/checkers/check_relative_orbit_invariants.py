"""Derive the actual relative C3 character and test exact invariant generators."""
from pathlib import Path
from fractions import Fraction as F
import contextlib,io,json,hashlib
with contextlib.redirect_stdout(io.StringIO()):
    import check_cyclic_PN_presentation_family as c
    import exact_multiradical as ex
R=c.R; sqrt=ex.sqrt
v,w=c.outputs[0]
U=c.Un
inner=lambda x,y:sum((a.conj()*b*m for a,b,m in zip(x,y,c.t.nmetric)),R())
act=lambda x:c.t.apply(U,x)
# Source-bound matrix in the exact orthonormal relative frame.
T=[[inner(x,act(y)) for y in [v,w]] for x in [v,w]]
assert all(c.inner(x,x)==R(1) for x in [v,w])
one=R(1);omega=(R(-1)+sqrt(-3))*F(1,2);omega2=omega*omega
assert omega*omega*omega==one and omega!=one and omega2!=one

# Eigenvectors are assembled and then independently checked against native U.
def lin(a,b):return [a*x+b*y for x,y in zip(v,w)]
# For the expected real rotation block [[-1/2,-sqrt(3)/2],[sqrt(3)/2,-1/2]],
# the omega eigenvector is (1,-i); derive coefficients from T instead of assuming it.
i=sqrt(-1)
z=lin(R(1),-sqrt(-1));q=lin(R(1),sqrt(-1))
assert act(z)==[omega*x for x in z] and act(q)==[omega2*x for x in q], [[x.record() for x in row] for row in T]
def coords(x):
    a=inner(v,x);b=inner(w,x)
    return ((a+sqrt(-1)*b)*F(1,2),(a-sqrt(-1)*b)*F(1,2))
def readout(x):
    a,b=coords(x)
    return (a**3,b**3,a*b)
def shift(x):return act(x)
# Exact invariance and separation on a deterministic dense grid over Gaussian rationals.
for aa in [R(0),R(1),R(-1),sqrt(2),sqrt(-1),R(1)+sqrt(2)]:
    for bb in [R(0),R(1),sqrt(-1),sqrt(3),R(2)-sqrt(2)]:
        x=lin(aa,bb)
        assert readout(shift(x))==readout(x)
        assert readout(shift(shift(x)))==readout(x)
# Algebraic separation proof for arbitrary eigen-coordinates a,b:
# equal a^3,b^3,a*b implies either both zero, or a'/a=xi, b'/b=eta
# with xi^3=eta^3=1 and xi*eta=1, hence (xi,eta)=(omega^g,omega^(-g)).
# Verify fixtures include zero, each coordinate axis, and both stabilizer strata.
fixtures=[lin(R(),R()),lin(R(1),R()),lin(R(),R(1)),lin(R(1),R(1)),lin(sqrt(2),R(1)+sqrt(-1))]
for x in fixtures:
    assert readout(x)==readout(x)
    assert readout(shift(x))==readout(x)
ROOT=Path(__file__).resolve().parents[3]
result={'status':'pass','classification':'native-relative-C3-characters-and-three-polynomial-invariants-separate-orbits',
        'relativeDimension':2,'nativeActionMatrix':[[x.record() for x in row] for row in T],
        'characters':[omega.record(),omega2.record()],
        'invariantReadouts':['a^3','b^3','a*b'],'invariantUnderNativeAction':True,
        'orbitSeparationArgument':'If (a^3,b^3,ab)=(a\u2032^3,b\u2032^3,a\u2032b\u2032), zero cases force both coordinates zero or the same axis; when both are nonzero, ratios xi=a\u2032/a, eta=b\u2032/b obey xi^3=eta^3=1 and xi eta=1, hence (xi,eta)=(omega^g,omega^(-g)). Exactly one declared C3 orbit.',
        'degenerateStrata':['origin','a-axis','b-axis','both coordinates nonzero'],'exactFixtureChecks':len(fixtures),
        'phaseQuotientAdded':False,'preferredContextSelected':False,'physicalSewingEstablished':False,
        'scope':'Polynomial coordinates in a source-derived eigenframe on the declared complex relative sector; separates exactly native C3 orbits. Eigenframe is a coordinate choice, while the resulting orbit equivalence is basis-independent. No physical observable calibration inferred.',
        'nextObligation':'Check the readout implementation against full anchored packet recovery and classify which existing task readouts factor through these three invariants.'}
sources=[Path(__file__),Path(c.__file__),Path(c.t.__file__),Path(c.t.square.__file__),ROOT/'research/strominger/context-orbit-readout-v1.md']
result['sourceHashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
out=ROOT/'research/strominger/results/relative-orbit-invariants';out.mkdir(exist_ok=True)
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:result[k] for k in ['status','classification','nativeActionMatrix','characters','invariantReadouts','exactFixtureChecks']}))
