"""Blind single-path tests. Score distinct partner patterns; ties use a fixed policy.
No catalogue, circular order, target witness, or backtracking."""
from random import Random
from collections import Counter

def run(policy,seed,k=7,trace=False):
    rng=Random(seed);I=[0];deg=[];rows=[]
    while True:
        n=len(deg);fam=[s for s in I if s.bit_count()==k-1];old=[s for s in I if s.bit_count()==k-2];opts=[p for p in I if all(p&s for s in fam)]
        if not opts:return rows if trace else n
        # Transpose the candidate table for fast unions of partner sets.
        inc=[sum(1<<j for j,p in enumerate(opts) if p>>i&1) for i in range(n)]
        def touch(p):
            b=0
            while p:t=p&-p;b|=inc[t.bit_length()-1];p^=t
            return b
        missed=[(s,~touch(s)) for s in old];leaders=[];low=len(opts)+1
        for p in opts:
            bad=0
            for s,qs in missed:
                if not s&p:bad|=qs
            losses=(touch(p)&bad).bit_count()
            if losses<low:leaders=[];low=losses
            if losses==low:leaders.append(p)
        def balance(p):
            d=[x+(p>>i&1) for i,x in enumerate(deg)]+[p.bit_count()];return len(d)*sum(x*x for x in d)-sum(d)**2
        def threats(p):return sum(not s&p for s in old) # new negative (k-1)-sets
        def worst_slack(p):
            available=sum(1<<i for i,d in enumerate(deg) if d+(p>>i&1)<k-1)
            old_min=min(((s&available).bit_count() for s in fam),default=k)
            new_min=min(((s&available).bit_count()+int(p.bit_count()<k-1) for s in old if not s&p),default=k)
            return -min(old_min,new_min)
        if policy!='random':
            key={'balance':balance,'fewest_threats':threats,'slack':worst_slack,'most_positive':lambda p:-p.bit_count()}[policy];scores=list(map(key,leaders));v=min(scores);leaders=[p for p,x in zip(leaders,scores) if x==v]
        p=rng.choice(leaders);rows.append(p);deg=[d+(p>>i&1) for i,d in enumerate(deg)]+[p.bit_count()];I += [s|1<<n for s in I if not s&p]
        assert max(s.bit_count() for s in I)<k
if __name__=='__main__':
    for policy in ('random','balance','fewest_threats','most_positive'):
        print(policy,sorted(Counter(run(policy,s) for s in range(40)).items()),flush=True)
