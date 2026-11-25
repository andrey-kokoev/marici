"""Full-domain degree relaxation, using a cutting-plane loop with at most 52 columns. Can also reuse a small pool of sampled shadow rectangles."""
from ramsey312_release_fractional import *

def pool_lp(s,cs,k,ss=None,threshold=7):
 X=np.array(s,dtype=np.uint64);rng=random.Random(k);cs=list(dict.fromkeys(cs));cost=[c for b,t,c in cs];idx=set(rng.sample(range(len(s)),min(90,len(s))));den=1000000
 if ss:idx.update(ss)
 for it in range(100):
    sub=X[list(idx)];mat=np.column_stack([((sub&b!=0) if b else np.ones(len(sub),dtype=bool))&(sub&t==0) for b,t,c in cs]);res=linprog(cost,A_ub=-mat.astype(float),b_ub=[-1]*len(idx),method='highs')
    if not res.success or res.fun>=threshold-1e-8:return None
    rect=[(*row,int(math.ceil(w*den+1e-5))) for row,w in zip(cs,res.x) if w>1e-10];cov=np.zeros(len(s),dtype=np.int64)
    for b,t,c,w in rect:cov+=w*(((X&b!=0) if b else True)&(X&t==0))
    bad=np.flatnonzero(cov<den);total=sum(c*w for b,t,c,w in rect)
    minimum=int(cov.min())
    if total<threshold*minimum:return dict(cert=rect,den=minimum,cost=total)
    if not len(bad):return None
    idx.update(rng.sample(list(bad),min(48,len(bad))));worst=np.flatnonzero(cov==minimum);idx.update(rng.sample(list(worst),min(32,len(worst))))
 return None

def main():
 cases=[l.split() for l in (D/'ramsey312_bounded24_6.txt').open() if l.startswith('L ')];out=[]
 for line in open(sys.argv[1]):
    k,*s=map(int,line.split());z=cases[k];h=F^int(z[2]);g=adj.copy()
    for e in z[5:]:i,j=map(int,e.split(':'));g[i]^=1<<j;g[j]^=1<<i
    cs=[(1<<i,0,11-(h&g[i]).bit_count()) for i in bits(h) if (h&g[i]).bit_count()<11];r=pool_lp(s,cs,k)
    if r:out.append(dict(k=k,**r))
 print('degree fractional passes',len(out));(D/'ramsey312_degree_fraction25.json').write_text(json.dumps(out))
if __name__=='__main__':main()
