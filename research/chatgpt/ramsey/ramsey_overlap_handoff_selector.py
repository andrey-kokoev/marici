"""Select by a consecutive apex-to-apex transition, not by desired sewing base. Verify cyclic and based uniqueness, then apply the unmodified mark reader."""
from ramsey_overlap_triangle_execution import orient,cycle,m,r,P,X,D,json,permutations,validate,execute,registry,normalize
from check_seed_typed_execution import tours
from check_seed_tour_family_transport import seam,marked_reader

def select(t,h):
    hits=[]
    for w in tours:
        for k in range(6):
            s=w[k:]+w[:k];u,v=s[2:4];assert u[1]==v[0]
            if u[0]!=t or v[1]!=h:continue
            assert s[0][0]==s[2][1]==s[3][0]==s[-1][1] and set(s)==set(registry);assert all(s[j][1]==s[j+1][0] for j in range(5));hits.append(s)
    s,=hits;return validate(execute(s))

def run():
    ds=cycle(m)[::2];records=[]
    for p in permutations('ABCD'):
        if {p[0],p[-1]}!={'A','B'}:continue
        pair=[];rho=dict(zip(p,(p[0],p[2],p[1],p[3])))
        for d in (ds,[r[i] for i in ds]):
            t,h=(p[i-1] for i in orient(d,X)[-1]['arrow']);path=select(t,h);s=tuple(e[3] for e in path);anti=normalize(tuple(rho[e[1]]+rho[e[0]] for e in reversed(s)));assert anti==normalize(s);pair.append(dict(order=t+h,word=s,seam=seam(path),bit=marked_reader(path,p[0])))
        assert pair[0]['seam']!=pair[1]['seam'];records.append(dict(binding=''.join(p),rows=pair))
    return records
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_overlap_handoff_selector.json').write_text(json.dumps(out)+'\n')
