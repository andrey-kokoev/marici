"""Check the twin-row difference and its four closing rectangles in every completion
of the fixed signed, joined-center example. Standard library only."""
from itertools import product
from ramsey_promoted_center_construction import setup,make_problem,propagate,L


def main():
    fixed,cols=setup(); keys,clauses=make_problem(fixed,cols)
    known=propagate(clauses,[keys.index((5,10,1))+1])
    while True:
        free=[i for i in range(1,len(keys)+1) if not {i,-i}&known]
        force=[s for i in free for s in (i,-i) if propagate(clauses,known|{-s}) is None]
        if not force:break
        known=propagate(clauses,known|set(force));assert known is not None
    count=0; results=set()
    for values in product([1,-1],repeat=len(free)):
        model=known|{i*s for i,s in zip(free,values)}
        if not all(cl&model for cl in clauses):continue
        count+=1;edges=fixed|{k:i in model for i,k in enumerate(keys,1)}
        def sign(i,j):
            p,x=(edges[min(i,j),max(i,j),h] for h in (0,1));assert p!=x
            return int(p)-int(x)
        c,z=2,10;d=8
        # Align the copies of C and Z at the newly filled column d.
        align=sign(c,d)*sign(z,d)
        pattern=tuple(sign(c,j)*align*sign(z,j) for j in cols)
        loops=[]
        for j,r in [(6,0),(7,1),(9,0),(9,1)]:
            loops.append(tuple(sign(k,j)*sign(r,j)*sign(r,d)*sign(k,d) for k in (c,z)))
        results.add((pattern,tuple(loops)))
    assert count==6 and len(results)==1
    pattern,loops=results.pop(); print('completions',count,'columns',''.join(L[j] for j in cols),'relative phases',pattern)
    print('rectangle signs (C,Z)',loops);cross=sum(pattern);n=len(cols)
    print('odd-sector 2-row Gram: diagonal',n,'off-diagonal',cross,'difference eigenvalue',n-cross)
    assert pattern==(-1,-1,1,1,1) and loops==((-1,1),(-1,-1),(-1,-1),(1,1))

if __name__=='__main__': main()
