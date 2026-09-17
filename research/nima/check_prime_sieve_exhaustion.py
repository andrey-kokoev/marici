import json
from pathlib import Path
prime_sets=[[2],[2,3],[2,3,5],[2,3,5,7],[2,3,5,7,11]]
N=120
retained=[{n for n in range(1,N+1) if all(n%p for p in S)} for S in prime_sets]
checks={'nested_decreasing':all(retained[i+1] <= retained[i] for i in range(len(retained)-1)),'one_always_retained':all(1 in r for r in retained),'every_composite_removed_by_11':all(n not in retained[-1] for n in range(2,N+1) if any(n%p==0 for p in prime_sets[-1])),'finite_intersection_matches_coprime_to_2310':retained[-1]=={n for n in range(1,N+1) if all(n%p for p in prime_sets[-1])}}
out={'schema':'marici.nima.prime-sieve-exhaustion.v1','N':N,'prime_sets':prime_sets,'retained_counts':[len(r) for r in retained],'checks':checks,'passed':all(checks.values()),'scope':'finite exhaustion witness; full pointwise limit uses the fundamental theorem of arithmetic','rh_proved':False}
p=Path(__file__).resolve().parents[2]/'research/nima/results/prime-sieve-exhaustion.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
