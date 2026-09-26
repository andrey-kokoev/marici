"""Finite groupoid/action illustrations of two-sided transport; not a HoTT checker."""
from itertools import product
from pathlib import Path
import json
G=(0,1)
fibre=list(product(G,repeat=2))
def left(p,z):return (z[0]^p,z[1])
def right(q,z):return (z[0],z[1]^q)
def diagonal(p,z):return (z[0]^p,z[1]^p)
checks=0
for p,q,z in product(G,G,fibre):
    assert right(q,left(p,z))==left(p,right(q,z))
    assert left(p^q,z)==left(p,left(q,z))
    assert right(p^q,z)==right(p,right(q,z))
    assert left(p,left(p,z))==z and right(q,right(q,z))==z
    checks+=1
for p,z in product(G,fibre):
    assert diagonal(p,z)==right(p,left(p,z))==left(p,right(p,z))
assert left(1,(0,0))!=(0,0) and diagonal(1,(0,0))==(1,1)
# A one-object groupoid: natural identity-functor automorphisms are its center.
fillers=[h for h in G if all((h^g)==(g^h) for g in G)]
assert fillers==[0,1]
canonical=0;alternative=1
relative_loop=alternative^canonical  # each element is its own inverse
assert relative_loop==1 and relative_loop!=0
# In the discrete comparison groupoid of this 1-groupoid model, unequal
# group elements have no equality; do not promote this to arbitrary HoTT types.
assert canonical!=alternative
report={'passed':True,'finite_interchange_cases':checks,
 'nonidentity_monodromy_with_commuting_square':True,
 'diagonal_transport_equals_two_orders':True,
 'BC2_identity_functor_comparison_choices':fillers,
 'nontrivial_comparison_requires_extra_choice':True,
 'scope':'Two finite semantic illustrations and a separate written path-induction argument. No machine-checked HoTT theorem, no derived physical defect, no port-net interpretation yet.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/two-sided-transport-models.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
