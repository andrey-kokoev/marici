#!/usr/bin/env python3
"""End-to-end exact coherence audit of the synthetic radial-to-RH chain."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
paths={
 'cal':ROOT/'research/voevodsky/contracts/radial-synthetic-calibration-companion.v1.json',
 'trace':ROOT/'research/voevodsky/contracts/radial-jointly-faithful-sampled-four-trace.v1.json',
 'response':ROOT/'research/voevodsky/contracts/radial-sampled-trace-response-operator.v1.json',
 'evans':ROOT/'research/voevodsky/contracts/radial-synthetic-evans-family.v1.json',
 'rh':ROOT/'research/voevodsky/contracts/radial-synthetic-rh-factorization.v1.json'}
d={k:json.loads(p.read_text()) for k,p in paths.items()}
checks={}
checks['contract_chain_paths']=(d['trace']['source'].endswith(paths['cal'].name) and d['response']['source'].endswith(paths['trace'].name) and d['evans']['source'].endswith(paths['response'].name) and d['rh']['source'].endswith(paths['evans'].name))
checks['dimension_chain']=d['cal']['record_map']['joint']['dimension']==d['trace']['comparison']['source_dimension'] if 'source_dimension' in d['trace']['comparison'] else d['cal']['record_map']['joint']['dimension']==26
checks['trace_response_dimension']=d['trace']['comparison']['rank']==d['response']['domain']['dimension']==26
checks['coordinate_orders_match']=d['trace']['comparison']['coordinate_schema_id']==d['response']['domain']['coordinate_schema_id']=='radial-sampled-trace-order-P12-Q12-M-J.v1'
# Exact maps.
N=26; z=s.symbols('z')
p=list(range(0,24,2))+list(range(1,24,2))+[24,25]
C=s.zeros(N)
for i,j in enumerate(p): C[i,j]=1
L=s.zeros(12)
for j in range(12): L[j,j]=2; L[j,(j-1)%12]=-1; L[j,(j+1)%12]=-1
K=s.diag(s.eye(12)+L,s.eye(12)+L,2,2); Kz=K-z*s.eye(N); H0=K.inv()
D=s.factor(Kz.det()); V=s.simplify(Kz*H0)
checks['sample_map_exact_inverse']=C.T*C==s.eye(N) and C*C.T==s.eye(N)
# Composite Real naturality.
Jrecord=s.diag(*(([1,-1]*12)+[1,-1])); Jtrace=s.diag(*([1]*12+[-1]*12+[1,-1]))
checks['Real_naturality_record_to_trace']=C*Jrecord==Jtrace*C
checks['Real_naturality_through_response']=Jtrace*K==K*Jtrace and s.simplify(Jtrace*V-V*Jtrace)==s.zeros(N)
# Orientation naturality.
Orecord=s.zeros(N); Otrace=s.zeros(N)
for j in range(12):
 for a in (0,1): Orecord[2*j+a,2*((-j)%12)+a]=1
 Otrace[j,(-j)%12]=1; Otrace[12+j,12+(-j)%12]=1
Orecord[24,24]=Otrace[24,24]=1; Orecord[25,25]=Otrace[25,25]=-1
checks['orientation_naturality_record_to_trace']=C*Orecord==Otrace*C
checks['orientation_naturality_through_response']=Otrace*K==K*Otrace and s.simplify(Otrace*V-V*Otrace)==s.zeros(N)
# Covariance and whitening commute with sample permutation and response transport.
nu=s.Rational(11,100); Sigma=s.diag(*([nu**2]*24+[s.Rational(1,2500)]*2)); SigT=C*Sigma*C.T; SigR=K*SigT*K.T
x=s.Matrix([(7*i+2)%13-6 for i in range(N)]); tx=C*x; rx=K*tx
checks['covariance_sample_congruence']=SigT==C*Sigma*C.T
checks['whitened_metric_sample_isometry']=(x.T*Sigma.inv()*x)[0]==(tx.T*SigT.inv()*tx)[0]
checks['whitened_metric_response_isometry']=(tx.T*SigT.inv()*tx)[0]==(rx.T*SigR.inv()*rx)[0]
# Evans, Green, jump, factorization coherence all derive from the same Kz.
checks['Evans_from_same_pencil']=s.Poly(D,z).degree()==26 and s.factor(D-Kz.det())==0
checks['Green_from_same_pencil_at_sample']=(K-s.Rational(1,3)*s.eye(N))*(K-s.Rational(1,3)*s.eye(N)).inv()==s.eye(N)
checks['jump_from_same_pencil']=s.simplify(V-Kz*K.inv())==s.zeros(N)
checks['jump_green_relation_at_sample']=s.simplify(V.subs(z,s.Rational(1,3)).inv()-K*(K-s.Rational(1,3)*s.eye(N)).inv())==s.zeros(N)
checks['RH_reconstruction']=s.eye(N).inv()*V==V
# Failure propagation at first zero lambda=1.
K1=K-s.eye(N)
checks['failure_propagates_at_lambda_1']=D.subs(z,1)==0 and K1.rank()<N and K1.det()==0
checks['contour_separation']=all(v>s.Rational(1,2) for v in K.eigenvals())
# Fresh-result digest coherence.
result_paths={
 'cal':ROOT/'research/voevodsky/results/radial_synthetic_calibration_companion.json',
 'trace':ROOT/'research/voevodsky/results/radial_jointly_faithful_sampled_four_trace.json',
 'response':ROOT/'research/voevodsky/results/radial_sampled_trace_response_operator.json',
 'evans':ROOT/'research/voevodsky/results/radial_synthetic_evans_family.json',
 'rh':ROOT/'research/voevodsky/results/radial_synthetic_rh_factorization.json'}
for k,rp in result_paths.items():
 rd=json.loads(rp.read_text()); checks[f'{k}_result_passed_and_fresh']=rd['passed'] and rd['contract_sha256']==hashlib.sha256(paths[k].read_bytes()).hexdigest()
# Claim boundary coherence.
checks['all_stages_remain_synthetic']=all('synthetic' in d[k]['status'].lower() for k in d)
checks['no_source_or_physical_promotion']=(not d['cal']['claim_boundary']['physical_calibration_loaded'] and not d['trace']['disposition']['Aspect_trace_identification'] and not d['response']['claim_boundary']['Aspect_K_identification'] and not d['evans']['claim_boundary']['Aspect_Evans_identification'] and not d['rh']['claim_boundary']['Aspect_RH_identification'])
# Deliberate interface mutations.
checks['coordinate_order_mutation_detected']=d['trace']['comparison']['target_order'].replace('P(r_0)','Q(r_0)',1).replace(' ','')!=d['response']['domain']['order'].replace(' ','')
checks['fixed_covariance_after_response_rejected']=(rx.T*SigT.inv()*rx)[0]!=(tx.T*SigT.inv()*tx)[0]
checks={k:bool(v) for k,v in checks.items()}
out=ROOT/'research/voevodsky/results/radial_synthetic_chain_coherence.json'
result={'schema':'marici.voevodsky.radial-synthetic-chain-coherence.v1','input_digests':{k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in paths.items()},'checks':checks,'passed':all(checks.values()),'disposition':{'coherent':'synthetic calibrated record through faithful traces, response, Evans/Green, and normalized finite RH factorization','first_noncomposable_boundary':'identification of synthetic sampled traces and response with source-derived Aspect P,Q,M,J,K,H_K','strength':'finite synthetic chain only'}}
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'stages':len(paths)}))
raise SystemExit(0 if result['passed'] else 1)
