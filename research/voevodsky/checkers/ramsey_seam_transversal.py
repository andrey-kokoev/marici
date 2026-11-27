"""Predict all legal single cross-edge repairs from parent cliques at a seam."""
from ramsey_forward_path_insertion import graph,check,D,combinations,Counter,sha256,json

def demands(g,gap):
    flank={gap-1,gap}&set(range(8));other=set(range(12))-flank
    for typ,k,pool in [('X',6,other),('E',5,{v for v in other if len(flank)==2 and all(not g[v]>>j&1 for j in flank)})]:
        for q in combinations(sorted(pool),k):
            if all(not g[i]>>j&1 for i,j in combinations(q,2)):yield typ,q

def run():
    rows=[s for s in combinations(range(8),3) if min(s[1]-s[0],s[2]-s[1])>=2];stats=Counter();examples={}
    for A,B in combinations(rows,2):
        if set(A)&set(B):continue
        for m in range(1,4):
            ss=[A]*m+[B]*(4-m);color=1<<list(combinations(range(4),2)).index((0,m));g=graph(8,ss,0);edge={8,8+m}
            if not all(check(graph(8,ss,c),4095,3,7) for c in (0,color)):continue
            for gap in range(9):
                qs=list(demands(g,gap));common=set.intersection(set(range(8,12)),*(set(q) for _,q in qs));pred=edge<=common;new=[tuple(v+(v>=gap) for v in s) for s in ss];assert check(graph(9,new,color),8191,3,7)==pred and check(graph(9,new,0),8191,3,7)==(not qs);stats['checked']+=1;stats['repairs' if qs and pred else 'already_legal' if pred else 'still_blocked']+=1
                if (A,B,m)==((0,2,4),(1,3,6),2) and gap in [1,4]:
                    psets={frozenset(v-7 for v in q if v>=8) for _,q in qs};examples[gap]=dict(counts=dict(Counter(t for t,q in qs)),common_ports=sorted(v-7 for v in common),minimal_port_sets=sorted(sorted(s) for s in psets if not any(r<s for r in psets)),surviving_examples={t:dict(sites=[v+1 for v in q if v<8],ports=[v-7 for v in q if v>=8]) for t,q in qs if not edge<=set(q)})
    print(stats,examples);data=dict(protocol_sha=sha256((D.parent/'ramsey_seam_transversal_protocol.md').read_bytes()).hexdigest(),counts=stats,examples=examples);p=D.parent/'ramsey_seam_transversal.json';s=json.dumps(data,indent=2)+'\n';assert not p.exists() or p.read_text()==s;p.write_text(s)
if __name__=='__main__':run()
