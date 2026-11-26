"""Exact face-incidence search on the frozen bad shell, with an optional interior point."""
from itertools import combinations,permutations
from functools import lru_cache
from ramsey38_novel_array_trial import prev,pf,cf,json,t
from ramsey38_global_shell import sub
from ramsey38_support_ball_completion import shelling
from ramsey38_compare_support_fillings import boundary

def setup(i):
    x=next(x for x in json.loads(pf.read_text())['entries'] if x['record']==i and x['root']==8);g=t.graph(x['word']);r={v:frozenset(s&g[8]) for v,s in g.items() if v not in g[8]|{8}};return r,frozenset(map(frozenset,x['cases']['24']['shell']))

def link_profile(fs):
    def oriented(f):return {(v,f[(i+1)%3]) for i,v in enumerate(f)}
    visited=set();components=0;orientable=True
    for start in fs:
        if start in visited:continue
        components+=1;assigned={start:tuple(sorted(start))};todo=[start];visited.add(start)
        while todo:
            f=todo.pop();arc=oriented(assigned[f])
            for u in fs:
                if len(f&u)!=2:continue
                cand=tuple(sorted(u));cand=cand[::-1] if arc&oriented(cand) else cand
                if u in assigned:orientable &= oriented(assigned[u])==oriented(cand)
                else:assigned[u]=cand;visited.add(u);todo.append(u)
    return components,orientable

def fill(p,req,bd):
    ts=sorted(sub(p,4),key=sorted);car=lambda f:sum(1<<i for i,t in enumerate(ts) if f<=t);faces=[(car(f),f in bd,f in req) for f in sub(p,3)];must=[car(f) for f in req|bd];m=sum(1<<i for i,t in enumerate(ts) if t in req);full=(1<<len(ts))-1;stats=[0,0]
    edges=sub(p,2);be=set.union(*(sub(f,2) for f in bd));needs=set.union(*(sub(f,2) for f in req|bd));fans=[]
    for e in edges:
        h=car(e);ends=sorted(set.union(set(),*(f-e for f in bd if e<=f)));opts=[]
        for n in range(0 if ends else 3,len(p-e-set(ends))+1):
            for q in permutations(p-e-set(ends),n):
                if not ends and (q[0]!=min(q) or q[1]>q[-1]):continue
                order=(ends[0],)+q+(ends[1],) if ends else q+(q[0],);ring=sum(car(e|{u,v}) for u,v in zip(order,order[1:]));opts.append(ring)
        fans.append((e,h,opts+([] if e in needs else [0])))
    def dfs(m,no):
        stats[0]+=1
        while True:
            free=full&~(m|no);plus=minus=0;opts=[]
            for h,b,needed in faces:
                n=(m&h).bit_count();a=free&h;quota=1 if b else 2
                if n>quota:return
                if n==quota:minus|=a
                elif n or b or needed:
                    need=quota-n;k=a.bit_count()
                    if k<need:return
                    if k==need:plus|=a
                    else:opts.append(a)
                elif a.bit_count()==1:minus|=a
            for h in must:
                if h&m:continue
                a=h&free
                if not a:return
                if not a&(a-1):plus|=a
                else:opts.append(a)
            if plus&minus:return
            if plus or minus:m|=plus;no|=minus;continue
            # Propagate entire fans rather than only face multiplicities.
            best=None
            for e,h,choices in fans:
                inc=m&h;ok=[z for z in choices if not z&no and z&inc==inc]
                if not ok:return
                both=ok[0];either=0
                for z in ok:both&=z;either|=z
                plus|=both&free;minus|=(h&~either)&free
                if len(ok)>1 and (best is None or len(ok)<len(best[1])):best=(h,ok)
            if plus&minus:return
            if plus or minus:m|=plus;no|=minus;continue
            break
        if not opts:
            S=frozenset(t for i,t in enumerate(ts) if 1<<i&m);stats[1]+=1
            defects={}
            for v in set.union(set(),*S):
                fs={t-{v} for t in S if v in t};chi=len(set.union(set(),*fs))-len(set.union(*(sub(f,2) for f in fs)))+len(fs)
                if chi!=(1 if any(v in f for f in bd) else 2):defects[v]=chi
            if defects:
                if len(p)==7:
                    prof=link_profile({t-{19} for t in S if 19 in t});assert defects[19]==0 and prof==(1,False);print('link Euler defect:',defects,'link at 19 connected, nonorientable',flush=True)
                return
            order=shelling(S)
            if order:assert boundary(S)==bd;return order
            # A shellable ball is dual-connected. A completed closed-incidence
            # component cannot be enlarged by face attachments at fixed boundary.
            return
        if best and len(best[1])<=4:
            h,choices=best
            for z in choices:
                ans=dfs(m|z,no|(h&~z))
                if ans:return ans
            return
        h=min(opts,key=int.bit_count);b=h&-h
        return dfs(m|b,no) or dfs(m,no|b)
    o=dfs(m,0);return o,stats
if __name__=='__main__':
    r,bd=setup(5);s,bd6=setup(6);assert bd==bd6 and {v for v in r if r[v]!=s[v]}=={22};p=frozenset.union(*r.values());
    for pts in [p,p|{28}]:
        order,stats=fill(pts,set(r.values()),bd);print(len(pts),stats,'certificate:',None if not order else [sorted(x) for x in order],flush=True)
        if order:
            assert all(any(s<=t for t in order) for s in r.values()) and all(any(s<=t for t in order) for s in setup(6)[0].values());assert boundary(order)==bd
            for rr in (r,s):assert {v for v,f in rr.items() if len(f)<4 and not any(f<=q for q in bd)}=={24}
            print('new vertex on boundary?',any(28 in f for f in bd),'released-edge link:',prev.fmt(t-r[24] for t in order if r[24]<=t))
    good=frozenset(map(frozenset,next(x for x in json.loads(cf.read_text())['certificates'] if x['record']==5 and x['root']==8)['actual_hidden']['24']));assert shelling(good);gd=boundary(good)
    assert gd^bd==sub(frozenset((9,19,26,27)),3) and {v for v,f in s.items() if len(f)<4 and not any(f<=q for q in gd)}=={24};print('alternative boundary flip',prev.fmt(bd-gd),'to',prev.fmt(gd-bd))
