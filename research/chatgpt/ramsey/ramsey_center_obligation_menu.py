"""Predict from the old red graph and the blue center ONLY. An outer slot must hit old fives missed by either center slot and old fours missed by both. A minimal independent transversal m encodes a subtree of potential slot neighborhoods. Every extension hits each vertex of m and avoids N(m). A signature forced by m or its mirror holds for the aligned partner regardless of extension. Look for three such certificates each transversal guarantees at least two of. No two-pair legality tests or legal partner input during derivation."""
from pathlib import Path
from itertools import combinations
import json
H=Path(__file__).parent;load=lambda f:json.loads((H/f).read_text());sw=lambda m:((m&21845)<<1)|((m&43690)>>1)
def predict(N,center):
    a,b,_=center;I=[0]
    for i,n in enumerate(N):I += [m|1<<i for m in I if not n&m]
    fives=[m for m in I if m.bit_count()==5];clauses=[m for m in I if (m.bit_count()==4 and not m&(a|b)) or (m.bit_count()==5 and (not m&a or not m&b))];mins=[]
    for m in sorted(I,key=int.bit_count):
        if all(m&c for c in clauses) and not any(t&m==t for t in mins):mins.append(m)
    dom=lambda m:sum_union(N[i] for i in range(16) if m>>i&1);patterns={};full=(1<<len(mins))-1
    for f in fives:
        for r in range(16):
            support=sum(1<<j for j,m in enumerate(mins) if any(x>>r&1 and dom(x)&f==f for x in (m,sw(m))))
            if support:patterns.setdefault(support,[r,f])
    maximal=[s for s in patterns if not any(s!=t and s&t==s for t in patterns)]
    menu=None
    if full in patterns:menu=[patterns[full]]
    else:
        for p,q,r in combinations(maximal,3):
            if ((p&q)|(p&r)|(q&r))==full:menu=[patterns[i] for i in (p,q,r)];break
    # Stronger falsifier: can ANY menu, even arbitrarily large, work on the
    # full set of paired single-slot candidates before enforcing joint legality?
    slots=[m for m in I if m<=sw(m) and any(t&m==t for t in mins)]
    def sig(m):return {(r,f) for x in (m,sw(m)) for r in range(16) if x>>r&1 for f in fives if not x&f}
    signatures=[sig(m) for m in slots];bad=[(slots[i],slots[j]) for i in range(len(slots)) for j in range(i+1) if signatures[i].isdisjoint(signatures[j])]
    relaxedMenu=None
    if not bad:
        masks={sum(1<<j for j,s in enumerate(signatures) if cert in s):cert for cert in sorted(set.union(*signatures))};maxima=[s for s in masks if not any(s!=t and s&t==s for t in masks)];full=(1<<len(slots))-1
        for p,q,r in combinations(maxima,3):
            if ((p&q)|(p&r)|(q&r))==full:relaxedMenu=[masks[x] for x in (p,q,r)];break
    return dict(clauses=len(clauses),minimal=len(mins),menu=menu,relaxedSlotPairs=len(slots),uncoveredPartnerCombinations=len(bad),firstUncovered=next(iter(bad),None),relaxedMenu=relaxedMenu)
def sum_union(ms):
    a=0
    for m in ms:a|=m
    return a
hosts={(h['record'],tuple(h['order'])):h['N'] for h in load('ramsey_strict_aligned_hosts.json')};out=[]
for row in load('ramsey_signature_core.json'):
    res=predict(hosts[row['record'],tuple(row['order'])],row['center']);menu=res['menu'];
    if menu:assert all(sum(any((s>>r&1) and not s&f for s in p[:2]) for r,f in menu)>=min(2,len(menu)) for p in row['partners'])
    out.append(dict(record=row['record'],center=row['center'],**res));print(row['record'],res)
(H/'ramsey_center_obligation_menu.json').write_text(json.dumps(out,indent=2)+'\n')
