"""Compare local support-set and signed valuation transitions against directional step residuals."""
import csv,math,statistics as st
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';P=[p for p in range(2,51) if all(p%i for i in range(2,math.isqrt(p)+1))]
def val(n,p):
 v=0
 while n%p==0:n//=p;v+=1
 return v
z=[];field={(int(r['l']),int(r['k'])):r['audit'] for r in csv.DictReader((D/'ramsey_mixed_field_26.csv').open())}
for r in csv.DictReader((D/'ramsey_prime_step_test.csv').open()):
 a,b=int(r['l']),int(r['k']);old=math.comb(a+b-5,a-2);new=math.comb(a+b-4,a-2);V=[(p,val(old,p),val(new,p)) for p in P];ent=[p for p,i,j in V if i==0<j];ext=[p for p,i,j in V if j==0<i];dv={p:j-i for p,i,j in V if j!=i};assert all(val(a+b-4,p)-val(b-2,p)==j-i for p,i,j in V);kind=('exchange' if ext else 'entry only') if ent else ('exit only' if ext else 'unchanged');mode='rise and fall' if min(dv.values())<0 else 'rise only';ex=all(field[i,j]=='exact' for i in [a-1,a] for j in [b-2,b-1,b]);z.append(dict(l=a,k=b,old=old,new=new,entry=ent,exit=ext,delta=dv,kind=kind,mode=mode,Q=float(r['ratio']),exact=ex,reversal=r['reverse']=='True'))
with (D/'ramsey_signature_transitions.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=z[0]);w.writeheader();w.writerows(z)
for field0 in ['kind','mode']:
 for t in sorted({r[field0] for r in z}):
  u=[r for r in z if r[field0]==t];print(t,len(u),round(math.exp(st.median(math.log(r['Q']) for r in u)),4),sum(r['Q']>1 for r in u),sum(r['exact'] for r in u),sum(r['reversal'] for r in u))
print('exact');
for r in z:
 if r['exact']:print(r['l'],r['k'],r['old'],r['new'],r['kind'],r['entry'],r['exit'],round(r['Q'],3),r['reversal'])
u=[r for r in z if 5 in r['entry'] and r['exit']];print('5-exchanges',len(u),sum(r['reversal'] for r in u),sum(r['exact'] for r in u))
