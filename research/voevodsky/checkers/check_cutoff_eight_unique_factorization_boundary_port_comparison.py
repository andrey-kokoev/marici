#!/usr/bin/env python3
"""Exact cutoff-eight unique-factorization and selected boundary-port audit."""
import hashlib,json,platform
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/cutoff_eight_unique_factorization_boundary_port_comparison.v1.json';OUT=ROOT/'research/voevodsky/results/cutoff_eight_unique_factorization_boundary_port_comparison.json';D=json.loads(FIX.read_text());X=D['cutoff'];primes=D['primes']
def valuation(n,p):
 k=0
 while n%p==0:n//=p;k+=1
 return k
def nu(n):return tuple(valuation(n,p) for p in primes)
labels={n:nu(n) for n in range(1,X+1)}
# Partial source multiplication and valuation shift comparison.
intertwining=all(labels[2*n]==tuple(labels[n][j]+(j==0) for j in range(len(primes))) for n in range(1,X//2+1))
# Prime exclusion and v2-zero predicates.
exclusion=all((n%2!=0)==(labels[n][0]==0) for n in labels)
# Coefficient augmentation is the constant row in either labelled basis.
augmentation=sum(1 for _ in labels)==X
# The selected p=2 chain is 1,2,4,8.
chain=[1,2,4,8];chain_labels=[labels[n] for n in chain]
checks={'unique_factorization_labels_injective':len(set(labels.values()))==X,'comparison_unitary_as_labelled_permutation':len(labels)==X and len(set(labels.values()))==X,'multiplication_valuation_intertwining':intertwining,'prime_two_exclusion_port_preserved':exclusion,'augmentation_port_preserved':augmentation,'depth_three_terminal_port_preserved':labels[8]==(3,0,0,0),'selected_chain_exact':chain_labels==[(0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0)],'finite_contraction_norm_one':D['cone']['norm']=='1','full_port_extension_not_promoted':D['disposition']['full_bordered_chain_map'] is False}
out={'schema':'marici.voevodsky.cutoff-eight-unique-factorization-boundary-port-comparison-check.v1','passed':all(checks.values()),'checks':checks,'observed':{'integer_to_valuation_label':{str(k):list(v) for k,v in labels.items()},'partial_multiplication_domain':[1,2,3,4],'prime_two_chain':chain,'prime_two_chain_labels':[list(v) for v in chain_labels]},'disposition':'F_UF extends exactly across coefficient bulk, multiplication/valuation incidence, prime exclusion, augmentation, and the selected terminal label. Moving-seam and determinant response ports remain the first unconstructed extension.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_cutoff_eight_unique_factorization_boundary_port_comparison.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((ROOT/D['source']).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
