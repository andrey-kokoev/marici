"""Hold decagon, common exit thread, and polarity fixed; measure fork distances and the involution on boundary endpoints induced by tracing unused paths in each agreement phase."""
from ramsey_octagon_phase_square import final,R,move,flags,polarity,D,json

def run():
    m,=final;p=polarity()[0]['map'];r=json.loads((D/'ramsey_polefree_component_exchange.json').read_text())['marked_counterexamples'];h,k=[frozenset(map(tuple,s['matching'])) for s in r];other=m^(h^k);states=[]
    for s in [m,other]:
        n=move(s,R);assert move(s,p)==n;adj={x:set() for x in range(30)}
        for x,y in flags-(s|n):adj[x].add(y);adj[y].add(x)
        routes={}
        for x in adj:
            if len(adj[x])!=1:continue
            w=[x];prev=None
            while adj[w[-1]]-{prev}:prev,y=w[-1],next(iter(adj[w[-1]]-{prev}));w.append(y)
            routes[x]=w
        states.append(routes)
    a,b=states;out=[]
    for x,w in a.items():
        v=b[x];i=next((i for i,(u,y) in enumerate(zip(w,v)) if u!=y),None);assert w[-1]==p[x] and [p[y] for y in v]==b[p[x]];out.append(dict(start=x,selected=w,alternative=v,common_edges=None if i is None else i-1,alternate_end_polar=w[-1]==v[-1]))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_phase_path_routing.json').write_text(json.dumps(out)+'\n')
