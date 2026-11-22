"""Inverse census: deletion D leaves alpha<=5 iff D hits every independent six-set of target. Bitset filter over 26334 five-sets; identify residual by exact induced isomorphism, classify D modulo S5."""
from ramsey_square_level_transfer import graph,D,json,inds,bits,combinations,Counter
from ramsey_common_partner_pattern import embedding
from itertools import permutations
from functools import lru_cache

def induced(G,V):return [sum(1<<j for j,y in enumerate(V) if G[x]>>y&1) for x in V]
@lru_cache(None)
def canon(m):
    E=list(combinations(range(5),2));return min(sum(1<<b for b,(i,j) in enumerate(E) if m>>E.index(tuple(sorted((p[i],p[j]))))&1) for p in permutations(range(5)))
def run():
    read=lambda k,n:[graph(l) for l in (D/f'pauli-realization-catalogues/r3{k}_{n}.g6').read_bytes().splitlines()];cores=read(6,17);sig=lambda H:sorted(map(int.bit_count,H));lookup=lambda H:next(i+1 for i,g in enumerate(cores) if sig(g)==sig(H) and embedding(H,g));old=[sum(1<<((i+d)%13) for d in (1,-1,5,-5)) for i in range(13)]+[0]*4
    for i,S in enumerate(((1,7,11),(3,5,9),(2,6,12),(4,8,10))):
        for x in S:old[x]|=1<<(13+i);old[13+i]|=1<<x
        old[13+i]|=1<<(13+(i+1)%4)|1<<(13+(i-1)%4)
    arch=lookup(old);sets=[sum(1<<v for v in u) for u in combinations(range(22),5)];cols=[sum(1<<i for i,s in enumerate(sets) if s>>v&1) for v in range(22)];out=[]
    for rec,G in enumerate(read(7,22),1):
        live=(1<<len(sets))-1
        for t in inds(G):
            if t.bit_count()!=6:continue
            hit=0
            for v in bits(t):hit|=cols[v]
            live&=hit
            if not live:break
        for i in bits(live):
            d=sets[i];V=list(bits(d));H=induced(G,[v for v in range(22) if not d>>v&1]);f=canon(sum(1<<b for b,(x,y) in enumerate(combinations(V,2)) if G[x]>>y&1));out.append(dict(target=rec,core=lookup(H),deleted=d,motif=f))
    return dict(archived=arch,rows=out)
if __name__=='__main__':
    z=run();print(z['archived'],len(z['rows']),len({r['target'] for r in z['rows']}));
    for c in range(1,8):
        rs=[r for r in z['rows'] if r['core']==c];print(c,len({r['target'] for r in rs}),Counter(r['motif'] for r in rs));
    (D/'ramsey_inverse_five_motifs.json').write_text(json.dumps(z)+'\n')
