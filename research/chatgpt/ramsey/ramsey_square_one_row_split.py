"""Second-level lookahead on surviving square seeds. Seek a concrete row/port-subset whose every remaining option is refuted by probed propagation; refresh probes on tentative choices for a no-retraction constructor."""
from ramsey_square_unit_builder import D,json,graph,inds,bits,gzip,Counter,combinations,build
from functools import lru_cache

def deeper(on,live,cs,ban,close,witness):
    @lru_cache(None)
    def probe(o,l):
        rounds=0
        while True:
            z=close(o,l)
            if z is None:return None,rounds
            o,l,p,_=z
            if p is None:return z,rounds
            yes=no=0
            for i in bits(l&~o):
                if close(o,l^(1<<i)) is None:yes|=1<<i
                if close(o|1<<i,l&~ban[i]) is None:no|=1<<i
            if not yes|no:return z,rounds
            for i in bits(yes):l&=~ban[i]
            o|=yes;l&=~no;rounds+=1
    rows=sorted((s for s in cs if not on&s),key=lambda s:((s&live).bit_count(),s));cert=None
    for s in rows:
        branches=[]
        for i in bits(s&live):
            z,depth=probe(on|1<<i,live&~ban[i]);branches.append([i,depth]);
            if z is not None:break
        else:cert=dict(clause=s,options=branches);break
    trail=[];refused=[];o,l=on,live
    while True:
        z,_=probe(o,l)
        if z is None:break
        o,l,p,_=z
        if p is None:return dict(certificate=cert,trail=trail,refused=refused,witness=witness(o))
        for i in bits(p):
            if probe(o|1<<i,l&~ban[i])[0] is not None:o|=1<<i;l&=~ban[i];trail.append(i);break
            refused.append(i)
        else:break
    return dict(certificate=cert,trail=trail,refused=refused,witness=None)

def run():
    old=json.loads((D/'ramsey_square_unit_builder.json').read_text());ls=gzip.decompress((D/'pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines();out=[];last=None
    for r in old:
        if r.get('probe')!='open':continue
        p,W=r['record'],r['seed'];
        if last!=p:H=graph(ls[p-1]);T=[t for t in inds(H) if t.bit_count()>=5];last=p
        ans=build(H,T,W,deeper)['residual'];cert=ans['certificate'];assert not(cert and r['ok']) and not(ans['witness'] and not r['ok'])
        if cert:
            a=next(bits(W));b=next(bits(H[a]&W));c,d=bits(W^(1<<a|1<<b));E=[1<<i|1<<j for i in (a,b) for j in (c,d)];F=(1<<len(H))-1;opts=[sum(1<<v for v,h in enumerate(H) if not (W>>v&1 or h&e)) for e in E];t,ps=next((t,ps) for t in T for ps in combinations(range(4),9-t.bit_count()) if not any(t&E[h] for h in ps) and sum((t&opts[h])<<(h*len(H)) for h in ps)==cert['clause']);cert.update(old_row=list(bits(t)),ports=[list(bits(E[h])) for h in ps],choices=[dict(vertex=i%len(H),port=list(bits(E[i//len(H)])),rounds=n) for i,n in cert['options']])
        out.append(dict(record=p,seed=W,ok=r['ok'],prior_built=bool(r['probe_greedy']),**ans))
    return out
if __name__=='__main__':
    z=run();print(Counter((r['ok'],r['prior_built'],bool(r['witness']),bool(r['certificate'])) for r in z));print([(r['record'],r['certificate']) for r in z if not r['ok']]);(D/'ramsey_square_one_row_split.json').write_text(json.dumps(z)+'\n')
