"""Glue the one degree-5 panel and the two degree-4 panels over the same ordered neutral pair. Both predictions must agree on the 5-by-8 shared X/Y edges. Output surviving panel assignments for the 9-by-5 residual block. Never require equality between the two different base orders."""
from ramsey_k33_12_mutual import *
from concurrent.futures import ProcessPoolExecutor

def init():
 global DCK
 DCK={(n,d['i'],d['e']):d['panels'] for n,s in [(16,4),(15,5)] for d in json.loads((T/f'k12deck{s}.json').read_text())}
@lru_cache(maxsize=2000)
def panels(n,j,e):return {tuple(sorted(mor(s,p) for s in row)) for row in DCK.get((n,j,e),[]) for p in aut(n,j)}
@lru_cache(maxsize=8192)
def lookup(n,j,e,z):
 idx=collections.defaultdict(list)
 for row in panels(n,j,e):
  desc=tuple((v.bit_count(),sum(((v>>x)&1)<<k for k,x in enumerate(z))) for v in row);idx[tuple(sorted(desc))].append((row,desc))
 return idx
@lru_cache(maxsize=24000)
def choice(n,j,e,z,ds):
 out=[]
 for row,d in lookup(n,j,e,z).get(tuple(sorted(ds)),[]):
  # Match same signatures via permutations of only the tied positions.
  parts=sorted(set(ds));src=[[k for k,v in enumerate(d) if v==s] for s in parts];dst=[[k for k,v in enumerate(ds) if v==s] for s in parts];
  for v in itertools.product(*(itertools.permutations(k) for k in src)):
   x=[0]*len(d)
   for a,b in zip(v,dst):
    for f,t in zip(a,b):x[t]=row[f]
   out.append(tuple(x))
 return out
@lru_cache(maxsize=30000)
def side(n,i,a,b,c):
 h=H[i] if n==16 else J[i];u=a|b|c;z=tuple(k for k in range(n) if not u>>k&1);assert len(z)==2;groups=[tuple(k for k in range(n) if a>>k&1)] if n==16 else [tuple(k for k in range(n) if x&~a&1<<k) for x in (c,b)];ds=[tuple((7-(h[k]&u).bit_count(),sum((h[k]>>v&1)<<t for t,v in enumerate(z))) for k in g) for g in groups];return u,z,groups,ds

def run(t):
 i,j,L,R=t;hi,hj=H[i],J[j];ct=collections.Counter();out=[];audit=[]
 for a,b,c,e in L:
  u,z,U,S=side(16,i,a,b,c)
  for f,g,h,p,q in R:
   v,y,V,F=side(15,j,f,g,h)
   if ((hi[z[0]]>>z[1])^(hj[y[0]]>>y[1]))&1:continue
   for yy in [y,y[::-1]]:
    if any(hi[x].bit_count()+(hj[k]&v).bit_count()!=8 for x,k in zip(z,yy)):continue
    ct['neutral']+=1;X=choice(15,j,e,yy,S[0]);
    if not X:continue
    zz=z if yy==y else z[::-1];Y=choice(16,i,p,zz,F[0]);
    if not Y:continue
    W=choice(16,i,q,zz,F[1]);
    if not W:continue
    ct['three_domains']+=1;idx=[]
    for opts in (Y,W):
     d=collections.defaultdict(list)
     for row in opts:d[tuple(sum((s>>k&1)<<t for t,s in enumerate(row)) for k in U[0])].append(row)
     idx.append(d)
    # Independent encoding of the 40 bits (right-group-major; rows in U[0]).
    def packed(A,us,vs,trans):
     return {sum(1<<(4*k+n) for k,u0 in enumerate(us) for n,v0 in enumerate(vs) if ((r[n]>>u0 if trans else r[k]>>v0)&1)) for r in A}
    LH=[packed(X,U[0],vv,False) for vv in V];RH=[packed(dom,U[0],vv,True) for dom,vv in zip((Y,W),V)];forced=[];block=[]
    for n,(lset,rset) in enumerate(zip(LH,RH)):
     mask=(1<<20)-1;la=ra=mask;lo=ro=0
     for bits in lset:la&=bits;lo|=bits
     for bits in rset:ra&=bits;ro|=bits
     forced.append((la&~ro)|(ra&~lo));block.append(not bool(lset&rset))
    cls='edge' if any(forced) else 'block' if any(block) else 'joint';ct[cls]+=1
    audit.append((i,j,a,b,c,f,g,h,z,yy,cls,forced))
    for row in X:
     hits=[idx[r].get(tuple(sum((s>>k&1)<<t for t,k in enumerate(vs)) for s in row),[]) for r,vs in enumerate(V)]
     for left,right in itertools.product(*hits):
      ct['agree']+=1
      if any(left[t]&right[n] for t,k in enumerate(V[0]) for n,w in enumerate(V[1]) if hj[k]>>w&1):continue
      ct['cross_triangle']+=1;out.append([i,j,[a,b,c],[f,g,h],z,yy,row,left,right])
 return ct,out,audit
if __name__=='__main__':
 data=json.loads((T/'k12mutual.json').read_text());ct=collections.Counter();out=[];audit=[]
 with ProcessPoolExecutor(6,initializer=init) as ex:
  for c,o,a in ex.map(run,data,chunksize=32):ct.update(c);out+=o;audit+=a
 print(ct,flush=True);(P/'ramsey_k33_12_seam.json').write_text(json.dumps(dict(counts=ct,remaining=out,certificates=audit))+'\n')
