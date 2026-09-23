"""Independent replay of exact eight-label upper and all-seven-label lower certificates."""
import copy,json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import sympy as s
from check_nine_point_no_seven_support_packet import replay
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
def verify(frozen,lower,claim):
 assert replay(frozen,lower)==36
 assert claim['minimum_source_label_support']==8
 neg=frozen['negative_initial_columns'];w=list(map(Q,frozen['weights']));t=list(map(Q,frozen['slopes']))
 original=[[-w[i] if i<neg else w[i] for i in range(9)],[]]
 original[1]=[original[0][i]*t[i] for i in range(9)]
 assert all(original[0][i]*original[1][j]-original[0][j]*original[1][i]>0 for i,j in combinations(range(9),2))
 Z=[[Q(j**d) for d in range(6)] for j in range(1,10)]
 witness=claim['eight_label_source_witness'];X,V=[list(map(Q,row)) for row in witness['source_rows']]
 assert len(X)==len(V)==9 and witness['deleted_label']==3
 support=tuple(i+1 for i in range(9) if X[i] or V[i]);assert support==tuple(witness['retained_labels']) and len(support)==8
 assert all(sum(row[i]*Z[i][d] for i in range(9))==sum(old[i]*Z[i][d] for i in range(9))
            for row,old in zip((X,V),original) for d in range(6))
 a0=X[0]-original[0][0];b0=V[0]-original[1][0]
 a1=X[1]-original[0][1]+6*a0;b1=V[1]-original[1][1]+6*b0
 area=a0*b1-a1*b0;assert area!=0 and area==Q(witness['nonzero_kernel_area_q01'])
 minors=[X[i]*V[j]-X[j]*V[i] for i,j in combinations((z-1 for z in support),2)]
 assert len(minors)==28 and min(minors)>0 and min(minors)==Q(witness['minimum_of_28_retained_minors'])
 return True
def main():
 frozen=json.loads((OUT/'nine-point-support-stress.json').read_text())['first_no_seven_support_target']
 lower=json.loads((OUT/'nine-point-no-seven-support-verification.json').read_text())
 claim=json.loads((OUT/'nine-point-minimum-eight-support.json').read_text());assert verify(frozen,lower,claim)
 refused=[]
 for defect in ('altered-source-entry','understated-minor','omitted-lower-case','false-support'):
  source=copy.deepcopy(frozen);low=copy.deepcopy(lower);bad=copy.deepcopy(claim)
  if defect=='altered-source-entry':bad['eight_label_source_witness']['source_rows'][0][0]='0'
  if defect=='understated-minor':bad['eight_label_source_witness']['minimum_of_28_retained_minors']='0'
  if defect=='omitted-lower-case':low['certificates'].pop()
  if defect=='false-support':bad['eight_label_source_witness']['retained_labels'].pop()
  try:verify(source,low,bad)
  except (AssertionError,ValueError,KeyError):refused.append(defect)
  else:raise AssertionError('corrupted support certificate accepted')
 result={'passed':True,'minimum_label_support':8,'lower_supports_excluded':36,'upper_retained_minors_checked':28,
  'mutations_refused':refused,'scope':'One fixed nine-point target; no physical history or universal support theorem.'}
 (OUT/'nine-point-minimum-eight-support-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
