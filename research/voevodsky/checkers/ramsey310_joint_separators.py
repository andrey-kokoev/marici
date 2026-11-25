"""uv run --with scipy python ... . Find shared linear demand certificates; verify in integers."""
from ramsey310_s3_local_transfer import D,F,sets,product,json
from fractions import Fraction
from math import lcm,gcd
from functools import reduce

def instances():
    for i,r in enumerate(json.loads((D/'ramsey310_s3_local_transfer_r10.json').read_text())['uncut']):
        A=json.loads((D/'ramsey310_matching_degree3_types.json').read_text())[0];
        for x,y,z,w in r['path']:A[x]^=1<<y;A[y]^=1<<x;A[z]|=1<<w;A[w]|=1<<z
        for j,data in enumerate(json.loads((D/f'ramsey310_s3_all_ports_{i}_replay.json').read_text())):
            E=data['E'];d=[9-a.bit_count()-sum(s>>v&1 for s in E) for v,a in enumerate(A)];m=sum(1<<v for v,x in enumerate(d) if x==1);C=list(sets(A,F,7))
            for a,b,c in product(*zip(E[:3],E[3:])):C=[s for s in C if (s&m&~(a|b|c)).bit_count()<=1]
            for k in (6,7):
                for t in sets(A,F,k):
                    if 6-k+sum(bool(t&a and t&b) for a,b in zip(E[:3],E[3:]))==0:C=[s for s in C if s&t]
            assert len(C)>=6 and all(sum(s>>v&1 for s in C)>=x for v,x in enumerate(d));yield (i,j),d,C

def margin(w,d,C):
    total=sum(x*y for x,y in zip(w,d));top=sum(sorted((sum(x for v,x in enumerate(w) if s>>v&1) for s in C),reverse=True)[:6]);return [total,top]

def separate(cases):
    # Cutting-plane LP: find w with <w,d-sum B> >=1 for every six-row choice B.
    import numpy as np
    from scipy.optimize import linprog
    M=[];x=np.zeros(26)
    for step in range(500):
        cuts=[]
        for _,d,C in cases:
            B=np.array([[s>>v&1 for v in range(26)] for s in C]);v=B[np.argsort(B@x)[-6:]].sum(axis=0)-d
            if v@x>-.999999:cuts.append(np.r_[v,-v])
        if not cuts:
            f=[Fraction(float(y)).limit_denominator(100000) for y in x];den=lcm(*(z.denominator for z in f));w=[int(z*den) for z in f];g=reduce(gcd,w);w=[y//g for y in w];assert all(t>u for _,d,C in cases for t,u in [margin(w,d,C)]);return w
        M+=cuts;r=linprog(np.ones(52),A_ub=M,b_ub=[-1]*len(M));
        if r.status==2:return None
        assert r.success;x=r.x[:26]-r.x[26:]
    raise RuntimeError('iteration limit')

if __name__=='__main__':
    cases=list(instances());w=separate(cases);print('common',w,flush=True);out=[]
    for k,d,C in cases:
        y=w or separate([(k,d,C)]);out.append(dict(case=k,eligible=len(C),weights=y,check=margin(y,d,C) if y else None));print(k,out[-1]['check'],flush=True)
    (D/'ramsey310_joint_separators.json').write_text(json.dumps(dict(shared=w,cases=out)))
