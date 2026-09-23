"""Exact finite-dictionary interface for variable audit values.
Source: t_j in [0,100+2j], moments (sum t, sum 128^-j t).
"""
from fractions import Fraction as Q
from sympy import Rational
from sympy.solvers.simplex import linprog,InfeasibleLPError

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sp(x):return Rational(x.numerator,x.denominator)
def lp(A,b,c):
 """Maximize c.x, x>=0; exact checked optimum or Farkas packet."""
 d=len(c);AA=[list(map(sp,row)) for row in A];bb=list(map(sp,b))
 try:
  v,p=linprog([-sp(x) for x in c],AA,bb);p=list(map(lambda x:Q(str(x)),p))
  if not (all(x>=0 for x in p) and all(dot(a,p)<=v for a,v in zip(A,b))):raise InfeasibleLPError('unchecked optimizer candidate')
 except InfeasibleLPError:
  _,y=linprog([0]*len(b),[[-sp(A[i][j]) for i in range(len(b))] for j in range(d)]+[bb],[0]*d+[-1])
  y=list(map(lambda x:Q(str(x)),y));assert all(x>=0 for x in y) and all(sum(A[i][j]*y[i] for i in range(len(b)))>=0 for j in range(d)) and dot(b,y)<0
  return {'status':'INCONSISTENT','multipliers':list(map(str,y))}
 _,y=linprog(bb,[[-sp(A[i][j]) for i in range(len(b))] for j in range(d)],[-sp(x) for x in c]);y=list(map(lambda x:Q(str(x)),y))
 assert all(x>=0 for x in y) and all(sum(A[i][j]*y[i] for i in range(len(b)))>=c[j] for j in range(d))
 assert dot(c,p)==dot(b,y)
 return {'status':'OPTIMUM','point':list(map(str,p)),'value':str(dot(c,p)),'multipliers':list(map(str,y))}

