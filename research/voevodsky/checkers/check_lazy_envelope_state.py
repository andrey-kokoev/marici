"""Lazy exact projection oracle with flat base-row proof provenance.
No optimization. Successive stages stream/recompute pairs, not cached tables.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def combine(r,s,u,v):
 a,b,w=r;c,d,z=s;p={i:u*x for i,x in w.items()}
 for i,x in z.items():p[i]=p.get(i,Q(0))+v*x
 return tuple(u*x+v*y for x,y in zip(a,c)),u*b+v*d,{i:x for i,x in p.items() if x}
class Base:
 def __init__(self,rows):self.rows=rows;self.work=0
 def stream(self):
  for i,(a,b) in enumerate(self.rows):self.work+=1;yield a,b,{i:Q(1)}
 def member(self,y):
  for r in self.stream():
   if dot(r[0],y)>r[1]:return {'cut':r}
  return {'lift':y}
class Project:
 def __init__(self,parent,index):self.parent=parent;self.index=index;self.work=0
 def stream(self):
  k=self.index
  for r in self.parent.stream():
   c=r[0][k]
   if c==0:
    self.work+=1;yield r[0][:k]+r[0][k+1:],r[1],r[2]
   elif c>0:
    for s in self.parent.stream():
     if s[0][k]<0:
      a,b,w=combine(r,s,1/c,-1/s[0][k]);self.work+=1;yield a[:k]+a[k+1:],b,w
 def member(self,y):
  lo=hi=None;lr=ur=None;k=self.index
  for r in self.parent.stream():
   a,b,w=r;c=a[k];rest=a[:k]+a[k+1:];rhs=b-dot(rest,y)
   if not c:
    if rhs<0:return {'cut':(rest,b,w)}
   else:
    v=rhs/c
    if c<0 and (lo is None or v>lo):lo=v;lr=r
    if c>0 and (hi is None or v<hi):hi=v;ur=r
  if lo is not None and hi is not None and lo>hi:
   a,b,w=combine(ur,lr,1/ur[0][k],-1/lr[0][k]);return {'cut':(a[:k]+a[k+1:],b,w)}
  h=lo if lo is not None else hi if hi is not None else Q(0)
  result=self.parent.member(y[:k]+(h,)+y[k:]);assert 'lift' in result
  return result

def family(n):
 rows=[]
 for j,cap in enumerate((1,1,4,4)):
  for sign in (-1,1):rows.append((tuple(Q(sign if k==j else 0) for k in range(4)),Q(cap)))
 for i in range(n):
  a=Q(2*i+1-n,n)
  rows.extend([((2*a,Q(0),Q(-1),Q(0)),a*a),((Q(0),2*a,Q(1),Q(-1)),a*a)])
 return rows

def main():
 packets=[]
 for n in (2,4,8):
  original=family(n)
  for refined in (False,True):
   # Public refinement z<=1 appended to original rows; it passes unchanged
   # through both eliminations. No old frame is replaced.
   rows=original+([((Q(0),Q(0),Q(0),Q(1)),Q(1))] if refined else [])
   base=Base(rows);first=Project(base,2);second=Project(first,0)
   cases=[]
   for stage,model,points in [(1,first,[(Q(0),Q(0),Q(3)),(Q(0),Q(0),Q(-3))]),
                             (2,second,[(Q(0),Q(3)),(Q(0),Q(-3)),(Q(0),Q(0))])]:
    for point in points:
     before=[base.work,first.work,second.work];result=model.member(point)
     out={'stage':stage,'point':list(map(str,point)),'work_delta':[a-b for a,b in zip([base.work,first.work,second.work],before)]}
     if 'lift' in result:out['lift']=list(map(str,result['lift']))
     else:
      a,b,w=result['cut'];assert dot(a,point)>b
      out['cut']={'a':list(map(str,a)),'b':str(b),'weights':[[i,str(v)] for i,v in sorted(w.items())]}
     cases.append(out)
   packets.append({'n':n,'refined':refined,'base_rows':[[list(map(str,a)),str(b)] for a,b in rows],
    'cases':cases,'persistent_row_count':len(rows),'flat_pair_facets':n*n,
    'total_base_row_visits':base.work,'first_stage_rows_generated':first.work})
 (OUT/'lazy-envelope-state.json').write_text(json.dumps({'packets':packets},indent=2)+'\n')
 print(json.dumps([{k:p[k] for k in ('n','refined','persistent_row_count','flat_pair_facets','total_base_row_visits','first_stage_rows_generated')} for p in packets],indent=2))
if __name__=='__main__':main()
