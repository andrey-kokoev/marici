"""Width-ten source criterion for each corner separately forcing a repair."""
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json


def run():
    k=10;F=(1<<k)-1;rows=[sum(1<<i for i in s) for s in combinations(range(k),3) if min(s[1]-s[0],s[2]-s[1])>=2];R=set(rows);cap=[]
    for m in range(F+1):
        q=m;n=0
        while q:b=q&-q;n+=1;q&=~(b|b<<1)
        cap.append(n)
    n=Counter();patterns=Counter();ex={};fmt=lambda m:[i+1 for i in range(k) if m>>i&1]
    for c in rows:
        moves=[3<<i for i in range(k-1) if (c&(3<<i)).bit_count()==1 and c^(3<<i) in R]
        for a,b in combinations(moves,2):
            if a&b or c^a^b not in R:continue
            p=(c,c^a,c^b);subs=[(0,0)]
            for row in p:subs +=[(d+1,u|row) for d,u in subs]
            if any(d+cap[F^u]>=7 for d,u in subs):continue
            singles=[s for s in rows if s not in p and all(d+1+cap[F&~(s|u)]<7 for d,u in subs)]
            for s,t in combinations(singles,2):
                if not s&t:continue
                z=F&~(s|t)
                if cap[z]>=5:continue
                helpers=[]
                for row in p:
                    ok=[]
                    for tag,(h,o) in enumerate(((s,t),(t,s))):
                        if row&h:continue
                        rest=F^(row|h);assert rest.bit_count()==4
                        if not(rest&(rest>>1)) and not(rest&o):ok.append(tag)
                    assert len(ok)<=1
                    if not ok:break
                    helpers.append(ok[0])
                if len(helpers)!=3:continue
                kind='same' if len(set(helpers))==1 else 'split';patterns[kind,s.bit_count()-(s&t).bit_count()]+=1;n['total']+=1
                if kind not in ex:ex[kind]=dict(rows=list(map(fmt,p)),new=list(map(fmt,(s,t))),helper_indices=helpers)
    assert n['total']==104;out=dict(width=k,count=n,helper_patterns={str(key):v for key,v in patterns.items()},examples=ex);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_corner_saturation.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
