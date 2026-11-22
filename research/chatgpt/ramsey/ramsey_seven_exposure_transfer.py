"""Transfer the proved extension filter to seven-sets of 34-cores. Count all pairwise-eight-compatible maximal-support multisets by degree capacity and ALL detected obstruction classes (not only first witness)."""
from functools import lru_cache
from collections import Counter
from itertools import combinations
from ramsey_deletion_rank_new_parents import induce,graph,D,json
from ramsey_fork_audit_uniform import grow,inds
from ramsey_final_miss_levels import levels,bits

def audit(H):
    T=[s for s in inds(H) if s.bit_count()==7];F=(1<<34)-1;kinds=[0]*3;pop=Counter();degrees=list(map(int.bit_count,H))
    def kind(s):
        v=s
        for i in bits(s):v|=H[i]
        x=F^v;return 0 if not x else 1 if x.bit_count()==1 and degrees[x.bit_length()-1]<=7 else 2
    for i,s in enumerate(T):k=kind(s);kinds[k]|=1<<i;pop[k]+=1
    hits=[sum(1<<i for i,s in enumerate(T) if s>>v&1) for v in range(34)];allrows=(1<<len(T))-1
    @lru_cache(None)
    def miss(s):
        z=0
        for v in bits(s):z|=hits[v]
        return allrows^z
    d=[sum(1<<i for i,v in enumerate(degrees) if v>=n) for n in (8,7,6)]
    @lru_cache(maxsize=300000)
    def triple(a,b,c):
        m=miss(a)&miss(b)&miss(c);return sum(1<<k for k,z in enumerate(kinds) if z&m)
    counts=Counter();ex={}
    def collect(S,tag,obs):
        a,b,c,e=S;cap=not (d[0]&((a&b)|((a|b)&c)|((a|b|c)&e)) or d[1]&((a&b&c)|(((a&b)|((a|b)&c))&e)) or d[2]&a&b&c&e);mask=0
        if tag=='fails_triple':
            for t in combinations(S,3):mask|=triple(*t)
            assert mask and (not cap or not(mask&4))
        key=f'{int(cap)}:{mask}:{tag}';counts[key]+=1;ex.setdefault(key,dict(supports=S,missed=obs))
    levels(H,on_classified=collect);return dict(pool=pop,counts=counts,examples=ex,endpoint_row_classes={u:kind(H[u]) for u in range(34) if degrees[u]==7})
if __name__=='__main__':
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());B=p['stem_graphs'][-1];U=p['to35'][1:];C=grow(B,U);E=grow(B,p['alternate']['to34']);G=induce(graph((1,7,11,16)),list(range(1,35)));G[0]|=1<<33;G[33]|=1;G[11]^=1<<22;G[22]^=1<<11;out={}
    for name,H in [('matched_failure',G),('intact',C),('thinned',E)]:out[name]=audit(H);print(name,out[name]['counts'],flush=True)
    (D/'ramsey_seven_exposure_transfer.json').write_text(json.dumps(out)+'\n')
