"""Cover every maximal rejected support using original clauses shared by all 11 live branches."""
from ramsey_request_scale import *
def main():
 groups=json.loads((D/'ramsey_request_scale_partitions.json').read_text());group=max((g for g in groups if g['legal']),key=lambda g:len(g['cases']));q=json.loads((K/'ramsey_compulsory_kernel_test.json').read_text())['triples'];p=json.loads((K/'ramsey_pure_port_fork.json').read_text());A=grow(p['stem_graphs'][-1],p['alternate']['to34']);I=prepare(A);lib=[x for x in I if 6<=x.bit_count()<=8];lists=[{s for s in lib if s.bit_count()+sum(not s&a for a in q[i]['triple'])==9} for i in group['cases']];shared=sorted(set.intersection(*lists));full=(1<<len(I))-1;cols=[sum(1<<i for i,s in enumerate(I) if s>>v&1) for v in range(34)]
 def hit(s):
    h=0
    while s:b=s&-s;s^=b;h|=cols[b.bit_length()-1]
    return h
 def sig(rows):
    l=full
    for s in rows:l&=hit(s)
    return l
 live=sig(lists[0]);assert live.bit_count()==1 and all(sig(c)==live for c in lists);S=I[live.bit_length()-1];common=sig(shared);print('target',S,'common clauses',len(shared),'common survivors',common.bit_count());res=dict(group=group,unique=S,shared=len(shared),common_survivors=common.bit_count());
 if common!=live:
    def unpack(m):
        while m:b=m&-m;yield I[b.bit_length()-1];m^=b
    candidates=list(unpack(common));extras=list(unpack(common^live));target=(1<<len(extras))-1;private=[]
    for L in lists:
        dp={0:()}
        for r in sorted(L-set(shared)):
            mask=sum(1<<j for j,x in enumerate(extras) if not r&x)
            for m,seq in list(dp.items()):
                if mask|m not in dp or len(seq)+1<len(dp[mask|m]):dp[mask|m]=seq+(r,)
        assert sig(dp[target])&common==live;private.append(dp[target])
    # Direct full-domain greedy cover, then remove redundant clauses; produces an upper bound only.
    left=full^common;cover={r:full^hit(r) for r in shared};kernel=[]
    while left:
        r=max(shared,key=lambda r:(left&cover[r]).bit_count());kernel.append(r);left&=~cover[r]
    for r in reversed(kernel.copy()):
        if sig([x for x in kernel if x!=r])==common:kernel.remove(r)
    assert sig(kernel)==common and all(sig(kernel+list(seq))==live for seq in private)
    res.update(common_kernel=kernel,surviving_masks=candidates,branch_minimum_additions=private);print('kernel',len(kernel),'minimum additions',list(map(len,private)));print('surviving',[[v for v in range(34) if x>>v&1] for x in candidates]);
 if common==live:
    # Monotonicity: maximal rejected independent sets suffice, including proper subsets of S that have no rejected extension.
    rejected=set(I)-{S};B=[s for s in rejected if not any(s|1<<v in rejected for v in range(34) if not s>>v&1)];domain=(1<<len(B))-1;cover={r:sum(1<<i for i,s in enumerate(B) if not s&r) for r in shared};left=domain;chosen=[]
    while left:
        r=max(shared,key=lambda r:(cover[r]&left).bit_count());chosen.append(r);left&=~cover[r]
    for r in reversed(chosen.copy()):
        acc=0
        for x in chosen:
            if x!=r:acc|=cover[x]
        if acc==domain:chosen.remove(r)
    assert sig(chosen)==live;private={r:I[(sig(set(chosen)-{r})&~live & -(sig(set(chosen)-{r})&~live)).bit_length()-1] for r in chosen};assert all(not r&s for r,s in private.items());res.update(maximal_rejected=len(B),greedy=chosen,private_witness=private);print('greedy',len(chosen),'max rejected',len(B));
 (D/'ramsey_shared_request_certificate.json').write_text(json.dumps(res,indent=1))
if __name__=='__main__':main()
