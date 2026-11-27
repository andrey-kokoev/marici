"""Minimum port edit cover on the entire earlier two-support census."""
from ramsey_seam_transversal import demands,graph,check,D,combinations,Counter,sha256,json

def run():
    rows=[s for s in combinations(range(8),3) if min(s[1]-s[0],s[2]-s[1])>=2];ordered=list(combinations(range(4),2));hist=Counter();blocked=Counter();ex={};trials=0;struct=Counter()
    for A,B in combinations(rows,2):
        if set(A)&set(B):continue
        for m in range(1,4):
            ss=[A]*m+[B]*(4-m);g=graph(8,ss,0);edges=[(i,j) for i in range(m) for j in range(m,4)];sets=[(es,sum(1<<ordered.index(e) for e in es)) for n in range(len(edges)+1) for es in combinations(edges,n)]
            if not check(g,4095,3,7):continue
            for es,c in sets:assert check(graph(8,ss,c),4095,3,7)
            for gap in range(9):
                qs=list(demands(g,gap));needs=[{(i,j) for i,j in edges if i+8 in q and j+8 in q} for _,q in qs];new=[tuple(v+(v>=gap) for v in s) for s in ss];best=None
                for es,c in sets:
                    pred=all(s.intersection(es) for s in needs);assert bool(pred)==check(graph(9,new,c),8191,3,7);trials+=1
                    if pred and best is None:best=es
                key='impossible' if best is None else str(len(best));hist[key]+=1;assert (best is None)==any(not s for s in needs)
                if not all(edges[0] in s for s in needs):blocked[key]+=1
                if best is None:
                    causes={t for (t,_),s in zip(qs,needs) if not s};struct['+'.join(sorted(causes))]+=1
                ex.setdefault(key,dict(A=A,B=B,m=m,gap=gap,edit=best,demands=len(qs)))
    assert sum(hist.values())==720 and sum(blocked.values())==344
    data=dict(protocol_sha=sha256((D.parent/'ramsey_port_edit_cover_protocol.md').read_bytes()).hexdigest(),all_minimum=hist,previously_blocked=blocked,irreparable_causes=struct,child_checks=trials,examples_zero_based=ex);print(data);dest=D.parent/'ramsey_port_edit_cover.json';s=json.dumps(data,indent=2)+'\n';assert not dest.exists() or dest.read_text()==s;dest.write_text(s)
if __name__=='__main__':run()
