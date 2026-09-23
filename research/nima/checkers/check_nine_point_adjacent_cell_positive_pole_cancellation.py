"""Local oriented-residue cancellation between adjacent positive G(2,9) eight-cells."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_four_mass_positive_source_boundary_pole_slice as original
 import check_nine_point_loop_canonical_residue as top
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,variables,Z=original.D,original.vars,original.Z
old=original.old
w2,w4,w5,w6,w7,w8,t,u=variables
Bcell=D.copy();Bcell[0,3]=-w4/t
Acell=D
assert Bcell.subs(w4,0)==Acell.subs(w4,0)
v=s.symbols('v',positive=True)
nonzero=zero=0
B9=s.Matrix.hstack(Bcell[:,:2],s.zeros(2,1),Bcell[:,2:])
for i,j in itertools.combinations(range(9),2):
 minor=s.factor(s.det(s.Matrix.hstack(B9[:,i],B9[:,j])))
 numerator,denominator=s.fraction(s.cancel(minor.subs(t,u+v)))
 assert all(x>=0 for x in s.Poly(numerator,w2,w4,w5,w6,w7,w8,u,v).coeffs()),(i,j,minor)
 assert all(x>=0 for x in s.Poly(denominator,w2,w4,w5,w6,w7,w8,u,v).coeffs())
 if minor==0:zero+=1
 else:nonzero+=1
assert (nonzero,zero)==(23,13)
assert s.factor(s.det(s.Matrix.hstack(Bcell[:,3],Bcell[:,4])))==0 # (phys 5,6)
# Replace the original normal pole (45)=h with (56)=g=w5(w4-h*t)
# in the same sourced top cyclic measure. dh/dg=-1/(w5*t).
measure_jac_B=-top.J/(w5*t)
leading=w2*w5*w6*w7*w8
remaining=(w4/t)*(w6*w7*(t-u))*(-w8*u)
residue_B=s.factor(measure_jac_B/(leading*remaining))
assert s.factor(residue_B+top.source_density)==0
assert s.factor(residue_B-1/(w2*w4*w5*w6*w7*w8*u*(t-u)))==0
point=original.point;A=Acell.subs(point);B=Bcell.subs(point)
assert A==B
Y=A*Z;H=Y[:,4:6];Btarget=H.inv()*Y[:,:4]
deltaY=s.zeros(2,6);deltaY[0,4]=1
Yreference=old.Cbar.subs(old.epsilon,original.pole)*Z
source_frame=H*Yreference[:,4:6].inv()
assert Y==source_frame*Yreference
deltaY=source_frame*deltaY
target_direction=H.inv()*(deltaY[:,:4]-deltaY[:,4:6]*Btarget)
target_vector=s.Matrix(list(target_direction))

def chart_derivative(cell):
 cols=[]
 for variable in variables:
  delta=cell.diff(variable).subs(point)*Z
  target=H.inv()*(delta[:,:4]-delta[:,4:6]*Btarget)
  cols.append(s.Matrix(list(target)))
 return s.Matrix.hstack(*cols)
JA=chart_derivative(Acell);JB=chart_derivative(Bcell)
detA=JA.det(method='domain-ge');detB=JB.det(method='domain-ge')
assert detA==original.J and detA!=0 and detB!=0
velocity_A=JA.inv()*target_vector
velocity_B=JB.inv()*target_vector
dw4_A=s.factor(velocity_A[1]);dw4_B=s.factor(velocity_B[1])
assert dw4_A==original.w4dot and dw4_B!=0
source_other=s.prod(point[x] for x in (variables[0],*variables[2:6]))*point[variables[7]]*(point[variables[6]]-point[variables[7]])
RA=s.factor(-s.S.One/(source_other*detA*dw4_A))
RB=s.factor(s.S.One/(source_other*detB*dw4_B))
assert RA==original.scalar and RB==-RA
px=s.det(s.Matrix.hstack(A[:,0],A[:,4]));assert px!=0
assert s.factor((RA+RB)*px**4)==0
report={'schema':'marici.nima.nine-point-adjacent-cell-positive-pole-cancellation.v1','passed':True,
 'positive_adjacent_cell':'Retain the source coordinates but set physical column5=(-w4/t,w4), so (56)=0 replaces (45)=0 and columns (5,6,7) become a triple parallel block. The loop column3, (12),(67),(89) stay zero.',
 'adjacent_cell_ordered_source_minor_counts':{'strictly_positive':23,'identically_zero':13},
 'common_positive_seven_dimensional_boundary':'w4=0',
 'sixfold_top_measure_residue_orientation_relation':'rho_B=-rho_A in the same eight source coordinate order',
 'target_jacobians_both_nonzero':True,
 'target_slice_w4_speeds_both_nonzero':True,
 'original_local_scalar_pole_residue':str(RA),
 'adjacent_local_scalar_pole_residue':str(RB),
 'local_scalar_pole_residues_cancel_exactly':True,
 'local_four_flavor_XXXX_pole_residues_cancel_exactly':True,
 'full_four_flavor_fermionic_numerator_identical_on_common_boundary':True,
 'every_fermionic_component_shared_boundary_residue_cancels':True,
 'boundary':'This is an EXACT local cancellation of the two shared-boundary source-sheet residues of two oriented positive eight-cells in the same rank-six target chart. It does NOT sum all fibre poles of the adjacent cell, construct a full n9 positive-image canonical form, or prove global triangulation/image coverage.'}
(OUT/'nine-point-adjacent-cell-positive-pole-cancellation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'adjacent_cell_positive':True,'local_oriented_residues_cancel':True,
 'full_image_form_proven':False},indent=2))
