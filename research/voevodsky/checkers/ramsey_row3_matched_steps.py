"""Same exact target cells k=5..9, same one-parameter median residual rule, same audit intervals. Bounds are not ground truth."""
from pathlib import Path
import csv,statistics
P=Path(__file__).resolve().parents[1]/'results';a={int(r['k']):r for r in csv.DictReader((P/'ramsey_mixed_field_26.csv').open()) if r['l']=='3'};K=range(5,10);R={k:int(a[k]['R_v1']) for k in range(3,10)};pred={};
for s in (1,2):
 step=lambda k:(k+1)//2 if s==1 else k;res=[R[k]-R[k-s]-step(k) for k in K];c=statistics.median(res);p=R.copy()
 for k in range(10,27):p[k]=p[k-s]+step(k)+c
 pred[s]=p;print(s,res,c,'errors',[(k,p[k],a[k]['lower'],a[k]['upper']) for k in range(10,27) if not int(a[k]['lower'])<=p[k]<=int(a[k]['upper'])]);print([p[k] for k in range(10,15)])
with (P/'ramsey_row3_matched_steps.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['k','lower','upper','one_step_calibrated','two_step_calibrated']);w.writerows([k,a[k]['lower'],a[k]['upper'],pred[1][k],pred[2][k]] for k in range(10,27))
