"""Actual six-event, two-feature witness for the adjacent cubic attachment."""
from pathlib import Path
from collections import defaultdict
from itertools import combinations,product
import runpy,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
f=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))
rel,mul,D,record,clean=(f[k] for k in ('relation','multiply','derivative','record','clean'))
def ordered(start,column,r):
    out=defaultdict(int)
    for (word,marks),coef in column.items():
        states=[start]
        for p in word:states.append(states[-1]|(1<<p))
        for positions in combinations(range(len(word)),r):
            seams=tuple(('e',states[i],states[i+1],marks[i]) for i in positions)
            cuts=(-1,)+positions+(len(word),)
            buffers=[record(states[a+1],word[a+1:b],marks[a+1:b]) for a,b in zip(cuts,cuts[1:])]
            for entries in product(*(b.items() for b in buffers)):
                c=coef
                for _,v in entries:c*=v
                out[seams,tuple(k for k,_ in entries)]+=c
    return clean(out)
def one(column):
    return {((('e',x,y,k),),(u,v)):c for (x,y,u,k,v),c in column.items()}
def join(a,b):
    out=defaultdict(int)
    for (sa,ba),ca in a.items():
        for (sb,bb),cb in b.items():
            out[sa+sb,ba[:-1]+(ba[-1]+bb[0],)+bb[1:]]+=ca*cb
    return clean(out)
a,b,c=[rel(pair,kind) for pair,kind in (((0,1),1),((2,3),1),((4,5),0))]
source=mul(mul(a,b),c)
assert source==mul(a,mul(b,c)) and len(source)==32
assert all(abs(v)==1 for v in source.values())
da,db,dc=D(0,a),D(3,b),D(15,c)
left=join(join(one(da),one(db)),one(dc))
right=join(one(da),join(one(db),one(dc)))
image=ordered(0,source,3)
assert image==left==right==f['balanced'](f['raw_joint']((3,15),(da,db,dc)))
assert not f['balanced_boundary'](image)
assert not ordered(0,source,2)
for kind in (0,1):assert not ordered(0,mul(source,rel((6,7),kind)),3)
sectors=[]
for ea in ((0,1),(1,3)):
    for eb in ((3,7),(7,15)):
        key=((('e',*ea,1),('e',*eb,1),('e',15,31,0)),((),(),(),()))
        assert image[key]==1
        sectors.append(key)
# Four-sector observation from the fixed residual form, not an invented metric.
y,w,gA,gB=s.symbols('y w gA gB',positive=True)
ma,mb,L=s.symbols('ma mb L',real=True)
X=s.symbols('X1:5',positive=True)
Q=s.Matrix([[2*L,1],[1,0]])/(2*y)
o=s.Matrix([1,-2*L])
def value(x,m):
    p=s.sqrt(2)*x*s.Matrix([1,m-L])
    return s.simplify((p.H*Q*o)[0]/x)
valsA=[value(X[0],ma),value(X[1],ma+gA)]
valsB=[value(X[2],mb),value(X[3],mb+gB)]
obs=s.simplify(w*w*(valsA[1]-valsA[0])*(valsB[1]-valsB[0]))
assert s.simplify(obs-w*w*gA*gB/(2*y*y))==0
assert s.diff(obs,L)==0
# Adjacent model [I^3 -> I^2]: action sends bc to abc and kills abc.
act=s.Matrix([[0,0],[1,0]])
h0,h1=s.symbols('h0 h1')
H=s.Matrix([[h0,h1]])
assert H*act==s.Matrix([[h1,0]])
assert s.solve([h1,h1-obs],[h1],dict=True)==[]
result={'passed':True,'actual_source_terms':len(source),'selected_two_feature_sectors':len(sectors),
 'checks':{'both_binary_balancings_equal_actual_D3':True,'three_seam_cycle':True,
 'old_D2_kills_new_layer':True,'D3_kills_fourth_power_fixtures':True,
 'positive_residual_gap_product':True,'arithmetic_multiplier_cancels':True,
 'adjacent_source_equivariant_nullhomotopy_obstruction':True},
 'scope':'Actual marked-path witness and exact observer algebra. Strict localization follows from the finite hereditary projective model, not merely scalar nonvanishing. Window-gap positivity and completed bounds are analytic proofs.'}
out=ROOT/'research/voevodsky/results/residual-adjacent-third-attachment.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
