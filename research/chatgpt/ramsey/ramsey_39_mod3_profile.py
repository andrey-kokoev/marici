"""Find a class-labelled abstract counterprofile; no realizability assumed."""
from functools import lru_cache
@lru_cache(None)
def parts(n,s,lo=0):
    if not n:return [()] if not s else []
    return [(x,)+t for x in range(max(lo,s-12*(n-1)),min(12,s//n)+1) for t in parts(n-1,s-x,x)]
def sq(t):return sum(x*x for x in t)
def run():
    for a in [(4,4,4),(5,4,3),(6,3,3),(5,5,2),(6,4,2)]:
        hs=[sum(a[j]*a[(i-j)%3] for j in range(3)) for i in range(3)];rs=sum(x*x for x in a);r1=(144-rs)//2
        rr={sq(r):r for r in parts(13,r1)};ener={144+2*(sq(z)+e):(z,r) for z in parts(6,(rs-12)//2) for e,r in rr.items()}
        dp={0:(0,[])}
        for i in range(3):
            opt={}
            for h in parts(13,hs[i],2):
                if sum(x%2 for x in h)!=a[2*i%3]:continue
                e=sq(h);c=sum(min(9,2*x) for x in h)
                if c>opt.get(e,(-1,None))[0]:opt[e]=c,h
            nd={}
            for e,(c,L) in dp.items():
                for f,(d,h) in opt.items():
                    if c+d>nd.get(e+f,(-1,None))[0]:nd[e+f]=c+d,L+[h]
            dp=nd
        for e,(c,H) in dp.items():
            if c>=272 and e in ener:print('a',a,'H',H,'R half classes',ener[e],'energy',e,'cap',c);return
if __name__=='__main__':run()
