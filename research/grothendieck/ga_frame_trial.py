"""Exact frame signatures: use t_perp scaled by |s|², recoverable by contracting s wedge t with s."""
from ga_seam_v5 import S,graph,check,combinations
from ramsey_repair_next_seam import grow
from itertools import permutations
from collections import defaultdict,Counter
import numpy as np
P=list(combinations(range(5),2));V=np.array([[int(i in row) for i in range(9)] for row in S]);I=np.eye(9,dtype=int);parents=[c for c in range(1024) if check(graph(9,S,c),16383,3,7)];frames=[(c,g) for c in parents for g in range(1,9)];perms=list(permutations(range(5)));ident=perms[0]
def neigh(c):
 M=np.zeros((5,5),int)
 for k,(i,j) in enumerate(P):M[i,j]=M[j,i]=c>>k&1
 return M@V

def iso(c,d):
 for p in perms:
    if all((c>>k&1)==(d>>P.index(tuple(sorted((p[i],p[j]))))&1) for k,(i,j) in enumerate(P)) and any(np.array_equal(V[list(p)],v) for v in (V,V[:,::-1])):return True
 return False

def gram(f,mode):
 c,g=f;T=neigh(c);v=[*V,I[g-1],I[g]]
 if mode in ('T','B'):v.extend(T)
 if mode=='C':v.extend(3*T-(V*T).sum(axis=1)[:,None]*V)
 x=np.array(v);return x@x.T

def signatures(mode):
 groups=defaultdict(list);orig={}
 for f in frames:
    G=gram(f,mode);orig[f]=G.tobytes()
    for p in perms:
     for l,r in ([(5,6),(6,5)] if mode in ('A','T') else [(5,6)]):
      ix=[*p,l,r]+([7+i for i in p] if len(G)>7 else []);groups[G[np.ix_(ix,ix)].tobytes()].append((f,p))
 return {f:groups[key] for f,key in orig.items()}
if __name__=='__main__':
 maps={mode:signatures(mode) for mode in ('A','O','T','B','C')}
 # Independent exterior-square coordinates: pair each blade with all x_j wedge x_k.
 def wedge(x,y):return np.array([x[i]*y[j]-x[j]*y[i] for i,j in combinations(range(9),2)])
 ext={}
 for f in frames:
    c,g=f;X=np.array([*V,I[g-1],I[g]]);T=neigh(c);Y=np.array([*X,*T]);assert np.array_equal(Y@Y.T,Y[:,::-1]@Y[:,::-1].T)
    ext[f]=np.array([[(wedge(s,t)@wedge(x,y)) for x in X for y in X] for s,t in zip(V,T)]).reshape(5,7,7)
 O=maps['O']
 for f in frames:
    verified=set()
    for h,p in O[f]:
        ix=[*p,5,6]
        if np.array_equal(ext[f],ext[h][np.ix_(p,ix,ix)]):verified.add((h,p))
    assert verified==set(maps['C'][f])
 counts=Counter();examples={};trials=[]
 for f in frames:
    for m in P:
        images={mode:{tuple(sorted(p[i] for i in m)) for h,p in maps[mode][f] if h==f} for mode in ('A','O','T','B')};
        if len(images['A'])>1 and not np.array_equal(V[m[0]],V[m[1]]):
            counts['eligible']+=1
            for mode,v in images.items():counts[mode,'ambiguous']+=len(v)>1
            if len(images['B'])>1:examples.setdefault('B',(f,m,sorted(images['B'])))
        for t in images['A']-{m}:trials.append(('A',f,m,f,t))
    for mode in ('A','C'):
     gr=defaultdict(list)
     for h,p in maps[mode][f]:
        if not iso(f[0],h[0]):gr[h].append(p)
     for h,ps in gr.items():
        for m in P:
            choices={tuple(sorted(p[i] for i in m)) for p in ps}
            if len(choices)==1:trials.append((mode+' transfer',f,m,h,choices.pop()))
 # Only now read child verdicts.
 from functools import lru_cache
 @lru_cache(None)
 def ok(f,m):
    c,g=f;return check(graph(10,[(*s,g) if i in m else s for i,s in enumerate(grow(S,g))],c),32767,3,7)
 for mode,f,m,h,t in trials:
    counts[mode,'trials']+=1;counts[mode,'legal source']+=bool(ok(f,m))
    if ok(f,m)!=ok(h,t):counts[mode,'errors']+=1;examples.setdefault(mode,(f,m,ok(f,m),h,t,ok(h,t)))
 print(counts,examples)
