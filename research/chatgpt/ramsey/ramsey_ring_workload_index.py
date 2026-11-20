"""Record the actual two-ring triangle-filter workload. Replay plans including index builds."""
from contextlib import redirect_stdout
from io import StringIO
from statistics import median
from time import perf_counter_ns
from random import Random
from ramsey_target_two_rings import find


def direct(u,d,rd,n):return any(u>>j&1 and (d&rd[j]) for j in range(n))
def bitmap(d,rd):return sum(1<<j for j,r in enumerate(rd) if d&r)

def run(k):
    scopes=[]
    def factory(n,offsets):
        queries=[];scopes.append((n,offsets,queries))
        def record(u,d,rd):
            hit=direct(u,d,rd,n);queries.append((u,d,rd,hit));return hit
        return record
    with redirect_stdout(StringIO()):rows=find(k,factory,False)
    def replay(plan):
        answers=[];peak=0;built=0
        for n,offsets,queries in scopes:
            idx={d:bitmap(d,rd) for d,rd in offsets} if plan=='full' else {}
            for u,d,rd,_ in queries:
                if plan=='direct':hit=direct(u,d,rd,n)
                elif plan=='memo':
                    key=(u,d)
                    if key not in idx:idx[key]=direct(u,d,rd,n)
                    hit=idx[key]
                else:
                    if d not in idx:idx[d]=bitmap(d,rd)
                    hit=bool(u&idx[d])
                answers.append(hit)
            peak=max(peak,len(idx));built+=len(idx)
        return answers,peak,built
    ref=[hit for _,_,qs in scopes for *_,hit in qs];times={p:[] for p in ('direct','memo','lazy','full')};rng=Random(37);stats={}
    for _ in range(15):
        names=list(times);rng.shuffle(names)
        for p in names:
            t=perf_counter_ns();ans,peak,built=replay(p);times[p].append((perf_counter_ns()-t)/1e6);assert ans==ref;stats[p]=(peak,built)
    print(k,len(rows),len(ref),{p:(round(median(v),2),*stats[p]) for p,v in times.items()})

if __name__=='__main__':run(6);run(7)
