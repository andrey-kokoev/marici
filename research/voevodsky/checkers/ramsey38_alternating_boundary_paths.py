"""A filled quadrilateral with disjoint alternating boundary bridges on opposite sides.
The conclusion uses linking in the doubled ball, not an assumption that its disk is proper.
Replay on record 3 AFTER the frozen predictions; not a new prospective test.
"""
from itertools import permutations,combinations
from collections import Counter
import json
from ramsey38_record3_polygon_trial import rows,pf,cf
from ramsey38_global_shell import sub

def find(required,boundary_faces):
    E=set.union(set(),*(sub(s,2) for s in boundary_faces));edges=set.union(set(),*(sub(s,2) for s in required));tri=set.union(set(),*(sub(s,3) for s in required));P=set.union(set(),*required)
    for a,b,c,d in permutations(sorted(P),4):
        if a!=min(a,b,c,d) or b>d:continue
        f=lambda *x:frozenset(x)
        if not {f(a,b),f(b,c),f(c,d),f(d,a)}<=E:continue
        if not ({f(a,b,c),f(a,c,d)}<=tri or {f(a,b,d),f(b,c,d)}<=tri):continue
        rest=P-{a,b,c,d}
        for x,y in permutations(rest,2):
            if {f(a,x),f(x,c),f(b,y),f(y,d)}<=E:
                for k in range(len(rest)-1):
                    for m in permutations(rest-{x,y},k):
                        path=(x,)+m+(y,)
                        if all(f(u,v) in edges for u,v in zip(path,path[1:])):return (a,b,c,d),path

if __name__=='__main__':
    saved=json.loads(pf.read_text())['predictions'];comp=json.loads(cf.read_text());counts=Counter();shell_hits=[];array_hits=[]
    for root,ds in saved.items():
        r=rows(int(root));req=set(r.values());cert=comp['certificates'][root]
        for drop,entry in ds.items():
            if entry['class']!='original':continue
            boundary=[s for v,s in r.items() if v!=int(drop) and len(s)<4];a=find(req,boundary);b=find(req|set(map(frozenset,entry['shell'])),list(map(frozenset,entry['shell'])))
            if a:
                assert drop not in cert and '0' not in cert;array_hits.append((root,drop,a))
            if b:shell_hits.append((root,drop,b))
    print('array obstructions',array_hits);print('additional fixed-shell coverage (includes array case)',shell_hits)
