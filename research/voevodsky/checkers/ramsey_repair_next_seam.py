from ramsey_five_port_multi import graph,check,sevens,D,combinations,sha256,json
from collections import deque,Counter

def grow(ss,k):return tuple(tuple(x+(x>=k) for x in s) for s in ss)
def run():
    src=D.parent/'ramsey_port_repair_orbits.json';data=json.loads(src.read_text());ss=grow(tuple(tuple(x-1 for x in s) for s in data['supports']),data['gap']);pairs=list(combinations(range(5),2));cols=[sum(1<<pairs.index((i-1,j-1)) for i,j in v['edits']) for v in data['representatives']];assert len(cols)==2
    queue=deque([(9,ss,())]);first=None;counts=Counter();initial=[];diffs=[]
    while queue:
        n,S,h=queue.popleft()
        if first is not None and len(h)+1>first:break
        assert n<13 and all(check(graph(n,S,c),(1<<(n+5))-1,3,7) for c in cols);counts[n]+=1
        for k in range(n+1):
            T=grow(S,k);gs=[graph(n+1,T,c) for c in cols];ok=[check(g,(1<<(n+6))-1,3,7) for g in gs];
            if not h:initial.append(ok)
            if all(ok):queue.append((n+1,T,h+(k,)))
            if ok[0]==ok[1]:continue
            first=len(h)+1;q=next(sevens(gs[ok.index(False)]));sites=[x+1 for x in q if x<=n];ports=[x-n for x in q if x>n];oldsites=[x-int(x>k+1) for x in sites if x!=k+1];diffs.append(dict(history=h+(k,),legal=ok,new_site_in_clique=k+1 in sites,old_sites=oldsites,ports=ports))
    out=dict(protocol_sha=sha256((D.parent/'ramsey_repair_next_seam_protocol.md').read_bytes()).hexdigest(),source_sha=sha256(src.read_bytes()).hexdigest(),initial=initial,first_distinguishing_length=first,legal_prefixes_checked=counts,differences=diffs);print(out);r=D.parent/'ramsey_repair_next_seam.json';s=json.dumps(out,indent=2)+'\n';assert not r.exists() or r.read_text()==s;r.write_text(s)
if __name__=='__main__':run()
