"""Fit parity medians only on exact inputs; separately enumerate integer parity offsets compatible with stored intervals (not a fit test)."""
import csv,json,statistics
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';a={int(r['k']):r for r in csv.DictReader((P/'ramsey_mixed_field_26.csv').open()) if r['l']=='3'};r=lambda k:int(a[k]['R_v1']);L=lambda k:int(a[k]['lower']);U=lambda k:int(a[k]['upper']);res=[[r(k)-r(k-1)-(k+1)//2 for k in range(5,10) if k%2==j] for j in (0,1)];cs=[int(statistics.median(z)) for z in res];K=range(10,27)
def pred(e,o):
 v=r(9);p={}
 for k in K:v+=(k+1)//2+(o if k%2 else e);p[k]=v
 return p
def fails(p):return [k for k in K if not L(k)<=p[k]<=U(k)]
fit=pred(*cs);pairs=[]
for e in range(L(10)-r(10),U(10)-r(10)+1):
 for o in range(L(11)-r(11)-e,U(11)-r(11)-e+1):
  if not fails(pred(e,o)):pairs.append((e,o))
two={k:r(k) for k in (8,9)}
for k in K:two[k]=two[k-2]+k+3
assert all(two[k]==pred(0,3)[k] for k in K);out=dict(residuals=res,calibrated=cs,failed=fails(fit),predictions=fit,compatible_integer_pairs=pairs);print(out);(P/'ramsey_row3_parity.json').write_text(json.dumps(out,indent=1)+'\n')
