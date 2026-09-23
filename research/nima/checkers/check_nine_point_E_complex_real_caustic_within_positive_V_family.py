"""Find the E algebraic real/complex caustic inside a regular positive V target family."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_relabelled_cells_miss_vertical_image as prev
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=prev.D,prev.vars
w2,w4,w5,w6,w7,w8,t,u=vars
e=s.symbols('e',real=True,positive=True)
p=dict(zip(vars,(e,1,1,1,1,1,3,2)))
V=D.subs(p).copy();V[0,1]=0;V[1,1]=e
Z9=prev.Z9;ZA=Z9[[0,1,3,4,5,6,7,8],:];ZE=prev.ZE
Y=V*ZA;H=Y[:,:2];assert s.factor(H.det())!=0
B=H.inv()*Y[:,2:];zA=ZA[:,2:]-ZA[:,:2]*B
Vs=D.copy();Vs[0,1]=0;Vs[1,1]=w2
JV=s.factor(s.Matrix.hstack(*[s.Matrix(list(Vs.diff(v).subs(p)*zA)) for v in vars]).det(method='domain-ge'))
assert JV!=0
start=(Y*ZE[:6,:].inv()).row_join(s.zeros(2,2))
K=s.Matrix([list(-ZE[6,:]*ZE[:6,:].inv())+[1,0],list(-ZE[7,:]*ZE[:6,:].inv())+[0,1]])
a,b,c,d,q=prev.a,prev.b,prev.c,prev.d,prev.q;T=prev.T
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def lifted(i,j):
 poly=s.Poly(minor(start+T*K,i,j),a,b,c,d)
 assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
 return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))],(a,b,c,d))
assert M.rank()==3
left=[s.factor((v.T*rhs)[0]) for v in M.T.nullspace()]
assert len(left)==1 and s.factor(left[0]/q)!=0
linear=tuple(next(iter(s.linsolve((M,rhs.subs(q,0)),(a,b,c,d)))))
frees=set().union(*(v.free_symbols for v in linear)) & {a,b,c,d}
assert len(frees)==1
free=next(iter(frees))
P=s.Poly(s.factor(linear[0]*linear[3]-linear[1]*linear[2]),free)
assert P.degree()==2
discriminant=s.factor(s.discriminant(P.as_expr(),free))
assert s.sign(discriminant.subs(e,s.Rational(1,20)))==-1
assert s.sign(discriminant.subs(e,s.Rational(1,40)))==1
numerator=s.factor(s.together(discriminant)).as_numer_denom()[0]
assert s.Poly(numerator,e).degree()==4
assert numerator.subs(e,s.Rational(1,40))>0 and numerator.subs(e,s.Rational(1,35))<0
terms=s.Poly(numerator,e)
# Positive derivative terms are bounded at 1/35 and the negative
# linear term can only decrease the derivative further for e>0.
assert s.factor(4*terms.nth(4)*s.Rational(1,35)**3+
                3*terms.nth(3)*s.Rational(1,35)**2+terms.nth(1))<0
assert s.factor(JV).subs(e,s.Rational(1,40))<0 and s.factor(JV).subs(e,s.Rational(1,35))<0
report={'schema':'marici.nima.nine-point-E-complex-real-caustic-within-positive-V-family.v1',
 'passed':True,'V_family':'w2=e>0, (w4,w5,w6,w7,w8,t,u)=(1,1,1,1,1,3,2), rank-six physical moment-curve Z9',
 'V_target_Jacobian':str(JV),
 'E_lifted_linear_left_null':list(map(str,left)),
 'E_forced_q_zero_quadratic':str(P.as_expr()),
 'E_quadratic_discriminant':str(discriminant),
 'unique_simple_positive_caustic_parameter_interval':['1/40','1/35'],
 'V_Jacobian_nonzero_for_all_positive_e':True,
 'E_discriminant_at_1_over_40':str(discriminant.subs(e,s.Rational(1,40))),
 'E_discriminant_at_1_over_20':str(discriminant.subs(e,s.Rational(1,20))),
 'scope':'The unique simple E complex/real algebraic fibre transition in (1/40,1/35) occurs inside a positive target-regular V family. It does not establish a pole of the complete E field trace or any physical nine-point boundary.'}
(OUT/'nine-point-E-complex-real-caustic-within-positive-V-family.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'V_target_Jacobian':str(JV),
 'E_discriminant':str(discriminant)},indent=2))
