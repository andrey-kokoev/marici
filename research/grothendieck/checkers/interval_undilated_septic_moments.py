"""Directed rational intervals for c=1 finite septic Laplace moments."""
from fractions import Fraction as F
from math import comb, factorial
import json, pathlib, sys
sys.path.insert(0,str(pathlib.Path(__file__).parents[2]/'nima'/'checkers'))
import preconditioned_spline_weil as n
Z=n.Z
BASE=[F(1),F(-5),F(33,4),F(-5),F(1)]; BM=[2,1,0,-1,-2]
CROSS=[F(1,2),F(-5,2),F(37,8),F(-5),F(37,8),F(-5,2),F(1,2)]; CM=[3,2,1,0,-1,-2,-3]
def lag_coeff(k):
 v={m:c for m,c in zip(BM,BASE)};ms=list(range(2+k,-3-k,-1))
 return [F(1,2)*(v.get(m-k,F(0))+v.get(m+k,F(0))) for m in ms],ms
L2,L2M=lag_coeff(2);L3,L3M=lag_coeff(3);L4,L4M=lag_coeff(4);L5,L5M=lag_coeff(5);L6,L6M=lag_coeff(6)
_EXP={};_SQRT2=n.sqrt_q(F(2))
def exp_one(x):
 if x not in _EXP:_EXP[x]=n.exp_q(x)
 return _EXP[x]
def iv_pow(a,k):
 if k<0:return n.inv(iv_pow(a,-k))
 out=(F(1),F(1));base=a
 while k:
  if k&1:out=n.mul(out,base)
  base=n.mul(base,base);k//=2
 return out
def negative_exp_factor(m,j,i):
 # exp((i+1/4)(ma+4-j)) = exp((i+1/4)(4-j))*sqrt(2)^(4im+m).
 knot=(F(4*i+1,4)*F(4-j));e=exp_one(knot)
 return n.mul(e,iv_pow(_SQRT2,4*i*m+m))
def J(b,s,m,j,i):
 if s[0]>=0: y=s;factor=(F(1),F(1))
 elif s[1]<=0: y=Z;factor=negative_exp_factor(m,j,i)
 else: raise AssertionError('knot sign unresolved')
 by=n.scale(b,y);poly=Z
 for r in range(8): poly=n.add(poly,n.scale(F(1,factorial(r)),n.pow_pos(by,r)))
 return n.scale(b**-8,n.mul(factor,poly))
def moment(b,a,cs,ms,i):
 out=Z
 for c,m in zip(cs,ms):
  for j in range(9):
   s=n.add(n.scale(F(m),a),(F(4-j),F(4-j)))
   out=n.add(out,n.scale(c*F((-1)**j*comb(8,j)),J(b,s,m,j,i)))
 return out
def enc(x):return [str(x[0]),str(x[1])]
def main():
 a=n.scale(F(2),n.log_q(F(2)));rows=[]
 scouts={('baseline',0):'0.46230108744927819962243646708542235',('baseline',1):'0.89027588857624307847720024851196792',('baseline',2):'0.80345297306923659860338883939827334',('baseline',3):'0.66872144889633627730551648917728647',('cross',0):'0.07353127229514322797102477913856001',('cross',1):'-0.22467948245869954578407016413575588',('cross',2):'-0.29263602431462840006539067213299917',('cross',3):'-0.27376238261924416296319275381633414',('lag2',0):'-0.028866934364186052915738235541315494',('lag2',1):'-0.19123994391337015504840427656819677',('lag2',2):'-0.11700673271247789064482174363658726',('lag2',3):'-0.069895620676766582742938874427880557'}
 for name,cs,ms in [('baseline',BASE,BM),('cross',CROSS,CM),('lag2',L2,L2M),('lag3',L3,L3M),('lag4',L4,L4M),('lag5',L5,L5M),('lag6',L6,L6M)]:
  for i in range(8):
   value=moment(F(i)+F(1,4),a,cs,ms,i);tol=F(1,10**33)
   if (name,i) in scouts:
    q=F(scouts[(name,i)]);assert value[0]<=q+tol and q-tol<=value[1],(name,i,float(value[0]),float(value[1]),float(q))
   rows.append({'profile':name,'n':i,'interval':enc(value),'width':str(value[1]-value[0])})
 result={'schema':'marici.grothendieck.interval-undilated-septic-moments-n8.v1','rows':rows,'passed':True}
 out=pathlib.Path(__file__).parents[1]/'results/interval-undilated-septic-moments.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':True,'max_width_float':float(max(F(r['width']) for r in rows))}))
if __name__=='__main__':main()
