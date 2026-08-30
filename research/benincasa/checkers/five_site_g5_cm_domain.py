import json
from pathlib import Path

from five_site_disjoint_mixed_pair_real_branches import K,Q,cases,roots,cf,xeval,p_rat_penultimate,Rat,sign_on_isolated_root
from five_site_disjoint_mixed_pair_hessian import add,scale,mul,sub,resultant

# The exact sign machinery is inherited from the certified RUR/Sturm checker.
label,m,dei,dej,dij=next(c for c in cases if c[0]=='g_5')
mm=K(m*m); A=dei+dej; delta=dei-dej; B=K(Q(25,2)+m*m); X=[K(),K(1)]
C=add(scale(X,B),[-A]); R=add([dei],scale(X,K(-Q(25,2))))
f=[scale(mul(X,mul(X,sub(scale(X,mm),[dij]))),K(-25*m*m)),scale(mul(C,C),K(4)),scale(C,K(-16)),[K(16)]]
g=[scale(mul(X,sub([delta*delta],mul(R,R))),mm),add(scale(mul(X,R),K(-4*m*m)),scale(mul(R,R),K(4))),add(scale(X,K(-4*m*m)),scale(R,K(16))),[K(16)]]
raw=resultant(f,g); landau=raw[next(i for i,z in enumerate(raw) if z.nz()):]
lin=p_rat_penultimate(f,g); pfun=Rat([K(-1)])*lin[0]/lin[1]

# Select the unique positive g5 root with positive p and same-sign multipliers.
xroots=sorted(z.real for z in roots([cf(z) for z in landau]) if abs(z.imag)<1e-7 and z.real>0)
x=xroots[2]; p=xeval(pfun.n,x)/xeval(pfun.d,x)
s=x**.5; c=2.5*s; disc=(x-4*p)**.5
ys=[(s-disc)/2,(s+disc)/2]

def gram(a,b):
    u=(a*a+c*c-cf(dei))/(2*a*c)
    v=(b*b+c*c-cf(dej))/(2*b*c)
    w=(a*a+b*b-cf(dij))/(2*a*b)
    det=1+2*u*v*w-u*u-v*v-w*w
    triangles=[abs(a-c)<=cf(dei)**.5<=a+c,abs(b-c)<=cf(dej)**.5<=b+c,abs(a-b)<=cf(dij)**.5<=a+b]
    return {'a':a,'b':b,'dot_ei':u,'dot_ej':v,'dot_ij':w,'gram_det':det,
            'triangle_inequalities':triangles,'all_triangle_inequalities':all(triangles),
            'all_2x2_gram_minors_nonnegative':all(1-z*z>=-1e-9 for z in (u,v,w))}

assignments=[gram(ys[0],ys[1]),gram(ys[1],ys[0])]

XR=Rat(X); z2=XR*(XR-Rat([K(4)])*pfun)
class Quad:
    def __init__(self,a=Rat(),b=Rat()):self.a,self.b=a,b
    def __add__(self,o):o=qq(o);return Quad(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Quad(-self.a,-self.b)
    def __sub__(self,o):return self+(-qq(o))
    def __mul__(self,o):
        o=qq(o);return Quad(self.a*o.a+self.b*o.b*z2,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
def qq(o):return o if isinstance(o,Quad) else Quad(o if isinstance(o,Rat) else Rat([K(o)]))
def rfloat(r):return xeval(r.n,x)/xeval(r.d,x)
def qsign(q):
    norm=q.a*q.a-q.b*q.b*z2
    ns=sign_on_isolated_root(landau,x,norm.n)*sign_on_isolated_root(landau,x,norm.d)
    assert ns!=0
    value=rfloat(q.a)+(x*(x-4*p))**.5*rfloat(q.b)
    assert abs(value)>1e-8
    return 1 if value>0 else -1
half=Rat([K(Q(1,2))]);
base=(XR-Rat([K(2)])*pfun)*half
def exact_assignment(zsign):
    a2=Quad(base,Rat([K(Q(zsign,2))])); b2=Quad(base,Rat([K(Q(-zsign,2))]))
    c2=Quad(XR*Rat([K(Q(25,4))]));
    gab=(a2+b2-Quad(Rat([dij])))*half
    gac=(a2+c2-Quad(Rat([dei])))*half
    gbc=(b2+c2-Quad(Rat([dej])))*half
    mab=a2*b2-gab*gab; mac=a2*c2-gac*gac; mbc=b2*c2-gbc*gbc
    det=a2*b2*c2+Quad(Rat([K(2)]))*gab*gac*gbc-a2*gbc*gbc-b2*gac*gac-c2*gab*gab
    signs=[qsign(q) for q in (a2,b2,c2,mab,mac,mbc,det)]
    return {'z_sign':zsign,'exact_principal_minor_signs':signs,
            'inside_open_cm_domain':all(s>0 for s in signs)}
exact=[exact_assignment(-1),exact_assignment(1)]
packet={'schema':'marici.five_site_g5_cm_domain.v1','x':x,'p':p,'c':c,
        'assignments':assignments,'exact_quadratic_extension_assignments':exact,
        'precision':'all Gram-principal-minor signs exact by Q(sqrt(5))(x) norm certificates; coordinates f64'}
Path('research/benincasa/results/five-site-g5-cm-domain.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
