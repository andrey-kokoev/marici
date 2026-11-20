"""Exact rooted (3,k) join capacity for two fixed residual graphs. No solver."""
from itertools import combinations_with_replacement


def capacity(n,red,k):
    blue=[s for s in range(1<<n) if not any((s>>i)&(s>>j)&1 for i,j in red)]
    maxima=[s for s in blue if not any(s!=t and s&t==s for t in blue)]
    assert max(s.bit_count() for s in blue)<=k-2
    largest=[b for b in blue if b.bit_count()==max(s.bit_count() for s in blue)]
    miss=min(sum(not a&b for b in largest) for a in maxima)
    cap=k-1
    if miss:cap=min(cap,len(largest)*(k-1-largest[0].bit_count())//miss)
    print(n,'maximal rows',len(maxima),'largest tests',len(largest),'min misses',miss,'counting cap',cap)
    for d in range(cap,-1,-1):
        for rows in combinations_with_replacement(maxima,d):
            if all(sum(not a&b for a in rows)+b.bit_count()<k for b in blue):
                print('capacity',d,'red row supports',[[i for i in range(n) if a>>i&1] for a in rows]);return d

if __name__=='__main__':
    for n,ds,k,expected in [(5,{2,3},4,2),(13,{1,5,8,12},6,2)]:
        red=[(i,j) for i in range(n) for j in range(i+1,n) if j-i in ds];assert capacity(n,red,k)==expected
