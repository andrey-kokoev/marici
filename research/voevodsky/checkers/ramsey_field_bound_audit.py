"""Audit v1 against selected bounds transcribed from Radziszowski DS1 rev.18 (2026), Tables Ia/Ib. Emit a separately labeled, bound-conditioned v2; never overwrite v1."""
import csv
from pathlib import Path
from fractions import Fraction
D=Path(__file__).resolve().parents[1]/'results'
old={(int(z['l']),int(z['k'])):int(z['R']) for z in csv.DictReader((D/'ramsey_conjectural_field_13.csv').open())}
# Each triple is (first column, inclusive lower bounds, inclusive upper bounds).
rows={3:(10,[40,47,53,61],[41,50,59,68]),4:(6,[36,49,59,73,92,102,128,139],[40,58,79,105,135,170,210,256]),5:(5,[43,59,80,101,133,149,183,203,233],[46,85,133,193,282,381,511,672,860]),6:(6,[102,115,134,183,204,262,294,347],[160,270,423,651,944,1346,1855,2499]),7:(7,[205,219,252,292,405,417,511],[492,832,1368,2119,3197,4665,6653]),8:(8,[282,329,343],[1518,2662,4402]),9:(9,[565,581],[4956,8675]),10:(10,[798],[16064])}
bounds={}
for a,(b,lo,hi) in rows.items():
    for j,(L,U) in enumerate(zip(lo,hi,strict=True)):bounds[a,b+j]=L,U
r={};out=[];fail=[]
for a in range(1,14):
    for b in range(a,14):
        x=old[a,b]; raw=x if a<=2 or a==3 and b<=9 or (a,b) in [(4,4),(4,5)] else (r[a,b-1]+(b+1)//2 if a==3 else int(Fraction(57,64)*(r[a-1,b]+r[a,b-1])+Fraction(1,2)));v=raw
        if (a,b) in bounds:
            L,U=bounds[a,b];v=min(max(raw,L),U)
            if not L<=x<=U:fail.append((a,b,x,L,U))
        r[a,b]=r[b,a]=v
for a in range(1,14):
    for b in range(1,14):
        L,U=bounds.get(tuple(sorted((a,b))),('','')); d=None if min(a,b)==1 else r[a,b]-r[a-1,b]-r[a,b-1]+r[a-1,b-1];out.append((a,b,old[a,b],L,U,r[a,b],d))
        if min(a,b)>1:assert max(r[a-1,b],r[a,b-1])<r[a,b]<=r[a-1,b]+r[a,b-1]
with (D/'ramsey_field_bound_audit_v2.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['l','k','R_v1','survey_lower','survey_upper','R_bound_conditioned_v2','D_v2']);w.writerows(out)
print('checked',len(bounds),'failed',fail,'changed_unordered',sum(old[a,b]!=r[a,b] for a in range(1,14) for b in range(a,14)),'corner',r[13,13]);print('row3', [r[3,b] for b in range(9,14)])
