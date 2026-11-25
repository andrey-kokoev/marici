"""One SAT instance per challenge: choose shadow rows covering all challenge supports and at most one selected row per deleted original. This searches all budget partitions simultaneously."""
from ramsey312_exact_four_cover import *
from functools import reduce
from operator import and_
import gzip

def solve_budget(d,s,el):
 h=F^d;anchors={i:adj[i]&h for i in bits(d)};cat=[];memo={}
 for t in el:
    g=t&d
    if not g:continue
    if g not in memo:memo[g]=reduce(and_,(anchors[i] for i in bits(g)))
    if memo[g]:cat.append((g,memo[g],t^g))
 challenge=set(anchors.values());rounds=0
 while True:
    rounds+=1;ss=sorted(challenge);full=(1<<len(ss))-1;col=[sum(1<<j for j,x in enumerate(ss) if x>>i&1) for i in range(52)];masks={}
    for g,b,t in cat:
        miss=full
        for i in bits(t):miss&=~col[i]
        opts=masks.setdefault(g,{})
        for i in bits(b):opts.setdefault(miss&col[i],(1<<i,t))
    rows=[]
    for g,opts in masks.items():
        mx=[]
        for r in sorted(opts,key=int.bit_count,reverse=True):
            if not any(r&~v==0 for v in mx):mx.append(r);rows.append((g,*opts[r],r))
    pool=IDPool(start_from=1+len(rows));clauses=[];inc=[[] for _ in ss]
    for i in bits(d):clauses.extend(CardEnc.atmost([j for j,(g,b,t,r) in enumerate(rows,1) if g>>i&1],1,vpool=pool).clauses)
    for j,(g,b,t,r) in enumerate(rows,1):
        for i in bits(r):inc[i].append(j)
    with Solver(name='g4',bootstrap_with=clauses+inc) as sl:
        if not sl.solve():return dict(cert=None,challenge=ss,rounds=rounds)
        model=set(sl.get_model());cert=[(g,b,t) for j,(g,b,t,r) in enumerate(rows,1) if j in model];assert sum(g.bit_count() for g,b,t in cert)==6
    missed=[x for x in s if not any(x&b and not x&t for g,b,t in cert)]
    if not missed:return dict(cert=cert,challenge_size=len(ss),rounds=rounds)
    challenge.update(missed[::max(1,len(missed)//24)][:25])

def main():
 el=list(sets(F,11));src,dst=sys.argv[1:3];
 with open(src) as f,gzip.open(D/f'ramsey312_global_{dst}.jsonl.gz','wt') as out:
    for l in f:
        d,*s=map(int,l.split());r=solve_budget(d,s,el);out.write(json.dumps(dict(d=d,n=len(s),**r))+'\n');out.flush()
if __name__=='__main__':main()
