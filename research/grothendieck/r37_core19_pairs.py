from r37_shared_triple import *
from math import prod
from itertools import chain
R,K,_=data(cores[19]['core']);V=[[i for i in range(16) if r>>i&1] for r in R];d=Counter(chain.from_iterable(V));G={}
for v in V:G.setdefault(tuple(sorted(d[j] for j in v)),[]).append(v)
H=[[prod(F(sum(j not in l for l in rows),len(rows)) for j in v) for v in V] for rows in G.values()];A=np.asarray(H,float);n=len(R)
def opt(A):return linprog([0]*n+[-1],A_ub=np.c_[-A,np.ones(len(A))],b_ub=np.zeros(len(A)),A_eq=[[1]*n+[0]],b_eq=[1])
res=opt(A);y=[F(float(t)).limit_denominator(10**7) for t in -res.ineqlin.marginals];vals=[sum(t*z for t,z in zip(y,h)) for h in zip(*H)];tight=[r for r,v in zip(R,vals) if v==max(vals)];assert max(vals)==F(3393,21856) and len(tight)==14;print('tight',tight)
assert tight==[4576,6016,7936,11267,11778,16414,16444,18443,26627,32948,33008,33248,34177,36097]
if __name__=='__main__':
 mask=lambda v:sum(1<<i for i in v);v=V[R.index(9349)];rows=G[tuple(sorted(d[j] for j in v))];print('sites',v,'class',rows)
 for k in range(1,6):
    hits=[t for t in combinations(v,k) if all(mask(t)&q for q in tight)]
    if k==2:print('pair counterwitnesses',[(t,next(q for q in tight if not mask(t)&q)) for t in combinations(v,2)])
    if hits:print('minimum',k,hits);break
 allowed=[i for i in range(16) if any(i in l for l in rows)];sets=list(combinations(allowed,5))
 for order in (1,2):
    terms=[()] + list(combinations(allowed,1))+(list(combinations(allowed,2)) if order==2 else []);E=np.array([[set(t)<=set(l) for l in sets] for t in terms],int);target=np.array([sum(set(t)<=set(l) for l in rows) for t in terms]);obj=np.array([all(mask(l)&q for q in tight) for l in sets],int);sol=linprog(obj,A_eq=E,b_eq=target);assert sol.success
    x=[F(float(z)).limit_denominator(1000000) for z in sol.x];y=[F(float(z)).limit_denominator(1000000) for z in sol.eqlin.marginals];assert min(x)>=0 and all(sum(a*b for a,b in zip(x,h))==t for h,t in zip(E.tolist(),target)) and all(sum(a*b for a,b in zip(y,h))<=t for h,t in zip(E.T.tolist(),obj));val=sum(a*int(b) for a,b in zip(x,obj));assert val==sum(a*int(b) for a,b in zip(y,target));print('order',order,'mass',val/len(rows))
 P=[[l for l in R if l&i==i] for i in map(mask,combinations(range(16),2))];B=np.array([[all(not l&q for l in group) for q in R] for group in P if group],int);sol=opt(B);print('proxy',-sol.fun,'zero groups',sum(~B.any(axis=1)));print('uniform worst',margin(R,[F(1,n)]*n))
