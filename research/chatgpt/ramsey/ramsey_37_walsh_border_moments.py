"""Core-only singleton Walsh moments by polynomial reduction and independent-set partition sums.
No border solutions are used as inputs or enumerated as solutions. Labels are 1-based on output.
"""
from functools import lru_cache
from itertools import combinations
from pathlib import Path


def moments(adj):
    n=len(adj);full=(1<<n)-1
    six=[sum(1<<i for i in t) for t in combinations(range(n),6) if all(not(adj[i]>>j&1) for i,j in combinations(t,2))]
    # Polynomial of the blue obligations modulo x_i^2=x_i and x_i*x_j=0 on red edges.
    p={0:1};peak=1
    for q in six:
        bad=p.copy();bits=q
        while bits:
            b=bits&-bits;bits-=b;row=adj[b.bit_length()-1];out={}
            for s,v in bad.items():
                if s&b:continue  # x_S(1-x_i)=0
                out[s]=out.get(s,0)+v
                if not s&row:out[s|b]=out.get(s|b,0)-v
            bad={s:v for s,v in out.items() if v}
        for s,v in bad.items():p[s]=p.get(s,0)-v
        p={s:v for s,v in p.items() if v};peak=max(peak,len(p))
    @lru_cache(None)
    def Z(m):
        if not m:return 1
        b=m&-m;r=m^b
        return Z(r)+Z(r&~adj[b.bit_length()-1])
    mass=0;first=[0]*n
    for s,v in p.items():
        m=full^s;bits=s
        while bits:
            b=bits&-bits;bits-=b;m&=~adj[b.bit_length()-1]
        w=Z(m);mass+=v*w
        for i,row in enumerate(adj):
            b=1<<i;ones=w if s&b else Z(m&~(row|b)) if m&b else 0
            first[i]+=v*(w-2*ones)
    return mass,first,len(six),peak,len(p)

if __name__=='__main__':
    line=Path(__file__).with_name('pauli-realization-catalogues').joinpath('r37_22.g6').read_bytes().splitlines()[0];bits=''.join(f'{v-63:06b}' for v in line[1:]);n=21
    adj=[0]*n
    for j in range(n):
        for i in range(j):
            if bits[j*(j-1)//2+i]=='1':adj[j]|=1<<i;adj[i]|=1<<j
    z,h,q,peak,end=moments(adj);S=[i+1 for i,v in enumerate(h) if v<0];print('red pairs',sum(r.bit_count() for r in adj)//2,'blue sixes',q,'peak/end terms',peak,end,'mass',z,'Walsh numerators',h,'red neighbors',S)
    # Only now read the held-out border.
    assert z==1 and all(abs(v)==1 for v in h) and S==[i+1 for i in range(n) if bits[n*(n-1)//2+i]=='1']
