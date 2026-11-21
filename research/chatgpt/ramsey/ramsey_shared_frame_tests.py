"""Twin overlap, single-switch neighbors and bad wirings at every shared-frame root."""
from itertools import combinations
from pathlib import Path
import json
from collections import Counter
from ramsey_regular_two_switch import iso, relation
from ramsey_mutual_repair_conjecture import apply, sevens, decode
D=Path(__file__).parent
records={r['record']:decode(r['graph6'].encode()) for r in json.loads((D/'ramsey_hall_center_conjecture.json').read_text())['regular']}
for row in json.loads((D/'ramsey_near_balanced_frames.json').read_text())['records']:
    for root in row['nearest']:
        if root['frame']!=13:continue
        A=records[row['source']];r=root['root'];V=[v for v in range(22) if v!=r and not A[r]>>v&1];x,y=next((v,w) for v,w in combinations(V,2) if A[r]&A[v]==A[r]&A[w]);common=[v for v in V if A[x]&A[y]&(1<<v)]
        E=[(v,w) for v,w in combinations(V,2) if A[v]>>w&1];stats=Counter();witness=None
        for e,f in combinations(E,2):
            a,b=e;c,d=f
            if len({a,b,c,d})!=4:continue
            for added in [((a,c),(b,d)),((a,d),(b,c))]:
                if any(A[i]>>j&1 for i,j in added):continue
                B=apply(A,(e,f),added)
                if any(B[i]&B[j] for i,j in added):continue
                bad=next(sevens(B),None);stats['valid' if bad is None else 'bad']+=1
                if bad is None:
                    for target in (187,188):
                        p=iso(B,records[target],relation(B),relation(records[target]))
                        if p: print('valid neighbor',row['source'],r,e,f,added,'->',target,'root',p[r])
                if bad and not witness:witness=(e,f,added,[v for v in range(22) if bad>>v&1])
        print(row['source'],r,'twins',x,y,'common',common,'moves',stats,'bad example',witness)
