"""Exact six-cell fibre classification across cyclic-wrap-positive source gauges."""
from pathlib import Path
from fractions import Fraction as Q
import json,random
from check_seven_point_fibre_polygon_stress import N,k,pairs,line,classify,vertices,zeros,constraints,solve

def build(rng,negative):
 # Remaining positive columns have increasing finite slopes; initial columns
 # have negative weights and slopes strictly above all remaining slopes.
 w=[rng.randint(1,9) for _ in range(7)];s=[0]
 for _ in range(6-negative):s.append(s[-1]+rng.randint(1,12))
 # For two negative columns, their slopes increase, all above the last
 # positive slope. For one negative column, simply pick a higher slope.
 top=s[-1]+rng.randint(1,12);large=[top]
 for _ in range(1,negative):large.append(large[-1]+rng.randint(1,12))
 t=large+s[:7-negative]
 x=[Q((-1 if j<negative else 1)*w[j]) for j in range(7)]
 y=[x[j]*t[j] for j in range(7)]
 return w,t,x,y

def main():
 rng=random.Random(20260827);rows=[];walls=[];hist={};counter=None;total=0
 for neg in (1,2,3,4,5,6):
  for run in range(120):
   w,t,x,y=build(rng,neg)
   assert all(line(x,y,*p)[0]>0 for p in pairs)
   outcomes,lines=classify(x,y);members=[o['cell'] for o in outcomes if o['status']=='INSIDE']
   closed=[o['cell'] for o in outcomes if o['negative_count']==0 and o['status']!='SINGULAR']
   key=f'open={len(members)},closed={len(closed)}';hist[key]=hist.get(key,0)+1;total+=1
   if len(members)==0 and len(closed)>1:
    points=[]
    for j in closed:
     if j in zeros:
      z=zeros[j];p=(-Q(x[z],k[z]),-Q(y[z],k[z]))
     else:p=solve(lines[constraints[j][0]],lines[constraints[j][1]])
     assert p is not None;points.append(p)
    assert len(set(points))==1
    p=points[0];active=[[i+1,j+1] for (i,j),(c,a,b) in lines.items() if c+p[0]*a+p[1]*b==0]
    walls.append({'negative_initial_columns':neg,'run':run,'weights':w,'slopes':t,
                  'closed_members':closed,'coincident_fibre_vertex':list(map(str,p)),'active_ordered_minors':active})
   if not closed or len(members)>1:
    counter={'kind':'closed-coverage-or-open-overlap-counterexample','negative_initial_columns':neg,'run':run,'weights':w,'slopes':t,
             'open_members':members,'closed_members':closed,'vertex_count':len(vertices(lines)),'outcomes':outcomes};break
   if run in (0,1,39,79,99,119):rows.append({'negative_initial_columns':neg,'run':run,'open_members':members,
                                            'closed_members':closed,'vertex_count':len(vertices(lines))})
  if counter:break
 result={'schema':'marici.nima.seven-point-multichamber-stress.v1','seed':20260827,
  'tested':total,'membership_count_histogram':hist,'shared_wall_witnesses':walls,'counterexample':counter,'retained_examples':rows,
  'scope':'Exact finite tests of strictly positive source matrices in six cyclic-wrap sign gauges. Open cells can have no member on a shared wall; closed membership is the coverage test. No finite pass proves universal coverage.'}
 (N/'results/seven-point-multichamber-stress.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'tested':total,'histogram':hist,'shared_walls':walls,'counterexample':counter},indent=2))
if __name__=='__main__':main()
