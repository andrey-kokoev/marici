"""Compute orientation transport; do not assign Clifford signs to the swaps."""
from itertools import combinations
from collections import Counter,deque
from ramsey38_novel_root8_diagonal import setup,sub,cf,pf,json,t
from ramsey38_compare_support_fillings import boundary

def replay(rr,bd):
    p=frozenset.union(*rr.values());base=min(p);cells=sorted(sub(p,4),key=sorted);bit={s:1<<i for i,s in enumerate(cells)}
    seed=sum(bit[f|{base}] for f in bd if base not in f);masks=[seed]
    # Each non-apex tet can be freely toggled along with its cone boundary;
    # the residual pure apex cone is uniquely determined by the boundary.
    for s in cells:
        if base not in s:
            delta=sum(bit[q] for q in sub(s|{base},4));masks += [x^delta for x in masks]
    forced=sum(bit[s] for s in set(rr.values()) if len(s)==4);edges=set.union(*(sub(f,2) for f in bd))
    for x in masks:
        if x&forced!=forced:continue
        ts=[s for s in cells if bit[s]&x]
        if not all(any(r<=s for s in ts) for r in rr.values()):continue
        hits=Counter(f for s in ts for f in sub(s,3));
        if any(n!=(1 if f in bd else 2) for f,n in hits.items()):continue
        for e in set.union(*(sub(s,2) for s in ts)):
            seg=[s-e for s in ts if e<=s];seen=set(seg[0]);deg=Counter(v for h in seg for v in h)
            for _ in seg:
                for h in seg:
                    if h&seen:seen.update(h)
            if seen!=set(deg) or any(d not in (1,2) for d in deg.values()) or sum(d==1 for d in deg.values())!=(2 if e in edges else 0):break
        else:yield ts

def transport(fs):
    fs=sorted(map(lambda f:tuple(sorted(f)),fs));G={f:{} for f in fs}
    for f,h in combinations(fs,2):
        if len(set(f)&set(h))!=2:continue
        def arcs(c):return {(c[i-1],v) for i,v in enumerate(c)}
        G[f][h]=G[h][f]=-1 if arcs(f)&arcs(h) else 1
    neg=None;sq={}
    for f in fs:
        q=deque([(f,1,[f])]);visited={(f,1)}
        while q:
            a,s,path=q.popleft()
            if (a,s)==(f,-1):
                if neg is None or len(path)<len(neg):neg=path
                break
            for b,w in G[a].items():
                if (b,w*s) not in visited:visited.add((b,w*s));q.append((b,w*s,path+[b]))
        for a,b in combinations(G[f],2):
            i=set(f)^set(a);j=set(f)^set(b)
            if i&j:continue
            end=tuple(sorted(set(f)^i^j))
            if end in G[a] and end in G[b]:sq[frozenset([f,a,b,end])]=G[f][a]*G[a][end]*G[end][b]*G[b][f]
    return neg,Counter(sq.values())
def carried_labels(loop):
    labels=list(loop[0]);start=labels.copy()
    for a,b in zip(loop,loop[1:]):
        old,=set(a)-set(b);new,=set(b)-set(a);labels[labels.index(old)]=new
    inv=sum(x>y for x,y in combinations(labels,2));assert (-1)**(len(loop)-1+inv)==-1
    return dict(zip(start,labels))

if __name__=='__main__':
    rr,bd=setup(5);cases=list(replay(rr,bd));assert len(cases)==4
    for ts in cases:
        loop,sq=transport({s-{19} for s in ts if 19 in s});assert loop and not sq[-1];print('failed:',len(loop)-1,loop,'returned labels',carried_labels(loop),'swap squares',sq)
    good=next(x for x in json.loads(cf.read_text())['certificates'] if x['record']==5 and x['root']==8)['actual_hidden']['24'];fs={frozenset(s)-{19} for s in good if 19 in s};neg,sq=transport(fs);assert neg is None;print('repaired:',neg,sq)
    entry=next(e for e in json.loads(pf.read_text())['entries'] if e['record']==5);g=t.graph(entry['word']);
    for root,center in [(8,19),(19,8)]:
        fs={frozenset(g[root]&n)-{center} for v,n in g.items() if v!=root and v not in g[root] and center in n and len(g[root]&n)==4};print('observed link triangles',root,center,sorted(map(sorted,fs)),transport(fs))
