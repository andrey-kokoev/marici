"""Partial finite selectors compare packets without equating histories."""
from fractions import Fraction as Q
from pathlib import Path
import json
roots=('x-low','x-high','y-low','y-high')
A=((Q(0),Q(1),Q(0),Q(1)),Q(1))
B=((Q(1),Q(2),Q(0),Q(1)),Q(0))
C=((Q(0),Q(1),Q(1),Q(2)),Q(0))
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def value(packet):
 m,c=packet
 return tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(4))+c
def compare(left,right,manifest_left,manifest_right,witness=None):
 if manifest_left!=manifest_right and witness is None:raise ValueError('ROW_WITNESS_REQUIRED')
 if manifest_left!=manifest_right:raise NotImplementedError('WITNESS_TRANSPORT_NOT_IN_THIS_LOCAL_CHECK')
 if value(left)!=value(right):raise ValueError('TARGET_MISMATCH')
 diff=(tuple(right[0][i]-left[0][i] for i in range(4)),right[1]-left[1])
 assert value(diff)==((Q(0),Q(0)),Q(0))
 return diff
left_candidates={A,B};right_candidates={B,C}
assert left_candidates & right_candidates=={B}
left=A;right=C
assert left in left_candidates and right in right_candidates and left!=right
signed=compare(left,right,roots,roots)
assert signed==((Q(0),Q(0),Q(1),Q(1)),Q(-1))
try:compare(left,right,roots,tuple(reversed(roots)))
except ValueError as e:assert str(e)=='ROW_WITNESS_REQUIRED'
else:raise AssertionError('cross manifest accepted')
try:compare(A,((Q(0),)*4,Q(0)),roots,roots)
except ValueError as e:assert str(e)=='TARGET_MISMATCH'
else:raise AssertionError('target mismatch accepted')
report={'passed':True,'candidate_set_intersection':'{B}','distinct_selected_packets':'A and C','signed_comparison':{'multiplier_delta':list(map(str,signed[0])),'surplus_delta':str(signed[1])},'same_target_and_bound':True,'different_manifest_without_row_witness':'ROW_WITNESS_REQUIRED','different_target':'TARGET_MISMATCH','authority':'LOCAL_MATH_ONLY; no owner grant from common manifest or graph admission','scope':'Frozen finite source-rooted partial selector overlap, not identification of histories or declared higher categorical cell.'}
out=Path(__file__).resolve().parents[1]/'results/partial-selector-overlap.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
