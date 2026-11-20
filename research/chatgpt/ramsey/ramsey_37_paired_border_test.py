"""Exhaust marked 4-doubled cores induced in the order-22 catalogue. All group labelings."""
from urllib.request import urlopen
from itertools import combinations,permutations,product
from collections import Counter

def audit():
    raw=urlopen('https://users.cecs.anu.edu.au/~bdm/data/r37_22.g6',timeout=30).read().splitlines();assert len(raw)==191
    ij=list(combinations(range(4),2));seen=set();found=0;dist=Counter()
    for s in raw:
        n=s[0]-63;assert n==22
        a=[0]*n;bits=''.join(f'{c-63:06b}' for c in s[1:]);ind=[0]
        for j in range(n):
            for i in range(j):
                if bits[j*(j-1)//2+i]=='1':a[i]|=1<<j;a[j]|=1<<i
            ind += [w|1<<j for w in ind if not w&a[j]]
        for R in (w for w in ind if w.bit_count()==5):
            ends=[v for v,b in enumerate(a) if not (1<<v)&R and not b&R]
            if len(ends)!=2:continue
            e,f=ends;assert a[e]>>f&1
            left={b&R:v for v,b in enumerate(a) if (b&R).bit_count()==1 and b>>e&1};right={b&R:v for v,b in enumerate(a) if (b&R).bit_count()==1 and b>>f&1}
            # No two private neighbors of one witness can both touch the same endpoint.
            dbl=left.keys()&right.keys();dist[len(dbl)]+=1
            for four in combinations(dbl,4):
                found+=1
                for perm in permutations(four):
                    d=tuple(int(a[left[perm[i]]]>>right[perm[j]]&1)+2*int(a[left[perm[j]]]>>right[perm[i]]&1) for i,j in ij);assert all(d);seen.add(d);seen.add(tuple(3 if c==3 else 3-c for c in d))
    def pred(d):
        arc={(i,j) for (i,j),c in zip(ij,d) if c&1}|{(j,i) for (i,j),c in zip(ij,d) if c&2}
        return not any((i,j) in arc and (j,k) in arc and (k,i) in arc for i,j,k in permutations(range(4),3))
    allp=set(product((1,2,3),repeat=6));accepted={d for d in allp if pred(d)}
    print('reservations by doubled count',dist,'4-core occurrences',found,'accepted',len(accepted),'in hosts',len(seen),'both',len(accepted&seen),'transitive present',(1,)*6 in seen)
    print('first false positive',min(accepted-seen,default=None),'first false negative',min(seen-accepted,default=None))
if __name__=='__main__':audit()
