"""Strengthen missed-ten capacity rows by counting isolated supports twice: two newcomers missing T must have disjoint supports. Isolated supports may also join every intersecting b-class missing the same T."""
from ramsey312_capacity_oracle import *
from collections import deque

def solve(s,h,g,T,seed,limit):
 X=np.array(s,dtype=np.uint64);mins=[]
 for x in sorted(s,key=int.bit_count):
    if not any(x&y==y for y in mins):mins.append(x)
 ms=np.array(mins,dtype=np.uint64);ts=np.array(T,dtype=np.uint64);cost=np.array([11-t.bit_count() for t in T]);vs=list(bits(h));blue=np.array([{1:2,2:5,3:8}.get(c,99) for c in cost]);n=len(s);rng=random.Random(seed);I=set(rng.sample(range(n),100));C={(1<<v,0):11-(g[v]&h).bit_count() for v in vs if (g[v]&h).bit_count()<11};C[0,0]=99;subiso={};tiso={};mm=(ms[:,None]&ts)==0;pool={};
 def incidence(b,t):
    if (b,t) not in pool:
        ok=(X&t)==0;rb=(X&b!=0) if b else np.ones(n,bool)
        if t.bit_count()==10:
            if t not in tiso:
                partner=np.zeros(n,bool)
                for y in ms[(ms&t)==0]:partner|=(X&y)==0
                tiso[t]=ok&~partner
            iso=tiso[t];p=(ok&(rb|iso)).astype(np.int8) if b else ok.astype(np.int8)+iso
        else:p=(rb&ok).astype(np.int8)
        pool[b,t]=p
    return pool[b,t]
 for it in range(limit):
    sel=np.array(sorted(I));K=list(C);M=np.column_stack([incidence(b,t)[sel] for b,t in K]);r=linprog(list(C.values()),A_ub=-M.astype(float),b_ub=[-1]*len(sel),method='highs');assert r.success;y=-r.ineqlin.marginals;ids=np.flatnonzero(y>1e-8);xx=X[sel[ids]];w=y[ids];rect=[];cov=np.zeros(n,np.int64)
    for j in np.flatnonzero(r.x>1e-10):
        b,t=K[j];a=math.ceil(1000000*r.x[j]+1e-6);rect.append((b,t,C[b,t],a));cov+=incidence(b,t).astype(np.int64)*a
    budget=sum(c*a for b,t,c,a in rect);den=int(cov.min());
    if all(b|t for b,t,c,a in rect) and budget<8*den:return dict(cert=rect,cost=budget,den=den,isolated=True,rounds=it+1)
    for mask,nadd in [(cov<1000000,12),(cov==den,15)]:
        bad=np.flatnonzero(mask);I.update(rng.sample(list(bad),min(nadd,len(bad))))
    for x in xx:
        if int(x) not in subiso:subiso[int(x)]=~np.any(mm[(ms&x)==0],axis=0)&(cost==1)
    miss=(xx[:,None]&ts)==0;iso=np.stack([subiso[int(x)] for x in xx])&miss;bitsmat=np.array([w*(xx&(1<<v)!=0) for v in vs]);mi=miss.astype(float);iv=iso.astype(float);pr=(bitsmat@(mi-iv)+w@iv)/cost;bp=(w@(mi+iv))/blue;added=0
    for j,v in enumerate(vs):
        i=int(pr[j].argmax());key=(1<<v,int(ts[i]));
        if pr[j,i]>1+1e-7 and key not in C:C[key]=int(cost[i]);added+=1
    for i in np.argsort(-bp)[:10]:
        if bp[i]<=1+1e-7:break
        key=(0,int(ts[i]));
        if key not in C:C[key]=int(blue[i]);added+=1
    if not added and r.fun>=8-1e-7:break
 return dict(cert=None,lp=float(r.fun),rounds=it+1,challenge=len(I),columns=len(C))

def main():
 f,label=sys.argv[1:3];cases=[l.split() for l in (D/'ramsey312_release26_two_targets.txt').open()];E=list(sets(F,11));
 for l in open(f):
    k,*s=map(int,l.split());z=cases[k];h=F^int(z[2]);g=adj.copy()
    for e in z[5:]:i,j=map(int,e.split(':'));g[i]^=1<<j;g[j]^=1<<i
    T={e&h for e in E};T={t for t in T if 5<=t.bit_count()<=10 and all(not t&g[i] for i in bits(t))};r=solve(s,h,g,sorted(T),k,140);print(k,bool(r['cert']),r.get('lp'),r['rounds']);(D/f'ramsey312_partner27_{label}.json').write_text(json.dumps(dict(k=k,case=z,**r)))
if __name__=='__main__':main()
