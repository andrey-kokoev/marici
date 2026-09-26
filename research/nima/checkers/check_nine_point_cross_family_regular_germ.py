"""Pole plus finite-part records for the four-cell comparison along one target curve.
Coefficients multiply the common eight-form chart volume; no pullback of an
8-form to a curve is being taken. First jets are evaluated exactly at the wall.
"""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
    import check_nine_point_four_cell_two_zero_column_facet_full_pole as base
wall=base.wall;first=wall.first;V=base.vars;e=wall.e;r=wall.root
w2,w4,w5,w6,w7,w8,t,u=V
pE=dict(zip(V,(e,1,1,1,1,1,3,2)))
Y=base.cube.E['E'].subs(pE)*base.Z9
B=Y[:,:2].inv()*Y[:,2:]
z=base.Z9[:,2:]-base.Z9[:,:2]*B
z0=z.subs(e,r).applyfunc(s.cancel)
z1=z.diff(e).subs(e,r).applyfunc(s.cancel)
chamber=first.support.five.prior.chamber
EB={v:s.factor(chamber.parse(chamber.EB['inverse_source_parameters'][str(v)]).subs(chamber.e,e)) for v in V}
# Reconstruct symbolic FB with rational simplification at matrix checks.
five=first.support.five
Z=five.Z;K=five.K;T=five.T
a0,b0,c0,d0,q0=five.a,five.b,five.c,five.d,five.q
start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
def lifted(i,j):
    poly=s.Poly(five.minor(start+T*K,i,j),a0,b0,c0,d0)
    return poly.coeff_monomial(1)+sum(poly.coeff_monomial(v)*v for v in (a0,b0,c0,d0))+poly.coeff_monomial(a0*d0)*q0
M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in five.bir.pairs],(a0,b0,c0,d0))
left=s.factor((M.T.nullspace()[0].T*rhs)[0])
qr=s.factor(-left.subs(q0,0)/s.diff(left,q0))
sol=M.gauss_jordan_solve(rhs.subs(q0,qr))[0]
assert s.factor(qr-sol[0]*sol[3]+sol[1]*sol[2])==0
source=start+T.subs(dict(zip((a0,b0,c0,d0),sol)))*K
gauge=(source[:,[0,2]].inv()*source).applyfunc(s.cancel)
FB=dict(zip(V,(gauge[1,1],gauge[1,3],-gauge[0,4],-gauge[0,5],-gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
assert all(s.cancel(v)==0 for v in gauge-five.cell.subs(FB))
points={'zero2_E_B':EB,'zero2_F_B':FB,
        'zero3_E_B':wall.points['E_B'],'zero3_F_B':wall.points['F_B']}
rows=[]
for key,C in base.C.items():
    p=points[key]
    p0={v:s.cancel(p[v].subs(e,r)) for v in V}
    p1={v:s.cancel(s.diff(p[v],e).subs(e,r)) for v in V}
    assert p0==base.point
    def at(expr):return s.cancel(expr.subs(p0))
    def derivative(expr):return s.cancel(sum(expr.diff(v).subs(p0)*p1[v] for v in V))
    def matrix_derivative(M):return M.applyfunc(derivative)
    C0=C.subs(p0);C1=matrix_derivative(C)
    H0=C0*base.Z9[:,:2];H1=C1*base.Z9[:,:2]
    J0=s.Matrix.hstack(*[s.Matrix(list(C.diff(v).subs(p0)*z0)) for v in V])
    J1=s.Matrix.hstack(*[s.Matrix(list(matrix_derivative(C.diff(v))*z0+C.diff(v).subs(p0)*z1)) for v in V])
    determinant=J0.det(method='domain-ge');assert determinant!=0
    minor=C[:,[0,4]].det();m0=at(minor);m1=derivative(minor);assert m0!=0
    denominator=w4*w5*w6*w7*w8*u*(t-u)
    d0=at(denominator);d1=derivative(denominator);assert d0!=0
    sign=base.cube.orient[key.split('_',1)[1]]
    # F(e)=v(e)/w2(e); v is regular and nonzero at the control.
    v0=s.factor(sign*m0**4*H0.det()**4/(d0*determinant))
    logarithmic=s.factor(4*m1/m0+4*s.trace(H0.inv()*H1)-d1/d0-s.trace(J0.inv()*J1))
    v1=s.factor(v0*logarithmic)
    a=s.cancel(s.diff(p[w2],e).subs(e,r));b=s.cancel(s.diff(p[w2],e,2).subs(e,r))
    assert a!=0
    pole=s.factor(v0/a)
    finite=s.factor(v1/a-v0*b/(2*a*a))
    rows.append({'cell':key,'chi1_power4_chi5_power4_pole':str(pole),
                 'chi1_power4_chi5_power4_finite_part':str(finite)})
P={x['cell']:s.Rational(x['chi1_power4_chi5_power4_pole']) for x in rows}
F={x['cell']:s.Rational(x['chi1_power4_chi5_power4_finite_part']) for x in rows}
for family in ('zero2','zero3'):
    assert P[family+'_E_B']+P[family+'_F_B']==0
# Comparison defects are differences of retained germ coefficients.
# Equal cross-family pole coefficients along the common curve need not hold
# just from equal intrinsic residues: target defining functions are relevant.
differences={role:{'pole':str(s.factor(P['zero3_'+role]-P['zero2_'+role])),
                   'finite':str(s.factor(F['zero3_'+role]-F['zero2_'+role]))}
             for role in ('E_B','F_B')}
pair_finite={family:s.factor(F[family+'_E_B']+F[family+'_F_B']) for family in ('zero2','zero3')}
assert all(s.Rational(v['pole'])==0 and s.Rational(v['finite'])!=0 for v in differences.values())
assert pair_finite['zero3']!=pair_finite['zero2']
assert sum(s.Rational(v['pole']) for v in differences.values())==0
assert s.factor(sum(s.Rational(v['finite']) for v in differences.values()))==s.factor(pair_finite['zero3']-pair_finite['zero2'])
report={'passed':True,'curve':'E source (e,1,1,1,1,1,3,2)', 'wall':str(r),
 'expansion':'coefficient = pole/(e-wall) + finite + O(e-wall)',
 'component':'chi1^4 chi5^4 in common target-chart eight-form coefficient',
 'four_germ_records':rows,'cross_family_differences':differences,
 'within_family_pair_finite_parts':{k:str(v) for k,v in pair_finite.items()},
 'pair_difference_finite_part':str(s.factor(pair_finite['zero3']-pair_finite['zero2'])),
 'comparison_addition_commutes':True,
 'scope':'Exact Laurent coefficients along one target curve, retaining regular differences. Scalar component jet, not a full multivariable form germ or higher HoTT filler.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/nine-point-cross-family-regular-germ.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'differences':differences,'pair_finite_difference_nonzero':pair_finite['zero3']!=pair_finite['zero2']},indent=2))
