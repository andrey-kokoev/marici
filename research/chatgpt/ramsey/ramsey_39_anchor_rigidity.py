"""Count completions up to permutations of missing vertices, holding the signed interval fixed.
Uses uniqueness of the order-35 host. Count induced embeddings modulo its affine automorphisms.
This is a classification test, not a constructor from blank labels."""
from math import gcd
from ramsey_39_rotate_reflect_completion import sign
N=35;ALL=(1<<N)-1;adj=[sum(int(sign(i,j))<<j for j in range(N)) for i in range(N)]
units=[u for u in range(N) if gcd(u,N)==1 and all(sign(0,j)==sign(0,u*j) for j in range(N))]

def count(radius,cap=500000):
    # Normalize image(0)=0; for radius>=1 the six remaining units act freely:
    # vertices in the image could all be multiples of 7 only if size<=5.
    S=[x%N for x in range(-radius,radius+1)];fixed={0:0};copies=mirror=0
    def visit(dom):
        nonlocal copies,mirror
        if not dom:
            copies+=1;mirror+=all(fixed[(-v)%N]==(-x)%N for v,x in fixed.items());return
        v=min(dom,key=lambda i:dom[i].bit_count());cand=dom[v]
        while cand:
            b=cand&-cand;cand^=b;x=b.bit_length()-1
            # Normalize by subgroup of multipliers fixing current images, not by translation.
            if any((u*x)%N<x and all((u*y)%N==y for y in fixed.values()) for u in units):continue
            child={i:m&(adj[x] if sign(i,v) else ALL^(adj[x]|b)) for i,m in dom.items() if i!=v}
            if all(child.values()):
                fixed[v]=x;visit(child);del fixed[v]
                if copies>=cap:raise RuntimeError('cap reached')
    visit({v:adj[0] if sign(0,v) else ALL^(adj[0]|1) for v in S if v});return copies,mirror
if __name__=='__main__':
    assert units==[1,11,16,19,24,34]
    for r in range(13,1,-1):print(2*r+1,*count(r),flush=True)
