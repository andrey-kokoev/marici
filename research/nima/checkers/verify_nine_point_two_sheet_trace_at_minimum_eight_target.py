"""Independent Pluecker-differential stress check for both-sheet trace bounds."""
import copy,json
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results';mp.mp.dps=95
def m(z):
 z=s.Rational(z);return mp.mpf(int(z.p))/int(z.q)
def contains(bounds,value):return m(bounds[0])<value<m(bounds[1])
def check(report):
 earlier=json.loads((OUT/'nine-point-algebraic-target-local-pushforward.json').read_text())
 assert report['passed'] and report['positive_sheet_coefficient_enclosure']==earlier['local_pushed_target_coefficient_enclosure']
 q=s.symbols('q');P=s.Poly(s.sympify(report['root_polynomial'],locals={'q':q}),q)
 lo,hi=map(s.Rational,report['conjugate_root_interval'])
 assert lo<hi and P.eval(lo)*P.eval(hi)<0
 root=(m(lo)+m(hi))/2
 original=json.loads((OUT/'nine-point-minimum-eight-support.json').read_text())['eight_label_source_witness']
 labels=original['retained_labels'];Z=s.Matrix([[j**k for k in range(6)] for j in labels])
 C=s.Matrix([[s.Rational(v) for v in row] for row in original['source_rows']])[:,[j-1 for j in labels]]
 K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
 a,b,c,d=s.symbols('a b c d');T=s.Matrix([[a,b],[c,d]]);eq=[]
 for i,j in ((0,1),(2,3),(4,5),(6,7)):
  p=s.Poly(s.expand((C+T*K)[0,i]*(C+T*K)[1,j]-(C+T*K)[0,j]*(C+T*K)[1,i]),a,b,c,d)
  assert p.coeff_monomial(a*d)==-p.coeff_monomial(b*c)
  eq.append(p.coeff_monomial(1)+sum(p.coeff_monomial(v)*v for v in (a,b,c,d))+p.coeff_monomial(a*d)*q)
 A,rhs=s.linear_eq_to_matrix(eq,(a,b,c,d));solution=A.inv()*rhs
 Cr=C+T.subs(dict(zip((a,b,c,d),solution)))*K
 field=mp.matrix([[mp.mpf(str(s.N(Cr[i,j].subs(q,s.Float(str(root),95)),90))) for j in range(8)] for i in range(2)])
 gauge=mp.matrix([[field[0,0],field[0,2]],[field[1,0],field[1,2]]])**-1*field
 w=[gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],-gauge[0,6],-gauge[0,7]]
 t=gauge[1,4]/w[2];u=gauge[1,6]/w[4]
 assert min(abs(v) for v in w)>0 and u!=0 and t!=u
 chart=mp.matrix([[1,w[0],0,0,-w[2],-w[3],-w[4],-w[5]],
                  [0,0,1,w[1],w[2]*t,w[3]*t,w[4]*u,w[5]*u]])
 Zm=mp.matrix([[j**k for k in range(6)] for j in labels]);Y=chart*Zm
 def det(i,j):return Y[0,i]*Y[1,j]-Y[0,j]*Y[1,i]
 denom=det(0,1);assert denom!=0
 jac=mp.matrix(8,8)
 for k in range(8):
  V=mp.matrix(2,8)
  if k==0:V[0,1]=1
  elif k==1:V[1,3]=1
  elif 2<=k<=5:
   j=k+2;V[0,j]=-1;V[1,j]=t if k<=3 else u
  elif k==6:V[1,4]=w[2];V[1,5]=w[3]
  else:V[1,6]=w[4];V[1,7]=w[5]
  dY=V*Zm;d0=dY[0,0]*Y[1,1]+Y[0,0]*dY[1,1]-dY[0,1]*Y[1,0]-Y[0,1]*dY[1,0]
  for row in range(2):
   for j in range(2,6):
    i=1 if row==0 else 0;sign=-1 if row==0 else 1
    deriv=dY[0,i]*Y[1,j]+Y[0,i]*dY[1,j]-dY[0,j]*Y[1,i]-Y[0,j]*dY[1,i]
    jac[row*4+j-2,k]=sign*(deriv*denom-det(i,j)*d0)/denom**2
 J=mp.det(jac);source=-1/(mp.fprod(w)*u*(t-u));second=source/J
 assert contains(report['nonpositive_sheet_jacobian_enclosure'],J)
 assert contains(report['nonpositive_sheet_source_coefficient_enclosure'],source)
 assert contains(report['nonpositive_sheet_coefficient_enclosure'],second)
 positive_bounds=earlier['local_pushed_target_coefficient_enclosure']
 trace_bounds=report['full_algebraic_trace_coefficient_enclosure']
 # The published exact trace bound must intersect the sum of independently
 # stress-checked branch bounds; its finer containment is proved by the
 # outward-rational interval construction, not by this numerical check.
 assert m(trace_bounds[0])<m(positive_bounds[1])+second
 assert m(trace_bounds[1])>m(positive_bounds[0])+second
 return True
def main():
 report=json.loads((OUT/'nine-point-fixed-target-two-sheet-trace.json').read_text());assert check(report)
 refused=[]
 for field in ('nonpositive_sheet_jacobian_enclosure','nonpositive_sheet_coefficient_enclosure'):
  bad=copy.deepcopy(report);bad[field]=['0','1']
  try:check(bad)
  except (AssertionError,ValueError):refused.append(field)
  else:raise AssertionError('mutated enclosure accepted')
 result={'passed':True,'independent_pluecker_nonpositive_sheet_stress':True,'mutations_refused':refused,
  'scope':'Numerical stress of the exact interval certificate; not global rational form equality.'}
 (OUT/'nine-point-fixed-target-two-sheet-trace-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
