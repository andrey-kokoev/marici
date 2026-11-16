"""Exact Hall-contact identity and arbitrary-order missing simplicial fillers.
A edges are red; B denotes their complement. Standard library only.
"""
from itertools import combinations


def graph(m, t, births):
    assert m >= 3 and 0 <= t <= m-2 and births >= 0
    r = m-1-t
    n = m-1+t+births
    G = [0]*n
    def add(u,v):
        G[u] |= 1<<v
        G[v] |= 1<<u
    # Pure B carrier L = range(m-1). First t separate single-contact arms.
    for i in range(t):
        add(i,m-1+i)
    # Remaining r contact vertices each contact every new birth.
    for j in range(births):
        for i in range(t,m-1):
            add(i,m-1+t+j)
    return G


def max_independent(G):
    n=len(G)
    # A clique in B is an independent set in A.
    def solve(mask):
        if not mask:return 0
        # Choose branch node with most A-neighbors in active set.
        nodes=[i for i in range(n) if mask>>i&1]
        v=max(nodes,key=lambda i:(G[i]&mask).bit_count())
        without=mask&~(1<<v)
        return max(solve(without),1+solve(without&~G[v]))
    return solve((1<<n)-1)


def is_triangle_free(G):
    return all((G[i]&G[j])==0 for i in range(len(G)) for j in range(i+1,len(G)) if G[i]>>j&1)


def hall_capacity(G,ell):
    H=range(ell,len(G))
    x=[sum((1<<i) for i in range(ell) if G[u]>>i&1) for u in H]
    adj=[sum(1<<j for j in range(len(x)) if j!=i and G[u]>>(ell+j)&1)
         for i,u in enumerate(H)]
    mx=-10**6
    deficits={}
    for bits in range(1<<len(x)):
        if any(bits>>i&1 and (adj[i]&bits) for i in range(len(x))):continue
        contacts=0
        for i,s in enumerate(x):
            if bits>>i&1: contacts |= s
        delta=bits.bit_count()-contacts.bit_count()
        mx=max(mx,delta)
        deficits[bits]=delta
    return ell+mx,deficits


def main():
    for m,t in [(4,1),(5,1),(6,3),(6,2),(6,1),(7,2),(8,2)]:
        r=m-1-t
        for births in range(r+2):
            G=graph(m,t,births)
            assert is_triangle_free(G)
            expected=t+max(r,births)
            assert max_independent(G)==expected,(m,t,births)
            if len(G)<=17:
                hall,_=hall_capacity(G,m-1)
                assert hall==expected
            assert (expected<=m-1)==(births<=r)
        print(f'm={m}, base contacts t={t}, residual contacts r={r}: '
              f'{r+1} birth channels, all proper subsets admissible; '
              f'all {r+1} births create B K_{m}. '
              f'Completion complex boundary Delta^{r}, H_{r-1}=Z.')
    print('All exact comparisons passed.')

if __name__=='__main__':main()
