"""Fit symmetric v1 mixed gains, rank by multiplicative error (one row per unordered pair)."""
import csv, math, statistics
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results'
rows=[]
for z in csv.DictReader((D/'ramsey_mixed_field_26.csv').open()):
    a,b=map(int,(z['l'],z['k']))
    if a<2 or a>b:continue
    v=int(z['D_v1']);x,y=a-2,b-2;rows.append((a,b,v,[1,math.log(math.comb(x+y,x)),x]))
M=[[sum(f[i]*f[j] for _,_,_,f in rows) for j in range(3)]+[sum(f[i]*math.log(v) for _,_,v,f in rows)] for i in range(3)]
for i in range(3):
    q=M[i][i];M[i]=[t/q for t in M[i]]
    for j in range(3):
        if j!=i:
            q=M[j][i];M[j]=[t-q*u for t,u in zip(M[j],M[i])]
c=[r[-1] for r in M];out=[]
for a,b,v,f in rows:
    p=math.exp(sum(t*u for t,u in zip(f,c)));out.append((a,b,b-a,a+b,v,p,p/v,max(p/v,v/p)))
out.sort(key=lambda r:(-r[-1],r[0],r[1]));
with (D/'ramsey_fit_error_ranks.csv').open('w',newline='') as fp:
    w=csv.writer(fp);w.writerow(['rank','l','k','gap','sum','D','fit','fit_over_D','error_factor']);w.writerows((i,*r) for i,r in enumerate(out,1))
for i,(a,b,g,s,v,p,r,e) in enumerate(out[:16],1):print(i,a,b,g,v,round(p,2),round(r,3),round(e,3))
for a in (2,3,4,5,6,7,8,9,10,12,16,20,24):
 u=[z for z in out if z[0]==a];print('strip',a,len(u),round(statistics.median(z[-1] for z in u),3),sum(z[-2]>1 for z in u),[(z[1],round(z[-2],2)) for z in sorted(u,key=lambda t:t[1]) if z[1] in (a,14,20,26)])
