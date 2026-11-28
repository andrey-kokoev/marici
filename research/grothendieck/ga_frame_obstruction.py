"""Inspect failures with two separate additions: port adjacency and path geometry."""
from ga_frame_trial import *
from functools import lru_cache
@lru_cache(None)
def obs(f,m):
 c,g=f;a=graph(10,[(*s,g) if i in m else s for i,s in enumerate(grow(S,g))],c)
 return [(k,t) for k in (3,7) for t in combinations(range(15),k) if all(bool(a[i]>>j&1)==(k==3) for i,j in combinations(t,2))]
def portmatch(c,d,p):return all((c>>k&1)==(d>>P.index(tuple(sorted((p[i],p[j]))))&1) for k,(i,j) in enumerate(P))
def pathgram(g):
 X=np.array([*V,I[g-1],I[g]]);L=np.eye(9,k=1,dtype=int)+np.eye(9,k=-1,dtype=int);return X@L@X.T
if __name__=='__main__':
 mp=signatures('C');cnt=Counter();example={};b=signatures('B')
 for f in frames:
    for mode in ('none','port','path'):
     gr=defaultdict(list)
     for h,p in mp[f]:
        if iso(f[0],h[0]):continue
        ix=[*p,5,6]
        if mode=='port' and not portmatch(f[0],h[0],p):continue
        if mode=='path' and not np.array_equal(pathgram(f[1]),pathgram(h[1])[np.ix_(ix,ix)]):continue
        gr[h].append(p)
     for h,ps in gr.items():
        for m in P:
            targets={tuple(sorted(p[i] for i in m)) for p in ps}
            if len(targets)!=1:continue
            t=targets.pop();x=obs(f,m);y=obs(h,t);cnt[mode,'tested']+=1;cnt[mode,'legal']+=not x
            if bool(x)!=bool(y):cnt[mode,'err']+=1
 print(cnt)
 for f in [(224,1),(352,4)]:print('obstructions',f,obs(f,(3,4)))
 print('frame matches',[(p,portmatch(224,352,p)) for h,p in mp[(224,1)] if h==(352,4)])
 print('B stabilizer',[(p,portmatch(96,96,p)) for h,p in b[(96,1)] if h==(96,1)])
 # A endpoint scope stress, compare marks under exchange of a single endpoint axis.
 for c in parents:
    for g,site in [(0,0),(9,8)]:
        X=np.array([*V,I[site]]);M=X@X.T
        for p in perms:
            ix=[*p,5]
            if not np.array_equal(M,M[np.ix_(ix,ix)]):continue
            for m in P:
                t=tuple(sorted(p[i] for i in m))
                if not obs((c,g),m) and obs((c,g),t):print('endpoint separates',c,g,m,t,obs((c,g),t)[:1]);quit()
 print('no endpoint separation')
