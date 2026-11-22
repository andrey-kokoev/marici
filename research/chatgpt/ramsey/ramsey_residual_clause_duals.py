"""Test the selected polarity first. Search all type-preserving and type-reversing Hall symmetries for a genuine exchange of the two residual handoff cases, distinguishing exchange of whole fills from exchange of marked fans."""
from itertools import permutations
from collections import Counter
from ramsey_antipode_extension import run as polarity
from ramsey_row_quotient_constructor import action,move,R
from ramsey_folded_entry_handoff import D,json

def run():
    rows=json.loads((D/'ramsey_residual_fan_reading.json').read_text());u=[frozenset(tuple(e['flag']) for e in q['extra']) for q in rows];lab=[q['extra'][0]['reading'] for q in rows];a,b=[i for i,s in enumerate(lab) if s=='handoff'];base=frozenset([(9,26),(14,15)]);f=polarity()[0]['map'];counts=Counter();examples=[]
    for p in permutations(range(6)):
        h=action(p)
        for dual in (False,True):
            g=[h[f[x] if dual else x] for x in range(30)];im=lambda s:move(s,g)
            if im(u[a])!=u[b] or im(u[b])!=u[a]:continue
            counts[dual,'extras']+=1
            if im(base)!=base:continue
            counts[dual,'base']+=1;images=[u.index(im(s)) if im(s) in u else None for s in u];pres=all(j is not None and lab[j]==lab[i] for i,j in enumerate(images));
            if pres:counts[dual,'classes']+=1
            examples.append(dict(dual=dual,involution=all(g[g[i]]==i for i in range(30)),images=images,letter_action=p,poles=[g[0],g[29]]))
    paths=[q['path'] for q in rows];route_images=[]
    for w in paths:
        v=[f[x] for x in reversed(w)];i,=[i for i,z in enumerate(paths) if z==v or z==[R[x] for x in v]];route_images.append(i)
    assert all(move(u[i],f)==u[j] for i,j in enumerate(route_images));return dict(route_images=route_images,polarity_images=[sorted(move(s,f)) for s in [base,u[a],u[b]]],counts={str(k):v for k,v in counts.items()},examples=examples)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_residual_clause_duals.json').write_text(json.dumps(out)+'\n')
