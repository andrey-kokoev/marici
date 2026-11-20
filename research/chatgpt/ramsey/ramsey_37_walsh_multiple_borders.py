"""Run the symbolic singleton calculation on all 22 deletions of catalogue record 1.
Cross-check counts and marginals independently using core-only red-independent candidates."""
from pathlib import Path
from collections import Counter
from ramsey_37_walsh_border_moments import moments

def audit():
    line=Path(__file__).with_name('pauli-realization-catalogues').joinpath('r37_22.g6').read_bytes().splitlines()[0];bits=''.join(f'{v-63:06b}' for v in line[1:]);hist=Counter();results=[]
    for omitted in range(22):
        ids=[i for i in range(22) if i!=omitted];adj=[0]*21
        for j,v in enumerate(ids):
            for i,u in enumerate(ids[:j]):
                if bits[v*(v-1)//2+u]=='1':adj[i]|=1<<j;adj[j]|=1<<i
        z,h,*_=moments(adj);counts=[(z-a)//2 for a in h];hist[z]+=1
        ss=[0]
        for i,row in enumerate(adj):ss += [s|1<<i for s in ss if not s&row]
        six=[s for s in ss if s.bit_count()==6];good=[s for s in ss if all(s&t for t in six)]
        assert z==len(good) and counts==[sum(s>>i&1 for s in good) for i in range(21)]
        results.append((z,omitted+1,[(u+1,c) for u,c in zip(ids,counts) if c],[[u+1 for i,u in enumerate(ids) if s>>i&1 and counts[i]!=z] for s in good]))
    print('border count -> deletion count:',sorted(hist.items()));print('largest example:',max(results))
if __name__=='__main__':audit()
