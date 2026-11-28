"""Direct test on zero-based catalogue record 2, root vertices 0..5."""
from itertools import combinations
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6'
l=p.read_text().splitlines()[2]; n=ord(l[0])-63;assert n==22
bits=''.join(f'{ord(c)-63:06b}' for c in l[1:]);a=[0]*22
for b,(j,i) in zip(bits,((j,i) for j in range(n) for i in range(j))):
    if b=='1':a[i]|=1<<j;a[j]|=1<<i

def independent(g,s):return all(not(g[i]>>j&1) for i,j in combinations(s,2))
def blades(g):return {frozenset(s) for s in combinations(range(6,22),6) if independent(g,s)}
def legal(g):return not any(g[i]&g[j] for i in range(n) for j in range(i) if g[i]>>j&1) and not any(independent(g,s) for s in combinations(range(n),7))
if __name__=='__main__':
    assert legal(a) and independent(a,range(6)); B=blades(a);assert len(B)==10
    remaining=B.copy(); cc=[]
    while remaining:
        c={remaining.pop()};old=None
        while old!=c:
            old=c.copy();c.update(t for t in remaining if any(len(t&s)==5 for s in old));remaining-=c
        cc.append(c)
    print('component sizes',sorted(map(len,cc)));print('isolated',[sorted(next(iter(c))) for c in cc if len(c)==1]);print('max single-edge reconstruction test:')
    for i,j in combinations(range(6,22),2):
        g=a.copy();g[i]^=1<<j;g[j]^=1<<i
        if blades(g)==B and legal(g):print('inequivalent by edge count, toggle',i,j);break
    else:print('no legal one-edge toggle with unchanged record')
