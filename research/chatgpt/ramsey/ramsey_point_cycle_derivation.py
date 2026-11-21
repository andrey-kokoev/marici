"""Extract the point-only residual graph by bounded contradiction, not model comparison."""
from ramsey_root_gate import base,bits,T,degree

def close(y,n):
    while True:
        old=y,n
        for m,l,h in base:
            a=(y&m).bit_count();f=m&~(y|n)
            if a>h or a+f.bit_count()<l:return None
            if a==h:n|=f
            elif a+f.bit_count()==l:y|=f
        if old==(y,n):return old

def contradiction(y,n,depth):
    s=close(y,n)
    if s is None:return True
    if not depth:return False
    y,n=s
    return any(contradiction(y|b,n,depth-1) and contradiction(y,n|b,depth-1) for b in bits.values() if not b&(y|n))

if __name__=='__main__':
    y,n=close(0,0)
    for d in range(3):
        old=None
        while old!=(y,n):
            old=y,n
            for b in bits.values():
                if b&(y|n):continue
                if contradiction(y|b,n,d):n|=b
                elif contradiction(y,n|b,d):y|=b
            y,n=close(y,n)
        print('extra splits',d,'fixed',y.bit_count(),n.bit_count())
        if (y.bit_count(),n.bit_count())==(20,12):break
    free=[(i,j) for (i,j),b in bits.items() if not (y|n)&b];tw={10,11};core=[e for e in free if not tw.intersection(e)];print('residual core',[(T[i],T[j]) for i,j in core]);assert len(core)==8
    for i in range(6):
        pair=bits[i,10]|bits[i,11];depth=next(d for d in range(4) if contradiction(y|pair,n,d) and contradiction(y,n|pair,d));print(T[i],'exactly one twin, extra split depth',depth)
    for i in set(sum((list(e) for e in core),[])):
        fixed=sum(bool(y&b) for e,b in bits.items() if i in e);need=degree[i]-fixed-int(i<6);assert need==1 and sum(i in e for e in core)==2
    print('residual core degree one at every vertex')
