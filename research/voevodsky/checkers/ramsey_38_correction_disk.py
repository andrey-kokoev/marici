"""Can the correction triangles around one hub form a triangulated disk? Its link must be a simple alternating cycle. Test all matchings saturating Z and all possible second matchings on the SAME sites whose union is a single cycle. A disk is counted twice (two alternating matchings), not once per growth order."""
from pathlib import Path
from itertools import permutations
import json
D=Path(__file__).resolve().parents[1]/'results';rows=json.loads((D/'ramsey_38_correction_continuation.json').read_text());out=[]
for row in rows:
    Z=row['Z'];W=row['W'];E={tuple(f['move']) for f in row['first']};orders=[(0,)+p for p in permutations(range(1,len(Z)))];full=closed=ways=0;example=None;uses=set()
    for choices in permutations(W,len(Z)):
        if not all((z,w) in E for z,w in zip(Z,choices)):continue
        full+=1;completions=0
        for order in orders:
            if not all((Z[order[(j+1)%len(Z)]],choices[i]) in E for j,i in enumerate(order)):continue
            completions+=1
            if example is None:example=[v for i in order for v in (Z[i],choices[i])]
        if completions:closed+=1;uses.update(zip(Z,choices))
        ways+=completions
    assert ways%2==0
    out.append(dict(poles=row['poles'],ring=row['ring'],full_matchings=full,extendible_on_same_sites=closed,disks=ways//2,missing_first_moves=sorted(E-uses),example_ring=example))
print(out[0]);print('disk range',min(x['disks'] for x in out),max(x['disks'] for x in out),'rings with dead full matching',sum(x['extendible_on_same_sites']<x['full_matchings'] for x in out),'rings with unsupported first move',sum(bool(x['missing_first_moves']) for x in out));(D/'ramsey_38_correction_disk.json').write_text(json.dumps(out,indent=2)+'\n')
