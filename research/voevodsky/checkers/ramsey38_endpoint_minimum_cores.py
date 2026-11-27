"""Minimum-cardinality incompatible first-stage predicates over shellable proper submeshes."""
from itertools import combinations,permutations
from functools import lru_cache
from collections import Counter
from ramsey38_marked_failure_funnel import p,P
from ramsey38_boundary_ball_index import candidates,index,build,cells
from ramsey38_shell_lookup_trial import bits

def run():
    src=p.prev.out/'ramsey38_marked_failure_funnel.json';roots=[e for e in p.json.loads(src.read_text())['details'] if e['category']=='no strict containment'];ids={e['record'] for e in roots};words={}
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i==max(ids):break
    atlas=build();idx=index(atlas);cellmask=[sum(1<<j for j in t) for t in cells];faces=[sum(1<<j for j in f) for f in combinations(range(7),3)];car={f:sum(1<<i for i,t in enumerate(cellmask) if f&t==f) for f in range(128)};closure={t:sum(1<<f for f in range(128) if f&t==f) for t in faces+cellmask}
    @lru_cache(None)
    def features(m):
        bd=occ=0
        for f in faces:
            if (m&car[f]).bit_count()==1:bd|=closure[f]
        for i,t in enumerate(cellmask):
            if m>>i&1:occ|=closure[t]
        return bd,occ
    @lru_cache(None)
    def subballs(B):
        out=[];m=(B-1)&B
        while m:
            if m in atlas:out.append(features(m))
            m=(m-1)&B
        return out
    @lru_cache(None)
    def core(B,atoms):
        subs=subballs(B);univ=(1<<len(subs))-1
        def ok(a,d,o):
            k,s=a;return bool((d if k=='expose' else o if k=='carry' else o&~d)>>s&1)
        sat=[sum(1<<j for j,(d,o) in enumerate(subs) if ok(a,d,o)) for a in atoms]
        def dfs(start,remaining,live):
            if not remaining:return () if not live else None
            for i in range(start,len(atoms)-remaining+1):
                n=live&sat[i]
                if n==live:continue
                tail=dfs(i+1,remaining-1,n)
                if tail is not None:return (atoms[i],)+tail
        for k in range(1,len(atoms)+1):
            c=dfs(0,k,univ)
            if c is not None:return c
        raise AssertionError('valid first subball')
    hist=Counter();kinds=Counter();out=[]
    for e in roots:
        g=p.graph(words[e['record']]);u=e['root'];L,rows,_,dec,stage,_=p.prepare(g,u);_,rs,ms=p.setup(g,u);lookup={frozenset(L[i] for i in t):b for t,b in bits.items()}
        @lru_cache(None)
        def pool(req,bs):return {sum(lookup[t] for t in ts) for bd in bs for ts in candidates(idx,L,req,set(map(dec,bd)))}
        for a in ms:
            r,S=stage((a,));x,v=a;rr={**rs,x:rs[x]|1<<L.index(v)}
            for b in p.setup(p.add(g,a),u)[2]:
                q,T=stage(tuple(sorted((a,b))))
                for j,k in permutations(rows,2):
                    starts=pool(r,tuple(S.get(frozenset([j]),())));ends=pool(q,tuple(T.get(frozenset([j,k]),())))
                    if not starts or not ends:continue
                    atoms=tuple(sorted({('bury',rs[x])}|{('bury' if h==j else 'carry' if s.bit_count()==4 else 'expose',s) for h,s in rr.items()}));
                    for B in sorted(ends):
                        c=core(B,atoms);hist[len(c)]+=1;kinds['+'.join(sorted(t for t,_ in c))]+=1;out.append(dict(record=e['record'],root=u,moves=[a,b],goal=[j,k],labels=L,end_mask=B,core=c))
    print(len(out),hist,kinds);p.prev.save(p.prev.out/'ramsey38_endpoint_minimum_cores.json',dict(source_sha=p.prev.sha(src.read_bytes()),sizes=dict(hist),one_core_kinds=dict(kinds),examples=out))
if __name__=='__main__':run()
