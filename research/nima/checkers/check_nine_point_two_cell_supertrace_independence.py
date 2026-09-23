"""A and E arbitrary-Y full two-sheet supertraces are rationally linearly independent."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_cell_arbitrary_y_two_sheet_trace as Etrace
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
global_trace=Etrace.global_trace
D,vars=global_trace.D,global_trace.variables
w2,w4,w5,w6,w7,w8,t,u=vars
Z8=global_trace.old.Z
p=dict(zip(vars,[s.S.One]*6+[s.S(3),s.S(2)]))
C=D.subs(p);Y=C*Z8;H=Y[:,:2];assert H.det()!=0
B0=H.inv()*Y[:,2:]
z=Z8[:,2:]-Z8[:,:2]*B0;h=Z8[:,:2]
sheets=[]
for root,point in global_trace.fibre(C,Z8):
 Ci=D.subs(point);Ai=Ci*h
 cols=[]
 for param in vars:
  delta=D.diff(param).subs(point)*z
  cols.append(s.Matrix([delta[i,j] for i in range(2) for j in range(4)]))
 Jz=s.Matrix.hstack(*cols).det(method='domain-ge')
 assert Jz!=0 and Ai.det()!=0
 sourceA=-s.S.One/(s.prod(point[v] for v in vars[:6])*point[u]*(point[t]-point[u]))
 # Physical labels 1 and 5 are local D columns 0 and 3.
 pair=s.factor(s.det(s.Matrix.hstack(Ci[:,0],Ci[:,3])))
 assert pair==point[w4]
 coeff=s.factor(sourceA*pair**4*Ai.det()**4/Jz)
 sheets.append({'kernel_area':str(root),'chi1_power4_chi5_power4':str(coeff)})
assert len(sheets)==2
A_trace=s.factor(sum(s.Rational(q['chi1_power4_chi5_power4']) for q in sheets))
assert A_trace!=0
# E's COMPLETE two-sheet chi3^4 chi5^4 trace is independently checked
# nonzero at two positive external/target witnesses, hence nonzero as
# a rational function. A has no chi3 at ALL, for arbitrary target.
assert all(witness['trace_nonzero'] for witness in Etrace.checks)
assert Etrace.E[:,1]==s.zeros(2,1)
A9=s.Matrix.hstack(D[:,:2],s.zeros(2,1),D[:,2:])
assert A9[:,2]==s.zeros(2,1)
report={'schema':'marici.nima.nine-point-two-cell-supertrace-independence.v1','passed':True,
 'A_full_two_sheet_chi1_power4_chi5_power4_witness':str(A_trace),
 'A_two_sheet_fibre_sheets':sheets,
 'A_chi3_dependence':'identically zero for arbitrary Y,Z9 because physical column3 zero',
 'E_full_two_sheet_chi3_power4_chi5_power4_nonzero_controls':
   [z['complete_two_sheet_chi3_power4_chi5_power4_trace'] for z in Etrace.checks],
 'generic_field_linear_independence':'The complete arbitrary-Y rational supertraces A and E are linearly independent over rational bosonic coefficient functions: E has a generically nonzero chi3^4 chi5^4 coordinate while A has zero there; A has a nonzero complete chi1^4 chi5^4 coordinate at an exact positive rank-six target.',
 'necessary_contour_constraint':'A bosonic-scalar combination a*A+b*E can be chi3-independent on a rational open only if b=0, unless ADDITIONAL chi3-sensitive source-cell traces are included to cancel E.',
 'scope':'A two-cell rational-span obstruction, NOT a proof that the complete n9 amplitude is chi3-blind or that E has nonzero coefficient in its correct contour. Other cells can cancel chi3 and full n9 image canonical form remains open.'}
(OUT/'nine-point-two-cell-supertrace-independence.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'arbitrary_Y_rational_supertraces_independent':True,
 'chi3_blind_two_cell_combination_requires_E_coefficient_zero':True},indent=2))
