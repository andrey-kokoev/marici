"""Generate from the common four-site witnesses, not from five-row families."""
from itertools import combinations
from pathlib import Path
from collections import Counter
import json

ALL=frozenset(range(1,11));D=Path(__file__).resolve().parents[1]/'results'
def independent(s):return all(i+1 not in s for i in s)
def cap(s):
    p=0;v=0
    for i in sorted(s):
        if i!=p+1 or not v:v+=1;p=i
    return v

def safe(rows):
    return all(n+cap(ALL.difference(*q))<7 for n in range(len(rows)+1) for q in combinations(rows,n))

def run():
    count=Counter();out=set();samples={};shapes=Counter()
    for x in range(1,10):
        pair={x,x+1}
        for w in map(frozenset,combinations(sorted(ALL-pair),3)):
            if not all(independent(w|{j}) for j in pair):continue
            count['five_site_shapes']+=1;rem=ALL-pair-w
            for M in map(frozenset,combinations(sorted(rem),2)):
                T=rem-M
                if not independent(T) or not all(independent(M|{j}) for j in pair):continue
                for c,d in ((x,x+1),(x+1,x)):
                    C=M|{c};B=M|{d}
                    for y in M:
                        for Y in (y-1,y+1):
                            if Y not in ALL-(M|pair):continue
                            N=(M-{y})|{Y};E=N|{c}
                            if not all(independent(N|{j}) for j in pair):continue
                            for S in map(frozenset,combinations(sorted(rem),3)):
                                if not independent(S) or not S&M or not S&T or S in (C,B,E,T) or E==T:continue
                                count['candidates']+=1
                                if not safe((C,B,E,S)):count['first_attachment_rejected']+=1;continue
                                if not safe((C,B,E,T)):count['second_attachment_rejected']+=1;continue
                                # Remaining potential joint seven after both mandatory repairs:
                                # only E can accompany S,T.
                                if cap(ALL-S-T)>=5 or cap(ALL-S-T-E)>=4:count['residual_rejected']+=1;continue
                                key=(tuple(sorted(C)),tuple(sorted((tuple(sorted(B)),tuple(sorted(E))))),tuple(sorted((tuple(sorted(S)),tuple(sorted(T))))));assert key not in out;out.add(key);shapes[len(S&M)]+=1
                                if not samples:samples=dict(block=sorted(pair),W=sorted(w),M=sorted(M),T=sorted(T),S=sorted(S),parents=list(map(sorted,(C,B,E))))
    # Compare exact labeled family keys to the independently generated minimum-cut census.
    from ramsey_corner_joint_repairs import run as census
    old=set()
    def collect(ss,bad,opts):
        if sum((1<<i) in bad for i in range(3))!=2:return
        fmt=lambda r:tuple(i+1 for i in range(10) if r>>i&1)
        c,b,e,s,t=map(fmt,ss);old.add((c,tuple(sorted((b,e))),tuple(sorted((s,t)))))
    census(10,collect);assert old==out and len(out)==456
    result=dict(counts=count,generated=len(out),common_sites_used_by_S=shapes,example=samples);print(result);(D/'ramsey_shared_hub_generator.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':run()
