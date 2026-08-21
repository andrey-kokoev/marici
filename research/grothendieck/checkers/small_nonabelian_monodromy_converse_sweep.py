"""Complete automorphism sweep for S3, D8, and Q8 cyclic actions."""

from itertools import permutations
from math import gcd
import json
from pathlib import Path


def perm_mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inv(p):
    return tuple(p.index(i) for i in range(len(p)))


def qmul(x, y):
    sx, ax = x; sy, ay = y
    if ax == 0: return (sx * sy, ay)
    if ay == 0: return (sx * sy, ax)
    if ax == ay: return (-sx * sy, 0)
    table = {(1, 2):(1, 3),(2, 3):(1, 1),(3, 1):(1, 2),
             (2, 1):(-1, 3),(3, 2):(-1, 1),(1, 3):(-1, 2)}
    s, a = table[(ax, ay)]
    return (sx * sy * s, a)


def qneg(x):
    return (-x[0], x[1])


def dmul(x, y):
    a, b = x; c, d = y
    return ((a + (-1 if b else 1) * c) % 4, (b + d) % 2)


def map_order(mapping, identity_map):
    cur = identity_map
    for n in range(1, 100):
        cur = {x: mapping[cur[x]] for x in mapping}
        if cur == identity_map:
            return n
    raise AssertionError("automorphism order")


def iterate(mapping, x, n):
    for _ in range(n):
        x = mapping[x]
    return x


def fiber_ok(group, mul, identity, mapping, action_order, n):
    def smul(x, y):
        k, h = x; ell, j = y
        return (mul(k, iterate(mapping, ell, h)), (h + j) % action_order)
    def power(x):
        out = (identity, 0)
        for _ in range(n): out = smul(out, x)
        return out
    failed = []
    for h in range(action_order):
        images = [power((k, h)) for k in group]
        target = [(k, (n * h) % action_order) for k in group]
        if sorted(images) != sorted(target): failed.append(h)
    return not failed, failed


def s3_data():
    group = list(permutations(range(3))); e = (0,1,2)
    maps = []
    for g in group:
        gi = perm_inv(g)
        maps.append({x: perm_mul(perm_mul(g, x), gi) for x in group})
    return group, perm_mul, e, 6, maps


def q8_data():
    group = [(s,a) for a in range(4) for s in (-1,1)]; e=(1,0)
    units = [(s,a) for a in (1,2,3) for s in (-1,1)]
    maps=[]
    for ii in units:
        for jj in units:
            if ii[1] == jj[1]: continue
            kk=qmul(ii,jj); mp={e:e,(-1,0):(-1,0)}
            for src,img in [((1,1),ii),((1,2),jj),((1,3),kk)]:
                mp[src]=img; mp[qneg(src)]=qneg(img)
            maps.append(mp)
    return group,qmul,e,4,maps


def d8_data():
    group=[(a,b) for b in range(2) for a in range(4)]; e=(0,0); maps=[]
    for r_image in ((1,0),(3,0)):
        for b in range(4):
            s_image=(b,1); mp={}
            for a,c in group:
                x=e
                for _ in range(a): x=dmul(x,r_image)
                if c: x=dmul(x,s_image)
                mp[(a,c)]=x
            maps.append(mp)
    return group,dmul,e,4,maps


def main():
    summaries=[]; counterexamples=[]; checks=0
    for name,data in [("S3",s3_data()),("D8",d8_data()),("Q8",q8_data())]:
        group,mul,e,exponent,maps=data; ident={x:x for x in group}; hist={}
        for mp in maps:
            order=map_order(mp,ident); hist[order]=hist.get(order,0)+1
            for n in range(1,13):
                ok,failed=fiber_ok(group,mul,e,mp,order,n)
                predicted=gcd(n,exponent*order)==1
                checks += len(group)*len(group)*order
                if ok != predicted:
                    counterexamples.append({"group":name,"order":order,"n":n,
                                            "compatible":ok,"failed":failed})
        summaries.append({"group":name,"automorphism_count":len(maps),
                          "automorphism_order_histogram":hist})
    assert not counterexamples, counterexamples
    result={"falsifier":"visible action prime survives every fiber",
            "groups":summaries,"automorphism_count":sum(x["automorphism_count"] for x in summaries),
            "index_cases":38*12,"coefficient_value_checks":checks,
            "counterexamples":counterexamples,"status":"pass_no_counterexample"}
    out=Path(__file__).parents[1]/"results"/"small-nonabelian-monodromy-converse-sweep.json"
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))


if __name__=="__main__": main()
