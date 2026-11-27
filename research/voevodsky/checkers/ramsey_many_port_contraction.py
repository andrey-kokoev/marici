from itertools import combinations,product
from collections import Counter
from hashlib import sha256
import json
from ramsey_retention_slice import D,check
P=D.parent/'ramsey_many_port_contraction_protocol.md';R=D.parent/'ramsey_many_port_contraction.json'
def legal(n,ss,col):
    g=[0]*(n+3);edges=[(i,i+1) for i in range(n-1)]+[(x-1,n+j) for j,s in enumerate(ss) for x in s]+[(n+i,n+j) for t,(i,j) in enumerate(combinations(range(3),2)) if col>>t&1]
    for i,j in edges:g[i]|=1<<j;g[j]|=1<<i
    return check(g,(1<<len(g))-1,3,7)
def run():
    U=range(1,8);opts=[s for s in combinations(U,3) if min(s[1]-s[0],s[2]-s[1])>=2];seen={};ex=None;t=Counter()
    for ss in product(opts,repeat=3):
        used=set.union(*map(set,ss))
        for col in range(8):
            if not legal(7,ss,col):continue
            t['legal_endpoints']+=1
            for x in U:
                if x in used:t['incidence_blocks']+=1;continue
                t['common_clear']+=1;flank=any(x-1 in s and x+1 in s for s in ss);old=[tuple(v-(v>x) for v in s) for s in ss];ok=legal(6,old,col);assert ok== (not flank);t['flank_blocks' if flank else 'can_contract']+=1
                key=(tuple(sorted(used)),col,x);opp=seen.get((key,not ok));seen.setdefault((key,ok),ss)
                if opp and ex is None:ex=dict(union=key[0],port_red_bits=col,site=x,works=ss if ok else opp,fails=opp if ok else ss)
    assert ex;out=dict(protocol_sha=sha256(P.read_bytes()).hexdigest(),counts=t,control=ex);print(out);text=json.dumps(out,indent=2)+'\n';assert not R.exists() or R.read_text()==text;R.write_text(text)
if __name__=='__main__':run()
