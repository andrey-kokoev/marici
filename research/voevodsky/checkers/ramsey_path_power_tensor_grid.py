"""Threshold-adapted extension of the width-12 four-port experiment. A=first residue, C=last; packed bitset e is bit l. CSV: incidence rows as masks, tensor ranks and full-menu repair."""
import csv,json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results'
def cell(l,k):
    if min(l,k)==1:return dict(state='boundary')
    n=(l-1)*(k-2);h=(1<<n)-1;res=[sum(1<<i for i in range(j,n,l)) for j in range(l)]+[0];size=1<<(l+1)
    if l==2 and n:return dict(state='root already red-illegal')
    def alpha(p):
        v=0
        while p:
            b=p&-p;p &= -(b<<(l-1));v+=1
        return v
    U=[0]*size
    for m in range(1,size):
        b=m&-m;U[m]=U[m^b]|res[b.bit_length()-1]
    al=[alpha(h&~u) for u in U];bs=[i.bit_count() for i in range(size)];data=[]
    for root in [0,l-1]:
        bad=bytearray(size);rows=[]
        for m in range(size):
            p=m
            while p:
                b=p&-p;p-=b
                if bad[m^b]:bad[m]=1;break
            if not bad[m] and max(bs[m]+al[m],1+bs[m]+al[m|1<<root])>=k:bad[m]=1;rows.append(m)
        repair=l+1-max(bs[m] for m in range(size) if not bad[m]);data.append((set(rows),repair))
    A,C=data;diff=A[0]^C[0];return dict(state='tested',core=n,arity=min((bs[m] for m in diff),default=None),rows_A=sorted(A[0]),rows_C=sorted(C[0]),repair_A=A[1],repair_C=C[1])
if __name__=='__main__':
    rr=[dict(l=l,k=k,**cell(l,k)) for l in range(1,14) for k in range(1,14)];z=next(z for z in rr if (z['l'],z['k'])==(3,8));assert z['rows_A']==[11,13] and z['rows_C']==[13,14];
    with (D/'ramsey_path_power_tensor_grid.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['l','k','state','core','arity','repair_A','repair_C','rows_A','rows_C']);w.writeheader();w.writerows(rr)
    for l in range(1,14):print(l,' '.join('x' if z['state']!='tested' else str(z['arity'] or '=') for z in rr if z['l']==l))
    print('repair differences',[(z['l'],z['k'],z['repair_A'],z['repair_C']) for z in rr if z.get('repair_A')!=z.get('repair_C')][:30]);print('8,8',[(k,len(v) if isinstance(v,list) else v) for k,v in cell(8,8).items()]);
