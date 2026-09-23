"""Compute normalized leading regular A+C pushed form in their overlapping corner normal cone."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_positive_square_corner_normal_fan as fan
 import check_nine_point_loop_canonical_residue as top
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
X,Y=s.symbols('X Y',positive=True)
alpha,beta=s.symbols('alpha beta',positive=True)
# In A target-normal coordinates: A:(X,Y)=(w4,v); C:(X,Y)=
# (w4_C+alpha*v_C,beta*v_C). Source residue signs A=-, C=+.
w4_C=X-alpha*Y/beta;v_C=Y/beta
jac=s.factor(s.det(s.Matrix([[s.diff(w4_C,X),s.diff(w4_C,Y)],
                               [s.diff(v_C,X),s.diff(v_C,Y)]])))
assert jac==1/beta
A_density=-s.S.One/(X*Y)
C_density=s.factor(jac/(w4_C*v_C))
assert s.factor(C_density-1/(Y*(X-alpha*Y/beta)))==0
combined=s.factor(A_density+C_density)
assert s.factor(combined-(alpha/beta)/(X*(X-alpha*Y/beta)))==0
assert s.factor(s.denom(combined).subs(Y,0))!=0
checks=[]
for item in fan.checks:
 a,b=[s.Rational(z) for z in item['C_slope_ray_positive_coordinates_inside_A_normal_cone']]
 assert a>0 and b>0
 assert s.factor(s.Rational(item['regular_C_target_normal_determinant'])/
                 s.Rational(item['regular_A_target_normal_determinant'])-b)==0
 c=s.factor(a/b);assert c>0
 total=s.factor(combined.subs({alpha:a,beta:b}))
 assert s.factor(total-c/(X*(X-c*Y)))==0
 # The common Y=0 edge lies in the closure of the overlap X>cY>0.
 assert s.factor(s.limit(Y*total,Y,0,dir='+'))==0
 assert s.factor(s.limit(Y*A_density,Y,0,dir='+'))==-1/X
 assert s.factor(s.limit(Y*C_density.subs({alpha:a,beta:b}),Y,0,dir='+'))==1/X
 checks.append({'point':item['point'],'C_slope_ray_A_coordinates':[str(a),str(b)],
  'positive_slope_ratio_c':str(c),
  'regular_A_leading_normal_density':str(A_density),
  'regular_C_leading_normal_density':str(C_density.subs({alpha:a,beta:b})),
  'overlap_sum_leading_normal_density':str(total),
  'shared_Y_zero_pole_cancels_on_overlap':True})
report={'schema':'marici.nima.nine-point-regular-ac-corner-leading-image-form.v1','passed':True,
 'universal_normal_model':'On regular A/C overlap in A normal target coordinates X,Y, the A leading density is -1/(XY), C is +1/[Y(X-cY)] with c=alpha/beta>0. Their sum is c/[X(X-cY)], with NO Y=0 simple pole.',
 'exact_positive_corner_controls':checks,
 'scope':'A normalized LEADING HOMOGENEOUS two-dimensional target-normal model, multiplied by the common regular six-dimensional corner base density and full fermionic numerator. It only describes the locally shared A/C sector, not full nonlinear target eight-form, B/D singular sectors, other cells or global image form.'}
(OUT/'nine-point-regular-ac-corner-leading-image-form.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_corner_controls':len(checks),
 'local_shared_target_pole_Y0_cancelled':True,'ratios':[x['positive_slope_ratio_c'] for x in checks]},indent=2))
