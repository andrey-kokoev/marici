"""On every new, individually viable local holdout, replace exactly one exclusive support."""
from ramsey310_s3_local_transfer import D,F,E,sets,json,Counter,independent
import ramsey310_s3_local_transfer as test
base=json.loads((D/'ramsey310_matching_degree3_types.json').read_text())[0];cases=json.loads((D/'ramsey310_s3_local_transfer_r10.json').read_text())['uncut'];results=[]
for case in cases:
    A=base.copy()
    for i,j,x,y in case['path']:
        A[i]^=1<<j;A[j]^=1<<i;A[x]|=1<<y;A[y]|=1<<x
    S=list(sets(A,F,7));hist=Counter();hits=[]
    for i in range(6):
        for s in S:
            if s in E or s&E[(i+3)%6]:continue
            e=list(E);e[i]=s
            if any((a&b).bit_count()>5 for side in [e[:3],e[3:]] for j,a in enumerate(side) for b in side[:j]):continue
            test.E=e;tag,cert=test.examine(A);hist[tag]+=1
            if cert:hits.append(dict(index=i,row=s,**cert))
    results.append(dict(path=case['path'],counts=hist,cuts=hits));test.E=E
print(json.dumps(results))
