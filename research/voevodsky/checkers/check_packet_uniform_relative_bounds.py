"""Exact collision multiplicity obstruction and l1 relative bounds."""
import json
import sympy as s

fixtures=[]
for m in (1,2,3,8,32):
    # m artificial vacuum cuts normalize to the same unit record.
    N=s.ones(1,m)
    Qfine=s.eye(m)
    correction=s.ones(m)-s.eye(m)
    assert N.T*N==Qfine+correction
    assert (N*N.T)[0]==m
    # Relative form entries have absolute value <=1 in this fixture,
    # independent of the growing l2 operator norm.
    assert max(abs(x) for x in correction)<=1
    if m>1:
        assert correction*s.ones(m,1)==(m-1)*s.ones(m,1)
    fixtures.append({'vacuum_cuts':m,'normalization_l2_norm_squared':m,
                     'correction_l2_positive_eigenvalue':max(0,m-1)})

# General matching relation: correction entries can be constructed directly
# from newly equal shapes. Test the l1 bound with complex coefficients.
images=(0,0,1,0,2,1)
x=(1+s.I,-2,3*s.I,1,-s.I,2)
y=(2,1-s.I,-1,2*s.I,3,-2)
T=sum(s.conjugate(x[i])*y[j] for i in range(6) for j in range(6)
      if i!=j and images[i]==images[j])
assert abs(complex(T)) <= float(sum(abs(z) for z in x)*sum(abs(z) for z in y))
result={'passed':True,'vacuum_multiplicity_fixtures':fixtures,
 'checks':{'raw_cut_hilbert_uniform_bound_obstructed':True,
           'new_match_l1_fixture_bound':True},
 'scope':'Exact vacuum coarsening model plus complex l1 regression. General tensor-carrier bounds are proved in companion note; no completed receiver injectivity certificate.'}
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/packet-uniform-relative-bounds.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
