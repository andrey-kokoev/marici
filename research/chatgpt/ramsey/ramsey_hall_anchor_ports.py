"""Prospective regular (3,k) full-root lift. Only needs the core, k, no target incidences.
When all k-1 ports are anchored, domains are independent (k-2)-sets with their own anchor only.
"""
from itertools import combinations
from functools import lru_cache
from ramsey_port_deletion_chain import D,json,independent,Counter

def anchor_lift(H,k):
    d=k-1;n=len(H);F=(1<<n)-1;deg=[m.bit_count() for m in H];anchors=[i for i in range(n) if deg[i]==d-1];active=sum(1<<i for i in anchors)
    if len(anchors)!=d or sum(d-x for x in deg)!=d*(d-1):return None # restricted full-anchor regular search only
    I=[0]
    for i,r in enumerate(H):I += [x|1<<i for x in I if not x&r]
    top=[s for s in I if s.bit_count()==d-1];flags=[sum(1<<i for i,s in enumerate(top) if s>>v&1) for v in range(n)];M=[];miss=[];domains=[]
    for v in anchors:
        row=0
        for s in top:
            if s&active!=1<<v:continue
            h=0
            for j in range(n):
                if s>>j&1:h|=flags[j]
            row|=1<<len(M);M.append(s);miss.append(((1<<len(top))-1)^h)
        domains.append(row)
    adj=[sum(1<<j for j in range(len(M)) if not x&miss[j]) for x in miss];contains=[sum(1<<j for j,s in enumerate(M) if s>>v&1) for v in range(n)];visits=0
    def dfs(rows,cap,G,selected):
        nonlocal visits
        visits+=1
        if not rows:return selected,G
        for v,c in enumerate(cap):
            if c<0:return
            f=contains[v];possible=sum(bool(r&f) for r in rows);forced=sum(not(r&~f) for r in rows)
            if not forced<=c<=possible:return
            if possible==c:rows=[r&f if r&f else r for r in rows]
            if forced==c:rows=[r&~f if r&~f else r for r in rows]
        j=min(range(len(rows)),key=lambda j:rows[j].bit_count());q=rows[j];other=rows[:j]+rows[j+1:]
        while q:
            b=q&-q;q-=b;i=b.bit_length()-1;s=M[i];nxt=[r&adj[i] for r in other]
            if not all(nxt) or independent(G,((1<<len(G))-1)^s,k-1):continue
            ans=dfs(nxt,[c-(s>>j&1) for j,c in enumerate(cap)],[r|((s>>j&1)<<len(G)) for j,r in enumerate(G)]+[s],selected+[s])
            if ans:return ans
    ans=dfs(domains,[d-x for x in deg],H,[]);result={'anchors':anchors,'domain_sizes':[r.bit_count() for r in domains],'search_nodes':visits}
    if ans:
        selected,G=ans;A=[r|((v>=n)<<len(G)) for v,r in enumerate(G)]+[((1<<d)-1)<<n];assert all(r.bit_count()==d for r in A) and all(not A[i]&A[j] for i,j in combinations(range(len(A)),2) if A[i]>>j&1) and not independent(A,(1<<len(A))-1,k);result.update(graph=A,supports=selected)
    return result
if __name__=='__main__':
    H=json.loads((D/'ramsey_slack_ladder_certificates.json').read_text())[1]['graph'];res=anchor_lift(H,9);print(res);(D/'ramsey_hall_anchor_ports.json').write_text(json.dumps(res)+'\n')
