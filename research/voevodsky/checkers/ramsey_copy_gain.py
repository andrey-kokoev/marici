"""Frozen constructor: keep supplied core C unchanged, add a root and a blue set of newcomers whose red supports are distinct old vertices' open red neighborhoods. Optimize only over those centers. Inputs are predecessor graphs, never endpoints. Output orders give lower bounds, not upper bounds on unrestricted Ramsey numbers."""
import itertools,json,sys
from ramsey_retention_slice import CAT,D,decode
sys.path.insert(0,str(D.parents[2]/'grothendieck'))
from r312_google_extension import adj as large
P=D.parent
def trial(a,k):
 n=len(a);F=(1<<n)-1
 def blue(p,k,s=0):
  if not k:yield s;return
  while p.bit_count()>=k:
   b=p&-p;p^=b;yield from blue(p&~a[b.bit_length()-1],k-1,s|b)
 assert next(blue(F,k),None) is None and not any(a[i]&a[j] for i,j in itertools.combinations(range(n),2) if a[i]>>j&1)
 # A maximum-size (k-1)-clique containing two centers misses both copied neighborhoods. Exclude those pairs before checking smaller-clique obstructions.
 compat=[F^1<<i for i in range(n)];count=0
 for q in blue(F,k-1):
  count+=1;p=q
  while p:b=p&-p;p^=b;compat[b.bit_length()-1]&=~q
 def valid(t):
  for j in range(1,len(t)+1):
   for u in itertools.combinations(t,j):
    p=F
    for i in u:p&=~a[i]
    if next(blue(p,k+1-j),None) is not None:return False
  return True
 best=[]
 def search(p,t):
  nonlocal best
  if len(t)>len(best):best=t
  while len(t)+p.bit_count()>len(best):
   b=p&-p;p^=b;i=b.bit_length()-1;u=t+[i]
   if len(u)<=k and valid(u):search(p&compat[i],u)
 search(F,[]);return dict(n=n,cliques=count,allowed_pairs=sum(v.bit_count() for v in compat)//2,red_pairs=sum(v.bit_count() for v in a)//2,centers=best,witness_order=n+1+len(best),threshold_lower=n+2+len(best))
out={}
for k,file in [(4,'r34_8.g6'),(5,'r35_13.g6'),(6,'r36_17.g6'),(12,None)]:
 graphs=[decode(s) for s in (CAT/file).read_text().splitlines()] if file else [large];rs=[trial(a,k) for a in graphs];out[k+1]=rs;print(k+1,len(rs),[(r['threshold_lower'],r['allowed_pairs']-r['red_pairs']) for r in rs],flush=True)
(P/'ramsey_copy_gain.json').write_text(json.dumps(out)+'\n')
