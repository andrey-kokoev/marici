"""Search exact strictly positive n=9 targets requiring more than seven source labels."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,random
import sympy as s
from check_nine_point_seven_support_coverage_probe import OUT as N,Z,cache,check

def power(rng):return Q(2)**rng.randint(-8,8)
def main():
 rng=random.Random(20260831);rows=[];hist={};bad=None;count=0
 for attempt in range(350):
  neg=attempt%9;w=[power(rng) for _ in range(9)];slopes=[Q(0)]
  for _ in range(8-neg):slopes.append(slopes[-1]+power(rng))
  high=[slopes[-1]+power(rng)]
  for _ in range(1,neg):high.append(high[-1]+power(rng))
  t=high+slopes[:9-neg] if neg else slopes
  x=[(-w[i] if i<neg else w[i]) for i in range(9)];y=[x[i]*t[i] for i in range(9)]
  assert all(x[i]*y[j]-x[j]*y[i]>0 for i,j in combinations(range(9),2))
  Y=s.Matrix([x,y])*Z;found=None
  for index,entry in enumerate(cache):
   if (record:=check(Y,entry)) is not None:found=(index,record);break
  count+=1
  if found is None:
   bad={'attempt':attempt,'negative_initial_columns':neg,'weights':list(map(str,w)),'slopes':list(map(str,t))};break
  hist[str(neg)]=hist.get(str(neg),0)+1
  if attempt in (0,1,2,8,79,159,249,349):rows.append({'attempt':attempt,'first_subset_index':found[0],
      'first_subset':found[1]['support'],'active_minors':found[1]['active_minors']})
 result={'schema':'marici.nima.nine-point-support-stress.v1','tested':count,
  'gauges':hist,'first_no_seven_support_target':bad,'retained_examples':rows,
  'scope':'Finite necessary-support test only. No seven-label subimage at a strictly positive target would refute any universal compiler using only seven-label cells. Finding one subset never establishes physical history-form matching or full coverage.'}
 (N/'nine-point-support-stress.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
