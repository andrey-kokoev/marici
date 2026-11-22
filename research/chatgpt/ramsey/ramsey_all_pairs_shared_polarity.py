"""Remove decagon premise. Use all S6 orbits of distinct unordered pairs (criterion symmetric); test every pair-stabilizing correlation that is involutory. Nonempty path condition excludes equal rows."""
from itertools import combinations,permutations
from collections import Counter
from ramsey_ten_cycle_shift_census import enum,action,move,polarity,flags,D,json

def run():
    ms=list(enum());ix={s:i for i,s in enumerate(ms)};base=polarity()[0]['map'];maps=[];duals=[]
    for p in permutations(range(6)):
        h=action(p);maps.append(h);g=[h[base[i]] for i in range(30)]
        if all(g[g[x]]==x for x in range(30)):duals.append(g)
    pending=set(combinations(range(len(ms)),2));out=[]
    while pending:
        i,j=next(iter(pending));s,t=ms[i],ms[j];orb={tuple(sorted((ix[move(s,h)],ix[move(t,h)]))) for h in maps};pending-=orb;adj={x:set() for x in range(30)}
        for x,y in flags-(s|t):adj[x].add(y);adj[y].add(x)
        ends=set();paths=[]
        for x in adj:
            if x in ends or len(adj[x])!=1:continue
            path=[x];prev=None
            while adj[path[-1]]-{prev}:prev,z=path[-1],next(iter(adj[path[-1]]-{prev}));path.append(z)
            ends.update((x,path[-1]));paths.append(path)
        counts=Counter();unrestricted=0
        for g in duals:
            if not all(all(g[v]==w for v,w in zip(path,path[::-1])) for path in paths):continue
            unrestricted+=1;a,b=move(s,g),move(t,g)
            if {a,b}=={s,t}:counts['preserve' if a==s else 'exchange']+=1
        perm={x:dict(t)[y] for y,x in s};left=set(perm);sizes=[]
        while left:
            x=next(iter(left));k=0
            while x in left:left.remove(x);x=perm[x];k+=1
            if k>1:sizes.append(2*k)
        out.append(dict(rep=[i,j],size=len(orb),active=sorted(sizes),paths=sorted(len(w)-1 for w in paths),counts=dict(counts),unrestricted=unrestricted))
    assert sum(r['size'] for r in out)==41328;return sorted(out,key=lambda r:r['rep'])
if __name__=='__main__':
    out=run();print('orbits',len(out),'hits',[(q['size'],q['active'],q['paths'],q['counts']) for q in out if q['counts']]);(D/'ramsey_all_pairs_shared_polarity.json').write_text(json.dumps(out)+'\n')
