"""Check the ordered 269 probe and whether any safe probe can classify the empty branch early."""
import json
from ramsey_cube_diagonal_colors import colors
from ramsey_cube_diagonal_pairs import charts, profile, D


def audit():
    sq=((1,4,8),(1,4,9),(1,5,8),(1,5,9)); diag=((2,4,9),(2,5,8))
    early=json.loads((D/'ramsey_early_neighbor_read.json').read_text());out=[]
    p=(2,6,9);r7=(3,5,7);r10=(3,5,10)
    for c in next(cs for s,_,cs in charts() if s==sq):
        pf=profile(sq,diag,c,[p,r7,r10]);z,=[e[1] for e in c if e[0]==2 and e[1]!=3]
        yes=p in pf[1];probe=r7 if yes else r10;t=(p,probe) if yes else (probe,)
        want=((0,1) if yes else (1,),());ok=all(r in pf[1] for r in t) and want in colors(pf,t)
        assert yes==(z==7) and ok==(z!=6)
        out.append(dict(cycle=sorted(c),neighbor=z,accepted_269=yes,next_row=probe,marked_success=ok))
    safe=[r for r in early['rows'] if r['after_cube'] and all(not a or j or z==6 for a,j,z in zip(r['obs'],r['joint'],early['neighbors']))];assert [r['row'] for r in safe]==[[2,6,9]]
    # All other informative rows precede 269. With no positives after it,
    # the negative branch has no remaining test to split 10 from 6.
    assert all(tuple(r['row'])<=p for r in early['rows'] if r['after_cube'])
    (D/'ramsey_safe_suffix_read.json').write_text(json.dumps(out,indent=2)+'\n');print([(r['neighbor'],r['accepted_269'],r['marked_success']) for r in out])

if __name__=='__main__':audit()
