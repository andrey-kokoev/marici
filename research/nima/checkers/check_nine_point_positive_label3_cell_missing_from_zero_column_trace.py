"""Exhibit a regular positive n9 eight-cell with genuine bosonic/fermionic label3 support."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
original=s.Matrix.hstack(D[:,:2],s.zeros(2,1),D[:,2:])
E=original.copy();E[:,1]=s.zeros(2,1);E[:,2]=s.Matrix([w2,0])
assert E.subs(w2,0)==original.subs(w2,0)
assert E[:,2]!=s.zeros(2,1) and E[:,1]==s.zeros(2,1)
assert E[:,[0,3]]==s.eye(2)
chi=s.Matrix(9,4,lambda i,j:s.Symbol(f'chi{i+1}_{j+1}'))
assert E*chi!=original*chi
assert (E*chi)[:,0].diff(chi[2,0])==s.Matrix([w2,0])
assert s.factor(s.det(s.Matrix.hstack(E[:,2],E[:,4]))-w2*w4)==0
v=s.symbols('gap',positive=True);positive=zero=0
for i,j in itertools.combinations(range(9),2):
 minor=s.factor(s.det(s.Matrix.hstack(E[:,i],E[:,j])))
 numerator,denominator=s.fraction(s.cancel(minor.subs(t,u+v)))
 assert all(c>=0 for c in s.Poly(numerator,w2,w4,w5,w6,w7,w8,u,v).coeffs()),(i,j,minor)
 assert all(c>=0 for c in s.Poly(denominator,w2,w4,w5,w6,w7,w8,u,v).coeffs())
 if minor==0:zero+=1
 else:positive+=1
assert (positive,zero)==(24,12)
Z=s.Matrix([[j**d for d in range(6)] for j in range(1,10)])
assert all(Z[list(rows),:].det()>0 for rows in itertools.combinations(range(9),6))
samples=[('first',('1','1','1','1','1','1','3','2')),
         ('second',('2','3','1','4','2','5','7/2','3/2')),
         ('third',('3','2','2','1','4','2','5','1'))]
checks=[]
for name,raw in samples:
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 assert all(p[z]>0 for z in vars[:6]) and p[t]>p[u]>0
 Y=E.subs(p)*Z
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(i for i in range(6) if i not in fixed)
 H=Y[:,list(fixed)];target=H.inv()*Y[:,list(free)]
 jac=s.Matrix.hstack(*(s.Matrix(list(H.inv()*(delta[:,list(free)]-
           delta[:,list(fixed)]*target))) for delta in
           (E.diff(parameter).subs(p)*Z for parameter in vars)))
 det=jac.det(method='domain-ge')
 assert det!=0
 dY=E.subs(p)*s.Matrix(9,6,lambda i,j:1 if (i,j)==(2,0) else 0)
 assert dY==s.Matrix([[p[w2]]+[0]*5,[0]*6])
 assert dY!=s.zeros(2,6)
 checks.append({'point':name,'source_to_target_chart_rank':8,
  'target_map_derivative_wrt_physical_Z3_nonzero':True,
  'nonzero_fermionic_pair_3_5_minor':str((w2*w4).subs(p)),
  'target_chart_jacobian_determinant':str(det)})
report={'schema':'marici.nima.nine-point-positive-label3-cell-missing-from-zero-column-trace.v1','passed':True,
 'cell':'Move the positive amplitude w2*e1 from physical column2 to physical column3, making physical column2 zero. Source variables remain (w2,w4,w5,w6,w7,w8,t,u).',
 'ordered_minors':{'strictly_positive':positive,'identically_zero':zero},
 'common_boundary_with_zero_column_cell':'w2=0, where BOTH physical columns2 and3 vanish',
 'fermionic_label3_support':'det(C[:,3],C[:,5])=w2*w4>0; hence the chi3^4 chi5^4 coefficient is nonzero in the full source Grassmann numerator.',
 'exact_positive_rank_six_external_controls':checks,
 'scope':'A distinct regular positive eight-cell and nonzero label3 dependence show that the previously computed ZERO-COLUMN sourced trace is not an inventory of n9 positive source cells. No cyclic top-residue orientation for this new cell, global image coverage, or full nine-point canonical-form contribution is established.'}
(OUT/'nine-point-positive-label3-cell-missing-from-zero-column-trace.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_ordered_minors':positive,'label3_supported':True,
 'exact_regular_target_controls':len(checks)},indent=2))
