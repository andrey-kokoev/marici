"""Group common quartet choices by the same two labeled pentagons before installation."""
from collections import defaultdict,Counter
import json
from ramsey_quartet_last_choice import decode
from ramsey_quartet_live_probe import configs,attach
from ramsey_inherited_swap_selector import D


def audit():
    src=json.loads((D/'ramsey_quartet_live_probe.json').read_text());groups=defaultdict(list)
    for t in src['records']:
        sq=tuple(map(tuple,t['square']));rs=tuple(map(tuple,t['quartet']));cs=tuple(sorted(decode(sq,rs)[3]));opts=[]
        for kind in ('live','joint_only'):
            for a in t[kind]:
                i=cs.index(tuple(map(tuple,a['cycle'])));es=tuple(map(tuple,a['quartet_links']));r=tuple(a['row']);ss=[[st for st in configs(sq,rs,c) if st[1]==es] for c in cs];assert all(ss) and attach(sq,rs,r,ss[i]) and not attach(sq,rs,r,ss[1-i]);opts.append(dict(kind=kind,accepts=i,row=r,repairs=[(rs[x-15],rs[y-15]) for x,y in es],fifth_links=[rs[x-15] for x in a['probe_links']]))
        groups[sq,cs].append(dict(rows=rs,moves=opts))
    hist=Counter();out=[]
    for (sq,cs),qs in sorted(groups.items()):
        good=[q for q in qs if q['moves']];dead=[q for q in qs if not q['moves']];directions={m['accepts'] for q in good for m in q['moves']};hist[len(qs),len(good),len(directions)]+=1;out.append(dict(square=sq,cycles=cs,common=len(qs),readable=len(good),accepting_directions=sorted(directions),choices=qs))
    print(hist);print([(t['square'],t['common'],t['readable'],t['accepting_directions']) for t in out]);(D/'ramsey_plan_later_read.json').write_text(json.dumps(dict(families={str(k):v for k,v in hist.items()},plans=out),indent=2)+'\n')
if __name__=='__main__':audit()
