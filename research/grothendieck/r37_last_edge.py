"""Compute unit proof rounds and single-edge flip certificates in catalogue labels."""
from itertools import combinations
from r37_reconstruct_catalogue import equality_cases
X=range(6,22);E={e:i+1 for i,e in enumerate(combinations(X,2))};rev={v:e for e,v in E.items()}
for idx,o,g,B in equality_cases((10,12)):
    if len(B)!=10 and not(idx==16 and o[:6]==[0,1,2,3,5,7]):continue
    known={-v for (i,j),v in E.items() if g[i]&g[j]&63 or any({i,j}<=s for s in B)};C=[]
    def add(t,sign,name):C.append(([sign*E[e] for e in combinations(t,2)],name,t))
    for t in combinations(X,3):add(t,-1,'triangle')
    for t in combinations(X,6):
        if frozenset(t) not in B:add(t,1,'absent six')
    for k in range(2,8):
        for t in combinations(X,k):
            u=0
            for i in t:u|=g[i]&63
            if u.bit_count()<k:add(t,1,'seven')
    while True:
        new={}
        for c,name,t in C:
            if any(v in known for v in c):continue
            r=[v for v in c if -v not in known];assert r
            if len(r)==1:new.setdefault(r[0],(name,[o[i] for i in t]))
        if not new:break
        last=new;known.update(new)
    def edge(v):return tuple(o[i] for i in rev[abs(v)])
    print(idx,o[:6],len(B),'last',[(edge(v),v>0,src) for v,src in last.items()],'free',[edge(v) for v in rev if v not in known and -v not in known])
    if len(B)==12:
        vertices=[o.index(i) for i in (9,14)];i,j=vertices
        common=[v for v in range(22) if v not in vertices and not((g[i]|g[j])>>v&1)]
        for pool,k in [(set(common)&set(X),4),(common,5)]:
            counts=[sum(all(not(g[x]>>y&1) for x,y in combinations(t,2)) for t in combinations(pool,d)) for d in range(1,k+1)]
            print('blue common-neighbor subsets by size',counts)
