"""Exact Gr(2,6) eight-form chart transition to the sourced Y0 frame."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
source=(ROOT/'research/sources/nima/papers/six-point-nmhv/1312.2007/amplituhedron.tex').read_text(encoding='utf8')
anchor=source.index(r'\section{The Superamplitude}');text=source[anchor:anchor+6000]
assert r'Y \to Y_0' in text and r'0_{4 \times k}' in text and r'1_{k \times k}' in text
assert r'\Omega =  \langle Y_1 \dots Y_k d^4 Y_1 \rangle' in text
assert r'\omega_{n,k}(Y_0;Z_a)' in text
# The numeric packet used gauge Y=[I_2|B_L|B_R], with row-major
# B=(B_L|B_R). Source extraction fixes Y0=[0_(2x4)|I_2]. In the
# Y0 chart set Y=[U_L|U_M|I_2], U=(U_L|U_M), also row-major.
a,b,c,d,e,f,g,h=s.symbols('a b c d e f g h')
UL=s.Matrix([[a,b],[c,d]]);UM=s.Matrix([[e,f],[g,h]])
R=UL.inv();BL=R*UM;BR=R
variables=(a,b,c,d,e,f,g,h)
coordinates=[BL[i,j] for i in range(2) for j in range(2)]+[BR[i,j] for i in range(2) for j in range(2)]
# Block-triangular Jacobian: dB_L/dU_M is left multiplication by R,
# determinant det(R)^2. dB_R/dU_L maps X to -R*X*R and has
# determinant det(R)^4. Swapping two four-coordinate blocks is even.
J=s.factor(s.det(R)**6)
assert s.cancel(J-s.det(UL)**(-6))==0
# The inverse gauge transition U_L=B_R^-1,U_M=B_R^-1*B_L.
B0=s.Matrix([[2,1],[1,3]]);B1=s.Matrix([[1,2],[3,4]])
point={a:2,b:1,c:1,d:3,e:1,f:2,g:3,h:4}
assert s.simplify(J.subs(point)-s.Rational(1,5**6))==0
actual_numeric=s.Matrix(coordinates).jacobian(variables).subs(point).det(method='domain-ge')
assert actual_numeric==J.subs(point)
assert s.simplify((R*UL).subs(point)-s.eye(2))==s.zeros(2,2)
assert s.simplify((BR.inv()*BL-UM).subs(point))==s.zeros(2,2)
# Y0 has U=0 and det U_L=0; old B requires U_L^-1 and is undefined.
Y0=s.Matrix([[0,0,0,0,1,0],[0,0,0,0,0,1]])
assert Y0[:,0:2].det()==0 and Y0[:,4:6].det()==1
# If omega_U is finite and nonzero at U=0, omega_B(B(U)) must
# cancel det(U_L)^(-6). Along U_L=eps*I, U_M=0 the factor is eps^-12.
eps=s.symbols('eps',nonzero=True)
assert s.simplify(J.subs({a:eps,b:0,c:0,d:eps,e:0,f:0,g:0,h:0})-eps**(-12))==0
assert s.Rational(1,5**5)!=J.subs(point)
report={'schema':'marici.nima.nine-point-Y0-chart-transition.v1','passed':True,
 'source':'research/sources/nima/papers/six-point-nmhv/1312.2007/amplituhedron.tex, section The Superamplitude',
 'old_target_chart':'Y=[I2|B_L|B_R], B row-major',
 'sourced_Y0_chart':'Y=[U_L|U_M|I2], U row-major, Y0=U=0',
 'target_eight_form_jacobian':'d^8B=(det U_L)^(-6) d^8U, orientations as declared',
 'finite_source_extraction_condition':'omega_U=omega_B(B(U))/(det U_L)^6 must extend regularly to U=0 before Berezin extraction',
 'one_parameter_test':'U_L=eps I2, U_M=0 requires omega_B(B(U)) vanish at least to order eps^12 for finite omega_U',
 'mutation_exponent_five_refused':True,
 'claim_boundary':'Exact ambient Gr(2,6) chart transition, not a regularity or full-form comparison for the four-pair cell. The prior positive-target B coefficient cannot be evaluated at source Y0 because B is undefined there.'}
(OUT/'nine-point-Y0-chart-transition.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'transition_exponent':-6,'Y0_in_old_chart':False,
 'epsilon_J_pole_order':12},indent=2))
