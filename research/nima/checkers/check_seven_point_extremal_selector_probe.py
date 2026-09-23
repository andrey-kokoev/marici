"""Is the unique repaired lift a fixed linear-optimization vertex of its fibre polygon?"""
import json,random
from fractions import Fraction as Q
from pathlib import Path
from check_seven_point_fibre_polygon_stress import N,k,pairs,zeros,constraints,line,solve,vertices,classify

def target_vertex(index,x,y,lines):
 if index in zeros:
  j=zeros[index];return (-Q(x[j],k[j]),-Q(y[j],k[j]))
 p,q=constraints[index];return solve(lines[p],lines[q])
def samples():
 rng=random.Random(20260826)
 for run in range(160):
  w=[rng.randint(1,9) for _ in range(7)];t=[0]
  for step in (rng.randint(1,12) for _ in range(6)):t.append(t[-1]+step)
  yield 'monotone-'+str(run),[Q(z) for z in w],[Q(w[i]*t[i]) for i in range(7)]
 for idx in range(6):
  if idx in zeros:
   z=zeros[idx];pts=[(1,j) if j<z else ((0,0) if j==z else (1,j-1)) for j in range(7)]
  else:
   t={0:[0,1,1,2,3,3,4],2:[4,0,1,1,2,3,4],4:[4,0,1,2,3,3,4]}[idx]
   pts=[(-1,-t[j]) if j==0 and idx in (2,4) else (1,t[j]) for j in range(7)]
  shift={0:(1,2),1:(2,3),2:(-3,-15),3:(-2,-15),4:(-3,-15),5:(2,7)}[idx]
  x=[Q(p[0])+Q(shift[0],10000)*k[j] for j,p in enumerate(pts)]
  y=[Q(p[1])+Q(shift[1],10000)*k[j] for j,p in enumerate(pts)]
  assert all(line(x,y,*pair)[0]>0 for pair in pairs)
  yield 'sector-'+str(idx),x,y

def main():
 directions=[(a,b) for a in range(-5,6) for b in range(-5,6) if a or b]
 fails={str(p):0 for p in directions};rivals=[];count=0
 for label,x,y in samples():
  classified,lines=classify(x,y);members=[r['cell'] for r in classified if r['status']=='INSIDE'];assert len(members)==1
  pos=target_vertex(members[0],x,y,lines);poly=vertices(lines);assert pos in poly
  for direction in directions:
   if any(direction[0]*(pos[0]-other[0])+direction[1]*(pos[1]-other[1])<0 for other in poly):
    fails[str(direction)]+=1
  if label.startswith('sector-'):
   rivals.append({'source':label,'member':members[0],'vertices':len(poly),
    'target_point':list(map(str,pos)),'coordinatewise_maximal':[all(pos[j]>=p[j] for p in poly) for j in range(2)]})
  count+=1
 best=sorted(fails.items(),key=lambda z:z[1])[:12]
 # Three exact polygon-vertex comparisons exclude EVERY nonzero fixed
 # linear objective, not merely the tested small integer directions.
 witness={}
 for label,x,y in samples():
  if label not in ('monotone-0','sector-2','sector-3'):continue
  assert all(line(x,y,*pair)[0]>0 for pair in pairs)
  records,lines=classify(x,y);selected=next(r['cell'] for r in records if r['status']=='INSIDE')
  q=target_vertex(selected,x,y,lines)
  witness[label]={(q[0]-p[0],q[1]-p[1]) for p in vertices(lines) if p!=q}
 assert (Q(-2231,15360),Q(-9817,7680)) in witness['monotone-0']
 assert (Q(1,85),Q(4,85)) in witness['sector-2']
 assert (Q(-1,90),Q(0)) in witness['sector-3']
 assert Q(19634,2231)>4
 obstruction={'monotone_0_difference':['-2231/15360','-9817/7680'],
  'sector_2_difference':['1/85','4/85'],'sector_3_difference':['-1/90','0'],
  'proof':'Any objective (cx,cy) maximizing each selected vertex must obey cx+(19634/2231)cy<=0, cx+4cy>=0 and cx<=0. Subtraction forces cy<=0; the latter two force cy>=0, hence cy=cx=0. No nonzero common objective exists.'}
 result={'schema':'marici.nima.seven-point-extremal-selector-probe.v1','tested':count,
  'universal_fixed_linear_objective_obstruction':obstruction,
  'zero_failure_directions':[k for k,v in fails.items() if v==0],
  'best_fixed_directions':best,'sector_witnesses':rivals,
  'conclusion':'Three exact positive fibres force the common maximizing direction to be zero. No nonzero fixed linear objective selects the repaired vertex on all positive fibres; a universal coverage proof needs another selection rule.',
  'scope':'Exact finite search over 120 small integer directions, 160 monotone and six sector samples; not a universal impossibility theorem.'}
 (N/'results/seven-point-extremal-selector-probe.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'zero_directions':result['zero_failure_directions'],'best':best,'obstruction':obstruction},indent=2))
if __name__=='__main__':main()
