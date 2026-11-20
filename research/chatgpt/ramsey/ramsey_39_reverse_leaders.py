"""Find a deletion path whose inverse always selects a maximum partner count."""
from ramsey_39_fixed_seed_exact import B,I
from functools import lru_cache
from random import Random
full=(1<<35)-1
order=list(range(35));Random(39).shuffle(order)
def members(p):
    while p:
        b=p&-p;yield b.bit_length()-1;p^=b
# Global candidate indices, then restrict by active vertex set and octet hits.
U=(1<<len(I))-1
inc=[]
for v in range(35):
    raw=bytearray((len(I)+7)//8)
    for j,p in enumerate(I):
        if p>>v&1:raw[j//8]|=1<<(j%8)
    inc.append(int.from_bytes(raw,'little'))
def touch(p,table):
    ans=0
    for i in members(p):ans|=table[i]
    return ans
E=[(s,touch(s,inc)) for s in I if s.bit_count()==8];S=[s for s in I if s.bit_count()==7]
@lru_cache(None)
def scores(active):
    gone=full^active; ok=U & ~touch(gone,inc)
    for e,t in E:
        if not e&gone:ok &=t
    opts=[I[i] for i in members(ok)]; table=[sum(1<<j for j,p in enumerate(opts) if p>>i&1) for i in range(35)]
    missed=[(s,~touch(s,table)) for s in S if not s&gone];out={}
    for p in opts:
        bad=0
        for s,m in missed:
            if not p&s:bad|=m
        out[p]=len(opts)-(touch(p,table)&bad).bit_count()
    return out

def path(active):
    if active.bit_count()==27:return []
    for v in order:
        if not active>>v&1:continue
        child=active^(1<<v);d=scores(child);n=d[B[v]&child]
        if n!=max(d.values()):continue
        tail=path(child)
        if tail is not None:return [(v+1,len(d),n,sum(x==n for x in d.values()))]+tail
    return None
if __name__=='__main__':print(path(full))
