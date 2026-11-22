"""Construct from naked decagons, no matching, polarity or row swap input. Keep each shortest antipodal path unused; force the remaining flag at BOTH internal vertices. Compare to one-ended constraints on marked cycle."""
from collections import Counter
from ramsey_folded_entry_handoff import P,T,D,json
from ramsey_history_matching_provenance import enum

def run():
    adj={x:set() for x in range(30)}
    for j,t in enumerate(T,15):
        for e in t:i=P.index(e);adj[i].add(j);adj[j].add(i)
    def walks(w):
        if len(w)==10:
            if w[0] in adj[w[-1]] and w[1]<w[-1]:yield w
        else:
            for y in adj[w[-1]]-set(w):
                if y>w[0]:yield from walks(w+[y])
    cnt=Counter();special=None;ms=list(enum());flag=lambda x,y:tuple(sorted((x,y)))
    for start in range(15):
        for w in walks([start]):
            left=set();right=set();arcs=[set(),set()];paths=[]
            for i,v in enumerate(w):
                arcs[i%2].add(flag(v,w[(i+1)%10]));
                if v<15:continue
                x=w[(i+5)%10];(d,k),=[(d,k) for d in adj[v] for k in adj[x] if k in adj[d]];p,=adj[d]-{v,k};q,=adj[k]-{d,x};left.add((d,p));right.add((q,k));paths.append([v,d,k,x])
            common=left|right;rows=[s|common for s in arcs];ok=all(len(s)==len(dict(s))==len({j for _,j in s})==15 for s in rows);cnt[(len(common),ok)]+=1
            if set(w)=={0,16,13,19,7,29,4,27,12,17}:
                valid=[m-arcs[0] for m in ms if arcs[0]<=m and (m-arcs[0])|arcs[1] in ms];special=dict(cycle=w,paths=paths,left=sorted(left),right=sorted(right),completion_counts=[sum(c<=s for s in valid) for c in [set(),left,right,common]])
                forced=set(left);rounds=[]
                while len(forced)<10:
                    occupied=set(w)|{v for e in forced for v in e};singles={flag(v,next(iter(adj[v]-occupied))) for v in adj.keys()-occupied if len(adj[v]-occupied)==1};assert singles and singles<=right;rounds.append(sorted(singles));forced.update(singles)
                special['one_end_propagation']=rounds
    return dict(census=[dict(forced=k,valid=v,cycles=n) for (k,v),n in cnt.items()],marked=special)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_open_shortcut_constructor.json').write_text(json.dumps(out)+'\n')
