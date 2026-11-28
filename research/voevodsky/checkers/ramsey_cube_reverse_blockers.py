"""Permanent blockers for monotone reverse extension of a 26-core. Verify certificates against all independent rows at every endpoint root."""
from ramsey_cube_retention_floor import G,combinations,D
import json
from collections import Counter
from random import Random

def audit():
    runs=[];rng=Random(4355)
    for r in range(35):
        V=[i for i in range(35) if i!=r and not G[r]>>i&1];p=sum(1<<i for i in V);I=[0]
        for i in V:I.extend([s|1<<i for s in I if not G[i]&s])
        Q=[q for q in I if q.bit_count()==7];E=[1<<i|1<<j for i,j in combinations(V,2) if not (G[i]>>j&1 or G[i]&G[j]&p)];B=[q for q in Q if all(e&q!=e for e in E)];S=[s for s in I if all(s&(G[i]|1<<i) for i in V)];univ=(1<<len(S))-1;bad=[sum(1<<j for j,s in enumerate(S) if not q&s) for q in B];assert __import__('functools').reduce(int.__or__,bad)==univ
        best=None
        for _ in range(64):
            perm=list(range(len(B)));rng.shuffle(perm);left=univ;chosen=[]
            while left:
                i=max(perm,key=lambda j:(left&bad[j]).bit_count());chosen.append(i);left &=~bad[i]
            for i in chosen[:]:
                if __import__('functools').reduce(int.__or__,(bad[j] for j in chosen if j!=i),0)==univ:chosen.remove(i)
            if best is None or len(chosen)<len(best):best=chosen
        obs=[B[i] for i in best];assert all(any(not q&s for q in obs) for s in I);assert all(all(G[i]&G[j]&p for i,j in combinations([v for v in V if q>>v&1],2)) for q in obs);runs.append(dict(root=r,sevens=len(Q),safe_links=len(E),permanent=len(B),maximal_rows=len(S),certificate=[[i for i in V if q>>i&1] for q in obs]))
    print(Counter((z['sevens'],z['safe_links'],z['permanent'],z['maximal_rows']) for z in runs),Counter(len(z['certificate']) for z in runs));(D.parent/'ramsey_cube_reverse_blockers.json').write_text(json.dumps(runs,indent=2)+'\n')
if __name__=='__main__':audit()
