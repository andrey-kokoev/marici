"""Direct same-x construction on flanked clear edges; no row-verdict lookup to choose labels."""
from itertools import combinations,permutations
from collections import Counter
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import D
import json


def audit():
    counts=Counter();examples={}
    for sq,_,cycles in charts():
        U=set().union(*sq);f,=set.intersection(*map(set,sq));mov=U-{f};W=set(range(1,11))-U
        for cyc in cycles:
            for X in combinations(sorted(mov),2):
                if any(set(X)<=set(r) for r in sq):continue
                Y=sorted(mov-set(X));e=(X[0]-1,X[1]+1)
                if not set(e)<=W or e in cyc or any(abs(y-i)==1 for y in Y for i in e):continue
                K=W-set(e);(a,b),=[p for p in combinations(sorted(K),2) if p in cyc];h,=K-{a,b};counts['edges']+=1;wins=[]
                for x,z in permutations(X):
                    for y,v in permutations(Y):
                        if abs(a-y)==1 or abs(b-v)==1:continue
                        rs=[tuple(sorted(s)) for s in ((h,b,x),(a,z,y),(h,a,x),(b,z,v))];base=path|cyc|{(i,11+j) for j,r in enumerate(sq) for i in r}|{(i,15+j) for j,r in enumerate(rs) for i in r}|{(11+i,15+j) for i,r in enumerate(sq) for j,s in enumerate(rs) if set(r).isdisjoint(s)};rep={(15,16),(17,18)};g=base|rep
                        tri=next((q for q in combinations(range(1,19),3) if all(p in g for p in combinations(q,2))),None);seven=next((q for q in combinations(range(1,19),7) if all(p not in g for p in combinations(q,2))),None);ok=not (tri or seven);counts['assignments',ok]+=1;wins.append(ok);examples.setdefault(str(ok),dict(square=sq,cycle=sorted(cyc),edge=e,rows=rs,triangle=tri,seven=seven))
                counts['admits',any(wins)]+=1
    out=dict(counts={str(k):v for k,v in counts.items()},examples=examples);print(out);(D/'ramsey_two_repairs_closed_form.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
