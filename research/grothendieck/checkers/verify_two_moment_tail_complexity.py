"""Independent exact geometry and owning suffix/admission verification."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,hashlib,copy
from flint import arb,ctx
ctx.prec=512
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aq(q):return arb(q.numerator)/q.denominator
def dot(a,b):return sum(x*y for x,y in zip(a,b))
r=load(R/'two-moment-tail-complexity.json');cp=R/'two-moment-tail-complexity-contract.json';contract=load(cp)
for p,h in r['bindings'].items():assert sha(Path(p))==h
assert sha(cp)==r['contract_sha256']
branch=load(R/'directed-C-only-Abel-branch.json')
for p,h in branch['bindings'].items():assert sha(Path(p))==h
E=branch['finite_pairing_evidence'];assert E['N']==1000000
# Recompute the suffix coefficient directly from the owning linear hats,
# without importing the pairing engine or the producer.
f=load(R/'time-bin-cubic-observer.json')['filters']
def rat(pair):return aq(Q(int(pair[0]),int(pair[1])))
ts=list(map(rat,f['nodes']));vals=[]
for side in (0,1):
 z=f['bulk'][side];vals.append([arb(int(n))/int(f['nodal_denominator'])/rat(z['normalizer']) for n in z['nodal_numerators']])
assert ts[0]==0 and ts[-1]==64 and vals[0][-1]==vals[1][-1]==0
B=arb(0);J=arb(0)
for i,(lo,hi) in enumerate(zip(ts,ts[1:])):
 p,z=vals[0][i:i+2];slope=(z-p)/(hi-lo)
 B+=(-4*lo).exp()*(p/4+slope/16)-(-4*hi).exp()*(z/4+slope/16)
 p,z=vals[1][i:i+2];slope=(z-p)/(hi-lo)
 J+=(2*hi).exp()*(z/2-slope/4)-(2*lo).exp()*(p/2-slope/4)
C=B-J;assert C<0
assert aq(Q(r['kernel_suffix_coefficient']['lower']))<C<aq(Q(r['kernel_suffix_coefficient']['upper']))
ln2=arb(2).log();assert arb(1)/2<ln2<1 and 100*ln2>64
psi=Q(E['psi_N']['upper']);assert psi==Q(r['psi_upper'])<2**24
assert 2*ln2*1000000+arb(1000000).log()+ln2>aq(psi)
# Exact polynomial certificate for all j>=0, not a sampled inequality.
p=list(map(Q,r['admission_induction']['P_j_coefficients']));a,b,c=p
nextp=[a+b+c,b+2*c,c];diff=[4*v-w for v,w in zip(p,nextp)]
assert p==[100,101,1] and diff==[198,301,3]==r['admission_induction']['four_P_j_minus_next_coefficients'] and all(v>=0 for v in diff)
assert 100<2**100-2**24

def verify_family(family):
 m=family['m'];caps=list(map(Q,family['caps']));slopes=list(map(Q,family['slopes']))
 assert m>=2 and caps==[Q(100+2*j) for j in range(m)]
 assert slopes[0]==1 and all(slopes[j+1]==slopes[j]/128 for j in range(m-1))
 assert all(v>0 for v in caps) and all(a>b>0 for a,b in zip(slopes,slopes[1:]))
 rows=family['facets'];assert len(rows)==2*m
 endpoints=set();facets=[];directions=set()
 for row in rows:
  j=row['generator'];sign=row['orientation'];assert (j,sign) not in directions;directions.add((j,sign));assert sign in (-1,1)
  normal=tuple(map(Q,row['normal']));bound=Q(row['upper']);assert normal==(-sign*slopes[j],Q(sign))
  coefficients=[normal[0]+normal[1]*v for v in slopes]
  assert coefficients[j]==0 and all(v!=0 for i,v in enumerate(coefficients) if i!=j)
  assert bound==sum(cap*max(Q(0),v) for cap,v in zip(caps,coefficients))
  pts=[]
  for raw,t_raw in zip(row['edge_endpoints'],row['endpoint_lifts']):
   point=tuple(map(Q,raw));t=list(map(Q,t_raw));assert len(t)==m
   assert all(0<=a<=cap for a,cap in zip(t,caps))
   assert point==(sum(t),dot(slopes,t)) and dot(normal,point)==bound
   # For all other atoms the exposing functional forces a unique endpoint.
   assert all(t[i]==(caps[i] if coefficients[i]>0 else 0) for i in range(m) if i!=j)
   endpoints.add(point);pts.append(point)
  assert pts[0]!=pts[1];facets.append((normal,bound))
 assert directions==set((j,s) for j in range(m) for s in (-1,1))
 # Distinct generator slopes imply distinct exposed edge directions.
 assert len(endpoints)==family['vertex_count']==2*m
 # Two nonparallel pairs of opposite normals bound the intersection.
 n0=facets[0][0];n1=facets[2][0];assert n0[0]*n1[1]!=n0[1]*n1[0]
 vertices=set()
 for (a,b),(c,d) in combinations(facets,2):
  denominator=c[1]-c[0]*a[1]/a[0]
  if denominator:
   y=(d-c[0]*b/a[0])/denominator;x=(b-a[1]*y)/a[0];point=(x,y)
   if all(dot(n,point)<=v for n,v in facets):vertices.add(point)
 assert vertices==endpoints
 for i,(row,(n,b)) in enumerate(zip(rows,facets)):
  witness=tuple(map(Q,row['omission_witness']))
  assert dot(n,witness)>b and all(dot(nn,witness)<=bb for j,(nn,bb) in enumerate(facets) if j!=i)
 assert family['necessary_and_sufficient_halfspaces']==2*m
for f in r['families']:verify_family(f)
assert [f['m'] for f in r['families']]==contract['finite_replays']
bad=copy.deepcopy(r['families'][0]);bad['facets'][0]['upper']=str(Q(bad['facets'][0]['upper'])+1)
try:verify_family(bad)
except AssertionError:pass
else:raise AssertionError('invalid support facet accepted')
assert r['status']=='CORROBORATED_FOR_ALL_M_GE_2'
print('PASS: independently recomputed owning suffix, uniform admission induction, exact normalized slopes, complete 2m-facet geometry, source lifts, separating queries and corruption rejection')
