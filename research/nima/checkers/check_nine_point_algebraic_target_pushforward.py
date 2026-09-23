"""Rigorous interval enclosure of the local pushed form at the minimum-eight target."""
import json
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
base=json.loads((OUT/'nine-point-minimum-eight-support.json').read_text())['eight_label_source_witness']
prior=json.loads((OUT/'nine-point-paired-cell-exact.json').read_text());assert prior['passed']
labels=base['retained_labels'];Z=[[Q(j**d) for d in range(6)] for j in labels]
Zs=s.Matrix(Z);Ks=s.Matrix([list(-Zs[6,:]*Zs[:6,:].inv())+[1,0],list(-Zs[7,:]*Zs[:6,:].inv())+[0,1]])
K=[[Q(str(Ks[i,j])) for j in range(8)] for i in range(2)]
C=[[Q(base['source_rows'][i][j-1]) for j in labels] for i in range(2)]
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
def lifted(i,j):
 const=C[0][i]*C[1][j]-C[0][j]*C[1][i]
 linear=sum(T[0,p]*(K[p][i]*C[1][j]-K[p][j]*C[1][i])+T[1,p]*(C[0][i]*K[p][j]-C[0][j]*K[p][i]) for p in range(2))
 return s.expand(s.Rational(const.numerator,const.denominator)+linear+q*(K[0][i]*K[1][j]-K[0][j]*K[1][i]))
