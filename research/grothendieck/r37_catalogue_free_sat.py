"""Lazy exact counterexample search. uv run --with python-sat <file> m rounds
A round limit is UNKNOWN, never a proof of nonexistence."""
from itertools import combinations
import sys
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType

def run(m, rounds, cap=9, fixed_five=0):
    # cap=-1 tests existence of the marked maximal attachment alone.
    assert 4<=m<=6
    V=range(22); E={e:i for i,e in enumerate(combinations(V,2),1)}
    def edges(s):return [E[e] for e in combinations(s,2)]
    # Independent maximal N is the first m vertices (symmetry). Each outside
    # vertex has a nonempty incidence word on N; sort words lexicographically
    # by forbidding an adjacent inversion (lazy below).
    clauses=[[-i] for i in edges(range(m))]+[[E[i,j] for i in range(m)] for j in range(m,22)]
    clauses += [[-i for i in edges(t)] for t in combinations(V,3)]
    U=range(m,22); six=list(combinations(U,6)); y=list(range(len(E)+1,len(E)+len(six)+1))
    if cap>=0:
        clauses += CardEnc.atmost(y,cap,encoding=EncType.seqcounter).clauses
        clauses += [edges(t)+[i] for t,i in zip(six,y)]
    if m==4 or fixed_five:
        # Forced support histogram: three private sites per root and one per pair.
        words=sorted([1<<i for i in range(4) for _ in range(3)]+[(1<<i)|(1<<j) for i,j in combinations(range(4),2)])
        if fixed_five:
            words={5:[1,1,2,2,4,4,7,8,8,11,12,16,16,20,21,24,26],
                   6:[1,2,3,5,8,16,19,20,24,26,32,34,36,37,40,60]}[m]
        clauses += [[E[i,j] if w>>i&1 else -E[i,j]] for j,w in enumerate(words,m) for i in range(m)]
        # With support words fixed, a seven can be blue only if its root
        # sites miss every outside word. Emit remaining-edge clauses directly.
        for t in combinations(V,7):
            roots=sum(1<<v for v in t if v<m); outside=[v for v in t if v>=m]
            if not any(words[v-m]&roots for v in outside):
                clauses.append([E[i,j] for i,j in combinations(outside,2) if not words[i-m]&words[j-m]])
    with Solver(name='cadical195',bootstrap_with=clauses) as solver:
        for r in range(rounds):
            if not solver.solve():print('UNSAT, rounds',r);return
            model=set(solver.get_model()); a=[0]*22
            for (i,j),v in E.items():
                if v in model:a[i]|=1<<j;a[j]|=1<<i
            def sevens(p,s):
                if len(s)==7:yield s;return
                while p.bit_count()>=7-len(s):
                    b=p&-p;p^=b;i=b.bit_length()-1;yield from sevens(p&~a[i],s+(i,))
            bad=list(sevens((1<<22)-1,()))
            if not bad:print('COUNTEREXAMPLE',a);return
            for t in bad:solver.add_clause(edges(t))
            for j in range(m,21):
                mask=(1<<m)-1
                if a[j]&mask > a[j+1]&mask:
                    solver.add_clause([-E[i,k] if E[i,k] in model else E[i,k] for k in (j,j+1) for i in range(m)])
            print('round',r+1,'independent sevens blocked',len(bad),flush=True)
    print('UNKNOWN: round limit')
if __name__=='__main__':run(*map(int,sys.argv[1:]))
