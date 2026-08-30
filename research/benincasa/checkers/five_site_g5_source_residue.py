import json,math
from fractions import Fraction as F
from pathlib import Path

from five_site_disjoint_mixed_pair_real_branches import roots_interval,K
from five_site_g5_cm_domain import landau,pfun

cm=json.loads(Path('research/benincasa/results/five-site-g5-cm-domain.json').read_text())
src=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
x=cm['x']; t=-x**.5
valid=next(a for a in cm['assignments'] if a['all_triangle_inequalities'] and a['all_2x2_gram_minors_nonnegative'])
a,b,c=valid['a'],valid['b'],cm['c']
P=[(math.cos(2*math.pi*k/5),math.sin(2*math.pi*k/5),1.0) for k in range(5)]
C=[(0.,0.,0.)]
for k in range(4):C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda u,v:sum(q*r for q,r in zip(u,v))
sub=lambda u,v:tuple(q-r for q,r in zip(u,v))
norm=lambda u:dot(u,u)**.5
v3,v4=C[3],C[4]
rhs=[(c*c+dot(v3,v3)-a*a)/2,(c*c+dot(v4,v4)-b*b)/2]
gram=[[dot(v3,v3),dot(v3,v4)],[dot(v3,v4),dot(v4,v4)]]
det=gram[0][0]*gram[1][1]-gram[0][1]**2
coef=[(rhs[0]*gram[1][1]-rhs[1]*gram[0][1])/det,(gram[0][0]*rhs[1]-gram[0][1]*rhs[0])/det]
l0=tuple(coef[0]*v3[j]+coef[1]*v4[j] for j in range(3))
cross=(v3[1]*v4[2]-v3[2]*v4[1],v3[2]*v4[0]-v3[0]*v4[2],v3[0]*v4[1]-v3[1]*v4[0])
nh=norm(cross); n=tuple(q/nh for q in cross); height=(c*c-dot(l0,l0))**.5

def cuts(label):
    sites={int(q)-1 for q in label[2:]}
    return [e for e in range(5) if (e in sites)!=((e+1)%5 in sites)]
def wall(label,y):
    if label=='G':return 5*t
    if label.startswith('G_minus_e'):
        edge=int(label[-2])-1
        return 5*t+2*y[edge]
    return len(label[2:])*t+sum(y[e] for e in cuts(label))

records=[]
for sheet in [-1,1]:
    l=tuple(l0[j]+sheet*height*n[j] for j in range(3)); y=[norm(sub(l,q)) for q in C]
    assert abs(wall('G_minus_e12',y))<1e-8 and abs(wall('g_5',y))<1e-8
    common=[q for q in src['common_prefactor'] if q!='g_5']
    terms=[]
    for term in src['terms']:
        if 'G_minus_e12' not in term:continue
        rem=[q for q in term if q!='G_minus_e12']
        value=1.0
        vals={q:wall(q,y) for q in common+rem}
        for z in vals.values():value/=z
        terms.append({'remaining':rem,'value':value,'walls':vals})
    total=sum(q['value'] for q in terms)/2 # source double-residue Jacobian
    records.append({'sheet':sheet,'loop_point':l,'edge_energies':y,'term_count':len(terms),
                    'residue_sum':total,'minimum_remaining_wall_abs':min(abs(v) for q in terms for v in q['walls'].values())})

class I:
    def __init__(self,l,h=None):self.l,self.h=F(l),F(l if h is None else h);assert self.l<=self.h
    def __add__(self,o):o=ii(o);return I(self.l+o.l,self.h+o.h)
    __radd__=__add__
    def __neg__(self):return I(-self.h,-self.l)
    def __sub__(self,o):return self+(-ii(o))
    def __rsub__(self,o):return ii(o)-self
    def __mul__(self,o):
        o=ii(o);v=[self.l*o.l,self.l*o.h,self.h*o.l,self.h*o.h];return I(min(v),max(v))
    __rmul__=__mul__
    def inv(self):assert not self.l<=0<=self.h;return I(min(1/self.l,1/self.h),max(1/self.l,1/self.h))
    def __truediv__(self,o):return self*ii(o).inv()
def ii(x):return x if isinstance(x,I) else I(x)
def sqrti(q):
    assert q.l>0
    lo=F(str(math.sqrt(float(q.l))-1e-13)); hi=F(str(math.sqrt(float(q.h))+1e-13))
    assert lo*lo<=q.l and hi*hi>=q.h
    return I(lo,hi)
