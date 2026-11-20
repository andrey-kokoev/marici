"""Test a destination-as-next-source convention separately from uninterrupted walking on the reflected cycle. Use literal routes, no completion decisions."""
import json
from pathlib import Path
from ramsey_strip_prism_proof import r,P,T

def swapped(p): return tuple(r[x] for x in p)
rows=json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text());first={tuple(z['path']) for z in rows if (z['path'][0],z['path'][1],z['path'][-2],z['path'][-1])==(0,16,7,29)};nexts={swapped(p) for p in first};assert len(first)==len(nexts)==5
for p in first:
    q=swapped(p);back=q[::-1];trip=p+back[1:];assert trip[-2:]==(17,0) and len(trip)==23 and len(set(trip))==22
    for n in nexts:
        assert n[:2]==(0,17) and n[-2:]==(4,29);assert trip[-2:]+n[1:2]==(17,0,17)
    assert [n for n in nexts if set(n[1:-1])==set(back[1:-1])]==[q]
print('Each of 5 trips: 5 destination-as-source routes; one retraces the entire reflected return. All immediately backtrack at pole 0.')
