"""Exact finite-baseline connector controls and uniform-bound arithmetic.
All-frequency existence/convergence is a written contraction proof, not sampling.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

checks={};rows=[]
# Exact flat Rosen chart p=1+c*u, q=1: independently use its Minkowski transform.
for c,u,b in ((F(1),F(1,3),F(1,4)),(F(-1,2),F(1,4),F(1,8)),(F(2),F(0),F(1,10))):
    p0=1+c*u
    a=-c*p0*b*b/(4+c*c*b*b)
    p1=p0+c*a
    B=1/(p0*p1) # integral_0^1 H(u+a*t) dt, H=1/(1+c*u)^2.
    C=-c/(p0*p0*p1) # integral_0^1 (1-t) H'(u+a*t) dt.
    k=b/B
    # Exact metric transformation: x=p X, v=V+(c*p*X^2)/2.
    du=a;dv=a+c*p1*b*b/2;dx=p1*b
    label=str(len(rows))
    checks[label+'_endpoint_fixed_point']=4*a==k*k*C
    checks[label+'_transverse_endpoint']=B*k==b
    checks[label+'_orthogonal_in_minkowski']=du+dv==0
    checks[label+'_finite_spacelike_norm']=dx*dx-2*du*dv==dx*dx+2*a*a>0
    checks[label+'_physical_transverse_component']=k/p0==dx
    checks[label+'_same_clock_endpoint_not_orthogonal']=c*p0*b*b/2!=0
    checks[label+'_clock_shift_differs_from_quadratic_truncation']=a!=-c*p0*b*b/4
    rows.append(dict(c=str(c),u=str(u),baseline=str(b),clock_shift_u=str(a),
                     transverse_separation=str(dx),separation_squared=str(dx*dx+2*a*a)))
# Uniform constants for the actual high-frequency vacuum family, n>=4,
# u in [-1,2]: gamma >=lambda I, gamma<=B0 I, ||gamma'||<=4/n, ||gamma''||<=4.
lam=F(1,2);B0=F(4,3);B1max=F(1);B2max=F(4)
H1max=B1max/lam**2
H2max=2*B1max**2/lam**3+B2max/lam**2
radius=F(1,4);baseline=F(1,4)
image_bound=B0**2*H1max*baseline**2/8
lipschitz=(B0**3*H1max**2/8+B0**2*H2max/24)*baseline**2
checks['metric_lower_bound']=F(7,8)**2*F(3,4)==F(147,256)>lam
checks['second_derivative_envelope']=F(4,3)*(F(8,4**4)+F(6,4**2)+F(16,4**3)+2)==F(85,24)<B2max
checks['inverse_metric_derivative_constants']=H1max==4 and H2max==32
checks['connector_interval_self_map']=image_bound==F(1,18)<radius
checks['uniform_contraction']=lipschitz==F(4,9)<1
checks['finite_clock_shift_bound_coefficient']=B0**2*16/8==F(32,9)
checks['transverse_error_bound_coefficient']=F(3,2)*B0**2*F(16,2)*F(32,9)==F(2048,27)<76
# This is bound evaluation, not numerical construction of r_n.
envelopes=[]
for n in (4,8,16,32,64):
    clock=F(32,9*n)*baseline**2
    transverse=F(76,n*n)*baseline**3
    # sqrt(2)<3/2 used for a rational longitudinal envelope.
    longitudinal=F(3,2)*clock
    total=F(5,n*n)*baseline+transverse+longitudinal
    envelopes.append(dict(n=n,clock=str(clock),transverse_error=str(transverse),longitudinal_error=str(longitudinal),total_displacement=str(total)))
checks['finite_baseline_envelope_tends_down']=all(F(envelopes[i+1]['total_displacement'])<F(envelopes[i]['total_displacement']) for i in range(len(envelopes)-1))
checks['same_baseline_used_for_all_frequencies']=baseline==F(1,4)
root=Path(__file__).resolve().parents[2]
paths=[Path(__file__),root/'research/voevodsky/geodesic-detector-readout-survives-c1-completion.md',root/'research/strominger/sources/fghn1901.00021.txt']
packet=dict(passed=all(checks.values()),checks=checks,flat_connector_controls=rows,vacuum_family_bounds=envelopes,
    scope='Exact finite connector identities and contraction constants. No sampled proof of the all-n vacuum metric estimates; no radar/interferometer or arbitrary-spacetime assertion.',
    source_sha256={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
Path(__file__).with_name('finite-baseline-fermi-detector.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
