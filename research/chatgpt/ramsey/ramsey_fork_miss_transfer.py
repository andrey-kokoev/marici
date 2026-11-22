"""Transfer the earlier exact 8/7/6 miss census to the batch by certified edge-marked graph isomorphisms. Count how many ports actually reuse the two newly compatible endpoints. Labels are zero-based."""
from collections import Counter
from ramsey_final_miss_levels import levels
from verify_ramsey_pure_forks import grow,D,json

def iso(G,H,pins):
    n=len(G);N=lambda A:[[i for i in range(n) if x>>i&1] for x in A];a,b=N(G),N(H)
    def rec(c,d):
        while True:
            old=len(set(c));s=[(v[i],tuple(sorted(v[j] for j in nb[i]))) for v,nb in ((c,a),(d,b)) for i in range(n)];ids={x:i for i,x in enumerate(sorted(set(s)))};c,d=[ids[x] for x in s[:n]],[ids[x] for x in s[n:]]
            if Counter(c)!=Counter(d):return
            if len(set(c))==old:break
        if old==n:
            p=[d.index(t) for t in c];assert all({p[j] for j in a[i]}==set(b[p[i]]) for i in range(n));return p
        _,t=min((k,t) for t,k in Counter(c).items() if k>1);i=c.index(t)
        for j in range(n):
            if d[j]==t:
                u,v=c[:],d[:];u[i]=v[j]=old;p=rec(u,v)
                if p:return p
    c=[0]*n;d=c[:]
    for k,(x,y) in enumerate(pins,1):c[x]=d[y]=k
    return rec(c,d)

def run():
    data=json.loads((D/'ramsey_pure_port_fork.json').read_text());audit=json.loads((D/'ramsey_fork_audit_uniform.json').read_text());H=data['stem_graphs'][-1];S=data['to35'];cert=[];summary={}
    for r in audit:
        skip=r['skip'];i,v=r['thin'];U=S[:skip]+S[skip+1:];kind='intact' if i is None else 'thin';pins=[33];
        if i is not None:U[i]^=1<<v;pins.extend([26+i,v])
        G=grow(H,U)
        matched=False
        for key,(A,base,_,_) in summary.items():
            if not key.startswith(kind):continue
            p=iso(A,G,zip(base,pins))
            if p:matched=True;break
        if not matched:
            key=f'{kind}_{skip}';hist=Counter();pair=sum(1<<x for x in pins[1:]);count=levels(G,lambda supports:hist.update([sum((s&pair)==pair for s in supports)]));summary[key]=(G,pins,count['counts'],dict(hist));p=list(range(len(G)))
        cert.append(dict(skip=skip,kind=key,map=p))
    return dict(census={k:dict(counts=s[2],reuse=s[3]) for k,s in summary.items()},isomorphisms=cert)
if __name__=='__main__':
    out=run();print(out['census']);(D/'ramsey_fork_miss_transfer.json').write_text(json.dumps(out)+'\n')
