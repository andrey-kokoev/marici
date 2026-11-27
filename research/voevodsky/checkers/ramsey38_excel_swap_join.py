"""Does taking both red alternatives of a table swap predict a four-red graph row?"""
from ramsey38_blind_swap_row import prev,gzip,json,graph,Counter,combinations,sys,Fraction
P=prev.out/'ramsey38_excel_swap_join_protocol.json';R=prev.out/'ramsey38_excel_swap_join.json'
protocol=dict(start=310577,records=128,selection='Consecutive records; least degree-seven root; mask every outside row with no support-size conditioning.',operation='Boolean union, an extra modeling hypothesis, NOT the lossless Excel fold. Observed: two distinct visible triples with the same two fixed reds and alternatives x/y predict their four-label union. Transported: visible triple V+x, witnessed x/y swap at a disjoint two-label tail U, predict V+x+y. Test separately. No fitted column order; tests swap joins, not adjacency of specific positions.',control='Reject any predicted support making a red triangle with a known neighbor of the masked row. Predict only novel supports. Control pool: all novel triangle-safe fours containing a visible triple (add any red). Uniform equal proposal budget per masked row. Score exact hidden row plus how often candidate pool is singleton/exhausted. Compare simple maximal triangle-safe mask on each issued row.')

def proposals(L,rows,neighbors):
    visible=set(rows.values());forbid=set().union(*(rows[j] for j in neighbors));safe=L-forbid;triples={s for s in visible if len(s)==3};base={s|{y} for s in triples if s<=safe for y in safe-s}-visible
    direct=set();trans=set()
    for a,b in combinations(triples,2):
        u=a&b
        if len(u)!=2:continue
        direct.add(a|b);xy=a^b
        for t in triples:
            if len(t&xy)==1 and not (t-xy)&u:trans.add(t|xy)
    return base,direct&base,trans&base,safe

def run():
    assert json.loads(P.read_text())==protocol
    # One seen edge; a transported edge whose other corner is not supplied.
    L=frozenset(range(7));vis={0:frozenset((0,1,2)),1:frozenset((0,1,3)),2:frozenset((2,4,5))};_,d,t,_=proposals(L,vis,[]);assert d=={frozenset((0,1,2,3))} and t=={frozenset((2,3,4,5))}
    counts=Counter();arms={m:Counter() for m in ['observed','transported']};null={m:Fraction() for m in arms};examples={}
    with gzip.open(prev.catalogue,'rt') as f:
        for i,w in enumerate(f,1):
            if i<protocol['start']:continue
            if i>=protocol['start']+protocol['records']:break
            g=graph(w.strip());counts['records']+=1;u=next((v for v in sorted(g) if len(g[v])==7),None)
            if not u:continue
            counts['roots']+=1;L=g[u];O=set(g)-L-{u}
            for v in sorted(O):
                vis={j:frozenset(g[j]&L) for j in O-{v}};base,d,t,safe=proposals(L,vis,g[v]&O);truth=frozenset(g[v]&L);counts['masked']+=1;counts['true_fours']+=len(truth)==4;counts['recoverable']+=truth in base
                for m,qs in [('observed',d),('transported',t)]:
                    if not qs:continue
                    c=arms[m];c['issued']+=1;c['guesses']+=len(qs);c['hit']+=truth in qs;c['strict_choice']+=qs!=base;c['strict_hit']+=qs!=base and truth in qs;c['safe_mask_hits_on_issued']+=safe==truth
                    if truth in base:null[m]+=Fraction(len(qs),len(base))
                    if truth in qs:examples.setdefault(m,dict(record=i,root=u,row=v,support=sorted(truth),alternatives=[sorted(s) for s in sorted(qs,key=sorted)],base_size=len(base)))
    print(counts,arms,{m:float(n) for m,n in null.items()});prev.save(R,dict(source_sha=prev.sha(P.read_bytes()),counts=dict(counts),arms={m:dict(c,control_expected=float(null[m])) for m,c in arms.items()},examples=examples))
if __name__=='__main__':{'freeze':lambda:prev.save(P,protocol),'test':run}[sys.argv[1]]()
