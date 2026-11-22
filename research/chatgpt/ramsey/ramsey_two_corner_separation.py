"""Test the red-edge separator first on four frozen splits, then on fixed maximal-port triples of fresh small triangle-free cores. Enumerate every independent fourth support. Stop on the first two-component counterexample."""
from itertools import combinations,combinations_with_replacement
from functools import reduce
from operator import and_
from random import Random
from ramsey_connected_fourth_repairs import comps,D,json,inds,grow,verify

def summary(H,cs):
    a,b=[reduce(and_,c) for c in cs];V=lambda s:[i for i in range(len(H)) if s>>i&1];return dict(intersections=[V(a),V(b)],edges=[[i,j] for i in V(a) for j in V(b) if H[i]>>j&1])

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);rows=json.loads((D/'ramsey_connected_fourth_repairs.json').read_text())['rows'];cal=[summary(H,r['minimal_components'])|dict(fixed=r['fixed'],sizes=r['components']) for r in rows if len(r['components'])==2];rng=Random(73);two=0;tried=0
    for n in range(5,13):
        for _ in range(120):
            h=[0]*n;es=list(combinations(range(n),2));rng.shuffle(es)
            for x,y in es:
                if not h[x]&h[y] and rng.random()<.62:h[x]|=1<<y;h[y]|=1<<x
            I=inds(h);k=max(map(int.bit_count,I))+2
            if k<5:continue
            M=[s for s in I if all(s>>i&1 or s&t for i,t in enumerate(h))];hit={t:sum(1<<i for i,s in enumerate(I) if s&t) for t in I};tried+=1
            for q in combinations_with_replacement(M,3):
                possible=(1<<len(I))-1
                for t in I:
                    room=k-1-t.bit_count()-sum(not s&t for s in q)
                    if room<0:possible=0;break
                    if not room:possible&=hit[t]
                    if not possible:break
                if possible.bit_count()<2:continue
                legal=[s for i,s in enumerate(I) if possible>>i&1];cs=comps(legal,lambda s:(s^(1<<v) for v in range(n)))
                if len(cs)!=2:continue
                two+=1;r=summary(h,cs)
                if not r['edges']:
                    for c in cs:verify(grow(h,[*q,c[0]]),k)
                    return dict(calibration=cal,cores=tried,splits=two,counterexample=r|dict(core=h,k=k,fixed=q,components=cs))
    return dict(calibration=cal,cores=tried,splits=two,counterexample=None)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_two_corner_separation.json').write_text(json.dumps(out)+'\n')
