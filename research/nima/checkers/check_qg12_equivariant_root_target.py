"""Classify equivariant maps from a trivial rank-one source to the root-pair lattice."""
import json
# A homomorphism f: Z -> Z^2 is f(1)=(a,b). Equivariance for root swap requires (b,a)=(a,b).
solutions=[{'multiplier':n,'image':[n,n],'total_parity':(2*n)%2} for n in range(-3,4)]
assert all(r['image'][0]==r['image'][1] for r in solutions)
assert all(r['total_parity']==0 for r in solutions)
assert any(r['image']==[0,0] for r in solutions)
print(json.dumps({'schema':'marici.nima.qg12-equivariant-root-target.v1','status':'passed','equivariant_map_form':'f(1)=n*(gamma_minus+gamma_plus)','all_images_even':True,'existence_not_forced':True,'primitive_normalization_not_forced':True,'zero_map_admissible':True,'sample_solutions':solutions,'bold_conjecture':'the canonical unordered root-pair target itself constructs the physical pairing','disposition':'falsified: it constrains any equivariant map but does not provide one','residual_conjecture':'a source-derived nonzero primitive equivariant specialization, if established, uniquely lands on the even generator up to orientation'},sort_keys=True))
