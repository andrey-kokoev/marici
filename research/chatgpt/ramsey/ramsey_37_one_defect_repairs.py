"""List radius-one illegal colorings around each labelled catalogue representative;
count single-edge repairs. A third repair certifies non-pairwise behavior."""
from collections import Counter
from itertools import combinations
from pathlib import Path
from ramsey_37_joint_pin_audit import E, ALL, cliques

def neighbours(line):
    bits=''.join(f'{b-63:06b}' for b in line[1:]);N=[0]*22
    for i,j in E:
        if bits[j*(j-1)//2+i]=='1':N[i]|=1<<j;N[j]|=1<<i
    B=[ALL^r^(1<<i) for i,r in enumerate(N)]
    five=list(cliques(B,5))
    for i,j in E:
        plus=bool(B[i]>>j&1);a,b=(N,B) if plus else (B,N); common=a[i]&a[j]
        cores=([1<<k for k in range(22) if common>>k&1] if plus else [s for s in five if s&common==s]);
        if not cores:continue
        v=ALL
        for s in cores:v&=s|(1<<i)|(1<<j)
        a[i]^=1<<j;a[j]^=1<<i;b[i]^=1<<j;b[j]^=1<<i
        repairs=[]
        for x,y in combinations([k for k in range(22) if v>>k&1],2):
            z=b[x]&b[y];ok=not z if not plus else not next(cliques([r&z if z>>k&1 else 0 for k,r in enumerate(b)],5),None)
            if ok:repairs.append((x,y))
        assert (i,j) in repairs
        a[i]^=1<<j;a[j]^=1<<i;b[i]^=1<<j;b[j]^=1<<i
        yield (i,j),plus,repairs
if __name__=='__main__':
    counts=Counter();best=None
    for idx,line in enumerate(Path(__file__).with_name('pauli-realization-catalogues').joinpath('r37_22.g6').read_bytes().splitlines(),1):
        for e,red,rep in neighbours(line):
            counts[len(rep)]+=1
            if best is None or len(rep)>len(best[-1]):best=(idx,e,red,rep)
    print(counts,best)
