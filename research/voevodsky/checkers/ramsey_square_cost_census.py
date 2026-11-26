"""Exact cost distributions and replay representative endpoints with independent clique checks. Compare with the unconditional +3 construction (copy two red-adjacent centers and add a root)."""
import json,gzip,sys,itertools,subprocess,collections
from ramsey_retention_slice import CAT,D,decode,check
sys.path.insert(0,str(D.parents[2]/'grothendieck'));from r312_google_extension import adj as big
P=D.parent
def enc(a):
 bits=''.join(str(a[i]>>j&1) for j in range(len(a)) for i in range(j));bits+='0'*(-len(bits)%6);return chr(63+len(a))+''.join(chr(63+int(bits[j:j+6],2)) for j in range(0,len(bits),6))
out={}
for k,src in [(7,(CAT/'r37_22.g6').read_text().splitlines()),(8,gzip.open(CAT/'r38_27.g6.gz','rt')),(9,[r['graph6'] for r in json.loads(D.read_text()) if r['l']==3 and r['k']==9]),(12,[enc(big)])]:
 it=iter(src);hist=collections.Counter();extra=collections.Counter();samples={};idx=0
 while True:
  batch=[s.strip() for s in itertools.islice(it,4096)]
  if not batch:break
  lines=subprocess.check_output([sys.argv[1],str(k)],input='\n'.join(batch)+'\n',text=True).splitlines();assert len(lines)==len(batch)
  for s,line in zip(batch,lines):
   lo,d,x,y,cut=map(int,line.split());hist[d]+=1;extra[d-lo]+=1
   if d not in samples and d>=0:
    a=decode(s);n=len(a);u,w=[j for j in range(n) if x>>j&1];v,z=[j for j in range(n) if y>>j&1];c=(u,v,w,z);g=a.copy()+[0]*5
    for j in range(4):
     h=n+j;t=(a[c[(j+2)%4]]|1<<c[(j+1)%4])&~cut;g[h]=t|1<<(n+4);g[n+4]|=1<<h
     for i in range(n):g[i]|=(t>>i&1)<<h
    assert check(g,((1<<len(g))-1)&~cut,3,k+1);samples[d]=dict(index=idx,graph6=s,corners=c,deletion=cut)
   idx+=1
 out[k]=dict(costs=hist,excess_over_min_overlap=extra,samples=samples);print(k,hist,extra,flush=True)
(P/'ramsey_square_cost_census.json').write_text(json.dumps(out)+'\n')
