"""Expansion of red graphs, not complements. Exact on named small witnesses/catalogues. For 52 give certified Laplacian lower and explicit cut upper. CLI: optimized ramsey_edge_expansion binary."""
from pathlib import Path
import json,sys,subprocess,collections,random,math
from fractions import Fraction
import numpy as np
from ramsey_retention_slice import CAT,D,decode
P=D.parent;records={};slices=json.loads(D.read_text());out={}
for r in slices:records[str((r['l'],r['k']))]=decode(r['graph6'])
records['(3, 3)']=[1<<((i+1)%5)|1<<((i-1)%5) for i in range(5)];sq={i*i%17 for i in range(1,17)};records['(4, 4)']=[sum(1<<j for j in range(17) if (i-j)%17 in sq) for i in range(17)]
def run(gs):
 lines=subprocess.check_output([sys.argv[1]],input=''.join(' '.join(map(str,a))+'\n' for a in gs),text=True).splitlines();rs=[]
 for a,l in zip(gs,lines,strict=True):
  cut,d,s=map(int,l.split());n=len(a);assert cut==sum((v&~s).bit_count() for i,v in enumerate(a) if s>>i&1) and d==min(s.bit_count(),n-s.bit_count());rs.append(dict(n=n,h=str(Fraction(cut,d)),cut=cut,den=d,mask=s))
 return rs
for k,a in records.items():out[k]=run([a])[0];out[k]['adj']=a;print(k,out[k]['h'],flush=True)
hists={}
for f in ('r34_8','r35_13','r36_17','r37_22'):
 gs=[decode(s) for s in (CAT/(f+'.g6')).read_text().splitlines()];hist=collections.Counter(r['h'] for r in run(gs));hists[f]=hist;print(f,hist,flush=True)
sys.path.insert(0,str(D.parents[2]/'grothendieck'));from r312_google_extension import adj as a
n=len(a);L=np.diag([v.bit_count() for v in a])-np.array([[v>>j&1 for j in range(n)] for v in a]);t=math.floor(1000*np.linalg.eigvalsh(L)[1])-1;H=((L+1)*1000-t*np.eye(n,dtype=int)).tolist();prev=1
for i in range(n):
 pivot=H[i][i];assert pivot>0
 for j in range(i+1,n):
  for k in range(i+1,n):H[j][k]=(pivot*H[j][k]-H[j][i]*H[i][k])//prev
 prev=pivot
rng=random.Random(52);upper=Fraction(n);w=None
for d in range(20,27):
 for rep in range(80):
  s=sum(1<<i for i in rng.sample(range(n),d));
  while True:
   c=[v.bit_count()-2*(v&s).bit_count() for v in a];delta,i,j=min((c[j]-c[i]+2*((a[j]>>i)&1),i,j) for i in range(n) if s>>i&1 for j in range(n) if not s>>j&1)
   if delta>=0:break
   s^=1<<i|1<<j
  size=sum((v&~s).bit_count() for i,v in enumerate(a) if s>>i&1);val=Fraction(size,d)
  if val<upper:upper=val;w=s
lo=min(Fraction((t*d*(n-d))//(1000*n)+1,d) for d in range(1,27));out['(3, 12)']=dict(n=n,lambda2_gt=str(Fraction(t,1000)),lower=str(lo),upper=str(upper),mask=w);print(out['(3, 12)']);(P/'ramsey_expansion_witnesses.json').write_text(json.dumps(dict(representatives=out,catalogues=hists))+'\n')
