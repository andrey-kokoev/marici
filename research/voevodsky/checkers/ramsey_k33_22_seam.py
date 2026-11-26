"""Match the marked 3-vertex neutral seam by induced graph, final degree 8, and four catalogue panels. A four-single panel on the first side must extend the SAME 16-graph of the second; its supports' intersections with the three shared vertices and sizes are already prescribed. Keep all ways to attach each panel and require the four induced 4x4 blocks to agree transposed. Emit remaining cases for exact SAT (no absent panel assumed)."""
from ramsey_k33_22_mutual import *
from concurrent.futures import ProcessPoolExecutor
@lru_cache(None)
def panels(j,e):
 data=DCK.get((j,e),[]);return {tuple(sorted(morph(s,p) for s in row)) for row in data for p in autos(j)}
@lru_cache(maxsize=10000)
def lookup(j,e,z):
 out=collections.defaultdict(list)
 for row in panels(j,e):
  desc=tuple((s.bit_count(),tuple((s>>i)&1 for i in z)) for s in row);out[tuple(sorted(desc))].append((row,desc))
 return out
@lru_cache(maxsize=20000)
def side(i,a,b,c):
 h=H[i];u=a|b|c;z=tuple(j for j in range(16) if not u>>j&1);sets=tuple(tuple(j for j in range(16) if s&~a&1<<j) for s in (b,c));sig=tuple(tuple((7-(h[j]&u).bit_count(),tuple((h[j]>>k)&1 for k in z)) for j in group) for group in sets);return u,z,sets,sig

def generate(i,j,L,R):
 cnt=collections.Counter();out=[];hi,hj=H[i],H[j]
 for l in L:
  a,b,c,e,f=l;u,z,U,S=side(i,a,b,c);G=[(e,U[1],S[1]),(f,U[0],S[0])];# e is the pair (a,b) and describes remaining single group c
  for r in R:
   if i==j and tuple(l)>tuple(r):continue
   d,g,h,p,q=r;v,t,V,J=side(j,d,g,h)
   for t1 in itertools.permutations(t):
    if any(hi[x].bit_count()+(hj[y]&v).bit_count()!=8 for x,y in zip(z,t1)):continue
    if any(((hi[z[k]]>>z[n])^(hj[t1[k]]>>t1[n]))&1 for k,n in comb(range(3),2)):continue
    cnt['neutral']+=1;inv=tuple(t1.index(x) for x in t);K=[(p,V[1],J[1]),(q,V[0],J[0])];domains=[]
    for jj,zz,gr in [(j,t1,G),(i,tuple(z[k] for k in inv),K)]:
     for ee,xs,ss in gr:
      opts=lookup(jj,ee,zz).get(tuple(sorted(ss)),[])
      if not opts:break
      ds=[]
      for row,sig in opts:
       for per in itertools.permutations(range(4)):
        if all(sig[k]==ss[n] for n,k in enumerate(per)):ds.append(tuple(row[k] for k in per))
      domains.append(ds)
     else:continue
     break
    if len(domains)!=4:continue
    cnt['four_domains']+=1;out.append(dict(candidate=[i,j,l,r,z,t1],domains=domains,groups=[G[0][1],G[1][1],K[0][1],K[1][1]]))
    # Compare both sides' matrices on their 8 single-only vertices (relative to z/t1 identification).
    def sub(x,vs):return tuple(tuple((s>>k)&1 for k in vs) for s in x)
    trans=lambda M:tuple(zip(*M));left=[[(sub(x,K[0][1]),sub(x,K[1][1]),x) for x in dom] for dom in domains[:2]];right=[collections.defaultdict(list),collections.defaultdict(list)]
    for n,dom in enumerate(domains[2:]):
     for y in dom:right[n][(trans(sub(y,G[0][1])),trans(sub(y,G[1][1])))].append(y)
    for A,C0,X in left[0]:
     for B,D0,Y in left[1]:
      for W in right[0].get((A,B),[]):
       for Z in right[1].get((C0,D0),[]):
        cnt['agreed']+=1
 return cnt,out

def init():
 global DCK
 DCK={(d['i'],d['e']):d['panels'] for d in json.loads((T/'k22deck.json').read_text())}
def task(r):return generate(*r)
if __name__=='__main__':
 data=json.loads((T/'k22mutual.json').read_text());cnt=collections.Counter();out=[]
 with ProcessPoolExecutor(8,initializer=init) as ex:
  for c,o in ex.map(task,data,chunksize=8):cnt.update(c);out+=o
 print(cnt,flush=True);(P/'ramsey_k33_22_seam.json').write_text(json.dumps(dict(counts=cnt,locally_supported=out))+'\n')
