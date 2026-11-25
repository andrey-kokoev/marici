"""Two-sided LP generation: price missing capacity rows against a small dual and price the primal against every legal support. Accept only integer-verified strict upper bounds."""
from ramsey312_release_fractional import *

def search(s,h,g,T,seed,limit=140,bonus=False,alpha=99):
 high=np.array([int(x.bit_count()==11) for x in s],dtype=np.int8);X=np.asarray(s,dtype=np.uint64);rng=random.Random(seed);budget=53-h.bit_count();cs={(1<<v,0):min(alpha,11-(g[v]&h).bit_count()) for v in bits(h) if (g[v]&h).bit_count()<11};cs[0,0]=99;idx=set(rng.sample(range(len(s)),min(100,len(s))));ts=np.array(T,dtype=np.uint64);cost=np.array([11-t.bit_count() for t in T]);blue=np.array([{1:2,2:5,3:8}.get(c,99) for c in cost]);vs=list(bits(h));
 for it in range(limit):
    sel=sorted(idx);sub=X[sel];keys=list(cs);c=np.array(list(cs.values()));mat=np.column_stack([((sub&b!=0) if b else np.ones(len(sub),dtype=bool)) & (sub&t==0) for b,t in keys]);mat=mat.astype(np.int8)
    if bonus:
        for j,(b,t) in enumerate(keys):
            if not b and t.bit_count()==10:mat[:,j]*=1+high[sel]
    r=linprog(c,A_ub=-mat.astype(float),b_ub=[-1]*len(sel),method='highs');assert r.success;lp=r.fun
    cov=np.zeros(len(s),dtype=np.int64);rect=[]
    for j in np.flatnonzero(r.x>1e-9):
        b,t=keys[j];w=math.ceil(r.x[j]*1000000+1e-6);rect.append((b,t,cs[b,t],w));cov+=w*(((X&b!=0) if b else True)&(X&t==0))*(1+high if bonus and b==0 and t.bit_count()==10 else 1)
    val=sum(w*c for b,t,c,w in rect);den=int(cov.min());
    if (0,0) not in [(b,t) for b,t,c,w in rect] and val<budget*den:return dict(cert=rect,den=den,cost=val,rounds=it+1,bonus=bonus)
    # Several extremal violations and a random sample keep the full-domain separation cheap.
    for cutoff,n in [(1000000,15),(int(cov.min())+1,10)]:
        bad=np.flatnonzero(cov<cutoff);idx.update(rng.sample(list(bad),min(n,len(bad))))
    y=-r.ineqlin.marginals;ids=np.flatnonzero(y>1e-10);active=sub[ids];weights=y[ids];miss=((active[:,None]&ts)==0);m=np.array([weights*((active&1<<v)!=0) for v in vs]);price=m@miss.astype(float)/np.minimum(cost,alpha);bp=(weights@miss.astype(float))/blue
    if bonus:bp+=((weights*high[np.array(sel)[ids]])@miss.astype(float))/blue*(cost==1)
    # Batch one maximizer for each relevant shared neighbor and several high-price unanchored witnesses.
    added=0
    for j,v in enumerate(vs):
        i=int(price[j].argmax());key=(1<<v,int(ts[i]));
        if price[j,i]>1+1e-7 and key not in cs:cs[key]=min(alpha,int(cost[i]));added+=1
    for i in np.argsort(-bp)[:8]:
        if bp[i]<=1+1e-7:break
        key=(0,int(ts[i]));
        if key not in cs:cs[key]=int(blue[i]);added+=1
    if not added and lp>=budget-1e-7:break
 return dict(cert=None,lp=float(lp),rounds=it+1,columns=len(cs),challenge=len(idx),pool=[(b,t,c) for (b,t),c in cs.items()],indices=list(map(int,sorted(idx))),dual=[(int(i),float(a)) for i,a in zip(sel,y) if a>1e-9])

def main():
 f,targets,label,limit=sys.argv[1:5];el=list(sets(F,11));cases=[l.split() for l in open(targets)];
 with (D/f'ramsey312_oracle_{label}.jsonl').open('w') as out:
    for l in open(f):
        k,*s=map(int,l.split());z=cases[k];d=int(z[2]);h=F^d;g=adj.copy()
        for e in z[5:]:i,j=map(int,e.split(':'));g[i]^=1<<j;g[j]^=1<<i
        tr={e&h for e in el};T=sorted(t for t in tr if 5<=t.bit_count()<=10 and all(not t&g[v] for v in bits(t)));
        if 'tens' in sys.argv[5:]:
            def independent(p,k,x):
                if not k:yield x;return
                while p.bit_count()>=k:
                    b=p&-p;p-=b;yield from independent(p&~g[b.bit_length()-1],k-1,x|b)
            T=sorted(set(T)|set(independent(h,10,0)))
        r=search(s,h,g,T,k,int(limit),'bonus' in sys.argv[5:]);out.write(json.dumps(dict(k=k,case=z,**r))+'\n');out.flush()
if __name__=='__main__':main()
