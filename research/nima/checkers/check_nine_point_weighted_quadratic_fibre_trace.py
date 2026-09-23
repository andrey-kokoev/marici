"""Evaluate full Jacobian-weighted four-mass trace in an irreducible quadratic field."""
import contextlib,io,json,os
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_genuinely_quadratic_four_mass_fibre as previous
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
idx=int(os.environ.get('NIMA_WEIGHTED_TRACE_WITNESS_INDEX','0'));assert idx in (0,1)
D,variables,Z,K,R=previous.D,previous.variables,previous.Z,previous.K,previous.R
source_row=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows'][idx]
point=dict(zip(variables,[s.Rational(v) for v in source_row['weights']]+[s.Rational(source_row['t']),s.Rational(source_row['u'])]))
initial=D.subs(point);epsilon=s.Rational(previous.rows[idx]['rational_target_perturbation'])
deltaY=s.zeros(2,6);deltaY[0,4]=epsilon
Y=initial*Z+deltaY;Cbar=initial+deltaY*R
assert Cbar*Z==Y
qa,qb,qc,qd,q=s.symbols('a b c d q');T=s.Matrix([[qa,qb],[qc,qd]])
F=Cbar+T*K

def pairminor(M,i,j):return s.det(s.Matrix.hstack(M[:,i],M[:,j]))

def lifted(i,j):
 p=s.Poly(pairminor(F,i,j),qa,qb,qc,qd)
 assert p.coeff_monomial(qa*qd)==-p.coeff_monomial(qb*qc)
 return p.coeff_monomial(1)+sum(p.coeff_monomial(v)*v for v in (qa,qb,qc,qd))+p.coeff_monomial(qa*qd)*q
M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))],(qa,qb,qc,qd))
sol=M.inv()*rhs
P=s.Poly(q-sol[0]*sol[3]+sol[1]*sol[2],q)
assert [str(v) for v in P.all_coeffs()]==previous.rows[idx]['inverse_quadratic_coefficients']
A,B,C=P.all_coeffs();S=s.factor(-B/A);V=s.factor(C/A)
class Q2:
 __slots__=('a','b')
 def __init__(self,a=0,b=0):self.a=s.Rational(a);self.b=s.Rational(b)
 @staticmethod
 def cast(x):return x if isinstance(x,Q2) else Q2(x)
 def __add__(self,other):
  other=self.cast(other);return Q2(self.a+other.a,self.b+other.b)
 __radd__=__add__
 def __neg__(self):return Q2(-self.a,-self.b)
 def __sub__(self,other):return self+-self.cast(other)
 def __rsub__(self,other):return self.cast(other)+-self
 def __mul__(self,other):
  other=self.cast(other)
  return Q2(self.a*other.a-self.b*other.b*V,self.a*other.b+self.b*other.a+self.b*other.b*S)
 __rmul__=__mul__
 def inverse(self):
  norm=self.a*self.a+self.a*self.b*S+self.b*self.b*V
  assert norm!=0
  return Q2((self.a+self.b*S)/norm,-self.b/norm)
 def __truediv__(self,other):return self*self.cast(other).inverse()
 def __rtruediv__(self,other):return self.cast(other)*self.inverse()
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=Q2(1)
  for _ in range(n):out=out*self
  return out
 def trace(self):return 2*self.a+self.b*S
 def iszero(self):return self.a==0 and self.b==0

def from_expr(expr):
 numerator,denominator=s.together(expr).as_numer_denom()
 n=s.rem(s.Poly(numerator,q),P);d=s.rem(s.Poly(denominator,q),P)
 N=Q2(n.nth(0),n.nth(1));D=Q2(d.nth(0),d.nth(1))
 return N/D

def mm(A,B):return [[sum((x*y for x,y in zip(row,col)),Q2()) for col in zip(*B)] for row in A]
def det2(X):return X[0][0]*X[1][1]-X[0][1]*X[1][0]
def inverse2(X):
 det=det2(X)
 return [[X[1][1]/det,-X[0][1]/det],[-X[1][0]/det,X[0][0]/det]]
def determinant(matrix):
 rows=[row[:] for row in matrix];out=Q2(1);n=len(rows)
 for j in range(n):
  pivot=next((i for i in range(j,n) if not rows[i][j].iszero()),None)
  assert pivot is not None
  if pivot!=j:rows[j],rows[pivot]=rows[pivot],rows[j];out=-out
  elem=rows[j][j];out=out*elem
  for i in range(j+1,n):
   if rows[i][j].iszero():continue
   coeff=rows[i][j]/elem
   for k in range(j+1,n):rows[i][k]=rows[i][k]-coeff*rows[j][k]
   rows[i][j]=Q2()
 return out

