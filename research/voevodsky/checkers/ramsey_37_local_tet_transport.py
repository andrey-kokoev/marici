"""Test weaker necessity: a four-port frame with an exclusive midpoint per pair; then ask if re-rooting at those midpoints admits compatible four-port frames using the two retained ports. Only a one-step test, not a commuting route test."""
from itertools import combinations
from pathlib import Path
from collections import Counter
import json
H=Path(__file__).resolve().parents[1];cat=H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6';out=[]
for idx,g in enumerate(cat.read_text().splitlines(),1):
 b=''.join(f'{ord(c)-63:06b}' for c in g[1:]);N=[set() for _ in range(22)]
 for j in range(22):
    for i in range(j):
        if b[j*(j-1)//2+i]=='1':N[i].add(j);N[j].add(i)
 frames={};support=set()
 for r in range(22):
    for ports in combinations(sorted(N[r]),4):
        P=set(ports);pairs={p:[] for p in combinations(ports,2)}
        for m in range(22):
            k=tuple(sorted(N[m]&P))
            if k in pairs:pairs[k].append(m)
        if all(pairs.values()):
            frames[r,ports]=pairs;support.update((r,p) for p in pairs)
 one=sum(all(any((m,p) in support for m in ms) for p,ms in pairs.items()) for pairs in frames.values());out.append(dict(record=idx,frames=len(frames),one_step=one))
print('records with frames / all six re-rootable:',sum(bool(t['frames']) for t in out),sum(bool(t['one_step']) for t in out));(H/'results/ramsey_37_local_tet_transport.json').write_text(json.dumps(out,indent=2)+'\n')
