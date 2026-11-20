"""Catalogue comparison: can six red spokes cover the old blue sixes, with/without a red triangle? Count minimum red triangles among six-spoke covers."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
H=Path(__file__).resolve().parents[1]; cat=H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6'; all6=[(sum(1<<i for i in t),t) for t in combinations(range(22),6)]; out=[]
for g in cat.read_text().splitlines():
    assert ord(g[0])==85; bits=''.join(f'{ord(x)-63:06b}' for x in g[1:]); n=[0]*22
    for j in range(22):
        for i in range(j):
            if bits[j*(j-1)//2+i]=='1': n[i]|=1<<j;n[j]|=1<<i
    assert not any(n[i]&n[j] for i,j in combinations(range(22),2) if n[i]>>j&1)
    six=[s for s,t in all6 if all(not(n[i]&s) for i in t)]; assert all(all(s>>i&1 or n[i]&s for i in range(22)) for s in six)
    hits=[sum(1<<j for j,s in enumerate(six) if s>>i&1) for i in range(22)];target=(1<<len(six))-1; best=99;w=None;miss=999
    for s,t in all6:
        a,b,c,d,e,f=t; union=hits[a]|hits[b]|hits[c]|hits[d]|hits[e]|hits[f]; k=(target^union).bit_count()
        if k==0:
            cost=sum((n[i]&s).bit_count() for i in t)//2
            if cost<best:best=cost;w=t
    # A smaller independent red set need not extend to a six. Check every maximal independent set too.
    def walk(s,available):
        global miss
        if not available:
            u=0
            for i in range(22):
                if s>>i&1:u|=hits[i]
            miss=min(miss,(target^u).bit_count());return
        while available:
            b=available&-available;available-=b;walk(s|b,available&~n[b.bit_length()-1])
    walk(0,(1<<22)-1);assert miss>0
    out.append(dict(record=len(out)+1,blue_sixes=len(six),min_triangles_with_six_red_spokes_and_no_blue_seven=best if w else None,example=w,min_blue_sevens_without_red_triangle=miss))
print(len(out), Counter(r['min_triangles_with_six_red_spokes_and_no_blue_seven'] for r in out), Counter(r['min_blue_sevens_without_red_triangle'] for r in out));(H/'results/ramsey_22_extension_color_cost.json').write_text(json.dumps(out,indent=2)+'\n')
