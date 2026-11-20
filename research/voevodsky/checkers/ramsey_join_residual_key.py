"""Residual join key pilot. Build keys from constraint tables only; independent full-color oracle.
Predeclared order: edges sorted by (larger endpoint, smaller endpoint); every prefix cut.
K1 = residual forbidden rows with containment pruning; K2 also conditions on forced unit colors.
No satisfiability test inside either key. First run (3,3), then same code for (3,4).
"""
from itertools import combinations
from collections import defaultdict
import json

def constraints(n,k):
    edges=[(i,j) for j in range(n) for i in range(j)]; masks={r:[sum(1<<edges.index(e) for e in combinations(t,2)) for t in combinations(range(n),r)] for r in {3,k}};return edges,masks

def residual(clauses,cut,value,unit):
    # A mask pair (R,B) forbids the simultaneous specified red and blue bits.
    assigned=(1<<cut)-1;red=value;blue=assigned^value;forced_r=forced_b=0
    while True:
        active={(r&~(red|blue),b&~(red|blue)) for r,b in clauses if not(r&blue or b&red)}
        if (0,0) in active:return ('dead',)
        if not unit:break
        r1=b1=0
        for r,b in active:
            if (r|b).bit_count()==1:r1|=b;b1|=r
        if r1&b1:return ('dead',)
        if not (r1|b1):break
        red|=r1;blue|=b1;forced_r|=r1;forced_b|=b1
    keep=[]
    for r,b in sorted(active,key=lambda t:((t[0]|t[1]).bit_count(),t)):
        if not any(x&r==x and y&b==y for x,y in keep):keep.append((r,b))
    return forced_r,forced_b,tuple(keep)

def run(n,k):
    edges,masks=constraints(n,k);m=len(edges);cl=[(r,0) for r in masks[3]]+[(0,b) for b in masks[k]]
    # Oracle: direct tuple tests; no access to residual keys. Generate all labeled completions.
    models=[v for v in range(1<<m) if all(v&r!=r for r in masks[3]) and all(v&b for b in masks[k])];report=[];example={};merge={}
    for cut in range(m):
        mask=(1<<cut)-1;future=defaultdict(list)
        for v in models:future[v&mask].append(v>>cut)
        # Partial join rows must satisfy every already fully assigned pattern.
        inside=[(r,b) for r,b in cl if (r|b)&~mask==0];rows=[x for x in range(1<<cut) if not any(x&r==r and x&b==0 for r,b in inside)]
        for mode in ('K1','K2'):
            by_key={};by_future={};live_keys=set();deadkeys=set();live=0
            for x in rows:
                key=residual(cl,cut,x,mode=='K2');f=tuple(future.get(x,()));rep=by_key.setdefault(key,x);assert future.get(rep,[])==list(f),'unsound merge'
                other=by_future.setdefault(f,(x,key));
                if other[1]!=key and f:example.setdefault(mode,dict(cut=cut,prefixes=[other[0],x],exterior=list(f),keys=[other[1],key]))
                if f:
                    live+=1;live_keys.add(key)
                    if x!=rep:merge.setdefault(mode,dict(cut=cut,prefixes=[rep,x],completion_count=len(f)))
                else:deadkeys.add(key)
            report.append(dict(cut=cut,mode=mode,rows=len(rows),live_rows=live,live_keys=len(live_keys),live_futures=sum(bool(f) for f in by_future),dead_keys=len(deadkeys)))
    return dict(n=n,k=k,edges=edges,model_count=len(models),cuts=report,first_live_false_split=example,first_live_merge=merge)
if __name__=='__main__':
    from pathlib import Path
    results=[run(n,k) for k in (3,4) for n in (5,6)]
    for r in results:
        print((3,r['k']),r['n'],'models',r['model_count'])
        for mode in ('K1','K2'):
            rows=[t for t in r['cuts'] if t['mode']==mode];print(mode,'live split cuts',[t['cut'] for t in rows if t['live_keys']>t['live_futures']],'split dead cuts',[t['cut'] for t in rows if t['dead_keys']>1],'first live merger',r['first_live_merge'].get(mode),'first false split',str(r['first_live_false_split'].get(mode))[:480])
    (Path(__file__).resolve().parents[1]/'results/ramsey_join_residual_key.json').write_text(json.dumps(results,indent=1)+'\n')
