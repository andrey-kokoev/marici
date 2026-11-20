"""Exhaust equality patterns of cyclic words by restricted growth strings. Rename letters ONLY to choose input representatives. When reconstructing the deck, compare words with letters FIXED, modulo rotation and reversal only. Every possible coloring by outward masks factors through such an equality pattern."""
from itertools import chain
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results'
def dihedral(s):return [a[i:]+a[:i] for a in (s,s[::-1]) for i in range(len(s))]
def normalize(s):
    d={};return tuple(d.setdefault(c,len(d)) for c in s)
def rgs(n,s=(0,),a=0):
    if len(s)==n:yield s;return
    for c in range(a+2):yield from rgs(n,s+(c,),max(a,c))
def solve(s,k):
    n=len(s);t=s+s;cnt=Counter(min(t[i:i+k],t[i:i+k][::-1]) for i in range(n));opts={}
    for w in cnt:
        for v in {w,w[::-1]}:opts.setdefault(v[:-1],[]).append((v[-1],w))
    # Fix a rare first window, orient it using the dihedral equivalence.
    w=min(cnt,key=lambda w:(cnt[w],w));cnt[w]-=1;ans=set()
    def dfs(seq,left):
        if not left:
            if seq[:k-1]==seq[-(k-1):]:ans.add(min(dihedral(seq[:n])))
            return
        for a,key in opts.get(seq[-(k-1):],[]):
            if cnt[key]:cnt[key]-=1;dfs(seq+(a,),left-1);cnt[key]+=1
    dfs(w,n-1);assert min(dihedral(s)) in ans;return ans
out=[];amb=[]
for n in (8,10):
    seen=set();h=Counter();examples={};total=0
    for s in rgs(n):
        total+=1
        if s in seen:continue
        seen.update(normalize(v) for v in dihedral(s));a=solve(s,4);h[len(a)]+=1
        if len(a)>1:
            examples.setdefault(len(a),sorted(a));amb.append(sorted(a));assert all(len(solve(v,5))==1 for v in a)
    out.append(dict(n=n,partitions=total,hist=h,examples=examples));print(out[-1],flush=True)
(D/'ramsey_four_window_ambiguous_words.json').write_text(json.dumps(amb)+'\n');(D/'ramsey_four_window_reconstruction.json').write_text(json.dumps(out,indent=2)+'\n')
