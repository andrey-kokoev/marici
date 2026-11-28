"""Read the installed diagonal with a fresh row: all supports vs later same-half occurrences."""
from itertools import combinations
from collections import Counter
import json
from ramsey_cube_opposite_face import marked_faces,analyze,charts,path,D,independent_sets


def options(sq,diag,cyc,probes):
    g=path|cyc|{(i,11+j) for j,s in enumerate(sq+diag) for i in s}|{(11+j,15+k) for j,r in enumerate(sq) for k,s in enumerate(diag) if set(r).isdisjoint(s)};sixes=independent_sets(16,g,6);edges=[(1<<i)|(1<<j) for i,j in g];out={}
    for r in probes:
        base=sum(1<<i for i in r)+sum(1<<(11+j) for j,s in enumerate(sq) if set(s).isdisjoint(r));possible=[j for j,s in enumerate(diag) if set(s).isdisjoint(r)]
        for n in range(len(possible)+1):
            for es in combinations(possible,n):
                red=base+sum(1<<(15+j) for j in es)
                if all(red&e!=e for e in edges) and all(red&q for q in sixes):out[r]=es;break
            if r in out:break
    return out


def audit():
    table=analyze(10);upper=sorted(map(tuple,table['leftover']))+ [tuple(r) for p in table['pieces'] for r in p['new']];upper=sorted(upper);halves={'upper':upper,'mirror':[tuple(11-i for i in reversed(r)) for r in reversed(upper)]};all_rows={r for r in combinations(range(1,11),3) if all(e not in path for e in combinations(r,2))};census=dict((sq,cs) for sq,_,cs in charts());hist=Counter();examples={};sizes=Counter();immediate=0
    for half,start,sq,opp in marked_faces():
        sheet=halves[half];corners=set(sq+opp);later=sheet[max(sheet.index(r) for r in corners)+1:];diags=[p for p in combinations(opp,2) if len(set(p[0])&set(p[1]))==1];assert len(diags)==2
        for c in census.get(sq,[]):
            a,b=[options(sq,d,c,all_rows-corners) for d in diags];delta=set(a)^set(b);after=[r for r in later if r in delta];hist[bool(delta),bool(after)]+=1;sizes[len(set(a)-set(b))>0,len(set(b)-set(a))>0]+=1
            immediate+=bool(later and later[0] in delta)
            if after:
                r=after[0];i=int(r in b);examples.setdefault('later',dict(half=half,start=start,square=sq,cycle=sorted(c),diagonals=diags,probe=r,accepts=i,red_to=[diags[i][j] for j in (a,b)[i][r]],rows_between=later.index(r)))
            if not delta:examples.setdefault('equal',dict(square=sq,cycle=sorted(c),diagonals=diags,legal_rows=sorted(a)))
    assert sum(hist.values())==256
    result=dict(immediate_next=immediate,by_any_and_later={str(k):v for k,v in hist.items()},directions={str(k):v for k,v in sizes.items()},examples=examples);print(result);(D/'ramsey_cube_diagonal_readout.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':audit()
