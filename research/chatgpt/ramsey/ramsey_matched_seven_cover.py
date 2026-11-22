"""Minimum old-row cover by DP over 11 assignments. Predeclared source-only pools: independent seven-vertex neighbourhoods of the parent, and of either deleted endpoint; compare against the exact minimum."""
from ramsey_deletion_rank_new_parents import graph,induce,D,json
from ramsey_fork_audit_uniform import inds
from ramsey_final_miss_levels import levels
from itertools import combinations

def run():
    P=induce(graph((1,7,11,16)),list(range(1,35)));P[0]|=1<<33;P[33]|=1;old=[t for t in inds(P) if t.bit_count()==7];pools={'all':set(old),'neighbourhood':set(P)&set(old),'endpoint_neighbourhood':{P[i] for i in [11,22]}&set(old)};pools['endpoint_minus_partner']={P[11]&~(1<<22),P[22]&~(1<<11)}&set(old);Q=[];good=[]
    for (x,y),bucket in [((11,22),Q),((16,17),good)]:
        G=P[:];G[x]^=1<<y;G[y]^=1<<x;pair=1<<x|1<<y;levels(G,on_classified=lambda S,tag,obs:bucket.append(S) if any(s&pair==pair for s in S) else None)
    assert (len(Q),len(good))==(11,138);full=(1<<len(Q))-1;cov={t:sum(1<<i for i,s in enumerate(Q) if sum(not(a&t) for a in s)>=3) for t in old};out={}
    for name,rows in pools.items():
        dp={0:()};reps={cov[t]:t for t in sorted(rows,reverse=True) if cov[t]}
        for mask,t in reps.items():
            for m,chain in list(dp.items()):
                n=m|mask
                if n not in dp or len(chain)+1<len(dp[n]):dp[n]=chain+(t,)
        best=dp[max(dp,key=lambda m:(m.bit_count(),-len(dp[m])))];out[name]=dict(rows=len(rows),nonempty_rows=sum(bool(cov[t]) for t in rows),distinct_masks=len(reps),max_covered=max(map(int.bit_count,dp)),certificate=[dict(vertices=[i for i in range(34) if t>>i&1],mask=cov[t],neighbourhood_of=[i for i in range(34) if P[i]==t],max_success_misses=max(sum(not(s&t) for s in S) for S in good)) for t in best]);assert all(sum(not(s&t) for s in S)<=2 for t in best for S in good)
    trace=[]
    for u,v in [(11,22),(22,11)]:
        t=P[u]&~(1<<v);trace.append(dict(center=u,size=t.bit_count(),mask=cov.get(t,0),owners=[sum(bool(s&(1<<u)) for s in S) for S in Q],misses=[sum(not(s&t) for s in S) for S in Q]))
    return dict(summary=out,universal_count=sum(m==full for m in cov.values()),endpoint_trace=trace,failed_assignments=Q)
if __name__=='__main__':
    out=run();print(out['summary']);(D/'ramsey_matched_seven_cover.json').write_text(json.dumps(out)+'\n')
