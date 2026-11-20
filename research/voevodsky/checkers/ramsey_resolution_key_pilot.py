"""Frozen: K5 lex cuts 4..9 (at most six suffix variables); full resolution + subsumption, no completion access while building keys."""
from itertools import combinations
from pathlib import Path
import json, hashlib

# Forbidden cubes (positive-requirement mask, negative-requirement mask).
def minimal(cubes):
    kept=[]
    for p,n in sorted(set(cubes),key=lambda c:((c[0]|c[1]).bit_count(),c)):
        if not any((a&p,b&n)==(a,b) for a,b in kept):kept.append((p,n))
    return tuple(kept)

def close(key):
    while True:
        more=[]
        for (p,n),(q,m) in combinations(key,2):
            pivot=(p&m)|(n&q)
            if pivot.bit_count()==1:more.append(((p|q)&~pivot,(n|m)&~pivot))
        new=minimal([*key,*more]);
        if new==key:return key
        key=new

def test(k):
    E=list(combinations(range(5),2));cl=lambda vs:sum(1<<E.index(e) for e in combinations(vs,2));base=[(cl(t),0) for t in combinations(range(5),3)]+[(0,cl(t)) for t in combinations(range(5),k)];results=[]
    for cut in range(4,10):
        low=(1<<cut)-1;keys=[]
        for p in range(1<<cut):
            raw=minimal((a>>cut,b>>cut) for a,b in base if not (a&low&~p or b&p));keys.append((raw,close(raw)))
        # Independent complete-graph oracle using all vertex subsets, not the residuals.
        def ok(x):return all(any(not(x>>E.index(e)&1) for e in combinations(t,2)) for t in combinations(range(5),3)) and all(any(x>>E.index(e)&1 for e in combinations(t,2)) for t in combinations(range(5),k))
        seen={};inverse={};raw_live=set();live=0
        for p,(raw,key) in enumerate(keys):
            f=tuple(s for s in range(1<<(10-cut)) if ok(p|(s<<cut)));assert seen.setdefault(key,f)==f and inverse.setdefault(f,key)==key
            if f:raw_live.add(raw);live+=1
        results.append(dict(cut=cut,live_prefixes=live,raw_live_keys=len(raw_live),closed_live_keys=sum(bool(f) for f in inverse)))
    return results
if __name__=='__main__':
    out={str(k):test(k) for k in (3,4)};print(out);out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();(Path(__file__).resolve().parents[1]/'results/ramsey_resolution_key_pilot.json').write_text(json.dumps(out,indent=2)+'\n')
