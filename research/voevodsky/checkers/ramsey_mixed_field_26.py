"""Extend v1 unchanged; audit R, not D. Extra direct bounds: Radziszowski DS1 rev.18, Tables Ia, Ib, IIa and IIb (selected rows)."""
from pathlib import Path
from fractions import Fraction
import csv
D=Path(__file__).resolve().parents[1]/'results';old={(int(z['l']),int(z['k'])):z for z in csv.DictReader((D/'ramsey_field_bound_audit_v2.csv').open())};R={};exact=set();direct={};LU={}
for (a,b),z in old.items():
    if z['survey_lower']:direct[a,b]=int(z['survey_lower']),int(z['survey_upper'])
for i,lo in enumerate([67,74,82,92,100,106,111,122,131,139,143,154,161],14):direct[3,i]=lo,dict(enumerate([77,87,97,109,120,132,145,157,171,185],14)).get(i)
for a,L,U in [(4,[148,159],[307,364]),(5,[267,275],[1081,1341])]:
    for b,x,y in zip((14,15),L,U):direct[a,b]=x,y
for a in range(1,27):
    for b in range(a,27):
        if a==1:v=1
        elif a==2:v=b
        elif a==3 and b<=9 or (a,b) in ((4,4),(4,5)):v=int(old[a,b]['R_v1'])
        else:v=R[a,b-1]+(b+1)//2 if a==3 else int(Fraction(57,64)*(R[a-1,b]+R[a,b-1])+Fraction(1,2))
        R[a,b]=R[b,a]=v
        if (a,b) in old:assert int(old[a,b]['R_v1'])==v
        if a<=2 or a==3 and b<=9 or (a,b) in ((4,4),(4,5)):
            exact.update(((a,b),(b,a)));l=u=v
        else:
            l=max(LU[a,b-1][0]+a-1,LU[a-1,b][0]+b-1);u=LU[a,b-1][1]+LU[a-1,b][1];x,y=direct.get((a,b),(0,None));l=max(l,x);u=min(u,y or u)
        assert l<=u;LU[a,b]=LU[b,a]=l,u
h=['|ℓ \\ k|'+'|'.join(map(str,range(1,27)))+'|','|---|'+'---:|'*26];fails=[]
with (D/'ramsey_mixed_field_26.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['l','k','D_v1','R_v1','lower','upper','audit']);
    for a in range(1,27):
        cells=[]
        for b in range(1,27):
            v=R[a,b];d=v-R[a-1,b]-R[a,b-1]+R[a-1,b-1] if min(a,b)>1 else '';l,u=LU[a,b];key=tuple(sorted((a,b)));lo,hi=direct.get(key,(0,None));status='exact' if (a,b) in exact else 'direct violation' if v<lo or hi is not None and v>hi else 'derived violation' if not l<=v<=u else 'within tested bounds';mark={'exact':'','direct violation':'✗','derived violation':'✗ᵈ','within tested bounds':'·'}[status];cells.append(str(d)+mark if d!='' else '—');w.writerow([a,b,d,v,l,u,status]);
            if a<=b and 'violation' in status:fails.append((a,b,v,l,u,status))
        h.append('|'+str(a)+'|'+'|'.join(cells)+'|')
(D/'ramsey_mixed_field_26.md').write_text('# Mixed-gain field: v1 extended unchanged\n\nValues are D; marks audit the reconstructed R: plain = exact input; · = model within tested bounds; ✗ = violates a direct interval; ✗ᵈ = violates a propagated bound; — = undefined. Not an exhaustive literature audit.\n\n'+'\n'.join(h)+'\n',encoding='utf8');print('failures',fails);print('corner',R[26,26],R[26,26]-2*R[25,26]+R[25,25])
