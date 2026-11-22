"""Allow zero-tick Hall intervals, keeping all observed apexes and exactly one native tour. Compare row-local minimum pauses with any synchronized clock. No graph inputs."""
from itertools import combinations_with_replacement
from ramsey_fan_clock_lift import native,orient,cycle,m,r,X,D,json,apex,permutations

def admissible_pairs():
    ds=cycle(m)[::2]
    for p in permutations('ABCD'):
        if {p[0],p[-1]}!={'A','B'}:continue
        fits=[]
        for d in (ds,[r[i] for i in ds]):
            a,b=orient(d,X)[-1]['arrow'];i,=[i for i,x in enumerate(d) if apex(x)==a];pins=[apex(x) for x in d[i:]+d[:i]]+[a];assert pins==[a,1,b,None,None,a];row=[]
            for t in native():
                w=t['word'];k,=[i for i,e in enumerate(w) if e[0]==p[a-1]];v=[e[0] for e in w[k:]+w[:k]]+[p[a-1]]
                for ks in combinations_with_replacement(range(7),4):
                    times=(0,*ks,6)
                    if all(c is None or v[j]==p[c-1] for j,c in zip(times,pins)):row.append((times,t['seam'],sum(x==y for x,y in zip(times,times[1:]))))
            fits.append(row)
        yield p,fits

def run():
    out=[]
    for p,fits in admissible_pairs():
        assert not ({s for s,_,_ in fits[0]}&{s for s,_,_ in fits[1]});summ=[]
        for row in fits:
            n=min(f[2] for f in row);best=[f for f in row if f[2]==n];assert {f[1] for f in best}=={p[0]};summ.append(dict(min_pauses=n,min_clock_count=len(best),seam=p[0],example=best[0][0],all_seams=sorted({f[1] for f in row})))
        out.append(dict(binding=''.join(p),rows=summ,shared_clocks=0))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_stuttering_fan_clock.json').write_text(json.dumps(out)+'\n')