class JointAuditModel:
 def __init__(self,m,audits):
  if m<2 or len(set(audits))!=len(audits) or any(type(j)!=int or not 0<=j<m for j in audits):raise ValueError('INVALID_SCHEMA')
  self.m=m;self.audits=tuple(sorted(audits));self.free=tuple(j for j in range(m) if j not in self.audits);self.d=2+len(audits)
  self.caps=[Q(100+2*j) for j in range(m)];self.slopes=[Q(1,128**j) for j in range(m)]
 def observe(self,t):return (sum(t),dot(self.slopes,t),*[t[j] for j in self.audits])
 def pullback(self,a):return [a[0]+a[1]*self.slopes[j]+sum(a[2+k] for k,i in enumerate(self.audits) if i==j) for j in range(self.m)]
 def shear_row(self,a,b):return tuple([a,b]+[-a-b*self.slopes[j] for j in self.audits])
 def bound(self,row):return sum(cap*max(Q(0),v) for cap,v in zip(self.caps,self.pullback(row)))
 def cuts(self):
  """Stream a fixed schema dictionary; ids, not rescalings, mark progress."""
  for k,j in enumerate(self.audits):
   for sign in (-1,1):
    row=tuple(Q(sign if n==k+2 else 0) for n in range(self.d));yield f'audit:{j}:{sign}',(row,self.bound(row))
  q=len(self.free)
  if q>=2:
   for j in self.free:
    for sign in (-1,1):
     row=self.shear_row(-sign*self.slopes[j],Q(sign));yield f'edge:{j}:{sign}',(row,self.bound(row))
   for sign in (-1,1):
    row=self.shear_row(Q(sign),Q(0));yield f'mass:{sign}',(row,self.bound(row))
  elif q==1:
   j=self.free[0]
   for sign in (-1,1):
    row=self.shear_row(Q(sign),Q(0));yield f'mass:{sign}',(row,self.bound(row))
    row=self.shear_row(-sign*self.slopes[j],Q(sign));yield f'equality:{sign}',(row,Q(0))
  else:
   for i in (0,1):
    for sign in (-1,1):
     row=self.shear_row(Q(sign if i==0 else 0),Q(sign if i==1 else 0));yield f'equality:{i}:{sign}',(row,Q(0))
 def dictionary_size(self):return 2*self.m+(4 if not self.free else 2)
 def cut(self,name):
  return next(row for key,row in self.cuts() if key==name)
 def source_lift(self,y):
  if len(y)!=self.d:raise ValueError('SCHEMA_MISMATCH')
  pins=dict(zip(self.audits,y[2:]))
  if any(not 0<=v<=self.caps[j] for j,v in pins.items()):return None
  U=y[0]-sum(pins.values());V=y[1]-sum(self.slopes[j]*v for j,v in pins.items());total=sum(self.caps[j] for j in self.free)
  if not 0<=U<=total:return None
  def greedy(order):
   rem=U;t={}
   for j in order:t[j]=min(rem,self.caps[j]);rem-=t[j]
   return t,sum(self.slopes[j]*t[j] for j in self.free)
  high,H=greedy(self.free);low,L=greedy(reversed(self.free))
  if not L<=V<=H:return None
  theta=(V-L)/(H-L) if H!=L else Q(0)
  t=tuple(pins[j] if j in pins else (1-theta)*low[j]+theta*high[j] for j in range(self.m))
  assert self.observe(t)==tuple(y) and all(0<=x<=b for x,b in zip(t,self.caps));return t
 def oracle(self,y):
  lift=self.source_lift(y)
  if lift is not None:return {'lift':list(map(str,lift))}
  # Streaming this fixed dictionary is complete by the product theorem.
  for name,(row,b) in self.cuts():
   if dot(row,y)>b:return {'cut':name}
  raise AssertionError('dictionary failed to separate outside joint image')
 def member(self,frames,y):
  if len(y)!=self.d or any(len(a)!=self.d for a,b in frames):raise ValueError('SCHEMA_MISMATCH')
  for i,(a,b) in enumerate(frames):
   if dot(a,y)>b:return {'status':'EXCLUDED_FRAME','frame_index':i}
  answer=self.oracle(y)
  return {'status':'ADMITTED_POINT' if 'lift' in answer else 'EXCLUDED_SOURCE',**answer}
 def maximize(self,frames,c):
  if len(c)!=self.d or any(len(a)!=self.d for a,b in frames):raise ValueError('SCHEMA_MISMATCH')
  rows=[];bounds=[];labels=[]
  for j in range(self.d):
   for sign in (-1,1):
    a=tuple(Q(sign if i==j else 0) for i in range(self.d));rows.append(a);bounds.append(self.bound(a));labels.append(f'box:{j}:{sign}')
  for i,(a,b) in enumerate(frames):rows.append(a);bounds.append(b);labels.append(f'frame:{i}')
  # A feasible unrestricted support witness already proves the refined optimum.
  coeff=self.pullback(c);t=tuple(cap if a>0 else Q(0) for cap,a in zip(self.caps,coeff));point=self.observe(t)
  if all(dot(a,point)<=b for a,b in frames):
   bound=self.bound(c);rows.append(tuple(c));bounds.append(bound);labels.append('support:objective')
   return {'status':'OPTIMUM','point':list(map(str,point)),'value':str(bound),'source_lift':list(map(str,t)),'multipliers':['0']*(len(rows)-1)+['1'],'rows':[{'normal':list(map(str,a)),'upper':str(b),'label':lab} for a,b,lab in zip(rows,bounds,labels)],'trace':[],'dictionary_size':self.dictionary_size()}
  used=set();trace=[]
  while True:
   result=lp(rows,bounds,c)
   if result['status']=='INCONSISTENT':break
   point=tuple(map(Q,result['point']));answer=self.oracle(point)
   if 'lift' in answer:result['source_lift']=answer['lift'];break
   name=answer['cut'];assert name not in used;used.add(name);a,b=self.cut(name);assert dot(a,point)>b
   trace.append({'candidate':list(map(str,point)),'cut':name});rows.append(a);bounds.append(b);labels.append(name)
   assert len(used)<=self.dictionary_size()
  return {**result,'rows':[{'normal':list(map(str,a)),'upper':str(b),'label':lab} for a,b,lab in zip(rows,bounds,labels)],'trace':trace,'dictionary_size':self.dictionary_size()}
