"""Controlled third-cut test on a previously rejected row. Predict a cut using only the OLD blocking cliques, then check the new cliques from scratch."""
import json
from itertools import combinations
from collections import Counter
from ramsey_cube_retention_floor import induced,G,D
from ramsey_cube_path_unlock import solve

def prepare(a,cuts,s):
    b=a[:];
    for i,j in cuts:b[i]^=1<<j;b[j]^=1<<i
    deg=[v.bit_count()+(s>>i&1) for i,v in enumerate(b)];es=[(i,j) for i,j in combinations(range(26),2) if (i,j) not in cuts and not b[i]&((1<<j)|b[j]) and max(deg[i],deg[j])<7 and not(s>>i&s>>j&1)];return b,deg,es

def demands(b,s):
    I=[0]
    for j,v in enumerate(b):I.extend([x|1<<j for x in I if not x&v]);
    return [x for x in I if x.bit_count()==8 or x.bit_count()==7 and not x&s]

def probe(a,cuts,s,qs=None):
    b,deg,es=prepare(a,cuts,s);qs=demands(b,s) if qs is None else qs;mask=[1<<i|1<<j for i,j in es];dem=set(tuple(e for e,z in zip(es,mask) if q&z==z) for q in qs);forced={d[0] for d in dem if len(d)==1};g=b[:]
    for i,j in forced:g[i]|=1<<j;g[j]|=1<<i
    over=[j for j,v in enumerate(g) if v.bit_count()+(s>>j&1)>7];tri=any(g[i]&g[j] for i,j in forced);return b,dem,forced,over,tri

def experiment():
    prior=json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text());a=induced(G,prior['core_labels']);# select first documented cut pair exhibiting a degree-only conflict, then first qualifying degree-seven row
    for rr in prior['runs']:
        if not rr['counts'].get('forced_degree'):continue
        cuts=list(map(tuple,rr['cuts']));b,_,_=prepare(a,cuts,0);I=[0]
        for j,v in enumerate(b):I.extend([x|1<<j for x in I if not x&v]);
        for s in sorted(I):
            if s.bit_count()!=7 or any(s>>i&1 and v.bit_count()==7 for i,v in enumerate(b)):continue
            qs=demands(b,s);_,ds,forced,over,tri=probe(a,cuts,s,qs)
            if () not in ds and over and not tri:break
        else:continue
        break
    else:raise AssertionError('no control')
    def exact(bb,dd):
        small=[]
        for d in sorted(dd,key=lambda x:(len(x),x)):
            st=set(d)
            if not any(v<=st for v in small):small.append(st)
        return solve(bb,small,s)
    counts=Counter();cases=[];win=None
    for e in combinations(range(26),2):
        i,j=e
        if not b[i]>>j&1:continue
        counts['all_third_cuts']+=1;cut=cuts+[e];bb,old,ff,oo,tt=probe(a,cut,s,qs)
        if oo or tt or () in old:continue
        counts['old_forced_conflicts_clear']+=1;released=sorted(forced-ff);newqs=demands(bb,s);_,new,nf,no,nt=probe(a,cut,s,newqs);repaired=not(no or nt or () in new);counts['new_forced_conflicts_clear']+=repaired;adds=exact(bb,new) if repaired else None;counts['true_completion']+=adds is not None
        if adds is not None:win=dict(remove=cut,add=adds,s=s)
        closure=[]
        if repaired:
            g=bb[:];todo=set(new)
            while todo:
                todo={tuple((i,j) for i,j in d if not g[i]&g[j] and g[i].bit_count()+(s>>i&1)<7 and g[j].bit_count()+(s>>j&1)<7) for d in todo};ff={d[0] for d in todo if len(d)==1};closure.append(dict(unavailable=() in todo,forced=sorted(ff)))
                if () in todo or not ff:break
                todo={d for d in todo if not ff.intersection(d)}
                for i,j in ff:g[i]|=1<<j;g[j]|=1<<i
                if any(g[i]&g[j] for i,j in ff) or any(v.bit_count()+(s>>i&1)>7 for i,v in enumerate(g)):
                    closure.append(dict(conflict=True));break
        cases.append(dict(third=e,closure=closure,released= released,new_cliques=len(set(newqs)-set(qs)),dead=sum(all(not all(q>>v&1 for v in edge) for edge in prepare(a,cut,s)[2]) for q in set(newqs)-set(qs)),overfull=no,triangle=nt))
    out=dict(cuts=cuts,row=[j for j in range(26) if s>>j&1],old_overfull=over,old_forced=sorted(forced),counts=counts,passes=cases,witness=win);print(out);(D.parent/'ramsey_cube_degree_release.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':experiment()
