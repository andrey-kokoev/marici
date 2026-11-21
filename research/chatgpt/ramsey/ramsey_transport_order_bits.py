"""Exact charged decisions for uniform labeled six-label Hall wirings. Fixed lex base and paired random controls. No per-witness order selection."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json,random,statistics
D=Path(__file__).parent
pairs=lambda n:list(combinations(range(n),2));P=pairs(6);T=[t for t in combinations(range(15),3) if len(set().union(*(P[i] for i in t)))==6];E=[e for e in pairs(15) if set(P[e[0]]).isdisjoint(P[e[1]])];Q=[]
def gen(path,seen):
    if len(path)==15:
        red={e for t,v in zip(T,path) for e in combinations(t,2) if v in e};Q.append(sum(1<<E.index(e) for e in red));return
    for v in T[len(path)]:
        if not seen>>v&1:gen(path+[v],seen|1<<v)
gen([],0);assert len(set(Q))==288
C=[sum(1<<i for i,q in enumerate(Q) if q>>j&1) for j in range(45)];F=(1<<288)-1
# Nested induced action: four columns -> six labels -> fifteen duads -> eligible links.
def lift(p,objects):return [objects.index(tuple(sorted((p[i],p[j])))) for i,j in objects]
def induced(p):return lift(lift(lift(p,pairs(4)),P),E)
j=induced([0,2,1,3]);a=induced([1,0,3,2]);b=induced([2,3,0,1]);assert all(a[b[x]]==b[a[x]] and j[a[j[x]]]==b[x] for x in range(45))
def group(order,gens):
    seen=set();out=[]
    for i in order:
        if i in seen:continue
        seen.add(i);q=[i]
        for v in q:
            for g in gens:
                if g[v] not in seen:q.append(g[v]);seen.add(g[v])
        out.extend(q)
    return out

def score(order):
    live=[(F,0)];hist=Counter()
    for i in order:
        nxt=[]
        for mask,d in live:
            x=mask&C[i];y=mask^x
            if not x or not y:nxt.append((mask,d));continue
            for z in (x,y):
                if z&(z-1):nxt.append((z,d+1))
                else:hist[d+1]+=1
        live=nxt
    assert not live and sum(hist.values())==288;return dict(sorted(hist.items()))
def total(h):return sum(i*n for i,n in h.items())
if __name__=='__main__':
    gens={'plain':[],'row':[j],'square':[a,b,j]};base=list(range(45));fixed={k:score(group(base,g)) for k,g in gens.items()};rng=random.Random(7308);samples=[]
    for _ in range(1000):
        rng.shuffle(base);samples.append([total(score(group(base,g))) for g in gens.values()]);
    out={'fixed':fixed,'random_seed':7308,'random_trials':len(samples),'random':{}}
    for i,k in enumerate(gens):
        vals=[row[i]/288 for row in samples];delta=[r[i]-r[0] for r in samples];out['random'][k]=dict(mean=statistics.mean(vals),min=min(vals),max=max(vals),better=sum(t<0 for t in delta),equal=delta.count(0),worse=sum(t>0 for t in delta));print(k,fixed[k],total(fixed[k])/288,out['random'][k]);
    (D/'ramsey_transport_order_bits.json').write_text(json.dumps(out)+'\n')
