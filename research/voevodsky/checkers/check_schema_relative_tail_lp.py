"""Exact exhaustive reference backend; rational linear audited tail schemas."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def solve(columns,target):
 n=len(columns);a=[[col[i] for col in columns]+[v] for i,v in enumerate(target)];pivot=0;where=[]
 for j in range(n):
  k=next((k for k in range(pivot,len(a)) if a[k][j]),None)
  if k is None:return None
  a[pivot],a[k]=a[k],a[pivot];z=a[pivot][j];a[pivot]=[v/z for v in a[pivot]]
  for k in range(len(a)):
   if k!=pivot:
    z=a[k][j];a[k]=[v-z*w for v,w in zip(a[k],a[pivot])]
  where.append(pivot);pivot+=1
 if any(all(v==0 for v in row[:-1]) and row[-1]!=0 for row in a):return None
 return tuple(a[k][-1] for k in where)
def pull(m,A,a):
 assert len(a)==2+len(A)
 return tuple(a[0]+a[1]*Q(1,128**j)+sum(a[2+k] for k,i in enumerate(A) if i==j) for j in range(m))
def rows(state):
 m=state['m'];out=[]
 for j in range(m):
  e=tuple(Q(int(k==j)) for k in range(m));out.extend([(e,Q(100+2*j)),(tuple(-v for v in e),Q(0))])
 for f in state['frames']:out.append((pull(m,state['audits'],list(map(Q,f['a']))),Q(f['b'])))
 return out

def certify(state,query):
 rs=rows(state);m=state['m']
 if query['kind']=='membership':
  point=list(map(Q,query['point']));d=2+len(state['audits'])
  for i,v in enumerate(point):
   n=pull(m,state['audits'],[Q(int(i==j)) for j in range(d)])
   rs.extend([(n,v),(tuple(-a for a in n),-v)])
  objective=(Q(0),)*m
 else:objective=pull(m,state['audits'],list(map(Q,query['objective'])))
 verts=[]
 for inds in combinations(range(len(rs)),m):
  # Solve active row equations via columns of their square matrix.
  x=solve([tuple(rs[i][0][j] for i in inds) for j in range(m)],tuple(rs[i][1] for i in inds))
  if x is not None and all(dot(a,x)<=b for a,b in rs):verts.append(x)
 if not verts:
  for k in range(1,m+2):
   for inds in combinations(range(len(rs)),k):
    w=solve([rs[i][0]+(rs[i][1],) for i in inds],(Q(0),)*m+(Q(-1),))
    if w is not None and min(w)>=0:
     return {'state':state,'query':query,'status':'EMPTY','weights':[[i,str(v)] for i,v in zip(inds,w)]}
  raise AssertionError('missing Farkas certificate')
 x=max(verts,key=lambda x:(dot(objective,x),x));weights=[]
 if any(objective):
  active=[i for i,(a,b) in enumerate(rs) if dot(a,x)==b]
  found=False
  for k in range(1,m+1):
   for inds in combinations(active,k):
    w=solve([rs[i][0] for i in inds],objective)
    if w is not None and min(w)>=0:
     weights=[[i,str(v)] for i,v in zip(inds,w)];found=True;break
   if found:break
  assert found
 return {'state':state,'query':query,'status':'FEASIBLE_OPTIMUM','x':list(map(str,x)),
         'value':str(dot(objective,x)),'weights':weights}
def extend(state,A):
 assert set(state['audits'])<=set(A) and len(set(A))==len(A)
 fs=[]
 for f in state['frames']:
  a=f['a'][:2]+[f['a'][2+state['audits'].index(j)] if j in state['audits'] else '0' for j in A]
  fs.append({'a':a,'b':f['b']})
 return {'m':state['m'],'audits':list(A),'frames':fs,'source':'tail-box-100+2j-128^-j-v1'}
def fixtures(m_values=(3,4)):
 for m in m_values:
  base={'m':m,'audits':[],'frames':[{'a':['1','0'],'b':'5'}],'source':'tail-box-100+2j-128^-j-v1'}
  expanded=extend(base,[0,m-1]);assert rows(base)==rows(expanded)
  refined={**expanded,'frames':expanded['frames']+[{'a':['0','0','-1','0'],'b':'-2'},{'a':['1','0','0','1'],'b':'6'}]}
  empty={**refined,'frames':refined['frames']+[{'a':['0','0','1','0'],'b':'1'}]}
  for state in (base,expanded,refined,empty):
   d=2+len(state['audits'])
   for a in ([1]+[0]*(d-1),[0,1]+[0]*(d-2)):
    yield state,{'kind':'maximize','objective':list(map(str,a))}
  yield refined,{'kind':'maximize','objective':['0','0','1','-1']}
  for point in (['3','257/128','2','0'],['0','0','0','0']):
   yield refined,{'kind':'membership','point':point}
def main():
 packets=[certify(s,q) for s,q in fixtures()]
 # Pure schema extension must preserve old objective values.
 for start in (0,11):
  assert packets[start]['value']==packets[start+2]['value']
  assert packets[start+1]['value']==packets[start+3]['value']
 p=OUT/'schema-relative-tail-lp.json';p.write_text(json.dumps({'packets':packets},indent=2)+'\n')
 print(json.dumps({'passed':True,'certificates':len(packets),'scope':'Exhaustive source-space reference; not a scalable generator optimizer.'}))
if __name__=='__main__':main()
