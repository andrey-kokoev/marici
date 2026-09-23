"""Exact test whether fixed two-cyclic Farkas supports persist across positive-source chambers."""
from pathlib import Path
from fractions import Fraction as Q
import json,random
from check_seven_point_fibre_polygon_stress import N,line
from check_seven_point_cyclic_farkas_packets import certificate
from check_seven_point_cyclic_extreme_stress import power
choices=[{'target':(1,6),'edges':((0,1),(1,2))},
         {'target':(2,6),'edges':((1,2),(2,3))}]
def main():
 rng=random.Random(20260831);rows=[]
 for candidate in choices:
  successes=0;failure=None
  for run in range(4900):
   neg=run%7;w=[power(rng) for _ in range(7)];t=[Q(0)]
   for _ in range(6-neg):t.append(t[-1]+power(rng))
   high=[t[-1]+power(rng)]
   for _ in range(1,neg):high.append(high[-1]+power(rng))
   slopes=high+t[:7-neg] if neg else t
   x=[(-w[i] if i<neg else w[i]) for i in range(7)];y=[x[i]*slopes[i] for i in range(7)]
   L=line(x,y,*candidate['target']);P,T=[line(x,y,*e) for e in candidate['edges']]
   coeff=certificate(L,P,T)
   if coeff is None:
    failure={'run':run,'negative_initial_columns':neg,'weights':list(map(str,w)),'slopes':list(map(str,slopes))}
    break
   successes+=1
  rows.append({'target_minor':[z+1 for z in candidate['target']],
   'fixed_support':[[z+1 for z in e] for e in candidate['edges']],
   'successes_before_first_failure':successes,'counterexample':failure})
 result={'schema':'marici.nima.seven-point-farkas-support-chambers.v1','rows':rows,
 'scope':'Exact adversarial positive-source tests of two fixed dual-support choices; failure rules out the fixed support, not adaptive sparse Farkas certificates or cyclic sufficiency.'}
 (N/'results/seven-point-farkas-support-chambers.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
