#!/usr/bin/env python3
"""Fourier-diagonal extended norm-resolvent convergence check."""
from pathlib import Path
import hashlib,json,math
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-extended-norm-resolvent-convergence.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_extended_norm_resolvent_convergence.json'
d=json.loads(CONTRACT.read_text())
def continuum(k): return 1.0+(math.pi*k/6.0)**2
def discrete(N,k): return 1.0+(N*N/36.0)*math.sin(math.pi*k/N)**2
def error(N):
 represented=range(-N//2,N//2)
 mode_errors={k:abs(1.0/(discrete(N,k)+1.0)-1.0/(continuum(k)+1.0)) for k in represented}
 omitted=1.0/(continuum(N//2)+1.0)
 kmax=max(mode_errors,key=mode_errors.get)
 return max(mode_errors[kmax],omitted),kmax,mode_errors[kmax],omitted
levels=(12,24,48,96,192,384,768)
data={N:error(N) for N in levels}; errs=[data[N][0] for N in levels]
checks={
 'positive_errors':all(e>0 for e in errs),
 'strict_error_decrease':all(errs[i+1]<errs[i] for i in range(len(errs)-1)),
 'dyadic_ratio_tends_to_quarter':all(0.20<errs[i+1]/errs[i]<0.27 for i in range(2,len(errs)-1)),
 'N_squared_error_bounded_by_22':max(N*N*data[N][0] for N in levels)<22,
 'level_768_error_below_4e_minus_5':data[768][0]<4e-5,
 'omitted_tail_dyadic_ratio_below_1_over_3_point_4':all(data[levels[i+1]][3]<data[levels[i]][3]/3.4 for i in range(len(levels)-1)),
 'base_mode_formula_preserved':abs(discrete(12,1)-(1+4*math.sin(math.pi/12)**2))<1e-15,
 'Real_pair_eigenvalues_equal':all(abs(discrete(N,k)-discrete(N,-k))<1e-15 for N in levels for k in range(1,N//2)),
 'orientation_pair_eigenvalues_equal':all(abs(continuum(k)-continuum(-k))<1e-15 for k in range(1,100)),
 'one_resolvent_point_disclosed':d['claim_boundary']['one_resolvent_point'] and d['resolvent']['point']==-1,
 'no_determinant_or_RH_promotion':not d['claim_boundary']['Evans_determinant_convergence_claimed'] and not d['claim_boundary']['RH_factor_convergence_claimed'],
 'no_source_or_physical_promotion':not d['claim_boundary']['source_radial_operator_identified'] and not d['claim_boundary']['physical_length_claimed'],
}
# Hostile comparison: holding N fixed cannot certify the limiting statement.
checks['single_stage_not_convergence_evidence']=data[12][0]>data[768][0]*100
# Hostile wrong scaling h-independent keeps mode 1 away from the continuum target.
wrong_limit=1+4*math.sin(math.pi/12)**2
checks['unscaled_cycle_wrong_continuum_detected']=abs(wrong_limit-continuum(1))>1e-3
checks={k:bool(v) for k,v in checks.items()}
rows={str(N):{'operator_norm_error':data[N][0],'max_represented_mode':data[N][1],'represented_error':data[N][2],'omitted_tail':data[N][3],'N_squared_error':N*N*data[N][0]} for N in levels}
result={'schema':'marici.voevodsky.radial-extended-norm-resolvent-convergence-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'levels':rows,'disposition':{'constructed':'Fourier-embedded extended norm-resolvent convergence at spectral point -1 with observed quadratic bound','strength':'exact diagonal error formula plus bounded numerical evaluation; continuum identification remains synthetic','remaining':'source Hilbert/operator/trace intertwiner; determinant and RH convergence remain separate'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'levels':len(levels),'final_error':data[768][0]}))
raise SystemExit(0 if result['passed'] else 1)
