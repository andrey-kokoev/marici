"""k=9, leave-one-red-link-out test on the cyclic witness. Chart-local means a Hall or root clause over at most 7 of the 8 label positions. Full-neighborhood tests are allowed at EVERY surviving degree-8 vertex, not only chart labels."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
D=Path(__file__).parent;F=(1<<35)-1;A=[sum(1<<((i+t)%35) for t in (1,-1,7,-7,11,-11,16,-16)) for i in range(35)];label=A[0];outside=F^(label|1);verts=lambda m:[i for i in range(35) if m>>i&1]

def test():
    rows=[];stats=Counter()
    for i,j in combinations(verts(outside),2):
        if not A[i]>>j&1:continue
        B=A[:];B[i]^=1<<j;B[j]^=1<<i;pair=(1<<i)|(1<<j);V=verts(F&~(A[i]|A[j]));I=[0]
        for v in V:I += [t|1<<v for t in I if not B[v]&t]
        nines=[pair|t for t in I if t.bit_count()==7];assert nines
        # Local clause: J spans <=7 labels and either |J|>=8 (root) or |J|>size of union.
        best=9;local_example=None
        for t in I:
            if t&~outside:continue
            J=t|pair;u=0
            for v in verts(J):u|=A[v]&label
            if J.bit_count()>=8 or u.bit_count()<J.bit_count():
                if u.bit_count()<best:best=u.bit_count();local_example=verts(J)
        stars=[(v,w) for v,s in enumerate(B) if s.bit_count()==8 for w in range(35) if w!=v and not(s>>w&1 or B[w]&s)];local=best<=7;stats[(local,bool(stars))]+=1
        rows.append(dict(edge=[i,j],distance=min(j-i,35-j+i),local=local,min_labels=best,local_example=local_example,star_checks=stars,nines=len(nines),example=verts(nines[0])))
    return rows,stats
if __name__=='__main__':
    rows,stats=test();print(stats);print('by distance',Counter((r['distance'],r['local'],bool(r['star_checks'])) for r in rows));print('blind example',next((r for r in rows if not(r['local'] or r['star_checks'])),None));(D/'ramsey_eight_label_star_test.json').write_text(json.dumps(rows)+'\n')
