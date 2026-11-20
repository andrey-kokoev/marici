"""T184 frame transport: move incidence, recompute the reader, compare to transported outputs. Distinguish symmetry of a triangulation from transport of an ordered chart."""
import json
from itertools import permutations,combinations,accumulate
from collections import Counter
from pathlib import Path
HOME=Path(__file__).resolve().parents[1];DATA=HOME/'results'
F=frozenset

def reader(v,u,edges,order):
    def z(x):return tuple(accumulate(x[i] for i in order))[:3]
    def mask(e):
        a,b=map(z,e);return F(i for i,(j,k) in enumerate(zip(a,b)) if j!=k)
    maxima=[e for e in edges if e<=v and len(mask(e))==3];c,=maxima;leaves=u-c
    contacts={w:F(i for i in c if F((w,i)) in edges) for w in leaves};red=F([c]+[F((w,i)) for w,h in contacts.items() if len(h)==1 for i in h]);return c,leaves,red

def main():
    data=json.loads((DATA/'esd7_explicit_analytical_census.json').read_text());coord={a['id']:tuple(a['barycentric']) for a in data['vertices']};names={v:k for k,v in coord.items()};vs=lambda a:F(coord[k] for k in a['vertices']);tets={vs(a) for a in data['tetrahedra']};v=vs(next(a for a in data['tetrahedra'] if a['id']=='T184'));u=F.union(*(q for q in tets if len(q&v)>=3));assert len(u)==8;edges={vs(a) for a in data['edges'] if vs(a)<=u};order=tuple(range(4));c,l,r=reader(v,u,edges,order);counts=Counter();rows=[];bad=None;orbit=Counter()
    for p in permutations(order):
        # p sends old barycentric slot i to new slot p[i].
        def g(x):return tuple(x[p.index(i)] for i in order)
        def G(s):return F(map(g,s))
        V,U,E=G(v),G(u),set(map(G,edges));expect=G(c),G(l),F(map(G,r));assert V==v
        assert reader(V,U,E,p)==expect;counts['transported_chart_matches']+=1
        common={vs(a) for a in data['edges'] if vs(a)<=U};local=(U==u and E==edges);global_ok=set(map(G,tets))==tets
        actual=reader(V,U,E,order);edge_ok=actual[0]==expect[0];all_ok=actual==expect;orbit[tuple(sorted(names[x] for x in expect[0]))]+=1
        if local:counts['local_symmetries']+=1;counts['local_same_output']+=int(all_ok)
        if global_ok:counts['global_symmetries']+=1;counts['global_same_output']+=int(all_ok);assert local
        if global_ok and not all_ok and bad is None:bad=dict(permutation=p,transported_pair=sorted(names[x] for x in expect[0]),reread_pair=sorted(names[x] for x in actual[0]))
        rows.append(dict(p=p,local=local,global_ok=global_ok,pair_ok=edge_ok,same_fixed_chart_output=all_ok));counts['all_frames_fixed_order_pair']+=int(edge_ok);counts['all_frames_fixed_order_output']+=int(all_ok)
    print(dict(counts),bad,sorted(orbit.items()));(DATA/'ramsey_t184_frame_transport.json').write_text(json.dumps(dict(counts=counts,counterexample=bad,transported_pair_orbit=[dict(pair=e,count=k) for e,k in sorted(orbit.items())],cases=rows),indent=2)+'\n')
if __name__=='__main__':main()
