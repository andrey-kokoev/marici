"""Does the set of positive gaps determine the fresh corners' one-port continuation profile on an even red path? Labels start at 1; masks start at bit 0."""
from itertools import combinations, product
from collections import defaultdict
from pathlib import Path
import json

def trial(w):
    k=w//2+2
    domain=[t for t in range(1<<w) if not t&(t<<1)]
    danger=[t for t in domain if t.bit_count()==k-2]
    families=defaultdict(list); memo={}
    for a,b,c in combinations(range(1,w),3):
        if min(b-a,c-b)<3:continue
        gaps=(a-1,b-a-3,c-b-3); pattern=tuple(i for i,t in enumerate(gaps) if t)
        sizes=[]; exts=[];corners=[]
        for delta in product(range(2),repeat=3):
            if any(not delta[i] for i in pattern):continue
            corner=tuple(t+d for t,d in zip((a,b,c),delta));s=sum(1<<(t-1) for t in corner)
            if s not in memo:memo[s]=frozenset(t for t in domain if all((s|t)&u for u in danger))
            exts.append(memo[s]);sizes.append(len(exts[-1]));corners.append(corner)
        families[pattern].append(((a,b,c),tuple(sorted(sizes)),tuple(exts),corners,gaps))
    out=[]
    for pat,rows in families.items():
        ex=None
        for x,y in combinations(rows,2):
            if x[1]==y[1] or sum(x[4])!=sum(y[4]):continue
            j=next(j for j,(e,f) in enumerate(zip(x[2],y[2])) if len(e)!=len(f));t=min(x[2][j]^y[2][j],key=lambda t:(t.bit_count(),t));ex=dict(starts=[x[0],y[0]],gaps=[x[4],y[4]],profiles=[x[1],y[1]],corners=[x[3][j],y[3][j]],support=[v+1 for v in range(w) if t>>v&1],accepted=[t in x[2][j],t in y[2][j]]);break
        out.append(dict(positive=pat,cubes=len(rows),distinct_size_profiles=len({r[1] for r in rows}),distinct_labeled_profiles=len({r[2] for r in rows}),same_layer_example=ex))
    return dict(width=w,blue_threshold=k,domain=len(domain),groups=out)
if __name__=='__main__':
    res=[trial(w) for w in (8,10,12,14)];p=Path(__file__).resolve().parents[1]/'results'/'ramsey_cube_gap_transfer.json';p.write_text(json.dumps(res,indent=1)+'\n');
    for r in res:
        ex=next((g['same_layer_example'] for g in r['groups'] if g['same_layer_example']),None);print(r['width'],ex)
