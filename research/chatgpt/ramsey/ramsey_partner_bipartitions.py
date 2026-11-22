"""Are triangle-free rooted compatibility graphs bipartite? Can two original rows certify failure directly? Each partner's demand list is its missed six-sets plus its missed five-sets also missed by the root. Link edges mean disjoint lists."""
from collections import deque
from ramsey_first_link_obstructions import run,bits,D,json,Counter

def audit():
    out=[]
    def visit(r,A,M,link,T):
        side={};par={};cycle=None
        for root in link:
            if root in side:continue
            side[root]=0;par[root]=None;queue=deque([root])
            while queue and cycle is None:
                x=queue.popleft()
                for y in bits(link[x]):
                    if y not in side:side[y]=side[x]^1;par[y]=x;queue.append(y)
                    elif side[y]==side[x]:
                        def path(v):
                            arr=[]
                            while v is not None:arr.append(v);v=par[v]
                            return arr
                        p,q=path(x),path(y);u=next(i for i in p if i in q);cycle=p[:p.index(u)+1]+q[:q.index(u)][::-1];break
            if cycle:break
        V=list(link);allv=(1<<len(V))-1;rows=T[6]+[t for t in T[5] if not A&t];cover={sum(1<<i for i,b in enumerate(V) if not t&M[b]):t for t in rows};cert=None
        if not cycle:
            # A cover must contain a row missed by the first partner. The second must cover all remaining partners.
            for s,t in cover.items():
                if not s&1:continue
                rem=allv^s;u=next((row for h,row in cover.items() if rem&~h==0),None)
                if u is not None:cert=[t,u];break
        if cycle:assert len(cycle)%2 and all(link[v]>>cycle[i-1]&1 for i,v in enumerate(cycle))
        else:assert all(side[x]!=side[y] for x in V for y in bits(link[x]))
        out.append(dict(parent=r['parent'],deleted=r['deleted'],first=A,vertices=len(V),two_rows=cert,odd_cycle=[M[x] for x in cycle] if cycle else None))
    run(on_triangle_free=visit);return out
if __name__=='__main__':
    z=audit();print(Counter('odd' if r['odd_cycle'] else 'rows' if r['two_rows'] else 'bipartite' for r in z));print(Counter(len(r['odd_cycle'] or []) for r in z));print(next((r for r in z if r['two_rows']),None));print(next((r for r in z if r['odd_cycle']),None));(D/'ramsey_partner_bipartitions.json').write_text(json.dumps(z)+'\n')
