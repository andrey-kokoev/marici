"""Exploratory controls: nearest-end distance, endpoint parity, and move-local path products."""
from ga_frame_obstruction import *
from functools import cache
@cache
def local(g,m):
 w=V[list(m)].sum(axis=0);L=np.eye(9,k=1,dtype=int)+np.eye(9,k=-1,dtype=int);u=I[g-1]+I[g];return int(w@L@u),int(w@L@w)
def run():
 maps=signatures('C');B=signatures('B');A=signatures('A');cnt=Counter();ex={};trials=[]
 for f in frames:
    c,g=f
    for m in P:
        amb=any(h==f and tuple(sorted(p[i] for i in m))!=m for h,p in A[f]);
        if amb and not np.array_equal(V[m[0]],V[m[1]]):
            terms=[p for h,p in B[f] if h==f and all(local(g,z)==local(g,tuple(sorted(p[i] for i in z))) for z in P)];cnt['B path ambiguous']+=any(tuple(sorted(p[i] for i in m))!=m for p in terms)
    gr=defaultdict(list)
    for h,p in maps[f]:
        if not iso(c,h[0]):gr[h].append(p)
    for h,ps in gr.items():
        for m in P:
            for mode in ['none','depth','parity','flank','internal','both']:
                z={tuple(sorted(p[i] for i in m)) for p in ps};dist=lambda g:min(g-1,8-g)
                def keep(t):
                    if mode=='depth':return dist(g)==dist(h[1])
                    if mode=='parity':return dist(g)%2==dist(h[1])%2
                    l,b=local(g,m);r,d=local(h[1],t);return {'none':True,'flank':l==r,'internal':b==d,'both':(l,b)==(r,d)}[mode]
                z={t for t in z if keep(t)}
                if len(z)==1:trials.append((mode,f,m,h,z.pop()))
 for mode,f,m,h,t in trials:
    x=not obs(f,m);y=not obs(h,t);cnt[mode,'total']+=1;cnt[mode,'legal to legal']+=x and y;cnt[mode,'errors']+=x!=y
    if x and y:ex.setdefault(mode,(f,m,h,t))
 print(cnt,ex)
if __name__=='__main__':run()