pairs=((0,1),(2,3),(4,5),(6,7));mat,rhs=s.linear_eq_to_matrix([lifted(*p) for p in pairs],(a,b,c,d));assert mat.det()!=0
solution=[s.factor(z) for z in mat.inv()*rhs]
P=s.Poly(q-solution[0]*solution[3]+solution[1]*solution[2],q)
assert s.expand(P.as_expr()-s.sympify(prior['quadratic_graph_polynomial'],locals={'q':q}))==0
GRID=10**80
class Interval:
 def __init__(self,lo,hi=None):
  lo=Q(lo);hi=Q(hi if hi is not None else lo)
  self.lo=Q(lo.numerator*GRID//lo.denominator,GRID)
  self.hi=Q(-((-hi.numerator*GRID)//hi.denominator),GRID)
  assert self.lo<=self.hi
 def __add__(self,o):
  o=iv(o);return Interval(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return Interval(-self.hi,-self.lo)
 def __sub__(self,o):return self+-iv(o)
 def __rsub__(self,o):return iv(o)+-self
 def __mul__(self,o):
  o=iv(o);v=[x*y for x in (self.lo,self.hi) for y in (o.lo,o.hi)];return Interval(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=iv(o);assert not(o.lo<=0<=o.hi)
  return self*Interval(1/o.hi,1/o.lo)
 def __rtruediv__(self,o):return iv(o)/self
 def contains_zero(self):return self.lo<=0<=self.hi
 def __repr__(self):return f'[{self.lo},{self.hi}]'
def iv(o):return o if isinstance(o,Interval) else Interval(o)
def fq(z):return Q(int(s.numer(z)),int(s.denom(z)))
coeff=[fq(P.nth(i)) for i in range(3)]
def evalp(x):return (coeff[2]*x+coeff[1])*x+coeff[0]
left,right=map(Q,prior['unique_root_interval']);assert evalp(left)*evalp(right)<0
for _ in range(130):
 mid=(left+right)/2
 if evalp(left)*evalp(mid)<0:right=mid
 else:left=mid
assert right-left<Q(1,10**45)
root=Interval(left,right)
def affine(expr,interval):
 poly=s.Poly(expr,q);assert poly.degree()<=1
 return iv(fq(poly.nth(0)))+iv(fq(poly.nth(1)))*interval
coef=[affine(v,root) for v in solution]
source=[[iv(C[i][j])+sum(coef[2*i+p]*K[p][j] for p in range(2)) for j in range(8)] for i in range(2)]
def determinant(M):
 work=[row[:] for row in M];n=len(work);prod=iv(1);sign=1
 for k in range(n):
  pivot=max(range(k,n),key=lambda h: abs(float((work[h][k].lo+work[h][k].hi)/2)))
  assert not work[pivot][k].contains_zero(),('unresolved interval pivot',k)
  if pivot!=k:work[k],work[pivot]=work[pivot],work[k];sign=-sign
  value=work[k][k];prod=prod*value
  for i in range(k+1,n):
   factor=work[i][k]/value
   for j in range(k+1,n):work[i][j]=work[i][j]-factor*work[k][j]
 return prod*sign
# Source GL2 gauge C1=e1 and C4=e2, with a normalized pair scale.
x,y=source[0][0],source[1][0];v,w=source[0][2],source[1][2]
Delta=x*w-y*v;assert not Delta.contains_zero()
D=[[ (w*source[0][j]-v*source[1][j])/Delta for j in range(8)],
   [(-y*source[0][j]+x*source[1][j])/Delta for j in range(8)]]
weights=[D[0][1],D[1][3],-D[0][4],-D[0][5],-D[0][6],-D[0][7]]
t=D[1][4]/weights[2];u=D[1][6]/weights[4]
assert all(z.lo>0 for z in weights) and (t-u).lo>0 and u.lo>0
for j in (4,5):assert (D[1][j]-weights[j-2]*t).contains_zero()
for j in (6,7):assert (D[1][j]-weights[j-2]*u).contains_zero()
# The relations above are exact ONLY at the polynomial root; interval
# containment by zero is necessary, and source positivity was proven in
# the exact cell packet. Construct the exact chart model from its weights.
chart=[[iv(1),weights[0],iv(0),iv(0),-weights[2],-weights[3],-weights[4],-weights[5]],
       [iv(0),iv(0),iv(1),weights[1],weights[2]*t,weights[3]*t,weights[4]*u,weights[5]*u]]
def projected(mat):return [[sum(mat[i][j]*Z[j][r] for j in range(8)) for r in range(6)] for i in range(2)]
Y=projected(chart);A=[[Y[0][0],Y[0][1]],[Y[1][0],Y[1][1]]];detA=A[0][0]*A[1][1]-A[0][1]*A[1][0];assert not detA.contains_zero()
R=[[A[1][1]/detA,-A[0][1]/detA],[-A[1][0]/detA,A[0][0]/detA]]
def leftmul(left,m):return [[sum(left[i][k]*m[k][j] for k in range(2)) for j in range(len(m[0]))] for i in range(2)]
B=leftmul(R,[row[2:] for row in Y]);cols=[]
for z in range(8):
 deriv=[[iv(0) for _ in range(8)] for _ in range(2)]
 if z==0:deriv[0][1]=iv(1)
 if z==1:deriv[1][3]=iv(1)
 if z in (2,3,4,5):
  j=z+2;deriv[0][j]=iv(-1);deriv[1][j]=t if z<=3 else u
 if z==6:deriv[1][4]=weights[2];deriv[1][5]=weights[3]
 if z==7:deriv[1][6]=weights[4];deriv[1][7]=weights[5]
 dY=projected(deriv)
 dB=leftmul(R,[[dY[i][j+2]-sum(dY[i][k]*B[k][j] for k in range(2)) for j in range(4)] for i in range(2)])
 cols.append([dB[i][j] for i in range(2) for j in range(4)])
jac=determinant([[cols[z][i] for z in range(8)] for i in range(8)]);assert not jac.contains_zero()
weightprod=iv(1)
for weight in weights:weightprod=weightprod*weight
sourcecoef=-iv(1)/(u*(t-u)*weightprod);pushed=sourcecoef/jac
# The other algebraic graph root cannot belong to the positive cell:
# identify one uniformly NEGATIVE nonpaired minor on its root interval.
other=Interval(-coeff[1]/coeff[2])-root;assert other.hi<root.lo
negative=[]
for i,j in combinations(range(8),2):
 if (i,j) in pairs:continue
 m=affine(lifted(i,j).subs(dict(zip((a,b,c,d),solution))),other)
 if m.hi<0:negative.append([labels[i],labels[j]])
assert negative
def outward(z,digits=12):
 scale=10**digits;lo=z.lo.numerator*scale//z.lo.denominator
 hi=-((-z.hi.numerator*scale)//z.hi.denominator)
 # A safe enclosing decimal grid (lo/scale <= z <= hi/scale).
 assert Q(lo,scale)<=z.lo<=z.hi<=Q(hi,scale)
 return [str(Q(lo,scale)),str(Q(hi,scale))]
result={'schema':'marici.nima.nine-point-algebraic-target-local-pushforward.v1','passed':True,
 'algebraic_kernel_area_polynomial':str(P.as_expr()),'refined_positive_root_interval':[str(left),str(right)],
 'other_root_interval':[str(other.lo),str(other.hi)],'other_root_negative_minor':negative[0],
 'jacobian_enclosure':outward(jac),'oriented_source_coefficient_enclosure':outward(sourcecoef),
 'local_pushed_target_coefficient_enclosure':outward(pushed),
 'target_coordinates':'B=(CZ[:,0:2])^-1 CZ[:,2:6], row-major',
 'scope':'Rigorous rational-interval local form coefficient at the exact minimum-eight-support target, and exclusion of the only other graph root from this paired cell. Not a global pushforward/history equality.'}
(OUT/'nine-point-algebraic-target-local-pushforward.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'local_form_coefficient_enclosure':result['local_pushed_target_coefficient_enclosure'],
 'jacobian_enclosure':result['jacobian_enclosure'],'other_root_negative_minor':negative[0]},indent=2))
