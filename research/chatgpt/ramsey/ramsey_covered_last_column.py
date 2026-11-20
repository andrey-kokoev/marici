"""Cover b7w; use only the old graph and Ramsey validity to derive bits. The
spectral predictor receives precisely that same prefix. Reveal the old answer last.
"""
from functools import reduce,lru_cache
from operator import and_,or_
from ramsey_row_rank_codec import legal
from ramsey_spectral_correction_codec import predict,seed

def inspect(rows):
    opts=tuple(legal(rows)); full=(1<<len(rows))-1
    plus=reduce(and_,opts); minus=full^reduce(or_,opts)
    @lru_cache(None)
    def depth(ss):
        if len(ss)==1:return 0
        splits=[(tuple(p for p in ss if p>>i&1),tuple(p for p in ss if not(p>>i&1))) for i in range(len(rows))]
        return 1+min(max(depth(a),depth(b)) for a,b in splits if a and b)
    return opts,plus,minus,depth(opts),predict(rows,True)

if __name__=='__main__':
    orig=seed(7,'double')[0];order=[j for i in range(10) for j in (i,i+10)];names=[f'a{i+1}' for i in range(3)]+[f'b{i+1}' for i in range(7)];names+= [s+'w' for s in names]
    for mask in range(8):
        g=orig.copy()
        for t,(i,j) in enumerate(((0,5),(1,6),(2,7))):
            for x,y in ((i,j),(j,i)):g[x]=(g[x]&~(1<<y))|((mask>>t&1)<<y)
        old=order[:-1]; project=lambda r:sum((r>>i&1)<<j for j,i in enumerate(old));rows=[project(g[i]) for i in old];opts,p,m,d,pred=inspect(rows)
        actual=project(g[order[-1]]);assert actual in opts
        print(mask,len(opts),p.bit_count(),m.bit_count(),d,'predicted forced correct',((p&pred)|(m&~pred)).bit_count(),'prediction valid',pred in opts)
        if not mask:
            for label,v in [('forced positive',p),('variable',((1<<19)-1)^(p|m))]:print(label,[names[i] for j,i in enumerate(old) if v>>j&1])
