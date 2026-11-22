"""Compare cyclic block traces of the actual electron and proton N operators, indexing proton ports by source face and its directed crossing's shared edge. This is port-resolved composition, not a physical time schedule."""
from ramsey_electron_face_joint_weights import D,json,F,A,read_operator,product
from assemble_metric_coefficient_protocol import tr
from itertools import permutations

def run():
    root=D.parents[1];load=lambda p:json.loads((root/p).read_text());ops=[]
    for n in ('electron','proton'):
        d=load(f'strominger/results/common-three-carrier-protocol/{n}.json');labels=d['source']['coordinates'];ops.append((read_operator(d['operators']['N'],len(labels)),[s.split(':')[0] for s in labels]))
    vertices=dict(A=(1,1,1),B=(1,-1,-1),C=(-1,1,-1),D=(-1,-1,1));faces=[]
    for normal in load('voevodsky/results/electron_tetrahedral_spinor_store.json')['normals']:
        missing,=[v for v,x in vertices.items() if all(F(a)==0 and F(b)==F(-h,3) for (a,b),h in zip(normal,x))];faces.append(set(vertices)-{missing})
    triangles=load('nima/results/twelve-triangle-positive-geometry.json')['triangles_and_transports'];port=lambda i,j:next(t['outer_arrow'] for t in triangles if set(t['triangle'][0][2:])==faces[i] and set(t['outer_arrow'])==faces[i]&faces[j]);out=[]
    for i,j,k in permutations(range(4),3):
        ports=[port(i,j),port(j,k),port(k,i)];vals=[]
        for (m,names),w in zip(ops,([f'face-{a}' for a in (i,j,k)],ports)):
            blocks=[{(r,c):x for (r,c),x in m.items() if names[c]==a and names[r]==b} for a,b in zip(w,w[1:]+w[:1])];vals.append(tr(product(blocks[2],product(blocks[1],blocks[0]))))
        e,p=vals;assert e==-e.flip(8) and e*e==A(F(-1,1728)) and p==A(F(1,1728));out.append(dict(loop=[i,j,k],ports=ports,e=e.record(),p=p.record()))
    by={tuple(q['loop']):q for q in out};assert all(q['e']!=by[i,k,j]['e'] for (i,j,k),q in by.items());return out
if __name__=='__main__':
    out=run();print(out[:2]);(D/'ramsey_face_crossing_loop_phase.json').write_text(json.dumps(out)+'\n')
