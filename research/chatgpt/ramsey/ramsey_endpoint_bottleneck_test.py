"""Exact endpoint-only test: maximize each independent support WITHOUT changing its membership at either endpoint. This avoids incorrectly ruling out nonmaximal supports that conserve endpoint slots."""
from ramsey_degree_capacity_audit import inds,bits,induce,graph,D,json,Counter
from ramsey_ports_saturated_core import four

def screen(B,u,v):
    I=inds(B);F=(1<<u)|(1<<v);M=sorted((s for s in I if all((s|F)>>i&1 or s&r for i,r in enumerate(B))),key=lambda s:(s&F!=F,s));T=[t for t in I if t.bit_count()==8];hits=[sum(1<<j for j,t in enumerate(T) if t>>i&1) for i in range(len(B))];miss=[]
    for s in M:
        h=0
        for i in bits(s):h|=hits[i]
        miss.append(((1<<len(T))-1)^h)
    mem=[sum(1<<i for i,s in enumerate(M) if s>>x&1) for x in (u,v)];lim=[9-B[x].bit_count() for x in (u,v)];adj=[sum(1<<j for j in range(i,len(M)) if not miss[i]&miss[j]) for i in range(len(M))];
    def visit(q,opts,room):
        if len(q)==4:return [M[i] for i in q]
        for k in range(2):
            if not room[k]:opts&=~mem[k]
        for i in bits(opts):
            r=visit(q+[i],opts&adj[i],[room[k]-(mem[k]>>i&1) for k in range(2)])
            if r:return r
    for i,s in enumerate(M):
        if s&F!=F:break
        q=visit([i],adj[i],[k-1 for k in lim]);
        if q:return q

def run():
    base=induce(graph((1,7,11,16)),list(range(1,35)));out=[]
    for p in json.loads((D/'ramsey_deletion_rank_new_parents.json').read_text()):
        A=base[:]
        for x,y in p['added']:A[x]|=1<<y;A[y]|=1<<x
        original=bool(four(A)['supports']);
        for r in p['rows']:
            u,v=r['edge'];B=A[:];B[u]^=1<<v;B[v]^=1<<u;S=screen(B,u,v);over={} if not S else {i:y for i,b in enumerate(B) if (y:=b.bit_count()+sum(s>>i&1 for s in S))>9};out.append(dict(parent=len(p['added']),parent_extendible=original,edge=[u,v],pass_endpoint=bool(S),actual=r['valid'],supports=S,overloaded=over))
    return out
if __name__=='__main__':
    out=run();print(Counter((r['parent_extendible'],r['pass_endpoint'],r['actual']) for r in out));print(next((r for r in out if r['pass_endpoint'] and not r['actual']),None));(D/'ramsey_endpoint_bottleneck_test.json').write_text(json.dumps(out)+'\n')
