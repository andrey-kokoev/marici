"""Fractional capacity certificates on rewired partial graphs. Rows: red degree; shared neighbor and missed original-eleven trace; triangle-free bound 2 on supports missing an independent ten. Every successful output checked using integer arithmetic."""
from ramsey312_google_two_step import *
import random,math,numpy as np
from scipy.optimize import linprog
from functools import reduce
from operator import or_

def run(s,h,g,el,seed,limit,full_pool=False,threshold=7,extra=()):
 if full_pool:from ramsey312_degree_lp import pool_lp
 pool=set()
 rng=random.Random(seed);X=np.array(s,dtype=np.uint64);ss=set(rng.sample(s,min(40,len(s))));den=100000;lp=None;tr={e&h for e in el}|set(extra);tr={t for t in tr if 5<=t.bit_count()<=10 and all(not t&g[v] for v in bits(t))};cs=[(1<<v,0,11-(g[v]&h).bit_count()) for v in bits(h) if 0<11-(g[v]&h).bit_count()<threshold];
 for it in range(limit):
    ls=sorted(ss);full=(1<<len(ls))-1;col={v:sum(1<<j for j,x in enumerate(ls) if x>>v&1) for v in bits(h)};rows={}
    def add(p,b,t,c):
        if p and (p not in rows or rows[p][2]>c):rows[p]=(b,t,c)
    for b,t,c in cs:add(col[b.bit_length()-1],b,t,c)
    for t in tr:
        cost=11-t.bit_count();m=full&~reduce(or_,(col[v] for v in bits(t))); 
        if not m:continue
        if cost==1:add(m,0,t,2)
        if cost==2:add(m,0,t,5)
        if cost==3 and threshold>8:add(m,0,t,8)
        for v,p in col.items():add(m&p,1<<v,t,cost)
    mx=[]
    for p in sorted(rows,key=lambda p:(rows[p][2],-p.bit_count())):
        if not any(p&~r==0 for r in mx):mx.append(p)
    if full_pool:
        pool.update(rows[p] for p in mx);pool.update(cs)
        solved=pool_lp(s,sorted(pool),seed,threshold=threshold)
        if solved:return dict(**solved,rounds=it+1)
    res=linprog([rows[p][2] for p in mx],A_ub=[[-(p>>i&1) for p in mx] for i in range(len(ls))],b_ub=[-1]*len(ls),method='highs');
    if not res.success:break
    lp=float(res.fun)
    if lp>=threshold-1e-8:break
    rect=[(*rows[p],int(math.ceil(w*den+1e-5))) for p,w in zip(mx,res.x) if w>1e-10];cost=sum(c*w for b,t,c,w in rect);coverage=np.zeros(len(s),dtype=np.int64)
    for b,t,c,w in rect:coverage+=w*((((X&b)!=0) if b else True)&((X&t)==0))
    bad=np.flatnonzero(coverage<den)
    if not len(bad) and cost<threshold*den:return dict(cert=rect,cost=cost,den=den,rounds=it+1)
    if not len(bad):break
    ss.update(s[j] for j in rng.sample(list(bad),min(24,len(bad))))
 return dict(cert=None,challenge=len(ss),last_lp=lp)

def main():
 idx,n=map(int,sys.argv[2:4]);el=list(sets(F,11));cases=[l.split() for l in (D/'ramsey312_bounded24_6.txt').open() if l.startswith('L ')];
 pooled=len(sys.argv)>4;skip=set();suffix=''
 if pooled:
    suffix='pool_';skip={r['k'] for r in json.loads((D/'ramsey312_degree_fraction25.json').read_text())};skip.update(r['k'] for f in D.glob('ramsey312_release_frac25_[0-9]*.jsonl') for r in map(json.loads,f.open()) if r['cert'])
 with (D/f'ramsey312_release_frac25_{suffix}{idx}.jsonl').open('w') as out:
    for k,line in enumerate(open(sys.argv[1])):
        if k%n!=idx or k in skip:continue
        ix,*s=map(int,line.split());assert ix==k;z=cases[k];h=F^int(z[2]);g=adj.copy();
        for e in z[5:]:i,j=map(int,e.split(':'));g[i]^=1<<j;g[j]^=1<<i
        r=run(s,h,g,el,k,4 if pooled else 12,pooled);out.write(json.dumps(dict(k=k,**r))+'\n');out.flush()
if __name__=='__main__':main()
