"""Fixed-host double common-minus neighborhoods and one-root exchanges between extremal quartets."""
from itertools import combinations
from collections import Counter,defaultdict
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results'
def main():
    U=frozenset(range(35));P=[set() for _ in U]
    for a,b in json.loads((D/'ramsey_39_glue_vs_circle.json').read_text())['plus_edges']:P[a].add(b);P[b].add(a)
    def perp(q):return U.difference(q,*[P[i] for i in q])
    best={};bytriple=defaultdict(list);allroots=0;fib=defaultdict(list)
    for t in combinations(range(35),4):
        if any(j in P[i] for i,j in combinations(t,2)):continue
        q=frozenset(t);c=perp(q);fib[c].append(q);allroots+=1
        if len(c)!=13:continue
        assert perp(c)==q
        k=sum(len(P[i]&P[j])==4 for i,j in combinations(t,2));shape={3:'P',4:'C'}[k];best[q]=(c,shape)
        for tr in combinations(t,3):bytriple[tr].append(q)
    stats=Counter();adj=defaultdict(set);ex=None
    for roots in bytriple.values():
        for a,b in combinations(roots,2):
            c,s=best[a];d,t=best[b];lost=len(c-d);stats[''.join(sorted((s,t))),lost]+=1;adj[a].add(b);adj[b].add(a)
            if lost==1 and s!=t and ex is None:ex=dict(roots=[sorted(a),sorted(b)],common_core=sorted(c&d),swapped=[sorted(c-d),sorted(d-c)])
    left=set(best);comps=Counter();parts=[]
    while left:
        v=left.pop();todo=[v];size=0;part=set()
        while todo:
            v=todo.pop();part.add(v);size+=1;fresh=left&adj[v];left-=fresh;todo.extend(fresh)
        comps[size]+=1;parts.append(part)
    def move(part,m,b):return {frozenset((m*i+b)%35 for i in q) for q in part}
    shift_fixed=all(move(part,1,1)==part for part in parts);mult_cycles=(len(parts)==3 and all(move(part,11,0) in parts and move(part,11,0)!=part for part in parts));assert shift_fixed and mult_cycles
    res=dict(translation_preserves_components=shift_fixed,multiplier_11_cycles_components=mult_cycles,legal_quartets=allroots,distinct_extremal_cores=len(best),all_extremal_recovered=all(len(fib[c])==1 for c,_ in best.values()),exchange_counts={f'{s}:replace_{k}':v for (s,k),v in stats.items()},exchange_degrees=dict(Counter(len(adj[q]) for q in best)),component_sizes=dict(comps),example=ex);print(res);(D/'ramsey_39_core_exchange.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':main()
