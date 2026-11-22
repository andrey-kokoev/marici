"""Forbid each vertex with NO seed assumptions; compare empty-row blocker closure with intersection of ALL inclusion-minimal legal fourth supports."""
from functools import reduce
from operator import and_
from collections import Counter
from ramsey_fork_audit_uniform import D,json,inds,grow
from ramsey_final_miss_levels import bits

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);n=len(H);F=(1<<n)-1;I=[t for t in inds(H) if 6<=t.bit_count()<=8];src=json.loads((D/'ramsey_compulsory_kernel_test.json').read_text());out=[];hist=Counter();witness=None
    for r in src['triples']:
        mins=r['minima'];q=r['triple'];
        if not mins:continue
        rows=[t for t in I if t.bit_count()+sum(not s&t for s in q)==9];cols=[sum(1<<j for j,t in enumerate(rows) if t>>x&1) for x in range(n)];allrows=(1<<len(rows))-1;exact=reduce(and_,mins);pred=0;memo={}
        def missed(mask):
            if mask not in memo:
                hit=0
                for i in bits(mask):
                    hit|=cols[i]
                    if hit==allrows:break
                memo[mask]=hit!=allrows
            return memo[mask]
        for v in range(n):
            live=F^(1<<v);depth=0
            while not missed(live):
                ban=sum(1<<x for x in bits(live) if missed(live&~H[x]));
                if not ban:break
                live^=ban;depth+=1
            if missed(live):pred|=1<<v
            elif exact>>v&1 and witness is None:witness=dict(fixed=q,minima=mins,vertex=v,survivors=list(bits(live)),depth=depth,minimum_options=min((t&live).bit_count() for t in rows))
        assert pred&~exact==0;hist[len(mins)>1,pred==exact]+=1;seeded=pred
        if pred!=exact:
            allowed=F
            for u in bits(pred):allowed&=~H[u]
            for v in bits(allowed&~pred):
                live=allowed^(1<<v)
                while not missed(live):
                    ban=sum(1<<x for x in bits(live) if missed(live&~H[x]));
                    if not ban:break
                    live^=ban
                if missed(live):seeded|=1<<v
        assert not seeded&~exact;out.append(dict(fixed=q,minima=len(mins),expected=list(bits(exact)),detected=list(bits(pred)),second_pass=list(bits(seeded))))
    return dict(hist={str(k):v for k,v in hist.items()},witness=witness,rows=out)
if __name__=='__main__':
    out=run();print(out['hist'],out['witness']);(D/'ramsey_blocker_backbone_audit.json').write_text(json.dumps(out)+'\n')
