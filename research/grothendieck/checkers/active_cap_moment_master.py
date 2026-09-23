"""Network-priced moment master. Exact source-grid progress, not facet cuts."""
from fractions import Fraction as Q
from active_cap_network_support import support
from finite_master_lp import maximize as lp,dot

class Block:
 def __init__(self,left,right,extra_edges=()):
  assert 0<=left<=right
  self.left=left;self.right=right;self.ids=tuple(range(left,right+1));self.m=len(self.ids)
  self.s=tuple(Q(1+j%3) for j in self.ids);self.r=tuple(Q(1,128**j) for j in self.ids);self.edges=[]
  for i,j in enumerate(self.ids):self.edges.extend([(0,i+1,Q(100+2*j)/self.s[i]),(i+1,0,Q(0))])
  if left==0:self.edges.append((0,1,Q(1)))
  for i in range(self.m-1):self.edges.extend([(i+1,i+2,Q(20)),(i+2,i+1,-Q(1,2))])
  for edge in extra_edges:
   assert set(edge)=={'block','tail','head','upper'} and (6*Q(edge['upper'])).denominator==1
   def node(j):
    if j is None:return 0
    assert type(j)==int and left<=j<=right
    return j-left+1
   self.edges.append((node(edge['tail']),node(edge['head']),Q(edge['upper'])))
 def observe(self,z):
  t=tuple(s*v for s,v in zip(self.s,z));return (t[0],t[-1],sum(t),dot(self.r,t))
 def price(self,a):
  q=tuple(self.s[i]*(a[0]*int(i==0)+a[1]*int(i==self.m-1)+a[2]+a[3]*self.r[i]) for i in range(self.m))
  answer=support(self.edges,(-sum(q),*q));assert answer['status']=='OPTIMUM'
  z=tuple(map(Q,answer['potential'][1:]));assert all((6*v).denominator==1 for v in z)
  return z,answer

def pull(blocks,a):
 return tuple((a[0] if b==0 else Q(0),(a[1] if b==len(blocks)-1 else -a[2]-Q(1,128**block.right)*a[3]),a[2],a[3]) for b,block in enumerate(blocks))

def query(blocks,frames=(),objective=(Q(0),)*4,point=None,fast_master=True,local_frames=(),initial_columns=None):
 B=len(blocks);assert B and all(blocks[i].right==blocks[i+1].left for i in range(B-1))
 zero=(Q(0),)*4;rows=[]
 def add(label,coeff,bound,mass=None):rows.append((label,tuple(coeff),tuple(mass or [Q(0)]*B),Q(bound)))
 for b in range(B):
  for sign in (-1,1):add(f'mass:{b}:{sign}',[zero]*B,sign,[Q(sign*int(i==b)) for i in range(B)])
 for b in range(B-1):
  for sign in (-1,1):
   coeff=[zero]*B;coeff[b]=(Q(0),Q(sign),Q(0),Q(0));coeff[b+1]=(Q(-sign),Q(0),Q(0),Q(0));add(f'share:{b}:{sign}',coeff,0)
 for i,(a,bound) in enumerate(frames):add(f'frame:{i}',pull(blocks,a),bound)
 for i,(b,a,bound) in enumerate(local_frames):
  coeff=[zero]*B;coeff[b]=tuple(a);add(f'local:{i}:{b}',coeff,bound)
 if point is not None:
  for i,value in enumerate(point):
   for sign in (-1,1):add(f'pin:{i}:{sign}',pull(blocks,tuple(Q(sign*int(j==i)) for j in range(4))),sign*value)
 if initial_columns is None:columns=[(b,block.price(zero)[0]) for b,block in enumerate(blocks)]
 else:
  columns=[(item['block'],tuple(map(Q,item['potential']))) for item in initial_columns]
  assert {b for b,z in columns}==set(range(B)) and len(set(columns))==len(columns)
  for b,z in columns:
   block=blocks[b];p=(Q(0),*z);assert len(z)==block.m and all((6*v).denominator==1 for v in z)
   assert all(p[v]-p[u]<=w for u,v,w in block.edges)
 seen=set(columns);trace=[];cost=pull(blocks,tuple(map(Q,objective)))
 for phase in (1,2):
  while True:
   A=[[mass[b]+dot(coeff[b],blocks[b].observe(z)) for b,z in columns] for label,coeff,mass,bound in rows];bounds=[row[3] for row in rows]
   artificial=list(range(2*B,len(rows))) if phase==1 else []
   for i,row in enumerate(A):row.extend(Q(-int(i==j)) for j in artificial)
   c=[Q(0) if phase==1 else dot(cost[b],blocks[b].observe(z)) for b,z in columns]+[-Q(1)]*len(artificial)
   master=lp(A,bounds,c) if fast_master else lp(A,bounds,c,proposer=None);assert master['status']=='OPTIMUM'
   weights=tuple(map(Q,master['multipliers']));pricing=[];new=None
   for b,block in enumerate(blocks):
    a=tuple((Q(0) if phase==1 else cost[b][j])-sum(w*coeff[b][j] for w,(label,coeff,mass,bound) in zip(weights,rows)) for j in range(4))
    alpha=sum(w*mass[b] for w,(label,coeff,mass,bound) in zip(weights,rows));z,certificate=block.price(a)
    pricing.append({'block':b,'objective':list(map(str,a)),'threshold':str(alpha),'certificate':certificate})
    if Q(certificate['value'])>alpha and new is None:new=(b,z)
   entry={'phase':phase,'columns':len(columns),'master':master,'pricing':pricing}
   if new is not None:
    assert new not in seen;entry['added']={'block':new[0],'potential':list(map(str,new[1]))};trace.append(entry);columns.append(new);seen.add(new);continue
   trace.append(entry)
   if phase==1:
    assert Q(master['value'])<=0
    if Q(master['value'])<0:
     result={'status':'INCONSISTENT','trace':trace,'columns':[{'block':b,'potential':list(map(str,z))} for b,z in columns]}
     if point is not None:
      eta=[Q(0)]*4
      for w,(label,coeff,mass,bound) in zip(weights,rows):
       if label.startswith('pin:'):
        _,i,sign=label.split(':');eta[int(i)]+=w*int(sign)
      upper=sum(Q(record['certificate']['value']) for record in pricing)+sum(weights[i]*row[3] for i,row in enumerate(rows) if i>=2*B and not row[0].startswith('pin:'))
      result['separator']={'normal':list(map(str,[-v for v in eta])),'upper':str(upper)}
     return result
    break
   lam=tuple(map(Q,master['point']));lifts=[]
   for b,block in enumerate(blocks):
    z=tuple(sum(lam[k]*col[j] for k,(side,col) in enumerate(columns) if side==b) for j in range(block.m));lifts.append(tuple(s*v for s,v in zip(block.s,z)))
   assert all(lifts[i][-1]==lifts[i+1][0] for i in range(B-1));glued=lifts[0]+tuple(x for lift in lifts[1:] for x in lift[1:])
   return {'status':'OPTIMUM','value':master['value'],'source_lift':list(map(str,glued)),'block_lifts':[list(map(str,t)) for t in lifts],'columns':[{'block':b,'potential':list(map(str,z))} for b,z in columns],'trace':trace}
