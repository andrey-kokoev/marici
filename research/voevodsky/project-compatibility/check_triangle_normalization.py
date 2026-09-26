"""Exact source-normalization and canonical simplex degeneration audit.
Polynomial identities only; no claim of physical chain specialization.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import hashlib,json

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
N=6 # E,a,b,r,s,t
ZERO=(0,)*N

def tidy(p): return {k:F(v) for k,v in p.items() if v}
def const(v): return tidy({ZERO:v})
def var(i):
    k=list(ZERO);k[i]=1
    return {tuple(k):F(1)}
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():out[k]=out.get(k,0)+v
    return tidy(out)
def scale(v,p):return tidy({k:F(v)*w for k,w in p.items()})
def mul(*ps):
    out=const(1)
    for p in ps:
        ans={}
        for k,v in out.items():
            for l,w in p.items():
                q=tuple(a+b for a,b in zip(k,l));ans[q]=ans.get(q,0)+v*w
        out=tidy(ans)
    return out
def sq(p):return mul(p,p)
def det(matrix):
    out={};n=len(matrix)
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        out=add(out,scale((-1)**inversions,mul(*(matrix[i][perm[i]] for i in range(n)))))
    return out
def at_E_zero(p):return {k:v for k,v in p.items() if k[0]==0}
def leading_E(p):
    degree=min(k[0] for k in p)
    return degree,{(0,)+k[1:]:v for k,v in p.items() if k[0]==degree}
def eq(p,q):return not add(p,scale(-1,q))

paths=[HERE/'check_triangle_normalization.py']+[ROOT/'temp/arxiv-2408.16386-source/sections'/s
    for s in ('applications.tex','method.tex','cosmologicalintegrals.tex')]
def inventory():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=inventory()
assert before['temp/arxiv-2408.16386-source/sections/applications.tex']=='3e92460fe2e34dc21a537c784dab3b2fbcd9b7cfee9e7372f06971b50d8b6f9b'
E,a,b,r,s,t=[var(i) for i in range(N)]
c=add(E,scale(-1,a),scale(-1,b))
one=const(1);zero={}
# D = squared external triangle area, H=16D.
H=mul(E,add(E,scale(-2,a)),add(E,scale(-2,b)),add(scale(2,a),scale(2,b),scale(-1,E)))
cm=[[zero,one,one,one],[one,zero,sq(a),sq(b)],
    [one,sq(a),zero,sq(c)],[one,sq(b),sq(c),zero]]
assert eq(scale(-1,det(cm)),H)
order,leading=leading_E(H)
assert order==1 and eq(leading,scale(8,mul(a,b,add(a,b))))
# Doubled Gram matrix at a vertex: det(M)=8 det(Gram)=288 K.
G=add(sq(a),sq(b),scale(-1,sq(c)))
U=add(sq(a),sq(r),scale(-1,sq(s)))
V=add(sq(b),sq(r),scale(-1,sq(t)))
M=[[scale(2,sq(a)),G,U],[G,scale(2,sq(b)),V],[U,V,scale(2,sq(r))]]
detM=det(M)
B=add(mul(a,V),mul(b,U))
assert eq(at_E_zero(detM),scale(-2,sq(B))) # K_0=-B^2/144
Hface=add(scale(4,mul(sq(a),sq(r))),scale(-1,sq(U)))
C=add(scale(2,mul(sq(a),V)),scale(-1,mul(G,U)))
assert eq(scale(2,mul(sq(a),detM)),add(mul(H,Hface),scale(-1,sq(C))))
# Affine exponents in epsilon: gamma=-1/2+epsilon.
gamma=(F(-1,2),F(1))
c_volume=(F(1,2),F(0))
kappa_exponent=tuple(x-y for x,y in zip(c_volume,gamma))
assert kappa_exponent==(F(1),F(-1))
assert (kappa_exponent[0]-1,kappa_exponent[1])==(F(0),F(-1))
# Transverse coordinate C=sqrt(H*Hface)*z at fixed r,s.
# dC/dt=-4*a^2*t, hence r*s*t dr ds dt has positive density
# sqrt(H*Hface)/(16*a^2) d(r^2) d(s^2) dz (orientation reverses).
def derivative(p,i):
    out={}
    for k,v in p.items():
        if k[i]:
            q=list(k);q[i]-=1;out[tuple(q)]=v*k[i]
    return tidy(out)
assert eq(derivative(C,5),scale(-4,mul(sq(a),t)))
# kappa contributes H^(1-epsilon), K^gamma contributes H^gamma,
# the transverse Jacobian H^(1/2): the total H power is exactly one.
H_power=tuple(x+y+z for x,y,z in zip(kappa_exponent,gamma,(F(1,2),F(0))))
assert H_power==(F(1),F(0))
face_power=tuple(x+y for x,y in zip(gamma,(F(1,2),F(0))))
assert face_power==(F(0),F(1))
assert 288*2==576
# Noncollinear E0 fixture: a=b=3, r=4, s=t=5.
# These are loop-edge labels r=y12,s=y31,t=y23.
a0=b0=F(3);r0=F(4);s0=t0=F(5);c0=-a0-b0
q=[r0+a0+s0,r0+b0+t0,s0+c0+t0,
   a0+b0+s0+t0,b0+c0+r0+s0,c0+a0+r0+t0,r0,t0,s0]
assert all(v>0 for v in q)
assert before==inventory()
report={'passed':True,'source_sha256':before,'source_unchanged':True,
 'chart':'reduced-family continuation c=E-a-b; a,b fixed',
 'external_volume':{'H_equals_16D':'E(E-2a)(E-2b)(2a+2b-E)',
   'generic_E_order':1,'leading_H':'8ab(a+b)', 'excluded_intersections':'a*b*(a+b)=0'},
 'internal_volume':{'K_equals_detM_over':288,'B':'a*(b^2+r^2-t^2)+b*(a^2+r^2-s^2)',
   'K_at_E0':'-B^2/144','exact_schur_identity':'2*a^2*detM = H*Hface-C^2',
   'real_nonnegative_limit_necessary_condition':'B=0',
   'scope':'canonical simplex distances, up to edge relabeling; not an admitted analytic continuation of the physical chain'},
 'literal_source_exponents':{'gamma':'-1/2+epsilon','c_external_D_exponent':'1/2',
   'kappa_external_D_exponent':'1-epsilon','kappa_over_E_generic_order':'E^(-epsilon)',
   'conditions':'fixed generic regulator; local branch; reduced-family chart; other normalized factors regular and nonzero'},
 'transverse_patch':{'coordinate':'C=sqrt(H*Hface)*z; -1<z<1',
   'K':'H*Hface*(1-z^2)/(576*a^2)',
   'positive_measure_density':'sqrt(H*Hface)/(16*a^2) dR dS dz',
   'orientation':'dT/dz<0; positive density is not an oriented-chain identification',
   'total_H_power':1,'total_Hface_power':'epsilon',
   'normalized_local_density_order':'H/E tends to 8ab(a+b)',
   'integrability_condition':'Re(epsilon)>-1/2, fixed regular regulator',
   'scope':'compact patch Hface>0; remaining denominators bounded away from zero; literal printed normalization; candidate real representative only',
   'verification':'Jacobian derivative, affine powers and one noncollinear denominator fixture checked; local convergence proof is written in triangle-transverse-density.md'},
 'distinctions':['fixed-spatial-invariant continuation keeps D fixed and is a different map',
   'pointwise coefficient valuation is not the integrated period valuation',
   'the printed normalization is audited literally, not independently certified physically',
   'no epsilon removal or ordinary residue of the full twisted period is proved']}
(HERE/'triangle-normalization.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
