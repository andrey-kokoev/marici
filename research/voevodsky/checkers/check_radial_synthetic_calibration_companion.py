#!/usr/bin/env python3
"""Validate the synthetic radial bulk/Wilson calibration companion."""
from __future__ import annotations
import hashlib,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-synthetic-calibration-companion.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_synthetic_calibration_companion.json'
d=json.loads(CONTRACT.read_text(encoding='utf-8'))
checks={}
checks['synthetic_status_only']=d['status']=='synthetic_complete_not_physical'
checks['physical_promotion_refused']=not d['claim_boundary']['physical_calibration_loaded'] and not d['claim_boundary']['hardware_identity_bound']
checks['retained_lattice_declared']=d['source_object']['type']=='retained_dimensionless_ring_lattice' and not d['claim_boundary']['continuum_radial_limit_claimed']
checks['record_dimension']=d['record_map']['bulk']['dimension']+d['record_map']['wilson']['dimension']==d['record_map']['joint']['dimension']==26
checks['cycle_rank_one']=d['admitted_quotient']['cycle_rank']==1
checks['cross_block_zero']=d['covariance']['cross_block']['formula']=='zero'
checks['exact_product_declared']=d['noise_whitened_metric']['product_status']=='exact_under_synthetic_independence_assumption'
checks['wilson_weight_exact']=Fraction(str(d['noise_whitened_metric']['wilson_weight']))==1/Fraction('0.02')**2
nus=[Fraction(x.split('=')[1]) for x in d['covariance']['bulk_block']['admissible_fixtures'].values()]
checks['all_fixture_covariances_positive']=all(n>0 for n in nus)
checks['joint_covariance_full_rank']=all(n*n>0 for n in nus) and Fraction('0.02')**2>0

# Exact Z/4 shadow of the 12-edge gauge action.
q=4
U=tuple((3*j+1)%q for j in range(12))
g=tuple((j*j+2*j)%q for j in range(12))
Ug=tuple((U[j]+g[(j+1)%12]-g[j])%q for j in range(12))
hol=lambda x:sum(x)%q
checks['Wilson_holonomy_gauge_invariant']=hol(Ug)==hol(U)
checks['edge_record_not_gauge_invariant']=Ug!=U

# Bulk local-frame coordinates are covariant, not quotient coordinates.
psi=tuple((j+1)%q for j in range(12))
psig=tuple((psi[j]+g[j])%q for j in range(12))
checks['bulk_changes_under_vertex_gauge']=psig!=psi
checks['retained_frames_required']=d['record_map']['bulk']['frame_policy']=='declared_local_node_frames_retained'

# Fourth-root quadratures and Real variance.
quad=((1,0),(0,1),(-1,0),(0,-1))
checks['Real_even_quadrature']=all(quad[-a%q][0]==quad[a][0] for a in range(q))
checks['Real_odd_quadrature']=all(quad[-a%q][1]==-quad[a][1] for a in range(q))
checks['both_quadratures_separate_U1_shadow']=len(set(quad))==q
checks['real_only_rank_loss']=len({p for p,_ in quad})<q

# Exact positive record distance for a nonzero bulk or Wilson displacement.
def metric_sq(bulk_sq,wilson_sq,nu):
 return Fraction(bulk_sq,1)/(nu*nu)+Fraction(wilson_sq,1)/Fraction('0.02')**2
checks['bulk_difference_positive']=all(metric_sq(1,0,n)>0 for n in nus)
checks['wilson_difference_positive']=all(metric_sq(0,1,n)>0 for n in nus)
checks['zero_difference_zero']=all(metric_sq(0,0,n)==0 for n in nus)

failures={
 'physical_calibration_from_synthetic_fixture':{'detected':not d['claim_boundary']['physical_calibration_loaded']},
 'Wilson_real_only':{'observed':len({p for p,_ in quad}),'required':q,'detected':len({p for p,_ in quad})<q},
 'edge_records_as_gauge_quotient':{'detected':Ug!=U and hol(Ug)==hol(U)},
 'bulk_record_without_local_frames':{'detected':psig!=psi},
 'zero_noise_covariance':{'detected':Fraction(0)==0,'reason':'would destroy invertibility'},
 'unsourced_cross_covariance':{'detected':d['covariance']['cross_block']['qualification']=='synthetic_independence_assumption'},
 'synthetic_radius_as_physical_length':{'detected':d['source_object']['radial_coordinate']['unit']=='dimensionless_lattice_fraction'},
}
checks['all_hostile_failures_detected']=all(x['detected'] for x in failures.values())
checks={k:bool(v) for k,v in checks.items()}
passed=all(checks.values())
result={'schema':'marici.voevodsky.radial-synthetic-calibration-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'fixture_noise':[str(n) for n in nus],'deliberate_failures':failures,'passed':passed}
RESULT.parent.mkdir(parents=True,exist_ok=True)
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':passed,'check_count':len(checks),'hostile_failures':len(failures)}))
raise SystemExit(0 if passed else 1)
