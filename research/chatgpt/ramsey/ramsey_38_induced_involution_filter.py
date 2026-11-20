"""Necessary six-column/three-flat filter: nine disjoint transpositions acting as an automorphism of their induced 18 vertices. Also check that their pairs can be arranged in 3x3 with constant internal colors along each row (three-flat equal signature)."""
from itertools import combinations
from pathlib import Path
from collections import Counter
import gzip

def trial(rows,k=9):
    V=range(len(rows)); t=list(combinations(V,2)); N=len(t);A=[0]*N;colors=[]
    def e(a,b):return rows[a]>>b&1
    for i,(a,b) in enumerate(t):
        colors.append(e(a,b))
        for j,(c,d) in enumerate(t[:i]):
            if len({a,b,c,d})==4 and e(a,c)==e(b,d) and e(a,d)==e(b,c):A[i]|=1<<j;A[j]|=1<<i
    def search(m,path):
        need=k-len(path)
        if need==0:return path if sum(colors[v] for v in path)%3==0 else None
        # greedy independent color classes bound the maximum clique in each prefix
        left=m;order=[];score=0
        while left:
            score+=1;cls=left
            while cls:
                b=cls&-cls;cls^=b;left^=b;v=b.bit_length()-1;order.append((v,score));cls&=~A[v]
        for v,s in reversed(order):
            if s<need:return None
            m^=1<<v;r=search(m&A[v],path+[v]);
            if r is not None:return r
        return None
    p=search((1<<N)-1,[]);return None if p is None else [t[i] for i in p]

def decode(line):
    n=line[0]-63;b=''.join(f'{v-63:06b}' for v in line[1:]);A=[0]*n
    for j in range(n):
        for i in range(j):
            if b[j*(j-1)//2+i]=='1':A[i]|=1<<j;A[j]|=1<<i
    return A
if __name__=='__main__':
    p=Path(__file__).with_name('pauli-realization-catalogues').joinpath('r38_27.g6.gz');ls=gzip.decompress(p.read_bytes()).splitlines();idx=[i*(len(ls)-1)//15 for i in range(16)]
    for i in idx:
        r=trial(decode(ls[i]));print(i+1,'passes' if r else 'excluded',flush=True)
