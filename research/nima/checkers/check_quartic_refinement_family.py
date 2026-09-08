"""One universal split parameter per canonically ordered quartic face."""
import runpy,json
from pathlib import Path
from itertools import combinations
from sympy import symbols,prod,expand,Poly,gcd,factor
z=runpy.run_path('research/nima/checkers/check_quartic_contact_source.py')
T,D,faces,weights,s,g,h=(z[k] for k in ('T','D','faces','weights','s','g','h'))
a=symbols('alpha');alloc={}
for d in D:
    qs=[sorted(f) for f in faces(d) if len(f)==4]
    for i,t in enumerate(T):
        if not d<=t:continue
        coeff=1
        for q in qs:
            e=(q[0],q[2]);other=(q[1],q[3]);assert (e in t)!=(other in t)
            coeff*=a if e in t else 1-a
        alloc[d,i]=expand(coeff)
    assert expand(sum(alloc[d,i] for i,t in enumerate(T) if d<=t)-1)==0
W=[expand(sum(weights[d]*alloc[d,i]*prod(s[e] for e in t-d) for d in D if d<=t)) for i,t in enumerate(T)]
polys=[];res=[]
for item in z['residuals']:
    i,j,k,l=item['indices'];r=expand(W[i]*W[j]-W[k]*W[l]);res.append(r)
    polys.extend(Poly(r,g,h,*s.values()).coeffs())
G=Poly(0,a)
for c in polys:G=gcd(G,Poly(c,a))
G=G.monic();assert G.as_expr()==1
assert Poly(res[0],g,h,*s.values()).coeff_monomial(g**2*h**3*s[0,3]*s[0,2]*s[0,4])==a**3
assert expand(Poly(res[2],g,h,*s.values()).coeff_monomial(g**2*h**3*s[2,5]*s[1,5]*s[3,5])+(a-1)**3)==0
checks={str(v):all(expand(r.subs(a,v))==0 for r in res) for v in (0,1)}
out={'status':'passed','ansatz':'Universal alpha for diagonal (q0,q2), 1-alpha for (q1,q3), sorted cyclic quadrilateral labels; product allocations for two quartic vertices','source_sum_preserved':True,'coefficient_condition_gcd':str(G.as_expr()),'endpoint_checks':checks,'quadric_residuals':[str(factor(r)) for r in res],'scope':'Exact characteristic-zero identities in formal channels. This one-parameter family is not all polynomial refinements.'}
Path('research/nima/results/quartic_refinement_family.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
