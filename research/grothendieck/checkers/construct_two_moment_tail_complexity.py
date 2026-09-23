"""Exact 2m-facet family from an admitted face of the owning tail relaxation."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,hashlib
from flint import arb,ctx
ctx.prec=256
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aq(q):return arb(q.numerator)/q.denominator
def interval(z):return aq(Q(z['lower'])).union(aq(Q(z['upper'])))
def enc(z):return {'lower':str(z.lower().fmpq()),'upper':str(z.upper().fmpq())}
def dot(a,b):return sum(x*y for x,y in zip(a,b))
cp=R/'two-moment-tail-complexity-contract.json';contract=load(cp);ch=sha(cp)
bp=R/'directed-C-only-Abel-branch.json';branch=load(bp)
for p,h in branch['bindings'].items():assert sha(Path(p))==h
E=branch['finite_pairing_evidence'];assert E['N']==1000000
C=interval(E['B0'])-interval(E['J_at_64']);assert C<0
log2=arb(2).log();assert arb(1)/2<log2<1 and 100*log2>64
psi=interval(E['psi_N']);psi_upper=Q(E['psi_N']['upper']);assert psi_upper<2**24
assert 2*log2*1000000+arb(1000000).log()+log2>psi
# Universal admission: prefix mass <=P_j=(j+1)(j+100) because log2<1.
# P_0=100, and 4P_j-P_(j+1)=3j^2+301j+198>=0.
# Hence P_j<=100*4^j < (2^100-2^24)*4^j <= n_j-psi(N).
assert 100<2**100-2**24
families=[]
for m in contract['finite_replays']:
 assert m>=2
 caps=[Q(100+2*j) for j in range(m)];slopes=[Q(1,2**(7*j)) for j in range(m)]
 def image(t):return sum(t),dot(slopes,t)
 rows=[];all_endpoints={}
 for j in range(m):
  for sign in (1,-1):
   normal=(-sign*slopes[j],Q(sign))
   t=[caps[i] if dot(normal,(Q(1),slopes[i]))>0 else Q(0) for i in range(m)]
   assert t[j]==0
   p=image(t);u=list(t);u[j]=caps[j];q=image(u)
   bound=sum(caps[i]*max(Q(0),dot(normal,(Q(1),slopes[i]))) for i in range(m))
   assert dot(normal,p)==bound==dot(normal,q) and p!=q
   all_endpoints[p]=tuple(t);all_endpoints[q]=tuple(u)
   rows.append({'generator':j,'orientation':sign,'normal':list(map(str,normal)),'upper':str(bound),'edge_endpoints':[list(map(str,p)),list(map(str,q))],'endpoint_lifts':[list(map(str,t)),list(map(str,u))]})
 assert len(all_endpoints)==2*m
 # Enumerate the halfspace intersection independently of source corner lists.
 H=[(tuple(map(Q,row['normal'])),Q(row['upper'])) for row in rows];hverts=set()
 for (a,b),(c,d) in combinations(H,2):
  determinant=a[0]*c[1]-a[1]*c[0]
  if determinant:
   p=((b*c[1]-a[1]*d)/determinant,(a[0]*d-b*c[0])/determinant)
   if all(dot(n,p)<=v for n,v in H):hverts.add(p)
 assert hverts==set(all_endpoints)
 for i,row in enumerate(rows):
  normal,bound=H[i];p,q=[tuple(map(Q,z)) for z in row['edge_endpoints']];mid=tuple((a+b)/2 for a,b in zip(p,q));eps=Q(1)
  for j,(n,b) in enumerate(H):
   if i==j:continue
   slack=b-dot(n,mid);assert slack>0
   slope=dot(n,normal)
   if slope>0:eps=min(eps,slack/(2*slope))
  witness=tuple(a+eps*b for a,b in zip(mid,normal))
  assert dot(normal,witness)>bound and all(dot(n,witness)<=b for j,(n,b) in enumerate(H) if j!=i)
  row['omission_witness']=list(map(str,witness))
 families.append({'m':m,'caps':list(map(str,caps)),'slopes':list(map(str,slopes)),'facets':rows,'vertex_count':len(all_endpoints),'necessary_and_sufficient_halfspaces':2*m})
out={'schema':'two-moment-tail-complexity.v1','status':'CORROBORATED_FOR_ALL_M_GE_2','contract_sha256':ch,'kernel_suffix_coefficient':enc(C),'psi_upper':str(psi_upper),'admission_induction':{'P_j_coefficients':[100,101,1],'four_P_j_minus_next_coefficients':[198,301,3],'base_exponent':100,'psi_coarse_upper':2**24},'families':families,'bindings':{str(p):sha(p) for p in (Path(__file__),cp,bp)},'scope':'All-m assertion uses the symbolic admission and exposed-edge proof, not extrapolation from finite samples. Exact normalized geometry; no prime-realizability claim.'}
assert sha(cp)==ch
(R/'two-moment-tail-complexity.json').write_text(json.dumps(out,indent=2)+'\n')
print('Constructed exact tail faces and facets:',[(f['m'],len(f['facets'])) for f in families])
