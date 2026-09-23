"""Candidate directed proof 2-cell: postwhiskering closes only up to normalization."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
def valid(p,T):
 a,b,c=map(Q,p);T=Q(T)
 return a>=0 and b>=0 and c>=0 and b-a==1 and b+c==T
def norm(p,T,root='source:[-x<=0,x<=1]'):
 if root!='source:[-x<=0,x<=1]':raise PermissionError('MISSING_PRIMITIVE_SOURCE_ROWS')
 assert valid(p,T)
 a,b,c=map(Q,p);out=(a+c,b+c,Q(0));assert valid(out,T);return out
def post(p,T,U):
 assert Q(U)>=Q(T) and valid(p,T)
 a,b,c=map(Q,p);return (a,b,c+Q(U)-Q(T))
checks=0;strict_fail=0
for T,U,n in product((Q(1),Q(3,2),Q(2),Q(3)),(Q(1),Q(3,2),Q(2),Q(3)),(1,2,3)):
 if U<T:continue
 # Enumerate valid rational original proof with b in [1,T].
 b=Q(1)+(Q(T)-1)*Q(n-1,2) if n in (1,2,3) else Q(1)
 if b>T:continue
 p=(b-1,b,Q(T)-b);assert valid(p,T)
 lhs=norm(post(p,T,U),U)
 rhs=norm(post(norm(p,T),T,U),U)
 assert lhs==rhs==(Q(U)-1,Q(U),Q(0))
 if post(norm(p,T),T,U)!=lhs:strict_fail+=1
 checks+=1
assert checks>10 and strict_fail>0
staged=(Q(1),Q(2),Q(1));assert norm(staged,3)==(Q(2),Q(3),Q(0))
# Postwhisker by x<=4. A strict naturality square fails at intermediate
# certificates, while completing the second path by normalization joins.
assert post(norm(staged,3),3,4)==(2,3,1)
assert norm(post(staged,3,4),4)==(3,4,0)
assert norm(post(norm(staged,3),3,4),4)==(3,4,0)
try:norm(staged,3,root='unrelated-source')
except PermissionError:root_refused=True
else:raise AssertionError('foreign source root admitted')
# A well-founded primitive support DAG is separate from mathematical joining.
primitive={'row:-x<=0','row:x<=1'}
deps={'normalize':{'row:-x<=0','row:x<=1'},'whiskered-comparison':{'normalize','row:x<=1'}}
def rooted(node,links,stack=()):
 if node in stack:return False
 return node in primitive or (node in links and all(rooted(x,links,stack+(node,)) for x in links[node]))
assert rooted('whiskered-comparison',deps)
cyclic={'normalize':{'whiskered-comparison'},'whiskered-comparison':{'normalize'}}
assert not rooted('whiskered-comparison',cyclic)
report={'passed':True,'checked_postwhiskering_squares':checks,'strict_square_failures':strict_fail,'lax_join':'normalize(post(p)) = normalize(post(normalize(p)))','foreign_source_root_refused':root_refused,'rooted_support_dag':True,'scope':'Finite positive postweakenings x<=T to x<=U on fixed primitive interval; candidate directed 2-cell not yet in original Farkas 1-category or authorized operational history.'}
out=Path(__file__).resolve().parents[1]/'results/farkas-comparison-whiskering.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
