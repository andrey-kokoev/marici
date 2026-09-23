"""Independent high-precision Pluecker stress check for exact interval packet."""
import copy,json
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
mp.mp.dps=95
q=s.symbols('q');prior=json.loads((OUT/'nine-point-paired-cell-exact.json').read_text())
poly=s.Poly(s.sympify(prior['quadratic_graph_polynomial'],locals={'q':q}),q)
def m(z):
 z=s.Rational(z);return mp.mpf(int(z.p))/int(z.q)
def contains(pair,value):return m(pair[0])<value<m(pair[1])
def verify(packet,upper):
 left,right=map(s.Rational,packet['refined_positive_root_interval'])
 assert left<right and poly.eval(left)*poly.eval(right)<0
 center=(m(left)+m(right))/2
 labels=upper['eight_label_source_witness']['retained_labels'];assert labels==[1,2,4,5,6,7,8,9]
 C=s.Matrix([[s.Rational(v) for v in row] for row in upper['eight_label_source_witness']['source_rows']])[:,[j-1 for j in labels]]
 Z=s.Matrix([[j**d for d in range(6)] for j in labels]);K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
 a,b,c,d=s.symbols('a b c d');T=s.Matrix([[a,b],[c,d]])
 pairs=((0,1),(2,3),(4,5),(6,7));eq=[]
 # Form the affine lift from constant/linear coefficients and a*d.
 for i,j in pairs:
  raw=s.Poly(s.expand((C+T*K)[0,i]*(C+T*K)[1,j]-(C+T*K)[0,j]*(C+T*K)[1,i]),a,b,c,d)
  assert raw.coeff_monomial(a*d)==-raw.coeff_monomial(b*c)
  eq.append(raw.coeff_monomial(1)+sum(raw.coeff_monomial(v)*v for v in (a,b,c,d))+raw.coeff_monomial(a*d)*q)
 M,rhs=s.linear_eq_to_matrix(eq,(a,b,c,d));sol=M.inv()*rhs
 Cz=C+T.subs(dict(zip((a,b,c,d),sol)))*K
 F=mp.matrix([[mp.mpf(str(s.N(Cz[i,j].subs(q,s.Float(str(center),95)),90))) for j in range(8)] for i in range(2)])
 base=mp.matrix([[F[0,0],F[0,2]],[F[1,0],F[1,2]]]);D=base**-1*F
 ws=[D[0,1],D[1,3],-D[0,4],-D[0,5],-D[0,6],-D[0,7]]
 t=D[1,4]/ws[2];u=D[1,6]/ws[4];assert min(ws)>0 and t>u>0
 W=mp.matrix([[1,ws[0],0,0,-ws[2],-ws[3],-ws[4],-ws[5]],
              [0,0,1,ws[1],ws[2]*t,ws[3]*t,ws[4]*u,ws[5]*u]])
 Zm=mp.matrix([[j**d for d in range(6)] for j in labels]);Y=W*Zm
 def det(i,j):return Y[0,i]*Y[1,j]-Y[0,j]*Y[1,i]
 denom=det(0,1);assert denom!=0
 jac=mp.matrix(8,8)
 for k in range(8):
  V=mp.matrix(2,8)
  if k==0:V[0,1]=1
  if k==1:V[1,3]=1
  if 2<=k<=5:
   j=k+2;V[0,j]=-1;V[1,j]=t if k<=3 else u
  if k==6:V[1,4]=ws[2];V[1,5]=ws[3]
  if k==7:V[1,6]=ws[4];V[1,7]=ws[5]
  dY=V*Zm;d0=dY[0,0]*Y[1,1]+Y[0,0]*dY[1,1]-dY[0,1]*Y[1,0]-Y[0,1]*dY[1,0]
  for row in range(2):
   for j in range(2,6):
    i=1 if row==0 else 0;sgn=-1 if row==0 else 1
    dn=dY[0,i]*Y[1,j]+Y[0,i]*dY[1,j]-dY[0,j]*Y[1,i]-Y[0,j]*dY[1,i]
    jac[row*4+j-2,k]=sgn*(dn*denom-det(i,j)*d0)/denom**2
 J=mp.det(jac);source=-1/(mp.fprod(ws)*u*(t-u));pushed=source/J
 assert contains(packet['jacobian_enclosure'],J)
 assert contains(packet['oriented_source_coefficient_enclosure'],source)
 assert contains(packet['local_pushed_target_coefficient_enclosure'],pushed)
 other=-(m(poly.nth(1))/m(poly.nth(2)))-center
 i,j=(labels.index(z) for z in packet['other_root_negative_minor'])
 M2=mp.matrix([[mp.mpf(str(s.N(Cz[r,col].subs(q,s.Float(str(other),95)),75))) for col in range(8)] for r in range(2)])
 assert M2[0,i]*M2[1,j]-M2[0,j]*M2[1,i]<0
 return True
def main():
 packet=json.loads((OUT/'nine-point-algebraic-target-local-pushforward.json').read_text())
 upper=json.loads((OUT/'nine-point-minimum-eight-support.json').read_text());assert verify(packet,upper)
 refused=[]
 for key in ('jacobian_enclosure','oriented_source_coefficient_enclosure','local_pushed_target_coefficient_enclosure'):
  bad=copy.deepcopy(packet);bad[key]=['0','1']
  try:verify(bad,upper)
  except (AssertionError,ValueError):refused.append(key)
  else:raise AssertionError('mutated bound passed')
 result={'passed':True,'independent_pluecker_differential_stress':True,
 'mutated_bounds_refused':refused,'scope':'High-precision independent stress of exact rational interval packet; exact interval certification is in the construction checker.'}
 (OUT/'nine-point-algebraic-target-local-pushforward-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
