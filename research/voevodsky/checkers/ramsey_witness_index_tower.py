"""Build the witness indexes from incidence, compare both projections, test six compatible port occurrences. Standard library."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import gzip,json
DATA=Path(__file__).resolve().parents[2]/'chatgpt/ramsey'

def run(line):
    n=line[0]-63;assert n==16
    bits=''.join(f'{b-63:06b}' for b in line[1:]);E={(i,j) for j in range(n) for i in range(j) if bits[j*(j-1)//2+i]=='1'}
    if len(E) not in (33,34):return
    assert all(any(e not in E for e in combinations(t,2)) for t in combinations(range(n),3))
    F=[s for s in combinations(range(n),5) if all(e not in E for e in combinations(s,2))];rows=[sum(1<<i for i,s in enumerate(F) if v in s) for v in range(n)];full=(1<<len(F))-1
    # A face's disjoint faces are the complement of the union of the vertex postings.
    D=[]
    for s in F:
        u=0
        for v in s:u|=rows[v]
        D.append(full^u)
    assert all(D[i]==sum(1<<j for j,t in enumerate(F) if set(F[i]).isdisjoint(t)) for i in range(len(F)))
    missed=[(a,b) for a,b in combinations(range(n),2) if not(rows[a]&rows[b]) and (a,b) not in E]
    adj=[sum(1<<j for j in range(i+1,len(F)) if not (r&D[j])) for i,r in enumerate(D)]
    def clique(m,k):
        if not k:return ()
        while m.bit_count()>=k:
            b=m&-m;m^=b;i=b.bit_length()-1;sub=clique(m&adj[i],k-1)
            if sub is not None:return (i,)+sub
    w=clique(full,6);repeat=0 in D
    if w:assert all(sum(set(F[i]).isdisjoint(t) for i in w)<=1 for t in F)
    return {'faces':len(F),'missed_blue_pairs':len(missed),'duplicate_postings':len(rows)-len(set(rows)),'duplicate_D':len(F)-len(set(D)),'empty_D':repeat,'six_compatible':bool(w) or repeat}
if __name__=='__main__':
    ls=gzip.decompress((DATA/'r36_16.g6.gz').read_bytes()).splitlines();cases=[run(l) for l in ls if sum((c-63).bit_count() for c in l[1:])==33];assert len(cases)==39
    print('33-edge residuals:',len(cases));
    for k in cases[0]:print(k,dict(sorted(Counter(r[k] for r in cases).items())))
    for e in json.loads((DATA/'ramsey_boundary_k6_witnesses.json').read_text())['records']:print('34-edge control',e['graph6'],run(e['graph6'].encode()))
