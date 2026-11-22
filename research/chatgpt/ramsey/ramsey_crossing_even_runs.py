"""Extract the residual ring directly from incidences; count extensions by matching runs, without enumerating Hall matchings. Cross-check every exact observation pattern including multiplicity zero."""
from itertools import combinations
from collections import Counter
from ramsey_folded_entry_handoff import P,T,D,json

def run():
    q=json.loads((D/'ramsey_open_shortcut_constructor.json').read_text())['marked'];w=set(q['cycle']);adj={x:set() for x in range(30)}
    for j,t in enumerate(T,15):
        for e in t:i=P.index(e);adj[i].add(j);adj[j].add(i)
    site={};internal=set()
    for j,d,k,x in q['paths']:
        internal.update((d,k));a,=adj[d]-{j,k};b,=adj[k]-{x,d};site[a]=site[b]=j
    ring=set(adj)-w-internal;assert set(site)==ring and all(len(adj[x]&ring)==2 for x in ring);r=[min(ring)];y=min(adj[r[0]]&ring)
    while y!=r[0]:r.append(y);y,=(adj[y]&ring)-{r[-2]}
    labels=[site[x] for x in r];assert len(r)==10 and labels[:5]==labels[5:];p=q['cycle'][1::2];assert any(labels[:5]==v[i:]+v[:i] for v in [p,p[::-1]] for i in range(5));out=[];prior=Counter(tuple(v) for v in json.loads((D/'ramsey_minimal_crossing_receipts.json').read_text())['all']['patterns'])
    for n in range(6):
        for opened in combinations(sorted(p),n):
            if not opened:ways=2
            else:
                i=labels.index(opened[0]);runs=''.join('0' if j in opened else '1' for j in (labels[i:]+labels[:i])).split('0');ways=int(all(len(s)%2==0 for s in runs))
            assert ways==prior[opened];out.append(dict(opened=opened,ways=ways))
    return dict(ring=r,site_labels=labels,patterns=out)
if __name__=='__main__':
    out=run();print(out['ring'],out['site_labels']);(D/'ramsey_crossing_even_runs.json').write_text(json.dumps(out)+'\n')
