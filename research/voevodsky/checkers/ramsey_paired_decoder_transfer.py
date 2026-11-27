from ramsey_relative_sign_joint_context import graph,grow,build,verdict,D,combinations,sha256,json,Counter
from itertools import islice
P=D.parent/'ramsey_paired_decoder_candidates.json';R=D.parent/'ramsey_paired_decoder_transfer.json';protocol=D.parent/'ramsey_paired_decoder_transfer_protocol.md';ports=list(combinations(range(5),2))
def terms(S,k):
    f={k-1,k}&set(range(9));res=[]
    for p in range(32):
        pool=set(range(9))-f
        for i in range(5):
            if p>>i&1:pool-=set(S[i])
        independent=[]
        for i in sorted(pool):
            if i-1 not in independent:independent.append(i)
        if len(independent)+p.bit_count()>=6:res.append(p)
    return [p for p in res if not any(t!=p and t&p==t for t in res)]
def family():
    rows=[s for s in combinations(range(8),3) if min(s[1]-s[0],s[2]-s[1])>=2]
    for ss in combinations(rows,5):
        es=[n for n,(i,j) in enumerate(ports) if not set(ss[i])&set(ss[j])];
        if len(es) in (3,4):yield ss,es

def freeze():
    out=[]
    for ss,es in islice(family(),64):
        S=grow(ss,1);T=[terms(S,k) for k in range(10)];pred=[]
        for k in range(1,9):
            for p in T[k]:
                bits=[e for e in es if all(p>>i&1 for i in ports[e])];
                if len(bits)!=1:continue
                for end,v in [(0,0),(9,8)]:
                    if all(v not in S[i] for i in range(5) if p>>i&1) and all(p&q for q in T[end]):pred.append([k,p,bits[0],end])
        out.append(dict(rows=ss,eligible=es,pred=pred))
    return dict(protocol_sha=sha256(protocol.read_bytes()).hexdigest(),families=out)
def save(dest,data):
    s=json.dumps(data,indent=2)+'\n';assert not dest.exists() or dest.read_text()==s;dest.write_text(s)
def test():
    data=json.loads(P.read_text());assert data['protocol_sha']==sha256(protocol.read_bytes()).hexdigest();stats=Counter();example=None
    for f in data['families']:
        S=grow(f['rows'],1);es=f['eligible'];pred=f['pred'];stats['families']+=1;stats['with_candidates']+=bool(pred);stats['candidates']+=len(pred);states=[set() for _ in pred];legal=0
        for mask in range(1<<len(es)):
            c=sum(1<<e for i,e in enumerate(es) if mask>>i&1);a=graph(9,S,c)
            if not verdict(a):continue
            legal+=1;cache={}
            for n,(k,p,e,end) in enumerate(pred):
                if k not in cache:
                    raw={sum(1<<(j-9) for j in q if j>=9) for q in combinations(sorted(set(range(14))-{k-1,k}),6) if all(not a[i]>>j&1 for i,j in combinations(q,2))};cache[k]={m for m in raw if not any(t!=m and t&m==t for t in raw)}
                ok=verdict(build({end:tuple(i+1 for i in range(5) if p>>i&1)},S,c));assert ok==(p in cache[k])==(not(c>>e&1));states[n].add(ok);stats['checked_predictions']+=1
        stats['legal_parents']+=legal;stats['with_legal_parent']+=bool(legal);active=[i for i,s in enumerate(states) if len(s)==2];stats['two_color_candidates']+=len(active);stats['two_color_families']+=bool(active)
        if active and example is None:example=dict(family=f,prediction=pred[active[0]])
    print(stats,example);save(R,dict(candidate_sha=sha256(P.read_bytes()).hexdigest(),stats=stats,example=example))
if __name__=='__main__':
    import sys
    if sys.argv[1]=='freeze':save(P,freeze())
    else:test()
