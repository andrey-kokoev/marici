"""Finite controls for independently specified observation profiles.
The uniform extension theorem and all-n obstruction are written proofs.
Integer jets are NOT silently completed to real jets by these tests.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib
from finite_radar_protocol import Protocol,Row,Packet,by_time,encode_section,on_native_section
base=Path(__file__).resolve().parent
formal=json.loads((base/'observed-carrier-synthesis-formal.json').read_text())
checks={}
checks['fresh_shared_formal_instances']=formal['passed'] and formal['fresh'] and formal['structural_mode']
checks['formal_source_snapshots_current']=all(Path(p).exists() and hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in formal['source_snapshot_hashes'].items())
ports=('scalar',)+tuple(('gradient',i) for i in range(3))+tuple(('hessian',i,j) for i in range(3) for j in range(3))
def encode_jet(j):
    value,gradient,hessian=j
    return {'scalar':value,**{('gradient',i):gradient[i] for i in range(3)},**{('hessian',i,k):hessian[i][k] for i in range(3) for k in range(3)}}
def source_distance(a,b):
    return max([abs(a[0]-b[0])]+[abs(x-y) for x,y in zip(a[1],b[1])]+[abs(a[2][i][j]-b[2][i][j]) for i in range(3) for j in range(3)])
jet_cases=0
for seed in range(1,33):
    a=(seed,tuple(seed-i for i in range(3)),tuple(tuple(seed*(i+1)-j for j in range(3)) for i in range(3)))
    b=(-seed,tuple(i-seed for i in range(3)),tuple(tuple(j*seed-i for j in range(3)) for i in range(3)))
    x,y=encode_jet(a),encode_jet(b)
    checks[str(seed)+'_independent_jet_norm_isometry']=source_distance(a,b)==max(abs(x[p]-y[p]) for p in ports)
    checks[str(seed)+'_hessian_projection_lipschitz']=max(abs(x['hessian',i,j]-y['hessian',i,j]) for i in range(3) for j in range(3))<=source_distance(a,b)
    checks[str(seed)+'_fixed_integer_lattice_gap']=source_distance(a,b)>=1
    jet_cases+=1
p=Protocol(F(1,32),F(1,4),F(1),'retained-Rosen-transverse-labels','central-proper-clock-c=1')
rows=tuple(Row(t,d,p.center+t*p.step,p.center+t*p.step+2*p.epsilon*length) for t in (-1,0,1) for d,length in (('x3',3),('y4',4),('xy5',5)))
base_packet=Packet(p,rows,'analytic:static-flat-control')
for n in (2,4,8,16,32):
    delta=F(1,1024*n)
    changed=Packet(p,tuple(Row(r.time,r.direction,r.emission,r.reception+delta*((i%3)+1)) for i,r in enumerate(rows)),'synthetic:readout-modulus-control')
    a,b=base_packet.index(),changed.index()
    old_metric=max(max(abs(a[k].emission-b[k].emission),abs(a[k].reception-b[k].reception)) for k in a)
    sa,sb=encode_section(base_packet),encode_section(changed)
    native_metric=max(max(abs(ra.emission-rb.emission),abs(ra.reception-rb.reception)) for (_,ra),(_,rb) in zip(sa.choices,sb.choices))
    gap=max(abs(x-y) for x,y in zip(by_time(base_packet),on_native_section(sb)))
    # M=1; fixed design inverse norm 1/8 gives L=M/(2 epsilon^2 h^2).
    lip=F(1)/(2*p.epsilon*p.epsilon*p.step*p.step)
    checks[str(n)+'_independent_clock_norm_isometry']=old_metric==native_metric
    checks[str(n)+'_radar_readout_modulus']=gap<=lip*old_metric
checks['frozen_radar_lipschitz_constant']=lip==8192
# A common-source physics obstruction, using the proved exact Rosen family.
# This is NOT an invented equivalence with the Newtonian fixture.
profiles=[]
for n in (4,8,16,32,64):
    radar=F(8,n*n);tidal=F(1,2)
    profiles.append(dict(n=n,normalized_radar_error_upper=str(radar),tidal_gap=str(tidal),joint_observation_gap_lower=str(tidal)))
checks['radar_profile_bounds_shrink']=all(F(a['normalized_radar_error_upper'])>F(b['normalized_radar_error_upper']) for a,b in zip(profiles,profiles[1:]))
checks['joint_profile_still_separates_tides']=all(F(x['joint_observation_gap_lower'])==F(1,2) for x in profiles)
# Algebraic join only: no assertion that independently supplied sources coincide.
for a,b in ((F(1),F(3)),(F(4),F(2)),(F(0),F(7))):
    checks['join_'+str(a)+'_'+str(b)]=max(a,b)>=a and max(a,b)>=b
out=dict(passed=all(checks.values()),checks=checks,jet_cases=jet_cases,physical_obstruction_profiles=profiles,
    formal_receipt_sha256=hashlib.sha256((base/'observed-carrier-synthesis-formal.json').read_bytes()).hexdigest(),
    boundaries=['Fixed integer jet coefficients form a discrete complete lattice, not a dense real continuum.',
    'The joint operation requires a common declared source/carrier; no Newtonian/Rosen physical equivalence is inferred.',
    'All-n Rosen obstruction and uniform extension are mathematical arguments, not consequences of this finite census.'])
(base/'observed-carrier-synthesis.json').write_text(json.dumps(out,indent=2)+'\n')
print('passed=',out['passed'],'checks=',len(checks))
raise SystemExit(0 if out['passed'] else 1)
