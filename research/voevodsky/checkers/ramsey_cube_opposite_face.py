"""Source-first test: take the four rows across an actual full cube from a square face."""
from itertools import product,combinations
from collections import Counter
import json
from ramsey_table_cube_differences import analyze
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import D
from ramsey_quartet_live_probe import independent_sets


def marked_faces():
    placements=[]
    for piece in analyze(10)['pieces']:
        start=tuple(piece['start'])
        for half,a in [('upper',start),('mirror',tuple(10-v for v in reversed(start)))]:
            corners=list(product(*[(v,v+1) for v in a]))
            for i in range(3):
                for side in (0,1):
                    sq=tuple(sorted(r for r in corners if r[i]==a[i]+side));rows=tuple(sorted(set(corners)-set(sq)));placements.append((half,a,sq,rows))
    return placements


def audit():
    placements=marked_faces()
    census={s:cs for s,_,cs in charts()};counts=Counter();sizes=Counter();pairs=Counter();examples={}
    for half,a,sq,rows in placements:
        counts['marked_faces']+=1
        if sq not in census:counts['unrealizable_parent']+=1;continue
        counts['realizable_parent']+=1
        for c in census[sq]:
            g=path|c|{(v,11+j) for j,r in enumerate(sq+rows) for v in r}|{(11+j,15+k) for j,r in enumerate(sq) for k,t in enumerate(rows) if set(r).isdisjoint(t)}
            # Opposite rows all share the switched site, so their links must be blue.
            triangles=[set(q) for q in combinations(range(1,19),3) if all(e in g for e in combinations(q,2))];sevens=[{i for i in range(1,19) if mask>>i&1} for mask in independent_sets(18,g,7)];bad=[q&set(range(15,19)) for q in triangles+sevens];assert all(bad)
            largest=max(n for n in range(5) for t in combinations(range(15,19),n) if not any(b<=set(t) for b in bad));singles=sum({i} not in bad for i in range(15,19));sizes[singles,largest]+=1
            U=set().union(*sq);fixed,=set.intersection(*map(set,sq));gsite,=set.intersection(*map(set,rows));mov=U-{fixed}
            for i,j in combinations(range(4),2):
                overlap=set(rows[i])&set(rows[j]);legal=not any(b<={15+i,15+j} for b in bad);pairs[len(overlap),legal]+=1
                assert legal==(overlap=={gsite})
                if not legal:
                    x,=overlap-{gsite};mate,=[v for v in mov-{x} if not any({v,x}<=set(r) for r in sq)]
                    pool=sorted(v for v in set(range(1,11))-U-{gsite} if abs(v-mate)!=1)
                    p=next(e for e in combinations(pool,2) if e not in c);old=[11+k for k,r in enumerate(sq) if x in r]
                    seven=sorted([*p,mate,*old,15+i,15+j]);assert len(seven)==7 and all(e not in g for e in combinations(seven,2))
                    examples.setdefault('constructed_edge_witness',dict(parent=sq,opposite_pair=[rows[i],rows[j]],partner=mate,outside_pair=p,old_ports=[sq[k-11] for k in old]))
            examples.setdefault(str((singles,largest)),dict(half=half,start=a,parent=sq,opposite=rows,cycle=sorted(c),triangle=sorted(triangles[0]) if triangles else None,seven=sorted(sevens[0]) if sevens else None))
    out=dict(counts=counts,by_overlap_and_joint={str(k):v for k,v in pairs.items()},by_single_and_joint_size={str(k):v for k,v in sizes.items()},examples=examples);print(counts,sizes,pairs);(D/'ramsey_cube_opposite_face.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
