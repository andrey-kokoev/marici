"""Replay the fixed random prefix. Test every border at 26 and every pair sign."""
from random import Random
from ramsey_39_pattern_border import borders

def add(n,p,pairs,ind):
    b=1<<n
    return pairs+[b|1<<i for i in range(n) if p>>i&1],ind+[s|b for s in ind if not s&p]

def options(n,pairs,ind):return list(borders(n,pairs,[s for s in ind if s.bit_count()==8]))

def main():
    rng=Random(39);pairs=[];ind=[0]
    for n in range(26):
        p=rng.choice(options(n,pairs,ind));pairs,ind=add(n,p,pairs,ind)
    opts=options(26,pairs,ind);chosen=rng.choice(opts)
    for p in opts:
        child=options(27,*add(26,p,pairs,ind));partners={q for q in opts if not(p&q) or all(s&(p|q) for s in ind if s.bit_count()==7)}
        assert partners=={v%(1<<26) for v in child}
        print([i+1 for i in range(26) if p>>i&1],p==chosen,len(partners),len(child))
    common=opts[0];union=0
    for p in opts:common &=p;union |=p
    print('shared positives',[i+1 for i in range(26) if common>>i&1]);print('common missed seven',next(([i+1 for i in range(26) if s>>i&1] for s in ind if s.bit_count()==7 and not s&union),None))
if __name__=='__main__':main()
