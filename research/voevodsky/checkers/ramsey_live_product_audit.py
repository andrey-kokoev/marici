"""Exact disjoint-coordinate factorization and greedy compulsory-core certificates for fresh 34-core live classes."""
from ramsey_request_scale import *
from functools import reduce,cache
from operator import and_,or_
from collections import Counter

def factors(X,m):
    if not m:return []
    b=m&-m;l=frozenset(x for x in X if not x&b);r=frozenset(x^b for x in X if x&b)
    if not l or not r:return [(b,frozenset([0 if l else b]))]+factors(l or r,m^b)
    left=factors(l,m^b);right=factors(r,m^b);shared=[f for f in left if f in right];z=m^reduce(or_,(v for v,_ in shared),0);return shared+[(z,frozenset(x&z for x in X))]

def main():
 p=json.loads((K/'ramsey_pure_port_fork.json').read_text());A=grow(p['stem_graphs'][-1],p['alternate']['to34']);I=prepare(A);F=(1<<34)-1;lib=[s for s in I if 6<=s.bit_count()<=8];qs=json.loads((K/'ramsey_compulsory_kernel_test.json').read_text())['triples'];groups=json.loads((D/'ramsey_request_scale_partitions.json').read_text());train=json.loads((D/'ramsey_shared_request_certificate.json').read_text())['group']['cases'];full=(1<<len(I))-1;cols=[sum(1<<j for j,s in enumerate(I) if s>>v&1) for v in range(34)]
 @cache
 def hits(t):return reduce(or_,(cols[v] for v in range(34) if t>>v&1),0)
 # Every independent set that avoids v extends to a maximal one in H-v. Such sets have either no extension in H or only v as extension.
 ex={0:0};boundary=[]
 for s in I:
    if s:bit=s&-s;ex[s]=ex[s^bit]|A[bit.bit_length()-1]
    free=F&~(s|ex[s]);
    if free.bit_count()<=1:boundary.append((s,free))
 out=[]
 for g in groups:
    if not g['legal'] or g['cases']==train:continue
    q=qs[g['cases'][0]]['triple'];raw=sorted(s for s in lib if s.bit_count()+sum(not s&a for a in q)==9);live=reduce(and_,map(hits,raw),full);X=frozenset(I[j] for j in range(len(I)) if live>>j&1);assert len(X)==g['legal'];core=reduce(and_,X);vary=reduce(or_,X)^core;fac=factors(frozenset(x^core for x in X),vary);assert {core|sum(v) for v in itertools.product(*(a for _,a in fac))}==X
    B=[s for s,free in boundary if (not free and core&~s or free&core)];bi=[sum(1<<j for j,s in enumerate(B) if s>>v&1) for v in range(34)];allB=(1<<len(B))-1
    masks={t:allB^reduce(or_,(bi[v] for v in range(34) if t>>v&1),0) for t in raw} if B else {};rem=allB;chosen=[]
    while rem:
        t=max(masks,key=lambda t:(rem&masks[t]).bit_count());assert rem&masks[t];rem&=~masks[t];chosen.append(t)
    for t in reversed(chosen.copy()):
        if reduce(or_,(masks[s] for s in chosen if s!=t),0)==allB:chosen.remove(t)
    dom=reduce(and_,map(hits,chosen),full);assert all(not(dom&~cols[v]) for v in range(34) if core>>v&1)
    out.append(dict(cases=g['cases'],legal=len(X),core=core,factors=[dict(mask=v,values=sorted(a)) for v,a in fac],clauses=chosen,guard_domain=dom.bit_count()))
 (D/'ramsey_live_product_audit.json').write_text(json.dumps(out));print('core sizes',Counter(x['core'].bit_count() for x in out),'factor counts',Counter(len(x['factors']) for x in out));lens=[len(x['clauses']) for x in out if x['core']];print('certificate',min(lens),statistics.median(lens),max(lens));print('nontrivial examples',[(x['cases'][0],[len(f['values']) for f in x['factors']],x['core'].bit_count(),len(x['clauses'])) for x in out if len(x['factors'])>1][:15]);print('singleton',sum(x['legal']==1 for x in out))
if __name__=='__main__':main()
