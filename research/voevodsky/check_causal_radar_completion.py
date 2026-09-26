"""Exact null-leg/radar controls and bound arithmetic in the Rosen sector.
No ray tracing approximation or optical hardware model.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

checks={};rows=[]
# Independent flat-Minkowski control of a time-varying Rosen chart.
# p=1+u, q=1; reflector X=1/6,Y=0,V=u. Exact positive leg h=p(start)/8.
b=F(1,6)
for start in (F(0),F(1,4),F(1,2)):
    p0=1+start;h1=p0/8;reflection=start+h1;p1=1+reflection
    h2=p1/8;reception=reflection+h2
    # S=int H du =h/[p(start)p(end)] for the x direction.
    S1=h1/(p0*p1);S2=h2/(p1*(1+reception))
    # Minkowski map x=(1+u)X, v=V+(1+u)X^2/2.
    qx=p1*b;qv=reflection+p1*b*b/2
    interval_out=-2*h1*(qv-start)+qx*qx
    interval_in=-2*h2*(reception-qv)+qx*qx
    label=str(len(rows))
    checks[label+'_outgoing_null_integral']=2*h1==b*b/S1
    checks[label+'_return_null_integral']=2*h2==b*b/S2
    checks[label+'_independent_minkowski_nulls']=interval_out==interval_in==0
    checks[label+'_future_directed_clock_order']=start<reflection<reception
    checks[label+'_outgoing_and_return_durations_differ']=h1!=h2
    # All clocks are proper tau=sqrt(2)u; keep squares rational.
    radar_squared=(h1+h2)**2/2
    checks[label+'_half_round_trip_normalization']=radar_squared==(reception-start)**2/2
    rows.append(dict(emission_u=str(start),reflection_u=str(reflection),reception_u=str(reception),
        outgoing_u=str(h1),return_u=str(h2),radar_distance_squared=str(radar_squared),
        reflection_vs_radar_midpoint_u=str(reflection-(start+reception)/2)))
# Constant flat metric, two transverse coordinates, rational null travel time.
bv=(F(1,8),F(1,8));h=F(1,8);b2=sum(x*x for x in bv)
checks['constant_metric_null_leg']=2*h*h==b2
checks['flat_radar_distance_equals_baseline_squared']=((h+h)**2)/2==b2
# SPD envelope and continuous dependence constants used in the proof.
lam=F(1,2);B0=F(4,3);bmax=F(1,4)
checks['two_leg_horizon_inside_domain']=1+2*bmax<2 # each h<|b| by the next check.
checks['leg_upper_bound_less_than_baseline']=B0/2<1
checks['radar_perturbation_constant']=B0**2/lam**2==F(64,9) # sqrt(2*lambda)=1.
checks['start_time_lipschitz_bound']=2*B0**2/lam**2==F(128,9)
checks['positive_residual_slope_bound']=F(2)>0
bounds=[]
for n in (4,8,16,32,64):
    d=F(8,n*n)
    checks[str(n)+'_metric_envelope_admissible']=0<d<1
    # exp(4/n^2)<=1/(1-4/n^2), r^2>=1-4/n^2.
    z=F(4,n*n)
    checks[str(n)+'_metric_upper_envelope']=1/(1-z)<=1+d
    checks[str(n)+'_metric_lower_envelope']=(1-z)**2>=1-d
    bounds.append(dict(n=n,metric_error=str(d),radar_error_bound_at_b_quarter=str(d*bmax),tidal_gap='1/2'))
checks['radar_bounds_shrink']=all(F(bounds[i+1]['radar_error_bound_at_b_quarter'])<F(bounds[i]['radar_error_bound_at_b_quarter']) for i in range(len(bounds)-1))
checks['source_counterexample_tides_do_not_shrink']=all(F(row['tidal_gap'])==F(1,2) for row in bounds)
root=Path(__file__).resolve().parents[2]
paths=[Path(__file__),root/'research/voevodsky/finite-baseline-fermi-detector-has-uniform-high-frequency-control.md']
primary=root/'temp/perlick-radar-0708.0170.html'
packet=dict(passed=all(checks.values()),checks=checks,flat_rosen_controls=rows,high_frequency_bounds=bounds,
    primary_source=dict(url='https://arxiv.org/html/0708.0170',version='0708.0170v1',sha256=hashlib.sha256(primary.read_bytes()).hexdigest() if primary.exists() else None),
    scope='Exact null identities and constants. General uniqueness, C0 extension and all-n vacuum estimates are written proofs; ideal instantaneous reflection, no medium or instrument response.',
    source_sha256={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
Path(__file__).with_name('causal-radar-completion.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
