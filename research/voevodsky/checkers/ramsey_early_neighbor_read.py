"""Can a permanent earlier port tell which marked 35x row to use?"""
from ramsey_cube_diagonal_pairs import analyze,charts,profile,independent_sets,D
from itertools import product
from collections import Counter
import json


def audit():
    sq=((1,4,8),(1,4,9),(1,5,8),(1,5,9));diag=((2,4,9),(2,5,8));t=analyze(10);sheet=sorted(list(map(tuple,t['leftover']))+[tuple(r) for p in t['pieces'] for r in p['new']]);corners=set(sq)|{(2,j,k) for j in (4,5) for k in (8,9)};earlier=[r for r in sheet if r<(3,5,7) and r not in corners];late=[r for r in earlier if r>max(corners)];cs=next(cs for s,_,cs in charts() if s==sq);obs={r:[] for r in earlier};joint={r:[] for r in earlier};suffixes=[]
    for c in cs:
        z,=[j if i==2 else i for i,j in c if 2 in (i,j) and 3 not in (i,j)];suffixes.append(z);q=(3,5,z);g,m=profile(sq,diag,c,earlier+([q] if z>6 else []));five=independent_sets(16,g,5)
        for r in earlier:
            obs[r].append(r in m);joint[r].append(any(n&(1<<15) and (not (a&n) or all((a|n)&s for s in five)) for a,n in product(m.get(r,()),m.get(q,()))))
    report=[]
    for r in earlier:
        if any(obs[r]):report.append(dict(row=r,after_cube=r in late,positive=sorted({z for z,p in zip(suffixes,obs[r]) if p}),retained=sorted({z for z,p in zip(suffixes,joint[r]) if p}),obs=obs[r],joint=joint[r]))
    classes={}
    for region,rs in [('after_cube',late),('all_earlier',earlier)]:
        classes[region]=[[r for r in rs if obs[r][i]] for i in range(len(cs))]
    res=dict(cycle_order=[sorted(c) for c in cs],neighbors=suffixes,rows=report,available_by_cycle=classes);(D/'ramsey_early_neighbor_read.json').write_text(json.dumps(res,indent=2)+'\n');print(suffixes);print(classes);print(report)
if __name__=='__main__':audit()
