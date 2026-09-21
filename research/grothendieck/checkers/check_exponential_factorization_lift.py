"""Exact normal-form section and right-linear factorization lift fixtures."""
from collections import defaultdict
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path
import json


def clean(a):return {k:v for k,v in a.items() if v}
def norm(a):return sum(abs(v) for v in a.values())
def mul(a,b):
    out=defaultdict(int)
    for u,c in a.items():
        for v,d in b.items():out[u+v]+=c*d
    return clean(out)
def end(word,start):
    for p,_ in word:
        assert not start & (1<<p)
        start |= 1<<p
    return start

def record_word(word,start,target):
    out={():1};v=start
    for p,mark in word:
        nxt=v|1<<p
        if mark:
            terms={v:1}
            if nxt!=target:terms[nxt]=-1
            temp=defaultdict(int)
            for t,c in out.items():
                for z,d in terms.items():temp[t+(z,)]+=c*d
            out=clean(temp)
        v=nxt
    return out

def record(a,start,target):
    out=defaultdict(int)
    for w,c in a.items():
        for t,d in record_word(w,start,target).items():out[t]+=c*d
    return clean(out)

def canonical(u,v):
    return tuple((p,0) for p in range(v.bit_length()) if (v & ~u)&(1<<p))
def derivative(w):
    return {w[:i]+((p,1),)+w[i+1:]:1 for i,(p,_) in enumerate(w)}

def section_chain(chain,start,target):
    if not chain:return {canonical(start,target):1}
    out={canonical(start,chain[0]):1}
    for u,v in zip(chain,chain[1:]+(target,)):
        out=mul(out,derivative(canonical(u,v)))
    return out

@lru_cache(None)
def normal_word(word,start):
    target=end(word,start);out=defaultdict(int)
    for chain,c in record_word(word,start,target).items():
        if all(u!=v and u&v==u for u,v in zip(chain,chain[1:])):
            for w,d in section_chain(chain,start,target).items():out[w]+=c*d
    return clean(out)

def normal(a,start):
    out=defaultdict(int)
    for w,c in a.items():
        for v,d in normal_word(w,start).items():out[v]+=c*d
    return clean(out)

@lru_cache(None)
def lift_word(word,start):
    out=defaultdict(int)
    for i in range(1,len(word)+1):
        edge=(word[i-1],);suffix=word[i:]
        for u,c in normal_word(word[:i-1],start).items():out[u+edge,suffix]+=c
        for u,c in normal_word(word[:i],start).items():out[u,suffix]-=c
    return clean(out)

def lift(a,start):
    out=defaultdict(int)
    for w,c in a.items():
        for pair,d in lift_word(w,start).items():out[pair]+=c*d
    return clean(out)

def multiply_lift(h):
    out=defaultdict(int)
    for (u,v),c in h.items():out[u+v]+=c
    return clean(out)

def second_record(h,start,target):
    out=defaultdict(int)
    for (u,v),c in h.items():
        middle=end(u,start)
        for t,d in record_word(v,middle,target).items():out[middle,u,t]+=c*d
    return clean(out)

def first_record(h,start):
    out=defaultdict(int)
    for (u,v),c in h.items():
        middle=end(u,start)
        for t,d in record_word(u,start,middle).items():out[middle,t,v]+=c*d
    return clean(out)

def project_second(h,start):
    out=defaultdict(int,h)
    for (u,v),c in h.items():
        for w,d in normal_word(v,end(u,start)).items():out[u,w]-=c*d
    return clean(out)

def diamond(p,q,kind):
    if kind==0:return {((p,0),(q,0)):1,((q,0),(p,0)):-1}
    return {((p,1),(q,0)):1,((p,0),(q,1)):1,
            ((q,1),(p,0)):-1,((q,0),(p,1)):-1}

normal_checks=0
for n in range(1,5):
    for order in permutations(range(n)):
        for marks in product((0,1),repeat=n):
            w=tuple(zip(order,marks));a={w:1};target=(1<<n)-1
            r=normal_word(w,0)
            assert record(r,0,target)==record(a,0,target)
            assert normal(r,0)==r
            assert norm(r)<=2**n
            h=lift_word(w,0)
            difference=defaultdict(int,a)
            for u,c in r.items():difference[u]-=c
            assert multiply_lift(h)==clean(difference)
            assert not first_record(h,0)
            assert norm(h)<=3*(2**n-1)
            normal_checks+=1

factor_checks=0
max_ratio=0
for n in range(4,9):
    for ka,kb,mark in product((0,1),repeat=3):
        a=diamond(0,1,ka)
        gap={tuple((p,mark) for p in range(2,n-2)):1}
        b=mul(gap,diamond(n-2,n-1,kb))
        v=mul(a,b);h=lift(v,0)
        expected=defaultdict(int)
        for (u,t),c in lift(a,0).items():
            for w,d in b.items():expected[u,t+w]+=c*d
        assert h==clean(expected) # right S-linearity on I
        assert multiply_lift(h)==v
        assert not first_record(h,0)
        assert not second_record(h,0,(1<<n)-1)
        assert project_second(h,0)==h
        assert norm(h)<=3*(2**n-1)*norm(v)
        max_ratio=max(max_ratio,norm(h)/norm(v))
        factor_checks+=1

nonlocal_checks=0
for length in (3,4):
    order=tuple(reversed(range(length)))
    for marks in product((0,1),repeat=length):
        w=tuple(zip(order,marks));a=defaultdict(int,{w:1})
        for u,c in normal_word(w,0).items():a[u]-=c
        a=clean(a)
        if not a:continue
        for kind in (0,1):
            b=diamond(length,length+1,kind)
            v=mul(a,b);h=lift(v,0)
            expected=defaultdict(int)
            for (u,t),c in lift(a,0).items():
                for z,d in b.items():expected[u,t+z]+=c*d
            assert h==clean(expected)
            assert multiply_lift(h)==v
            assert not second_record(h,0,(1<<(length+2))-1)
            assert project_second(h,0)==h
            assert norm(h)<=3*(2**(length+2)-1)*norm(v)
            max_ratio=max(max_ratio,norm(h)/norm(v))
            nonlocal_checks+=1

# Cancellation test on a sum of genuinely different product presentations.
v=defaultdict(int)
for order in permutations(range(4)):
    for ka,kb in product((0,1),repeat=2):
        a=diamond(order[0],order[1],ka)
        b=diamond(order[2],order[3],kb)
        coefficient=(order[0]*order[2]+order[1]+3*ka+kb)%5-2
        for w,c in mul(a,b).items():v[w]+=coefficient*c
v=clean(v);assert v
h=lift(v,0)
assert multiply_lift(h)==v and not second_record(h,0,15)
assert norm(h)<=3*(2**4-1)*norm(v)

result={'schema':'marici.grothendieck.exponential-factorization-lift.v1','passed':True,
        'normal_section_and_telescoping_checks':normal_checks,
        'product_and_right_linearity_checks':factor_checks,
        'nonlocal_relation_factor_checks':nonlocal_checks,
        'cancelling_product_sum_checked':True,
        'largest_fixture_lift_to_path_norm_ratio':max_ratio,
        'scope':'Exact finite record identities and path coefficient norms. The universal exponential bound and all-radius exactness are proved in the companion note, not inferred from these fixtures.'}
root=Path(__file__).resolve().parents[3]
p=root/'research/grothendieck/results/exponential-factorization-lift.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
