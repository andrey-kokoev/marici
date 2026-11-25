"""Replay the adjacent-overlap formula on every fresh corner of every cube of four even paths. Labels are one-based and the two ports are mutually blue."""
from itertools import combinations,product
from math import comb
from pathlib import Path
import json

def scan(m):
    w=2*m; cuts=[sum(1<<(2*i+(i>=j)) for i in range(m)) for j in range(m+1)]
    dom=[t for t in range(1<<w) if not t&(t<<1)];miss={t:[j for j,u in enumerate(cuts) if not u&t] for t in dom};rows=[];groups={};examples={};cache={}
    C=lambda n,r:comb(n,r) if 0<=r<=n else 0
    for a,b,c in combinations(range(1,w),3):
        if min(b-a,c-b)<3:continue
        gaps=(a-1,b-a-3,c-b-3);pat=tuple(bool(x) for x in gaps)
        for ds in product(range(2),repeat=3):
            if any(p and not d for p,d in zip(pat,ds)):continue
            corner=tuple(i+d for i,d in zip((a,b,c),ds));s=sum(1<<(v-1) for v in corner);J=tuple(miss[s]);L=len(J);B=sum(j in (0,m) for j in J)
            if J not in cache:
                denied={t for t in dom if set(J).intersection(miss[t])};pr=tuple(sum(t.bit_count()==r for t in denied) for r in range(m+1));assert pr==tuple(L*C(m,r)-(L-B)*C(m-2,r-2)-max(0,L-1)*C(m-1,r) for r in range(m+1));cache[J]=(pr,denied)
            pr,denied=cache[J];key=(pat,pr);row=dict(start=(a,b,c),corner=corner,cuts=J);rows.append(row)
            for old in groups.get(key,[]):
                A=cache[tuple(old['cuts'])][1];d=A^denied
                if d and 'equal_profile_different_labels' not in examples:
                    t=min(d,key=lambda x:(x.bit_count(),x));examples['equal_profile_different_labels']=dict(rows=[old,row],T=[i+1 for i in range(w) if t>>i&1],allowed=[t not in A,t not in denied],accepted=len(dom)-len(A))
            groups.setdefault(key,[]).append(row)
    return dict(width=w,fresh_corners=len(rows),cut_intervals=len(cache),distinct_domains=len({frozenset(d) for _,d in cache.values()}),distinct_profiles=len({p for p,_ in cache.values()}),**examples)
if __name__=='__main__':
    res=[scan(m) for m in range(4,8)];print(res);(Path(__file__).resolve().parents[1]/'results'/'ramsey_cube_cut_overlap.json').write_text(json.dumps(res,indent=1)+'\n')
