"""Compare signed k-step errors with occurrence ranks of prime subsets in Pascal coefficients. Count each step at most once per (arity,rank); different bins may overlap."""
import csv,math,itertools,statistics,collections
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';steps={(int(z['l']),int(z['k'])):z for z in csv.DictReader((D/'ramsey_prime_step_test.csv').open())};field={(int(z['l']),int(z['k'])):z for z in csv.DictReader((D/'ramsey_mixed_field_26.csv').open())};bins=collections.defaultdict(list);whole=collections.Counter();pr=[p for p in range(2,50) if all(p%i for i in range(2,math.isqrt(p)+1))]
for a in range(3,27):
    counts=collections.Counter();signatures=collections.Counter()
    for b in range(2,27):
        n=math.comb(a+b-4,a-2);sig=tuple(p for p in pr if n%p==0);signatures[sig]+=1;tags=set()
        for ar in (1,2,3):
            for s in itertools.combinations(sig,ar):counts[s]+=1;tags.add((ar,min(counts[s],4)))
        if (a,b) not in steps:continue
        z=steps[a,b];exact=all(field[min(i,j),max(i,j)]['audit']=='exact' for i,j in ((a,b),(a,b-1),(a-1,b),(a-1,b-1),(a,b-2),(a-1,b-2)));tags.add(('whole',min(signatures[sig],4)));whole[min(signatures[sig],4)]+=1
        for t in tags:bins[t].append((float(z['delta_log']),exact,z['reverse']=='True',a,b))
for t,g in bins.items():pass
with (D/'ramsey_prime_combo_steps.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['arity','occurrence_4_means_4plus','steps','typical_growth_ratio','exact_steps','exact_reversals','reversal_cells']);
 for ar in [1,2,3,'whole']:
    for rank in range(1,5):
        g=bins[ar,rank];r=(ar,rank,len(g),math.exp(statistics.median(z[0] for z in g)) if g else '',sum(z[1] for z in g),sum(z[1] and z[2] for z in g),';'.join(f'{a}:{b}' for _,_,v,a,b in g if v));print(r);w.writerow(r)
