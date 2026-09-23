"""Exact two-phase simplex with Bland's rule; bounded feasible master contract."""
from fractions import Fraction as Q

def maximize(A,b,c):
 A=[list(map(Q,row)) for row in A];b=list(map(Q,b));c=list(map(Q,c));m=len(b);n=len(c)
 assert m==len(A) and all(len(row)==n for row in A)
 negative=[i for i,v in enumerate(b) if v<0];N=n+m+len(negative);table=[];rhs=[];basis=[]
 for i,(row,value) in enumerate(zip(A,b)):
  sign=Q(1 if value>=0 else -1);t=[sign*v for v in row]+[Q(0)]*(N-n);t[n+i]=sign
  if value<0:
   k=n+m+negative.index(i);t[k]=Q(1);basis.append(k)
  else:basis.append(n+i)
  table.append(t);rhs.append(sign*value)
 pivots=0
 def pivot(i,j):
  nonlocal pivots
  value=table[i][j];table[i]=[v/value for v in table[i]];rhs[i]/=value
  for k in range(len(table)):
   if k!=i:
    value=table[k][j];table[k]=[a-value*b for a,b in zip(table[k],table[i])];rhs[k]-=value*rhs[i]
  basis[i]=j;pivots+=1;assert all(v>=0 for v in rhs)
 def optimize(cost):
  while True:
   reduced=[cost[j]-sum(cost[basis[i]]*table[i][j] for i in range(len(table))) for j in range(len(cost))]
   entering=next((j for j,v in enumerate(reduced) if v>0),None)
   if entering is None:return sum(cost[k]*v for k,v in zip(basis,rhs))
   eligible=[i for i in range(len(table)) if table[i][entering]>0]
   if not eligible:raise RuntimeError('UNBOUNDED_MASTER')
   leaving=min(eligible,key=lambda i:(rhs[i]/table[i][entering],basis[i]));pivot(leaving,entering)
 phase1=[Q(0)]*(n+m)+[-Q(1)]*len(negative)
 if optimize(phase1)!=0:raise RuntimeError('NONEMPTY_MASTER_CONTRACT_VIOLATED')
 # Zero artificial basics may pivot out with either coefficient sign.
 i=0
 while i<len(basis):
  if basis[i]>=n+m:
   assert rhs[i]==0
   entering=next((j for j in range(n+m) if j not in basis and table[i][j]),None)
   if entering is None:table.pop(i);rhs.pop(i);basis.pop(i);continue
   pivot(i,entering)
  i+=1
 table[:]=[row[:n+m] for row in table];cost=c+[Q(0)]*m;value=optimize(cost)
 x=[Q(0)]*n
 for k,v in zip(basis,rhs):
  if k<n:x[k]=v
 # Slack columns are the accumulated original-row transformations.
 weights=[sum(cost[basis[i]]*table[i][n+j] for i in range(len(table))) for j in range(m)]
 return {'status':'OPTIMUM','point':list(map(str,x)),'value':str(value),'multipliers':list(map(str,weights)),'simplex_pivots':pivots}
