from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
from check_six_point_chy_localization_algebra import G,LABELS,sij,u,x3,x4,x5
from check_six_point_nmhv_ordering_relations import LAM,TILDE,bracket,square,amplitude

ROOT=Path(__file__).resolve().parents[3];RESULT=ROOT/"research/nima/results/six-point-chy-yang-mills-pfaffian.json"

def eval_poly(expr,C):
 p=sp.Poly(expr,x5,domain=sp.QQ);return sum((c*C**k for (k,),c in p.terms()),sp.zeros(6))
def setup():
 tri={}
 for v in (x3,x4):
  q=[p.as_expr() for p in G.polys if sp.degree(p.as_expr(),v)==1 and p.as_expr().free_symbols<={v,x5}][0];tri[v]=sp.solve(q,v)[0]
 mod=sp.Poly([p.as_expr() for p in G.polys if p.as_expr().free_symbols<={x5}][-1],x5,domain=sp.QQ).monic();cs=mod.all_coeffs()[1:]
 C=sp.zeros(6)
 for i in range(5):C[i+1,i]=1
 for i,c in enumerate(reversed(cs)):C[i,5]=-c
 I=sp.eye(6);Z={1:sp.zeros(6),2:I,3:eval_poly(tri[x3],C),4:eval_poly(tri[x4],C),5:C,6:-I}
 inv=lambda i,j:(Z[i]-Z[j]).inv()
 phi={}
 for i in LABELS:
  for j in LABELS:
   if i!=j:phi[i,j]=sij(i,j)*(inv(i,j)**2)
  phi[i,i]=-sum((phi[i,j] for j in LABELS if j!=i),sp.zeros(6))
 a,b,c=3,4,5;minor=phi[a,a]*(phi[b,b]*phi[c,c]-phi[b,c]*phi[c,b])-phi[a,b]*(phi[b,a]*phi[c,c]-phi[b,c]*phi[c,a])+phi[a,c]*(phi[b,a]*phi[c,b]-phi[b,b]*phi[c,a])
 gauge=(Z[1]-Z[2])*(Z[2]-Z[6])*(Z[6]-Z[1]);detprime=minor*(gauge**-2)
 PT=I
 for r in range(6):PT=PT*inv(LABELS[r],LABELS[(r+1)%6])
 return I,Z,inv,PT,detprime

def ref(i,negative):
 for r in LABELS:
  if r!=i and (square(i,r)!=0 if negative else bracket(LAM[r],LAM[i])!=0):return r
 raise AssertionError("no reference spinor")
def dots(helicity):
 refs={i:ref(i,helicity[i]<0) for i in LABELS}
 ek={};ee={}
 for i in LABELS:
  r=refs[i]
  for j in LABELS:
   if helicity[i]<0:ek[i,j]=sp.cancel(-bracket(LAM[i],LAM[j])*square(j,r)/(2*square(i,r)))
   else:ek[i,j]=sp.cancel(bracket(LAM[r],LAM[j])*square(j,i)/(2*bracket(LAM[r],LAM[i])))
 for i in LABELS: ee[i,i]=sp.Integer(0)
 for i,j in __import__('itertools').combinations(LABELS,2):
  ri,rj=refs[i],refs[j]
  if helicity[i]<0 and helicity[j]<0:value=sp.cancel(bracket(LAM[i],LAM[j])*square(rj,ri)/(2*square(i,ri)*square(j,rj)))
  elif helicity[i]>0 and helicity[j]>0:value=sp.cancel(bracket(LAM[ri],LAM[rj])*square(j,i)/(2*bracket(LAM[ri],LAM[i])*bracket(LAM[rj],LAM[j])))
  elif helicity[i]<0:value=sp.cancel(-bracket(LAM[i],LAM[rj])*square(j,ri)/(2*square(i,ri)*bracket(LAM[rj],LAM[j])))
  else:value=sp.cancel(-bracket(LAM[j],LAM[ri])*square(i,rj)/(2*square(j,rj)*bracket(LAM[ri],LAM[i])))
  ee[i,j]=value;ee[j,i]=value
 return ek,ee

def pfaffian(M,indices,I,memo):
 key=tuple(indices)
 if not key:return I
 if key in memo:return memo[key]
 first=indices[0];total=sp.zeros(6)
 for pos in range(1,len(indices)):
  rest=indices[1:pos]+indices[pos+1:]
  total+=((-1)**(pos+1))*M[first,indices[pos]]*pfaffian(M,rest,I,memo)
 memo[key]=total;return total

def chy(negative,I,Z,inv,PT,detprime):
 h={i:(-1 if i in negative else 1) for i in LABELS};ek,ee=dots(h);M={}
 for i in LABELS:
  for j in LABELS:
   if i!=j:
    M[i-1,j-1]=sp.Rational(1,2)*sij(i,j)*inv(i,j)
    M[i+5,j+5]=ee[i,j]*inv(i,j);M[i+5,j-1]=ek[i,j]*inv(i,j);M[j-1,i+5]=-M[i+5,j-1]
  M[i-1,i-1]=sp.zeros(6);M[i+5,i+5]=sp.zeros(6)
  M[i+5,i-1]=-sum((ek[i,j]*inv(i,j) for j in LABELS if j!=i),sp.zeros(6));M[i-1,i+5]=-M[i+5,i-1]
 # CHY uses twice each Lorentz dot product. Five Pfaffian pairings then
 # supply 2^5; the selected reduced-Pfaffian prefactor is +1.
 M={key:2*value for key,value in M.items()}
 indices=[i for i in range(12) if i not in (0,1)]
 pfprime=pfaffian(M,indices,I,{})
 # Convert the ordered three-variable residue to the unsigned amplitude convention.
 return sp.cancel((-1)**(6-3)*sp.trace(PT*pfprime*detprime.inv()))
def main():
 I,Z,inv,PT,detprime=setup();mhv=chy((1,2),I,Z,inv,PT,detprime);nmhv=chy((1,2,3),I,Z,inv,PT,detprime)
 mhv_target=sp.cancel(bracket(LAM[1],LAM[2])**4/sp.prod(bracket(LAM[i],LAM[i%6+1]) for i in LABELS));nmhv_target=amplitude(LABELS)
 mhv_ratio=sp.cancel(mhv/mhv_target);nmhv_ratio=sp.cancel(nmhv/nmhv_target)
 checks={"mhv_control_matches":mhv_ratio==1,"nmhv_component_matches":nmhv_ratio==1,"common_normalization":mhv_ratio==nmhv_ratio}
 out={"schema":"marici.nima.six_point_chy_yang_mills_pfaffian.result.v1","status":"passed" if all(checks.values()) else "failed","checks":checks,"mhv_chy":str(mhv),"mhv_target":str(mhv_target),"mhv_ratio":str(mhv_ratio),"nmhv_chy":str(nmhv),"nmhv_target":str(nmhv_target),"nmhv_ratio":str(nmhv_ratio),"claim_boundary":"Exact reduced-Pfaffian CHY evaluation matches one MHV control and one NMHV gluon component after applying the declared twice-dot-product matrix convention and multivariate-residue orientation. It does not yet cover all 20 NMHV gluon components or color dressing inside the same checker."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__":main()
