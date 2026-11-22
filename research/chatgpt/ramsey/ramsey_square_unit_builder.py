"""Blind row propagation. Demand masks are positive CNF clauses over incidences; red adjacency supplies binary incompatibilities. Iterate simultaneous singleton forcing; compare one-literal lookahead, then deterministic greedy construction with no retractions."""
from ramsey_square_level_transfer import D,json,graph,inds,bits,gzip,Counter,grow,verify,combinations

def build(H,T,W,residual=None):
    a=next(bits(W));b=next(bits(H[a]&W));c,d=bits(W^(1<<a|1<<b));ends=[1<<i|1<<j for i in (a,b) for j in (c,d)];opts=[sum(1<<v for v,r in enumerate(H) if not r&e and not W>>v&1) for e in ends];n=len(H);F=sum(s<<(h*n) for h,s in enumerate(opts));ban=[H[i]<<(h*n) for h in range(4) for i in range(n)];rows=set()
    for t in T:
        for ps in combinations(range(4),9-t.bit_count()):
            if not any(t&ends[h] for h in ps):rows.add(sum((t&opts[h])<<(h*n) for h in ps))
    # Remove redundant supersets; index by a representative literal for cheap subsumption.
    buckets={};cs=[]
    for s in sorted(rows,key=lambda x:(x.bit_count(),x)):
        if any(any(t&s==t for t in buckets.get(i,())) for i in bits(s)):continue
        if not s:return dict(unit='dead',unit_forced=0,rounds=0)
        cs.append(s);buckets.setdefault((s&-s).bit_length()-1,[]).append(s)
    def close(on,live):
        depth=0
        while True:
            if on&~live:return None
            f=0;pick=None
            for s in cs:
                if on&s:continue
                m=s&live
                if not m:return None
                if m&(m-1)==0:f|=m
                if pick is None or m.bit_count()<pick.bit_count():pick=m
            if not f:return on,live,pick,depth
            for i in bits(f):live&=~ban[i]
            on|=f;depth+=1
    def witness(on):
        S=[e|((on>>(h*n))&((1<<n)-1)) for h,e in enumerate(ends)];verify(grow(H,S),9);return S
    base=close(0,F)
    if base is None:return dict(unit='dead',unit_forced=0,rounds=None)
    on,live,pick,depth=base;out=dict(unit='open' if pick else 'built',unit_forced=on,rounds=depth)
    def greedy(state):
        while state is not None:
            o,l,p,_=state
            if p is None:return witness(o)
            state=next((z for i in bits(p) if (z:=close(o|1<<i,l&~ban[i])) is not None),None)
    out['unit_greedy']=greedy(base);rounds=0
    while pick is not None:
        yes=no=0
        for i in bits(live&~on):
            if close(on,live^(1<<i)) is None:yes|=1<<i
            if close(on|1<<i,live&~ban[i]) is None:no|=1<<i
        if not yes|no:break
        for i in bits(yes):live&=~ban[i]
        state=close(on|yes,live&~no);rounds+=1
        if state is None:return dict(**out,probe='dead',probe_rounds=rounds)
        on,live,pick,_=state
    out.update(probe='open' if pick else 'built',probe_forced=on,probe_rounds=rounds,probe_greedy=greedy((on,live,pick,0)))
    if residual and pick:out['residual']=residual(on,live,cs,ban,close,witness)
    return out

def run():
    ref=json.loads((D/'ramsey_invisible_region_repairs.json').read_text());ls=gzip.decompress((D/'pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines();out=[];last=None
    for r in ref:
        p=r['record'];W=r['seed'];
        if p!=last:H=graph(ls[p-1]);T=[t for t in inds(H) if t.bit_count()>=5];last=p
        ans=build(H,T,W);ok=bool(r['full']);assert not ok or ans.get('probe',ans['unit'])!='dead';assert ok or not(ans.get('unit_greedy') or ans.get('probe_greedy'));out.append(dict(record=p,seed=W,ok=ok,**ans))
    return out
if __name__=='__main__':
    z=run();print(Counter((r['ok'],r['unit'],r.get('probe')) for r in z));print(sum(bool(r.get('unit_greedy')) for r in z),sum(bool(r.get('probe_greedy')) for r in z));(D/'ramsey_square_unit_builder.json').write_text(json.dumps(z)+'\n')
