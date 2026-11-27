"""Separate a safe move, a one-cell finish, and a two-cell finish on frozen middle pools."""
from ramsey38_middle_choice_holdout import P,R,prev,json,graph,setup,add,boundary,attaches,Counter
from itertools import combinations
from collections import defaultdict

def run():
    truth=json.loads(R.read_text());assert truth['prediction_sha']==prev.sha(P.read_bytes());it=iter(truth['results']);res=[];tot=Counter();groups=defaultdict(dict)
    for e in json.loads(P.read_text())['cases']:
        g=graph(e['word']);u=e['u'];L=sorted(g[u]);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);cells=sorted(map(frozenset,combinations(L,4)),key=sorted)
        for d in e['requests']:
            ref=next(it);assert (ref['record'],ref['moves'],ref['goal'])==(e['record'],d['moves'],d['goal']);goal=set(d['goal']);h=g;old=[]
            for x,v in d['moves']:
                _,rs,_=setup(h,u);old.append(dec(rs[x]));h=add(h,(x,v))
            _,rs,_=setup(h,u);req=set(map(dec,rs.values()));short={j:dec(s) for j,s in rs.items() if s.bit_count()<4};stats=[]
            def status(B):
                bd=boundary(B);hid={j for j,s in short.items() if not any(s<=f for f in bd)};return hid<=goal,hid==goal and not set(old)&bd and all(any(s<=t for t in B) for s in req)
            for pool in d['pool']:
                M=frozenset(map(frozenset,pool));sealed=set(L)-set.union(set(),*boundary(M));passes=all(any(s<=t for t in M) for s in req if s&sealed);safe=[];one=[];two=[]
                if passes:
                    for t in cells:
                        if t in M or not attaches(M,t):continue
                        B=M|{t};ok,win=status(B)
                        if not ok:continue
                        safe.append(sorted(t));
                        if win:one.append(sorted(t))
                        for a in cells:
                            if a not in B and attaches(B,a) and status(B|{a})==(True,True):two.append([sorted(t),sorted(a)])
                stats.append(dict(sealed=passes,safe=safe,one=one,two=two))
            choices={k:next((i for i,z in enumerate(stats) if z[k]),None) for k in ('sealed','safe','one')};choices['two']=next((i for i,z in enumerate(stats) if z['one'] or z['two']),None);assert choices['two']==d['look'] and choices['sealed']==d['baseline'];actual=set(ref['ok']);depth=1 if choices['one'] is not None else 2 if choices['two'] is not None else None;tot['depth_'+str(depth)]+=1
            for k,i in choices.items():tot[k+'_pick']+=i is not None;tot[k+'_hit']+=i in actual
            groups[e['record'],tuple(map(tuple,d['moves'])),tuple(d['goal'][:2])][d['goal'][2]]=actual
            res.append(dict(record=e['record'],goal=d['goal'],moves=d['moves'],depth=depth,choices=choices,actual=sorted(actual),pools=stats))
    overlaps=[]
    for (r,m,p),goals in groups.items():
        for (a,A),(b,B) in combinations(goals.items(),2):
            if A and B:overlaps.append(dict(record=r,moves=m,prefix=p,targets=[a,b],common=sorted(A&B),ok=[sorted(A),sorted(B)]))
    print(tot,overlaps);prev.save(prev.out/'ramsey38_middle_depth_ablation.json',dict(verification_sha=prev.sha(R.read_bytes()),counts=dict(tot),overlaps=overlaps,results=res))
if __name__=='__main__':run()
