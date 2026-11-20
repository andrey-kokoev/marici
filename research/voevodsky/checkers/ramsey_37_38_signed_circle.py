"""Exhaustive one-circle red offset test; representatives k and -k coincide at the diameter. Fix 0 in an independent set by translation."""
from itertools import combinations

def independent(pool, need, neighbors):
    if not need: return True
    while pool.bit_count() >= need:
        b = pool & -pool; pool ^= b
        if independent(pool & ~neighbors[b.bit_length()-1], need-1, neighbors): return True
    return False

def search(n,t):
    winners=[]
    for size in range(1+(t//2)):
        for offsets in combinations(range(1,n//2+1),size):
            s={d%n for a in offsets for d in (a,-a)}
            if len(s)>=t or any((a-b)%n in s for a in s for b in s): continue
            nb=[sum(1<<((i+a)%n) for a in s) for i in range(n)]
            if not independent(((1<<n)-1)^1^nb[0],t-1,nb): winners.append(offsets)
    return winners

if __name__=='__main__':
    for t,n in [(7,22),(8,27)]:
        for m in range(n,0,-1):
            w=search(m,t);print(t,m,len(w),w[:4]);
            if w: break
