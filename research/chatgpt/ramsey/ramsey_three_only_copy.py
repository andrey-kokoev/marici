"""Search for a collision-corrected copy whose only failures need three ports. Deterministic maximal triangle-free stress graphs, every oriented matching considered."""
from ramsey_copy_exchange_counter import D,json,inds,bits,combinations,Counter,grow
from random import Random

def search(H):
    n=len(H);I=inds(H);alpha=max(map(int.bit_count,I));k=alpha+1;T=[[t for t in I if t.bit_count()==alpha-i] for i in range(3)];cache={}
    def miss(s):
        if s not in cache:cache[s]=tuple(sum(1<<j for j,t in enumerate(ts) if not t&s) for ts in T)
        return cache[s]
    edges=[(a,b) for a,b in combinations(range(n),2) if H[a]>>b&1 and max(H[a].bit_count(),H[b].bit_count())+2<=k];
    for (a,b),(c,d) in combinations(edges,2):
        X=1<<a|1<<b;Y=1<<c|1<<d;W=X|Y
        if X&Y or (H[a]|H[b])&Y:continue
        ends=[(a,c),(a,d),(b,c),(b,d)]
        for rot in ((b,c,d,a),(d,b,a,c)):
            S=[1<<i|1<<j|(H[x]&~(W|H[i]|H[j])) for (i,j),x in zip(ends,rot)];G=grow(H,S)
            if max(map(int.bit_count,G))>k:continue
            m=list(map(miss,S));
            if any(x[0]&y[0] for x,y in combinations(m,2)) or m[0][2]&m[1][2]&m[2][2]&m[3][2]:continue
            bad=[t for t in T[1] if sum(not s&t for s in S)>=3];
            if bad:
                Z=((1<<n)-1)&~(S[0]|S[1]|S[2]|S[3]);z=max(t.bit_count() for t in I if not t&~Z);assert z+4<=k;assert all(sum(bool(t&s) for s in S)>=3 for t in T[0]);return dict(core=H,seed=[a,b,c,d],ports=S,donors=rot,alpha=alpha,blue=max(map(int.bit_count,inds(G))),invisible=Z,invisible_alpha=z,max_rows=len(T[0]),bad=bad)

def run():
    rng=Random(18119);counts=Counter()
    for n in range(11,22):
        for _ in range(2000):
            H=[0]*n;E=list(combinations(range(n),2));rng.shuffle(E)
            for x,y in E:
                if not H[x]&H[y]:H[x]|=1<<y;H[y]|=1<<x
            if min(map(int.bit_count,H))<2:continue
            counts[n]+=1;r=search(H)
            if r:return dict(counts=counts,witness=r)
    return dict(counts=counts,witness=None)
if __name__=='__main__':
    z=run();print(z);(D/'ramsey_three_only_copy.json').write_text(json.dumps(z)+'\n')
