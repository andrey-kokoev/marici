"""Frozen shared-row signed swap comparison. Graph loaded after labels are fixed."""
from itertools import product, combinations, permutations
from collections import defaultdict, Counter
import json,runpy
from ramsey_excel_corner_collisions import cube,local,analyze,D


def audit():
    cells=[''.join(c) for c in product('01*',repeat=3) if c!=('*',)*3];oc=defaultdict(list)
    for z in analyze(9)['pieces']:
        a=tuple(z['start'])
        for r in cube(a):
            b=local(a,r)
            for s in cells:
                if all(x=='*' or int(x)==y for x,y in zip(s,b)):oc[s].append((tuple(r),a,b))
    tags={};witness={}
    for s,t in combinations(cells,2):
        if not any(x!='*' and y!='*' and x!=y for x,y in zip(s,t)):continue
        signs=set()
        for r,a,b in oc[s]:
            for q,h,f in oc[t]:
                if r!=q:continue
                for i in range(3):
                    if s[i]==t[i]=='*':
                        tag='same' if b[i]==f[i] else 'opposite';signs.add(tag);witness.setdefault((s,t,tag),dict(row=r,starts=[a,h],axis=i+1,steps=[1-2*b[i],1-2*f[i]]))
        tags[s,t]='+'.join(sorted(signs)) or 'neither'
    g=runpy.run_path(str(D/'ramsey_cube_construct35.py'));assert cells==g['cells'];E=[(s,t) for i,s in enumerate(cells) for j,t in enumerate(cells[i+1:],i+1) if g['G'][i]>>j&1];orb={}
    for p in permutations(range(3)):
        for b in product(range(2),repeat=3):
            def f(s):return ''.join('*' if s[i]=='*' else str(int(s[i])^k) for i,k in zip(p,b))
            e=frozenset(frozenset((f(s),f(t))) for s,t in E);orb.setdefault(e,(p,b))
    assert len(orb)==8;by=defaultdict(Counter);ex={}
    for pair,tag in sorted(tags.items()):
        yes=[v for e,v in orb.items() if frozenset(pair) in e];no=[v for e,v in orb.items() if frozenset(pair) not in e];by[tag][len(yes)]+=1
        if tag=='opposite':ex[tag]=dict(cells=pair,occurrence=witness[*pair,tag],red_completions=len(yes))
        if yes and no and tag!='neither':ex.setdefault(tag,dict(cells=pair,occurrences=[witness[*pair,k] for k in tag.split('+')],red_transform=yes[0],blue_transform=no[0]))
    out=dict(pairs_by_number_of_red_completions=by,examples=ex,transform='Output coordinate j reads input coordinate p[j] XOR b[j]; p is zero-based.');print(out);(D.parent/'results/ramsey_same_row_swap.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
