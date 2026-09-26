"""Test all-positive-face-fibre F_B/F_D target-normal pairing on two exact target planes."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_oriented_eight_cell_cube as cube
 import check_nine_point_positive_slope_face_normal_cones as horizontal
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
vars=cube.vars;w2,w4,w5,w6,w7,w8,t,u=vars
FB,FD=(cube.F[x][:,[0,2,3,4,5,6,7,8]] for x in ('F_B','F_D'))
external=horizontal.external
# Insert physical row2 between old moment nodes 1 and 2 so the
# complete nine external rows are a strictly ordered moment curve.
Zfull=s.Matrix.vstack(horizontal.loop.Z8six[:1,:],
 s.Matrix([[s.Rational(3,2)**k for k in range(6)]]),horizontal.loop.Z8six[1:,:])
assert [Zfull[j,1] for j in range(9)]==[1,s.Rational(3,2),2,4,5,6,7,8,9]
assert Zfull[[0,2,3,4,5,6,7,8],:]==horizontal.loop.Z8six
assert cube.E['E_B'][:,[0,2,3,4,5,6,7,8]]==horizontal.B
assert cube.E['E_D'][:,[0,2,3,4,5,6,7,8]]==horizontal.D
assert all(z['nonparallel_for_every_pair_of_positive_face_preimages'] for z in horizontal.checks)
lamB,lamD=s.symbols('lambda_B lambda_D',real=True)
rows=[]
for name,raw in [('first',(1,1,1,1,1,1,2,2)),
                 ('second',(2,3,3,2,1,4,3,3))]:
 p=dict(zip(vars,map(s.Rational,raw)));Y=FB.subs(p)*external
 fixed=next(pair for pair in __import__('itertools').combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(k for k in range(6) if k not in fixed)
 def jac(C,point):
  Y0=C.subs(point)*external
  H=Y0[:,list(fixed)];B=H.inv()*Y0[:,list(free)]
  return s.Matrix.hstack(*[s.Matrix(list(H.inv()*(delta[:,list(free)]-
                  delta[:,list(fixed)]*B))) for delta in
                  (C.diff(variable).subs(point)*external for variable in vars)])
 J=jac(FB,p);assert J.rank()==7
 r=J.nullspace()[0]
 assert r[0]==r[6]==r[7]==0
 lows=[-p[v]/r[i] for i,v in enumerate(vars[:6]) if r[i]>0]
 highs=[-p[v]/r[i] for i,v in enumerate(vars[:6]) if r[i]<0]
 lower=max(lows);upper=min(highs) if highs else s.oo
 assert lower<0 and upper>0
 tangent=s.Matrix.hstack(*(J[:,j] for j in (0,2,3,4,5)),J[:,6]+J[:,7])
 assert tangent.rank()==6
 L=s.Matrix.vstack(*(n.T for n in tangent.T.nullspace()))
 pB={v:p[v]+lamB*r[i] for i,v in enumerate(vars)}
 pD={v:p[v]+lamD*r[i] for i,v in enumerate(vars)}
 nB=s.simplify(L*jac(FB,pB)[:,6]);nD=s.simplify(L*jac(FD,pD)[:,6])
 wedge=s.factor(s.det(s.Matrix.hstack(nB,nD)))
 numerator,denominator=s.fraction(wedge)
 x,y=s.symbols('x y',positive=True)
 shift=s.Poly(s.expand(numerator.subs({lamB:lower+x,lamD:lower+y})),x,y)
 coefficient_signs={str(s.sign(z)) for z in shift.coeffs()}
 # On the finite rectangle 0<x,y<upper-lower, the mixed xy term
 # cannot outweigh the negative linear x term, so wedge<0 strictly.
 A=shift.coeff_monomial(x*y)
 B=-shift.coeff_monomial(x)
 C=-shift.coeff_monomial(y)
 assert shift.coeff_monomial(1)==0 and A>0 and B>0 and C>0
 width=upper-lower
 assert width>0 and s.factor(B-A*width)>0
 assert denominator>0
 rows.append({'target':name,'positive_fibre_interval':[str(lower),str(upper)],
  'strict_negative_wedge_for_all_positive_fibre_preimages':True,
  'finite_rectangle_bound_B_minus_A_width':str(s.factor(B-A*width)),
  'normal_wedge_numerator':str(s.factor(numerator)),
  'normal_wedge_denominator':str(s.factor(denominator)),
  'shifted_wedge_coeff_signs':sorted(coefficient_signs),
  'shifted_wedge_polynomial':str(shift.as_expr())})
report={'schema':'marici.nima.nine-point-vertical-label3-exceptional-positive-normal-cones.v1',
 'passed':True,'positive_target_plane_controls':rows,
 'horizontal_E_B_E_D_transfer':'With strictly ordered full nine-point moment nodes (1,3/2,2,4,5,6,7,8,9), deleting zero physical row2 recovers the previously exact-certified B/D eight-point moment external configuration and complete E_B/E_D matrices. Earlier all-positive-face-fibre nonparallel normal-cone certificates therefore transfer identically to E_B/E_D at the same two positive target planes.',
 'vertical_F_B_F_D_all_positive_fibre_nonparallel':True,
 'scope':'Both exceptional face pairs have nonparallel transverse target normals for every pair of positive face preimages over TWO specified positive target planes each; no all-target nonlinear cone-gluing or global n9 canonical-form claim.'}
(OUT/'nine-point-vertical-label3-exceptional-positive-normal-cones.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'controls':[{'target':z['target'],'positive_interval':z['positive_fibre_interval'],'shifted_coefficient_signs':z['shifted_wedge_coeff_signs']} for z in rows]},indent=2))
