"""Recover the private class from two consecutive side footprints; quantify extra neutral support."""
from itertools import combinations,product
from collections import Counter
from ramsey_excel_corner_predecessor_readout import squares,CAT,decode,D
import json

def audit():
    faces=json.loads((D.parent/'ramsey_square_width_balance.json').read_text())['cases'];sides={frozenset((i,(i+1)%4)):i for i in range(4)};hist=Counter();stats=Counter();special=None
    for idx,line in enumerate((CAT/'r37_22.g6').read_text().splitlines(),1):
        a=decode(line);V=set(range(22));N=[{j for j in V if m>>j&1} for m in a]
        for c in squares(a):
            ext=V-set(c);fp=[ext&(N[c[i]]|N[c[(i+1)%4]]) for i in range(4)];neutral=ext-set.union(*fp);choices=[];roles=[]
            for j in range(4):
                loss=fp[j]-fp[(j+1)%4];assert loss==N[c[j]]&ext
                certs=[frozenset(q) for q in combinations(sorted(loss|neutral),4) if loss.intersection(q) and all(y not in N[x] for x,y in combinations(q,2))];best=max(len(q&loss) for q in certs);ws=[q for q in certs if len(q&loss)==best];hist[len(loss),best,len(ws)]+=1;choices.append(ws);roles.append(dict(corner=c[j],lost=sorted(loss),max_class_hits=best,certificates=[sorted(q) for q in ws]))
            disjoint=sum(len(set.union(set(),*w))==16 for w in product(*choices));stats['squares']+=1;stats['disjoint_possible']+=bool(disjoint)
            if min(len(r['lost']) for r in roles)<4:special=dict(record=idx,corners=c,neutral=sorted(neutral),roles=roles,disjoint_tuples=disjoint)
            for face in faces:
                corners=list(map(tuple,face['corners']));assert all(sum(abs(p-q) for p,q in zip(corners[j],corners[(j+1)%4]))==1 for j in range(4))
                for start,direction in product(range(4),(-1,1)):
                    image=[(start+direction*j)%4 for j in range(4)];
                    for j in range(4):
                        h,k,l=(image[(j+t)%4] for t in range(3));left=fp[sides[frozenset((h,k))]];right=fp[sides[frozenset((k,l))]];assert left-right==set(roles[h]['lost']) and right-left==set(roles[l]['lost']);stats['marked_turns']+=1
    out=dict(counts=stats,private_certificates={str(k):v for k,v in hist.items()},exception=special);print(out);(D.parent/'ramsey_directed_side_loss.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
