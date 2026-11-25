"""Price flexible capacity-one classes: a common red bit and a union of upper intervals. Any two interval maxima jointly miss a core independent ten. Extend a dual-active incompatible family to generous intervals using a small pair-witness cover."""
from ramsey312_capacity_oracle import *
from functools import lru_cache

def go(s,h,g,seed,r,limit):
 X=np.array(s,dtype=np.uint64);cs={(b,(t,)):c for b,t,c in r['pool']};I=set(r['indices']);rng=random.Random(seed);vs=list(bits(h))
 def ten(p,k,x):
    if not k:yield x;return
    while p.bit_count()>=k:
        b=p&-p;p-=b;yield from ten(p&~g[b.bit_length()-1],k-1,x|b)
 ts=list(ten(h,10,0));tsarr=np.array(ts,np.uint64);fullrows={};
 @lru_cache(None)
 def miss(x):return int.from_bytes(np.packbits((tsarr&x)==0,bitorder='little').tobytes(),'little')
 def inc(key):
    if key not in fullrows:
        b,tt=key;ok=np.zeros(len(s),bool)
        for t in tt:ok|=(X&t)==0
        fullrows[key]=((X&b!=0)&ok if b else ok).astype(np.int8)
    return fullrows[key]
 def expand(fam):
    # Find all pair witnesses, choosing the ten that covers most members of the family when possible.
    mx=[]
    for x in sorted(set(fam),key=int.bit_count,reverse=True):
        if not any(x&~z==0 for z in mx):mx.append(x)
    if len(mx)==1:return (ts[(miss(mx[0])&-miss(mx[0])).bit_length()-1],)
    patterns={};col={i:sum(1<<j for j,x in enumerate(mx) if x>>i&1) for i in vs};full=(1<<len(mx))-1
    for t in ts:
        p=full&~reduce(or_,(col[i] for i in bits(t)));patterns.setdefault(p,t)
    sig=[0]*len(mx);need=[(1<<(j+1))-1 for j in range(len(mx))];chosen=[]
    for p in sorted(patterns,key=int.bit_count,reverse=True):
        ii=list(bits(p));
        if not any(need[j]&p for j in ii):continue
        chosen.append(p)
        for j in ii:need[j]&=~p;sig[j]|=patterns[p]
        if not any(need):break
    assert not any(need);zs=[]
    for t in sorted(set(sig),key=int.bit_count):
        if not any(z&~t==0 for z in zs):zs.append(t)
    assert all(miss(h&~(t&u)) for t in zs for u in zs);return tuple(zs)
 for it in range(limit):
    sel=np.array(sorted(I));K=list(cs);M=np.column_stack([inc(key)[sel] for key in K]);res=linprog(list(cs.values()),A_ub=-M.astype(float),b_ub=[-1]*len(sel),method='highs');assert res.success;cov=np.zeros(len(s),np.int64);cert=[]
    for j in np.flatnonzero(res.x>1e-9):
        b,tt=K[j];w=math.ceil(res.x[j]*1000000+1e-5);cert.append((b,tt,cs[K[j]],w));cov+=inc(K[j]).astype(np.int64)*w
    cost=sum(c*w for b,tt,c,w in cert);mn=int(cov.min())
    if cost<8*mn and all(b or any(tt) for b,tt,c,w in cert):return dict(cert=cert,den=mn,cost=cost,rounds=it+1)
    for mask,n in [(cov<1000000,25),(cov==mn,18)]:
        bad=np.flatnonzero(mask);I.update(rng.sample(list(bad),min(n,len(bad))))
    ids=np.flatnonzero(res.ineqlin.marginals<-1e-8);xx=[s[sel[i]] for i in ids];yy=-res.ineqlin.marginals[ids];conf=[{j for j,y in enumerate(xx) if not miss(x)&miss(y)} for x in xx];good=[]
    for v in vs:
        V={i for i,x in enumerate(xx) if x>>v&1};
        if sum(yy[i] for i in V)<1+1e-7:continue
        for order in [sorted(V,key=lambda i:-yy[i]),sorted(V,key=lambda i:sum(yy[j] for j in conf[i]&V)/yy[i]),rng.sample(sorted(V),len(V))]:
            fam=[];blocked=set()
            for i in order:
                if i not in blocked:fam.append(i);blocked.update(conf[i])
            val=sum(yy[i] for i in fam)
            if val>1+1e-6:good.append((val,v,tuple(sorted(xx[i] for i in fam))))
    added=0
    for val,v,fam in sorted(set(good),reverse=True)[:5]:
        tt=expand(fam);key=(1<<v,tt)
        if key not in cs:cs[key]=1;added+=1
    print('step',it,'pool',len(K),'restricted',round(res.fun,4),'minimum budget',round(cost/max(1,mn),4),'added',added,flush=True)
    if not added and res.fun>=8:break
 return dict(cert=None,lp=res.fun,rounds=it+1)

def main():
 f,pool,label=sys.argv[1:4];k,*s=map(int,open(f).read().split());r=json.loads(open(pool).read());assert k==r['k'];z=r['case'];h=F^int(z[2]);g=adj.copy()
 for e in z[5:]:i,j=map(int,e.split(':'));g[i]^=1<<j;g[j]^=1<<i
 result=go(s,h,g,k,r,90);(D/f'ramsey312_interval27_{label}.json').write_text(json.dumps(dict(k=k,case=z,**result)))
if __name__=='__main__':main()
