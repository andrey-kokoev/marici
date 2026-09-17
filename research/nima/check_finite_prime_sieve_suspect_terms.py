import json
from pathlib import Path
N=120
primes=(2,3)
removed=[n for n in range(1,N+1) if any(n%p==0 for p in primes)]
retained=[n for n in range(1,N+1) if all(n%p for p in primes)]
out={'schema':'marici.nima.finite-prime-sieve-suspect-terms.v1','N':N,'selected_primes':primes,'removed_divisible_labels':removed,'retained_labels':retained,'checks':{'partition_exact':len(removed)+len(retained)==N,'no_retained_label_divisible':all(all(n%p for p in primes) for n in retained),'primitive_label_retained':1 in retained},'interpretation':'sieve deletion removes exactly the divisible theta labels; no sign estimate or arbitrary term removal is used','next_test':'attach explicit phi_n values and test the surviving finite sum'}
out['passed']=all(out['checks'].values());out['rh_proved']=False
p=Path(__file__).resolve().parents[2]/'research/nima/results/finite-prime-sieve-suspect-terms.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
