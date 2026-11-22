"""All correlations stabilizing each representative unordered pair, counting only involutions; measure how many of the five unused paths each reverses in place."""
from collections import Counter
from itertools import permutations
from ramsey_ten_cycle_shift_census import enum,action,move,polarity,flags,D,json

def run():
    ms=list(enum());f=polarity()[0]['map'];duals=[]
    for p in permutations(range(6)):
        h=action(p);g=[h[f[i]] for i in range(30)]
        if all(g[g[i]]==i for i in range(30)):duals.append(g)
    out=[]
    for r in json.loads((D/'ramsey_ten_cycle_shift_census.json').read_text()):
        s,t=[ms[i] for i in r['representative']];adj={x:set() for x in range(30)}
        for i,j in flags-(s|t):adj[i].add(j);adj[j].add(i)
        paths=[];ends=set()
        for x in adj:
            if len(adj[x])!=1 or x in ends:continue
            w=[x];prev=None
            while adj[w[-1]]-{prev}:prev,y=w[-1],next(iter(adj[w[-1]]-{prev}));w.append(y)
            ends.update((x,w[-1]));paths.append(w)
        counts=Counter();
        for g in duals:
            a,b=move(s,g),move(t,g)
            if {a,b}!={s,t}:continue
            fixed=sum([g[i] for i in w]==w[::-1] for w in paths);counts[('preserve' if a==s else 'exchange',fixed)]+=1
        out.append(dict(rep=r['representative'],lengths=r['lengths'],endpoint_types=['mixed' if (w[0]<15)!=(w[-1]<15) else 'duads' if w[0]<15 else 'partitions' for w in paths],counts=[dict(action=k,fixed=n,count=v) for (k,n),v in sorted(counts.items())]))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_shared_middle_polarity_census.json').write_text(json.dumps(out)+'\n')
