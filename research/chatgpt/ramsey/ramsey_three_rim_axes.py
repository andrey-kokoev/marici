"""Transport the recovered rim half-turn by the existing native t, deriving the vertex permutation from face projectors. Compare all three opposite-edge partitions and their signed commutators."""
from ramsey_rim_signed_dictionary import as_op,E,I,sm,adj,gmm,D,json,product
from electron_packet_interface import matrix_add,ACTIONS,F
from ramsey_crossing_axis_scramble import pts
from ramsey_electron_face_joint_weights import read_operator
from assemble_metric_coefficient_protocol import sharp,ONE
from itertools import combinations,product as pairs

def run():
    h=I
    for a in E:h=matrix_add(h,a)
    t=sm(-F(1,2),h);assert t in ACTIONS;U=as_op(t);root=D.parents[1];load=lambda p:json.loads((root/p).read_text());norm=load('voevodsky/results/electron_tetrahedral_spinor_store.json')['normals'];missing=[next(v for v,x in pts.items() if all(F(b)==F(-h,3) for h,(a,b) in zip(x,w))) for w in norm];L=read_operator(load('strominger/results/common-three-carrier-protocol/electron.json')['operators']['L'],8);P=[{(i%2,j%2):z for (i,j),z in L.items() if i//2==j//2==k} for k in range(4)];g={a:missing[P.index(product(product(U,q),sharp(U,[ONE,ONE])))] for a,q in zip(missing,P)}
    basis=json.loads((D/'ramsey_rim_signed_dictionary.json').read_text());records=[]
    for row in basis:
        k=row['axis']-1;e=sm(row['sign'],E[k]);edges=['AB','CD'];chain=[]
        for _ in range(3):
            axis,= [i+1 for i,a in enumerate(E) if sm(row['sign'],a)==e];perm={v:missing[P.index(product(product(as_op(e),q),sharp(as_op(e),[ONE,ONE])))] for v,q in zip(missing,P)};assert all(perm[a]==b and perm[b]==a for a,b in edges);chain.append(dict(pair=edges,axis=axis,sign=row['sign']));edges=[''.join(g[x] for x in s) for s in edges];e=gmm(gmm(t,e),adj(t))
        assert [z['axis'] for z in chain]==[3,1,2] and edges==['AB','CD'];records.append(chain)
    n=0
    for i,j in combinations(range(3),2):
        for a,b in pairs((1,-1),repeat=2):
            x,y=sm(a,E[i]),sm(b,E[j]);assert gmm(x,y)==sm(-1,gmm(y,x));n+=1
    return dict(vertex_cycle=g,chains=records,sector_checks=n)
if __name__=='__main__':
    out=run();print(out['vertex_cycle'],out['chains'][0],out['sector_checks']);(D/'ramsey_three_rim_axes.json').write_text(json.dumps(out)+'\n')
