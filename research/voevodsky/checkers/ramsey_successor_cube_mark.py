"""A shared edge selects a diagonal port in either realization. Test, do not assume, red."""
from itertools import product
from collections import Counter
import json
from ramsey_cube_diagonal_pairs import profile,analyze,D


def audit():
    tab=analyze(10);upper=sorted(list(map(tuple,tab['leftover']))+[tuple(r) for p in tab['pieces'] for r in p['new']]);flip=lambda r:tuple(11-i for i in reversed(r));sheet={'upper':upper,'mirror':list(map(flip,reversed(upper)))};starts=[tuple(p['start']) for p in tab['pieces']];halves={'upper':starts,'mirror':[tuple(10-i for i in reversed(t)) for t in reversed(starts)]};counts=Counter();trials=Counter();example=None;records=[]
    for t in json.loads((D/'ramsey_cube_diagonal_colors.json').read_text())['records']:
        half=t['half'];start=tuple(t['start']);order=halves[half];idx=order.index(start);sq=tuple(map(tuple,t['square']));diags=[tuple(map(tuple,d)) for d in t['diagonals']];opp=set(diags[0]+diags[1]);last=max(sheet[half].index(r) for r in opp|set(sq));common=set(map(tuple,t['common_rows']));c=set(map(tuple,t['cycle']));pf=[profile(sq,d,c,common)[1] for d in diags];seen=set();marks=[];attempts=0;controls=set()
        for j,a in enumerate(order):
            corners=set(product(*[(v,v+1) for v in a]));fresh=corners-seen;seen|=corners
            edge=corners&opp
            if j<=idx or len(edge)!=2 or len(set.intersection(*map(set,edge)))!=2:continue
            targets=[next(i for i,r in enumerate(d) if r in edge) for d in diags]
            for r in common:
                if r not in sheet[half] or sheet[half].index(r)<=last:continue
                vals=[any(m&(1<<(15+i)) for m in masks[r]) for masks,i in zip(pf,targets)]
                if vals[0]!=vals[1]:controls.add((a,r,diags[vals.index(True)][targets[vals.index(True)]]))
            for r in sorted(fresh):
                attempts+=1;legal=r in common;yes=[legal and any(m&(1<<(15+i)) for m in masks[r]) for masks,i in zip(pf,targets)];trials[legal,sum(map(bool,yes))]+=1
                if yes[0]!=yes[1]:
                    mark=dict(successor=a,shared_edge=sorted(edge),probe=r,targets=[d[i] for d,i in zip(diags,targets)],accepts=yes.index(True),next_cube=j==idx+1,later_row=sheet[half].index(r)>last);marks.append(mark)
                    if example is None:example=dict(half=half,start=start,square=sq,cycle=sorted(c),**mark)
        counts['later_row_control']+=bool(controls);counts['cases']+=1;counts['has_marked_trial']+=bool(attempts);counts['distinguished']+=bool(marks);counts['next_cube_distinguished']+=any(m['next_cube'] for m in marks);counts['later_row_distinguished']+=any(m['later_row'] for m in marks);records.append(dict(half=half,start=start,square=sq,attempts=attempts,witnesses=marks,control_examples=sorted(controls)[:1]))
    result=dict(counts=counts,trials={str(k):v for k,v in trials.items()},example=example,records=records);print(counts,trials,example);(D/'ramsey_successor_cube_mark.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':audit()
