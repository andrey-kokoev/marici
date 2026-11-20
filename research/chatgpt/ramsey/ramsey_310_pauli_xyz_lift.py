"""Exact remaining one-qubit case: I plus all three nonidentity Pauli suffixes.
Requires python-sat. Small changed-edge vertex covers (<=3) were already excluded
by the 36-core rebuild. A complement of any one nonidentity class within the
support is a vertex cover. Search for valid 39 graphs and unrestricted borders.
"""
from collections import Counter
from itertools import combinations, product
from pysat.card import CardEnc
from pysat.solvers import Solver
from exoo39_symbolic_relations import edges

def flip(x,y):return bool(x and y and x!=y)
def main():
    E=edges(); V=range(39); C=range(4); var=lambda i,c:4*i+c+1
    clauses=[];top=156
    for i in V:
        row=[var(i,c) for c in C];clauses.append(row);clauses.extend([-x,-y] for x,y in combinations(row,2))
    for c in (1,2,3):
        clauses.append([var(i,c) for i in V]);card=CardEnc.atleast([var(i,t) for i in V for t in (1,2,3) if t!=c],4,top_id=top);clauses+=card.clauses;top=card.nv
    for c in (2,3):
        for i in V:clauses.append([-var(i,c)]+[var(j,c-1) for j in range(i)])
    pairs=list(combinations(range(3),2));patterns={p:[cs for cs in product(C,repeat=3) if all(r^flip(cs[i],cs[j]) for r,(i,j) in zip(p,pairs))] for p in product((0,1),repeat=3)}
    for vs in combinations(V,3):
        p=tuple(e in E for e in combinations(vs,2));clauses.extend([-var(i,c) for i,c in zip(vs,cs)] for cs in patterns[p])
    stats=Counter();print('input clauses',len(clauses),flush=True)
    with Solver(name='cadical195',bootstrap_with=clauses) as sol:
        while sol.solve():
            model=set(sol.get_model());cs=[next(c for c in C if var(i,c) in model) for i in V];adj=[0]*39
            for i,j in combinations(V,2):
                if ((i,j) in E)^flip(cs[i],cs[j]):adj[i]|=1<<j;adj[j]|=1<<i
            assert all(not(adj[i]&adj[j]) for i,j in combinations(V,2) if adj[i]>>j&1);stats['tested']+=1
            sets=[0];bad=0
            for i,row in enumerate(adj):
                born=[s|1<<i for s in sets if not s&row];bad=next((s for s in born if s.bit_count()==10),0)
                if bad:break
                sets+=born
            if bad:sol.add_clause([-var(i,cs[i]) for i in V if bad>>i&1]);continue
            stats['valid39']+=1;nine=[s for s in sets if s.bit_count()==9];border=next((s for s in sets if all(s&t for t in nine)),None)
            if border is not None:print('WITNESS',cs,border);return
            sol.add_clause([-var(i,cs[i]) for i in V]);
        print('UNSAT',dict(stats),flush=True)
if __name__=='__main__':main()
