"""Exact first two scores. For exposure, certify the whole optimal face when possible."""
from r37_shared_triple import data,cores,F,Counter,combinations,margin,np,linprog
from math import prod
eligible=[0,1,2,3,4,5,6,9,10,12,13,14,15,16,18,19,24,25,26,27,28,29,30,31,32,33,34,35,36]
def rat(v):return [F(float(x)).limit_denominator(10**7) for x in v]
st=Counter();first={};proof=None
for i in eligible:
 R,K,_=data(cores[i]['core']);T=[[sum(1<<v for v in t) for t in combinations([j for j in range(16) if q>>j&1],3)] for q in R];ct=Counter(t for L in T for t in L);raw=[sum(F(1,ct[t]) for t in L) for L in T];rank=[sum(y<=x for y in raw) for x in raw];rules=[rank,raw,[max(F(1,max(ct[t],ct[u])) for t,u in combinations(L,2) if (t&u).bit_count()==1) for L in T],[v/(1+sum((r&q).bit_count()==4 for q in R)) for r,v in zip(R,raw)]]
 for j,w in enumerate(rules):
    m,r=margin(R,w);st[j,m>0]+=1
    if j>=2:
        b=margin(R,rules[j-2])[0]>0;st[j,'rescued']+=m>0 and not b;st[j,'lost']+=m<=0 and b;st[j,'reversed']+=any((raw[h]-raw[k])*(w[h]-w[k])<0 for h,k in combinations(range(len(R)),2))
    if m<=0:first.setdefault(j,(i,r,str(m)))
 if proof:continue
 V=[[j for j in range(16) if r>>j&1] for r in R];d=Counter(j for L in V for j in L);G={}
 for L in V:G.setdefault(tuple(sorted(d[j] for j in L)),[]).append(L)
 H=[[prod(F(sum(j not in L for L in rows),len(rows)) for j in v) for v in V] for rows in G.values()];A=np.asarray(H,dtype=float);n=len(R);res=linprog([0]*n+[-1],A_ub=np.c_[-A,np.ones(len(H))],b_ub=np.zeros(len(H)),A_eq=[[1]*n+[0]],b_eq=[1]);assert res.success
 x=rat(res.x[:-1]);y=rat(-res.ineqlin.marginals);x=[z/sum(x) for z in x];y=[z/sum(y) for z in y];lo=min(sum(z*v for z,v in zip(x,h)) for h in H);vals=[sum(z*v for z,v in zip(y,h)) for h in zip(*H)];hi=max(vals)
 if lo!=hi:continue
 active=[r for r,v in zip(R,vals) if v==hi];s=next((s for s in R if all(s&r for r in active)),None)
 if s is not None:proof=(i,s,str(hi),len(active))
print(st,first,'exposure exact all-optima counterexample',proof)
