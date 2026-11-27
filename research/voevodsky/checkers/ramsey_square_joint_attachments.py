"""Two independent literal swaps; all ports mutually blue. Keep distinct supports."""
from itertools import combinations
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json


def run(k):
    full=(1<<k)-1;rows=[sum(1<<i for i in t) for t in combinations(range(k),3) if min(t[1]-t[0],t[2]-t[1])>=2];R=set(rows);sq=set()
    for s in rows:
        moves=[3<<i for i in range(k-1) if (s&(3<<i)).bit_count()==1 and (s^(3<<i)) in R]
        for a,b in combinations(moves,2):
            if not a&b and s^a^b in R:sq.add(tuple(sorted((s,s^a,s^b,s^a^b))))
    cap=[]
    for mask in range(1<<k):
        free=full^mask;n=0
        while free:
            v=free&-free;n+=1;free&=~(v|(v<<1))
        cap.append(n)
    count=Counter();example={};display=lambda x:[i+1 for i in range(k) if x>>i&1]
    for p in sorted(sq):
        sub=[(0,0)]
        for m in p:sub+=[(u|m,h+1) for u,h in sub]
        U=sub[-1][0];assert U.bit_count()==5
        if any(cap[u]+h>=7 for u,h in sub):continue
        count['legal_squares']+=1;single=[s for s in rows if s not in p and all(cap[u|s]+h+1<7 for u,h in sub)]
        for s,t in combinations(single,2):
            mask=s|t;pred=(U|mask)==full;actual=all(cap[u|mask]+h+2<7 for u,h in sub);assert pred==actual
            count['eligible']+=1;label='pass' if pred else 'reject';count[label]+=1
            if label not in example:example[label]=dict(parent=list(map(display,p)),attachments=list(map(display,(s,t))),uncovered=display(full^(U|mask)))
    return dict(width=k,squares=len(sq),counts=count,examples=example)

if __name__=='__main__':
    out=[run(k) for k in range(6,13)];print([(v['width'],v['squares'],dict(v['counts'])) for v in out]);p=Path(__file__).resolve().parents[1]/'results/ramsey_square_joint_attachments.json';p.write_text(json.dumps(out,indent=2)+'\n')
