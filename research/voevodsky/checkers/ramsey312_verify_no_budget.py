"""Independent finite-rectangle replay: generate missed sets directly on the 46-core, without using the original eleven catalog. Shrink the challenge by activation literals, then verify every partition separately."""
from ramsey312_exact_four_cover import *
from itertools import combinations
from functools import reduce
from operator import or_,and_
from collections import Counter

def main():
 suffix=sys.argv[1] if len(sys.argv)>1 else '';z=json.loads((D/f'ramsey312_no_budget{suffix}.json').read_text());d=z['d'];ss=z['challenge'];h=F^d;ds=list(bits(d));A={i:adj[i]&h for i in ds};el=list(sets(h,11));assert all(x&~h==0 and all(not x&adj[i] for i in bits(x)) and all(x&t for t in el) for x in ss);full=(1<<len(ss))-1;col=[sum(1<<j for j,x in enumerate(ss) if x>>i&1) for i in range(52)];rows=[];groups={};raw=0
 for k in range(1,7):
    for grp in combinations(ds,k):
        g=sum(1<<v for v in grp);B=reduce(and_,(A[i] for i in grp));P=h&~reduce(or_,(A[i] for i in grp));cs=set()
        if B:
            for t in sets(P,11-k):
                mask=full
                for i in bits(t):mask&=~col[i]
                for i in bits(B):raw+=1;cs.add(mask&col[i])
        mx=[]
        for r in sorted(cs,key=int.bit_count,reverse=True):
            if r and not any(r&~p==0 for p in mx):mx.append(r);rows.append((g,r));groups.setdefault(g,[]).append(len(rows))
 pool=IDPool(start_from=len(rows)+1);incs=[[] for _ in ss];base=[]
 for i in ds:base+=CardEnc.atmost([j for j,(g,r) in enumerate(rows,1) if g>>i&1],1,vpool=pool).clauses
 for j,(g,r) in enumerate(rows,1):
    for i in bits(r):incs[i].append(j)
 gates=[pool.id(('gate',i)) for i in range(len(ss))];
 kept=list(range(len(ss)));union=set();cnt=Counter();possible=0
 def parts(m):
    if not m:yield [];return
    g=m;b=m&-m
    while g:
        if g&b:
            for p in parts(m^g):yield [g]+p
        g=(g-1)&m
 for p in parts(d):
    cnt[tuple(sorted(g.bit_count() for g in p))]+=1
    if not all(g in groups for g in p):continue
    possible+=1;allowed={j for g in p for j in groups[g]};clauses=[[-gates[i],*[j for j in incs[i] if j in allowed]] for i in kept];aux=IDPool(start_from=max(gates)+1)
    for g in p:clauses+=CardEnc.equals(groups[g],1,vpool=aux).clauses
    with Solver(name='g4',bootstrap_with=clauses) as sl:
        assert not sl.solve(assumptions=gates);small=sl.get_core() or [];union.update(gates.index(a) for a in small)
 kept=sorted(union)
 print('legal challenge',len(ss),'sufficient',len(kept),'all partitions',sum(cnt.values()),'nonempty classes',possible,'raw',raw,'maximal',len(rows));(D/f'ramsey312_no_budget{suffix}_replay.json').write_text(json.dumps(dict(d=ds,obstruction=[ss[i] for i in kept],partitions=sum(cnt.values()),nonempty=possible,raw_classes=raw,maximal_rows=len(rows))))
if __name__=='__main__':main()
