"""Table-first 3→4 support prediction; the column rule is reused unchanged, blind to the tested row."""
from ramsey38_excel_swap_join import prev,gzip,json,graph,Counter,combinations,sys,Fraction
from ramsey38_blind_column_frame import frame
P=prev.out/'ramsey38_tabulated_join_protocol.json';R=prev.out/'ramsey38_tabulated_join_transfer.json'
protocol=dict(start=310705,records=128,selection='First degree-seven root of each consecutive record. Mask each outside row in turn. Do not select on size, legal completion or overlap.',table='Enumerate the 20 width-eight separated-three-red words BEFORE graph lookup. For every pair differing by one adjacent RB/BR exchange take the Boolean OR of the words. Keep all distinct four-position outputs. This is a proposed generator, not the historical lossless display fold.',mapping='Root at position 1, seven columns in ascending stable refinement colors from the frozen blind-column-frame checker, with exactly one hidden row. Abstain for unresolved ties. Do not optimize orientation or permutation.',filter='Drop generated supports involving the root, already-visible supports, and labels forbidden by red triangles. No visible triple required.',control='Uniform subset of ALL novel triangle-safe fours at the same per-row guess count. Report all vs strict choices, expected exact hits and per-root outcomes. Not a timed solver benchmark.')

def table():
    triples=[set(c) for c in combinations(range(1,9),3) if min(c[1]-c[0],c[2]-c[1])>=2];assert len(triples)==20
    return sorted({tuple(sorted(a|b)) for a,b in combinations(triples,2) if len(a^b)==2 and max(a^b)-min(a^b)==1})

def run():
    pat=table();assert json.loads(P.read_text())==dict(protocol,patterns=[list(p) for p in pat]);usable=[s for s in pat if 1 not in s];out=[];tot=Counter();expected=Fraction();example=None
    with gzip.open(prev.catalogue,'rt') as f:
        for i,w in enumerate(f,1):
            if i<protocol['start']:continue
            if i>=protocol['start']+protocol['records']:break
            g=graph(w.strip());u=next((v for v in sorted(g) if len(g[v])==7),None);c=Counter();null=Fraction()
            if u is not None:
                L=g[u];O=set(g)-L-{u}
                for v in sorted(O):
                    c['masked']+=1;blocks=frame(g,u,L,{v});truth=frozenset(g[v]&L);c['true_fours']+=len(truth)==4
                    if any(len(b)!=1 for b in blocks):c['ties']+=1;continue
                    order=[u]+[b[0] for b in blocks];vis={j:frozenset(g[j]&L) for j in O-{v}};safe=L-set().union(*(vis[j] for j in g[v]&O));base=set(map(frozenset,combinations(safe,4)))-set(vis.values());guesses=base&{frozenset(order[j-1] for j in s) for s in usable};hit=truth in guesses
                    c['recoverable']+=truth in base;c['issued']+=bool(guesses);c['guesses']+=len(guesses);c['exact']+=hit
                    c['strict_issued']+=bool(guesses and guesses<base);c['strict_exact']+=hit and guesses<base
                    if truth in base:null+=Fraction(len(guesses),len(base))
                    if hit and example is None:example=dict(record=i,root=u,row=v,columns=order,support=sorted(truth),available=len(base),guesses=len(guesses))
            out.append(dict(record=i,root=u,counts=dict(c),expected=float(null)));tot.update(c);expected+=null
    assert len(out)==128;print('table',len(pat),len(usable),'counts',tot,'null',float(expected));prev.save(R,dict(protocol_sha=prev.sha(P.read_bytes()),table_patterns=len(pat),usable=len(usable),counts=dict(tot),expected=float(expected),example=example,per_record=out))
if __name__=='__main__':{'freeze':lambda:prev.save(P,dict(protocol,patterns=table())),'test':run}[sys.argv[1]]()
