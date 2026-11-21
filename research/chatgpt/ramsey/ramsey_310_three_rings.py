"""Exact offset search: precompute all legal single rings and pairs, then glue triples."""
from itertools import combinations,combinations_with_replacement
from functools import lru_cache
from ramsey_hall_center_conjecture import independent
F=8191
def rot(m,k):return ((m<<k)|(m>>(13-k)))&F
def rev(m):return sum(1<<((-i)%13) for i in range(13) if m>>i&1)
def sumset(m,s):
    out=0
    while m:
        b=m&-m;m-=b;out|=rot(s,b.bit_length()-1)
    return out
R=[]
for t in range(1,64):
    s=t<<1;s|=rev(s)
    if not sumset(s,s)&s:R.append(s)
@lru_cache(None)
def indsets(r):return [m for m in range(1,8192) if not sumset(m,r)&m]
@lru_cache(None)
def alpha(r):
    a=[0]*8192
    for m in range(1,8192):
        b=m&-m;a[m]=max(a[m-b],1+a[(m-b)&~rot(r,b.bit_length()-1)])
    return a
@lru_cache(None)
def pair(a,b):
    out=[]
    for m in range(8192):
        if m!=min(rot(m,j) for j in range(13)):continue
        if sumset(m,a|b)&m or m.bit_count()+max(a.bit_count(),b.bit_count())>9:continue
        if all(x.bit_count()+alpha(b)[F^sumset(x,m)]<10 for x in indsets(a)):out.append(m)
    return out

def mult(m,u):return sum(1<<((i*u)%13) for i in range(13) if m>>i&1)
def run():
    tested=0;types=0
    for a,b,c in combinations_with_replacement(sorted(R),3):
        if (a,b,c)!=min(tuple(sorted(mult(r,u) for r in (a,b,c))) for u in range(1,13)):continue
        types+=1
        for x in pair(a,b):
            for y in pair(a,c):
                if a.bit_count()+x.bit_count()+y.bit_count()>9:continue
                for w in pair(b,c):
                    if b.bit_count()+x.bit_count()+w.bit_count()>9 or c.bit_count()+y.bit_count()+w.bit_count()>9:continue
                    for z in {rot(w,i) for i in range(13)}:
                        if sumset(x,z)&y:continue
                        # A maximum independent set meets ring A, B or C; try all vertices via bit search.
                        A=[rot(a,i)|(rot(x,i)<<13)|(rot(y,i)<<26) for i in range(13)]+[rot(rev(x),i)|(rot(b,i)<<13)|(rot(z,i)<<26) for i in range(13)]+[rot(rev(y),i)|(rot(rev(z),i)<<13)|(rot(c,i)<<26) for i in range(13)]
                        tested+=1
                        # Translation can put one chosen vertex at position 0 in its ring.
                        if all(not independent(A,((1<<39)-1)&~(A[v]|1<<v),9) for v in (0,13,26)):
                            assert not independent(A,(1<<39)-1,10) and all(not A[i]&A[j] for i,j in combinations(range(39),2) if A[i]>>j&1)
                            print('witness',a,b,c,x,y,z,flush=True);return
    print('exhausted',types,'ring types;',tested,'triangle-free degree/pair-filtered configurations')
if __name__=='__main__':run()
