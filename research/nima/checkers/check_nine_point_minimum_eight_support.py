"""Exact eight-label witness plus independent all-seven-support lower bound."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from pathlib import Path
import json
import sympy as s
from check_nine_point_no_seven_support_packet import replay
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
frozen=json.loads((OUT/'nine-point-support-stress.json').read_text())['first_no_seven_support_target']
packet=json.loads((OUT/'nine-point-no-seven-support-verification.json').read_text());assert replay(frozen,packet)==36
neg=frozen['negative_initial_columns'];w=list(map(Q,frozen['weights']));t=list(map(Q,frozen['slopes']))
x=[(-w[i] if i<neg else w[i]) for i in range(9)];y=[x[i]*t[i] for i in range(9)]
Z=[[Q(j**d) for d in range(6)] for j in range(1,10)]
K=[[Q((-1)**(j-p)*comb(6,j-p)) if 0<=j-p<=6 else Q(0) for j in range(9)] for p in range(3)]
assert all(sum(K[p][i]*Z[i][d] for i in range(9))==0 for p in range(3) for d in range(6))
# Rounded discovery is FROZEN as rational data before this exact check.
a0,a1,c0,c1=Q(4062,1000000),Q(5481,1000000),Q(-37665,1000000),Q(-105941,1000000)
deleted=2;assert K[2][deleted]==1
A=[a0,a1,-x[deleted]-a0*K[0][deleted]-a1*K[1][deleted]]
B=[c0,c1,-y[deleted]-c0*K[0][deleted]-c1*K[1][deleted]]
q01=A[0]*B[1]-A[1]*B[0];assert q01!=0
X=[x[j]+sum(A[p]*K[p][j] for p in range(3)) for j in range(9)]
V=[y[j]+sum(B[p]*K[p][j] for p in range(3)) for j in range(9)]
assert X[deleted]==V[deleted]==0
assert all(sum(X[i]*Z[i][d] for i in range(9))==sum(x[i]*Z[i][d] for i in range(9)) for d in range(6))
assert all(sum(V[i]*Z[i][d] for i in range(9))==sum(y[i]*Z[i][d] for i in range(9)) for d in range(6))
retained=[i for i in range(9) if i!=deleted]
minors={(i+1,j+1):X[i]*V[j]-X[j]*V[i] for i,j in combinations(retained,2)}
assert len(minors)==28 and min(minors.values())>0
assert all(X[i]*V[j]-X[j]*V[i]==0 for i,j in combinations(range(9),2) if deleted in (i,j))
result={'schema':'marici.nima.nine-point-minimum-eight-support.v1','passed':True,
 'positive_original_nine_label_source':True,'seven_or_fewer_supports_excluded_by_exact_packets':36,
 'eight_label_source_witness':{'deleted_label':3,'retained_labels':[i+1 for i in retained],
  'free_kernel_coefficients':list(map(str,(a0,a1,c0,c1))),
  'dependent_kernel_coefficients':[str(A[2]),str(B[2])],
  'nonzero_kernel_area_q01':str(q01),
  'source_rows':[list(map(str,X)),list(map(str,V))],
  'minimum_of_28_retained_minors':str(min(minors.values())),
  'observed_row_moments_equal':True},
 'minimum_source_label_support':8,
 'scope':'Exact minimum support for this fixed admitted nine-point target and fixed positive moment-curve external Z. It does not identify a physical NNMHV history cell, certify a canonical form or imply a universal support threshold.'}
(OUT/'nine-point-minimum-eight-support.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'minimum_support':8,'minimum_retained_minor':result['eight_label_source_witness']['minimum_of_28_retained_minors'],
 'deleted_label':3},indent=2))
