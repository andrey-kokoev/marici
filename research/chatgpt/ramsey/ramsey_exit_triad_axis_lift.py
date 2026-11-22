"""Lift the cyclic ordering (own exit, mate exit, unused exit) to S4 by fixing the entry apex. Compare a derived transport of frames with a symmetry of the selected strip."""
from ramsey_strip_diagonal_frame import cycle,m,r,X,P,D,json,permutations
from ramsey_first_fan_rim_probe import T,apex

def run():
    c=cycle(m);native=json.loads((D/'ramsey_three_rim_axes.json').read_text())['vertex_cycle'];rev={v:k for k,v in native.items()};out=[]
    for w in (c,[r[i] for i in c]):
        i=w.index(29);a,b=w[i-1],w[i+1];h,={P.index(k) for k in T[14]}-{a,b};blocks=[a,b,h];root=apex(w[0]);matches=[];stabs=[]
        for perm in permutations(range(1,5)):
            ex=[X.index(tuple(sorted(perm[x-1] for x in e))) for e in X];pd=lambda d:tuple(sorted(ex[k] for k in d));moved=[P.index(pd(d)) for d in P]+[15+T.index(tuple(sorted(map(pd,t)))) for t in T];
            if set(map(moved.__getitem__,w))==set(w) and any(moved[d]!=d and moved[moved[moved[d]]]==d for d in blocks):stabs.append(perm)
            if perm[root-1]==root and [moved[d] for d in blocks]==blocks[1:]+blocks[:1]:matches.append((perm,moved))
        (perm,moved),=matches;assert not stabs and moved[29]==29 and moved[0]!=0;bindings={}
        for p in permutations('ABCD'):
            if {p[0],p[3]}!={'A','B'}:continue
            f={p[k]:p[x-1] for k,x in enumerate(perm)};bindings[''.join(p)]='t' if f==native else 'inverse' if f==rev else 'other vertex axis'
        out.append(dict(exit_order=blocks,root=root,column_map=perm,new_entry=moved[0],binding=bindings))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_exit_triad_axis_lift.json').write_text(json.dumps(out)+'\n')
