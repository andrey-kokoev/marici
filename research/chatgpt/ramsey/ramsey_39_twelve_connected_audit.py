"""Replay the saved sample; enumerate every triangle-free budget-passing 2-factor, without independence cuts."""
from ramsey_39_twelve_order_sat import test,Random,Counter,json,Path,sevens
D=Path(__file__).parent;baseline=json.loads((D/'ramsey_39_twelve_order_sat.json').read_text());rng=Random(baseline['seed']);seen=set();rows=[]
while len(seen)<baseline['samples']:
    W=tuple(sorted([0,1]+rng.sample(range(2,39),10)))
    if W in seen:continue
    seen.add(W);hist=Counter();example={}
    def audit(cycles,edges,A):
        shape=tuple(sorted(map(len,cycles)));degree=max(map(int.bit_count,A));hist[str((shape,edges,degree))]+=1
        if shape==(12,) and (not example or degree<example['max_degree']):
            I=next(sevens(A,k=10),None);example.update(cycle=cycles[0],edges=edges,max_degree=degree,independent_ten=[i for i in range(39) if I is not None and I>>i&1])
    test(W,audit)
    if hist:rows.append(dict(weights=W,histogram=dict(hist),example=example));print(rows[-1],flush=True)
assert len(rows)==baseline['stats']['ten obstruction'];(D/'ramsey_39_twelve_connected_audit.json').write_text(json.dumps(rows,indent=2)+'\n')
