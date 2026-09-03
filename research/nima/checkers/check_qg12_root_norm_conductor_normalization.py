"""Compare the root norm factor two with the q_g2 conductor coefficient."""
import json
import sympy as sp
p,k=sp.symbols('p k', nonzero=True)
r=sp.Rational(1,64)/(p**4*(k-1))
euler_inv=1/(k-1)
coinvariant_scalar=-sp.factor(r*euler_inv)
norm_pair=(coinvariant_scalar,coinvariant_scalar)
augmented=sp.factor(sum(norm_pair))
expected=-sp.Rational(1,32)/(p**4*(k-1)**2)
assert sp.factor(augmented-expected)==0
assert sp.factor(coinvariant_scalar*2-expected)==0
print(json.dumps({'schema':'marici.nima.qg12-root-norm-conductor-normalization.v1','status':'passed','individual_residue':'1/(64*p^4*(k-1))','inverse_euler':'1/(k-1)','oriented_coinvariant_scalar':str(coinvariant_scalar),'norm_pair':[str(x) for x in norm_pair],'augmentation_after_norm':str(augmented),'expected_connecting_coefficient':str(expected),'factor_two_matches_exactly':True,'bold_conjecture':'the norm factor two obstructs the exact conductor normalization','disposition':'falsified','residual_conjecture':'the exact coefficient is compatible with norm transfer of one oriented occurrence scalar, but scalar compatibility does not construct the source chain map'},sort_keys=True))
