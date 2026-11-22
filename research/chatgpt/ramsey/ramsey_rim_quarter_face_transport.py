"""Use one recorded rim step, not an external S4 relabeling, to rotate the two face tags. Test preservation of the selected Hall component and of the native arrow registry independently."""
from ramsey_strip_diagonal_frame import cycle,m,r,X,P,orient,frame,D,json,permutations
from ramsey_first_fan_rim_probe import T

def run():
    c=cycle(m);native={'AB','BA','BC','CA','AD','DB'};out=[]
    for w in (c,[r[i] for i in c]):
        d=w[::2];fixed,moving=frame(d,X);succ=dict(s['arrow'] for s in orient(d,X)[:4]);fac=lambda e,f:[sorted((*e,x)) for x in f];tag=fac(fixed,moving);turn=lambda e:tuple(succ[x] for x in e);new=fac(turn(fixed),turn(moving));assert set(turn(fixed))==set(moving) and set(turn(moving))==set(fixed);assert len(set(map(tuple,tag+new)))==4
        def hall(f):
            ex=[X.index(tuple(sorted(f[x] for x in e))) for e in X];image=lambda u:tuple(sorted(ex[i] for i in u));return [P.index(image(u)) for u in P]+[15+T.index(tuple(sorted(image(u) for u in t))) for t in T]
        h=hall(succ);swaps=[]
        for p in permutations(range(1,5)):
            f=dict(zip(range(1,5),p));img=hall(f);
            if {f[x] for x in fixed}==set(moving) and {img[x] for x in w}==set(w):swaps.append(p)
        assert not swaps
        reports=[]
        for p in permutations('ABCD'):
            if {p[0],p[3]}!={'A','B'}:continue
            g={p[i-1]:p[succ[i]-1] for i in succ};missing={g[e[0]]+g[e[1]] for e in native}-native;assert {'CD','DC'}<=missing;reports.append(dict(binding=''.join(p),absent=sorted(missing)))
        out.append(dict(rim=succ,faces=tag,rotated_faces=new,rotated_cycle=[h[x] for x in w],common_visits=len(set(w)&{h[x] for x in w}),diagonal_exchanging_component_symmetries=swaps,registry_controls=reports))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_rim_quarter_face_transport.json').write_text(json.dumps(out)+'\n')
