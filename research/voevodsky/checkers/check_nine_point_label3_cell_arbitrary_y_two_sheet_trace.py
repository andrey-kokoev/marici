"""Arbitrary-Y E trace is the relabelled eight-point trace; chi3 component survives both sheets."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_four_mass_global_target_trace_by_recentring as global_trace
 import check_nine_point_label3_cell_composite_local_cancellation as adjacent
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
D,vars=global_trace.D,global_trace.variables
E=adjacent.E
retained=(0,2,3,4,5,6,7,8) # physical labels 1,3,4,5,6,7,8,9
assert E[:,list(retained)]==D and E[:,1]==s.zeros(2,1)
Z9=s.Matrix(9,6,lambda i,j:s.Symbol(f'Z{i+1}_{j+1}'))
chi9=s.Matrix(9,4,lambda i,j:s.Symbol(f'chi{i+1}_{j+1}'))
Z8=Z9[list(retained),:];chi8=chi9[list(retained),:]
assert E*Z9==D*Z8 and E*chi9==D*chi8
for parameter in vars:assert E.diff(parameter)*Z9==D.diff(parameter)*Z8
B=global_trace.B
z9=Z9[:,2:]-Z9[:,:2]*B;h9=Z9[:,:2]
z8=Z8[:,2:]-Z8[:,:2]*B;h8=Z8[:,:2]
assert E*z9==D*z8 and E*h9==D*h8
assert s.Matrix(list(E*z9)).jacobian(vars)==s.Matrix(list(D*z8)).jacobian(vars)
assert s.factor(s.det(s.Matrix.hstack(E[:,2],E[:,4]))-vars[0]*vars[1])==0
moment=s.Matrix([[j**d for d in range(6)] for j in (1,3,4,5,6,7,8,9)])
weights=[('first',(1,1,1,1,1,1,3,2)),
         ('second',(2,3,1,4,2,5,s.Rational(7,2),s.Rational(3,2)))]
checks=[]
for name,raw in weights:
 p=dict(zip(vars,[s.Rational(x) for x in raw]))
 C=D.subs(p);Y=C*moment;H=Y[:,:2];assert H.det()!=0
 B0=H.inv()*Y[:,2:]
 z=moment[:,2:]-moment[:,:2]*B0;h=moment[:,:2]
 sheets=[]
 for root,point in global_trace.fibre(C,moment):
  Ci=D.subs(point);Ai=Ci*h
  cols=[]
  for parameter in vars:
   delta=D.diff(parameter).subs(point)*z
   cols.append(s.Matrix([delta[i,j] for i in range(2) for j in range(4)]))
  Jz=s.Matrix.hstack(*cols).det(method='domain-ge')
  assert Ai.det()!=0 and Jz!=0
  source_E=s.S.One/(s.prod(point[z0] for z0 in vars[:6])*point[vars[7]]*
                      (point[vars[6]]-point[vars[7]]))
  pair=s.factor(point[vars[0]]*point[vars[1]])
  coeff=s.factor(source_E*pair**4*Ai.det()**4/Jz)
  sheets.append({'kernel_area':str(root),'positive_sheet':root==0,
                 'chi3_power4_chi5_power4_component':str(coeff)})
 assert len(sheets)==2
 trace=s.factor(sum(s.Rational(x['chi3_power4_chi5_power4_component']) for x in sheets))
 checks.append({'target':name,'two_sheets':sheets,
                'complete_two_sheet_chi3_power4_chi5_power4_trace':str(trace),
                'trace_nonzero':bool(trace!=0)})
assert all(x['trace_nonzero'] for x in checks)
report={'schema':'marici.nima.nine-point-label3-cell-arbitrary-y-two-sheet-trace.v1','passed':True,
 'arbitrary_Y_identity':'For E with physical column2 zero, deleting physical row2 gives the exact four-pair D source chart on physical labels (1,3,4,5,6,7,8,9). For every first-pivot Y=[I2|B], its fibre ideal, eight-parameter Jacobian, and full fermionic numerator equal D evaluated on retained rows; the oriented E density is opposite the original A density. E is independent of external Z2 and chi2, but genuinely depends on Z3 and chi3.',
 'full_two_sheet_exact_positive_external_witnesses':checks,
 'generic_nonzero_chi3_component':'A nonzero rational trace at exact targets establishes a nonzero chi3^4 chi5^4 component on a nonempty algebraic open of E simple-fibre target/external parameters.',
 'scope':'E is ONE positive source-cell contour candidate. Other cell contributions might cancel its full two-sheet chi3 component; this does not establish the complete n9 image form or contour weights.'}
(OUT/'nine-point-label3-cell-arbitrary-y-two-sheet-trace.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'arbitrary_Y_relabelling':True,
 'nonzero_full_two_sheet_chi3_controls':sum(x['trace_nonzero'] for x in checks)},indent=2))
