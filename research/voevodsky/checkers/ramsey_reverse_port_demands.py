from ramsey_relative_sign_joint_context import build,verdict,grow,graph,D,combinations,sha256,json,Counter

def families():
    current=[()];hits=[sum(1<<p for p in range(32) if p&m) for m in range(32)]
    for m in range(32):current += [a+(m,) for a in current if all((s&m)!=s for s in a)]
    def preds(a):
        h=2**32-1
        for m in a:h&=hits[m]
        return h
    d={preds(a):a for a in current};assert len(d)==len(current)==7581;return d

def run():
    F=families();z=json.loads((D.parent/'ramsey_port_repair_orbits.json').read_text());ss=grow(tuple(tuple(x-1 for x in s) for s in z['supports']),1);pairs=list(combinations(range(5),2));seen={};w=[];cases=[]
    for rep in z['wins']:
        col=sum(1<<pairs.index((i-1,j-1)) for i,j in rep);a=graph(9,ss,col);blue=lambda q:all(not(a[i]>>j&1) for i,j in combinations(q,2))
        for k in range(10):
            f={k-1,k}&set(range(9));V=set(range(14))-f;E=len(f)==2 and any(blue(q) for q in combinations([i for i in V if all(not(a[i]>>j&1) for j in f)],5));masks={sum(1<<(i-9) for i in q if i>=9) for q in combinations(sorted(V),6) if blue(q)};true=tuple(sorted(s for s in masks if not any(t!=s and t&s==t for t in masks)));gate=resp=0
            for m in range(32):
                p=[i for i in range(5) if m>>i&1];L=blue([9+i for i in p]) and all(not(a[9+i]>>j&1) for i in p for j in f);gate+=int(L)<<m;ok=verdict(build({k:tuple(i+1 for i in p)},ss,col));assert ok==(not E and L and all(m&t for t in true));resp+=int(ok)<<m
            fits=[u for h,u in F.items() if h&(0 if E else gate)==resp];assert true in fits;forced=sorted(set.intersection(*(set(u) for u in fits)));alt=min((u for u in fits if u!=true),key=lambda u:(len(u),u),default=None);row=dict(edits=rep,gap=k,gate=gate,veto=E,responses=resp,true=true,models=len(fits),forced=forced,alternative=alt);cases.append(row);key=(k,gate,E,resp);prev=seen.setdefault(key,row)
            if prev['true']!=true:w.append([prev,row])
    print('gap9',[(x['models'],x['true'],x['forced'],x['alternative']) for x in cases if x['gap']==9]);print('unique',sum(x['models']==1 for x in cases),'graph pairs',len(w),'no veto example',next((p for p in w if not p[0]['veto'] and p[0]['responses']),None));r=D.parent/'ramsey_reverse_port_demands.json';s=json.dumps(dict(protocol_sha=sha256((D.parent/'ramsey_reverse_port_demands_protocol.md').read_bytes()).hexdigest(),mask='bit i-1 denotes port i; probe truth table bit m denotes probe mask m',cases=cases,graph_witnesses=w),indent=2)+'\n';assert not r.exists() or r.read_text()==s;r.write_text(s)
if __name__=='__main__':run()
