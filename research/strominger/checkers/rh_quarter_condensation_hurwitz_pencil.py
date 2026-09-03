import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
def trim(p):
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def add(p,q,s=F(1)):
 r=[F(0)]*max(len(p),len(q))
 for i,x in enumerate(p):r[i]+=x
 for i,x in enumerate(q):r[i]+=s*x
 return trim(r)
def mul(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):r[i+j]+=x*y
 return trim(r)
def exact(p,q):
 p=p[:];z=[F(0)]*max(1,len(p)-len(q)+1)
 while len(p)>=len(q) and any(p):
  d=len(p)-len(q);c=p[-1]/q[-1];z[d]=c;p=add(p,[F(0)]*d+[c*x for x in q],F(-1))
 assert p==[F(0)];return trim(z)
def Q(s):
 p=[F(1)]
 for c in (F(1),F(5,4),F(3,2),F(7,4)):p=mul(p,[c+s,F(1)])
 return p
@lru_cache(None)
def D(n,s):
 if n<=1:return [F(1)]
 X=mul(mul(Q(s+n-1),D(n-1,s)),D(n-1,s+2));Y=mul(mul(Q(s),D(n-1,s+1)),D(n-1,s+1));return exact(add(X,Y,F(-1)),D(n-2,s+2))
def routh(p):
 b=list(reversed(p));cols=(len(b)+1)//2;R=[[F(0)]*cols for _ in b];R[0][:]=b[0::2]+[F(0)]*(cols-len(b[0::2]));R[1][:]=b[1::2]+[F(0)]*(cols-len(b[1::2]))
 for i in range(2,len(b)):
  if R[i-1][0]==0:return False,i
  for j in range(cols-1):R[i][j]=(R[i-1][0]*R[i-2][j+1]-R[i-2][0]*R[i-1][j+1])/R[i-1][0]
  if R[i][0]<=0:return False,i
 return R[0][0]>0 and R[1][0]>0,None
records=[];first_failure=None
for n in range(2,7):
 for s in range(3):
  X=mul(mul(Q(s+n-1),D(n-1,s)),D(n-1,s+2));Y=mul(mul(Q(s),D(n-1,s+1)),D(n-1,s+1))
  for j in range(9):
   t=F(j,8);p=add(X,Y,-t);ok,row=routh(p);rec={"order":n,"shift_offset":s,"t":str(t),"hurwitz_stable":ok,"first_nonpositive_row":row};records.append(rec)
   if not ok and first_failure is None:first_failure=rec
checks={"entire_sampled_pencil_hurwitz_stable":first_failure is None,"endpoints_included":{r["t"] for r in records}>={"0","1"},"tested_135_pencil_members":len(records)==135,"condensation_endpoint_stable":all(r["hurwitz_stable"] for r in records if r["t"]=="1")}
result={"schema":"marici.strominger.rh_quarter_condensation_hurwitz_pencil.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact Routh arrays test the condensation pencil X-tY at ninth-grid parameters t in [0,1]. Stability of every sampled member would support a proper-position closure; a failure identifies where subtraction exits the Hurwitz cone. The result is finite and does not prove the continuous pencil stable.","record_count":len(records),"first_failure":first_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_condensation_hurwitz_pencil.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
