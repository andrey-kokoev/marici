"""Independent exact replay of all 36 n=9 seven-support infeasibility witnesses."""
import copy,json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
def replay(frozen,packet):
 neg=frozen['negative_initial_columns'];w=list(map(Q,frozen['weights']));t=list(map(Q,frozen['slopes']))
 x=[(-w[i] if i<neg else w[i]) for i in range(9)];y=[x[i]*t[i] for i in range(9)]
 assert all(x[i]*y[j]-x[j]*y[i]>0 for i,j in combinations(range(9),2))
 Z=s.Matrix([[j**d for d in range(6)] for j in range(1,10)]);Y=s.Matrix([x,y])*Z
 assert len(packet['certificates'])==36
 expected=set(combinations(range(1,10),7));seen=set()
 for item in packet['certificates']:
  labels=tuple(item['retained_labels']);assert labels in expected and labels not in seen;seen.add(labels)
  z=Z[[i-1 for i in labels],:];inv=z[:6,:].inv();k=tuple(map(Q,(-z[6,:]*inv).row_join(s.ones(1,1))))
  assert all(sum(k[i]*z[i,d] for i in range(7))==0 for d in range(6))
  C=Y*inv;X=[Q(C[0,i]) for i in range(6)]+[Q(0)];V=[Q(C[1,i]) for i in range(6)]+[Q(0)]
  minor_labels=[tuple(p) for p in item['contradiction_minors']];weights=list(map(Q,item['positive_weights']))
  assert len(minor_labels)==len(weights)<=3 and len(set(minor_labels))==len(weights)
  assert all(p in set(combinations(range(1,8),2)) and lam>0 for p,lam in zip(minor_labels,weights))
  components=[]
  for (i,j),weight in zip(minor_labels,weights):
   i-=1;j-=1
   components.append((weight*(X[i]*V[j]-X[j]*V[i]),
                      weight*(k[i]*V[j]-k[j]*V[i]),
                      weight*(X[i]*k[j]-X[j]*k[i])))
  sums=[sum(row[h] for row in components) for h in range(3)]
  assert sums[0]==Q(item['weighted_constant'])<0 and sums[1:]==[0,0]
 assert seen==expected
 return len(seen)
def main():
 frozen=json.loads((OUT/'nine-point-support-stress.json').read_text())['first_no_seven_support_target']
 packet=json.loads((OUT/'nine-point-no-seven-support-verification.json').read_text())
 assert packet['passed'] and replay(frozen,packet)==36
 refused=[]
 for defect in ('negative-weight','false-constant','missing-subset','changed-source'):
  bad=copy.deepcopy(packet);source=copy.deepcopy(frozen)
  if defect=='negative-weight':bad['certificates'][0]['positive_weights'][0]='-1'
  if defect=='false-constant':bad['certificates'][0]['weighted_constant']='0'
  if defect=='missing-subset':bad['certificates'].pop()
  if defect=='changed-source':source['weights'][0]='-1'
  try:replay(source,bad)
  except (AssertionError,ValueError,KeyError):refused.append(defect)
  else:raise AssertionError('bad packet accepted: '+defect)
 result={'passed':True,'strict_positive_nine_source':True,'seven_support_subsets_excluded':36,'controls_refused':refused,
  'scope':'No n=9 positive source supported on seven or fewer labels can project to this fixed strictly positive target. Minimum possible support is eight; existence of an eight-label lift is not established.'}
 (OUT/'nine-point-no-seven-support-packet-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
