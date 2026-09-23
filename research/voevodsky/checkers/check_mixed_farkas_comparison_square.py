"""Mixed source-refinement / target-weakening square; exact rational proof data."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
def ok(p,L,T):
 a,b,c=map(Q,p);return Q(L)>0 and min(a,b,c)>=0 and b-a==1 and Q(L)*b+c==Q(T)
def refine(p,L,K,T,source_rows=('low:-x<=0','high:x<=L')):
 if source_rows!=('low:-x<=0','high:x<=L'):raise PermissionError('MISSING_PRIMITIVE_ROWS')
 assert 0<Q(K)<=Q(L) and ok(p,L,T)
 a,b,c=map(Q,p);r=(a,b,c+(Q(L)-Q(K))*b)
 assert ok(r,K,T);return r
def weaken(p,L,T,U):
 assert Q(U)>=Q(T) and ok(p,L,T)
 a,b,c=map(Q,p);r=(a,b,c+Q(U)-Q(T));assert ok(r,L,U);return r
def norm(p,L,T):
 assert ok(p,L,T)
 a,b,c=map(Q,p);v=c/Q(L);r=(a+v,b+v,Q(0));assert ok(r,L,T);return r
squares=0;intermediate_fail=0
for L,K,T,U in product((Q(1,2),Q(1),Q(3,2),Q(2),Q(3)),repeat=4):
 if not 0<K<=L<=T<=U:continue
 p=(Q(0),Q(1),T-L)
 left=weaken(refine(p,L,K,T),K,T,U)
 right=refine(weaken(p,L,T,U),L,K,U)
 assert left==right # raw square COMMUTES STRICTLY
 final=norm(left,K,U)
 assert final==norm(right,K,U)==(U/K-1,U/K,Q(0))
 via_refine=norm(weaken(norm(refine(p,L,K,T),K,T),K,T,U),K,U)
 via_weaken=norm(refine(norm(weaken(p,L,T,U),L,U),L,K,U),K,U)
 assert final==via_refine==via_weaken
 if weaken(norm(refine(p,L,K,T),K,T),K,T,U)!=final:intermediate_fail+=1
 squares+=1
assert squares>20 and intermediate_fail>0
try:refine((Q(1),Q(2),Q(1)),1,Q(1,2),3,source_rows=('high:x<=L',))
except PermissionError:root_refused=True
else:raise AssertionError('source provenance omitted')
report={'passed':True,'mixed_squares_checked':squares,'raw_transport_square':'strictly commutes for 0<K<=L<=T<=U','normalized_final':'(U/K-1,U/K,0)','strict_intermediate_packet_failures':intermediate_fail,'omitted_row_refused':root_refused,'scope':'Positive nested source intervals, monotone target weakenings and retained primitive row bounds; no proof-history higher interchange, widening, live authority or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/mixed-farkas-comparison-square.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
