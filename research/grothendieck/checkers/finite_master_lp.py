"""Checked fast LP proposal with a finite exact basis fallback.
Contract: the nonnegative-variable LP is nonempty and has a finite optimum.
The fallback is deliberately exhaustive; no practical complexity claim.
"""
if not __debug__:raise RuntimeError('Certificate checks require assertions enabled')
from fractions import Fraction as Q
from itertools import combinations
from exact_master_simplex import maximize as propose

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def checked(A,b,c,answer):
 assert answer['status']=='OPTIMUM';x=tuple(map(Q,answer['point']));w=tuple(map(Q,answer['multipliers']));value=Q(answer['value'])
 assert len(x)==len(c) and len(w)==len(b) and all(v>=0 for v in x+w)
 assert all(dot(a,x)<=bound for a,bound in zip(A,b))
 assert all(sum(weight*a[j] for weight,a in zip(w,A))>=c[j] for j in range(len(c)))
 assert dot(c,x)==dot(b,w)==value

def solve(A,b):
 n=len(b);a=[list(row)+[value] for row,value in zip(A,b)]
 for j in range(n):
  pivot=next((i for i in range(j,n) if a[i][j]),None)
  if pivot is None:return None
  a[j],a[pivot]=a[pivot],a[j];v=a[j][j];a[j]=[x/v for x in a[j]]
  for i in range(n):
   if i!=j:
    v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
 return tuple(row[-1] for row in a)

def maximize(A,b,c,proposer=propose):
 A=[tuple(map(Q,row)) for row in A];b=tuple(map(Q,b));c=tuple(map(Q,c));n=len(c)
 assert len(A)==len(b) and all(len(row)==n for row in A)
 failure='DISABLED'
 if proposer is not None:
  try:
   answer=proposer(A,b,c);checked(A,b,c,answer);return {**answer,'master_method':'CHECKED_PROPOSAL'}
  except Exception as error:failure=type(error).__name__
 normals=A+[tuple(-Q(int(i==j)) for j in range(n)) for i in range(n)];bounds=b+(Q(0),)*n;attempts=0
 for indices in combinations(range(len(normals)),n):
  attempts+=1;basis=[normals[i] for i in indices];x=solve(basis,[bounds[i] for i in indices])
  if x is None or any(dot(a,x)>bound for a,bound in zip(normals,bounds)):continue
  y=solve(list(zip(*basis)),c)
  if y is None or any(v<0 for v in y):continue
  w=[Q(0)]*len(A)
  for i,v in zip(indices,y):
   if i<len(A):w[i]=v
  answer={'status':'OPTIMUM','point':list(map(str,x)),'value':str(dot(c,x)),'multipliers':list(map(str,w)),'master_method':'FINITE_BASIS_FALLBACK','proposal_failure':failure,'bases_examined':attempts}
  checked(A,b,c,answer);return answer
 raise RuntimeError('BOUNDED_NONEMPTY_MASTER_CONTRACT_NOT_ESTABLISHED')
