"""Nonprivate square: copy each donor's neighbourhood except neighbours conflicting with a named endpoint. Try filling uncoloured vertices without changing a private colour. Compare against exact optimum on exceptional seeds."""
from ramsey_neighbourhood_square import D,json,decode,inds,bits,permutations,combinations,Counter,verify,grow
from ramsey_rooted_square_propagation import test
from itertools import product

def run():
    cases=json.loads((D/'ramsey_neighbourhood_square.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for row in cases:
        if not row['good'] or row['private']:continue
        p,W=row['record'],row['seed'];H=decode(lines[p-1]);I=inds(H);T=[t for t in I if t.bit_count()>=4];a=next(bits(W));b=next(bits(W&H[a]));c,d=bits(W^(1<<a|1<<b));ends=list(product((a,b),(c,d)));un=[v for v,h in enumerate(H) if not (h|1<<v)&W];dbl=[v for v,h in enumerate(H) if (h&W).bit_count()==2];raw=[]
        def fails(S):return [t for t in T if t.bit_count()+sum(not t&s for s in S)>=8]
        for rot in permutations((a,b,c,d)):
            if any(v in e for v,e in zip(rot,ends)):continue
            base=[1<<i|1<<j|(H[v]&~(W|H[i]|H[j])) for v,(i,j) in zip(rot,ends)];assert all(all(not H[v]&s for v in bits(s)) for s in base);bad=fails(base);assert all(t.bit_count()==6 and (t&W).bit_count()==1 and (t&(1<<dbl[0])) for t in bad);extensions=[]
            for f in product(range(5),repeat=len(un)):
                S=base[:]
                for v,k in zip(un,f):
                    if k<4:S[k]|=1<<v
                if any(s&H[v] for s in S for v in bits(s)):continue
                if not fails(S):extensions.append(S);verify(grow(H,S),8)
            raw.append(dict(donors=rot,base=base,bad=bad,extensions=extensions))
        # All completions from rooted solver, retaining the exact prescribed overlap.
        ts=[[t for t in I if t.bit_count()==k] for k in (4,5,6)];miss={s:[sum(1<<i for i,t in enumerate(u) if not s&t) for u in ts] for s in I};sol=[]
        def audit(dom,L,E):
            for v in product(*(list(bits(l)) for l in L)):
                if all(E[i,j][v[i]]>>v[j]&1 for i,j in combinations(range(4),2)):
                    S=[dom[i][x] for i,x in enumerate(v)]
                    if not fails(S):sol.append(S)
        test(H,I,miss,W,audit);assert sol
        for z in raw:
            z['best_drops'],z['best_add'],z['nearest']=min((sum((s&~t).bit_count() for s,t in zip(z['base'],S)),sum((t&~s).bit_count() for s,t in zip(z['base'],S)),S) for S in sol)
        out.append(dict(record=p,seed=W,free=un,double=dbl,legal=len(sol),orientations=raw));print(p,W,un,dbl,len(sol),[(len(z['bad']),len(z['extensions']),z['best_drops'],z['best_add']) for z in raw])
    return out
if __name__=='__main__':(D/'ramsey_collision_square.json').write_text(json.dumps(run())+'\n')
