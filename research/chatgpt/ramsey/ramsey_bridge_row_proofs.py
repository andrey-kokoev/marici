"""Row-labelled proofs of compulsory private incidences. Use only seed compatibility, red-edge exclusions and old-row obligations. Earliest sufficient size tier, fresh-solver failed-literal unit propagation, then deletion-minimal UNSAT cores of row labels (not minimum-cardinality)."""
from ramsey_invisible_region_repairs import D,json,graph,inds,bits,prove,gzip,Counter,CardEnc,Solver,grow,verify,combinations

def audit(H,T,r):
    W=r['seed'];n=len(H);a=next(bits(W));b=next(bits(H[a]&W));c,d=bits(W^(1<<a|1<<b));ends=[1<<i|1<<j for i in (a,b) for j in (c,d)];dom={u:[h for h,e in enumerate(ends) if not H[u]&e] for u in range(n) if not W>>u&1};B=[[-(4*u+h+1),-(4*v+h+1)] for u,hs in dom.items() for v in bits(H[u]) if v>u and v in dom for h in set(hs)&set(dom[v])];proofs=[];unresolved=[(u,h) for u in r['always'] for h in dom[u]]
    for level in (7,6,5):
        if not unresolved:break
        ts=[];C=B.copy();plain=B.copy()
        for t in T:
            if t.bit_count()<level:continue
            clauses=[[4*u+h+1 for u in bits(t) if u in dom for h in ps if h in dom[u]] for ps in combinations(range(4),9-t.bit_count()) if not any(ends[h]&t for h in ps)]
            if not clauses:continue
            ts.append(t);g=4*n+len(ts);C.extend([[-g]+c for c in clauses]);plain.extend(clauses)
        labels=list(range(4*n+1,4*n+1+len(ts)));todo=[]
        with Solver(name='g4',bootstrap_with=C) as sat,Solver(name='g4',bootstrap_with=plain) as prop:
            # propagate with assumption, no prior solve or learned clauses in prop
            for u,h in unresolved:
                lit=4*u+h+1
                if sat.solve(assumptions=[-lit]+labels):todo.append((u,h));continue
                direct=[]
                for t in ts:
                    if not t>>u&1 or t&ends[h] or any(v!=u and h in dom.get(v,[]) for v in bits(t)):continue
                    colors={j for j,e in enumerate(ends) if e&t or any(j in dom.get(v,[]) for v in bits(t))};
                    if len(colors)==t.bit_count()-4:direct.append(t)
                local=not prop.propagate(assumptions=[-lit])[0];core=sorted(i for i in sat.get_core() if i>0)
                for g in list(core):
                    alt=[z for z in core if z!=g]
                    if not sat.solve(assumptions=[-lit]+alt):core=alt
                rows=[ts[g-4*n-1] for g in core];assert rows and not sat.solve(assumptions=[-lit]+core);proofs.append(dict(vertex=u,port=h,level=level,unit_refutes=local,direct=direct,rows=rows))
        unresolved=todo
    assert not unresolved;return proofs

def run():
    src=json.loads((D/'ramsey_private_bridge_minima.json').read_text());ls=gzip.decompress((D/'pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines();out=[];last=None
    for r in src:
        p=r['record'];
        if last!=p:H=graph(ls[p-1]);T=[s for s in inds(H) if s.bit_count()>=5];last=p
        out.append(dict(record=p,seed=r['seed'],proofs=audit(H,T,r)))
    return out
if __name__=='__main__':
    z=run();ps=[p for r in z for p in r['proofs']];print(Counter((p['level'],p['unit_refutes']) for p in ps));print(Counter(len(p['rows']) for p in ps));(D/'ramsey_bridge_row_proofs.json').write_text(json.dumps(z)+'\n')
