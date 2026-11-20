"""Enumerate cyclic distance classes without an offset seed. Fixed compute budget, no target order."""
from itertools import combinations
from time import monotonic

def search(n,deadline):
    full=(1<<n)-1
    def rows(d):return [((d<<i)|(d>>(n-i)))&full for i in range(n)]
    def blue_nine(d):
        adj=[full^v^(1<<i) for i,v in enumerate(rows(d))]
        def has(m,k):
            if not k:return True
            while m.bit_count()>=k:
                b=m&-m;m^=b
                if has(m&adj[b.bit_length()-1],k-1):return True
            return False
        return has(adj[0],8) # translate any nine-set to contain zero
    def visit(k,d):
        if monotonic()>deadline:raise TimeoutError
        if k>n//2:return None if blue_nine(d) else d
        e=d|1<<k|1<<(n-k);r=rows(e)
        if all(not(e&r[i]) for i in range(1,n) if e>>i&1):
            out=visit(k+1,e)
            if out is not None:return out
        return visit(k+1,d)
    return visit(1,0)

def verify(n,d):
    # Independent verification of every border: maintain all blue cliques of the prefix.
    blue=[0]
    for j in range(n):
        red=sum(1<<i for i in range(j) if d>>((j-i)%n)&1)
        assert red in blue and all(red&s for s in blue if s.bit_count()==8)
        blue += [s|1<<j for s in blue if not s&red]
    return max(s.bit_count() for s in blue)
if __name__=='__main__':
    deadline=monotonic()+20;n=1
    try:
        while True:
            d=search(n,deadline)
            print(n,None if d is None else ([i for i in range(1,n//2+1) if d>>i&1],verify(n,d)),flush=True)
            # A cyclic graph can have noncyclic induced subgraphs: skip gaps.
            n+=1
    except TimeoutError:print('budget expired at',n)
