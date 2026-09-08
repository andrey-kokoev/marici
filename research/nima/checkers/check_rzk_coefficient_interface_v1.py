"""Exact bounded mathematical regressions for the Rzk coefficient interface.
Not a Rzk compiler test; no imports or execution of other-owner checkers.
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json


def mul(a,b):
    assert len(a[0])==len(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def sub(a,b):
    return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]


def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def zero(a):return all(x==0 for row in a for x in row)


def rank(a):
    a=[[Fraction(x) for x in row] for row in a];r=0
    for c in range(len(a[0])):
        pivot=next((k for k in range(r,len(a)) if a[k][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];v=a[r][c]
        a[r]=[x/v for x in a[r]]
        for k in range(len(a)):
            if k!=r:
                v=a[k][c];a[k]=[x-v*y for x,y in zip(a[k],a[r])]
        r+=1
        if r==len(a):break
    return r


def determinant(a):
    a=[[Fraction(x) for x in row] for row in a];ans=Fraction(1)
    for c in range(len(a)):
        p=next((k for k in range(c,len(a)) if a[k][c]),None)
        if p is None:return 0
        if p!=c:a[c],a[p]=a[p],a[c];ans=-ans
        v=a[c][c];ans*=v
        for k in range(c+1,len(a)):
            ratio=a[k][c]/v
            a[k]=[x-ratio*y for x,y in zip(a[k],a[c])]
    assert ans.denominator==1
    return int(ans)

# 1. I^0=Z(u,a), I^1=Z(b); d(a)=b. V^0=Z^2, E^0=Z.
dI=[[0,1]];rho=[[1,0],[1,1]];Delta=[[-1,1]];ell=[[1]]
m=mul(Delta,rho)
assert m==[[0,1]] and not zero(m)
assert mul(ell,dI)==m
assert mul(rho,[[1],[0]])==[[1],[1]]
# B differential is Delta; Phi^0=rho and Phi^1=ell.
assert zero(sub(mul(Delta,rho),mul(ell,dI)))
missing_homotopy_defect=sub(mul(Delta,rho),mul([[0]],dI))
assert not zero(missing_homotopy_defect)

# 2. Exact primitive boundary graph fixture. Edges are vertex indices.
edges=[(0,1),(0,6),(0,7),(1,2),(1,4),(2,3),(2,7),(3,4),(3,6),(4,5),(5,6),(5,7)]
inc=[[int(v==b)-int(v==a) for v in range(8)] for a,b in edges]
diagonal=[[1] for _ in range(8)]
assert zero(mul(inc,diagonal)) and rank(inc)==7 and rank(diagonal)==1
# A spanning tree provides a unit maximal minor, not merely a unit entry.
seen={0};tree=[]
while len(seen)<8:
    found=False
    for k,(a,b) in enumerate(edges):
        if (a in seen)!=(b in seen):
            seen.update((a,b));tree.append(k);found=True;break
    assert found
minor=[[inc[k][j] for j in range(1,8)] for k in tree]
unit_minor=determinant(minor)
assert abs(unit_minor)==1
relative_ranks={'0':1-rank(diagonal),'1':8-rank(inc)-rank(diagonal),'2':12-rank(inc)}
assert relative_ranks=={'0':0,'1':0,'2':5}
# ker(inc) consists exactly of constant vectors by connectedness. Hence im(diag)
# equals that integral kernel, and the unit minor certifies torsion-free H^2.
unshifted_relative_pi0_rank=relative_ranks['0']
shifted_probe_pi0_rank=relative_ranks['2']  # probe Z[-2]
assert unshifted_relative_pi0_rank==0 and shifted_probe_pi0_rank==5
assert shifted_probe_pi0_rank!=0  # rejects promotion to acyclic stable fibre

# 3. Constant-mode counit cone: C^-1=Z, C^0=Z plus Z^2.
dCone=[[1],[-1],[-1]]
pi=[[1,1,0],[1,0,1]];section=[[0,0],[1,0],[0,1]];H=[[1,0,0]]
assert zero(mul(pi,dCone))
assert mul(pi,section)==eye(2)
assert mul(dCone,H)==sub(eye(3),mul(section,pi))
assert mul(H,dCone)==eye(1)
assert 3-rank(dCone)==2  # Cone is NOT acyclic.

# 4. Finite explicit counterexample in an unrestricted polynomial model.
a=((1,),(1,));b=((1,1),(1,))  # coefficients ordered by branch degree

def conductor(p):
    assert p[0][0]==p[1][0]
    return p[0][0]
assert conductor(a)==conductor(b)==1 and a!=b
# Both are global constant-compatible degree-zero sections. The nonnegative
# section complex has no degree-minus-one boundaries that could identify them.

# 5. Four valid faces without a filler. All edges identity on V^-1 plus V^0.
H012=[[0,1],[0,0]];d=[[0,0],[0,0]]
assert zero(mul(d,H012)) and zero(mul(H012,d))
assert zero(sub(mul(eye(2),eye(2)),eye(2)))
R=sub(d,H012)
assert not zero(R)
assert not any(target==source-2 for source in (-1,0) for target in (-1,0))
# Hom^-2(V,V)=0, so the nonzero R cannot equal delta K.

spec=Path('research/nima/rzk-coefficient-interface-v1.md')
result={'status':'passed','checked_at':datetime.now(timezone.utc).isoformat(),
'spec_sha256':hashlib.sha256(spec.read_bytes()).hexdigest(),
'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
'fixtures':{
'coherent_descent':{'passed':True,'nonzero_overlap_defect':m,'omitted_ell_rejected':True},
'probe_vs_stable_fibre':{'passed':True,'relative_cohomology_ranks':relative_ranks,'maximal_minor':unit_minor,'tree_edge_indices':tree,'unshifted_mapping_space':'contractible','shifted_probe':'Z[-2]','shifted_pi0':'Z^5','false_acyclicity_rejected':True},
'supported_counit_constant_mode':{'passed':True,'cone_H0_rank':2,'false_equivalence_rejected':True},
'branch_collision':{'passed':True,'pair_a':'(1,1)','pair_b':'(1+x,1)','same_conductor':1,'false_readout_injectivity_rejected':True},
'prescribed_tetrahedral_boundary':{'passed':True,'all_face_boundaries_hold':True,'residual':R,'degree_minus_two_maps_rank':0,'filler_exists':False}},
'nonverification':['No Rzk terms added or compiled','No full loaded or polynomial source checker rerun','No upstream geometric or physical comparison verified','No global conservative-probe theorem established']}
out=Path('research/nima/results/rzk_coefficient_interface_v1.json')
with out.open('w',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result))
