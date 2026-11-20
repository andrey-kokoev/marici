"""Classify local binary triangle completions when every pin must recover the opposite sign."""
from itertools import product

signs=(-1,1)
pairs=list(product(signs,repeat=2))
for values in product(signs,repeat=4):
    f=dict(zip(pairs,values))
    if all(f[b,a]==c and f[a,c]==b and f[b,c]==a for (a,b),c in f.items()):
        print(values,'triangle product',f[1,1], 'permits +++',f[1,1]==1)

def check(x):
    # Equality of pair products iff rows normalized at column 0 coincide.
    normalized=[tuple(r[0]*v for v in r) for r in x]
    for p in range(len(x[0])):
        for q in range(p+1,len(x[0])):
            predictions={-r[p]*r[q] for r in x}
            if len(predictions)>1:
                assert len(set(normalized))>1
                return 'conflict',p,q
    assert len(set(normalized))==1
    return 'consistent',
if __name__=='__main__':
    # Exhaust every possible restriction to two columns of a 3x9 table.
    print('consistent two-column patterns',sum(check(list(zip(*cols)))[0]=='consistent' for cols in product(product(signs,repeat=3),repeat=2)),'of 64')
