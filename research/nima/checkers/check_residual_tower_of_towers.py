"""Strict, source-anchored two-index coherence prototype on forgotten packets.

Jet depths 0..3, nerve/coherence dimensions 0..4. Not a weak infinity-category
construction or a certificate for the selected analytical observer protocol.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,combinations
import importlib.util,json
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('roles',ROOT/'checkers/check_four_residual_coherence_roles.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)


def eye(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def mm(A,B):return [[a.dot(row,col) for col in zip(*B)] for row in A]
def inv(A):
    n=len(A);rows,pivots=a.rref([row+unit for row,unit in zip(A,eye(n))],n)
    assert pivots==list(range(n))
    return [row[n:] for row in rows]
def kron(A,B):
    # First packet is the low-bit factor, as in actual block concatenation.
    return [[A[i][j]*B[k][l] for l in range(len(B[0])) for j in range(len(A[0]))]
            for k in range(len(B)) for i in range(len(A))]
def indices(n,m):return [t for t in range(1<<n) if t.bit_count()<=m]
def sub(A,rows,cols):return [[A[i][j] for j in cols] for i in rows]
def projection(n,m,q):
    large=indices(n,m);small=indices(n,q)
    return [[Q(t==u) for u in large] for t in small]


def frames(n):
    size=1<<n;I=eye(size);U=eye(size)
    V=[[Q((1+t.bit_count()) if t==u else 0) for u in range(size)] for t in range(size)]
    for i,j in ((1,0),(3,1),(7,3)):
        if i<size:U[i][j]=1
    for i,j in ((2,0),(7,2)):
        if i<size:V[i][j]=1
    result=[I,U,V,mm(V,U)]
    for A in result:
        assert all(not A[t][u] or u.bit_count()<=t.bit_count() for t in range(size) for u in range(size))
    return result


def face(vertices,i):return vertices[:i]+vertices[i+1:]
def degeneracy(vertices,i):return vertices[:i+1]+vertices[i:]
def wire_matrix(A):return [[str(x) for x in row] for row in A]


def main():
    counts={'source_fox_anchors':0,'source_product_basis_checks':0,'frame_anchor_checks':0,
            'depth_comparison_squares':0,'triangle_compositions':0,'higher_route_checks':0,
            'face_face_identities':0,'degeneracy_degeneracy_identities':0,
            'face_degeneracy_identities':0,'depth_cell_face_squares':0,
            'depth_cell_degeneracy_squares':0,'product_comparison_squares':0,'product_depth_squares':0,
            'mixed_realization_product_cubes':0,'evidence_fiber_comparisons':0}
    full=frames(3);assert mm(full[1],full[2])!=mm(full[2],full[1])
    Z=[[Q(b&t==t) for b in range(8)] for t in range(8)]
    for b,col in enumerate(a.basis(8)):
        source=a.paths(col,0,3)
        for t in range(8):
            seams=tuple(('e',(1<<(2*i))-1,((1<<(2*i))-1)|(1<<(2*i+1)),0)
                        for i in range(3) if t&(1<<i))
            assert a.f['vacuum_rows'](0,63,source,t.bit_count()).get(seams,0)==Z[t][b]
            counts['source_fox_anchors']+=1
    level_frames={};bridges={};anchors={}
    for m in range(4):
        J=indices(3,m);level_frames[m]=[sub(A,J,J) for A in full]
        anchors[m]=[mm(A,sub(Z,J,range(8))) for A in level_frames[m]]
        bridges[m]={(i,j):mm(level_frames[m][j],inv(level_frames[m][i])) for i,j in product(range(4),repeat=2)}
        for i,j in product(range(4),repeat=2):
            assert mm(bridges[m][i,j],anchors[m][i])==anchors[m][j]
            counts['frame_anchor_checks']+=1
        for i,j,k in product(range(4),repeat=3):
            assert mm(bridges[m][j,k],bridges[m][i,j])==bridges[m][i,k]
            counts['triangle_compositions']+=1
    for m in range(4):
        for q in range(m+1):
            P=projection(3,m,q)
            for i,j in product(range(4),repeat=2):
                assert mm(P,bridges[m][i,j])==mm(bridges[q][i,j],P)
                assert mm(P,anchors[m][i])==anchors[q][i]
                counts['depth_comparison_squares']+=1
    cell_counts={}
    for dimension in range(5):
        sequences=list(product(range(4),repeat=dimension+1))
        cell_counts[str(dimension)]=len(sequences)
        for vertices in sequences:
            for m in range(4):
                route=eye(len(indices(3,m)))
                for i,j in zip(vertices,vertices[1:]):route=mm(bridges[m][i,j],route)
                assert route==bridges[m][vertices[0],vertices[-1]]
                counts['higher_route_checks']+=1
            # Full simplicial identities, including repeated-frame degeneracies.
            for i,j in combinations(range(len(vertices)),2):
                assert face(face(vertices,j),i)==face(face(vertices,i),j-1)
                counts['face_face_identities']+=1
            if dimension<4:
                for i in range(len(vertices)):
                    for j in range(i,len(vertices)):
                        assert degeneracy(degeneracy(vertices,j),i)==degeneracy(degeneracy(vertices,i),j+1)
                        counts['degeneracy_degeneracy_identities']+=1
                for j in range(len(vertices)):
                    for i in range(len(vertices)+1):
                        lhs=face(degeneracy(vertices,j),i)
                        rhs=(degeneracy(face(vertices,i),j-1) if i<j else vertices if i in (j,j+1)
                             else degeneracy(face(vertices,i-1),j))
                        assert lhs==rhs
                        counts['face_degeneracy_identities']+=1
            # A cell is (depth, vertex sequence); depth transport uses the
            # already checked numerical comparison squares on every edge.
            for m in range(4):
                for q in range(m+1):
                    def truncate(cell):
                        assert cell[0]==m
                        return q,cell[1]
                    if dimension:
                        for i in range(len(vertices)):
                            assert truncate((m,face(vertices,i)))==(q,face(truncate((m,vertices))[1],i))
                            counts['depth_cell_face_squares']+=1
                    if dimension<4:
                        for i in range(len(vertices)):
                            assert truncate((m,degeneracy(vertices,i)))==(q,degeneracy(truncate((m,vertices))[1],i))
                            counts['depth_cell_degeneracy_squares']+=1
    # Product transport is induced by source multiplication, not stipulated
    # independently at each observer realization.
    for n,k in ((1,1),(1,2),(2,1)):
        Fn,Fk,Fo=frames(n),frames(k),frames(n+k)
        products=[mm(Fo[i],kron(inv(Fn[i]),inv(Fk[i]))) for i in range(4)]
        for u,v in product(a.basis(1<<n),a.basis(1<<k)):
            assert a.paths(a.inverse(a.tensor(u,v)),0,n+k)==a.f['multiply'](
                a.paths(a.inverse(u),0,n),a.paths(a.inverse(v),n,k))
            counts['source_product_basis_checks']+=1
        for i,j in product(range(4),repeat=2):
            Tn=mm(Fn[j],inv(Fn[i]));Tk=mm(Fk[j],inv(Fk[i]));To=mm(Fo[j],inv(Fo[i]))
            assert mm(To,products[i])==mm(products[j],kron(Tn,Tk))
            counts['product_comparison_squares']+=1
        for i in range(4):
            for m in range(n+k+1):
                Jn,Jk,Jo=indices(n,min(n,m)),indices(k,min(k,m)),indices(n+k,m)
                columns=[x+(y<<n) for y in Jk for x in Jn]
                truncated=sub(products[i],Jo,columns)
                input_projection=kron(projection(n,n,min(n,m)),projection(k,k,min(k,m)))
                assert mm(projection(n+k,n+k,m),products[i])==mm(truncated,input_projection)
                counts['product_depth_squares']+=1
    # Reassociate three products while changing the intermediate realizations.
    Fs={n:frames(n) for n in (1,2,3)};cache={}
    def mixed(i,j,k,n,m):
        key=(i,j,k,n,m)
        if key not in cache:cache[key]=mm(Fs[n+m][k],kron(inv(Fs[n][i]),inv(Fs[m][j])))
        return cache[key]
    for i,j,k,l in product(range(4),repeat=4):
        left=mm(mixed(j,i,l,2,1),kron(mixed(i,i,j,1,1),eye(2)))
        right=mm(mixed(i,k,l,1,2),kron(eye(2),mixed(i,i,k,1,1)))
        assert left==right
        counts['mixed_realization_product_cubes']+=1
    # Observer coordinate changes must preserve the meaning of evidence, too.
    # Solve for whole rational source fibers, preserving the old terminal fact.
    for m in range(4):
        for i,j in product(range(4),repeat=2):
            row=a.basis(len(indices(3,m)))[-1]
            source_row=a.pull([row],anchors[m][j])[0]
            transported=a.pull(a.pull([row],bridges[m][i,j]),anchors[m][i])[0]
            for value in (Q(0),Q(1)):
                direct=a.solve([[Q(1)]*8,source_row],[1,value],8)
                indirect=a.solve([[Q(1)]*8,transported],[1,value],8)
                assert a.canonical(direct,8)==a.canonical(indirect,8)
                counts['evidence_fiber_comparisons']+=1
    # A depth-violating realization is invertible on retained full data, but
    # cannot descend to the declared terminal-only observation.
    bad=eye(8);bad[0][7]=1
    hidden=[Q(i==7) for i in range(8)]
    P=projection(3,3,0)
    assert a.apply(P,hidden)==[0] and a.apply(mm(P,bad),hidden)==[1]
    assert mm(bad,inv(bad))==eye(8)
    # A corrupted bridge breaks a triangle despite matching all carrier sizes.
    broken=[row[:] for row in bridges[3][1,2]];broken[0][0]+=1
    assert mm(broken,bridges[3][0,1])!=bridges[3][0,2]
    report={'schema':'finite-source-anchored-tower-of-towers-v1','passed':True,
        'indices':{'jet_depth':[0,1,2,3],'nerve_coherence_dimension':[0,1,2,3,4]},
        'jet_dimensions':[1,4,7,8],'realizations_per_depth':4,
        'cells_per_depth_by_coherence_dimension':cell_counts,'checks':counts,
        'frames_at_full_depth':[wire_matrix(A) for A in full],
        'levels':[{'jet_depth':m,'moment_labels':indices(3,m),
                   'source_anchors':[wire_matrix(E) for E in anchors[m]],
                   'comparisons':[{'from':i,'to':j,'matrix':wire_matrix(T)} for (i,j),T in bridges[m].items()]}
                  for m in range(4)],
        'negative_controls':{'invertible_but_depth_mixing_frame_does_not_descend':True,
                             'corrupted_comparison_fails_triangle':True},
        'hidden_source_witness':{'moment_coordinates':list(map(str,hidden)),
                                 'original_terminal':0,'depth_mixed_terminal':1,
                                 'source':'H tensor H tensor H, H=Q-P'},
        'meaning':'A strict realization groupoid at each jet depth, with its nerve through dimension four; depth truncation commutes with source anchors, comparisons, faces, degeneracies and products.',
        'higher_witnesses':'Forced strict equalities. Higher cells do not add source measurements or new residual values.',
        'retention':'Depth truncation alone remains lossy. Exact-source use must retain omitted moments as typed residuals; unknown-source use retains compatible histories. The coherence nerve is not a residual store.',
        'scope':'Illustrative rational coordinate realizations of the complete finite forgotten jets. Not the historical selected scalar observers, nontrivial weak higher homotopies, all marked-source actions, completed-source reconstruction, or an infinite tower certificate.'}
    path=ROOT/'results/residual-tower-of-towers.json'
    path.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:report[key] for key in ('passed','indices','jet_dimensions','cells_per_depth_by_coherence_dimension','checks','negative_controls')},indent=2))


if __name__=='__main__':main()
