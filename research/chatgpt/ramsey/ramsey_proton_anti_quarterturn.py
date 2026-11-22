"""Test spatial signed-coordinate transport, oriented port ownership, and complex conjugation independently on the archived native proton transfers. Source tetrahedron coordinates from the original constructor."""
from ramsey_crossing_axis_scramble import pts,D,json
from itertools import permutations,product
from fractions import Fraction as F

def run():
    files=D.parents[1]/'nima/results';tri=json.loads((files/'twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports'];face={r['outer_arrow']:set(r['triangle'][0][2:]) for r in tri};ar=json.loads((files/'twelve-triangle-1836-arrows.json').read_text());W={(tuple(a['source']),tuple(a['target'])):(F(a['weight_real']),F(a['weight_imag_sqrt3'])) for a in ar};out=[]
    for rec in json.loads((D/'ramsey_rim_quarter_face_transport.json').read_text()):
        for ctrl in rec['registry_controls']:
            p=ctrl['binding'];g={p[int(i)-1]:p[j-1] for i,j in rec['rim'].items()};(perm,sign),=[(q,s) for q in permutations(range(3)) for s in product((1,-1),repeat=3) if all(tuple(s[i]*v[q[i]] for i in range(3))==pts[g[a]] for a,v in pts.items())];axes='xyz';results=[]
            for reverse,conj in product((False,True),repeat=2):
                def port(e):return ''.join(g[v] for v in (e[::-1] if reverse else e))
                def addr(k):
                    stage,e,ax=k;i=perm.index(axes.index(ax));return (stage,port(e),axes[i]),sign[i]
                good={s:0 for s in ('raw','local','aligned')}
                for (a,b),(u,v) in W.items():
                    aa,x=addr(a);bb,y=addr(b);good[a[0]]+=W.get((aa,bb))==(x*y*u,x*y*(-v if conj else v))
                results.append(dict(reverse=reverse,conjugate=conj,correct_faces=sum(face[port(e)]=={g[v] for v in face[e]} for e in face),correct_coefficients=good))
            assert [r for r in results if sum(r['correct_coefficients'].values())==1836 and r['correct_faces']==12]==[results[-1]];out.append(dict(binding=p,rim=rec['rim'],tests=results))
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_proton_anti_quarterturn.json').write_text(json.dumps(out)+'\n')
