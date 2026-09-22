"""Four-seam source cycle, actual-record pentagon and adjacent obstruction."""
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
            bs=[record(states[a+1],word[a+1:b],marks[a+1:b]) for a,b in zip(cuts,cuts[1:])]
            for entries in product(*(v.items() for v in bs)):
                c=coef
                for _,v in entries:c*=v
                out[seams,tuple(k for k,_ in entries)]+=c
    return clean(out)
def one(col):return {((('e',x,y,k),),(u,v)):c for (x,y,u,k,v),c in col.items()}
def join(a,b):
    out=defaultdict(int)
    for (sa,ba),ca in a.items():
        for (sb,bb),cb in b.items():
            out[sa+sb,ba[:-1]+(ba[-1]+bb[0],)+bb[1:]]+=ca*cb
    return clean(out)
trees=((((0,1),2),3),((0,(1,2)),3),(0,((1,2),3)),(0,(1,(2,3))),((0,1),(2,3)))
def evaluate(tree,cols):
    return cols[tree] if isinstance(tree,int) else join(evaluate(tree[0],cols),evaluate(tree[1],cols))
def decorate(tree,keys):
    return ('leaf',keys[tree]) if isinstance(tree,int) else (decorate(tree[0],keys),decorate(tree[1],keys))
def rotate(tree,path=()):
    if path:
        i=path[0];out=list(tree);out[i]=rotate(out[i],path[1:]);return tuple(out)
    (a,b),c=tree
    assert a!='leaf'
    return (a,(b,c))
a,b,c,d=[rel((2*i,2*i+1),kind) for i,kind in enumerate((1,1,1,0))]
source=f['chain_product']((a,b,c,d))
assert len(source)==128 and all(abs(v)==1 for v in source.values())
cols=[one(D(start,col)) for start,col in zip((0,3,15,63),(a,b,c,d))]
images=[evaluate(tree,cols) for tree in trees]
actual=ordered(0,source,4)
assert all(im==actual for im in images)
assert not f['balanced_boundary'](actual)
assert not ordered(0,source,3)
assert not ordered(0,mul(source,rel((8,9),0)),4)
# Test the two pentagon routes on bracketed ACTUAL record keys, before
# forgetting parentheses or merging intermediate buffers.
checks=nonvacuum=0
for keys in product(*(col.keys() for col in cols)):
    start=decorate(trees[0],keys)
    route3=rotate(rotate(rotate(start,(0,)),()),(1,))
    route2=rotate(rotate(start,()),())
    assert route3==route2==decorate(trees[3],keys)
    checks+=1
    nonvacuum+=any(any(buf for buf in key[1]) for key in keys)
assert nonvacuum>0
sectors=[]
for ea,eb,ec in product(((0,1),(1,3)),((3,7),(7,15)),((15,31),(31,63))):
    key=((('e',*ea,1),('e',*eb,1),('e',*ec,1),('e',63,127,0)),((),(),(),(),()))
    assert actual[key]==1;sectors.append(key)
# Product of three residual differences in the existing form.
y,w=s.symbols('y w',positive=True)
gaps=s.symbols('gA gB gC',positive=True)
L=s.symbols('L',real=True)
means=s.symbols('mA mB mC',real=True)
Q=s.Matrix([[2*L,1],[1,0]])/(2*y);o=s.Matrix([1,-2*L])
def v(m):return s.simplify((s.Matrix([s.sqrt(2),s.sqrt(2)*(m-L)]).H*Q*o)[0])
value=s.simplify(w**3*s.prod(v(m+g)-v(m) for m,g in zip(means,gaps)))
assert s.simplify(value-w**3*s.sqrt(2)*s.prod(gaps)/(4*y**3))==0
assert s.diff(value,L)==0
h=s.symbols('h')
assert s.solve([h,h-value],[h],dict=True)==[]
result={'passed':True,'actual_source_terms':len(source),'selected_three_feature_sectors':len(sectors),
 'actual_record_pentagons':checks,'pentagons_with_nonvacuum_buffers':nonvacuum,
 'checks':{'all_five_parenthesizations_equal_D4':True,'both_pentagon_routes_agree_before_flattening':True,
 'four_seam_cycle':True,'D3_kills_new_layer':True,'D4_kills_fifth_power_fixture':True,
 'three_residual_gap_observation':True,'adjacent_nullhomotopy_obstruction':True},
 'scope':'Actual typed bottom-cycle records and canonical reassociation. General quotient/chain compatibility and strict localization are proved in the note; no higher homotopy or perfect-duality claim is inferred from these fixtures.'}
out=ROOT/'research/voevodsky/results/four-seam-residual-pentagon.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
