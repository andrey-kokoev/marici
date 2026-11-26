"""Partial error audit, distinct from constructor depth. Seed intervals from stored 26 audit. Extend with disjoint clique lower constructions and Pascal upper bounds. Stream symmetric rows. Run-length encode equal error lower bounds."""
import csv,gzip,json
from collections import Counter
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';N=1000
old={(int(r['l']),int(r['k'])):r for r in csv.DictReader((D/'ramsey_mixed_field_26.csv').open())};counts=Counter();bad=[];peak=0
with gzip.open(D/'ramsey_interval_error_bands_1000.csv.gz','wt',newline='') as f:
 w=csv.writer(f);w.writerow(['l','first_k','last_k','status','minimum_absolute_error']);prev=None
 for a in range(1,N+1):
  row=[None]*(N+1);last=None
  for b in range(a,N+1):
   z=old.get((a,b));
   if a<=2:v=lo=hi=(1 if a==1 else b)
   else:
    x,l,u=prev[b];y,m,t=row[b-1] if b>a else prev[b];v=(int(z['R_v1']) if a==3 and b<=9 or (a,b) in ((4,4),(4,5)) else y+(b+1)//2 if a==3 else (57*(x+y)+32)//64);lo=max(l+b-1,m+a-1);hi=u+t
    if z:lo=max(lo,int(z['lower']));hi=min(hi,int(z['upper']))
   if z:assert v==int(z['R_v1']) and (lo,hi)==(int(z['lower']),int(z['upper']))
   assert lo<=hi;row[b]=(v,lo,hi);err=max(0,lo-v,v-hi);status='exact' if lo==hi else 'not excluded' if err==0 else 'below' if v<lo else 'above';counts[status]+=1+(a!=b)
   if err:peak=max(peak,err);bad.append((a,b,err))
   if (status,err)!=last:
    if last:w.writerow([a,start,b-1,*last]);
    start=b;last=(status,err)
  w.writerow([a,start,N,*last]);prev=row
print(counts,'unordered failures',len(bad),'first',bad[:10],'peak',peak)
