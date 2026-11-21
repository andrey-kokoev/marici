"""Test the added bridge preserving orientation of the flag-read square rim to the uncancelled native face boundary. No pole, graph color or native endpoint name used to select a binding."""
from ramsey_flag_triangle_probe import roles,flags,D,json,permutations
from collections import Counter

def run():
    native=json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text());faces=native['retained_face_cycles'];occ=Counter((u,v) for f in faces for u,v in zip(f,f[1:]));rim={e for e in occ if e[::-1] not in occ};seam={e for e in occ if e[::-1] in occ};b,q,r,m=roles(flags[0]);assert roles(flags[1])==(b,q,m,r);walk=(b,r,q,m,b);out=[]
    for p in permutations(native['vertex_labels']):
        path=[p[i] for i in walk];rr=set(zip(path,path[1:]));
        if rr not in (rim,{e[::-1] for e in rim}):continue
        # Require the two selected triangle supports to be the actual faces.
        data=[]
        for i in (r,m):
            candidates=[f for f in faces if set(f)=={p[b],p[q],p[i]}];
            if len(candidates)!=1:break
            f,=candidates;(s,t),=seam.intersection(zip(f,f[1:]));data.append(dict(apex=p[i],seam=s+t,role='arrival' if t==p[b] else 'departure'))
        if len(data)==2:out.append(dict(binding=''.join(p),preserves=rr==rim,walk=''.join(path),rows=data))
    assert len(out)==4 and all([r['role'] for r in x['rows']]==(['arrival','departure'] if x['preserves'] else ['departure','arrival']) for x in out);return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_directed_rim_binding.json').write_text(json.dumps(out)+'\n')
