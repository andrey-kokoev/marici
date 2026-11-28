"""Coordinate-blade support test. New vertex v implicit in both blades."""
from itertools import combinations
from pathlib import Path

def audit(line):
    n=ord(line[0])-63; assert n==22
    bits=''.join(format(ord(c)-63,'06b') for c in line[1:]); adj=[0]*n
    for bit,(j,i) in zip(bits,((j,i) for j in range(n) for i in range(j))):
        if bit=='1': adj[i]|=1<<j; adj[j]|=1<<i
    assert not any(adj[i]&adj[j] for i,j in combinations(range(n),2) if adj[i]>>j&1)
    def independent(p,s):
        yield s
        while p:
            b=p&-p;p^=b
            yield from independent(p&~adj[b.bit_length()-1],s|b)
    sets=list(independent((1<<n)-1,0)); assert max(map(int.bit_count,sets))==6
    six=[s for s in sets if s.bit_count()==6]
    maximal=[s for s in sets if all((s>>v&1) or (adj[v]&s) for v in range(n))]
    gaps=[sum(not (s&t) for t in six) for s in maximal]; assert min(gaps)>0
    return len(maximal),min(gaps)

if __name__=='__main__':
    lines=(Path(__file__).resolve().parents[1]/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6').read_text().splitlines()
    results=list(map(audit,lines));print('graphs, maximal attachments, range of per-graph minimum misses:',len(lines),sum(m for m,g in results),min(g for m,g in results),max(g for m,g in results))
