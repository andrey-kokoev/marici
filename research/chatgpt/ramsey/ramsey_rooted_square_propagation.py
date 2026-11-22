"""Square-rooted support domains, not SAT. Binary constraints enforce independence, exact shared seed, and six-set diversity. Arc consistency then path consistency; enumerate residual completions and test 5/4-set rows."""
from ramsey_capacity_transfer_78 import D,json,decode,inds,bits,combinations,verify,grow,Counter
from itertools import product

def test(H,I,miss,W,on_residual=None):
    a=next(bits(W));b=next(bits(H[a]&W));c,d=bits(W^(1<<a|1<<b));seed=[(1<<i|1<<j) for i,j in product((a,b),(c,d))];dom=[[s for s in I if s&W==t] for t in seed];full=[(1<<len(S))-1 for S in dom];live=full.copy();edge={(i,j):[sum(1<<y for y,t in enumerate(dom[j]) if not (s&t&~W or miss[s][2]&miss[t][2])) for s in dom[i]] for i in range(4) for j in range(4) if i!=j};steps=[]
    def arc():
        while all(live):
            new=[sum(1<<x for x in bits(live[i]) if all(edge[i,j][x]&live[j] for j in range(4) if j!=i)) for i in range(4)]
            if new==live:break
            live[:]=new
    arc();ac=all(live);acsize=[s.bit_count() for s in live]
    while all(live):
        change=False
        for i,j in combinations(range(4),2):
            for x in bits(live[i]):
                for y in bits(edge[i,j][x]&live[j]):
                    if any(not(edge[i,k][x]&edge[j,k][y]&live[k]) for k in range(4) if k not in (i,j)):
                        edge[i,j][x]^=1<<y;edge[j,i][y]^=1<<x;change=True
        if not change:break
        arc()
    if all(live) and on_residual is not None:on_residual(dom,live,edge)
    sols=[];c6=0;edge6=set();edgeok=set();remaining=sum((edge[i,j][x]&live[j]).bit_count() for i,j in combinations(range(4),2) for x in bits(live[i])) if all(live) else 0
    for a in bits(live[0]):
        for b in bits(edge[0,1][a]&live[1]):
            for c in bits(edge[0,2][a]&edge[1,2][b]&live[2]):
                for d in bits(edge[0,3][a]&edge[1,3][b]&edge[2,3][c]&live[3]):
                    vs=(a,b,c,d);es={(i,j,vs[i],vs[j]) for i,j in combinations(range(4),2)};edge6.update(es);S=[dom[i][v] for i,v in enumerate(vs)];c6+=1;p,q,r,s=[miss[t] for t in S];
                    if any(x[1]&y[1]&z[1] for x,y,z in combinations((p,q,r,s),3)) or p[0]&q[0]&r[0]&s[0]:continue
                    sols.append(S);edgeok.update(es)
    if sols:verify(grow(H,sols[0]),8)
    return dict(seed=W,initial=[s.bit_count() for s in full],ac=ac,acsize=acsize,pc=all(live),pcsize=[s.bit_count() for s in live],remaining_pairs=remaining,pairs_with_six=len(edge6),pairs_with_completion=len(edgeok),six=c6,legal=len(sols),example=next(iter(sols),None))

def run():
    ref={r['record']:set(r['sets']) for r in json.loads((D/'ramsey_overlap_shapes.json').read_text())};out=[]
    for idx,line in enumerate((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines(),1):
        H=decode(line)
        if min(h.bit_count() for h in H)!=5:continue
        cand=(sum(1<<i for i in v) for v in combinations([i for i,h in enumerate(H) if h.bit_count()==5],4));cand=[w for w in cand if all((H[i]&w).bit_count()==1 for i in bits(w))];
        if not cand:continue
        I=inds(H);T=[[t for t in I if t.bit_count()==k] for k in (4,5,6)];miss={s:[sum(1<<j for j,t in enumerate(ts) if not s&t) for ts in T] for s in I}
        for w in cand:
            r=test(H,I,miss,w);assert bool(r['legal'])==(w in ref.get(idx,set()));out.append(dict(record=idx,**r))
    return out
if __name__=='__main__':
    z=run();print([sum(bool(r[k]) for r in z) for k in ('ac','pc','six','legal')],sum(r['six'] for r in z),sum(r['legal'] for r in z));print(Counter(tuple(sorted(r['pcsize'])) for r in z if r['legal']).most_common(15));(D/'ramsey_rooted_square_propagation.json').write_text(json.dumps(z)+'\n')
