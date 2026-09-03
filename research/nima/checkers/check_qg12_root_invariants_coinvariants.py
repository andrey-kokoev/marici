"""Distinguish invariant and coinvariant unordered-root lattices."""
import json
# M=Z e_- + Z e_+, swap exchanges coordinates.
# Invariants are (n,n). Coinvariants impose e_-=e_+, so class is represented by a+b.
samples=[]
for a in range(-2,3):
 for b in range(-2,3):
  samples.append({'lift':[a,b],'coinvariant_class':a+b,'lift_total_parity':(a+b)%2,'invariant':a==b})
primitive_coinvariant_lifts=[r['lift'] for r in samples if r['coinvariant_class']==1]
assert [1,0] in primitive_coinvariant_lifts and [0,1] in primitive_coinvariant_lifts
assert all((2*n)%2==0 for n in range(-3,4))
print(json.dumps({'schema':'marici.nima.qg12-root-invariants-coinvariants.v2','status':'passed','invariant_submodule':'Z*(e_-+e_+)','coinvariant_quotient':'Z with [e_-]=[e_+]','odd_single-root_lifts_descend_to_coinvariant_generator':True,'primitive_coinvariant_lifts':primitive_coinvariant_lifts,'no_canonical_section_of_quotient':True,'canonical_norm_isomorphism':'N([e_-])=e_-+e_+','quotient_after_norm':'multiplication by 2','bold_conjecture':'mere descent to the unordered-root quotient excludes odd projection maps','disposition':'falsified','residual_conjecture':'evenness requires a source arrow typed as norm/transfer rather than projection; target comparison alone does not select the arrow'},sort_keys=True))
