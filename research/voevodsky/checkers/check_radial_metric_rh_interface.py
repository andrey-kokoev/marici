#!/usr/bin/env python3
"""Check metric descent and locate the first typed RH-chain interface gap."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
CAL=ROOT/'research/voevodsky/contracts/radial-synthetic-calibration-companion.v1.json'
RH=ROOT/'research/aspect/contracts/theta-rh-interaction-net-state.v3.json'
RESULT=ROOT/'research/voevodsky/results/radial_metric_rh_interface.json'
c=json.loads(CAL.read_text()); r=json.loads(RH.read_text())
checks={}
# Z/4 exact gauge shadow.
q=4; U=tuple((j+1)%q for j in range(12)); g=tuple((j*j+j)%q for j in range(12))
Ug=tuple((U[j]+g[(j+1)%12]-g[j])%q for j in range(12))
checks['Wilson_descends']=sum(U)%q==sum(Ug)%q
psi=tuple((2*j+1)%q for j in range(12)); psig=tuple((psi[j]+g[j])%q for j in range(12))
checks['unframed_bulk_descent_rejected']=psi!=psig and c['record_map']['bulk']['frame_policy']=='declared_local_node_frames_retained'
# Exact covariance-isometry shadow: signed Real action preserves parity-block covariance.
Sigma=[[F(0) for _ in range(4)] for _ in range(4)]
for i,v in enumerate((F(2),F(3),F(5),F(7))): Sigma[i][i]=v
Sigma[0][2]=Sigma[2][0]=F(1); Sigma[1][3]=Sigma[3][1]=F(1)
s=(1,-1,1,-1)
checks['Real_covariance_isometry']=all(Sigma[i][j]==s[i]*s[j]*Sigma[i][j] for i in range(4) for j in range(4))
# Opposite parity mutation must fail.
bad=[row[:] for row in Sigma]; bad[0][1]=bad[1][0]=F(1)
checks['opposite_parity_covariance_rejected']=not all(bad[i][j]==s[i]*s[j]*bad[i][j] for i in range(4) for j in range(4))
# Pullback rank criterion: rank-deficient record differential gives pseudometric.
def rank(A):
 A=[list(map(F,row)) for row in A]; m=len(A); n=len(A[0]); rr=0
 for col in range(n):
  pivot=next((i for i in range(rr,m) if A[i][col]),None)
  if pivot is None: continue
  A[rr],A[pivot]=A[pivot],A[rr]; p=A[rr][col]
  A[rr]=[x/p for x in A[rr]]
  for i in range(m):
   if i!=rr and A[i][col]:
    z=A[i][col]; A[i]=[a-z*b for a,b in zip(A[i],A[rr])]
  rr+=1
 return rr
checks['injective_record_differential_gives_metric']=rank([[1,0],[0,1],[1,1]])==2
checks['rank_loss_gives_only_pseudometric']=rank([[1,0],[2,0]])<2
constructors={x['id']:x['status'] for x in r['constructors']}
checks['downstream_chain_explicitly_open']=constructors.get('downstream_evans_green_rh_chain')=='open'
checks['calibrated_record_dimension_declared']=c['record_map']['joint']['dimension']==26
# Search exact serialized contracts for any claimed calibrated comparison.
rhtext=RH.read_text(); caltext=CAL.read_text()
needles=('calibrated_record_to_four_trace','four_trace_to_calibrated_record','C_cal')
checks['comparison_map_absent']=not any(n in rhtext or n in caltext for n in needles)
checks['four_traces_declared']=r['interface']['boundary_trace']==['P','Q','M','J']
checks['response_names_do_not_supply_comparison']=r['interface']['response']==['K','H_K','compatible_J_K_family'] and checks['comparison_map_absent']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-metric-rh-interface-check.v1','inputs':{'calibration_sha256':hashlib.sha256(CAL.read_bytes()).hexdigest(),'rh_v3_sha256':hashlib.sha256(RH.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'first_missing_typed_object':{'id':'calibrated_record_four_trace_comparison','required_signature':'R^26 <-> Y_P plus Y_Q plus Y_M plus Y_J','required_properties':['evaluable_rule','units','gauge_equivariance','Real_equivariance','covariance_transport','quotient_kernel_and_rank'],'status':'absent'},'disposition':'conditional_metric_descent_survives_downstream_metric_transport_deferred_at_first_missing_comparison'}
RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'first_missing':result['first_missing_typed_object']['id']}))
raise SystemExit(0 if result['passed'] else 1)
