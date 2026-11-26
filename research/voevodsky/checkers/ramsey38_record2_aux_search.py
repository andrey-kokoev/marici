"""Constructive breadth-first search by shelling outward from the three observed cells."""
from itertools import combinations
from functools import reduce
from ramsey38_record2_spanning_disk import p,rows
from ramsey38_support_ball_completion import shelling
from ramsey38_compare_support_fillings import boundary
labels=sorted(p)+[28];n=len(labels)
def code(s):return sum(1<<labels.index(i) for i in s)
def decode(s):return frozenset(a for i,a in enumerate(labels) if s>>i&1)
def closure(s):
    t=s;h=0
    while t:h|=1<<t;t=(t-1)&s
    return h
cells=[code(t) for t in combinations(labels,4)];cl={t:closure(t) for t in cells};F={t:[t^(1<<i) for i in range(n) if t>>i&1] for t in cells}; fm={t:sum(1<<f for f in F[t]) for t in cells};groups={}
for t in cells:
    for k in (1,2,3):
        for fs in combinations(F[t],k):groups[t,sum(1<<f for f in fs)]=reduce(int.__or__,map(closure,fs))
req=sum(1<<code(s) for s in set(rows.values()) if len(s)<4 and s!=rows[7]);rel=1<<code(rows[7]);fixed=tuple(code(rows[i]) for i in (4,26,12)) # valid shelling of the starting ball
def search():
    allc=bd=0
    for t in fixed:allc|=cl[t];bd^=fm[t]
    Q=[(allc,bd,fixed)];seen={allc}
    while Q:
        nex=[]
        for allc,bd,order in Q:
            for t in cells:
                shared=bd&fm[t];match=groups.get((t,shared))
                if match is None or cl[t]&allc!=match:continue
                ac=allc|cl[t];newbd=bd^fm[t]
                if ac in seen:continue
                seen.add(ac);surf=0;bits=newbd
                while bits:
                    b=bits&-bits;bits-=b;surf|=closure(b.bit_length()-1)
                if req&ac&~surf:continue
                seq=order+(t,)
                if req&~surf==0 and not rel&surf:
                    ts=list(map(decode,seq));print('found:',[sorted(t) for t in ts]);bd_faces=boundary(ts)
                    assert shelling(frozenset(ts)) and all(any(r<=t for t in ts) for r in rows.values())
                    assert {v for v,r in rows.items() if len(r)<4 and not any(r<=f for f in bd_faces)}=={7}
                    e=rows[2];print('new fan endpoints:',sorted(set.union(set(),*(f-e for f in bd_faces if e<=f))))
                    print('link of released edge:',sorted(sorted(t-rows[7]) for t in ts if rows[7]<=t));return
                nex.append((ac,newbd,seq))
        print('length',len(Q[0][2])+1,'frontier',len(nex),flush=True);Q=nex
def seven_label_lower_bound():
    import ramsey38_release_census as census
    from ramsey38_rotation_holdout import g
    from unittest.mock import patch
    with patch.object(census,'N',g):ls,_,buckets=census.predict(19)
    e=rows[2];assert e=={8,11};link=[rows[v]-e for v in (4,26,12)];assert link==[{6,16},{16,25},{20,25}]
    for fset in buckets[0]+buckets[7]:
        fs=[{ls[i] for i in census.bits(f)} for f in fset];ends=set.union(set(),*(f-e for f in fs if e<=f));assert len(ends)==2 and ends&{16,25};print('seven-label fan endpoints:',sorted(ends))
if __name__=='__main__':seven_label_lower_bound();search()
