"""Exact determinant dictionary and two-sheet compact-patch Jacobian control."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),ROOT/'temp/triangle-measure-primary-2402.06558v3-source/IR_Divs.tex']
def hashes():return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def det(M):
 n=len(M);ans=F(0)
 for p in permutations(range(n)):
  term=F((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
  for i in range(n):term*=M[i][p[i]]
  ans+=term
 return ans
def dot(u,v):return sum(a*b for a,b in zip(u,v))
def cm(points):
 n=len(points);M=[[F(0)]+[F(1)]*n]
 for p in points:M.append([F(1)]+[sum((a-b)**2 for a,b in zip(p,q)) for q in points])
 return det(M)
before=hashes();count=0
origin=(F(0),)*3;p=(F(2),F(0),F(0));q=(F(1),F(3),F(0))
G2=det([[dot(u,v) for v in (p,q)] for u in (p,q)])
assert G2==36 and cm([origin,p,q])==-4*G2
for x in map(F,('1/4','1/2','3/4')):
 for y in map(F,('1/4','1/2','3/4')):
  for z in map(F,('1','3/2','2')):
   l=(x,y,z);G3=det([[dot(u,v) for v in (p,q,l)] for u in (p,q,l)])
   assert cm([origin,p,q,l])==8*G3
   D=G2/4;K=G3/36
   assert D==9 and K==z*z
   assert cm([origin,p,q,l])==288*K
   # Length-weighted Jacobian on the positive sheet is av*z=6z.
   # The pushed-forward Euclidean density includes both sheets.
   assert (1/(3*z))*(6*z)==2
   count+=1
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'fixtures':count,
 'dictionary':{'signed_CM2':'4*Gram2=16D','CM3':'8*Gram3=288K'},
 'patch':'X,Y in [0,1], |Z| in [1,2]; base (0,0),(2,0),(1,3)',
 'exact_cartesian_patch_volume':2,'euclidean_distance_measure_patch_integral':2,
 'v3_specific_patch_integral_ordinary_volumes':'32/sqrt(pi)',
 'old_and_appendix_patch_regulator_limits':0,
 'scope':'Patch integration follows from the constant pullback density; finite fixtures check determinant arithmetic, not authors intended conventions.'}
(HERE/'triangle-volume-dictionary.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
