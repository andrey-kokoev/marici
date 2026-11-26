"""Identify diagonal numerators compatible with the archived intervals, without treating interval midpoints as observations. Replay both frozen models across 1..1000; propagate bounds exactly as in the original audit."""
import csv,json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';src={(int(r['l']),int(r['k'])):tuple(int(r[s]) for s in ('R_v1','lower','upper')) for r in csv.DictReader((D/'ramsey_mixed_field_26.csv').open())};old=list(csv.DictReader((D/'ramsey_diagonal_discount_switch.csv').open()))
def run(n,nums):
 prev={};bad={q:[] for q in nums};changed=0;different_exact=0;near=[]
 for a in range(1,n+1):
  row={}
  for b in range(a,n+1):
   seed=src.get((a,b));fixed=a<=2 or a==3 and b<=9 or (a,b) in ((4,4),(4,5));both=prev.get(b);left=both if a==b else row.get(b-1)
   if fixed:
    z=1 if a==1 else b if a==2 else seed[0];vs=[z]*len(nums);lo=hi=z
   else:
    x,l,u=both;y,m,t=left;vs=[y[i]+(b+1)//2 if a==3 else ((q if a==b and a>=5 else 114)*(x[i]+y[i])+64)//128 for i,q in enumerate(nums)];lo=max(l+b-1,m+a-1);hi=u+t
    if seed:lo=max(lo,seed[1]);hi=min(hi,seed[2])
   if seed:assert (lo,hi)==seed[1:];
   if len(nums)==2 and seed:assert vs[1]==seed[0]
   for q,v in zip(nums,vs):
    if not lo<=v<=hi:bad[q].append((a,b))
   if len(nums)==2 and vs[0]!=vs[1]:
    changed+=1;different_exact+=lo==hi
    if seed and lo<=min(vs)<=max(vs)<=hi:
     near.append((min(min(vs)+1-lo,hi-max(vs)+1),a,b,vs,lo,hi))
   row[b]=(vs,lo,hi)
  prev=row
 return bad,changed,different_exact,sorted(near)[:6]
small=run(26,list(range(129)))[0];scores={q:len(bs) for q,bs in small.items()};best=min(scores.values());big,changed,exact,near=run(1000,[113,114]);r=dict(minimum_violations=best,best_numerators=[q for q,c in scores.items() if c==best],million_grid_violations=big,disagree_unordered=changed,disagree_exact=exact,nearest_separating_bounds=near);print(r);(D/'ramsey_discount_identification.json').write_text(json.dumps(r)+'\n')
