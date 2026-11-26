"""Mask every edge from 8 and 19 to the other 25 vertices. Leave 8--19 red.
Generate both red supports from the visible induced graph; compare orientations only afterwards.
"""
from itertools import combinations
from collections import Counter
from ramsey38_novel_array_trial import t,prev,pf,json
entry=next(e for e in json.loads(pf.read_text())['entries'] if e['record']==5);g=t.graph(entry['word']);U,V=8,19;core=sorted(set(g)-{U,V});C=(1<<len(core))-1
adj=[sum(1<<j for j,w in enumerate(core) if w in g[v]) for v in core]
def independent(mask,chosen=0):
    yield chosen
    while mask:
        b=mask&-mask;mask-=b;yield from independent(mask&~adj[b.bit_length()-1],chosen|b)
def labels(s):return [v for i,v in enumerate(core) if s>>i&1]
def mask(vs):return sum(1<<i for i,v in enumerate(core) if v in vs)
def baseline():
    inds=list(independent(C));assert max(map(int.bit_count,inds))<=7;Q=[s for s in inds if s.bit_count()==7];supports=[s for s in inds if s.bit_count()<=6 and all(s&q for q in Q)] # plus red partner: at most 7 total red neighbors
    pairs=[(s,h) for s in supports for h in supports if s&h==0];return Q,supports,pairs
def rebuild(s,h):
    graph={v:(g[v]-{U,V}) for v in core};graph.update({U:set(labels(s))|{V},V:set(labels(h))|{U}})
    for v in (U,V):
        for w in graph[v]-{U,V}:graph[w].add(v)
    return graph

def shell_scan(graph,r,limit=1,first=False):
    # Exact first witnesses for no release and for each single hidden row, using
    # only actual red-neighbor labels. Do not give the degree-six root a spare label.
    import ramsey38_release_census as c
    from unittest.mock import patch
    labs=sorted(graph[r]);n=len(labs);m=lambda S:sum(1<<i for i,v in enumerate(labs) if v in S);rows={v:m(nb) for v,nb in graph.items() if v!=r and v not in labs};assert max(map(int.bit_count,rows.values()))<=4
    T=tuple(x for x in range(1<<n) if x.bit_count()==4);F=tuple(x for x in range(1<<n) if x.bit_count()==3);h={f:sum(1<<i for i,tet in enumerate(T) if tet&f==f) for f in F};wins={}
    with patch.multiple(c,T=T,F=F,carriers=h):
        for bd,closure in c.templates():
            if max(bd)>=1<<n:continue
            missing=tuple(v for v,s in rows.items() if s.bit_count()<4 and s not in closure)
            if len(missing)>limit or missing in wins:continue
            order=c.first_ball(bd,set(rows.values()))
            if order:
                wins[missing]=[sorted(labs[i] for i in cell) for cell in order]
                if first:return wins
    return wins

if __name__=='__main__':
    Q,ss,ps=baseline();actual=tuple(mask(g[v]) for v in (U,V));assert actual in ps;print(len(Q),len(ss),len(ps),Counter((s.bit_count(),h.bit_count()) for s,h in ps));print('actual',list(map(labels,actual)));print('unordered',[(labels(s),labels(h)) for s,h in ps if s<h][:12]);
    for s,h in ps:
        if 2 not in labels(s):continue  # name the sides; equivalently reveal only the anchor 8--2 red
        graph=rebuild(s,h);A,B=map(labels,(s,h));ij=[(a,b) for a in A for b in B if b in graph[a]];print('optional edge',25 in B,'rows and columns:',A,B,'incidences',ij)
        sides=set(A+B);edge_set={frozenset(e) for e in ij}; components=0
        while sides:
            seen={next(iter(sides))}
            for _ in range(len(A+B)):
                for e in edge_set:
                    if e&seen:seen.update(e)
            sides-=seen;components+=1
        rank=len(ij)-len(A+B)+components;print('independent cycles:',rank);assert rank==int(25 in B)
        if rank:assert all(frozenset(e) in edge_set for e in [(4,11),(11,12),(12,25),(25,26),(26,16),(16,4)])
        for r in (U,V):
            cert=shell_scan(graph,r);print('root',r,'exact hidden sets of size <=1:',sorted(cert),'example sizes:',[len(q) for q in cert.values()],flush=True)
            if not cert:print('two releases, first certificate:',shell_scan(graph,r,2,True),flush=True)
