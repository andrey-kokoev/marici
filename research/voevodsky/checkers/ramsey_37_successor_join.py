"""Check one native same-clock successor: which red-port pairs join at the same site, and which retained fields determine the next directed witness across admissible frames?"""
from collections import defaultdict,Counter
from ramsey_37_middle_support_recovery import pairs,E,D
import json
pred={k:defaultdict(set) for k in ('port','arrival_and_port','current_link','current_link_and_port')};join=Counter();examples=[];frames=0
for pair in pairs:
    for F,G in [pair,pair[::-1]]:
        mate={next(t for t in G if not t&s):s for s in F};step={s:mate[next(t for t in G if len(t&s)==1)] for s in F};hits={}
        for s in F:
            q=s;row={}
            for d in (1,2,-2,-1):
                q=step[q];u,=s&q;v,=step[s]&step[q];z=sum(len(q&t)-len(s&t) for t in G if u in t)
                if tuple(sorted((u,v))) in E:row[('A' if d>0 else 'B')+('+' if z>0 else '-')]=(u,v)
            assert set(row)=={'A+','B-'};hits[s]=row
        for s,h in hits.items():
            frames+=1;nxt=hits[step[s]]
            for p,(u,v) in h.items():
                for t,(w,x) in nxt.items():join[p,t]+=int(v==w)
                w,x=nxt[p];assert w==v
                for k,key in [('port',p),('arrival_and_port',(v,p)),('current_link',(u,v)),('current_link_and_port',(u,v,p))]:pred[k][key].add((w,x))
                if (u,v)==(8,13):examples.append((p,x))
res={k:dict(Counter(map(len,m.values()))) for k,m in pred.items()};print(frames,join,res,sorted(set(examples)));(D/'ramsey_37_successor_join.json').write_text(json.dumps(dict(frames=frames,joins={str(k):v for k,v in join.items()},possible_next_link_counts=res,example_8_13=sorted(set(examples))),indent=2)+'\n')
