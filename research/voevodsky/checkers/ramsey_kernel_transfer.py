"""Freeze the 12-row guard, project to nine points only after exact syntactic matching. Validate using separate full-domain keys."""
from ramsey_request_scale import *
from collections import Counter,defaultdict
from functools import reduce
from operator import and_
def main():
 cert=json.loads((D/'ramsey_shared_request_certificate.json').read_text());K0=cert['common_kernel'];grid=cert['surviving_masks'];train=set(cert['group']['cases']);triples=json.loads((K/'ramsey_compulsory_kernel_test.json').read_text())['triples'];hist=Counter();matched=[];proj=defaultdict(list);near=[]
 def present(t,q):return t.bit_count()+sum(not t&s for s in q)==9
 p=json.loads((K/'ramsey_pure_port_fork.json').read_text());A=grow(p['stem_graphs'][-1],p['alternate']['to34']);I=prepare(A);L=[t for t in I if 6<=t.bit_count()<=8];N={x:j for j,x in enumerate(I)};full=(1<<len(I))-1;cols=[sum(1<<i for i,s in enumerate(I) if s>>v&1) for v in range(34)]
 from functools import cache
 @cache
 def hit(t):
    h=0
    while t:b=t&-t;t-=b;h|=cols[b.bit_length()-1]
    return h
 assert reduce(and_,map(hit,K0),full)==sum(1<<N[x] for x in grid)
 # Blind nine-point prediction; use saved full-domain counts ONLY to audit, never to rank or select rows.
 reference=json.loads((D/'ramsey_request_scale.json').read_text())[1]['rows'];outside=[];miss={x:[t for t in L if not x&t] for x in grid}
 for i,r in enumerate(triples):
    if i in train:continue
    q=r['triple'];flags=[present(t,q) for t in K0];hist[sum(flags)]+=1
    inside=[x for x in grid if not any(present(t,q) for t in miss[x])];total=reference[i]['survivors'];assert total>=len(inside);outside.append(dict(case=i,inside=inside,total=total,guard=sum(flags)))
    if sum(flags)==11:
        guard=reduce(and_,(hit(t) for t,v in zip(K0,flags) if v),full);small=[];m=guard
        while m:b=m&-m;small.append(I[b.bit_length()-1]);m-=b
        rows=[t for t in L if present(t,q)];surv=tuple(x for x in small if all(x&t for t in rows));assert reduce(and_,map(hit,rows),full)==sum(1<<N[x] for x in surv);near.append(dict(case=i,missing=flags.index(False),domain=len(small),supports=surv,grid_sufficient=all(x in grid for x in surv)))
    if all(flags):
        rows=[t for t in L if present(t,q)];surv=tuple(x for x in grid if all(x&t for t in rows));assert reduce(and_,map(hit,rows),full)==sum(1<<N[x] for x in surv);matched.append(i);proj[surv].append(i)
 res=dict(heldout=len(triples)-len(train),hist=hist,matched=matched,near=near,projection_audit=outside,groups=[dict(supports=s,cases=cases) for s,cases in proj.items()]);print('hits',len(matched),'hist',hist,'groups',[(len(k),len(v)) for k,v in proj.items()]);(D/'ramsey_kernel_transfer.json').write_text(json.dumps(res))
if __name__=='__main__':main()
