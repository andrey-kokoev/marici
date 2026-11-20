"""Select endpoints from a growing word. One canonical fresh endpoint per prefix.
All endpoints, loops included. Only count legal continuations to the stated horizon.
"""
from functools import cache
from collections import Counter
from itertools import combinations

@cache
def moves(w):
    old=list(zip(w,w[1:]));n=len(old)
    def join(e,f):return e[1]==f[0] or f[1]==e[0]
    opts=[]
    for y in range(max(w)+2):
        e=(w[-1],y);P=[v for v in old if join(v,e)];N=[v for v in old if not join(v,e)]
        if any(join(a,b) for a,b in combinations(P,2)):continue
        if any(not any(join(a,b) for a,b in combinations(t,2)) for t in combinations(N,3)):continue
        opts.append(w+(y,))
    return opts

@cache
def ways(w,d):return 1 if d==0 else sum(ways(u,d-1) for u in moves(w))

def grow(w,h):
    opts=moves(w)
    if not opts:return [w]
    scores=[ways(u,min(h,8-(len(u)-1))) for u in opts];return [z for u,s in zip(opts,scores) if s==max(scores) for z in grow(u,h)]

if __name__=='__main__':
    for h in range(5):
        terminal=grow((0,),h);print(h,sorted(Counter(len(w)-1 for w in terminal).items()),'example',next((w for w in terminal if len(w)==9),None))
    for w in [(0,1,2,3),(0,1,2,3,0),(0,1,2,3,0,4)]:print('prefix',w,[(u[-1],ways(u,1),ways(u,2),ways(u,8-(len(u)-1))) for u in moves(w)])
