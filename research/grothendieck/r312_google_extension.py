"""Extension audit; zero-based vertex labels in archived matrix order."""
from verify_r312_google_52 import adj,n
from collections import Counter

def sets(p,k,s=0):
    if not k:
        yield s
        return
    while p.bit_count()>=k:
        b=p&-p; p^=b
        yield from sets(p&~adj[b.bit_length()-1],k-1,s|b)

def labels(m):return [i for i in range(n) if m>>i&1]
if __name__=='__main__':
    low=sum(1<<i for i in range(n) if adj[i].bit_count()==10)
    hist=Counter(s&low for s in sets((1<<n)-1,11))
    best=sum(hist.values());solutions=[];tested=0;t=low
    while True:
        if not any(adj[i]&t for i in labels(t)):
            tested+=1;miss=sum(v for k,v in hist.items() if not k&t)
            if miss<best: best=miss;solutions=[]
            if miss==best:solutions.append(labels(t))
        if not t:break
        t=(t-1)&low
    print('old 11-sets',sum(hist.values()),'entirely degree 11',hist[0], 'example',labels(next(sets(((1<<n)-1)^low,11))))
    print('low',labels(low),'independent neighborhoods',tested,'minimum missed',best,'optimizers',solutions)
