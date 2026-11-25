"""Exact distance-two changes in labeled exclusive masks, without testing intermediate moves.
Usage: python ... generate case-number pack-file candidates-file; after matching_supply.rs,
python ... check case-number survivors-file. Counts include changes of wiring by permutations.
"""
import sys,json
from functools import lru_cache
from itertools import combinations
from collections import Counter
from ramsey310_s3_local_transfer import D,F,E,sets,bits
import ramsey310_s3_local_transfer as replay

def run():
    mode,c,*args=sys.argv[1:];case=json.loads((D/'ramsey310_s3_local_transfer_r10.json').read_text())['uncut'][int(c)];A=json.loads((D/'ramsey310_matching_degree3_types.json').read_text())[0]
    for i,j,x,y in case['path']:A[i]^=1<<j;A[j]^=1<<i;A[x]|=1<<y;A[y]|=1<<x
    if mode=='check':
        hist=Counter();results=[]
        for line in open(args[0]):
            e=tuple(map(int,line.split()));replay.E=e;tag,cert=replay.examine(A);assert tag in ('pass','contrast');hist[tag]+=1;results.append(dict(rows=e,verdict=tag,certificate=cert))
        print(json.dumps(dict(case=c,counts=hist,survivors=results)));return
    lib={k:list(sets(A,F,k)) for k in (5,6,7)};S=lib[7];ss=set(S);assert len(ss)==len(S)
    with open(args[0],'w') as f:
        for a in (A,*lib.values()):print(len(a),*a,file=f)
    M={s:sum(1<<j for j,t in enumerate(S) if not t&s) for s in S};Q={s:sum(1<<j for j,t in enumerate(lib[6]) if not t&s) for s in S}
    @lru_cache(None)
    def pair(a,b):return a!=b and (a&b).bit_count()<=5 and not M[a]&M[b]
    def same(i,j):return i//3==j//3
    hist=Counter();edges=[(i,j) for i in range(26) for j in bits(A[i]&((1<<i)-1))]
    with open(args[1],'w') as f:
        for i,j in combinations(range(6),2):
            fixed=set(range(6))-{i,j};e=list(E)
            def domain(k):return [s for s in S if s!=E[k] and all(s!=E[h] and (not same(k,h) or pair(s,E[h])) and (abs(k-h)!=3 or not s&E[h]) for h in fixed)]
            ds=domain(j)
            for s in domain(i):
                e[i]=s
                for t in ds:
                    if t==s or (abs(i-j)==3 and t&s) or (same(i,j) and not pair(t,s)):continue
                    e[j]=t
                    if any(Q[a]&Q[b]&Q[c] for a,b,c in (e[:3],e[3:])):continue
                    hist['root_admissible']+=1
                    nd=[9-a.bit_count()-sum(z>>v&1 for z in e) for v,a in enumerate(A)]
                    if min(nd)<1 or max(nd)>6 or any(nd[x]+nd[y]>6 for x,y in edges):continue
                    hist['capacity']+=1
                    single=sum(1<<v for v,x in enumerate(nd) if x==1)
                    if any((single&~(e[3*(m&1)]|e[1+3*((m>>1)&1)]|e[2+3*((m>>2)&1)])).bit_count()>6 for m in range(8)):continue
                    hist['to_supply']+=1;print(*e,file=f)
    print(json.dumps(dict(case=c,counts=hist)))
if __name__=='__main__':run()
