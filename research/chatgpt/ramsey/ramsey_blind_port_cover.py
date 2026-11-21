"""Rank supports and cover the relaxed four-port problem using only core maximum rows (no valid completions)."""
from ramsey_final_miss_levels import D,json,bits,attach
from collections import Counter
from itertools import combinations

def predict(H,k,d=4):
    I=[0]
    for v,r in enumerate(H):I += [s|1<<v for s in I if not s&r]
    M=[s for s in I if all(s>>i&1 or s&r for i,r in enumerate(H))];T=[s for s in I if s.bit_count()==k-2];m=len(M);F=(1<<len(T))-1;col=[sum(1<<i for i,t in enumerate(T) if t>>v&1) for v in range(len(H))];miss=[]
    for s in M:
        h=0
        for v in bits(s):h|=col[v]
        miss.append(F^h)
    adj=[sum(1<<j for j in range(i,m) if not x&miss[j]) for i,x in enumerate(miss)];q=[]
    def enum(p,opts):
        if len(p)==d:q.append(p);return
        for v in bits(opts):enum(p+[v],opts&adj[v])
    enum([], (1<<m)-1);inc=Counter(t for row in q for t in set(row));pool=q;cover=[]
    while pool:
        c=Counter(t for row in pool for t in set(row));v,n=c.most_common(1)[0];cover.append([M[v],n]);pool=[r for r in pool if v not in r]
    # Can a smaller hitting set cover every relaxed solution? branch on an uncovered tuple.
    def hit(rows,depth):
        if not rows:return []
        if depth==0:return None
        for v in set(rows[0]):
            ans=hit([r for r in rows if v not in r],depth-1)
            if ans is not None:return [v]+ans
    exact=None
    for size in range(1,min(len(cover),5)+1):
        exact=hit(q,size)
        if exact is not None:break
    top={v for v,_ in inc.most_common(3)};outside=[r for r in q if top.isdisjoint(r)];Fcore=(1<<len(H))-1
    from ramsey_port_deletion_chain import independent
    after7=[r for r in outside if all(not independent(H,Fcore^(M[i]|M[j]|M[l]),k-3) for i,j,l in combinations(r,3))];after6=[r for r in after7 if not independent(H,Fcore^(M[r[0]]|M[r[1]]|M[r[2]]|M[r[3]]),k-4)]
    return {'outside_top3':[len(outside),len(after7),len(after6)],'q':len(q),'active':len(inc),'greedy_cover':cover,'exact_cover':None if exact is None else [M[v] for v in exact], 'ranking':[[M[v],n,miss[v].bit_count()] for v,n in inc.most_common(12)],'fewest_misses':sorted((x.bit_count(),s) for s,x in zip(M,miss))[:12]}
if __name__=='__main__':
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());B=p['stem_graphs'][-1];H=attach(B,p['alternate']['to34']);r=predict(H,10);print(r);(D/'ramsey_blind_port_cover.json').write_text(json.dumps(r)+'\n')
