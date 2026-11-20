"""Exact ordered extensions (through 3 columns) using bitsets. uv run --with python-sat -- python <file>."""
from itertools import combinations
from pysat.solvers import Solver
from pauli_realization_audit import independent_witness,triangle_free,encode_graph6,decode_graph6

def symbolic(n):
    E=lambda i,j:j*(j-1)//2+i+1
    with Solver(name='cadical195') as s:
        for t in combinations(range(n),3):s.add_clause([-E(i,j) for i,j in combinations(t,2)])
        while s.solve():
            pos=set(s.get_model());rows=[0]*n
            for i,j in combinations(range(n),2):
                if E(i,j) in pos:rows[i]|=1<<j;rows[j]|=1<<i
            t=independent_witness(rows,9)
            if t is None:return rows
            s.add_clause([E(i,j) for i,j in combinations(sorted(t),2)])
    raise ValueError(n)

def audit(a,s):
    ind=[0];assert triangle_free(a)
    for i,r in enumerate(a):ind += [m|1<<i for m in ind if not(m&r)]
    assert max(m.bit_count() for m in ind)<s
    hi,mid,lo=([m for m in ind if m.bit_count()==k] for k in (s-1,s-2,s-3))
    C=[m for m in ind if all(m&t for t in hi)];print('seed',encode_graph6(a),'candidates',len(C),flush=True)
    def mask(vs):return sum(1<<i for i in vs)
    allc=(1<<len(C))-1
    dis=lambda m:mask(i for i,x in enumerate(C) if not x&m)
    E=[dis(x) for x in C];N=[allc for x in C];loMiss=[[] for x in C]
    for t in mid:
        missed=dis(t)
        for i,x in enumerate(C):
            if not x&t:N[i]&=~missed
    for t in lo:
        missed=dis(t)
        for i,x in enumerate(C):
            if not x&t:loMiss[i].append((t,missed))
    pairs=sum(e.bit_count()+n.bit_count() for e,n in zip(E,N));triples=dead=supp=blocked=0
    for i,x in enumerate(C):
        for j,y in enumerate(C):
            if not((E[i]|N[i])>>j&1):continue
            en=(E[i]&N[j]).bit_count()+(N[i]&E[j]).bit_count();nn=N[i]&N[j];ee=(E[i]&E[j]).bit_count()
            if E[i]>>j&1:
                w=en+nn.bit_count();triples+=w;dead+=w==0
            if N[i]>>j&1:
                forbidden=0
                for t,missed in loMiss[i]:
                    if not y&t:forbidden|=missed
                w=en+ee+(nn&~forbidden).bit_count();triples+=w;dead+=w==0
                blocked+=(nn&forbidden).bit_count()
            supp+=((E[i]|N[i])&(E[j]|N[j])).bit_count()
    print('counts',len(C),pairs,triples,'dead ordered pairs',dead,'pairwise triple supports ordered',supp,'blocked empty triple wirings',blocked,flush=True)
    return len(C),pairs,triples

if __name__=='__main__':
    for n in (24,27):
        r=symbolic(n); audit([v&((1<<24)-1) for v in r[:24]],9)
