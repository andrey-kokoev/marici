"""Group q=4 row obligations by their four spokes. Compare double completions, singleton completions, and progressively weaker consequences of sharing a four-set. Exact proper partial 3-colour SAT, with independent witnesses."""
from ramsey_root_signature_transfer import D,json,graph,bits,inds,combinations,Counter,Solver
from itertools import product

def audit(H):
    I=inds(H);n=len(H);T=[s for s in I if s.bit_count()==5 and max((s&h).bit_count() for h in H)==4];P={q:[] for q in I if q.bit_count()==4 and any(q&~h==0 for h in H)}
    for q in P:P[q]=[next(bits(t^q)) for t in T if t&q==q]
    P={q:xs for q,xs in P.items() if xs};assert all(len(xs)==1 or len(xs)==2 and H[xs[0]]>>xs[1]&1 for xs in P.values());base=[[-(1+3*i+k),-(1+3*j+k)] for i,j in combinations(range(n),2) if H[i]>>j&1 for k in range(3)]+[[-(1+3*i+k),-(1+3*i+h)] for i in range(n) for k,h in combinations(range(3),2)]
    def test(C):
        with Solver(name='g4',bootstrap_with=base+C) as sat:
            if not sat.solve():return None
            m=set(sat.get_model());return [sum(1<<i for i in range(n) if 1+3*i+k in m) for k in range(3)]
    def hit(q,colors):return [1+3*i+k for i in bits(q) for k in colors]
    D2=[];D1=[];hitall=[];nozero=[];paint=[];triples=Counter();forks=[]
    for q,xs in P.items():
        h=[hit(q,range(3))];hitall+=h
        full=[hit(q|1<<x,cs) for x in xs for cs in combinations(range(3),2)];(D2 if len(xs)==2 else D1).extend(full)
        if len(xs)==2:
            nozero+=h
            for x in xs:
                for cs in combinations(range(3),2):paint.append(hit(q,cs)+hit(1<<x,range(3)))
            forks.append([q,*xs])
    results={k:test(C) for k,C in dict(singles=D1,doubles=D2,hit_all_spokes=hitall,singles_hit_all=D1+hitall,doubles_hit_all=D2+hitall,singles_color_ends=D1+nozero+paint,full=D1+D2).items()};assert results['full'] is None
    return dict(rows=len(T),spokes=len(P),single=sum(len(x)==1 for x in P.values()),forks=forks,double_rows=len({q|1<<x for q,xs in P.items() if len(xs)==2 for x in xs}),results=results)
if __name__=='__main__':
    z=[audit(graph(l)) for l in (D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()];print([(r['spokes'],r['single'],len(r['forks']),{k:v is None for k,v in r['results'].items()}) for r in z]);(D/'ramsey_fifth_vertex_forks.json').write_text(json.dumps(z)+'\n')
