import json, math
from fractions import Fraction as F
from pathlib import Path

src = json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())['five_cycle']
P = [(math.cos(2*math.pi*k/5), math.sin(2*math.pi*k/5), 1.0) for k in range(5)]
C = [(0.0,0.0,0.0)]
for k in range(4):
    C.append(tuple(C[-1][j]+P[k][j] for j in range(3)))
dot=lambda u,v:sum(a*b for a,b in zip(u,v))
y=[math.sqrt(dot(q,q)) for q in C] # loop point l=C_0
X5=-(y[3]+y[4])
X=[-X5/4]*4+[X5]
assert abs(sum(X))<1e-12 and y[0]==0

def cuts(sites):
    return [e for e in range(5) if (e in sites) != ((e+1)%5 in sites)]
def wall(label):
    if label=='G': return sum(X)
    if label.startswith('G_minus_e'):
        return sum(X)+2*y[int(label[-2])-1]
    sites={int(c)-1 for c in label[2:]}
    return sum(X[i] for i in sites)+sum(y[e] for e in cuts(sites))

assert abs(wall('G'))<1e-12
assert abs(wall('G_minus_e12'))<1e-12
assert abs(wall('g_5'))<1e-12
common=[q for q in src['common_prefactor'] if q not in {'G','g_5'}]
terms=[]
for term in src['terms']:
    if 'G_minus_e12' not in term: continue
    rem=[q for q in term if q!='G_minus_e12']
    vals={q:wall(q) for q in common+rem}
    terms.append({'remaining':rem,'minimum_abs':min(abs(z) for z in vals.values()),
                  'value':math.prod(1/z for z in vals.values())})
assert len(terms)==26
minimum=min(q['minimum_abs'] for q in terms)
total=sum(q['value'] for q in terms)/2

class I:
    def __init__(self,l,h=None):
        self.l,self.h=F(l),F(l if h is None else h); assert self.l<=self.h
    def __add__(self,o):o=ii(o);return I(self.l+o.l,self.h+o.h)
    __radd__=__add__
    def __neg__(self):return I(-self.h,-self.l)
    def __sub__(self,o):return self+(-ii(o))
    def __rsub__(self,o):return ii(o)-self
    def __mul__(self,o):
        o=ii(o);v=(self.l*o.l,self.l*o.h,self.h*o.l,self.h*o.h);return I(min(v),max(v))
    __rmul__=__mul__
    def inv(self):
        assert not self.l<=0<=self.h
        return I(min(1/self.l,1/self.h),max(1/self.l,1/self.h))
    def __truediv__(self,o):return self*ii(o).inv()
def ii(x):return x if isinstance(x,I) else I(x)
def sqrti(q):
    assert q.l>0
    lo=F(str(math.sqrt(float(q.l))-1e-13));hi=F(str(math.sqrt(float(q.h))+1e-13))
    assert lo*lo<=q.l and hi*hi>=q.h
    return I(lo,hi)

s5=I(F(2236067977499789,10**15),F(2236067977499790,10**15))
assert s5.l*s5.l<5<s5.h*s5.h
yi=[I(0),sqrti(I(2)),sqrti((I(11)+s5)/2),sqrti((I(21)+s5)/2),sqrti(I(17))]
x5=-(yi[3]+yi[4]);xi=[-x5/4]*4+[x5]
def iwall(label):
    if label=='G':return sum(xi,I(0))
    if label.startswith('G_minus_e'):return sum(xi,I(0))+2*yi[int(label[-2])-1]
    sites={int(c)-1 for c in label[2:]}
    return sum((xi[i] for i in sites),I(0))+sum((yi[e] for e in cuts(sites)),I(0))
itotal=I(0); certified_walls={}
for term in src['terms']:
    if 'G_minus_e12' not in term:continue
    labels=common+[q for q in term if q!='G_minus_e12']
    value=I(1)
    for q in labels:
        z=iwall(q);assert not z.l<=0<=z.h
        certified_walls[q]=[str(z.l),str(z.h)];value=value/z
    itotal=itotal+value
itotal=itotal/2
assert not itotal.l<=0<=itotal.h
packet={'schema':'marici.five_site_g5_total_soft_source_coefficient.discovery.v1',
        'energy_specialization':X,'edge_distances':y,'term_count':len(terms),
        'minimum_remaining_wall_abs':minimum,'triple_residue_coefficient':total,
        'discovery_nonzero':abs(total)>1e-10,
        'exact_residue_interval':[str(itotal.l),str(itotal.h)],
        'exact_certified_nonzero':True,
        'exact_remaining_walls_certified_nonzero':True,
        'certified_wall_count':len(certified_walls),
        'precision':'exact rational interval certificate plus f64 discovery'}
Path('research/benincasa/results/five-site-g5-total-soft-source-coefficient.json').write_text(
    json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
