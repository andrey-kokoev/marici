"""Does the E meromorphic supertrace survive when the entire E fibre is non-real?"""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_relabelled_cells_miss_vertical_image as prev
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=prev.D,prev.vars
w2,w4,w5,w6,w7,w8,t,u=vars
ZE=prev.ZE;Z9=prev.Z9
e=s.Rational(1,20);p=dict(zip(vars,(e,1,1,1,1,1,3,2)))
V=D.subs(p).copy();V[0,1]=0;V[1,1]=e
Y=V*Z9[[0,1,3,4,5,6,7,8],:]
H=Y[:,:2];assert H.det()!=0
B=H.inv()*Y[:,2:]
z=ZE[:,2:]-ZE[:,:2]*B;h=ZE[:,:2]
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
assert [s.factor((v.T*rhs)[0]) for v in M.T.nullspace()]==[-q]
linear=tuple(next(iter(s.linsolve((M,rhs.subs(q,0)),(a,b,c,d)))))
frees=set().union(*(v.free_symbols for v in linear)) & {a,b,c,d}
assert len(frees)==1
free=next(iter(frees))
P=s.Poly(s.factor(linear[0]*linear[3]-linear[1]*linear[2]),free)
assert P.degree()==2 and s.discriminant(P.as_expr(),free)<0
roots=s.solve(P.as_expr(),free);assert len(roots)==2
sheets=[];values=[]
for root in roots:
 source=start+T.subs(dict(zip((a,b,c,d),(v.subs(free,root) for v in linear))))*K
 inverse=source[:,[0,2]].inv();gauge=inverse*source
 point=dict(zip(vars,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
         -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
 assert all(abs(complex(s.N((gauge-D.subs(point))[i,j],18)))<1e-12 for i in range(2) for j in range(8))
 assert s.simplify(D.subs(point)*z)==s.zeros(2,4)
 Jz=s.Matrix.hstack(*[s.Matrix(list(D.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
 assert Jz!=0
 rho=s.S.One/(s.prod(point[v] for v in vars[:6])*point[u]*(point[t]-point[u]))
 component=s.cancel(rho*(point[w2]*point[w4])**4*(D.subs(point)*h).det()**4/Jz)
 values.append(component)
 sheets.append({'complex_root':str(s.N(root,12)),
                'chi3_power4_chi5_power4_continued_value':str(s.N(component,12))})
trace=s.simplify(values[0]+values[1])
assert s.simplify(s.im(trace))==0
report={'schema':'marici.nima.nine-point-complex-E-trace-over-positive-V-target.v1',
 'passed':True,'no_real_E_fibre':True,'two_complex_sheets':sheets,
 'exact_real_two_sheet_chi3_power4_chi5_power4_trace':str(trace),
 'nonzero':bool(trace!=0),
 'scope':'Algebraic meromorphic two-sheet E supertrace at one positive V target outside both A and E positive source supports; does not reconstruct the global n9 image form.'}
(OUT/'nine-point-complex-E-trace-over-positive-V-target.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'E_no_real_source_sheet':True,
 'E_chi3_two_complex_sheet_trace_nonzero':bool(trace!=0),'trace':str(trace)},indent=2))
