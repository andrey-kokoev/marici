"""Greedy side test, with replayable per-side results; report exact edge coverage."""
from ramsey310_exclusive_census import index
from ramsey310_one_side_demands import possible, residual
from ramsey310_cached_kernel import CachedKernel
from pathlib import Path
import json,sys,heapq
D=Path(__file__).resolve().parents[1]/'results'
LOG=D/'ramsey310_side_frontier.jsonl'

def bits(m):
    while m:
        b=m&-m;yield b.bit_length()-1;m^=b

def run(n,budget):
    A=residual(n);S,dis,p=index(n);lookup={s:i for i,s in enumerate(S)};N=len(S)
    def side(i,j):return max(i,j)*N+min(i,j)
    def mates(k):
        i,j=divmod(k,N);o=dis[i]&dis[j]
        for l in bits(o):
            for z in bits(p[l]&o):yield side(l,z)
    weights={}
    for i,row in enumerate(p):
        for j in bits(row):
            o=dis[i]&dis[j];w=sum((p[l]&o).bit_count() for l in bits(o))
            if w:weights[side(i,j)]=w
    total=sum(weights.values())//2;covered=0;done=set()
    def record(k,ok):
        nonlocal covered
        if k in done:return
        done.add(k)
        if not ok:
            covered+=weights[k];weights[k]=0
            for l in mates(k):
                if weights[l]:weights[l]-=1
    for f in [D/'ramsey310_one_side_demands.jsonl',LOG]:
        if not f.exists():continue
        for r in map(json.loads,f.read_text().splitlines()):
            if r['record']==n:
                for e in r['sides']:record(side(*(lookup[s] for s in e['rows'])),e['passes'])
    follow=D/'ramsey310_complete_side.jsonl'
    if follow.exists():
        for r in map(json.loads,follow.read_text().splitlines()):
            if r['record']==n and not r['passes']:
                k=side(*(lookup[s] for s in r['side']));assert k in done
                # This side previously passed the necessary test, so its edges were not charged.
                done.remove(k);record(k,False)
    heap=[(-w,k) for k,w in weights.items() if w and k not in done];heapq.heapify(heap)
    cache=CachedKernel(A);initial=covered;tested=passed=0
    while heap and tested<budget:
        neg,k=heapq.heappop(heap)
        if -neg!=weights[k]:
            if weights[k]:heapq.heappush(heap,(-weights[k],k))
            continue
        i,j=divmod(k,N);E=[S[i],S[j]];ok=possible(A,E,cache);record(k,ok);tested+=1;passed+=ok
        with LOG.open('a') as f:f.write(json.dumps(dict(record=n,sides=[dict(rows=E,passes=ok)]))+'\n')
    print(n,'new tests',tested,'passed',passed,'newly excluded',covered-initial,'total excluded',covered,'remaining',total-covered,flush=True)
if __name__=='__main__':
    for n in [49241,49289,49915,49939]:run(n,int(sys.argv[1]) if len(sys.argv)>1 else 8)
