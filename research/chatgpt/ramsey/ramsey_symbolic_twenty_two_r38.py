"""Symbolic R(3,8) seeds and exact labeled extension counts up to three columns.
uv run --with python-sat -- python research/chatgpt/ramsey/ramsey_symbolic_twenty_two_r38.py
"""
from itertools import combinations
from collections import Counter
from pysat.solvers import Solver
from pauli_realization_audit import independent_witness,triangle_free,encode_graph6

def symbolic(n):
    E=lambda i,j:j*(j-1)//2+i+1
    with Solver(name='cadical195') as s:
        for t in combinations(range(n),3):s.add_clause([-E(i,j) for i,j in combinations(t,2)])
        while s.solve():
            pos=set(s.get_model());a=[0]*n
            for i,j in combinations(range(n),2):
                if E(i,j) in pos:a[i]|=1<<j;a[j]|=1<<i
            t=independent_witness(a,8)
            if t is None:return a
            s.add_clause([E(i,j) for i,j in combinations(sorted(t),2)])
    raise ValueError('no seed')

def run(a):
    assert len(a)==22 and triangle_free(a) and independent_witness(a,8) is None
    N=(1<<22)-1;inds=[0]
    for i,r in enumerate(a):inds += [m|1<<i for m in inds if not m&r]
    sevens=[m for m in inds if m.bit_count()==7];c=[m for m in inds if all(m&z for z in sevens)]
    from functools import lru_cache
    @lru_cache(None)
    def safe(mask,k):return independent_witness(a,k,N^mask) is None
    # Pair of new vertices: when joined, they must have disjoint supports;
    # when unjoined their joint nonneighbors cannot contain an independent six.
    adj=[{} for _ in c]
    for i,x in enumerate(c):
        for j in range(i,len(c)):
            y=c[j];options=[e for e,ok in [(1,not(x&y)),(0,safe(x|y,6))] if ok]
            if options:adj[i][j]=adj[j][i]=options
    pairs=triples=0;extendible=set();example=None
    for i,row in enumerate(adj):
        for j,ij in row.items():
            pairs+=len(ij)
            for k in row.keys() & adj[j].keys():
                for b in ij:
                    for d in row[k]:
                        for e in adj[j][k]:
                            total=b+d+e
                            if total==3 or (not total and not safe(c[i]|c[j]|c[k],5)):continue
                            triples+=1;extendible.add((i,j,b))
                            if example is None:example=([c[i],c[j],c[k]],(b,d,e))
    print('seed',encode_graph6(a),'independent sevens',len(sevens),'ordered extension counts',len(c),pairs,triples,'first columns allowing a second',sum(bool(r) for r in adj),'ordered pairs allowing a third',len(extendible),flush=True)
    if example:
        supports,links=example;g=a[:]+[0]*3
        for j,m in enumerate(supports,22):
            for i in range(22):
                if m>>i&1:g[i]|=1<<j;g[j]|=1<<i
        for (i,j),b in zip(combinations(range(22,25),2),links):
            if b:g[i]|=1<<j;g[j]|=1<<i
        assert triangle_free(g) and independent_witness(g,8) is None
        print('example',[[i for i in range(22) if m>>i&1] for m in supports],links,flush=True)
if __name__=='__main__':
    for n in (22,25):run([r&((1<<22)-1) for r in symbolic(n)[:22]])
