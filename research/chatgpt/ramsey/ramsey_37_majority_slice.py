"""Three cyclic relabelings of a red wedge give a non-pairwise slice on 22 vertices."""
from pathlib import Path
from itertools import combinations
E=list(combinations(range(22),2)); best=(232,)
for idx,line in enumerate(Path(__file__).with_name('pauli-realization-catalogues').joinpath('r37_22.g6').read_bytes().splitlines(),1):
    bits=''.join(f'{b-63:06b}' for b in line[1:]);N=[0]*22
    for i,j in E:
        if bits[j*(j-1)//2+i]=='1':N[i]|=1<<j;N[j]|=1<<i
    for i,j,k in combinations(range(22),3):
        if sum((N[x]>>y)&1 for x,y in [(i,j),(j,k),(i,k)])!=2:continue
        mixed=((N[i]^N[j])|(N[j]^N[k])) & ~((1<<i)|(1<<j)|(1<<k)); size=3+3*mixed.bit_count()
        if size<best[0]:best=(size,idx,(i,j,k),[v for v in range(22) if mixed>>v&1])
print(best)
