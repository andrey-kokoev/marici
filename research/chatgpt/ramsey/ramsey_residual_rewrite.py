"""Two reversible residual rewrites; keep the base data unchanged."""
from math import comb
from ramsey_spectral_correction_codec import predict,update,seed


def transform(g,feedback=False,inverse=False):
    history=[];out=[]
    for j,r in enumerate(g):
        inp=r&((1<<j)-1);v=inp^predict(history,True)
        out=update(out,v)
        history=update(history,v if feedback!=inverse else inp)
    return out

def cost(g):
    n=comb(len(g),2);k=sum(r.bit_count() for r in g)//2
    return k,n.bit_length()+(comb(n,k)-1).bit_length()

if __name__=='__main__':
    orig=seed(7,'double')[0];order=[j for i in range(10) for j in (i,i+10)]
    for mask in range(8):
        g=orig.copy()
        for t,(i,j) in enumerate(((0,5),(1,6),(2,7))):
            for x,y in ((i,j),(j,i)):g[x]=(g[x]&~(1<<y))|((mask>>t&1)<<y)
        base=[sum((g[i]>>j&1)<<t for t,j in enumerate(order)) for i in order]
        first=transform(base);second=transform(first);online=transform(base,True)
        assert transform(transform(second,inverse=True),inverse=True)==base
        assert transform(online,True,True)==base
        print(mask,*map(cost,(base,first,second,online)))
