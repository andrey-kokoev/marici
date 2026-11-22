"""Compute exact port replacement distance with multiset overlap; for any depth >2 case additionally search all pairs of replacement maximal supports independently with the two retained ports fixed."""
from itertools import combinations,combinations_with_replacement
from collections import Counter
from ramsey_final_miss_levels import levels,bits,D,json
from ramsey_fork_audit_uniform import inds,grow,verify

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);good=[];bad=[]
    def visit(s,tag,_):
        if tag=='valid':good.append(tuple(sorted(s)))
        if tag=='fails_four':bad.append(tuple(sorted(s)))
    levels(H,on_classified=visit);indexes=[{} for _ in range(4)]
    for g in good:
        for n in range(4):
            for t in combinations(g,n):indexes[n].setdefault(t,g)
    rows=[];witness=None
    for s in bad:
        n,t=next((n,t) for n in (3,2,1,0) for t in combinations(s,n) if t in indexes[n]);g=indexes[n][t];repairable=[i for i in range(4) if s[:i]+s[i+1:] in indexes[3]];edge=p['alternate'];joint=1<<edge['removed_incidence']|1<<(len(p['stem_graphs'][-1])+edge['thinned_port_index_among_retained']);j,=[i for i,v in enumerate(s) if v&joint==joint];assert j in repairable;kept=s[:j]+s[j+1:];g=indexes[3][kept];verify(grow(H,g),10);rows.append(dict(failed=s,kept=kept,valid=g,repairable_slots=repairable,reused_slot=j))
        if n<2 and witness is None:witness=s
    checks=[]
    if witness:
        I=inds(H);M=[s for s in I if all(s>>v&1 or s&r for v,r in enumerate(H))];F=(1<<len(M))-1;hit=[sum(1<<j for j,s in enumerate(M) if s>>v&1) for v in range(34)];ms={}
        for t in I:
            if t.bit_count() in (6,7,8):
                h=0
                for v in bits(t):h|=hit[v]
                ms[t]=F^h
        for a,b in combinations(witness,2):
            allowed=F;one=[]
            for t,m in ms.items():
                spare=9-t.bit_count()-int(not a&t)-int(not b&t)
                if spare==0:allowed &= ~m
                elif spare==1:one.append(m)
                else:assert spare>=2
            feasible=0
            for j in bits(allowed):
                partners=allowed
                for m in one:
                    if m>>j&1:partners &= ~m
                feasible+=partners.bit_count()
            assert feasible==0;checks.append(dict(pair=[a,b],eligible=allowed.bit_count(),completions=feasible))
    assert len(bad)==404 and len(good)==1699;return dict(hist=dict(Counter(4-len(r['kept']) for r in rows)),direct_checks=checks,repairs=rows)
if __name__=='__main__':
    out=run();print(out['hist'],out['direct_checks']);(D/'ramsey_two_port_repair_depth.json').write_text(json.dumps(out)+'\n')
