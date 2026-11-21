"""Moment counterexample, exhaustive balanced SAT stage and bounded one-chord sample."""
from ramsey_39_twelve_order_sat import *
D=Path(__file__).parent
h=[12]+[3]*12+[4]*22+[2]*4;r=[12]+([2]*2+[3]*6+[4]*11)*2
assert len(h)==len(r)==39 and sum(h)==sum(r)==144 and sum(x*x for x in h)==sum(x*x for x in r)==620 and sum(x%2 for x in h)==12 and sum(min(9,2*x) for x in h)==273
if sys.argv[1]=='balanced':
    results={m:test(tuple(i for i in range(39) if int(m)>>i&1),degree_budget=True) for m in (D/'ramsey_39_balanced_masks.txt').read_text().split()};print(Counter(results.values()));(D/'ramsey_39_balanced_results.json').write_text(json.dumps(results))
else:
    rng=Random(31039);stats=Counter();pairs=Counter();seen=set();end=monotonic()+float(sys.argv[1]);examples=[]
    while monotonic()<end:
        W=tuple(sorted([0,1]+rng.sample(range(2,39),10)))
        if W in seen:continue
        seen.add(W);H=Counter((a+b)%39 for a in W for b in W)
        if len(H)!=39:stats['uncovered']+=1;continue
        tested=False
        for a,b in combinations(W,2):
            cap=[min(9,2*H[p]+int((p-a)%39 in W)+int((p-b)%39 in W)) for p in range(39)]
            if min(cap)<3 or sum(cap)<272:continue
            tested=True;status=test(W,degree_budget=True,chord=(a,b));pairs[status.split(':')[0]]+=1
            if status.startswith('candidate'):examples.append((W,a,b,status))
        stats['tested' if tested else 'no feasible chord caps']+=1
    print(len(seen),stats,pairs,'candidates',len(examples));(D/'ramsey_39_chord_sample.json').write_text(json.dumps({'stats':stats,'pairs':pairs,'candidates':examples}))
