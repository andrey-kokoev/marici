"""Three disjoint independent supports = proper partial 3-colouring. Each selected maximum row needs two distinct colours. Compute indispensable rows, deletion-minimal refutations and exact lower bounds via near-colourings. No preselected support list."""
from itertools import combinations
from random import Random
from pysat.solvers import Solver
from ramsey_inverse_five_motifs import graph,D,json,inds,bits

def audit(H):
    n=len(H);T=sorted(s for s in inds(H) if s.bit_count()==5);C=[[-(1+3*i+k),-(1+3*j+k)] for i,j in combinations(range(n),2) if H[i]>>j&1 for k in range(3)]+[[-(1+3*i+k),-(1+3*i+h)] for i in range(n) for k,h in combinations(range(3),2)];g=[1+3*n+j for j in range(len(T))];
    for gate,t in zip(g,T):
        for ps in combinations(range(3),2):C.append([-gate]+[1+3*i+k for i in bits(t) for k in ps])
    rng=Random(987);best=g;forced=[];near=[]
    with Solver(name='g4',bootstrap_with=C) as sat:
        assert not sat.solve(assumptions=g)
        for a in g:
            if sat.solve(assumptions=[b for b in g if a!=b]):
                forced.append(a);model=set(sat.get_model());S=[sum(1<<i for i in range(n) if 1+3*i+k in model) for k in range(3)];assert [z for z,t in zip(g,T) if sum(bool(s&t) for s in S)<2]==[a];near.append(S)
        for rep in range(32):
            order=g.copy();rng.shuffle(order);assert not sat.solve(assumptions=order);core=set(sat.get_core());
            for a in order:
                if a not in core or a in forced:continue
                if not sat.solve(assumptions=list(core-{a})):core=set(sat.get_core())
            if len(core)<len(best):best=sorted(core)
        assert not sat.solve(assumptions=list(best));assert all(sat.solve(assumptions=[b for b in best if b!=a]) for a in best)
    return dict(rows=len(T),indispensable=[T[g.index(a)] for a in forced],near_colorings=near,core=[T[g.index(a)] for a in best])
if __name__=='__main__':
    z=[audit(graph(l)) for l in (D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()];print([(r['rows'],len(r['indispensable']),len(r['core'])) for r in z]);(D/'ramsey_three_color_row_kernel.json').write_text(json.dumps(z)+'\n')
