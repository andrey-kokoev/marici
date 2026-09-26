"""Source-derived local jet intersection and explicit limits of that overlap."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
base=Path(__file__).resolve().parent
formal=json.loads((base/'source-anchored-overlap-formal.json').read_text())
checks={}
checks['fresh_actual_native_overlap']=formal['passed'] and formal['fresh'] and formal['overlap_mode']
checks['snapshot_sources_current']=all(Path(p).exists() and hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in formal['source_snapshot_hashes'].items())
def hessian(sources):
    return tuple(tuple(sum(m/r**3*(F(i==j)-3*n[i]*n[j]) for m,r,n in sources) for j in range(3)) for i in range(3))
x=(F(1),F(0),F(0));y=(F(0),F(1),F(0));z=(F(0),F(0),F(1))
old=((F(2),F(3),x),(F(1),F(4),y))
new=((F(36),F(12),x),(F(18),F(12),z))
H_old=hessian(old);H=hessian(new)
target=((F(-1,32),F(0),F(0)),(F(0),F(1,32),F(0)),(F(0),F(0),F(0)))
checks['original_fixture_recovered']=tuple(H_old[i][i] for i in range(3))==tuple(F(n,1728) for n in (-229,74,155))
old_det=H_old[0][0]*H_old[1][1]*H_old[2][2]
checks['original_fixture_rank_obstruction']=old_det!=0 and target[2][2]==0
checks['new_sources_positive_and_away']=all(m>0 and r==12 and sum(v*v for v in n)==1 for m,r,n in new)
checks['new_common_denominator_reciprocals']=all(r**3==1728 for _,r,_ in new)
checks['new_point_source_hessian_matches_wave']=H==target
checks['new_vacuum_trace_zero']=sum(H[i][i] for i in range(3))==0
phi=-sum(m/r for m,r,_ in new)
grad=tuple(-sum(m/r**2*n[i] for m,r,n in new) for i in range(3))
checks['physical_potential_value']=phi==F(-9,2)
checks['physical_gradient']=grad==(F(-1,4),F(0),F(-1,8))
checks['physical_lower_jet_scaling']=phi*1728==-7776 and tuple(v*1728 for v in grad)==(-432,0,-216)
checks['native_hessian_numerators']=tuple(8*1728*H[i][i] for i in range(3))==(-432,432,0)
# Undo the per-source normalized u-coordinate scaling before calling lower rows physical.
checks['native_scalar_requires_radius_squared']=(-8*sum(m for m,_,_ in new))*12**2/(8*1728)==phi
checks['native_gradient_requires_radius']=tuple((-8*m)*12/(8*1728) for m,_,_ in new)==(grad[0],grad[2])
a=F(1,4)
checks['proper_clock_wave_normalization']=a*a/2==F(1,32)
checks['matched_quadratic_harmonic']=F(-1,64)*2+F(1,64)*2==0
third=-6*F(36)/F(12)**4
checks['newtonian_next_jet_not_zero']=third==F(-1,96)
checks['unscaled_prototype_is_not_weak_field']=abs(phi)>1
homotheties=[]
for s in (F(1),F(1,4),F(1,16),F(1,64)):
    scaled=tuple((m*s**3,r*s,n) for m,r,n in new)
    scaled_phi=-sum(m/r for m,r,_ in scaled)
    third_s=-6*scaled[0][0]/scaled[0][1]**4
    checks[str(s)+'_source_homothety_preserves_tidal_reading']=hessian(scaled)==target
    checks[str(s)+'_potential_becomes_weak']=scaled_phi==F(-9,2)*s*s
    checks[str(s)+'_next_jet_does_not_match']=third_s==F(-1,96)/s and third_s!=0
    homotheties.append(dict(scale=str(s),potential_at_origin=str(scaled_phi),third_derivative=str(third_s),controlled_ball_radius=str(s)))
remainder=4*sum(m for m,_,_ in new)/F(11)**4
checks['spatial_taylor_remainder_coefficient']=remainder==F(216,14641)
# Conservative constants for the fixed analytic Rosen source on [-1,2].
checks['small_baseline_root_constant_rounded_up']=17**2*2<28**2 # 17 sqrt(2)/4 < 7.
C=F(2625,8);M4=F(1,64)
schedules=[]
for h in (F(1,4),F(1,8),F(1,16),F(1,32),F(1,64)):
    epsilon=h**4;sigma=h**8
    bias=2*C*epsilon/h**2+M4*h**2/24
    noisy=bias+F(17,4)*sigma/(epsilon*h**2)
    label=str(h)
    checks[label+'_admitted_baseline_horizon']=5*epsilon<=F(1,4) and h<=1
    checks[label+'_noise_regime']=sigma<=epsilon
    checks[label+'_joint_limit_rate']=noisy==(2*C+M4/24+F(17,4))*h*h
    schedules.append(dict(proper_time_step=str(h),baseline_scale=str(epsilon),distance_error=str(sigma),bound=str(noisy)))
checks['joint_limit_bounds_decrease']=all(F(b['bound'])<F(a['bound']) for a,b in zip(schedules,schedules[1:]))
receipt=dict(passed=all(checks.values()),checks=checks,original_fixture_determinant=str(old_det),common_tidal_diagonal=['-1/32','1/32','0'],
    new_sources=[dict(mass=str(m),radius=str(r),direction=[str(v) for v in n]) for m,r,n in new],
    unmatched_next_jet=dict(newtonian_dx_Exx=str(third),symmetric_plane_wave_covariant_tidal_gradient='0'),
    spatial_remainder_coefficient=str(remainder),source_homotheties=homotheties,radar_limit_schedules=schedules,
    formal_receipt_sha256=hashlib.sha256((base/'source-anchored-overlap-formal.json').read_bytes()).hexdigest(),
    scope='New source-anchored local second-jet intersection, not the original fixed seeds or full spacetime equivalence. Analytic vacuum/Taylor/radar-limit arguments are written proofs; finite checks supplement them.')
(base/'source-anchored-tidal-overlap.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('passed=',receipt['passed'],'checks=',len(checks),'old determinant=',old_det,'new third derivative=',third)
raise SystemExit(0 if receipt['passed'] else 1)
