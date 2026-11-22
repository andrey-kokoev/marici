"""Fix the literal swap and both boundary flags, but no C5, decagon or global polarity. Find counterexamples, recording full matchings and the actual boundary component. Test matching polarity by three-edge paths using the established exhaustive class criterion."""
from ramsey_row_quotient_constructor import R,move,flags,final
from ramsey_history_matching_provenance import enum,D,json

def run():
    rows=[]
    for m in enum():
        if not {(0,16),(7,29)}<=m:continue
        n=move(m,R);u=flags-(m|n);adj={x:set() for x in range(30)}
        for x,y in u:adj[x].add(y);adj[y].add(x)
        paths=[];ends=set()
        for x in adj:
            if len(adj[x])!=1 or x in ends:continue
            w=[x];prev=None
            while adj[w[-1]]-{prev}:prev,z=w[-1],next(iter(adj[w[-1]]-{prev}));w.append(z)
            paths.append(w);ends.update((x,w[-1]))
        z=0;w=[z];a=dict(m);b={y:x for x,y in n}
        while True:
            w.extend([a[z],b[a[z]]]);z=w[-1]
            if not z:break
        rows.append(dict(matching=sorted(m),lengths=sorted(len(p)-1 for p in paths),entry_cycle=w,exit_thread=next((p for p in paths if 29 in (p[0],p[-1])),None),selected=m in final))
    return rows
if __name__=='__main__':
    from collections import Counter
    out=run();print(len(out),Counter(tuple(r['lengths']) for r in out));print([(r['entry_cycle'],r['exit_thread'],r['selected']) for r in out]);(D/'ramsey_literal_swap_polarity_controls.json').write_text(json.dumps(out)+'\n')
