from itertools import combinations,product
from collections import Counter
from hashlib import sha256
import json
from ramsey_retention_slice import check,D
P=D.parent/'ramsey_midpoint_joint_insertion_protocol.md';R=D.parent/'ramsey_midpoint_joint_insertion.json'
def legal(k,A,B,red):
    g=[0]*(k+2)
    for i,j in [*((i,i+1) for i in range(k-1)),*((x-1,k) for x in A),*((x-1,k+1) for x in B),*([(k,k+1)] if red else [])]:g[i]|=1<<j;g[j]|=1<<i
    return check(g,(1<<len(g))-1,3,7)
def run():
    rows=[s for s in combinations(range(1,8),3) if min(s[1]-s[0],s[2]-s[1])>=2];out=[];tot=Counter()
    for A in rows:
        gaps=[list(range(a+1,b)) for a,b in zip((0,*A),(*A,8))];opts=[g for i,g in enumerate(gaps) if len(g)>int(i in (1,2))];
        if len(opts)!=2:continue
        entry=dict(A=A,gaps=opts,cases=[])
        for B,red in product(rows,[False,True]):
            if not legal(7,A,B,red):continue
            ways=[];details=[]
            for gap in opts:
                ok=[];reason=[]
                for x in gap:
                    if x in B:reason.append('new site red to B');continue
                    shrink=lambda s:tuple(t-(t>x) for t in s);a,b=shrink(A),shrink(B);valid=legal(6,a,b,red);reason.append('legal' if valid else 'illegal parent');
                    if valid:ok.append(x)
                ways.append(ok);details.append(reason)
            pattern=''.join('1' if w else '0' for w in ways);tot[('red' if red else 'blue')+'_'+pattern]+=1;entry['cases'].append(dict(B=B,ABred=red,ways=ways,reasons=details))
        out.append(entry)
    assert len(out)==6;print(tot);print([(e['A'],sum(bool(c['ways'][0])!=bool(c['ways'][1]) for c in e['cases'])) for e in out]);print(next((e['A'],e['gaps'],c) for e in out for c in e['cases'] if c['ABred'] and bool(c['ways'][0])!=bool(c['ways'][1])));data=dict(protocol_sha=sha256(P.read_bytes()).hexdigest(),counts=tot,cases=out);text=json.dumps(data,indent=2)+'\n';assert not R.exists() or R.read_text()==text;R.write_text(text)
if __name__=='__main__':run()
