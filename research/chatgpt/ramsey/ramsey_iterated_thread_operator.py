"""Recompute every thread and every local reversal solely from the current ordered pair. End flags are forced common; orient each thread from its partition endpoint."""
from ramsey_row_quotient_constructor import P,T,action,final,R,move
from ramsey_folded_entry_handoff import D,json
flags={(P.index(d),j) for j,t in enumerate(T,15) for d in t}
def step(a,b):
    adj={x:set() for x in range(30)}
    for x,y in flags-(a|b):adj[x].add(y);adj[y].add(x)
    common=set();outputs=[set(),set()];flag=lambda x,y:tuple(sorted((x,y)))
    for j in range(15,30):
        if len(adj[j])!=1:continue
        x,=adj[j];k,=adj[x]-{j};i,=adj[k]-{x};assert adj[i]=={k};common.update([flag(j,x),flag(i,k)])
        for s,out in zip((a,b),outputs):
            d,=[u for u,v in s if v==j];p=list(range(6))
            for block in T[j-15]:
                if block!=P[d]:u,v=block;p[u],p[v]=v,u
            g=action(p);out.add(flag(g[i],g[k]))
    pair=tuple(frozenset(common|s) for s in outputs);assert all(len(s)==len(dict(s))==len({v for u,v in s})==15 and s<=flags for s in pair);return pair

def run():
    m,=final;n=move(m,R);p=(m,n);seen=[];rows=[]
    while p not in seen:
        seen.append(p);rows.append(dict(exit=[next(d for d,j in s if j==29) for s in p],at26=[next(d for d,j in s if j==26) for s in p],overlap_with_initial=[[len(s&t) for t in (m,n)] for s in p]));assert step(*p[::-1])==step(*p)[::-1];p=step(*p)
    assert seen[2]==(n,m) and seen[3]==seen[1][::-1] and p==seen[0];return dict(repeat=seen.index(p),period=len(seen)-seen.index(p),states=rows)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_iterated_thread_operator.json').write_text(json.dumps(out)+'\n')
