"""All perfect matchings against their literal images, without residual-fill or strip-length assumptions. Count active components exchanged as sets, separately for exactly the marked fixed poles, any two fixed poles, and all cases."""
from collections import Counter
from ramsey_history_matching_provenance import enum,D,json
from ramsey_row_quotient_constructor import R,move

def run():
    fixed={i for i,v in enumerate(R) if i==v};out=[]
    for m in enum():
        n=move(m,R);adj={}
        for x,y in m^n:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
        left=set(adj);cs=[]
        while left:
            x=min(left);w=[x];y=min(adj[x]);
            while y!=x:w.append(y);y,=adj[y]-{w[-2]}
            left-=set(w);cs.append(w)
        perm=[next(j for j,c in enumerate(cs) if R[w[0]] in c) for w in cs];poles=sorted(fixed&adj.keys());assert all((perm[i]==i)==(len(set(w)&fixed)==2) for i,w in enumerate(cs));out.append(dict(poles=poles,components=cs,action=perm,matching=sorted(m)))
    summary={};
    for key,rows in [('marked',[r for r in out if r['poles']==[0,29]]),('two',[r for r in out if len(r['poles'])==2]),('all',out)]:
        c=Counter((tuple(sorted(map(len,r['components']))),any(i!=v for i,v in enumerate(r['action']))) for r in rows);summary[key]=[dict(sizes=k,exchanged=b,count=n) for (k,b),n in sorted(c.items())]
    target={0,16,13,19,7,29,4,27,12,17};marked=[]
    for r in out:
        m=frozenset(r['matching']);n=move(m,R)
        if len(r['components'])==3 and any(set(w)==target for w in r['components']) and {(0,16),(7,29)}<=m:marked.append(dict(common=sorted(m&n),**r))
    return dict(fixed=sorted(fixed),summary=summary,marked_counterexamples=marked,swapped_examples=[r for r in out if any(i!=v for i,v in enumerate(r['action']))][:2])
if __name__=='__main__':
    out=run();print(out['summary']);(D/'ramsey_polefree_component_exchange.json').write_text(json.dumps(out)+'\n')
