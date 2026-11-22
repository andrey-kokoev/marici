"""Decompose incidences selected by neither literal matching. Endpoints have residual degree one, so tracing from them requires no choice."""
from ramsey_exit_common_missing_endpoint import m,mate,P,T,D,json

def run():
    allflags={(P.index(d),j) for j,t in enumerate(T,15) for d in t};adj={i:set() for i in range(30)}
    for x,y in allflags-(m|mate):adj[x].add(y);adj[y].add(x)
    used=set();paths=[];rings=[]
    for x in sorted(adj,key=lambda x:(len(adj[x]),-x)):
        if x in used:continue
        path=[x];p=None;y=x
        while True:
            used.add(y);z=adj[y]-{p};
            if not z:break
            p,y=y,min(z)
            if y==x:break
            assert y not in used;path.append(y)
        (paths if len(adj[x])==1 else rings).append(path)
    assert len(used)==30;return dict(paths=paths,rings=rings)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_unused_flag_threads.json').write_text(json.dumps(out)+'\n')
