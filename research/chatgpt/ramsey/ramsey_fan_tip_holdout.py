"""Hold out the other active partitions. For each unused tetrahedral fan, predict its common owner from tip exchange without consulting that owner; test all ordered thread states and report stabilizer orbits of candidates."""
from ramsey_fan_tip_exchange import prediction,P,T,X,D,json
from ramsey_iterated_thread_operator import final,move,R,step

def test():
    m,=final;a,b=m,move(m,R);out=[]
    for phase in range(4):
        rows=[]
        for j in sorted({v for _,v in a^b}):
            d,={P.index(e) for e in T[j-15]}-{x for x,k in a|b if k==j};s,e=[set(X[i]) for i in P[d]];owner=dict(a)[d];assert (d,owner) in b
            # Compute the antipode using the active rows only, then exclude the shortcut middle.
            v=j;inv={k:x for x,k in a};f=dict(b)
            for _ in range(2):v=f[inv[v]]
            i=inv[v];mid,=[k for k,t in enumerate(T,15) if P[d] in t and P[i] in t];third,={k for k,t in enumerate(T,15) if P[d] in t}-{j,mid};assert third==owner
            if not s&e:rows.append(dict(partition=j,duad=d,opposite=True,owner=owner,antipode=i,middle=mid));continue
            r=prediction(j,d);rows.append(r|dict(owner=owner,antipode=i,middle=mid,transports=r['predicted']==owner,owner_fixed=owner in r['fixed'],source_fixed=j in r['fixed']))
        out.append(rows);a,b=step(a,b)
    assert out[0]==out[2] and out[1]==out[3];return out
if __name__=='__main__':
    out=test();print([[ (r.get('entry',r.get('partition')),r['owner'],r.get('predicted'),r.get('source_fixed')) for r in rows] for rows in out[:2]]);(D/'ramsey_fan_tip_holdout.json').write_text(json.dumps(out)+'\n')
