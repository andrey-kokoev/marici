"""Name every cross-cell, including a zero reading. Roles are independent of values."""
from itertools import product


def build(A, B, value):
    cells = {(a,b):value(a,b) for a,b in product(A,B)}
    # Each entry: start, end, underlying cell. Identities are not sign readings.
    readings = {('id',v):(v,v,None) for v in (*A,*B)}
    for a,b in cells:
        readings['ab',a,b] = a,b,(a,b)
        readings['ba',a,b] = b,a,(a,b)
    start = {(v,r) for r,(v,_,_) in readings.items()}
    end = {(v,r) for r,(_,v,_) in readings.items()}
    return cells,readings,start,end

if __name__=='__main__':
    A=(1,2,3);B=(4,5,6,7);positive={(1,5),(2,6),(3,4),(3,7)}
    cells,R,S,T=build(A,B,lambda a,b:int((a,b) in positive))
    for a,b in cells:
        f=('ab',a,b);r=('ba',a,b)
        assert R[f][2]==R[r][2] and (a,f) in S and (b,f) in T and (b,r) in S and (a,r) in T
        assert (b,f) not in S and (a,f) not in T
    assert {r for v,r in S&T}=={('id',v) for v in A+B}
    print(len(cells),'named cells;',len(R),'readings including identities;',sum(cells.values()),'positive cell values')
