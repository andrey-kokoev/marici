"""Polyhedral relative residues and Farkas/base-change coherence.
Four composable presentation arrows yield a checked 4-simplex. Appending one
fine row gives a natural forgetful comparison, hence a categorical prism.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def mat(rows):return tuple(tuple(map(Q,r)) for r in rows)
def mv(A,x):return tuple(sum(a*b for a,b in zip(r,x)) for r in A)
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def eye(n):return mat([[int(i==j) for j in range(n)] for i in range(n)])
def check(obj,target,arrow):
 A,r,s=obj;B,u,t=target;M,d,c=arrow
 assert len(M)==len(B) and all(len(row)==len(A) for row in M)
 assert len(d)==len(s) and len(c)==len(B) and all(x>=0 for row in M for x in row) and all(x>=0 for x in c)
 assert B==mm(M,A) and t==add(s,d)
 assert u==add(sub(mv(M,r),mv(B,d)),c)
def step(obj,M,d,c=None):
 A,r,s=obj;B=mm(M,A);c=tuple(Q(0) for _ in B) if c is None else c
 target=(B,add(sub(mv(M,r),mv(B,d)),c),add(s,d));arrow=(M,d,c)
 check(obj,target,arrow);return target,arrow
def compose(first,second):
 M,d,c=first;N,e,k=second
 return mm(N,M),add(d,e),add(mv(N,c),k)
def fold(arrows):
 out=arrows[0]
 for a in arrows[1:]:out=compose(out,a)
 return out
def all_brackets(arrows):
 if len(arrows)==1:return [arrows[0]]
 return [compose(a,b) for i in range(1,len(arrows)) for a in all_brackets(arrows[:i]) for b in all_brackets(arrows[i:])]
def refine(obj,normal,bound):
 A,r,s=obj
 return A+(normal,),r+(bound-sum(x*y for x,y in zip(normal,s)),),s
def extend(arrow):
 M,d,c=arrow;n=len(M[0]);return tuple(row+(Q(0),) for row in M)+(tuple(Q(0) for _ in range(n))+(Q(1),),),d,c+(Q(0),)
def forget(obj):
 n=len(obj[0]);return tuple(tuple(Q(int(i==j)) for j in range(n+1)) for i in range(n)),tuple(Q(0) for _ in obj[2]),tuple(Q(0) for _ in range(n))
def encode_obj(obj):
 A,r,s=obj;return {'normals':[[str(x) for x in a] for a in A],'residual':list(map(str,r)),'reference':list(map(str,s))}
def main():
 if not __debug__:raise RuntimeError('Assertions required')
 # All presentations describe 0<=h,k and h+k<=1; extra rows are redundant.
 obj=(mat([[-1,0],[0,-1],[1,1]]),(Q(0),Q(0),Q(1)),(Q(0),Q(0)))
 Ms=[mat([[1,0,0],[0,1,0],[0,0,1],[0,1,1],[1,0,1]]),
 mat([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0]]),mat([[0,1,0],[0,0,1],[1,0,0]]),mat([[0,0,1],[1,0,0],[0,1,0]])]
 shifts=[(Q(1,4),Q(1,4)),(Q(1,4),Q(-1,4)),(Q(-1,2),Q(1,4)),(Q(0),Q(-1,4))]
 objects=[obj];arrows=[]
 for M,d in zip(Ms,shifts):
  obj,a=step(obj,M,d);objects.append(obj);arrows.append(a)
 assert objects[-1]==objects[0]
 brackets=all_brackets(arrows);assert len(brackets)==5 and all(a==brackets[0] for a in brackets)
 assert brackets[0]==(eye(3),(Q(0),Q(0)),(Q(0),Q(0),Q(0)))
 # All ten edges and ten triangular face laws of the nerve 4-simplex.
 edges={};triangles=0
 for i in range(5):
  for j in range(i+1,5):
   edges[i,j]=fold(arrows[i:j]);check(objects[i],objects[j],edges[i,j])
 for i in range(5):
  for j in range(i+1,5):
   for k in range(j+1,5):assert compose(edges[i,j],edges[j,k])==edges[i,k];triangles+=1
 # Add the SAME physical bound h<=1/2 at every reference, not the same
 # untransported residual constant. Forgetful squares commute certificate-wise.
 normal=(Q(1),Q(0));bound=Q(1,2);refined=[refine(o,normal,bound) for o in objects];squares=0
 for (i,j),a in edges.items():
  lifted=extend(a);check(refined[i],refined[j],lifted)
  fi,fj=forget(objects[i]),forget(objects[j]);check(refined[i],objects[i],fi);check(refined[j],objects[j],fj)
  assert compose(lifted,fj)==compose(fi,a);squares+=1
 # Explicit staircase triangulation of Delta^1 x Delta^4: move along
 # refined edges to pivot k, forget there, then traverse original edges.
 prism_brackets=0;reference=None
 for k in range(5):
  chain=[extend(a) for a in arrows[:k]]+[forget(objects[k])]+arrows[k:]
  composites=all_brackets(chain);assert len(composites)==14
  endpoint=fold(chain);check(refined[0],objects[-1],endpoint)
  assert all(a==endpoint for a in composites);prism_brackets+=len(composites)
  if reference is None:reference=endpoint
  else:assert endpoint==reference
 # A nonzero Farkas surplus also composes; the law is not limited to equality.
 loose,a=step(objects[0],eye(3),(Q(0),Q(0)),(Q(0),Q(0),Q(1)))
 looser,b=step(loose,eye(3),(Q(1,4),Q(0)),(Q(0),Q(0),Q(1)))
 check(objects[0],looser,compose(a,b))
 rejected=[]
 bad=(arrows[0][0],arrows[0][1],(Q(-1),)+arrows[0][2][1:])
 try:check(objects[0],objects[1],bad)
 except AssertionError:rejected.append('negative-surplus')
 else:raise AssertionError('invalid surplus accepted')
 # Appending an untranslated h-bound after changing reference is wrong.
 wrong=(refined[1][0],objects[1][1]+(bound,),objects[1][2])
 try:check(refined[0],wrong,extend(arrows[0]))
 except AssertionError:rejected.append('untransported-fine-bound')
 else:raise AssertionError('wrong bound accepted')
 report={'passed':True,'presentations':[encode_obj(o) for o in objects],
 'nerve_4_simplex':{'vertices':5,'edges':len(edges),'triangle_equalities':triangles,'four_arrow_parenthesizations':len(brackets)},
 'refinement_prism':{'natural_squares':squares,'staircase_5_simplices':5,'checked_five_arrow_parenthesizations':prism_brackets,
 'meaning':'Natural forgetful transformation between original and refined presentation chains; dimension is simplicial, not fiber dimension.'},
 'rejections':rejected,
 'scope':'Exact Farkas/base-change category for polyhedral constraints. No analytic residue-jet identification, authority issuance, or old five-cone identification.'}
 (OUT/'polyhedral-residue-coherence.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ('passed','nerve_4_simplex','refinement_prism','rejections')},indent=2))
if __name__=='__main__':main()
