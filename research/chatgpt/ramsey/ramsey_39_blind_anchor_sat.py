"""uv run --with python-sat python research/chatgpt/ramsey/ramsey_39_blind_anchor_sat.py
Inputs: order 35, signs on [-5,5], inversion. No known host, degrees or missing offsets.
Try shift invariance as a *branching hypothesis*. If unsat, release it. Separation adds
only valid negative-nine clauses; a returned solution is checked independently.
"""
from itertools import combinations
from pysat.solvers import Solver

N=35

def main():
    vs=range(N);edges=list(combinations(vs,2));seed=list(range(-5,6)); ids={};v={}
    for i,j in edges:
        e=min((i,j),tuple(sorted((-i%N,-j%N))));v[i,j]=ids.setdefault(e,len(ids)+1)
    def lit(i,j):return v[tuple(sorted((i%N,j%N)))]
    shift=len(ids)+1
    clauses=[[lit(i,j) if j-i in (1,7) else -lit(i,j)] for i,j in combinations(seed,2)]
    for i,j,k in combinations(vs,3):clauses.append([-v[i,j],-v[i,k],-v[j,k]])
    for i,j in edges:
        a,b=lit(i,j),lit(i+1,j+1);clauses.extend(([-shift,-a,b],[-shift,a,-b]))
    def ninth_sets(rows,limit):
        # Enumerate until a bounded batch of new forbidden sets is found.
        def visit(mask,t):
            if len(t)==9:yield t;return
            while mask.bit_count()>=9-len(t):
                bit=mask&-mask;mask^=bit;i=bit.bit_length()-1
                yield from visit(mask&~rows[i],t+(i,))
        from itertools import islice
        return list(islice(visit((1<<N)-1,()),limit))
    with Solver(name='cadical195',bootstrap_with=clauses) as sat:
        for assume in (shift,-shift):
            rejected=0
            while sat.solve(assumptions=[assume]):
                model=set(sat.get_model());rows=[0]*N
                for i,j in edges:
                    if v[i,j] in model:rows[i]|=1<<j;rows[j]|=1<<i
                bad=ninth_sets(rows,128)
                if not bad:
                    assert all(not(rows[i] & rows[j]) for i,j in edges if rows[i]>>j&1)
                    independent=[0]
                    for i,row in enumerate(rows):independent += [p|1<<i for p in independent if not p&row]
                    assert max(p.bit_count() for p in independent)==8
                    print('shift branch',assume==shift,'rejected candidates',rejected,'neighbors of 0',[i for i in vs if rows[0]>>i&1], 'positive edges',sum(r.bit_count() for r in rows)//2);return
                rejected+=1
                for t in bad:sat.add_clause([lit(i,j) for i,j in combinations(t,2)])
    print('no completion')
if __name__=='__main__':main()
