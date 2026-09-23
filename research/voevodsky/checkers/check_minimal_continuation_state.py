"""Exact state-count bounds for three continuation contracts on one source fiber.
Shared source/family code is fixed. Count persistent history-dependent states,
not packet bits, provenance or arbitrary-precision source descriptions.
"""
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
intervals=[(Q(0),Q(1)),(Q(1),Q(2)),(Q(2),Q(3)),(Q(0),Q(3)),(Q(1,2),Q(5,2))]
def source(h):return (Q(50)-h/128,Q(51)+129*h/128,Q(52)-h)
def observe(x):return sum(x),sum(v*Q(1,128**j) for j,v in enumerate(x))
def bounds(mask):
 chosen=[intervals[i] for i in range(len(intervals)) if mask>>i&1]
 return max(a for a,b in chosen),min(b for a,b in chosen)
def main():
 N=len(intervals);full=(1<<N)-1
 legal={mask:bounds(mask) for mask in range(1,full+1) if bounds(mask)[0]<=bounds(mask)[1]}
 @lru_cache(None)
 def partition(mask):
  if not mask:return ()
  first=mask&-mask;best=None
  for group in legal:
   if group&first and group&mask==group:
    answer=(group,)+partition(mask^group)
    if best is None or len(answer)<len(best):best=answer
  return best
 groups=partition(full);assert len(groups)==2
 # Independent interval-stabbing construction: greedily take least right end.
 remaining=set(range(N));points=[];assignment={}
 while remaining:
  h=min(intervals[i][1] for i in remaining);points.append(h)
  covered={i for i in remaining if intervals[i][0]<=h<=intervals[i][1]}
  assert covered
  for i in covered:assignment[i]=len(points)-1
  remaining-=covered
 assert len(points)==2
 # Sharp lower witness: two disjoint admissible fibers cannot share any output.
 assert intervals[0][1]<intervals[2][0]
 # Shareability is not transitive: closed intervals share their boundary points.
 assert 3 in legal and 6 in legal and 5 not in legal
 base=observe(source(Q(0)))
 for lo,hi in intervals:
  for h in (lo,(lo+hi)/2,hi):
   x=source(h);assert observe(x)==base and all(0<=v<=100+2*j for j,v in enumerate(x))
 for i,state in assignment.items():assert intervals[i][0]<=points[state]<=intervals[i][1]
 # Fine threshold possibility and universality distinguish all distinct intervals.
 distinctions=[]
 thresholds=sorted({v for pair in intervals for v in pair})
 for i,j in combinations(range(N),2):
  for h in thresholds:
   answers=lambda k:(intervals[k][0]<=h,intervals[k][1]<=h)
   if answers(i)!=answers(j):distinctions.append({'histories':[i,j],'h_le':str(h),'answers':[answers(i),answers(j)]});break
  else:raise AssertionError('indistinguishable fine intervals')
 report={'passed':True,'history_intervals':[[str(a),str(b)] for a,b in intervals],
 'source_parameterization':['50-h/128','51+129h/128','52-h'],
 'common_public_point':list(map(str,base)),
 'minimal_state_counts':{'public_only':1,'public_plus_valid_lift':2,'fine_reexposure':5},
 'minimal_fixed_width_history_bits':{'public_only':0,'public_plus_valid_lift':1,'fine_reexposure':3},
 'lift_encoding':{'points':list(map(str,points)),'history_to_state':assignment},
 'exhaustive_legal_groups':len(legal),'optimal_partition_masks':groups,
 'fine_distinctions':distinctions,'nontransitive_compatibility':{'compatible_pairs':[[0,1],[1,2]],'incompatible_pair':[0,2]},
 'scope':'Exact minimum state cardinalities for this fixed finite family and deterministic exact contracts. Shared code, migration verification, transcripts and archives excluded.'}
 (OUT/'minimal-continuation-state.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ('passed','minimal_state_counts','minimal_fixed_width_history_bits','lift_encoding','nontransitive_compatibility')},indent=2))
if __name__=='__main__':main()
