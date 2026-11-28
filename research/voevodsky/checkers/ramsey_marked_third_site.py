"""Hold the placement, prefix and marked role fixed; vary only the outside pentagon."""
from itertools import combinations
from ramsey_cube_diagonal_pairs import profile,independent_sets,charts,path,D
import json


def audit():
    sq=((1,4,8),(1,4,9),(1,5,8),(1,5,9));target=(2,4,9);diag=(target,(2,5,8));alt=((2,5,9),(2,4,8));prefix=(3,5);rows=[prefix+(v,) for v in range(7,11)];out=[]
    for parent,_,cycles in charts():
        if parent!=sq:continue
        for c in cycles:
            g,ms=profile(sq,diag,c,rows);_,other=profile(sq,alt,c,rows);accept=[r for r in rows if any(m&(1<<15) for m in ms.get(r,[]))];assert not any(m&(1<<15) for rr in other.values() for m in rr)
            z,=[j if i==2 else i for i,j in c if 2 in (i,j) and 3 not in (i,j)];pred=[prefix+(z,)] if z>6 else [];assert pred==accept
            failed={}
            for r in rows:
                if r in accept:continue
                red=set(r)|{11+j for j,s in enumerate(sq) if set(r).isdisjoint(s)}|{15};q=next((e for e in sorted(g) if set(e)<=red),None)
                if q:failed[str(r)]=dict(red_triangle_with_new=q);continue
                # Port 16 has support 258, sharing site 5 with the probe: its link cannot be red.
                assert set(r)&set(diag[1]);six=next(m for m in independent_sets(16,g,6) if all(not (m>>i&1) for i in red));failed[str(r)]=dict(blue_six=[i for i in range(1,17) if six>>i&1])
            out.append(dict(square=sq,cycle=sorted(c),target=target,other_neighbor=z,accepted=accept,failed=failed))
    assert len(out)==4;print(out[0]);print(out[-1]);(D/'ramsey_marked_third_site.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
