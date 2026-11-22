"""Implicit minimum hitting set: SAT master only sees separated triples; graph separator returns first surviving triangle (loops allow repeated supports). No table of surviving triples constructed. Oracle yields both minimum certificate and a matching lower-bound teaching set."""
from ramsey_global_five_basis import D,json,inds,decode,bits,minimum
from statistics import median
from time import perf_counter

def learn(H,A):
    I=inds(H);six=[t for t in I if t.bit_count()==6];T=[t for t in I if t.bit_count()==5 and not t&A];S=sorted(s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H)) and all((s|A)&t for t in six));miss=lambda s,ts:sum(1<<j for j,t in enumerate(ts) if not t&s);q=[miss(s,T) for s in S];p=[miss(s,six) for s in S];base=[sum(1<<j for j in range(i,len(S)) if not p[j]&u) for i,u in enumerate(p)];columns=[sum(1<<i for i,s in enumerate(S) if not s&t) for t in T];patterns=set();hist=[];start=perf_counter()
    while True:
        selected=sorted(minimum(patterns,T)['rows']) if patterns else [];adj=base.copy()
        for t in selected:
            mask=columns[T.index(t)]
            for i in bits(mask):adj[i]&=~mask
        triple=None
        for i,N in enumerate(adj):
            for j in bits(N):
                live=N&adj[j]
                if live:triple=(i,j,next(bits(live)));break
            if triple:break
        if triple is None:return dict(rows=selected,trace=hist,ms=1000*(perf_counter()-start))
        i,j,k=triple;h=(q[i]&q[j])|(q[i]&q[k])|(q[j]&q[k]);assert h not in patterns
        if not h:return dict(survivor=[S[i],S[j],S[k]],trace=hist)
        patterns.add(h);hist.append(dict(triple=[S[i],S[j],S[k]],trial=selected,violated=[T[i] for i in bits(h)]))

def disjoint_lower(ans):
    # To attain the cover size, disjoint violation lists must each meet exactly one different certificate row.
    rows=set(ans['rows']);groups={t:[] for t in rows}
    for j,event in enumerate(ans['trace']):
        d=set(event['violated']);hit=d&rows
        if len(hit)==1:groups[next(iter(hit))].append((j,d))
    def choose(left,used):
        if not left:return []
        options={t:[v for v in groups[t] if not used&v[1]] for t in left};t=min(left,key=lambda t:len(options[t]))
        for j,d in options[t]:
            rest=choose(left-{t},used|d)
            if rest is not None:return [j]+rest
    return choose(rows,set())

def run():
    cases=json.loads((D/'ramsey_global_five_basis.json').read_text());drops={r['parent']:r['deleted'] for r in json.loads((D/'ramsey_bare_core_rank.json').read_text())};lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in cases:
        p,A=r['parent'],r['first'];G=decode(lines[p-1]);vs=[i for i in range(22) if i!=drops[p]];H=[sum(1<<j for j,y in enumerate(vs) if G[x]>>y&1) for x in vs];ans=learn(H,A);ans['disjoint_trace_indices']=disjoint_lower(ans);assert len(ans['rows'])==len(r['root']['rows']);out.append(dict(parent=p,first=A,screen=r['trips'],**ans))
    return out
if __name__=='__main__':
    z=run();print(sum(len(r['trace']) for r in z),min(len(r['trace']) for r in z),median(len(r['trace']) for r in z),max(len(r['trace']) for r in z));print(sum(len(r['trace'])==len(r['rows']) for r in z));print(max(((len(r['trace']),r['parent'],r['first'],r['screen']) for r in z)));(D/'ramsey_lazy_root_basis.json').write_text(json.dumps(z)+'\n')
