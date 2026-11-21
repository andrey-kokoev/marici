"""Can a nonnegative sum of row budgets prove reuse? Build exact rational primal/dual certificates."""
from fractions import Fraction
from collections import Counter
from ramsey_final_miss_levels import attach,D,json
import numpy as np
from scipy.optimize import linprog

def test(H,k,d,old):
    I=[0]
    for i,r in enumerate(H):I += [s|1<<i for s in I if not s&r]
    allowed=set(I)-set(old);M=sorted(s for s in allowed if not any((s|1<<i) in allowed for i in range(len(H)) if not s>>i&1));T=[t for t in I if k-1-t.bit_count()<d];B=np.array([k-1-t.bit_count() for t in T]);M0=M
    # A fractional feasibility certificate can use ANY subset of supports.
    if len(M)>200:
        import random
        M=random.Random(42).sample([s for s in M if s.bit_count()==8],300)
    arr=np.array(M,dtype=np.int64);A=np.array([(t&arr)==0 for t in T]);res=linprog(np.zeros(len(M)),A_ub=A,b_ub=B,A_eq=np.ones((1,len(M))),b_eq=[d],bounds=(0,None));out={'rows':len(T),'maximal_allowed':len(M0)}
    if res.success:
        # Round weights down on a slightly oversized feasible packing if needed.
        x=[Fraction(float(a)).limit_denominator(100000) for a in res.x];
        if sum(x)!=d or not all(sum(a for s,a in zip(M,x) if not s&t)<=b for t,b in zip(T,B.tolist())):
            res=linprog(-np.ones(len(M)),A_ub=A,b_ub=B,bounds=(0,None));x=[Fraction(int(a*10000),10000) for a in res.x];assert sum(x)>=d;x=[a*d/sum(x) for a in x]
        W=[(s,a) for s,a in zip(M,x) if a];assert sum(a for s,a in W)==d and all(sum(a for s,a in W if not s&t)<=k-1-t.bit_count() for t in I);out['fractional']=[(s,str(a)) for s,a in W]
    else:
        assert M==M0;res=linprog(B,A_ub=-A.T.astype(float),b_ub=-np.ones(len(M)),bounds=(0,None));w=[(t,Fraction(float(a)).limit_denominator()) for t,a in zip(T,res.x) if a>1e-8];assert all(sum(a for t,a in w if not s&t)>=1 for s in allowed);cap=sum(a*(k-1-t.bit_count()) for t,a in w);assert cap<d;out.update(cap=str(cap),dual=[(t,str(a)) for t,a in w])
    return out
if __name__=='__main__':
    info=json.loads((D/'ramsey_reuse_stress.json').read_text());out={}
    for n,k,d,steps in [(5,4,3,[1,-1]),(13,6,4,[1,-1,5,-5])]:
        H=[sum(1<<(j-1) for j in range(1,n) if (j-i)%n in {v%n for v in steps}) for i in range(1,n)];u,v=info[str(n)][0]['edge'];H[u-1]^=1<<(v-1);H[v-1]^=1<<(u-1);out[str(n)]=test(H,k,d,info[str(n)][0]['old']);print(n,out[str(n)],flush=True)
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());out['35']=test(attach(p['stem_graphs'][-1],p['alternate']['to34']),10,4,info['35']['old']);print('35',out['35'],flush=True);(D/'ramsey_fractional_reuse.json').write_text(json.dumps(out)+'\n')
