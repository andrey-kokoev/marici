"""Classify ordered-root allocations with the exact conductor augmentation."""
import json
import sympy as sp
p,k,lam=sp.symbols('p k lam', nonzero=True)
C=-sp.Rational(1,32)/(p**4*(k-1)**2)
pair=(sp.factor(lam*C),sp.factor((1-lam)*C))
assert sp.factor(sum(pair)-C)==0
samples={name:[str(sp.factor(x.subs(lam,v))) for x in pair] for name,v in [('minus_projection',1),('plus_projection',0),('norm_pair',sp.Rational(1,2)),('asymmetric',sp.Rational(1,3))]}
assert samples['minus_projection'][1]=='0'
assert samples['plus_projection'][0]=='0'
print(json.dumps({'schema':'marici.nima.qg12-conductor-augmentation-fiber.v1','status':'passed','exact_total':str(C),'general_fiber':'(lambda*C,(1-lambda)*C)','samples':samples,'norm_parameter':'1/2','single_root_parameters':['0','1'],'normalization_uniquely_selects_norm_pair':False,'bold_conjecture':'the exact connecting coefficient uniquely selects the even norm allocation','disposition':'falsified','residual_conjecture':'the coefficient fixes only augmentation; selecting lambda=1/2 requires source-derived root-transposition equivariance or an oriented relative-chain map'},sort_keys=True))
