"""Can a fixed 3+7 split of the ten middle sites label ordered continuation samples by the four channel/sign ports? Exhaust all splits and allow any lookup from block to port; report best number correctly classified. Also test red-only samples and one pole at a time. This tests block membership, not arbitrary block operators."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict,Counter
import json
D=Path(__file__).resolve().parents[1]/'results';rows=json.loads((D/'ramsey_37_ordered_star_sign.json').read_text());V=sorted({r['slot'] for r in rows});assert len(V)==10
out={}
for pole in ('pole0','pole6','both'):
    for red in (False,True):
        T=[r for r in rows if (pole=='both' or r['pole']==pole) and (not red or r['red'])];best=-1;hist=Counter()
        for a in combinations(V,3):
            cells=defaultdict(Counter)
            for r in T:cells[r['slot'] in a,r['continuation'] in a][('A' if r['local_step']>0 else 'B')+('+' if r['change']>0 else '-')]+=1
            score=sum(max(c.values()) for c in cells.values());hist[score]+=1
            if score>best:best=score;ex=a
        out[pole+(' red' if red else ' all')]=dict(total=len(T),best=best,example=ex,hist=dict(hist))
print(out);(D/'ramsey_37_star_block_feed.json').write_text(json.dumps(out,indent=2)+'\n')
