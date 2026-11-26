"""Finite, speculative extrapolation. CSV separates exact input, predictions and mixed differences."""
from fractions import Fraction
from pathlib import Path
import csv

def nearest(x): return int(x + Fraction(1,2))
R={}; exact=set(); out=[]
for a in range(1,14):
    for b in range(a,14):
        if a==1:v=1
        elif a==2:v=b
        elif a==3 and b<=9:v={3:6,4:9,5:14,6:18,7:23,8:28,9:36}[b]
        elif (a,b) in ((4,4),(4,5)):v=18 if b==4 else 25
        else:
            if a==3:v=R[a,b-1]+(b+1)//2
            else:v=nearest(Fraction(57,64)*(R[a-1,b]+R[a,b-1]))
            R[a,b]=R[b,a]=v;continue
        R[a,b]=R[b,a]=v;exact.update(((a,b),(b,a)))
for a in range(1,14):
    row=[]
    for b in range(1,14):
        d=None if min(a,b)==1 else R[a,b]-R[a-1,b]-R[a,b-1]+R[a-1,b-1];row.append(d);out.append((a,b,R[a,b],'exact' if (a,b) in exact else 'model',d))
        if min(a,b)>=2:assert max(R[a-1,b],R[a,b-1])<R[a,b]<=R[a-1,b]+R[a,b-1]
    print(a,*row)
with (Path(__file__).resolve().parents[1]/'results'/'ramsey_conjectural_field_13.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['l','k','R','R_status','D']);w.writerows(out)
print('diagonal',[R[i,i] for i in range(2,14)])
