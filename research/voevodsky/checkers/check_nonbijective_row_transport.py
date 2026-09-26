"""Coincident math cannot turn a duplicate/omitted slot map into a permutation."""
from pathlib import Path
import json
rows=(((1,0),1,'A'),((1,0),1,'B'),((0,1),1,'C'))
weights=(1,0,0)
good=(1,0,2);bad=(0,1,1)
def evaluate(rs,ms):return tuple(sum(rs[i][0][j]*ms[i] for i in range(len(rs))) for j in (0,1)),sum(rs[i][1]*ms[i] for i in range(len(rs)))
def transport(perm):
 if len(perm)!=len(rows) or any(type(i) is not int for i in perm) or sorted(perm)!=list(range(len(rows))):return 'NOT_A_BIJECTION',None
 return 'VALID_PERMUTATION',evaluate(tuple(rows[i] for i in perm),tuple(weights[i] for i in perm))
assert transport(good)==('VALID_PERMUTATION',((1,0),1))
assert evaluate(tuple(rows[i] for i in bad),tuple(weights[i] for i in bad))==((1,0),1)
assert transport(bad)[0]=='NOT_A_BIJECTION'
report={'passed':True,'duplicate_rows':'A and B both x<=1, distinct row IDs','bad_index_map':'(0,1,1) duplicates B and omits C but example math x<=1 coincides','gate':'NOT_A_BIJECTION before transport','scope':'Local fixture, no verified source publication, event history or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/nonbijective-row-transport.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
