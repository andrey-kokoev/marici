"""Exact budget cover using only the global catalog of independent elevens. For speed generate cover rows on a growing challenge subset. Optional suffix from CLI labels each shard."""
from ramsey312_google_two_step import *
from functools import reduce,lru_cache
from operator import or_,and_
import gzip

def cover(d,s,el):
    h=F^d;anchors={1<<i:adj[i]&h for i in bits(d)};cat={}
    for e in el:
        g=e&d
        if g:cat.setdefault(g,[]).append(e^g)
    cat={g:(reduce(and_,(anchors[1<<i] for i in bits(g))),ts) for g,ts in cat.items()};cat={g:(b,ts) for g,(b,ts) in cat.items() if b};start=set(anchors.values());rounds=0
    def parts(m):
        if not m:yield ();return
        b=m&-m
        for g in cat:
            if b&g and m&g==g:
                for p in parts(m^g):yield (g,*p)
    ps=sorted(parts(d),key=lambda p:(-len(p),p));assert ps
    while True:
        rounds+=1;ss=sorted(start);full=(1<<len(ss))-1;col=[sum(1<<j for j,x in enumerate(ss) if x>>i&1) for i in range(52)]
        @lru_cache(None)
        def rows(g):
            mask,ts=cat[g];cs={}
            for t in ts:
                miss=full
                for v in bits(t):miss&=~col[v]
                for i in bits(mask):cs.setdefault(miss&col[i],(1<<i,t))
            mx={}
            for r in sorted(cs,key=int.bit_count,reverse=True):
                if not any(r&~z==0 for z in mx):mx[r]=cs[r]
            return mx,reduce(or_,mx,0)
        def solve(p,rem):
            if not p:return [] if not rem else None
            poss=[rows(g)[1] for g in p];opts=[]
            if rem&~reduce(or_,poss):return None
            for j,g in enumerate(p):
                need=rem&~reduce(or_,poss[:j]+poss[j+1:],0);v=[r for r in rows(g)[0] if not need&~r];
                if not v:return None
                opts.append((len(v),j,v))
            _,j,v=min(opts);g=p[j]
            for r in sorted(v,key=lambda r:(r&rem).bit_count(),reverse=True):
                z=solve(p[:j]+p[j+1:],rem&~r)
                if z is not None:return [(g,*rows(g)[0][r]),*z]
            return None
        for p in ps:
            z=solve(p,full)
            if z is not None:break
        else:return dict(cert=None,challenge=ss,rounds=rounds)
        misses=[x for x in s if not any(x&b and not x&t for g,b,t in z)]
        if not misses:return dict(cert=z,rounds=rounds,challenge_size=len(ss))
        start.update(misses[::max(1,len(misses)//24)][:25]);rows.cache_clear()

def main():
 el=list(sets(F,11));f,prefix=sys.argv[1:3];
 with open(f) as src,gzip.open(D/f'ramsey312_shadow_{prefix}.jsonl.gz','wt') as out:
    for l in src:
        d,*s=map(int,l.split());r=cover(d,s,el);out.write(json.dumps(dict(d=d,n=len(s),**r))+'\n');out.flush()
if __name__=='__main__':main()
