"""Actual-source lower-filtration defects of three ideal cubic detectors.

No numerical theta substitution: positive symbolic window parameters retain
exact source supports, and the companion proof uses certified positivity.
"""
from pathlib import Path
from itertools import product
import runpy,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
g=runpy.run_path(str(ROOT/'research/nima/checkers/check_translated_cubic_observer_growth.py'))
t=runpy.run_path(str(ROOT/'research/nima/checkers/check_all_depth_observer_tower.py'))
f=g['f'];ordered=t['ordered']
oldkeys=[((('e',*ea,1),('e',*eb,1),('e',15,31,0)),((),)*4)
 for ea in ((0,1),(1,3)) for eb in ((3,7),(7,15))]
pkeys=[oldkeys[0],((('e',0,1,1),('e',5,7,1),('e',15,31,0)),((),)*4)]
y,ga,gb,uA,uB=s.symbols('y ga gb uA uB',positive=True)
kA2,kA3,kA5,kB5,kB7,kD3,kD7=s.symbols('kA2 kA3 kA5 kB5 kB7 kD3 kD7',positive=True)
S0=ga*gb/(2*y*y);SX=-uA*(uB+gb)/(2*y*y)
weights=[uA*uB,-uA*(uB+gb),-(uA+ga)*uB,(uA+ga)*(uB+gb)]
weights=[v/(2*y*y) for v in weights]
N0=2*(kA2+kA3)*(kB5+kB7);NX=2*(kA2+kA5)*(kD3+kD7)
family=[]
for pairs,ksA,ksB,target,N in [(((0,1),(2,3)),(kA2,kA3),(kB5,kB7),S0,N0),
                             (((0,2),(1,3)),(kA2,kA5),(kD3,kD7),SX,NX)]:
    start=sum(1<<p for p in pairs[0])
    for i,j,last in product(range(2),range(2),(4,5)):
        p=pairs[0][i];q=pairs[1][j]
        key=((('e',0,1<<p,1),('e',start,start|(1<<q),1),('e',15,15|(1<<last),0)),((),)*4)
        sign=(-1)**(i+j+(last==5))
        family.append((key,sign*target*ksA[i]*ksB[j]/N))
def values(image):
    old=sum(image.get(k,0)*w for k,w in zip(oldkeys,weights))
    private=image.get(pkeys[0],0)*S0+image.get(pkeys[1],0)*SX
    redundant=sum(image.get(k,0)*w for k,w in family)
    return [s.factor(z) for z in (old,private,redundant)]
# Verify exact agreement on the ENTIRE homogeneous cubic source, not one witness.
count=0
for pairs in g['pairings'](tuple(range(6))):
    for kinds in ((1,1,0),(1,0,1),(0,1,1)):
        start=0;ds=[]
        for pair,kind in zip(pairs,kinds):
            ds.append(g['one'](f['derivative'](start,f['relation'](pair,kind))))
            start|=sum(1<<j for j in pair)
        v=values(g['join'](g['join'](ds[0],ds[1]),ds[2]))
        assert s.simplify(v[0]-v[1])==0 and s.simplify(v[0]-v[2])==0
        count+=1
assert count==270
mixed=f['relation']((0,1),1)
x=f['multiply'](mixed,{((2,3,4,5),(1,0,0,0)):1})
xprime=f['multiply'](mixed,{((2,3,5,4),(1,0,0,0)):1})
v0=f['chain_product'](t['factors'](3))
# These one-relation examples are genuinely below I^2.
assert f['derivative'](0,x) and f['derivative'](0,xprime)
U=-ga*uB/(2*y*y)
R=S0*kB5/(2*(kB5+kB7))
vx=values(ordered(0,x,3));vxp=values(ordered(0,xprime,3));vv=values(ordered(0,v0,3))
assert all(s.simplify(a-b)==0 for a,b in zip(vx,(U,S0,R)))
assert all(s.simplify(a-b)==0 for a,b in zip(vxp,(0,0,-R)))
assert vv==[S0]*3
M=s.Matrix.hstack(s.Matrix(vv),s.Matrix(vx),s.Matrix(vxp))
assert s.simplify(M.det()+R*S0*(S0-U))==0
assert M.det()!=0
# A source in the old saturated evaluation kernel but not in either private one.
old_kernel_values=[s.factor(S0*a-U*b) for a,b in zip(vx,vv)]
assert old_kernel_values[0]==0
assert s.simplify(old_kernel_values[1]-S0*(S0-U))==0
assert s.simplify(old_kernel_values[2]-S0*(R-U))==0
# Pairwise defects kill cubic inputs but are nonzero on the lower source.
assert s.simplify(vx[1]-vx[0])!=0 and s.simplify(vx[2]-vx[0])!=0
assert s.simplify(vx[1]-vx[2])!=0
result={'passed':True,'cubic_basis_products_checked':count,
 'lower_source_values':{'x':[str(a) for a in vx],'x_prime':[str(a) for a in vxp],
                       'v0':[str(a) for a in vv]},
 'top_corner_three_detector_rank':3,
 'checks':{'all_three_equal_on_entire_cubic_component':True,
 'explicit_lower_filtration_discrepancies':True,
 'three_distinct_source_compatible_observer_quotients':True,
 'defects_descend_to_previous_full_filtered_source':True},
 'scope':'Actual ordered recorder and exact symbolic source identities. Saturated-module inequivalence is relative to the fixed source evaluation. No assertion of abstract module nonisomorphism or equality/inequality of Ext classes with unidentified kernels is made.'}
out=ROOT/'research/voevodsky/results/cubic-recalibration-tower-defect.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
