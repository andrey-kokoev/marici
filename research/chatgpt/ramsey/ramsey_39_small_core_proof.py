"""Targeted obstruction for a (3,8;27,80) graph. Inputs: published smaller (3,7) edge minima
and the published count 15 of (3,7;20,44) cores. No order-27 (3,8) catalogue.
uv run --with igraph --with python-sat python ramsey_39_small_core_proof.py
"""
from pathlib import Path
from itertools import combinations
from ramsey_border_order import unpack,key,graph
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType
from pysat.formula import IDPool

FILE=Path(__file__).with_name('ramsey_37_20_44_cores.txt')
def profiles():
    sol=[]
    for a in range(28):
        for b in range(28-a):
            d=2*a+b-2;c=27-a-b-d
            if min(c,d)<0:continue
            slack=2160-(76*a+76*b+80*c+86*d)
            if slack>=0:sol.append((a,b,c,d,slack));assert c>slack
    return sol

def test(m):
    g=graph(20,m);assert key(g)==m and g.ecount()==44 and g.clique_number()==2 and g.independence_number()==6
    I=[0]
    for i,nb in enumerate(g.get_adjlist()):
        e=sum(1<<j for j in nb);I += [s|1<<i for s in I if not s&e]
    # 6 neighbors of root have no mutual edges. Only 6x20 cross links unknown.
    pool=IDPool();X=[[pool.id((i,j)) for j in range(20)] for i in range(6)];C=[]
    for row in X:
        for a,b in g.get_edgelist():C.append([-row[a],-row[b]])
    C+=CardEnc.equals([v for row in X for v in row],bound=30,vpool=pool).clauses
    # Safe symmetry break: order rows lexicographically (least first).
    for a,b in zip(X,X[1:]):
        prefix=None
        for x,y in zip(a,b):
            pre=[] if prefix is None else [-prefix];C.append(pre+[-x,y]);nxt=pool.id();C.append(pre+[x,y,nxt]);C.append(pre+[-x,-y,nxt]);prefix=nxt
    for s in I:
        k=8-s.bit_count()
        if k<=6:
            js=[j for j in range(20) if s>>j&1]
            for ids in combinations(range(6),k):C.append([X[i][j] for i in ids for j in js])
    for col in range(20):
        ls=[row[col] for row in X];d=g.degree(col);lo=max(0,4-d);hi=min(6,7-d)
        if lo:C+=CardEnc.atleast(ls,bound=lo,vpool=pool).clauses
        if hi<len(ls):C+=CardEnc.atmost(ls,bound=hi,vpool=pool).clauses
    for row in X:
        C+=CardEnc.atleast(row,bound=3,vpool=pool).clauses;C+=CardEnc.atmost(row,bound=6,vpool=pool).clauses
    with Solver(name='cadical195',bootstrap_with=C) as sat:return sat.solve()
if __name__=='__main__':
    print(profiles());cores=[int(s,16) for s in FILE.read_text().split()];assert len(set(cores))==len(cores)==15
    for i,m in enumerate(cores):print(i+1,test(m),flush=True)
