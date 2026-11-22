"""How early can residual-edge necessity be recognized? Fix R only; range over all partitions of its complement into independent fives (without row/validity tests). A potential witness is two endpoints plus an independent subset of their common antineighbourhood. Count colour-independent versus adaptive witnesses and minimum named port information."""
from ramsey_inverse_five_motifs import D,json,graph,bits,inds,Counter,combinations

def audit(H,r):
    R=r['R'];S=r['S'];I=inds(H);F=(1<<len(H))-1;V=F^R;P={s for s in I if s.bit_count()==5 and not s&R};part=[(s,t,V^s^t) for s,t in combinations(sorted(P),2) if not s&t and V^s^t>t and V^s^t in P];assert tuple(sorted(S)) in part
    out=[]
    for e in r['edges']:
        a,b=bits(e);U=F&~(e|H[a]|H[b]);W=[j|e for j in I if j&~U==0 and j.bit_count()>=3];
        # Exactly the newly independent old sets of size at least five. Blanket criteria use no port labels.
        def defeats(w,p):return w.bit_count()+sum(not s&w for s in p)>=8
        marks=[sum(1<<i for i,p in enumerate(part) if defeats(w,p)) for w in W];allp=(1<<len(part))-1;union=0
        for m in marks:union|=m
        low=next((w for w in W if w.bit_count()+3-min(3,(w&V).bit_count())>=8),None);fixed=next((w for w,m in zip(W,marks) if m==allp),None);yes=any(defeats(w,S) for w in W);assert yes==(e in r['forced_edges']);
        atlas=[]
        if union==allp:
            from functools import lru_cache
            reps={m:w for m,w in zip(marks,W) if m};maximal=[m for m in reps if not any(m!=v and m&~v==0 for v in reps)]
            @lru_cache(None)
            def cover(left):
                if not left:return ()
                pivot=left&-left
                return min(((reps[m],)+cover(left&~m) for m in maximal if m&pivot),key=len)
            atlas=cover(allp)
        earliest=None
        if yes:
            for k in range(4):
                for known in combinations(S,k):
                    pm=sum(1<<i for i,p in enumerate(part) if all(c in p for c in known));
                    if not pm&~union:earliest=k;break
                if earliest is not None:break
        out.append(dict(e=e,alpha_without_edge=max((w.bit_count() for w in W),default=0),cheap=low,universal_witness=fixed,forced_partitions=union.bit_count(),earliest=earliest,actual=yes,atlas=atlas))
    return dict(R=R,partitions=len(part),edges=out)
if __name__=='__main__':
    z=json.loads((D/'ramsey_residual_edge_certificate.json').read_text());ls=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out={i:[audit(graph(ls[int(i)-1]),r) for r in rs] for i,rs in z.items()};rs=sum(out.values(),[]);es=sum((r['edges'] for r in rs),[]);print(len(rs),len(es),Counter(e['earliest'] for e in es),sum(e['cheap'] is not None for e in es),sum(e['universal_witness'] is not None for e in es),Counter(r['partitions'] for r in rs));(D/'ramsey_preport_edge_demands.json').write_text(json.dumps(out)+'\n')
