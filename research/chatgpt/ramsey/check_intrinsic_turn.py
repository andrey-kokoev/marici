"""Can an incoming red edge specify a non-return red step on the 8-vertex witness?"""
from collections import Counter
from itertools import combinations

N = [{(v-1)%8,(v+1)%8,(v+4)%8} for v in range(8)]
def squares(u,v):
    return sum(y in N[x] for x in N[u]-{v} for y in N[v]-{u} if x!=y)

def main():
    p=lambda x:(-x)%8
    assert all({p(w) for w in N[v]}==N[p(v)] for v in range(8))
    assert (p(4),p(0))==(4,0) and p(1)==7 and p(7)==1
    counts=Counter(squares(u,v) for u,v in combinations(range(8),2) if v in N[u]);assert counts=={1:8,2:4}
    for v in range(8):
        for u in N[v]:
            choices=[w for w in N[v]-{u} if squares(v,w)==squares(u,v)]
            assert len(choices)==(1 if squares(u,v)==1 else 0)
    print('Red edges by number of incident red squares:',sorted(counts.items()))
    print('Incoming 4->0: reflection fixes the input and exchanges exits 1 and 7.')
if __name__=='__main__':main()
