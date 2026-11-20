"""Bounded one-branch test: exact partner scores, smallest-mask tie break."""
from itertools import combinations

def run(limit=12):
    rows=[]; ind=[0]
    while len(rows)<limit:
        n=len(rows);seven=[s for s in ind if s.bit_count()==7];eight=[s for s in ind if s.bit_count()==8]
        choices=sorted(p for p in ind if all(p&s for s in eight))
        if not choices:break
        scores=[sum(not(p&q) or all((p|q)&s for s in seven) for q in choices) for p in choices]
        best=max(scores);p=choices[scores.index(best)]
        print(n,len(choices),best,scores.count(best),p)
        rows=[r|((p>>i&1)<<n) for i,r in enumerate(rows)]+[p];ind += [s|(1<<n) for s in ind if not s&p]
    for k,color in [(3,1),(9,0)]:
        assert not any(all((rows[i]>>j&1)==color for i,j in combinations(t,2)) for t in combinations(range(len(rows)),k))
    print('verified',len(rows))
if __name__=='__main__':run()
