"""Freeze corrected two-orientation rule. All induced matching seeds on complete smaller catalogues and a seeded record-uniform sample from the 27-vertex catalogue. No tuning by degree beyond necessary target-capacity checks."""
from ramsey_neighbourhood_square import D,json,inds,bits,verify,grow,combinations,Counter
import gzip
from random import Random
from functools import lru_cache

def graph(line):
    n=line[0]-63;H=[0]*n
    for j in range(n):
        for i in range(j):
            k=j*(j-1)//2+i
            if ((line[1+k//6]-63)>>(5-k%6))&1:H[i]|=1<<j;H[j]|=1<<i
    return H

def audit(H,k):
    n=len(H);F=(1<<n)-1;I=inds(H);assert max(s.bit_count() for s in I)==k-1;T=[[t for t in I if t.bit_count()==k-i] for i in (1,2,3)];
    @lru_cache(None)
    def misses(s):return [sum(1<<i for i,t in enumerate(Tj) if not t&s) for Tj in T]
    edges=[(a,b) for a,b in combinations(range(n),2) if H[a]>>b&1];cnt=Counter();ex=None
    for (a,b),(c,d) in combinations(edges,2):
        X=1<<a|1<<b;Y=1<<c|1<<d
        if X&Y or (H[a]|H[b])&Y:continue
        W=X|Y;cnt['matchings']+=1;P=[H[i]&~W for i in (a,b,c,d)];coll=any(u&v for u,v in combinations(P,2));theorem=False
        if not coll:
            cnt['private']+=1;Z=F&~(W|P[0]|P[1]|P[2]|P[3]);theorem=not any(t&~Z==0 for t in T[2]);cnt['predicted']+=theorem
        if any(H[v].bit_count()+2>k for v in (a,b,c,d)):assert not theorem;continue
        cnt['degree_seeds']+=1;ends=[(a,c),(a,d),(b,c),(b,d)];success=0
        for rot in ((b,c,d,a),(d,b,a,c)):
            S=[1<<i|1<<j|(H[x]&~(W|H[i]|H[j])) for (i,j),x in zip(ends,rot)];
            if any(s.bit_count()>k for s in S) or any(H[v].bit_count()+sum(s>>v&1 for s in S)>k for v in range(n)):continue
            cnt['capacity_orientations']+=1;m=list(map(misses,S));
            if any(u[0]&v[0] for u,v in combinations(m,2)):continue
            cnt['top_pass']+=1
            if any(u[1]&v[1]&w[1] for u,v,w in combinations(m,3)) or m[0][2]&m[1][2]&m[2][2]&m[3][2]:continue
            success+=1
            if ex is None:verify(grow(H,S),k+1);ex=dict(seed=W,ports=S,private=not coll)
        if not coll:assert success==2*theorem
        if success:cnt['successful_seeds']+=1;cnt['successful_orientations']+=success;cnt['collision_successes']+=bool(coll)
    return dict(counts=cnt,example=ex)

def run():
    out={}
    for k,n in ((4,8),(5,13),(6,17),(7,22),(8,27)):
        p=D/'pauli-realization-catalogues'/f'r3{k}_{n}.g6';raw=gzip.decompress(p.with_suffix('.g6.gz').read_bytes()) if k==8 else p.read_bytes();ls=raw.splitlines();idx=list(range(len(ls))) if k<8 else sorted(Random(68437).sample(range(len(ls)),64));rows=[dict(record=i+1,**audit(graph(ls[i]),k)) for i in idx];out[k]=rows;print(k,len(rows),sum(bool(r['example']) for r in rows),sum((r['counts'] for r in rows),Counter()),flush=True)
    return out
if __name__=='__main__':(D/'ramsey_square_level_transfer.json').write_text(json.dumps(run())+'\n')
