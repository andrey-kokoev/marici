"""Unrestricted single-vertex extension of each 39-vertex completion of the frozen eleven-branch fold. Exact labeled supports, zero-based; emit small replayable failure covers."""
from ramsey_request_scale import *
from ramsey_fork_audit_uniform import verify
from functools import reduce
from operator import or_
def main():
 cert=json.loads((D/'ramsey_shared_request_certificate.json').read_text());p=json.loads((K/'ramsey_pure_port_fork.json').read_text());A=grow(p['stem_graphs'][-1],p['alternate']['to34']);q=json.loads((K/'ramsey_compulsory_kernel_test.json').read_text())['triples'];out=[]
 for i in cert['group']['cases']:
    G=grow(A,[*q[i]['triple'],cert['unique']]);assert len(G)==39;verify(G,10);I=inds(G);F=(1<<39)-1;maximal=[]
    for m in I:
        free=F^m;s=m
        while free and s:b=s&-s;s-=b;free&=~G[b.bit_length()-1]
        if not free:maximal.append(m)
    nine=[s for s in I if s.bit_count()==9];live=maximal;cover=[]
    for t in nine:
        if any(not s&t for s in live):cover.append(t);live=[s for s in live if s&t];
        if not live:break
    sols=[s for s in I if any(s&m==s for m in live) and all(s&t for t in nine)] if live else [];assert bool(sols)==bool(live)
    if not live:
        # Remove redundant nines; verify coverage on all maximal independent red supports.
        for t in cover.copy():
            trial=[x for x in cover if x!=t];
            if not any(all(s&x for x in trial) for s in maximal):cover=trial
        assert all(any(not(s&t) for t in cover) for s in maximal)
    out.append(dict(case=i,graph=G,independent=len(I),maximal=len(maximal),nines=len(nine),supports=sols,obstruction=cover if not live else None));print(i,len(I),len(maximal),len(nine),len(sols),len(cover),flush=True)
 (D/'ramsey_eleven_next_vertex.json').write_text(json.dumps(out))
if __name__=='__main__':main()
