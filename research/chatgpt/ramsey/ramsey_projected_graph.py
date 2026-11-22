"""Replace each size-two trace of a maximum row by a colour inequality. Test obstructions of the resulting ordinary graph independently of balance; distinguish K4, other non-3-colourable, and equitable-only failures."""
from ramsey_inverse_five_motifs import D,json,graph,inds,combinations,bits,Counter

def coloring(G):
    def rec(todo,S):
        if not todo:return S
        i=max(bits(todo),key=lambda v:(sum(bool(s&G[v]) for s in S),(G[v]&todo).bit_count()));
        for k,s in enumerate(S):
            if s&G[i]:continue
            a=S.copy();a[k]|=1<<i;r=rec(todo^(1<<i),a)
            if r is not None:return r
            if not s:break
    return rec(sum(1<<i for i in G),[0]*3)

def audit(H,rs):
    I=inds(H);T=[s for s in I if s.bit_count()==6];forbid={q:sum(1<<i for i,h in enumerate(H) if not h&q and not q>>i&1) for q in I if q.bit_count()==4};forbid={q:u for q,u in forbid.items() if u.bit_count()>=4};out=[]
    for r in rs:
        if r['arity']!=2:continue
        R=r['R'];V=((1<<len(H))-1)^R;G={i:H[i]&V for i in bits(V)};extra={s&V for s in T if (s&V).bit_count()==2}
        for e in extra:a,b=bits(e);G[a]|=1<<b;G[b]|=1<<a
        clique=next(((a,b,c,d) for a in G for b in bits(G[a]) if a<b for c in bits(G[a]&G[b]) if b<c for d in bits(G[a]&G[b]&G[c]) if c<d),None);col=None if clique else coloring(G);out.append(dict(R=R,new_edges=len(extra),K4=clique,coloring=col,forbidden_four=next((q for q in forbid if q&~R==0),None)))
    return out
if __name__=='__main__':
    z=json.loads((D/'ramsey_reservoir_row_obstructions.json').read_text());ls=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out={i:audit(graph(ls[int(i)-1]),rs) for i,rs in z.items()};print(Counter('K4' if r['K4'] else 'imbalance' if r['coloring'] else 'chromatic' for rs in out.values() for r in rs));(D/'ramsey_projected_graph.json').write_text(json.dumps(out)+'\n')
