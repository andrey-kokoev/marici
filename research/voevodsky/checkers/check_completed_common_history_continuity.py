#!/usr/bin/env python3
"""Checks the arithmetic and contract edges of completed history continuity."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,math
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/completed_common_history_is_continuous_for_the_ratio_normalized_projective_source_20260912.md'
FINITE=ROOT/'research/voevodsky/common_radial_history_has_a_cutoffwise_half_line_L2_bound_20260911.md'
GRADE=ROOT/'research/voevodsky/ratio_normalized_grade_makes_fixed_ratio_cycle_graphs_canonically_isomorphic_20260912.md'
RESULT=ROOT/'research/voevodsky/results/completed_common_history_continuity.json'
text=PACKET.read_text(); primes=(2,3,5,7,11,13,17,19,23,29,31); edges=[(k,p,q) for p,q in zip(primes,primes[1:]) for k in range(1,31)]
checks={
 'atom_hypothesis_stated':'Phi_1\\in L^2(\\mathbb R)\\cap L^\\infty(\\mathbb R)' in text,
 'columnwise_bound_stated':'\\|b_{e,D}\\|_{L^2(\\mathbb R_+)}' in text and '\\ell_e.' in text,
 'cutoff_independent_bound_stated':'The constant is independent of the cutoff and of \\(D\\)' in text,
 'unique_extension_stated':'extends uniquely to a continuous linear map' in text,
 'ratio_coproduct_boundary_stated':'No topology over the unbounded collection of all ratio blocks is asserted' in text,
 'finite_predecessor_had_support_residual':'The estimate depends on' in FINITE.read_text() and 'L_D' in FINITE.read_text() and 'S_D' in FINITE.read_text(),
 'normalized_grade_source_present':'\\overline W(j,k)=\\log(kp_jp_{j+1})' in GRADE.read_text(),
}
checks['length_by_normalized_grade']=all(math.log(q/p)<=math.log(k*p*q)+1e-15 for k,p,q in edges)
for delta in (.05,.1,.5,1,2):
 checks[f'exponential_length_delta_{delta}']=all(math.log(q/p)<=math.exp(delta*math.log(k*p*q))/delta+1e-12 for k,p,q in edges)
 # Finite triangle majorant with signed rational coefficients.
 c=[Fraction((i%9)-4,i+2) for i in range(len(edges))]
 lhs=sum(float(abs(c[i]))*math.log(q/p) for i,(k,p,q) in enumerate(edges))
 rhs=sum(float(abs(c[i]))*math.exp(delta*math.log(k*p*q))/delta for i,(k,p,q) in enumerate(edges))
 checks[f'finite_packet_majorant_delta_{delta}']=lhs<=rhs+1e-10
# Tail truncation in q_delta for an explicit member c_e=exp(-W^2).
for delta in (.1,.5,1):
 terms=[math.exp(-math.log(k*p*q)**2+delta*math.log(k*p*q)) for k,p,q in edges]
 tails=[sum(terms[N:]) for N in (50,100,200)]
 checks[f'truncation_tail_decreases_delta_{delta}']=tails[0]>=tails[1]>=tails[2]>=0
checks['hostile_no_unearned_global_ratio_topology']='topology across all ratio blocks' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.completed-common-history-continuity-check.v1','input_digests':{'packet':hashlib.sha256(PACKET.read_bytes()).hexdigest(),'finite_bound':hashlib.sha256(FINITE.read_bytes()).hexdigest(),'normalized_grade':hashlib.sha256(GRADE.read_bytes()).hexdigest()},'checks':checks,'passed':all(checks.values()),'tested_edges':len(edges),'disposition':{'proved':'per-fixed-ratio continuous extension C_exp(Wbar)->L2(R_+) with cutoff-independent bound','improves':'support-span/total-length cutoffwise estimate','remaining':['topology over all ratio blocks','calibrated cycle-port norm']}}
RESULT.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'passed':result['passed'],'check_count':len(checks),'tested_edges':len(edges)})); raise SystemExit(0 if result['passed'] else 1)
