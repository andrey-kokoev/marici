"""Independent Euclidean loop-Jacobian challenge to the literal source normalization.
A passing check means the discrepancy is reproduced, NOT physical identification.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import permutations
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
paths=[Path(__file__),ROOT/'temp/arxiv-2408.16386-source/sections/method.tex',
 ROOT/'temp/arxiv-2408.16386-source/sections/cosmologicalintegrals.tex']
def inventory():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def det(m):
    ans=F(0)
    for p in permutations(range(3)):
        term=F((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)))
        for i in range(3):term*=m[i][p[i]]
        ans+=term
    return ans
before=inventory();count=0
for a in map(F,(1,2)):
 for v in map(F,(1,3)):
  for p in map(F,(0,1)):
   for h in map(F,('-2','-1/2','1/2','2')):
    x,y=F(1,3),F(2,5)
    J=[[2*x,2*y,2*h],[2*(x-a),2*y,2*h],[2*(x-p),2*(y-v),2*h]]
    assert det(J)==8*a*v*h
    sqrtK=a*v*abs(h)/6
    assert 2/(a*v*abs(h))==1/(3*sqrtK)
    count+=1
# Homogeneity including the three y dy factors (degree six).
for dim in (3,4,5,6):
    gamma=F(dim-4,2)
    printed=6+4*F(5-dim,2)+6*gamma
    euclidean=6+4*F(3-dim,2)+6*gamma
    assert printed==dim+4 and euclidean==dim
# d=5: gamma=1/2; remove the common pi*sqrt(K) factor.
ratios=[]
for D in map(F,(1,4)):
    src=F(16);geom=6/D
    assert src/geom==F(8,3)*D
    assert (F(16,9)*D)/F(1,3)==F(16,3)*D # small-epsilon ratio slope
    ratios.append(str(src/geom))
assert ratios[0]!=ratios[1] # no dimension-only factor reconciles both geometries
assert before==inventory()
report={'passed':True,'source_unchanged':True,'source_sha256':before,
 'jacobian_fixture_count':count,'printed_measure_matches_euclidean':False,
 'euclidean_d3_measure':'(1/(3 sqrt(K))) product y dy, including both transverse signs',
 'euclidean_general_measure':'pi^((d-2)/2)*3^(d-4)/Gamma((d-2)/2) * D^((3-d)/2)*K^((d-4)/2)',
 'printed_to_euclidean_ratio':'16D/(3 sqrt(pi))*Gamma((d-2)/2)/Gamma((d-3)/2)',
 'ratio_at_d5_for_D_1_4':ratios,'small_epsilon_ratio':'(16/3)*epsilon*D + O(epsilon^2)',
 'homogeneity':'printed weighted measure has degree d+4; Euclidean measure has degree d',
 'scope':'Ordinary Euclidean simplex volumes and unnormalized d^d loop momentum. An external-kinematic prefactor or different volume convention could explain the difference but must be supplied; no silent correction of the paper.',
 'verification_boundary':'Exact finite Jacobian/coefficient checks and homogeneity; general angular integration and interpretation are derived in triangle-measure-audit.md.'}
(HERE/'triangle-measure-audit.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
