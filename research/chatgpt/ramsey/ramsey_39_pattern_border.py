"""Generate borders from the two forbidden patterns by unit propagation + branching.
Start empty. Select a legal border uniformly; no target matrix or distance rule.
"""
from itertools import combinations
from random import Random


def borders(n, pairs, octets):
    full=(1<<n)-1
    def search(pos, neg):
        while True:
            before=pos|neg
            for clauses,yes,no in ((pairs,False,True),(octets,True,False)):
                for c in clauses:
                    if c & (pos if yes else neg):continue
                    free=c & ~(pos|neg)
                    if not free:return
                    if not free&(free-1):
                        if yes:pos|=free
                        else:neg|=free
            if before==pos|neg:break
        free=full&~(pos|neg)
        if not free:yield pos;return
        b=free&-free
        yield from search(pos,neg|b);yield from search(pos|b,neg)
    yield from search(0,0)


def run(seed=39):
    rng=Random(seed);ind=[0];pairs=[];n=0
    while True:
        octets=[s for s in ind if s.bit_count()==8]
        opts=list(borders(n,pairs,octets));expected={p for p in ind if all(p&s for s in octets)}
        assert len(opts)==len(expected) and set(opts)==expected
        print(n,len(pairs),len(octets),len(opts))
        if not opts:return n
        p=rng.choice(opts);bit=1<<n
        pairs.extend(bit|(1<<i) for i in range(n) if p>>i&1)
        ind+= [s|bit for s in ind if not s&p];assert max(map(int.bit_count,ind))<=8
        n+=1

if __name__=='__main__':run()
