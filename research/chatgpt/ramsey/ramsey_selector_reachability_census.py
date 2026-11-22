"""Compare candidate certification, the retained vs visited exit, and live first-two-event behavior over the same 36 boundary-compatible records. No assumed traversal timeout."""
from collections import Counter
from itertools import permutations
from ramsey_three_selector_interventions import match,rho,P,X,D,json,apex,registry,execute,validate

def run():
    out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        supp={d:{e for e in registry if any(set(e)=={p[i-1] for i in X[k]} for k in P[d])} for d in range(15)};hist=Counter();examples={}
        for m in match():
            n={rho[d]:rho[j] for d,j in m.items()};rows=[]
            for col,f,g in [(2,m,n),(3,n,m)]:
                inv={j:d for d,j in g.items()};x=0;lap=[]
                while True:
                    j=f[x];y=inv[j];lap.extend([(x,j,x),(j,y,y)]);x=y
                    if x==0:break
                tail=p[col-1];head,={'C','D'}-{tail};word,=[(a,b) for a in registry for b in registry if a[0]==tail and a[1]==b[0] and b[1]==head];ds=[t[2] for t in lap[:4]];cert=any(word[0] in supp[ds[i]] and word[1] in supp[ds[j]] for i,j in [(0,3),(3,2)]);ex=supp[{j:d for d,j in f.items()}[29]]|supp[inv[29]];assert set(word)<=ex;validate(execute(word));visited=any(j==29 for _,j,_ in lap)
                pos=0;v=None;events=[];seen=set();status='no progress'
                while (pos,v,tuple(events)) not in seen:
                    seen.add((pos,v,tuple(events)));x,y,d=lap[pos];pos=(pos+1)%len(lap)
                    if x<15 and v is None and apex(x)==col:v=tail
                    opts=[e for e in supp[d] if e[0]==v];
                    if len(opts)>1:status='branch';break
                    if opts:
                        e,=opts;events.append(e);v=e[1]
                        if len(events)==2:status='hit' if tuple(events)==word else 'other pair';break
                rows.append((cert,visited,status))
            key=(all(s[0] for s in rows),all(s[1] for s in rows),tuple(s[2] for s in rows));hist[key]+=1;examples.setdefault(key,list(m.values()))
        assert sum(hist.values())==36;out.append(dict(binding=''.join(p),classes=[dict(both_certified=k[0],exit_reached=k[1],live=k[2],n=v,example=examples[k]) for k,v in hist.items()]))
    return out
if __name__=='__main__':
    out=run();print([(r['both_certified'],r['exit_reached'],r['live'],r['n']) for r in out[0]['classes']]);(D/'ramsey_selector_reachability_census.json').write_text(json.dumps(out)+'\n')
