"""Exact point-evaluation pseudoexpectation for raw, unquadratized recurrence generators.
Degree means generator-wise (Macaulay) total degree, not degree after cancellation.
Run a second control substituting triangle-forced zero edges first.
"""
from r37_exchange_falsifier import a,blades,legal,independent
from itertools import combinations
X=range(6,22); rootmask=63

def attack(simplify):
    # At a fixed integral edge point, each surviving recurrence either forces
    # zero or identifies two flags. Independent flags have no zero factor.
    # Components connected to b_empty=1 must remain one; others may be zero.
    parent={}
    def find(s):
        while s!=parent[s]:s=parent[s]
        return s
    for k in range(7):
        for t in combinations(X,k):
            if not independent(a,t):continue
            s=frozenset(t);parent[s]=s
            for v in s:
                p=s-{v}
                factors=sum(not simplify or not(a[u]&a[v]&rootmask) for u in p)
                if factors+1<=4:parent[find(s)]=find(p)
    one=find(frozenset());return sum(find(s)==one for s in blades(a))

if __name__=='__main__':
    assert legal(a) and len(blades(a))==10
    print('minimum integral flag objective over given edges, raw / overlap-simplified:',attack(False),attack(True))
