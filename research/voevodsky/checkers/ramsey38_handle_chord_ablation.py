"""Compare alternating rim endpoints with planar rotations on every partial link."""
from ramsey38_partial_handle import planar,prev,json,combinations,faces,Counter

def cycle(rim):
    adj={}
    for a,b in rim:adj.setdefault(a,[]).append(b);adj.setdefault(b,[]).append(a)
    assert all(len(n)==2 for n in adj.values());order=[min(adj),min(adj[min(adj)])]
    while True:
        nxt,=set(adj[order[-1]])-{order[-2]}
        if nxt==order[0]:break
        assert nxt not in order;order.append(nxt)
    assert len(order)==len(adj);return order

def crossing(fs,order):
    es=sorted({tuple(sorted(e,key=order.index)) for f in fs for e in combinations(f,2) if set(e)<=set(order)},key=lambda e:order.index(e[0]))
    for (a,b),(c,d) in combinations(es,2):
        if order.index(a)<order.index(c)<order.index(b)<order.index(d):return [[a,b],[c,d]]

def run():
    rows=[];total=Counter()
    for z in json.loads((prev.out/'ramsey38_partial_handle.json').read_text())['cases']:
        rim=z['rim'];order=cycle(rim);cap={frozenset(e+[0]) for e in rim};fixed=set(map(frozenset,z['fixed']));opts=sorted(set(map(frozenset,z['triangles']))-fixed,key=sorted);cnt=Counter();first={};all_on_rim=all(t<=set(order) for t in fixed|set(opts))
        for k in range(len(opts)+1):
            for q in combinations(opts,k):
                fs=fixed|set(q);cross=crossing(fs,order);ok=planar(frozenset(fs|cap));assert not(ok and cross)
                kind='cross' if cross else 'pass' if ok else 'planarity_only';cnt[kind]+=1
                first.setdefault(kind,dict(k=k,optional=faces(q),chords=cross))
        assert min(first[t]['k'] for t in first if t!='pass')==z['relative']['k'];print(z['vertex'],order,cnt,first.get('planarity_only'),flush=True);rows.append(dict(row=z['row'],vertex=z['vertex'],tip=z['tip'],bd=z['bd'],order=order,all_on_rim=all_on_rim,counts=dict(cnt),first=first));total.update(cnt)
    prev.save(prev.out/'ramsey38_handle_chord_ablation.json',dict(counts=dict(total),cases=rows));print(total)
if __name__=='__main__':run()
