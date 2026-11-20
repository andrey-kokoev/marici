"""Symbolic 20x20 block and exact one-column tree. uv run --with python-sat -- python <file>."""
from itertools import combinations
from pysat.solvers import Solver
from pauli_realization_audit import encode_graph6,triangle_free,independent_witness

def symbolic(n):
    # Order the original 190 variables first, then each successive column.
    ix={(i,j):j*(j-1)//2+i+1 for j in range(n) for i in range(j)}
    with Solver(name='cadical195') as s:
        for k,sign in [(3,-1),(7,1)]:
            for t in combinations(range(n),k):s.add_clause([sign*ix[e] for e in combinations(t,2)])
        assert s.solve();pos=set(s.get_model());return [sum(1<<j for j in range(n) if i!=j and ix[tuple(sorted((i,j)))] in pos) for i in range(n)]

def columns(a):
    masks=[0];sixes=[]
    for i,r in enumerate(a):
        new=[m|(1<<i) for m in masks if not(m&r)];masks+=new
        sixes.extend(m for m in new if m.bit_count()==6)
    return [m for m in masks if all(m&t for t in sixes)]

def tree(a):
    levels=[[a]]; labels=[]
    for _ in range(3):
        nxt=[];masks=[]
        for b in levels[-1]:
            valid=columns(b);masks.append(valid)
            for m in valid:
                c=[r|(((m>>i)&1)<<len(b)) for i,r in enumerate(b)]+[m];assert triangle_free(c) and independent_witness(c,7) is None;nxt.append(c)
        levels.append(nxt);labels.append(masks)
    print('seed',encode_graph6(a),'ordered extension counts',list(map(len,levels)),'first columns',[[i for i in range(20) if m>>i&1] for m in labels[0][0]],'children per first column',list(map(len,labels[1])),flush=True)
    for j,children in enumerate(labels[1]):
        if children:
            m=children[0];print('example second support after first choice',j+1,[i for i in range(21) if m>>i&1]);break

if __name__=='__main__':
    for n in [20,22]:
        a=symbolic(n);tree([r%2**20 for r in a[:20]])
