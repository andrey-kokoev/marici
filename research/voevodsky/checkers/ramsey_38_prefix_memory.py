"""Exhaust middle cycles in the pools of the joint-frontier certificates, not all choices of pools. Count distinct middle completions, not triangulations. Permit either reading direction from the fixed first Z. Group live histories by identical opening edge, used sites, and current oriented edge. Check for absence of any common winning next move."""
from ramsey_38_joint_annuli import load,zipone,boundaries,D
from collections import defaultdict,Counter
from itertools import permutations
import json
rows=load('ramsey_38_joint_frontier');rings=load('ramsey_38_correction_continuation');out=[]
for r,data in zip(rows,rings):
    I=r['ring'];U=sorted(r['last']);Z=data['Z'];W=sorted(set(r['middle'])-set(Z));stats=defaultdict(Counter);raw=Counter()
    for M in boundaries(Z,W):
        fit=bool(zipone(I,M));win=fit and any(zipone(M,[U[0],*t]) for t in permutations(U[1:]) if t[0]<t[-1]);raw['circles']+=1;raw['inner']+=fit;raw['both']+=win
        for seq in (M,[M[0],*M[:0:-1]]):
            for k in range(3,len(seq)+1):
                s=stats[tuple(seq[:k])];s['inner']+=fit;s['both']+=win
    assert raw['both'];children=defaultdict(dict)
    for pref,c in stats.items():children[pref[:-1]][pref[-1]]=dict(c)
    live=lambda opts:{v for v,s in opts.items() if s['both']};groups=defaultdict(list);mixed=[];branch=[]
    for pre,opt in children.items():
        if not live(opt):continue
        groups[(pre[:2],frozenset(pre),pre[-2:])].append((pre,live(opt))); 
        if len(live(opt))>1:branch.append(pre)
        if any(s['inner']>0 and not s['both'] for s in opt.values()):mixed.append(pre)
    obstruction=None
    for entries in sorted(groups.values(),key=lambda ls:len(ls[0][0])):
        if not set.intersection(*(s for _,s in entries)):
            obstruction=[dict(prefix=p,next=sorted(s)) for p,s in entries];break
    def example(ls):
        if ls:
            p=min(ls,key=lambda p:(len(p),p));return dict(prefix=p,next=children[p])
    tests={}
    for name,key in [('edge',lambda p:p[-2:]),('edge_depth',lambda p:(p[-2:],len(p))),('edge_used',lambda p:(p[-2:],frozenset(p))),('opening_edge_used',lambda p:(p[:2],p[-2:],frozenset(p)))]:
        bucket=defaultdict(list)
        for p,opt in children.items():
            if live(opt):bucket[key(p)].append(live(opt))
        tests[name]=dict(merged=sum(len(ls)>1 for ls in bucket.values()),conflicts=sum(not set.intersection(*ls) for ls in bucket.values()))
    out.append(dict(memory_tests=tests,poles=r['poles'],ring=I,pools=[Z,W,U],counts=raw,branch=example(branch),dead_alternative=example(mixed),memory_obstruction=obstruction));
print({key:sum(bool(r[key]) for r in out) for key in ['branch','dead_alternative','memory_obstruction']});print(out[0]);print(next((x['memory_obstruction'] for x in out if x['memory_obstruction']),None));(D/'ramsey_38_prefix_memory.json').write_text(json.dumps(out,indent=2)+'\n')
