"""Enumerate all single flips then all joint refills, independently checking each coloring."""
from pathlib import Path
from itertools import combinations
V=range(17); E=list(combinations(V,2)); idx={e:1<<k for k,e in enumerate(E)}
def masks(k):return [sum(idx[e] for e in combinations(t,2)) for t in combinations(V,k)]
tri=masks(3);six=masks(6)
def valid(r):return not any(r&m==m for m in tri) and all(r&m for m in six)
for record,line in enumerate(Path(__file__).with_name('pauli-realization-catalogues').joinpath('r36_17.g6').read_bytes().splitlines(),1):
    assert line[0]==80
    bits=''.join(f'{v-63:06b}' for v in line[1:]);r=sum(idx[i,j] for i,j in E if bits[j*(j-1)//2+i]=='1');assert valid(r)
    free=[b for b in idx.values() if valid(r^b)]; flips=[0]
    for b in free:flips += [s|b for s in flips]
    legal=[r^s for s in flips if valid(r^s)];full=sum(free);forced=r&~full
    clauses=[]
    for ms,color in [(tri,forced|full),(six,~forced)]:
        ws={m&full for m in ms if m&color==m};clauses.append([w for w in ws if not any(v!=w and v&w==v for v in ws)])
    assert set(legal)=={r^s for s in flips if all((r^s)&w!=w for w in clauses[0]) and all((r^s)&w for w in clauses[1])}
    print(record,len(free),len(legal),[[w.bit_count() for w in cs] for cs in clauses])