def ki(z,s5):return I(z.a)+I(z.b)*s5
def poleval(poly,x,s5):
    out=I(0)
    for c0 in reversed(poly):out=out*x+ki(c0,s5)
    return out
def ivecadd(u,v):return tuple(a0+b0 for a0,b0 in zip(u,v))
def ivecscale(a0,u):return tuple(a0*q for q in u)
def idot(u,v):return sum((a0*b0 for a0,b0 in zip(u,v)),I(0))

s5=I(F(2236067977499789,10**15),F(2236067977499790,10**15));assert s5.l*s5.l<5<s5.h*s5.h
xi=I(F(str(x-1e-10)),F(str(x+1e-10)));assert roots_interval(landau,xi.l,xi.h)==1
pi=poleval(pfun.n,xi,s5)/poleval(pfun.d,xi,s5)
si=sqrti(xi); di=sqrti(xi-I(4)*pi); ai=(si-di)/2; bi=(si+di)/2; ci=I(F(5,2))*si
c72=(s5-I(1))/4; c144=-(s5+I(1))/4
s72=sqrti(I(10)+I(2)*s5)/4; s144=sqrti(I(10)-I(2)*s5)/4
PI=[(I(1),I(0),I(1)),(c72,s72,I(1)),(c144,s144,I(1)),(c144,-s144,I(1)),(c72,-s72,I(1))]
CI=[(I(0),I(0),I(0))]
for k0 in range(4):CI.append(ivecadd(CI[-1],PI[k0]))
V3,V4=CI[3],CI[4]; rr=[(ci*ci+idot(V3,V3)-ai*ai)/2,(ci*ci+idot(V4,V4)-bi*bi)/2]
gg=[[idot(V3,V3),idot(V3,V4)],[idot(V3,V4),idot(V4,V4)]]; dd=gg[0][0]*gg[1][1]-gg[0][1]*gg[0][1]
cc=[(rr[0]*gg[1][1]-rr[1]*gg[0][1])/dd,(gg[0][0]*rr[1]-gg[0][1]*rr[0])/dd]
L0=ivecadd(ivecscale(cc[0],V3),ivecscale(cc[1],V4))
CR=(V3[1]*V4[2]-V3[2]*V4[1],V3[2]*V4[0]-V3[0]*V4[2],V3[0]*V4[1]-V3[1]*V4[0]); NH=sqrti(idot(CR,CR)); NN=tuple(q/NH for q in CR)
HH=sqrti(ci*ci-idot(L0,L0)); exact=[]; support_separation=[]
def iwall(label,y):
    if label=='G':return I(5)*(-si)
    if label.startswith('G_minus_e'):return I(5)*(-si)+I(2)*y[int(label[-2])-1]
    return I(len(label[2:]))*(-si)+sum((y[e] for e in cuts(label)),I(0))
for sheet in [-1,1]:
    LL=ivecadd(L0,ivecscale(I(sheet)*HH,NN)); YY=[sqrti(idot(tuple(a0-b0 for a0,b0 in zip(LL,q)),tuple(a0-b0 for a0,b0 in zip(LL,q)))) for q in CI]
    labelled_walls=sorted(set(src['common_prefactor']+sum(src['terms'],[]))-{'g_5','G_minus_e12'})
    wall_intervals={q:[str(iwall(q,YY).l),str(iwall(q,YY).h)] for q in labelled_walls}
    assert all(not F(lo)<=0<=F(hi) for lo,hi in wall_intervals.values())
    edge_intervals=[[str(z.l),str(z.h)] for z in YY]
    assert all(z.l>0 for z in YY)
    support_separation.append({'sheet':sheet,'remaining_wall_intervals':wall_intervals,
        'remaining_walls_certified_nonzero':True,'edge_energy_intervals':edge_intervals,
        'all_edge_energies_certified_positive':True})
    total=I(0)
    for term in src['terms']:
        if 'G_minus_e12' not in term:continue
        vals=[iwall(q,YY) for q in [z for z in src['common_prefactor'] if z!='g_5']+[z for z in term if z!='G_minus_e12']]
        value=I(1)
        for z in vals:value=value/z
        total=total+value
    total=total/2
    exact.append({'sheet':sheet,'residue_interval':[str(total.l),str(total.h)],'certified_nonzero':not total.l<=0<=total.h})
assert all(q['certified_nonzero'] for q in exact)
packet={'schema':'marici.five_site_g5_source_residue.v1','records':records,
        'exact_interval_certificates':exact,
        'support_separation_certificates':support_separation,
        'precision':'exact rational interval certificate plus f64 coordinates'}
Path('research/benincasa/results/five-site-g5-source-residue.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
