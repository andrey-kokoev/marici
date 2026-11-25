"""Cache seven-set conflict rows per exclusive support, then add two-support constraints."""
from functools import lru_cache
from ramsey310_codegree7_test import F,sets

def bits(m):
    while m:
        b=m&-m;yield b.bit_length()-1;m^=b

class CachedKernel:
    def __init__(self,A):
        self.A=A;self.C=list(sets(A,F,7));self.six=list(sets(A,F,6));self.full=(1<<len(self.C))-1
        self.inc=[sum(1<<i for i,s in enumerate(self.C) if s>>v&1) for v in range(27)]
        self.miss={t:self.full & ~self.union(t) for t in self.C+self.six}
        self.base=[sum(1<<j for j,t in enumerate(self.C) if (t&s).bit_count()<=5) for s in self.C]
        self.single=lru_cache(maxsize=160)(self._single)
        self.triple_block=lru_cache(maxsize=290000)(self._triple_block)
    def _triple_block(self,i,j):
        mask=0
        for t in bits(self.miss[self.C[i]]&self.miss[self.C[j]]):mask |= self.miss[self.C[t]]
        return mask
    def union(self,t):
        m=0
        for v in bits(t):m|=self.inc[v]
        return m
    def filter(self,adj,strict):
        for t in strict:
            m=self.miss[t];keep=~m
            for j in bits(m):adj[j]&=keep
    def _single(self,e):
        adj=self.base.copy();self.filter(adj,(t for t in self.C if not e&t));return adj
    def kernel(self,E):
        e=E[0];adj=self.single(e).copy()
        if len(E)==2:
            f=E[1];adj=[x&y for x,y in zip(adj,self.single(f))];self.filter(adj,(t for t in self.six if not t&(e|f)))
        ub=[9-a.bit_count()-sum(s>>v&1 for s in E) for v,a in enumerate(self.A)]
        blocked=0
        for v,k in enumerate(ub):
            if k==0:blocked|=self.inc[v]
            if k==1:
                m=self.inc[v];keep=~m
                for i in bits(m):adj[i]&=keep
        if blocked:
            for i in range(len(adj)):adj[i]=0 if blocked>>i&1 else adj[i]&~blocked
        return self.C,adj,self.inc
