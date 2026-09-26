"""Exact ordinary R calibration in momentum-super-twistor coordinates."""
import sympy as s
EPS=s.Matrix([[0,1],[-1,0]])
class Kinematics:
 def __init__(self,rows):
  self.z=[None]+[s.Matrix([r]) for r in rows];self.n=len(rows)
  self.lam={i:self.z[i][:,:2].T for i in range(1,self.n+1)}
  self.X={}
  for i in range(1,self.n+1):
   j=i-1 or self.n
   self.X[i]=s.Matrix.hstack(self.z[j][:,2:].T,self.z[i][:,2:].T)*s.Matrix.hstack(self.lam[j],self.lam[i]).inv()
 def bracket(self,*indices):return s.Matrix.vstack(*(self.z[i] for i in indices)).det()
 def theta(self,row,i,L):
  j=i-1 or self.n;inv=s.Matrix.vstack(self.lam[j].T,self.lam[i].T).inv()
  row[j]+=(L*inv[:,0])[0];row[i]+=(L*inv[:,1])[0]
 def ordinary(self,a,b):
  n=self.n;X=self.X
  L1=self.lam[n].T*(X[n]-X[a]).T*EPS*(X[a]-X[b])*EPS
  L2=self.lam[n].T*(X[n]-X[b]).T*EPS*(X[b]-X[a])*EPS
  row={i:s.S.Zero for i in range(1,n+1)}
  self.theta(row,b,L1);self.theta(row,a,L2);self.theta(row,n,-L1-L2)
  numerator=s.det(s.Matrix.hstack(self.lam[a],self.lam[a-1]))*s.det(s.Matrix.hstack(self.lam[b],self.lam[b-1]))
  denominator=(X[a]-X[b]).det()*(L1*EPS*self.lam[b])[0]*(L1*EPS*self.lam[b-1])[0]*(L2*EPS*self.lam[a])[0]*(L2*EPS*self.lam[a-1])[0]
  if denominator==0:raise ValueError('singular ordinary R')
  return {i:s.factor(v) for i,v in row.items()},s.factor(numerator/denominator)
 def inner(self,a1,b1,a,b,branch):
  n=self.n;X=self.X
  def transported(u,v):return self.lam[n].T*(X[n]-X[u]).T*EPS*(X[u]-X[v])
  if branch=='left-nested':
   anchor=a1;xi=transported(b1,a1)
   def factor(u,v):return xi*EPS*(X[anchor]-X[u]).T*EPS*(X[u]-X[v])*EPS
  elif branch=='right-nested':
   anchor=n
   def factor(u,v):return self.lam[n].T*(X[n]-X[u]).T*EPS*(X[u]-X[v])*EPS
  else:raise ValueError('unknown branch')
  L1,L2=factor(a,b),factor(b,a)
  row={i:s.S.Zero for i in range(1,n+1)}
  self.theta(row,b,L1);self.theta(row,a,L2);self.theta(row,anchor,-L1-L2)
  lower=self.lam[a-1];upper=self.lam[b]
  replacement=(transported(a1,b1)*EPS).T
  if branch=='left-nested' and b==b1:upper=replacement
  if branch=='right-nested' and a==b1:lower=replacement
  numerator=s.det(s.Matrix.hstack(self.lam[a],lower))*s.det(s.Matrix.hstack(upper,self.lam[b-1]))
  denominator=(X[a]-X[b]).det()*(L1*EPS*upper)[0]*(L1*EPS*self.lam[b-1])[0]*(L2*EPS*self.lam[a])[0]*(L2*EPS*lower)[0]
  if denominator==0:raise ValueError('singular inner R')
  return {i:s.factor(v) for i,v in row.items()},s.factor(numerator/denominator)
 def five_bracket(self,a,b):
  seq=(self.n,a-1,a,b-1,b)
  row={i:s.S.Zero for i in range(1,self.n+1)};den=s.S.One
  for k,i in enumerate(seq):
   minor=self.bracket(*(seq[(k+j)%5] for j in range(1,5)))
   row[i]=minor;den*=minor
  if den==0:raise ValueError('singular five bracket')
  return row,1/den
