"""Reverse optimal words, vary the reflection axis, and test all binary end-readouts."""
from collections import Counter
from itertools import combinations
from ramsey_35_all_optimal_words import enumerate_repairs
from ramsey_35_min_nonjoins import adj

def norm(w):
    d={};return tuple(d.setdefault(x,len(d)) for x in w)
def audit():
    _,ws=enumerate_repairs();stats=Counter();fixed=[]
    for w,r in ws.items():
        R={frozenset((i-1,j-1) for i,j in fix) for fix in r};rev=norm(reversed(w));assert rev in ws
        def move(E,f):return frozenset(tuple(sorted((f(i),f(j)))) for i,j in E)
        T={frozenset((i-1,j-1) for i,j in fix) for fix in ws[rev]};assert {move(E,lambda i:12-i) for E in R}==T
        if rev==w:
            sw=all(move(E,lambda i:12-i)!=E for E in R);stats['word fixed; swaps' if sw else 'word fixed; preserves']+=1;fixed.append((''.join(chr(65+c) for c in w),sw))
        J={(i,j) for i,j in combinations(range(13),2) if w[i+1]==w[j] or w[j+1]==w[i]};swap=False;keep=False
        for k in range(13):
            f=lambda i:(k-i)%13
            if move(J,f)!=J:continue
            assert {move(E,f) for E in R}==R
            if all(move(E,f)!=E for E in R):swap=True
            else:keep=True
        stats['any axis swaps']+=swap;stats['any axis preserves']+=keep
    print(stats,fixed)

def border():
    legal=Counter();exact=Counter();union=0;total=0
    def walk(o):
        nonlocal total,union
        if len(o)<13:
            for j in range(13):
                if j not in o and adj(o[-1],j):walk(o+[j])
            return
        total+=1;v=o[:-1];rows=[sum(1<<j for j,b in enumerate(v) if adj(a,b)) for a in v];target=sum(1<<j for j,b in enumerate(v) if adj(b,o[-1]));quads=[sum(1<<i for i in t) for t in combinations(range(12),4) if not any(rows[i]>>j&1 for i,j in combinations(t,2))];ok=False
        for rule in range(16):
            p=1<<11
            for i in range(11):p|=((rule>>((rows[-1]>>i&1)*2+(rows[0]>>(11-i)&1)))&1)<<i
            if any(rows[i]&p for i in range(12) if p>>i&1) or any(not p&t for t in quads):continue
            legal[rule]+=1;exact[rule]+=int(p==target);ok=True
        union+=ok
    walk([0,1]);print(total,legal,exact,union)
if __name__=='__main__':audit();border()
