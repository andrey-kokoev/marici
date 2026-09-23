"""Two-block lifted moment optimizer; moment allocation remains variable."""
from fractions import Fraction as Q
from joint_audit_tail_interface import lp,dot

def maximize(left,right,frames,objective):
 if left.right!=right.left:raise ValueError('SHARED_ENDPOINT_REQUIRED')
 rate=Q(1,128**left.right);maps={'L':(0,1,3,4),'R':(1,2,5,6)};models={'L':left,'R':right}
 def pull(a):return (a[0],-a[2]-rate*a[3],a[1],a[2],a[3],a[2],a[3])
 def embed(a,side):
  out=[Q(0)]*7
  for i,j in enumerate(maps[side]):out[j]=a[i]
  return tuple(out)
 rows=[];bounds=[];labels=[]
 # Keeping duplicate shared-coordinate bounds is deliberate and certified.
 for side in ('L','R'):
  for i in range(4):
   for sign in (-1,1):
    a=tuple(Q(sign*int(j==i)) for j in range(4));rows.append(embed(a,side));bounds.append(models[side].support(a)[0]);labels.append(f'{side}:box:{i}:{sign}')
 for i,(a,b) in enumerate(frames):rows.append(pull(a));bounds.append(b);labels.append(f'frame:{i}')
 used=set();trace=[];c=pull(objective)
 while True:
  answer=lp(rows,bounds,c)
  if answer['status']=='INCONSISTENT':break
  allocation=tuple(map(Q,answer['point']));lifts={};cut=None
  for side in ('L','R'):
   point=tuple(allocation[j] for j in maps[side]);result=models[side].oracle(point)
   if 'cut' in result:cut=(side,result['cut']);break
   lifts[side]=tuple(map(Q,result['source_lift']))
  if cut is None:
   assert lifts['L'][-1]==lifts['R'][0]
   public=(allocation[0],allocation[2],allocation[3]+allocation[5]-allocation[1],allocation[4]+allocation[6]-rate*allocation[1])
   answer['allocation']=list(map(str,allocation));answer['point']=list(map(str,public));answer['left_lift']=list(map(str,lifts['L']));answer['right_lift']=list(map(str,lifts['R']));break
  side,name=cut;label=side+':'+name;assert label not in used;used.add(label)
  a,b=next(row for key,row in models[side].cuts() if key==name);a=embed(a,side);assert dot(a,allocation)>b
  trace.append({'allocation':list(map(str,allocation)),'cut':label});rows.append(a);bounds.append(b);labels.append(label)
  assert len(used)<=left.dictionary_size()+right.dictionary_size()
 return {**answer,'rows':[{'normal':list(map(str,a)),'upper':str(b),'label':label} for a,b,label in zip(rows,bounds,labels)],'trace':trace,'dictionary_size':left.dictionary_size()+right.dictionary_size()}
