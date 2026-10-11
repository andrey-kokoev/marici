"""Exact native cross-sector factorization through a shared radial face.

Uses Q(sqrt(-3)); a geometric face restriction is tested separately from
unrestricted low-rank algebraic factorization. No extra vertices are added.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
Z=(F(0),F(0));ONE=(F(1),F(0))


def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-3*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def div(a,b):
    q=b[0]*b[0]+3*b[1]*b[1]
    assert q
    return mul(a,(b[0]/q,-b[1]/q))
def rank(a):
    a=[list(r) for r in a];i=0
    for j in range(len(a[0])):
        p=next((p for p in range(i,len(a)) if a[p][j]!=Z),None)
        if p is None:continue
        a[i],a[p]=a[p],a[i]
        pivot=a[i][j];a[i]=[div(v,pivot) for v in a[i]]
        for k in range(len(a)):
            if k!=i:
                c=a[k][j];a[k]=[add(v,neg(mul(c,w))) for v,w in zip(a[k],a[i])]
        i+=1
        if i==len(a):break
    return i

def mv(a,v):
    return [sumz(mul(x,y) for x,y in zip(row,v)) for row in a]
def sumz(xs):
    out=Z
    for x in xs:out=add(out,x)
    return out


def main():
    geometry=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())
    arrows=json.loads((ROOT/'results/twelve-triangle-1836-arrows.json').read_text())
    owner={r['outer_arrow']:r['triangle'][0].removeprefix('F_') for r in geometry['triangles_and_transports']}
    rotations={r['outer_arrow']:[[F(x) for x in row] for row in r['rotation']] for r in geometry['triangles_and_transports']}
    faces=sorted(set(owner.values()));axes='xyz'
    labels={f:sorted(k for k,v in owner.items() if v==f) for f in faces}
    values={(tuple(a['source']),tuple(a['target'])):(F(a['weight_real']),F(a['weight_imag_sqrt3'])) for a in arrows}
    points=dict(zip('ABCD',[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]))
    rows=[]
    for fa,fb in combinations(faces,2):
        common=sorted(set(fa)&set(fb));assert len(common)==2
        # Shared face Oab, O=0: its plane is spanned by the two shared vertices.
        a,b=[points[k] for k in common]
        normal=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
        assert any(normal)
        directions=[]
        for source,target in [(fa,fb),(fb,fa)]:
            source_ports=[(g,i) for g in labels[source] for i in range(3)]
            target_ports=[(g,i) for g in labels[target] for i in range(3)]
            gblock=[[values.get((('local',h,axes[j]),('aligned',g,axes[i])),Z)
                     for h,j in source_ports] for g,i in target_ports]
            nblock=[[values.get((('aligned',h,axes[j]),('raw',g,axes[i])),Z)
                     for h,j in source_ports] for g,i in target_ports]
            assert rank(gblock)==3 and rank(nblock)==1
            # G and N act on different retained stage ports. If encoded as a
            # single linear map, their interface is a direct sum, not shared.
            combined=[row+[Z]*9 for row in gblock]+[[Z]*9+row for row in nblock]
            assert rank(combined)==4
            assert sum(v!=Z for row in gblock for v in row)==27
            assert sum(v!=Z for row in nblock for v in row)==81
            # Native G block factors through a three-component COMMON FRAME:
            # source restriction sum_h R_h^T x_h /12, target lift R_g.
            for r,(g,i) in enumerate(target_ports):
                for c,(h,j) in enumerate(source_ports):
                    expected=(sum(rotations[g][i][k]*rotations[h][j][k] for k in range(3))/12,F(0))
                    assert gblock[r][c]==expected
            # Natural spatial-face restriction: aggregate ambient vector then
            # project to span(a,b). Normal input is killed there. Choose one
            # actual source triangle carrying that normal, all others zero.
            v=[(F(normal[i]),F(0)) if h==labels[source][0] else Z for h,i in source_ports]
            gout=mv(gblock,v)
            # Orthogonal projection annihilates the ambient normal exactly.
            assert sum(normal[i]*a[i] for i in range(3))==0
            assert sum(normal[i]*b[i] for i in range(3))==0
            assert any(x!=Z for x in gout)
            # A 2-dimensional linear interface cannot carry rank-3 G. Even
            # one common scalar collective interface cannot carry G.
            # N alone has an exact scalar factorization by pivot row/column.
            pivot=next((i,j) for i,row in enumerate(nblock) for j,vv in enumerate(row) if vv!=Z)
            i0,j0=pivot
            left=[row[j0] for row in nblock]
            right=[div(x,nblock[i0][j0]) for x in nblock[i0]]
            assert all(mul(left[i],right[j])==nblock[i][j] for i in range(9) for j in range(9))
            directions.append(dict(source=source,target=target,G_rank=3,N_rank=1,stage_retained_combined_rank=4,
                                   G_support=27,N_support=81,
                                   native_common_frame_factorization=True,
                                   shared_face_plane_normal=list(normal),
                                   face_restriction_kernel_witness_survives_G=True,
                                   N_scalar_factorization=True))
        rows.append(dict(pair=[fa,fb],shared_geometric_face=['O']+common,directions=directions))
    result=dict(schema='marici.nima.1836-pair-face-factorization.v1',status='pass',
                coefficient_field='Q(sqrt(-3))',rows=rows,
                disposition='Every native G cross-block factors through three common-frame components but not a two-dimensional linear face interface; N cross-blocks factor through one scalar. Retaining their distinct stage domains gives combined rank four per direction.',
                residual='A richer face record carrying a third/normal component might support gluing. No native internal-face comparison maps currently establish that interpretation. Rank obstruction concerns linear coefficient interfaces, not all possible higher-coherence interfaces.')
    out=ROOT/'results/1836-pair-face-factorization.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
