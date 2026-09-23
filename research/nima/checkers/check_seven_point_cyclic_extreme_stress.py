"""Adversarial exact search against cyclic-only fibre sufficiency on admitted targets."""
import json,random
from fractions import Fraction as Q
from pathlib import Path
from check_seven_point_fibre_polygon_stress import N,pairs,line,vertices
from check_seven_point_cyclic_fibre_reduction_probe import cyclic,poly,bounded

def power(rng):
 n=rng.randrange(-14,15);return Q(2)**n

def main():
 rng=random.Random(20260830);count=0;bad=None;hist={}
 for attempt in range(14000):
  neg=attempt%7;w=[power(rng) for _ in range(7)]
  t=[Q(0)]
  for _ in range(6-neg):t.append(t[-1]+power(rng))
  high=[t[-1]+power(rng)]
  for _ in range(1,neg):high.append(high[-1]+power(rng))
  slopes=high+t[:7-neg] if neg else t
  x=[(-w[i] if i<neg else w[i]) for i in range(7)];y=[x[i]*slopes[i] for i in range(7)]
  lines={p:line(x,y,*p) for p in pairs}
  assert all(c>0 for c,a,b in lines.values())
  cyclic_lines={p:lines[p] for p in cyclic};candidate=poly(cyclic_lines)
  assert bounded(cyclic_lines)
  fails=[(z,[(i+1,j+1) for (i,j),(c,a,b) in lines.items() if c+a*z[0]+b*z[1]<0]) for z in candidate]
  fails=[(z,indices) for z,indices in fails if indices]
  hist[str(neg)]=hist.get(str(neg),0)+1;count+=1
  if fails:
   bad={'attempt':attempt,'negative_initial_columns':neg,'weights':list(map(str,w)),'slopes':list(map(str,slopes)),
    'bad_cyclic_vertex':list(map(str,fails[0][0])),'violated_noncyclic_minors':fails[0][1],
    'full_positive_polygon_vertices':len(vertices(lines)),'cyclic_polygon_vertices':len(candidate)}
   break
 result={'schema':'marici.nima.seven-point-cyclic-extreme-stress.v1','tested':count,
  'gauges_tested':hist,'first_admitted_target_counterexample':bad,
  'scope':'Deterministic adversarial exact powers-of-two weights and gaps across seven positive-source sign gauges. A found bad cyclic vertex refutes cyclic sufficiency even when the target has a strictly positive source.'}
 (N/'results/seven-point-cyclic-extreme-stress.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
