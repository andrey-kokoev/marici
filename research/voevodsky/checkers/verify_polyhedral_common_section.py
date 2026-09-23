"""Independent exact vertex and shared-face proof replay; no producer import."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 d=json.loads((OUT/'polyhedral-common-section.json').read_text());r=[Q(1,128**j) for j in range(4)]
 center=[Q(50),Q(51),Q(52),Q(53)];delta=Q(1,128**4)
 def local(x):return ((sum(x)-sum(center))/delta,(sum(a*b for a,b in zip(r,x))-sum(a*b for a,b in zip(r,center)))/delta,(x[0]-50)/delta,(x[1]-51)/delta)
 def admitted(x):return len(x)==4 and all(0<=v<=100+2*j for j,v in enumerate(x))
 expected=[((-1,0,0,0),0),((1,0,0,0),1),((0,-1,0,0),0),((0,1,0,0),1),((0,0,-1,0),0),((0,0,1,0),1),((0,0,0,-1),0),((0,0,0,1),1),((1,0,-1,0),0),((0,1,-1,0),0),((-1,-1,1,0),0)]
 assert d['fine_rows']==[{'normal':list(map(str,a)),'upper':str(b)} for a,b in expected]
 assert {tuple(map(Q,c['local'])) for c in d['admitted_local_cube']}==set(product((Q(0),Q(1)),repeat=4))
 for c in d['admitted_local_cube']:
  x=tuple(map(Q,c['source']));assert admitted(x) and local(x)==tuple(map(Q,c['local']))
 V=[tuple(map(Q,v)) for v in d['public_vertices']];assert V==[(0,0),(1,0),(1,1),(0,1)]
 assert d['triangles']==[[0,1,2],[0,2,3]]
 X=[tuple(map(Q,x)) for x in d['vertex_source_lifts']];assert len(X)==4
 for v,x in zip(V,X):
  assert admitted(x);z=local(x);assert z[:2]==v
  assert all(sum(Q(a)*b for a,b in zip(n,z))<=bound for n,bound in expected)
 # Complete coverage: for q<=p use barycentric (1-p,p-q,q);
 # for p<=q use (1-q,p,q-p). Nonnegative on their domains, sum 1.
 # On p=q both reduce to (1-p)*X0+p*X2, giving exact face agreement.
 controls=0
 for p,q in product((Q(0),Q(1,3),Q(1,2),Q(1)),repeat=2):
  ids,weights=([0,1,2],(1-p,p-q,q)) if q<=p else ([0,2,3],(1-q,p,q-p))
  assert min(weights)>=0 and sum(weights)==1
  x=tuple(sum(w*X[i][j] for i,w in zip(ids,weights)) for j in range(4));z=local(x)
  assert admitted(x) and z==(p,q,max(p,q),Q(0))
  assert all(sum(Q(a)*b for a,b in zip(n,z))<=bound for n,bound in expected);controls+=1
 # Bounds force h=(0,1,1,1) at the four corners, for EVERY section.
 forced=[Q(0),Q(1),Q(1),Q(1)]
 for (p,q),h in zip(V,forced):assert max(p,q)==min(Q(1),p+q)==h
 assert forced[0]+forced[2]!=forced[1]+forced[3]
 result={'passed':True,'vertex_lifts':4,'source_cube_corners':16,'barycentric_controls':controls,
 'continuum_certificate':'Explicit two-triangle cover and common diagonal formula; affine inequalities checked at each vertex.',
 'global_affine_section_impossible':True,'scope':'No general triangulation algorithm or size bound claimed.'}
 (OUT/'polyhedral-common-section-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
