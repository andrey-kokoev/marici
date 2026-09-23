"""Endpoint-plus-moment access for cap-redundant balanced-gain chains."""
from fractions import Fraction as Q
from joint_audit_tail_interface import lp,dot

def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

class MomentChain:
 def __init__(self,left,right):
  if not 0<=left<right or right-left<3:raise ValueError('at least four block atoms required')
  self.left=left;self.right=right;self.indices=tuple(range(left,right+1));self.m=len(self.indices);self.d=4
  self.scales=tuple(Q(1+j%3) for j in self.indices);self.slopes=tuple(Q(1,128**j) for j in self.indices);self.ell=Q(1,8);self.width=Q(1,8)
  self.base_low=left*self.ell;self.base_high=1+Q(left,4);self.caps=(self.base_high-self.base_low,)+(self.width,)*(self.m-1)
  self.S=tuple(sum(self.scales[i:]) for i in range(self.m));self.R=tuple(dot(self.scales[i:],self.slopes[i:]) for i in range(self.m))
  self.offset_source=tuple(s*(self.base_low+i*self.ell) for i,s in enumerate(self.scales));self.offset=self.observe(self.offset_source)
  self.columns=((self.scales[0],self.scales[-1],self.S[0],self.R[0]),)+tuple((Q(0),self.scales[-1],self.S[i],self.R[i]) for i in range(1,self.m))
  self.generators=tuple((Q(1),self.S[i],self.R[i]) for i in range(1,self.m))
  assert all(0<=self.offset_source[i] and self.scales[i]*(self.base_high+Q(i,4))<=100+2*j for i,j in enumerate(self.indices))
 def observe(self,t):return (t[0],t[-1],sum(t),dot(self.slopes,t))
 def source(self,delta):
  z=self.base_low+delta[0];out=[self.scales[0]*z]
  for i in range(1,self.m):z+=self.ell+delta[i];out.append(self.scales[i]*z)
  return tuple(out)
 def support(self,a):
  coeff=tuple(dot(a,g) for g in self.columns);delta=tuple(b if v>0 else Q(0) for b,v in zip(self.caps,coeff));t=self.source(delta)
  return dot(a,self.offset)+sum(b*max(Q(0),v) for b,v in zip(self.caps,coeff)),t
 def pull_residual(self,n):
  D,U,V=n;s=self.scales[0]
  return ((-D-U*self.S[0]-V*self.R[0])/s,D/self.scales[-1],U,V)
 def cuts(self):
  for sign in (-1,1):
   a=(Q(sign)/self.scales[0],Q(0),Q(0),Q(0));yield f'base:{sign}',(a,self.support(a)[0])
  for i,g in enumerate(self.generators):
   for j in range(i+1,len(self.generators)):
    n=cross(g,self.generators[j]);scale=next(abs(v) for v in n if v);n=tuple(v/scale for v in n)
    for sign in (-1,1):
     a=self.pull_residual(tuple(sign*v for v in n));yield f'pair:{i}:{j}:{sign}',(a,self.support(a)[0])
 def dictionary_size(self):return (self.m-1)*(self.m-2)+2
 def lift(self,point):
  delta0=point[0]/self.scales[0]-self.base_low
  if not 0<=delta0<=self.caps[0]:return None
  # The first endpoint fixes delta0; three other equalities determine a box fiber.
  n=self.m-1;A=[];b=[]
  for i in range(n):
   for sign in (-1,1):A.append(tuple(Q(sign*int(j==i)) for j in range(n)));b.append(self.width if sign>0 else Q(0))
  for j in (1,2,3):
   a=tuple(self.columns[i][j] for i in range(1,self.m));rhs=point[j]-self.offset[j]-delta0*self.columns[0][j]
   for sign in (-1,1):A.append(tuple(sign*v for v in a));b.append(sign*rhs)
  answer=lp(A,b,(Q(0),)*n)
  if answer['status']=='INCONSISTENT':return None
  delta=(delta0,*map(Q,answer['point']));t=self.source(delta)
  assert self.observe(t)==tuple(point) and all(0<=v<=cap for v,cap in zip(delta,self.caps));return t
 def oracle(self,point):
  for name,(a,b) in self.cuts():
   if dot(a,point)>b:return {'cut':name}
  t=self.lift(point)
  if t is None:raise RuntimeError('PROPOSAL_FAILED: facet-admitted point has no checked lift')
  return {'source_lift':list(map(str,t))}
 def maximize(self,frames,c):
  rows=[];bounds=[];labels=[]
  for j in range(4):
   for sign in (-1,1):
    a=tuple(Q(sign*int(i==j)) for i in range(4));rows.append(a);bounds.append(self.support(a)[0]);labels.append(f'box:{j}:{sign}')
  for i,(a,b) in enumerate(frames):rows.append(a);bounds.append(b);labels.append(f'frame:{i}')
  # Exact contradiction fast path: it does not infer emptiness from an error.
  for i,(a,b) in enumerate(zip(rows,bounds)):
   for j in range(i):
    if all(x==-y for x,y in zip(a,rows[j])) and b+bounds[j]<0:
     weights=['0']*len(rows);weights[i]=weights[j]='1'
     return {'status':'INCONSISTENT','multipliers':weights,'rows':[{'normal':list(map(str,a)),'upper':str(b),'label':label} for a,b,label in zip(rows,bounds,labels)],'trace':[],'method':'EXACT_OPPOSITE_ROW_FARKAS'}
  value,t=self.support(c);point=self.observe(t);trace=[]
  if all(dot(a,point)<=b for a,b in frames):
   rows.append(c);bounds.append(value);labels.append('support:objective');answer={'status':'OPTIMUM','point':list(map(str,point)),'value':str(value),'multipliers':['0']*(len(rows)-1)+['1'],'source_lift':list(map(str,t))}
  else:
   used=set()
   while True:
    answer=lp(rows,bounds,c)
    if answer['status']=='INCONSISTENT':break
    point=tuple(map(Q,answer['point']));result=self.oracle(point)
    if 'source_lift' in result:answer['source_lift']=result['source_lift'];break
    name=result['cut'];assert name not in used;used.add(name)
    a,b=next(row for key,row in self.cuts() if key==name)
    trace.append({'point':list(map(str,point)),'cut':name});rows.append(a);bounds.append(b);labels.append(name)
    assert len(used)<=self.dictionary_size()
  return {**answer,'rows':[{'normal':list(map(str,a)),'upper':str(b),'label':label} for a,b,label in zip(rows,bounds,labels)],'trace':trace}