Ft=(Cbar+T*K).subs(dict(zip((qa,qb,qc,qd),sol)))
Ffield=[[from_expr(Ft[i,j]) for j in range(8)] for i in range(2)]
cols=[[Ffield[0][j],Ffield[1][j]] for j in (0,2)]
G=inverse2([[cols[j][i] for j in range(2)] for i in range(2)])
Cg=mm(G,Ffield)
# Source chart parameters are recovered in exactly the authored gauge.
w=[Cg[0][1],Cg[1][3],-Cg[0][4],-Cg[0][5],-Cg[0][6],-Cg[0][7]]
t=-Cg[1][4]/Cg[0][4];u=-Cg[1][6]/Cg[0][6]
parameters=w+[t,u]
source=-Q2(1)
for v in w:source=source/v
source=source/u/(t-u)
H=[[Q2(Y[i,j]) for j in (4,5)] for i in range(2)]
Bchart=mm(inverse2(H),[[Q2(Y[i,j]) for j in range(4)] for i in range(2)])
prefix=mm(inverse2(H),[[Ffield[i][j] for j in (0,2)] for i in range(2)])
Zfield=[[Q2(Z[i,j]) for j in range(6)] for i in range(8)]
derivatives=[]
for v in variables:
 matrix=D.diff(v)
 dD=[]
 for i in range(2):
  out=[]
  for j in range(8):
   poly=s.Poly(matrix[i,j],variables)
   element=Q2()
   for powers,coefficient in poly.terms():
    factor=Q2(coefficient)
    for k,power in enumerate(powers):factor=factor*parameters[k]**power
    element=element+factor
   out.append(element)
  dD.append(out)
 dY=mm(dD,Zfield)
 correction=mm([[dY[i][j] for j in (4,5)] for i in range(2)],Bchart)
 diff=[[dY[i][j]-correction[i][j] for j in range(4)] for i in range(2)]
 deriv=mm(prefix,diff)
 derivatives.append([deriv[i][j] for i in range(2) for j in range(4)])
J=determinant([[derivatives[col][r] for col in range(8)] for r in range(8)])
weight=source/J
px=Cg[0][0]*Cg[1][4]-Cg[0][4]*Cg[1][0]
py=Cg[0][1]*Cg[1][5]-Cg[0][5]*Cg[1][1]
assert not weight.iszero() and not px.iszero() and not py.iszero()
moments=[(weight*px**(4-j)*py**j).trace() for j in range(5)]
hankel=s.Matrix(3,3,lambda i,j:moments[i+j])
assert hankel.rank()==2 and hankel.det()==0
assert weight.b!=0
# Independent control: evaluate field elements at both exact radicals,
# reconstruct the target-chart Jacobian directly with SymPy at 35 digits.
roots=s.solve(P.as_expr(),q);assert len(roots)==2
for root in roots:
 root_numeric=s.N(root,70)
 assert abs(complex(s.N(P.eval(root_numeric),30)))<1e-20,s.N(P.eval(root_numeric),30)
 assert abs(complex(s.N(weight.a+weight.b*root_numeric,30)))>1e-25
# Independent numerical Jacobian: rebuild the sourced D matrix and its
# full 8x8 chart derivative without using quotient-field matrix algebra.
rnum=s.N(roots[0],75)
values=[s.N(x.a+x.b*rnum,75) for x in parameters]
subs=dict(zip(variables,values));Cn=D.subs(subs);Yn=Cn*Z
Hn=Yn[:,4:6];Bn=Hn.inv()*Yn[:,:4]
cols=[]
for variable in variables:
 derivative=D.diff(variable).subs(subs)*Z
 dBn=Hn.inv()*(derivative[:,:4]-derivative[:,4:6]*Bn)
 cols.append(s.Matrix(list(dBn)))
Jnum=s.Matrix.hstack(*cols).det(method='berkowitz')
sourced=-s.S.One/(s.prod(values[:6])*values[7]*(values[6]-values[7]))
predicted=s.N(weight.a+weight.b*rnum,65)
relative=s.N((sourced/Jnum-predicted)/predicted,35)
assert abs(complex(relative))<1e-25,relative
report={'schema':'marici.nima.nine-point-weighted-quadratic-fibre-trace.v1','passed':True,
 'witness_index':idx,'source_weights':source_row['weights'],'rational_target_perturbation':str(epsilon),
 'inverse_quadratic_coefficients':[str(v) for v in P.all_coeffs()],
 'single_sheet_oriented_source_over_target_jacobian_coefficients':[str(weight.a),str(weight.b)],
 'single_sheet_weight_genuinely_irrational':True,
 'complete_two_sheet_jacobian_weighted_trace':str(weight.trace()),
 'five_flavor_selected_full_weighted_trace_moments':[str(v) for v in moments],
 'rank_two_weighted_hankel':True,
 'independent_direct_numeric_eight_by_eight_jacobian_control':True,
 'scope':'Exact Q[q]/P arithmetic performs the full 8x8 target-chart Jacobian and source dlog weight without floating radical evaluation. The oriented weighted coefficient and all five flavor-selected moment traces are rational even though each individual sheet weight is irrational. The source inverse is the genuinely irreducible quadratic witness; the result is a complex two-sheet fibre contour, not the complete positive image canonical form.'}
filename='nine-point-weighted-quadratic-fibre-trace'+('-witness2' if idx else '')+'.json'
(OUT/filename).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'witness_index':idx,'weighted_trace_rational':True,'hankel_rank':2},indent=2))
