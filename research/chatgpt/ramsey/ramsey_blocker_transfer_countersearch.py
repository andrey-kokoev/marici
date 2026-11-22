"""Frozen blocker rule on new cores. Exhaustively audit every independent partial support of each tested repairable triple; enumerate maximal repairs as independent oracle. Stop on first false acceptance."""
from itertools import combinations,combinations_with_replacement
from random import Random
from ramsey_fork_audit_uniform import D,json,inds,grow,verify
from ramsey_final_miss_levels import bits

def audit(H,stats):
    I=inds(H);n=len(H);F=(1<<n)-1;k=max(s.bit_count() for s in I)+2
    if k<5:return
    M=[s for s in I if all(s>>v&1 or s&r for v,r in enumerate(H))];N={0:0}
    for s in sorted(I):
        if s:N[s]=N[s&(s-1)]|H[(s&-s).bit_length()-1]
    for q in combinations_with_replacement(M,3):
        z=[(t,k-1-t.bit_count()-sum(not(s&t) for s in q)) for t in I];
        if min(v for _,v in z)<0:continue
        T=[t for t,v in z if v==0];legal=[s for s in M if all(s&t for t in T)]
        if not legal:continue
        stats[0]+=1;false={s for s in I if not any(s&m==s for m in legal)}
        for s in sorted(false,key=lambda x:(x.bit_count(),x)):
            if any(s^(1<<v) in false for v in bits(s)):continue
            live=F^N[s];trace=[]
            while all(live&t for t in T):
                b=sum(1<<x for x in bits(live) if any(not(t&live&~H[x]) for t in T));trace.append(b)
                if not b:
                    verify(grow(H,[*q,legal[0]]),k);return dict(H=H,k=k,fixed=q,commit=s,live=live,rounds=trace,tight=T,legal_maximal=legal)
                live^=b
            stats[1]+=1

def run():
    rng=Random(743);stats=[0,0];tested=0
    for n in range(5,14):
        for _ in range(70):
            H=[0]*n;E=list(combinations(range(n),2));rng.shuffle(E)
            for x,y in E:
                if not H[x]&H[y] and rng.random()<.68:H[x]|=1<<y;H[y]|=1<<x
            tested+=1;r=audit(H,stats)
            if r:return dict(tested=tested,prior_tests=stats,example=r)
    return dict(tested=tested,prior_tests=stats,example=None)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_blocker_transfer_countersearch.json').write_text(json.dumps(out)+'\n')
