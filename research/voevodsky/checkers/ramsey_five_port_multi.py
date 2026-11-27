from itertools import combinations,combinations_with_replacement
from ramsey_forward_path_insertion import graph,check,D,sha256,json

def sevens(g):
    def visit(p,q):
        if len(q)==7:yield q;return
        while len(q)+p.bit_count()>=7:
            b=p&-p;p-=b;i=b.bit_length()-1;yield from visit(p&~g[i],q+(i,))
    yield from visit((1<<len(g))-1,())

def run():
    rows=[s for s in combinations(range(8),3) if min(s[1]-s[0],s[2]-s[1])>=2];pairs=list(combinations(range(5),2));count=0
    for idx,ss in enumerate(combinations_with_replacement(rows,5),1):
        if not check(graph(8,ss,0),8191,3,7):continue
        edges=[e for e in pairs if set(ss[e[0]]).isdisjoint(ss[e[1]])];
        if len(edges)<2:continue
        for gap in range(9):
            count+=1;t=[tuple(x+(x>=gap) for x in s) for s in ss];qs=list(sevens(graph(9,t,0)));ps={frozenset(i-9 for i in q if i>=9) for q in qs};ms=[p for p in ps if not any(r<p for r in ps)];ds=[{e for e in edges if set(e)<=p} for p in ms]
            if not ds or not all(ds) or set.intersection(*ds):continue
            sol=next((es for es in combinations(edges,2) if all(s.intersection(es) for s in ds)),None)
            if sol is None:continue
            for es in [(),*((e,) for e in edges),sol]:
                col=sum(1<<pairs.index(e) for e in es);assert check(graph(8,ss,col),8191,3,7) and check(graph(9,t,col),16383,3,7)==(len(es)==2)
            out=dict(protocol_sha=sha256((D.parent/'ramsey_five_port_multi_protocol.md').read_bytes()).hexdigest(),multisets_seen=idx,candidate_seams_checked=count,supports=[[x+1 for x in s] for s in ss],after=gap,blue_sevens=len(qs),witnesses=[dict(ports=sorted(i+1 for i in p),child_sites=[i+1 for i in next(q for q in qs if {v-9 for v in q if v>=9}==p) if i<9],eligible_edges=[(i+1,j+1) for i,j in sorted(d)]) for p,d in sorted(zip(ms,ds),key=lambda x:sorted(x[0]))],repair=[(i+1,j+1) for i,j in sol]);return out
    return dict(no_two_edge_example=True)
if __name__=='__main__':
    out=run();print(out);dest=D.parent/'ramsey_five_port_multi.json';text=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
