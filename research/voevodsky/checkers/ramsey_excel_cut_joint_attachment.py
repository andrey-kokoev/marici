"""Source cut-difference vs joint legality in a declared width-seven graph chart."""
from collections import defaultdict,Counter
from itertools import combinations
from pathlib import Path
import json
from ramsey_excel_signed_cut import read_pair

rows=list(s for s in combinations(range(1,8),3) if min(s[1]-s[0],s[2]-s[1])>=2)

def obstruction(ss):
    n=7+len(ss);red={(i,i+1) for i in range(1,7)}|{(i,k) for k,s in enumerate(ss,8) for i in s};vertices=range(1,n+1)
    for size,color in [(3,True),(7,False)]:
        for q in combinations(vertices,size):
            if all((e in red)==color for e in combinations(q,2)):return q
    return None

def run():
    from functools import lru_cache
    check=lru_cache(None)(obstruction);bins=defaultdict(list);controls=Counter();first=None;ind=[s for s in combinations(range(1,8),3) if min(s[1]-s[0],s[2]-s[1])>=2]
    for a,b in combinations(rows,2):
        if sum(abs(i-j) for i,j in zip(a,b))!=1:continue
        key=tuple(read_pair(a,b)['prefix']['red']);bins[key].append((a,b))
    for key,parents in bins.items():
        for s,t in combinations(rows,2):
            batch=[]
            for p in parents:
                assert not check(p);single=tuple(check(tuple(sorted((*p,x)))) is None for x in (s,t));q=check(tuple(sorted((*p,s,t))));free=[u for u in ind if not (set(u)&set(p[0]) or set(u)&set(p[1]))];pred=not any(set(u).isdisjoint(s) and set(u).isdisjoint(t) for u in free)
                assert pred==(q is None);controls['joint_graph_checks']+=1;controls['joint_failures']+=int(q is not None)
                if len(set((*p,s,t)))==4:
                    controls['four_distinct_checks']+=1;controls['four_distinct_failures']+=int(q is not None)
                batch.append((p,single,q is None))
            for (p,ok,v),(q,ok2,w) in combinations(batch,2):
                if ok==ok2==(True,True) and v!=w:
                    controls['matched_single_legal_contrasts']+=1
                    if first is None or (len(set((*p,*q,s,t))),-key.index(1))>first[0]:
                        good,bad=(p,q) if v else (q,p);first=((len(set((*p,*q,s,t))),-key.index(1)),dict(cut=key.index(1)+1,legal=good,illegal=bad,attachments=[s,t],blue_seven=obstruction((*bad,s,t))))
    print(controls,first);d=Path(__file__).resolve().parents[1]/'results/ramsey_excel_cut_joint_attachment.json';d.write_text(json.dumps(dict(scope='Red path, four blue-to-each-other ports; distinct exterior support rows, fixed port labels; repeated interior/exterior supports permitted.',counts=controls,example=first[1] if first else None),indent=2)+'\n')
if __name__=='__main__':run()
