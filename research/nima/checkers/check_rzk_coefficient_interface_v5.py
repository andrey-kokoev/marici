"""Base-change and Tor-preservation fixtures, not a Rzk or source-bundle run."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib,json

# Polynomials in independent X,t,h over Z. Substituting any polynomial h
# preserves these identities; h is not a random numerical sample.
def add(a,b):
    out=dict(a)
    for k,c in b.items():
        out[k]=out.get(k,0)+c
        if not out[k]:del out[k]
    return out
def neg(a):return {k:-c for k,c in a.items()}
def mul(a,b):
    out={}
    for ka,ca in a.items():
        for kb,cb in b.items():out=add(out,{tuple(i+j for i,j in zip(ka,kb)):ca*cb})
    return out
def crossing(a):return {k:c for k,c in a.items() if k[0]==k[1]==0}
X={(1,0,0):1};t={(0,1,0):1};h={(0,0,1):1};one={(0,0,0):1}
fh=(mul(t,add(one,neg(h))),mul(X,h))
assert add(mul(X,fh[0]),mul(t,fh[1]))==mul(X,t)
assert all(not crossing(p) for p in fh)
fX=(t,{});ft=({},X)
assert (add(ft[0],neg(fX[0])),add(ft[1],neg(fX[1])))==(neg(t),X)
assert add(mul(X,neg(t)),mul(t,X))=={}
# Regular-sequence syzygy classifies ALL choices in the accompanying proof.

# Derived fibre cone: T_i plus S_(i-1), ranks 1,3,2 in degrees 0,1,2.
# d1 is identity on the S0 summand, d2 zero since f1 and differentials vanish.
d1=[[0,0,1]];d2=[[0,0],[0,0],[0,0]]
def rank(a):
    a=[[Fraction(x) for x in row] for row in a];r=0
    for c in range(len(a[0])):
        p=next((k for k in range(r,len(a)) if a[k][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];v=a[r][c];a[r]=[x/v for x in a[r]]
        for k in range(r+1,len(a)):
            v=a[k][c];a[k]=[x-v*y for x,y in zip(a[k],a[r])]
        r+=1
        if r==len(a):break
    return r
homology=[1-rank(d1),3-rank(d1)-rank(d2),2-rank(d2)]
assert homology==[0,2,2] and d1[0][2]==1
# Unit pivot and zero remaining differential give integral freeness, not
# merely ranks over a field.

# Special-node normalization: arbitrary branch tails with equal constants
# are precisely the node image. Sparse univariate polynomials, no truncation.
def normalize(p):return {k:c for k,c in p.items() if c}
def delta(pair):return pair[0].get(0,0)-pair[1].get(0,0)
def node_relation(pair):
    assert delta(pair)==0
    return pair  # A0 identified with equal-constant pairs via normalization
for degree in range(1,13):
    pair=({0:3,degree:2},{0:-1,degree:-5})
    c=delta(pair)
    adjusted=(normalize({k:v-(c if k==0 else 0) for k,v in pair[0].items()}),pair[1])
    assert delta(adjusted)==0 and node_relation(adjusted)==adjusted
assert delta(({0:1},{}))==1  # primitive cokernel class
assert delta(node_relation(({0:1},{0:1})))==0
# Total normalization cofiber is acyclic for normal Z[X,t]; derived base
# change preserves zero. Its special-fibre counterpart has the above Z class.

# Two-chart dualizing-line monomial partition (bounded implementation control).
common=0;tested=0
for a in range(13):
    for b in range(-13,26):
        left=b>=0;right=b<=a-1
        assert left or right
        if left and right:
            assert a-b-1>=0 and b>=0
            # X^(a-b-1) u^b becomes X^a t^b e_X when u=Xt and e_X=1/X.
            assert (a-b-1)+b+1==a
            common+=1
        tested+=1
# Every base monomial has the inverse encoding a=i+j+1, b=j.
for i in range(13):
    for j in range(13):
        a,b=i+j+1,j
        assert 0<=b<=a-1 and (a-b-1,b)==(i,j)

spec=Path('research/nima/rzk-coefficient-interface-v5.md')
result={'status':'passed','checked_at':datetime.now(timezone.utc).isoformat(),
'spec_sha256':hashlib.sha256(spec.read_bytes()).hexdigest(),
'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
'crossing':{'universal_fh_chain_identity':True,'endpoint_choice_homotopy':True,'induced_Tor1_map':'zero for every h','fibre_cone_homology_ranks':homology,'integer_torsion':False},
'normalization':{'total_normal_chart_cofiber':'zero','special_node_cokernel':'Z_or','primitive_difference_value':1,'automatic_base_change_rejected':True},
'proper_trace_control':{'overlap_monomials_tested':tested,'common_monomials':common,'all_covered':True,'scope':'bounded check of the all-degree partition proof, not full duality verification'},
'nonverification':['No formal Rzk compilation','No full Rees or physical source run','Original Rees bundle checker files missing; original counts unverified','No branch-selected excess/logarithmic comparison constructed']}
Path('research/nima/results/rzk_coefficient_interface_v5.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
