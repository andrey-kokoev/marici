from itertools import combinations
from collections import Counter,defaultdict
from ramsey_history_threshold import D,json,save,sha256,profile,graph,grow,verdict


def run():
    charts=json.loads((D.parent/'ramsey_double_flank_contact.json').read_text())['charts'];families=sorted({tuple(map(tuple,c['rows'])) for z in charts for c in z['cases'] if c['gap'] in (z['first'],z['first']+1)})
    base=[profile(b) for b in range(256)];classes=defaultdict(list);pairs=list(combinations(range(5),2));ex=None;priority=None
    for ss in families:
        rows=[sum(1<<(i-1) for i in s) for s in ss];edges=[(i,j) for i,j in pairs if not rows[i]&rows[j]]
        for red in ([],edges[:1],edges[1:],edges):
            profiles={}
            for p in range(32):
                if any((p>>a)&(p>>b)&1 for a,b in red):continue
                u=0
                for i,m in enumerate(rows):
                    if p>>i&1:u|=m
                profiles.setdefault(bytes(x+2*p.bit_count() for x in base[u]),p)
            raw=bytes(map(max,zip(*profiles)))
            if raw[0]>=14:continue
            keep=[v for v in profiles if not any(w!=v and w[0]>=v[0] and all(a<=b for a,b in zip(v,w)) for w in profiles)];key=bytes(max(s.bit_count(),14-x) for s,x in enumerate(raw));hits={sum(1<<i for i,v in enumerate(keep) if v[s]+d>=14) for s,d in enumerate(key)};m=min((m for m in range(1,1<<len(keep)) if all(m&h for h in hits)),key=int.bit_count);reps={v:profiles[v] for i,v in enumerate(keep) if m>>i&1};col=sum(1<<pairs.index(e) for e in red);rr=[tuple(i-1 for i in row) for row in ss];deg=sorted(x.bit_count() for x in graph(8,rr,col));item=dict(rows=ss,red=[(a+1,b+1) for a,b in red],groups=[[i+1 for i in range(5) if p>>i&1] for p in reps.values()],degrees=deg)
            for prev,prevraw,prevreps in classes[key]:
                rank=(deg!=prev['degrees'],raw!=prevraw,set(reps)!=prevreps,item['groups']!=prev['groups'],ss!=prev['rows'])
                if priority is not None and rank<=priority:continue
                priority=rank;ex=dict(first=prev,second=item)
                if raw!=prevraw:
                    s=min((s for s in range(512) if raw[s]!=prevraw[s]),key=int.bit_count);h=[i for i in range(9) if s>>i&1];sizes=[(x[s]+len(h))//2 for x in (prevraw,raw)]
                    for src,size in zip((prev,item),sizes):
                        t=[tuple(i-1 for i in row) for row in src['rows']];c=sum(1<<pairs.index((a-1,b-1)) for a,b in src['red'])
                        for g in reversed(h):t=grow(t,g)
                        G=graph(8+len(h),t,c);assert verdict(G)==(size<7);assert any(all(not(G[a]>>b&1) for a,b in combinations(q,2)) for q in combinations(range(len(G)),size)) and not any(all(not(G[a]>>b&1) for a,b in combinations(q,2)) for q in combinations(range(len(G)),size+1))
                    ex.update(gaps=h,sizes=sizes)
            classes[key].append((item,raw,set(reps)))
    groups=list(classes.values());out=dict(sources=sum(map(len,groups)),classes=len(groups),class_sizes=dict(Counter(map(len,groups))),cross_row=sum(len({v['rows'] for v,r,p in g})>1 for g in groups),same_rows_different_colors=sum(len({v['rows'] for v,r,p in g})<len(g) for g in groups),different_scores=sum(len({r for v,r,p in g})>1 for g in groups),different_min_profiles=sum(len({frozenset(p) for v,r,p in g})>1 for g in groups),example=ex,protocol_sha=sha256((D.parent/'ramsey_history_language_protocol.md').read_bytes()).hexdigest());assert out['sources']==154;print(out);save(D.parent/'ramsey_history_language.json',out)

if __name__=='__main__':run()
