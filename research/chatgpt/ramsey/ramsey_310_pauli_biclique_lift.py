"""Exact SAT search for the proposed I/X/Z lift of Exoo, with both sides >=4.
Run: uv run --with python-sat python ramsey_310_pauli_biclique_lift.py
One-hot labels; forbid precisely those labelled triples that become red triangles.
Then check blue tens and try every independent border against all blue nines.
"""
from itertools import combinations,product
from collections import Counter
from pysat.card import CardEnc
from pysat.solvers import Solver
from exoo39_symbolic_relations import edges

def main():
    E=edges(); V=range(39); A=[sum(1<<j for j in V if tuple(sorted((i,j))) in E) for i in V]; var=lambda i,c:3*i+c+1
    cnf=[];top=117
    for i in V:
        x=[var(i,c) for c in range(3)];cnf.append(x);cnf.extend([-u,-v] for u,v in combinations(x,2))
    for c in (1,2):
        card=CardEnc.atleast([var(i,c) for i in V],4,top_id=top);cnf.extend(card.clauses);top=card.nv
    # first nonidentity must be X, quotienting X/Z exchange.
    for i in V:cnf.append([-var(i,2)]+[var(j,1) for j in range(i)])
    tri=Counter();tab={}
    for patt in product((0,1),repeat=3):
        tab[patt]=[cs for cs in product(range(3),repeat=3) if all(bool(r)^({cs[i],cs[j]}=={1,2}) for r,(i,j) in zip(patt,((0,1),(0,2),(1,2))))]
    for vs in combinations(V,3):
        patt=tuple((i,j) in E for i,j in combinations(vs,2));assert sum(patt)<3
        for cs in tab[patt]:cnf.append([-var(i,c) for i,c in zip(vs,cs)]);tri[sum(patt)]+=1
    print('forbidden triangle assignments',sorted(tri.items()),flush=True);stats=Counter()
    with Solver(name='cadical195',bootstrap_with=cnf) as sol:
        while sol.solve():
            model=set(sol.get_model());colors=[next(c for c in range(3) if var(i,c) in model) for i in V];new=[r^sum(1<<j for j in V if {colors[i],colors[j]}=={1,2}) for i,r in enumerate(A)];assert all(not(new[i]&new[j]) for i,j in combinations(V,2) if new[i]>>j&1);stats['triangle_free']+=1
            sets=[0];bad=0
            for i,r in enumerate(new):
                sets.extend([s|1<<i for s in sets if not s&r]);bad=next((s for s in reversed(sets) if s.bit_count()>=10),0)
                if bad:break
            if bad:sol.add_clause([-var(i,colors[i]) for i in V if bad>>i&1]);continue
            stats['valid39']+=1;nine=[s for s in sets if s.bit_count()==9];border=next((s for s in sets if all(s&t for t in nine)),None)
            if border is not None:print('WITNESS',colors,border);return
            sol.add_clause([-var(i,colors[i]) for i in V]);
        print('UNSAT',dict(stats),flush=True)
if __name__=='__main__':main()
