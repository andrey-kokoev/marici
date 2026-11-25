"""Incremental row/column LP. Seed with valid transferred certificate classes from one-restoration parents. Only integer full-domain lower coverage proves an exclusion."""
from ramsey312_google_two_step import *
import numpy as np, highspy, random, math, gzip
from scipy.sparse import csr_matrix

def adapted(b,t,h):
 if b and not b&h:return None
 t=t&h
 if b and t:
    if any(adj[v]&t for v in bits(t)):return None
    return b,t,11-t.bit_count()
 if b:return b,0,11-(adj[b.bit_length()-1]&h).bit_count()
 if any(adj[v]&t for v in bits(t)):return None
 c={10:2,9:5,8:8}.get(t.bit_count(),99);return 0,t,c

def run(k,s,d,E,donors,limit,extra,alpha=99,singles=None):
 h=F^d;budget=1+d.bit_count();vs=list(bits(h));X=np.asarray(s,dtype=np.uint64);rng=random.Random(7001+k);T=sorted({t&h for t in E if 5<=(t&h).bit_count()<=10}|set(extra));ts=np.array(T,np.uint64);cc=np.array([11-t.bit_count() for t in T]);bc=np.array([{1:2,2:5,3:8}.get(c,99) for c in cc]);high=np.array([int(x.bit_count()==11) for x in s],np.int8);single_masks=sorted((singles or {}).keys());us=np.array(single_masks,np.uint64);L=highspy.Highs();L.setOptionValue('output_flag',False);L.setOptionValue('threads',1);L.setOptionValue('presolve','off');L.setOptionValue('solver','simplex');L.setOptionValue('parallel','off');K=[];C=set();sel=[];used=set();idx=np.array([],dtype=int);Kbs=[];Kts=[]
 def mat(ids,keys):
    if not keys:return np.empty((len(ids),0),np.float64)
    b=np.array([b for b,t,c in keys],np.uint64);t=np.array([t for b,t,c in keys],np.uint64);x=X[ids,None];M=(((x&b!=0)|(b==0))&(x&t==0)).astype(np.int8);flag=np.array([b==0 and c==2 and t.bit_count()==10 for b,t,c in keys]);
    if flag.any():M[:,flag]*=1+high[ids,None]
    return M
 def cols(ks):
    new=[p for p in dict.fromkeys(ks) if p not in C];
    if not new:return
    m=csr_matrix(mat(idx,new).T,dtype=float);l=len(new);assert L.addCols(l,[p[2] for p in new],np.zeros(l),np.full(l,highspy.kHighsInf),m.nnz,m.indptr,m.indices,m.data)==highspy.HighsStatus.kOk;K.extend(new);C.update(new)
 def rows(ar):
    nonlocal idx
    new=sorted(set(map(int,ar))-used)
    if not new:return
    used.update(new);sel.extend(new);idx=np.array(sel);m=csr_matrix(mat(np.array(new),K),dtype=float);l=len(new);assert L.addRows(l,np.ones(l),np.full(l,highspy.kHighsInf),m.nnz,m.indptr,m.indices,m.data)==highspy.HighsStatus.kOk
 cols([(1<<v,0,min(alpha,11-(adj[v]&h).bit_count())) for v in vs if (adj[v]&h).bit_count()<11]+[(0,0,99)]+list(donors));rows(rng.sample(range(len(s)),min(220,len(s))));lp=None
 for it in range(limit):
    L.run();assert L.getModelStatus()==highspy.HighsModelStatus.kOptimal;sol=L.getSolution();lp=L.getObjectiveValue();w=np.array(sol.col_value);y=np.array(sol.row_dual);good=np.flatnonzero(w>1e-8);rect=[(*K[j],int(math.ceil(w[j]*1000000+1e-5))) for j in good];val=sum(c*w for b,t,c,w in rect);sub=np.arange(len(s)) if lp<budget and (it%3==0 or it<3) else np.array(rng.sample(range(len(s)),min(5000,len(s))));x=X[sub];hc=high[sub];cov=np.zeros(len(sub),np.int64)
    for b,t,c,w0 in rect:cov+=w0*(((x&b!=0) if b else True)&(x&t==0))*(1+hc if b==0 and c==2 and t.bit_count()==10 else 1)
    den=int(cov.min());
    if len(sub)==len(s) and val<budget*den and all(b|t for b,t,c,w0 in rect):return dict(cert=rect,den=den,cost=val,bonus=True,rounds=it+1,singles={t:singles[t] for b,t,c,w in rect if not b and c==1})
    old=len(used)
    for target,num in [(1000000,24),(den+1,12)]:
        bad=sub[cov<target];rows(rng.sample(list(bad),min(num,len(bad))))
    ids=np.flatnonzero(y>1e-9);x=X[idx[:len(y)][ids]];v=y[ids];mi=((x[:,None]&ts)==0).astype(float);price=(np.array([v*(x&(1<<i)!=0) for i in vs])@mi)/np.minimum(cc,alpha);blue=(v@mi+(v*high[idx[:len(y)][ids]])@mi*(cc==1))/bc;added=[]
    for j,b in enumerate(vs):
        for ii in np.argpartition(price[j],-3)[-3:]:
            if price[j,ii]>1.000001:added.append((1<<b,T[ii],min(alpha,int(cc[ii]))))
    for ii in np.argpartition(blue,-10)[-10:]:
        if blue[ii]>1.000001:added.append((0,T[ii],int(bc[ii])))
    if len(us):
        for start in range(0,len(us),5000):
            block=us[start:start+5000];prices=v@((x[:,None]&block)==0).astype(float)
            for jj in np.argpartition(prices,-min(18,len(block)))[-18:]:
                if prices[jj]>1.000001:added.append((0,int(block[jj]),1))
    oldc=len(K);cols(added)
    if oldc==len(K) and lp>=budget-1e-7:break
 return dict(cert=None,rounds=it+1,last_lp=lp)

def main():
 shard,targets,label,limit=sys.argv[1:5];el=list(sets(F,11));cases=[l.split() for l in open(targets)];data=json.load(gzip.open(D/'ramsey312_two_retained_certs.json.gz'));donors={}
 for r in data:donors.setdefault(int(r['case'][2]),set()).update((b,t) for b,t,c,w in r['cert']);
 extras=list(sets(F,10)) if 'tens' in sys.argv[5:] else []
 wit={}
 if 'witness' in sys.argv[5:]:
    for ln in open(sys.argv[sys.argv.index('witness')+1]):
        w=ln.split();wit[int(w[0])]=dict(tuple(map(int,p.split(':'))) for p in w[1:])
 with (D/f'ramsey312_warm_{label}.jsonl').open('w') as o:
    for l in open(shard):
        k,*s=map(int,l.split());z=cases[k];d=int(z[2]);h=F^d;assert z[3]=='0';rows=set();
        for v in bits(d):
            for b,t in donors.get(d^(1<<v),[]):
                p=adapted(b,t,h)
                if p and p[2]<d.bit_count()+1:rows.add(p)
        r=run(k,s,d,el,rows,int(limit),[t for t in extras if t&d==0],singles=wit.get(k));o.write(json.dumps(dict(k=k,case=z,**r))+'\n');o.flush()
if __name__=='__main__':main()
