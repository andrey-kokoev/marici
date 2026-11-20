"""Reconstruct relaxed types on record 89 and enumerate old blue-triple clauses. Test menu and exact repair independently. Vertices printed in aligned coordinates (order maps them back to catalogue)."""
from pathlib import Path
from itertools import combinations,combinations_with_replacement
import json
H=Path(__file__).parent;load=lambda f:json.loads((H/f).read_text());swap=lambda m:((m&21845)<<1)|((m&43690)>>1);sites=lambda f:[i for i in range(16) if f>>i&1]
rows=[r for r in load('ramsey_one_center_census.json')['rows'] if not r['menu']];out=[]
for r in rows:
    matched=0
    for h in load('ramsey_strict_aligned_hosts.json'):
        if h['record']!=r['record']:continue
        N=h['N'];a,b,_=r['center'];I=[0]
        for i,n in enumerate(N):I += [m|1<<i for m in I if not m&n]
        if a not in I or b not in I:continue
        sets={k:[m for m in I if m.bit_count()==k] for k in (3,4,5)};T=[];S=[];K=[]
        for m in I:
            t=swap(m);u=m|t
            if m>t or any(not f&(x|m) for x in (a,b) for f in sets[5]) or any(not f&(a|b|m) for f in sets[4]):continue
            for red in (0,1):
                if (m&t if red else any(not f&u for f in sets[5]) or any(not f&(u|x) for x in (a,b) for f in sets[4])):continue
                T.append((m,t,red));S.append({(i,f) for x in (m,t) for i in sites(x) for f in sets[5] if not x&f});K.append({f for f in sets[3] if not red and not f&(u|a|b)})
        assert len(T)==3 and sum(not k for k in K)==1
        def common(ids):return set.intersection(*(S[i] for i in ids))
        def test(fs):
            ids=[i for i,k in enumerate(K) if not k.intersection(fs)];assert ids
            # <=3 partner types: a menu exists iff each pair shares some signature.
            return all(common([i,j]) for i,j in combinations_with_replacement(ids,2)),all(not K[i] for i in ids)
        assert test([])==(False,False);clauses=sorted(set.union(*K));menus=[f for f in clauses if test([f])[0]];exact=[f for f in clauses if test([f])[1]];assert all(test(clauses));matched+=1
        out.append(dict(record=r['record'],order=h['order'],center=r['center'],types=T,disqualifying_triples=[[sites(f) for f in sorted(k)] for k in K],single_menu_repairs=list(map(sites,menus)),single_exact_repairs=list(map(sites,exact))))
    assert matched==1
assert len(out)==2;print(out);(H/'ramsey_89_triple_repair.json').write_text(json.dumps(out,indent=2)+'\n')
