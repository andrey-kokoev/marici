"""Deterministic reflected construction experiment; standard library only.
A signed incidence uses mask 1=parallel, 2=crossed, 3=both, 0=neither.
"""
from itertools import combinations
from itertools import product
from pauli_realization_audit import triangle_free, independent_witness, encode_graph6

L='ABCabcuvdeZ'  # singletons a,b,c; doubletons u=AC,v=BC; repeats d,e

def setup():
    fixed={}
    def put(i,j,h,value):fixed[min(i,j),max(i,j),h]=bool(value)
    def block(i,j,mask):
        for h in (0,1):put(i,j,h,mask & (1<<h))
    # Signed seed (one chosen orientation, not forced by the unsigned marks).
    seed=['X..P.PP','.X..XPX','..P XPPX'.replace(' ','')]
    for i,row in enumerate(seed):
        for j,x in enumerate(row,3):block(i,j,'.PX'.index(x))
    supports=[{i for i in range(3) if seed[i][j]!='.'} for j in range(7)]
    doubles=[s for s in supports if len(s)==2]
    for i in range(3):block(i,10,0)
    put(10,10,1,True)
    for j,s in enumerate(supports,3):
        if not all(s&t for t in doubles):block(j,10,0)
    return fixed,[j for j,s in enumerate(supports,3) if all(s&t for t in doubles)]


def make_problem(fixed,center_cols):
    def key(i,j):return (i//2,j//2,(i^j)&1)
    keys=sorted({key(i,j) for i,j in combinations(range(22),2)}-fixed.keys());ids={k:i for i,k in enumerate(keys,1)}
    clauses=set()
    for n,sign in ((3,-1),(7,1)):
        for vs in combinations(range(22),n):
            if tuple(sorted(v^1 for v in vs))<vs:continue
            c=set()
            for i,j in combinations(vs,2):
                k=key(i,j)
                if k in fixed:
                    if fixed[k]==(sign==1):break
                else:c.add(ids[k]*sign)
            else:clauses.add(frozenset(c))
    for j in center_cols:clauses.add(frozenset(ids[j,10,h] for h in (0,1)))
    return keys,clauses


def propagate(clauses,given):
    known=set(given)
    while True:
        add=set()
        for clause in clauses:
            if clause&known:continue
            rest=[x for x in clause if -x not in known]
            if not rest:return None
            if len(rest)==1:add.update(rest)
        if any(-x in known|add for x in add):return None
        if not add-known:return known
        known.update(add)

if __name__=='__main__':
    fixed,cols=setup();keys,clauses=make_problem(fixed,cols)
    # Fix the arbitrary naming of the two copies of Z using its c connection.
    known=propagate(clauses,[keys.index((5,10,1))+1]);print('initial forced',len(known),'of',len(keys))
    while True:
        undecided=[i for i in range(1,len(keys)+1) if not {i,-i}&known]
        forced=[lit for i in undecided for lit in (i,-i) if propagate(clauses,known|{-lit}) is None]
        if not forced:break
        known=propagate(clauses,known|set(forced));assert known is not None
        print('after single-literal contradiction checks',len(known))
    print('residual:',[keys[i-1] for i in undecided]);assert [keys[i-1] for i in undecided]==[(2,2,1),(8,8,1),(9,9,1)]
    for vals in product([False,True],repeat=3):
        full=known|{i if v else -i for i,v in zip(undecided,vals)}
        if not all(c&full for c in clauses):continue
        edges=dict(fixed);edges.update({k:i in full for i,k in enumerate(keys,1)})
        rows=[0]*22
        for i,j in combinations(range(22),2):
            if edges[i//2,j//2,(i^j)&1]:rows[i]|=1<<j;rows[j]|=1<<i
        assert triangle_free(rows) and independent_witness(rows,7) is None
        print('valid residual joins',vals,encode_graph6(rows))
