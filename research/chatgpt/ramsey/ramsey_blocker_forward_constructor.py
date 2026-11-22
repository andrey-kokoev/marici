"""Construct without repair oracle. Audit ALL independent commitments by monotonicity: enumerate minimal incompatible commitments as independent minimal transversals of the neighbour masks of known minimal repairs. A missed minimal nonface disproves completeness."""
from functools import lru_cache
from collections import Counter
from ramsey_fork_audit_uniform import grow,inds,verify,D,json
from ramsey_final_miss_levels import bits

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);F=(1<<34)-1;I=inds(H);T=[s for s in I if 6<=s.bit_count()<=8];N={0:0}
    for s in sorted(I):
        if s:N[s]=N[s&(s-1)]|H[(s&-s).bit_length()-1]
    out=[]
    for r in json.loads((D/'ramsey_compulsory_kernel_test.json').read_text())['triples']:
        mins=r['minima'];q=r['triple'];
        if not mins:continue
        rows=[s for s in T if s.bit_count()+sum(not s&a for a in q)==9];cols=[sum(1<<j for j,t in enumerate(rows) if t>>v&1) for v in range(34)];full=(1<<len(rows))-1
        @lru_cache(None)
        def missed(live):
            hits=0
            for v in bits(live):
                hits|=cols[v]
                if hits==full:return False
            return True
        @lru_cache(None)
        def close(live):
            if missed(live):return 0
            b=sum(1<<x for x in bits(live) if missed(live&~H[x]));return close(live^b) if b else live
        s=0;probes=0;trace=[]
        while True:
            live=close(F^N[s]);un=[t for t in rows if not t&s];
            if not un:break
            t=min(un,key=lambda t:((t&live).bit_count(),t));choice=None
            for x in bits(t&live):
                probes+=1
                if close(live&~H[x]):choice=x;break
            if choice is None:break
            trace.append(choice);s|=1<<choice
        success=not un
        if success:verify(grow(H,[*q,s]),10)
        bans=[N[k] for k in mins];bad={s for s in I if all(s&b for b in bans)};mf=[s for s in bad if all(s^(1<<v) not in bad for v in bits(s))];escape=[s for s in mf if close(F^N[s])];out.append(dict(fixed=q,trace=trace,success=success,probes=probes,minimal_impossible=len(mf),escape=escape));close.cache_clear();missed.cache_clear()
    return out
if __name__=='__main__':
    out=run();print(Counter((r['success'],bool(r['escape'])) for r in out),sum(r['minimal_impossible'] for r in out),sum(len(r['escape']) for r in out));print(next((r for r in out if r['escape']),None));(D/'ramsey_blocker_forward_constructor.json').write_text(json.dumps(out)+'\n')
