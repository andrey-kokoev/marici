"""Factor the X1-soft exceptional Cayley--Menger kernel on sewn wall loci."""
import json
import sympy as sp
a,k,p,xi=sp.symbols('a k p xi')
K=a**4-8*a**2*k*p**2*xi-10*a**2*p**2+16*k**2*p**4+40*k*p**4*xi+16*p**4*xi**2+9*p**4
restrictions={'q_g1':sp.factor(K.subs(xi,-1)),'q_g2':sp.factor(K.subs(a,p)),'q_g3':sp.factor(K.subs(a,-3*p))}
assert sp.factor(restrictions['q_g1']-(a**2+4*k*p**2-5*p**2)**2)==0
out={name:{'exceptional_restriction':str(value),'is_square':False} for name,value in restrictions.items()}; out['q_g1']['is_square']=True
for name in ('q_g2','q_g3'):
 coeff,factors=sp.factor_list(restrictions[name]); out[name]['factor_list']=[(str(f),int(e)) for f,e in factors]; out[name]['is_square']=all(int(e)%2==0 for _,e in factors)
print(json.dumps({'schema':'marici.nima.qG12-exceptional-k-wall-restrictions.v1','status':'passed','restrictions':out,'bulk_soft_factor':'K0=x^2*K_exc+O(x^3)','claim_boundary':'exceptional leading kernel only; further normal valuation needed where restriction vanishes'},sort_keys=True))
