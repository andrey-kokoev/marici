"""Normalization-block regressions for strict versus derived certificates.
Standard library, no coefficient truncation, not compiled Rzk code.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

# Polynomials stored by coefficient sequence; multiplication is untruncated.
def norm(p):
    p=list(p)
    while p and not p[-1]:p.pop()
    return tuple(p)
def add(p,q):return norm([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q)))])
def neg(p):return tuple(-x for x in p)
def mul(p,q):
    if not p or not q:return ()
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return norm(r)
def val(p):return p[0] if p else 0
def tail(p):return add(p,(-val(p),))
def pairadd(a,b):return (add(a[0],b[0]),add(a[1],b[1]))
def pairneg(a):return (neg(a[0]),neg(a[1]))
def action(a,s):return (mul(a[0],s[0]),mul(a[1],s[1]))
def node(a):assert val(a[0])==val(a[1]);return a
def nu(a):return node(a)  # canonical inclusion A into normalization pairs
def p2(a):node(a);return val(a[0])
def p1(s):return (val(s[0]),val(s[1]))
def h(s):return node((tail(s[0]),tail(s[1])))
def j2(c):return (norm((c,)),norm((c,)))
def j1(c):return (norm((c[0],)),norm((c[1],)))
def isJ(s):return val(s[0])==val(s[1])==0

zero=((),());one=((1,),(1,));x=((0,1),());y=((),(0,1))
sheet=((1,),())
# Explicit counterexample to A-linearity of the ambient positive-tail homotopy.
assert h(sheet)==zero
assert h(action(x,sheet))==x
assert action(x,h(sheet))==zero and x!=zero
# Constant inclusion also fails A-linearity (x acts by zero on the target).
assert action(x,j1((1,0)))!=j1((0,0))

count=0
for degree in range(1,13):
    xp=(0,)*degree+(2,);yp=(0,)*degree+(-3,)
    s=(add((1,),xp),add((-2,),yp))
    a=node((add((4,),xp),add((4,),yp)))
    # p d = d p on A, where target differential is the diagonal.
    assert p1(nu(a))==(p2(a),p2(a))
    # dh+hd=1-jp in degrees 1 and 2; no road coordinates enter this block.
    assert nu(h(s))==pairadd(s,pairneg(j1(p1(s))))
    assert h(nu(a))==pairadd(a,pairneg(j2(p2(a))))
    assert p1(j1(p1(s)))==p1(s) and p2(j2(p2(a)))==p2(a)
    # p1 and p2 are A-linear for the target conductor action.
    assert p1(action(a,s))==tuple(p2(a)*c for c in p1(s))
    assert p2(action(a,one))==p2(a)*p2(one)
    k=h(s);assert isJ(k)
    # On ker p, differential and inverse contraction are BOTH identity on J.
    assert nu(k)==k and h(nu(k))==k
    assert isJ(action(a,k)) and h(action(a,k))==action(a,h(k))
    # h has no component out of P2, so h squared is zero by degree.
    count+=1

# Kernel/readout problem versus relative normalization problem.
first=((1,),(1,));second=((1,1),(1,))
assert first!=second and p1(first)==p1(second)==(1,1)
assert nu(node(first))==first and nu(node(second))==second
# These are zero-road boundaries in the endpoint complex; neither has the
# nonzero sheet difference required by the primitive road unit.
assert all(p1(s)[0]-p1(s)[1]==0 for s in (first,second))

spec=Path('research/nima/rzk-coefficient-interface-v3.md')
result={'status':'passed','checked_at':datetime.now(timezone.utc).isoformat(),
'spec_sha256':hashlib.sha256(spec.read_bytes()).hexdigest(),
'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
'normalization_block':{'tested_branch_degrees':count,'polynomial_arithmetic':'untruncated integers','chain_comparison_and_R_linear_contraction':True,'kernel_identity_contraction':True},
'strict_certificate_control':{'ambient_h_A_linear':False,'witness':'h(x*(1,0))=x but x*h((1,0))=0','ambient_j_A_linear':False},
'derived_certificate_route':{'category':'D(A)','kernel':'[J --id--> J]','acyclicity_reason':'identity differential on identical A-modules','strict_ambient_splitting_required':False},
'branch_tests':{'kernel_readout_collision':True,'relative_quotient_both_boundaries':True,'neither_is_primitive_road_unit':True},
'nonverification':['No formal Rzk compilation or full certificate validator','No full road/D3/geometric source checker rerun','No unrestricted physical or filtered equivalence inferred from samples']}
Path('research/nima/results/rzk_coefficient_interface_v3.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
