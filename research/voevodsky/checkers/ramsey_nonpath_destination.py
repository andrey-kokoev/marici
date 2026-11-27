"""Matched non-path controls for the recorded width-eleven destination, no changed rows."""
from itertools import combinations as choose
from pathlib import Path
import json


def audit(chord):
    k=11;sites=set(range(1,k+1));core={(i,i+1) for i in range(1,k)}|{chord};rows=[{1,5,10},{1,5,11},{1,4,10},{1,6,9},{3,6,9}];repairs={(0,4),(1,4)}
    def cliques(ids,links):
        vs=sorted(sites|{12+i for i in ids});red=core|{(s,12+i) for i in ids for s in rows[i]}|{(12+i,12+j) for i,j in links};return [[q for q in choose(vs,n) if all((e in red)==c for e in choose(q,2))] for n,c in [(3,True),(7,False)]]
    for i in [3,4]:assert cliques((0,1,2,i),set())==[[],[]]
    for i in (0,1):
        tri,blue=cliques((i,3,4),set());assert not tri and blue and all(not rows[j].isdisjoint(rows[l]) for j,l in [(i,3),(3,4)]) and rows[i].isdisjoint(rows[4])
    tri,blue=cliques(range(5),repairs);assert not tri
    H=sites-rows[3]-rows[4]-{1,10};maxima=next(f for n in range(len(H),-1,-1) if (f:=[q for q in choose(sorted(H),n) if all(e not in core for e in choose(q,2))]));must=set.intersection(*(set(q) for q in maxima));return dict(chord=chord,available=sorted(H),maximum_sets=maxima,mandatory=sorted(must),blue_after_repairs=blue)

if __name__=='__main__':
    out=list(map(audit,[(7,10),(2,5)]));assert out[0]['blue_after_repairs'] and not out[1]['blue_after_repairs'] and [4 in v['mandatory'] for v in out]==[False,True];assert tuple(sorted(12-i for i in (7,10)))==(2,5);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_nonpath_destination.json').write_text(json.dumps(out,indent=2)+'\n')
