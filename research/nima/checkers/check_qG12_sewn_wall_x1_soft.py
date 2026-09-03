"""Exact rational-factor specialization of sewn q_G12 wall residues at X1-soft."""
import json
import sympy as sp
x,p,k,a,xi=sp.symbols('x p k a xi', nonzero=True)
y=p+x*k/2; z=p-x*k/2; b=2*p+x*(1+xi)
rows={
 'q_g1':{'N':a+z-x,'O':(y+z-x)*(a-y),'S':(a-x-z)*(a+y+2*z),'differential':'-da','valuation':0},
 'q_g2':{'N':b+z-y,'O':(b-x)*(x+z-y),'S':(b-y-z)*(x+b+2*z),'differential':'+x dxi','valuation':-2},
 'q_g3':{'N':-x-y-z,'O':(b-x)*(-b-z-y),'S':(b-y-z)*(-b-x-2*z),'differential':'+x dxi','valuation':-1},
}
out={}; leads={}
for name,row in rows.items():
 r=sp.factor(row['N']/(row['O']*row['S'])); lead=sp.factor((x**(-row['valuation'])*r).subs(x,0)); leads[name]=lead
 out[name]={'rational_factor':str(r),'rational_soft_valuation':row['valuation'],'rational_leading_coefficient':str(lead),'pulled_differential':row['differential'],'valuation_after_differential':row['valuation']+(1 if name!='q_g1' else 0)}
assert sp.factor(leads['q_g1']-(a+p)/(2*p*(a-p)**2*(a+3*p)))==0
assert sp.factor(leads['q_g2']-1/(4*p*(1-k)*(xi+1)))==0
assert sp.factor(leads['q_g3']+1/(16*p**2*(xi+1)))==0
print(json.dumps({'schema':'marici.nima.qG12-sewn-wall-x1-soft.v1','status':'passed','chart':'y=p+x*k/2,z=p-x*k/2,b=2p+x(1+xi)','rows':out,'claim_boundary':'rational factors and pulled differentials only; sqrt(K), relative reduction, epsilon normalization, and cycle pairing excluded'},sort_keys=True))
