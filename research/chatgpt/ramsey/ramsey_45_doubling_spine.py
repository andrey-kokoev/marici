"""Check forced distance 9, red saturation, and unit orbit on Z/24."""
from itertools import combinations
from math import gcd

def distances(vs):
    return frozenset(min(j-i,24-j+i) for i,j in combinations(sorted(vs),2))

def main():
    spine={1,2,4,8}; probe=[0,3,6,9,12]; D=spine|{9}
    r4={distances((0,)+t):(0,)+t for t in combinations(range(1,24),3)}
    b5={distances((0,)+t) for t in combinations(range(1,24),4)}
    assert distances(probe)=={3,6,9,12}
    for d in (3,6,12):assert distances(range(0,4*(d//3),d//3))<=spine|{d}
    for d in sorted(set(range(1,13))-D):
        t=next((0,)+t for t in combinations(range(1,24),3) if distances((0,)+t)<=D|{d});print('adding',d,'forces',t)
    ds=range(1,13);valid={frozenset(d for d in ds if m>>(d-1)&1) for m in range(4096)};valid={v for v in valid if not any(s<=v for s in r4) and all(s&v for s in b5)}
    orbit={frozenset(min(u*d%24,-u*d%24) for d in D) for u in range(24) if gcd(u,24)==1}
    assert valid==orbit and [v for v in valid if 1 in v]==[D];print('all valid masks:',sorted(sorted(v) for v in valid))
if __name__=='__main__':main()
