"""Frozen diagonal-only 113/128 switch at 5; audit against the same saved bounds as v1."""
import csv
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';rows=list(csv.DictReader((D/'ramsey_mixed_field_26.csv').open()));z={(int(r['l']),int(r['k'])):r for r in rows};v={};fails=[];changed=0
with (D/'ramsey_diagonal_discount_switch.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['l','k','R_base','R_switch','D_base','D_switch','lower','upper'])
 for a in range(1,27):
  for b in range(a,27):
   r=z[a,b];old=int(r['R_v1']);p=old
   if a>=4 and r['audit']!='exact':
    num=113 if a==b and a>=5 else 114;p=(num*(v[a-1,b]+v[a,b-1])+64)//128
   v[a,b]=v[b,a]=p;d=p-v[a-1,b]-v[a,b-1]+v[a-1,b-1] if a>1 else '';w.writerow([a,b,old,p,r['D_v1'],d,r['lower'],r['upper']]);changed+=int(old!=p)
   if not int(r['lower'])<=p<=int(r['upper']):fails.append((a,b,p,r['lower'],r['upper']))
   if a==b and a in (5,6,7,10,13,26):print(a,old,p,r['D_v1'],d)
print('distinct cells changed',changed,'outside',fails)
