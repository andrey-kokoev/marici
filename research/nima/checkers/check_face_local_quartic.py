"""Exact face-local allocation constraints, bounded symbolic six-point case."""
import json,runpy
from pathlib import Path
from itertools import combinations
from sympy import symbols,prod,expand,Poly,groebner
z=runpy.run_path('research/nima/checkers/check_quartic_contact_source.py')
T,D,faces,weights,s,g,h=(z[k] for k in ('T','D','faces','weights','s','g','h'))
Q=list(combinations(range(6),4));params=symbols(' '.join('a'+''.join(map(str,q)) for q in Q));P=dict(zip(Q,params))
alloc={}
for d in D:
    qs=[tuple(sorted(f)) for f in faces(d) if len(f)==4]
    for i,t in enumerate(T):
        if not d<=t:continue
        alloc[d,i]=prod(P[q] if (q[0],q[2]) in t else 1-P[q] for q in qs)
    assert expand(sum(alloc[d,i] for i,t in enumerate(T) if d<=t)-1)==0
W=[expand(sum(weights[d]*alloc[d,i]*prod(s[e] for e in t-d) for d in D if d<=t)) for i,t in enumerate(T)]
constraints=[]
for item in z['residuals']:
    i,j,k,l=item['indices'];res=expand(W[i]*W[j]-W[k]*W[l])
    for c in Poly(res,g,h,*s.values()).coeffs():
        c=Poly(c,*params).monic().as_expr()
        if c not in constraints:constraints.append(c)
assert len(constraints)<=300 and max(Poly(c,*params).total_degree() for c in constraints)<=4
# Fixed dimensions, max 300 input polynomials of degree <=4; execution timeout 30s.
G=groebner(constraints,*params,order='grevlex')
one=any(p.as_expr()==1 for p in G.polys)
out={'status':'inconsistent' if one else 'proper_ideal','parameter_faces':[list(q) for q in Q],'constraint_count':len(constraints),'constraints':[str(c) for c in constraints],'groebner_basis':[str(p.as_expr()) for p in G.polys],'scope':'Constant face-specific allocations, products for independent quartics, generic formal channel identities over Q. No momentum-dependent allocation claim.'}
Path('research/nima/results/face_local_quartic.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
