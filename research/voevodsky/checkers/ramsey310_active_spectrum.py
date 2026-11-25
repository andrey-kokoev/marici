"""Exact combinatorial Gram counts + numerical SVD on nested witness prefixes.
uv run --with numpy python ... . OPENBLAS_NUM_THREADS=1 recommended.
"""
import csv,json,math,itertools,os
from pathlib import Path
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from functools import cache
from ramsey310_codegree7_test import sets
D=Path(__file__).resolve().parents[1]/'results';n=39
a=np.loadtxt(D.parents[1]/'chatgpt/ramsey/ramsey_3_10_witness_39.csv',delimiter=',',dtype=int);assert a.shape==(n,n) and np.array_equal(a,a.T)
def measure(p):
 F=(1<<p)-1;edges=[(i,j) for j in range(p,n) for i in range(j)];m=len(edges);M=[1<<i|1<<j for i,j in edges];B=np.zeros((n,m));
 for e,(i,j) in enumerate(edges):B[[i,j],e]=1
 _,s,V=np.linalg.svd(B,full_matrices=True);Q=V[sum(s>1e-8):];q=len(Q);H=[];counts=[]
 for k in (3,10):
  # Independent sets of the forbidden-prefix-edge graph: fixed blue blocks red cliques, fixed red blocks blue cliques.
  adj=[sum(1<<j for j in range(p) if (i!=j and a[i,j]==(k==10))) for i in range(p)];hist={};
  for b in range(min(p,k)+1):
   for t in sets(adj,F,b):
    if b==k:raise AssertionError('monochromatic fixed clique')
    vs=[i for i in range(p) if t>>i&1];subs=[0,*[1<<v for v in vs],*[1<<v|1<<w for v,w in itertools.combinations(vs,2)]]
    for mask in subs:hist.setdefault(mask,[0]*(k+1))[b]+=1
  @cache
  def entry(f,h):return sum(c*math.comb(n-p-h,k-b-h) for b,c in enumerate(hist.get(f,())) if 0<=k-b-h<=n-p-h)
  counts.append(entry(0,0));G=np.array([[entry((u|v)&F,((u|v)&~F).bit_count()) for u in M] for v in M],dtype=float);H.append(Q@G@Q.T)
 def stats(h):
  w=np.maximum(0,np.linalg.eigvalsh(h)[::-1]);return dict(rank=int(sum(w>w[0]*1e-10)),r95=int(np.searchsorted(np.cumsum(w),.95*w.sum())+1),top=float(w[0]/w.sum()))
 return dict(prefix=p,edges=m,tangent=q,active=counts,raw=stats(H[0]+H[1]),equal_family_energy=stats(H[0]/np.trace(H[0])+H[1]/np.trace(H[1])))
if __name__=='__main__':
 out=[]
 for p in (0,10,20,30,35,37):
  r=measure(p);print(r,flush=True);out.append(r)
 (D/'ramsey310_active_spectrum.json').write_text(json.dumps(out,indent=1))
