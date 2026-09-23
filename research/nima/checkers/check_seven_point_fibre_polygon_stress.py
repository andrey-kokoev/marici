"""Exact 2D fibre polygon membership stress test for the six repaired n=7 cells."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json,random
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
k=(1,-6,15,-20,15,-6,1);pairs=list(combinations(range(7),2))
constraints={0:((1,2),(4,5)),2:((2,3),(0,6)),4:((4,5),(0,6))}
zeros={1:2,3:0,5:4}
def line(x,y,i,j):return (Q(x[i]*y[j]-x[j]*y[i]),Q(k[i]*y[j]-k[j]*y[i]),Q(x[i]*k[j]-x[j]*k[i]))
def solve(L,M):
 c,a,b=L;d,e,f=M;det=a*f-b*e
 if det==0:return None
 return ((b*d-c*f)/det,(c*e-a*d)/det)
def classify(x,y):
 lines={p:line(x,y,*p) for p in pairs};out=[]
 for index in range(6):
  if index in zeros:
   j=zeros[index];a=-Q(x[j],k[j]);b=-Q(y[j],k[j]);expected={p for p in pairs if j in p}
  else:
   first,second=constraints[index];point=solve(lines[first],lines[second])
   if point is None:out.append({'cell':index,'status':'SINGULAR'});continue
   a,b=point;expected=set(constraints[index])
  values={p:c+a*d+b*e for p,(c,d,e) in lines.items()}
  negative=[list((i+1,j+1)) for (i,j),value in values.items() if value<0]
  active={p for p,value in values.items() if value==0}
  out.append({'cell':index,'status':'INSIDE' if not negative and active==expected else 'OUTSIDE',
              'negative_count':len(negative),'extra_zeros':len(active-expected)})
 return out,lines
def vertices(lines):
 result=set()
 for p,q in combinations(pairs,2):
  xy=solve(lines[p],lines[q])
  if xy is not None and all(c+xy[0]*a+xy[1]*b>=0 for c,a,b in lines.values()):result.add(xy)
 return result
def main():
 rng=random.Random(20260826);rows=[];hist={};first_bad=None
 for run in range(160):
  w=[rng.randint(1,9) for _ in range(7)];steps=[rng.randint(1,12) for _ in range(6)];t=[0]
  for step in steps:t.append(t[-1]+step)
  x=[Q(z) for z in w];y=[Q(w[i]*t[i]) for i in range(7)]
  out,lines=classify(x,y);inside=[r['cell'] for r in out if r['status']=='INSIDE']
  key=str(len(inside));hist[key]=hist.get(key,0)+1
  if len(inside)!=1:
   first_bad={'run':run,'weights':w,'slopes':t,'members':inside,'classifications':out,
              'fibre_polygon_vertices':len(vertices(lines))};break
  if run in (0,1,2,9,49,99,159):rows.append({'run':run,'weights':w,'slopes':t,'member':inside[0],
                                                    'fibre_polygon_vertices':len(vertices(lines))})
 # Crucial control: the simple monotone t-gauge samples only one image
 # chamber. Lift each of the six proposed cell seeds to a STRICTLY positive
 # seven-column source through an exact kernel shift, then classify again.
 sectors=[]
 for idx in range(6):
  if idx in zeros:
   z=zeros[idx];points=[(1,j) if j<z else ((0,0) if j==z else (1,j-1)) for j in range(7)]
  else:
   t={0:[0,1,1,2,3,3,4],2:[4,0,1,1,2,3,4],4:[4,0,1,2,3,3,4]}[idx]
   points=[(-1,-t[j]) if j==0 and idx in (2,4) else (1,t[j]) for j in range(7)]
  x=[Q(a) for a,b in points];y=[Q(b) for a,b in points];L=[line(x,y,*p) for p in pairs]
  selected=None
  for aa in range(-20,21):
   for bb in range(-20,21):
    if all(c+Q(aa,10000)*a+Q(bb,10000)*b>0 for c,a,b in L):selected=(aa,bb);break
   if selected:break
  assert selected is not None
  X=[x[j]+Q(selected[0],10000)*k[j] for j in range(7)]
  V=[y[j]+Q(selected[1],10000)*k[j] for j in range(7)]
  classified,_=classify(X,V);members=[r['cell'] for r in classified if r['status']=='INSIDE']
  sectors.append({'seed_cell':idx,'kernel_shift_numerators':list(selected),'strictly_positive_top_source':True,'members':members})
 report={'schema':'marici.nima.seven-point-fibre-polygon-stress.v1','seed':20260826,'sector_lifts':sectors,
 'tested':sum(hist.values()),'membership_count_histogram':hist,'first_counterexample':first_bad,
 'retained_examples':rows,
 'method':'At fixed Y the 2x7 source fibre is C+[a,b]^T k. Every ordered minor is affine in (a,b); exact rational halfspace intersection is the positive fibre polygon. Six repaired candidates solve two facet/zero-column equations and test all 21 inequalities.',
 'scope':'Deterministic finite stress test. Even all counts one cannot certify universal six-cell coverage.'}
 (N/'results/seven-point-fibre-polygon-stress.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'tested':report['tested'],'histogram':hist,'sector_lift_members':[r['members'] for r in sectors],
  'first_counterexample':first_bad,'examples':rows},indent=2))
if __name__=='__main__':main()
