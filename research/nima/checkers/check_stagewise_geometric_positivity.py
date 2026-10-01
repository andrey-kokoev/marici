"""Audit stagewise positivity without equating PSD with positive geometry.

Checks (1) the oriented-cell positive cone and its closed subcone, and (2) a
literal spatial-coordinate interpretation of the existing coefficient maps.
The latter interpretation is tested, not silently assumed to be their meaning.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import (
    POINTS, LABELS, ONE, ZERO, OMEGA, I, mean, compose, rotation,
    transpose, mm, mv, det, zmul, zconj, zscale, znorm, zmv,
    zmm, zreal, projector,
)
from check_collective_four_state_identity import rank


def main():
    generators=((1,2,0,3),(3,0,2,1))
    group={(0,1,2,3)};front=list(group)
    while front:
        p=front.pop()
        for g in generators:
            q=compose(g,p)
            if q not in group: group.add(q);front.append(q)
    permutations=sorted(group)
    rotations=[rotation(p) for p in permutations]
    triangles=[];points=dict(POINTS)
    for p in permutations:
        a,b,c=[LABELS[p[i]] for i in range(3)]
        centre='F_'+''.join(sorted((a,b,c)))
        points[centre]=mean([POINTS[k] for k in (a,b,c)])
        triangles.append((centre,a,b))
    Xs=[transpose(tuple(points[k] for k in t)) for t in triangles]
    X=tuple(row for block in Xs for row in block)
    edges=sorted({tuple(sorted(e)) for t in triangles for e in zip(t,t[1:]+t[:1])})
    D=[[F(0)]*12 for _ in edges]
    for i,t in enumerate(triangles):
        for a,b in zip(t,t[1:]+t[:1]):
            D[edges.index(tuple(sorted((a,b))))][i]+=1 if a<b else -1
    D=tuple(tuple(r) for r in D)
    assert len(D)==18 and rank(D)==11
    assert mv(D,(F(1),)*12)==(F(0),)*18
    # Hence ker(boundary) is exactly span(1,...,1); its strictly positive part
    # is the one-dimensional positive fundamental-cycle ray.
    Q=tuple(tuple(F(1,12) for _ in range(12)) for _ in range(12))
    assert mm(Q,Q)==Q and all(x>0 for row in Q for x in row)
    assert all(x==0 for row in mm(D,Q) for x in row)
    coeff=(ONE,OMEGA,zmul(OMEGA,OMEGA))
    vs=[zmv(block,coeff) for block in Xs]
    Ps=[projector(v) for v in vs]
    u=tuple(z for v in vs for z in v)
    norm=sum(znorm(z) for z in u);assert norm==80
    N=projector(u)
    L=tuple(tuple(Ps[i//3][i%3][j%3] if i//3==j//3 else ZERO
                  for j in range(36)) for i in range(36))
    blocks=[[mm(R,transpose(S)) for S in rotations] for R in rotations]
    Gr=tuple(tuple(blocks[i//3][j//3][i%3][j%3]/12 for j in range(36)) for i in range(36))
    G=zreal(Gr)
    A=tuple((z,) for z in u)
    B=(tuple(zscale(zconj(z),1/norm) for z in u),)
    assert zmm(G,L)==N
    # Local mode-amplitude injection. Cone input is twelve positive REAL weights,
    # not arbitrary nonnegative Cartesian components in an unrelated basis.
    E=tuple(tuple(vs[i//3][i%3] if j==i//3 else ZERO for j in range(12)) for i in range(36))
    assert zmm(L,E)==E
    assert zmm(G,E)==zmm(E,zreal(Q))
    assert zmm(N,E)==zmm(E,zreal(Q))
    assert zmm(B,E)==(tuple((F(1,12),F(0)) for _ in range(12)),)
    assert A==zmm(E,tuple((ONE,) for _ in range(12)))
    probes=((F(1),)*12,tuple(F(i+1,12) for i in range(12)),tuple(F(1,i+1) for i in range(12)))
    for weights in probes:
        average=sum(weights)/12
        assert average>0
        psi=zmm(E,tuple(((w,F(0)),) for w in weights))
        afterL=zmm(L,psi);afterG=zmm(G,afterL);afterN=zmm(N,afterG)
        assert afterL==psi and afterG==afterN
        assert afterN==tuple((zscale(z,average),) for z in u)
        hub=zmm(B,psi)
        assert hub==(((average,F(0)),),)
        assert zmm(A,hub)==afterN
    for a in (F(1,10),F(1),F(7)):
        closed=(a,)*12
        assert mv(D,closed)==(F(0),)*18
        assert mv(Q,closed)==closed
    # PSD of the original stages is algebraic: each is Hermitian idempotent.
    def dagger(m): return tuple(tuple(zconj(z) for z in r) for r in transpose(m))
    for P in Ps:
        assert dagger(P)==P and zmm(P,P)==P
    assert transpose(Gr)==Gr and mm(Gr,Gr)==Gr
    assert dagger(N)==N and zmm(N,N)==N
    # Literal coordinate-map audit: columns are the three spatial corner roles.
    # This is NOT the same as a phase field attached to an unchanged surface.
    def mesh_audit(Y):
        copies={k:[] for k in points}
        imag=0;volume_real=F(0)
        for g,t in enumerate(triangles):
            block=Y[3*g:3*g+3]
            for j,label in enumerate(t):
                p=tuple(block[i][j] for i in range(3));copies[label].append(p)
                imag+=sum(z[1]!=0 for z in p)
            volume_real+=det(tuple(tuple(z[0] for z in r) for r in block))/6
        split={k:len(set(v)) for k,v in copies.items() if len(set(v))>1}
        return {'imaginary_coordinate_entries':imag,'split_shared_vertices':split,
                'signed_volume_of_real_parts':str(volume_real),
                'literal_real_mesh_admissible':imag==0 and not split and volume_real>0}
    source_audit=mesh_audit(zreal(X))
    assert source_audit['literal_real_mesh_admissible'] and source_audit['signed_volume_of_real_parts']=='8/3'
    Y=zmm(L,zreal(X));Z=zmm(G,Y);W=zmm(N,Z)
    assert Y==Z==W
    literal=[mesh_audit(t) for t in (Y,Z,W)]
    assert all(not r['literal_real_mesh_admissible'] for r in literal)
    assert all(r['signed_volume_of_real_parts']=='0' for r in literal)
    assert all(set(r['split_shared_vertices'])==set(LABELS) for r in literal)
    # The four face centres project to zero: their normal offset was removed.
    assert all(Y[3*g+i][0]==ZERO for g in range(12) for i in range(3))
    hub_corners=zmm(B,zreal(X))
    assert zmm(A,hub_corners)==Y
    # Hostile positive source: rigidly rotate the entire closed mesh while keeping
    # the numerical reference-frame maps fixed. The input remains positive, but
    # symmetry averaging annihilates it (trace of this 120-degree rotation is 0).
    S=rotation(generators[0]);assert det(S)==1 and sum(S[i][i] for i in range(3))==0
    rotated=tuple(r for block in Xs for r in mm(S,block))
    ra=mesh_audit(zreal(rotated));assert ra['literal_real_mesh_admissible']
    assert ra['signed_volume_of_real_parts']=='8/3'
    killed=zmm(N,zreal(rotated))
    assert all(z==ZERO for r in killed for z in r)
    # This control is deliberately a FIXED-frame test. Co-rotating the operators
    # would be a different, covariant transition rule and must be specified.
    # Passing audit assertions does not certify geometric admissibility.
    # No embedded-stage or atlas transition witnesses have yet been supplied.
    admissibility={name:{'status':'uncertified','missing_stage_geometry_witness':True,
                         'eligible_for_geometric_minimality_claim':False}
                   for name in ('original_1836','compressed_73','compressed_72')}
    assert all(not item['eligible_for_geometric_minimality_claim'] for item in admissibility.values())
    result={'status':'passed','audit_assertions_passed':True,
            'mandatory_requirement':'stagewise-positivity-requirement.md',
            'stagewise_geometric_positivity_required':True,
            'geometric_admissibility':admissibility,
            'geometric_minimum_established':False,
            'boundary_operator_shape':[18,12],'boundary_rank':11,
            'positive_closed_cell_cone':'{a*(1,...,1): a>0}',
            'amplitude_cone_stage_maps':{'original':['identity_12','mean_projector_Q','mean_projector_Q'],
                                         'compressed':['positive_mean','identity_scalar','positive_diagonal_injection'],
                                         'both_preserve_positivity':True,'both_preserve_closed_positive_inputs':True},
            'original_projector_stages_PSD':True,'source_mesh':source_audit,
            'literal_spatial_stages':dict(zip(('L','G after L','N after G after L'),literal)),
            'compressed_intermediate':'one complex coordinate chart row, not a supplied spatial cell complex',
            'rigid_rotation_control':{'source_positive_volume':'8/3','fixed_frame_output_zero':True,
                                      'scope':'Reference transports held fixed; does not refute a co-transported atlas rule.'},
            'conclusion':'Stagewise positive cell amplitudes admit both 1836 and 73 arrows. Treating the existing maps as literal spatial-coordinate maps fails for both. No stagewise positive-geometric atlas/embedding transition has been supplied, so geometric minimality remains uncertified.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'stagewise-geometric-positivity.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS audit: positive closed-chain cone is one ray; both networks preserve its weights stagewise. Literal spatial-map interpretation fails: split seams and zero real-part volume. Geometric minimality not certified.')

if __name__=='__main__': main()
