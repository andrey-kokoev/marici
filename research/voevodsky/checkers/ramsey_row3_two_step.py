"""Compare one-step model with parity-separated two-step updates. Calibrate constant only on exact R(3,3)..R(3,9). Use the stored audit, not model values, for validation."""
from pathlib import Path
import csv,statistics
P=Path(__file__).resolve().parents[1]/'results';a={int(r['k']):r for r in csv.DictReader((P/'ramsey_mixed_field_26.csv').open()) if r['l']=='3'};exact={k:int(a[k]['R_v1']) for k in range(3,10)};res=[exact[k]-exact[k-2]-k for k in range(5,10)];c=int(statistics.median(res));raw=exact.copy();cal=exact.copy();print('calibration',res,c)
with (P/'ramsey_row3_two_step.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['k','lower','upper','one_step','two_step_raw','two_step_calibrated']);
 for k in range(10,27):
  raw[k]=raw[k-2]+k;cal[k]=cal[k-2]+k+c;l,u=int(a[k]['lower']),int(a[k]['upper']);vals=[int(a[k]['R_v1']),raw[k],cal[k]];w.writerow([k,l,u,*vals]);print(k,l,u,*vals,[i for i,v in enumerate(vals) if not l<=v<=u])
