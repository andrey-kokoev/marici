"""Frozen chart trial; table columns 1..16, catalogue vertices 0..15."""
from pathlib import Path
from itertools import combinations,product
from collections import defaultdict
import json,sys
D=Path(__file__).resolve().parents[1]/'voevodsky';sys.path.insert(0,str(D/'checkers'))
from ramsey_table_cube_differences import analyze

def candidates():
    d=analyze(16);cols=set(range(1,17));U=set(d['leftover']);feet=defaultdict(list)
    for p in d['pieces']:
        U.update(p['new']);cube=list(product(*[(i,i+1) for i in p['start']]));foot=set().union(*map(set,cube))
        for t in cube:feet[t].append(foot)
    A=set();B=set();C=set()
    for t in U:
        for x in t:
            for sign in (-1,1):
                v=x+sign;u=x-sign
                if not {v,u}<=cols-set(t):continue
                t1=tuple(sorted(set(t)-{x}|{u}));t2=tuple(sorted(set(t)-{x}|{v}))
                if t1 in U and t2 not in U and min(b-a for a,b in zip(t2,t2[1:]))>=2:A.add((t,v))
    for t,fs in feet.items():
        if len(fs)>=2:B.update((t,v) for v in set.intersection(*fs)-set(t))
    Q={q for q in combinations(sorted(cols),4) if all(t in feet for t in combinations(q,3))}
    for q in Q:
        if not any(all(t in Q for t in combinations(sorted(set(q)|{v}),4)) for v in cols-set(q)):C.update((t,next(iter(set(q)-set(t)))) for t in combinations(q,3))
    return [sorted(X) for X in (A,B,C)]

def trial(idx):
    lists=candidates();a=json.loads((D/'results/ramsey_37_catalogue_free.json').read_text())['certificates'][idx]['core'];order=sorted(range(16),key=lambda i:(a[i].bit_count(),i));blue=lambda t:all(not(a[i]>>j&1) for i,j in combinations(t,2))
    for perm in (False,True):
        bind=lambda i:order[((i-1)^int(perm))];chosen=[]
        for L in lists:
            good=[(t,v) for t,v in L if blue(list(map(bind,t))+[bind(v)])];chosen.append((len(L),len(good),good[:1]))
        for size,ng,first in chosen:
            if not first:print(idx,perm,size,ng,'EMPTY');continue
            t,v=first[0];T=set(map(bind,t));V=bind(v);ext=[q for q in combinations(range(16),5) if T<=set(q) and blue(q)];co=[q for q in ext if V in q];print(idx,perm,size,ng,(t,v),sorted(T),V,len(ext),len(co),co[:1])
if __name__=='__main__':trial(int(sys.argv[1]) if len(sys.argv)>1 else 6)
