"""Strip leftover edges, preserving a fixed three-port extension. Required-edge hitting sets from deficient subsets give exact certificate sizes; compare with matching-alone and ordinary Hall on each independent transversal of a matched reservoir."""
from ramsey_inverse_five_motifs import D,json,graph,bits,combinations,Counter,inds

def audit(H,S,R):
    E=[1<<a|1<<b for a,b in combinations(bits(R),2) if H[a]>>b&1];J=R;demands={};outside=[t for t in inds(H) if not t&R]
    while J:
        N=0
        for v in bits(J):N|=H[v]
        lower=J.bit_count()>4;bad=[i for i,s in enumerate(S) if (s&N).bit_count()<J.bit_count()];
        # Edge deletion can increase old alpha: check zero- and one-port obstructions too.
        extra=next((t for t in outside if not t&N and t.bit_count()+J.bit_count()+sum(not t&s for s in S)>=8),None)
        if extra is not None:
            clause=sum(1<<i for i,e in enumerate(E) if e&J==e);assert clause;demands.setdefault(clause,[]).append(dict(J=J,lower=lower,bad=bad,outside=extra))
        J=(J-1)&R
    small=[c for c in demands if not any(d!=c and d&~c==0 for d in demands)];valid=[s for s in range(1<<len(E)) if all(c&s for c in small)];k=min(s.bit_count() for s in valid);best=[s for s in valid if s.bit_count()==k];ms=[sum(1<<i for i in p) for p in combinations(range(len(E)),3) if (E[p[0]]|E[p[1]]|E[p[2]]).bit_count()==6];return dict(R=R,S=S,edges=E,min_edges=k,kernels=best,matchings=len(ms),sufficient_matchings=sum(m in valid for m in ms),forced_edges=[E[i] for i in range(len(E)) if 1<<i in small],private_witnesses={E[i]:demands[1<<i][0] for i in range(len(E)) if 1<<i in small},min_clauses=small)
if __name__=='__main__':
    z=json.loads((D/'ramsey_uncovered_five.json').read_text());ls=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out={i:[audit(graph(ls[int(i)-1]),r['S'],r['leftover']) for r in rows if not r['bad']] for i,rows in z.items()};rs=sum(out.values(),[]);print(Counter((len(r['edges']),r['min_edges'],len(r['forced_edges'])) for r in rs));print(sum(r['sufficient_matchings'] for r in rs),sum(r['matchings'] for r in rs));(D/'ramsey_residual_edge_certificate.json').write_text(json.dumps(out)+'\n')
