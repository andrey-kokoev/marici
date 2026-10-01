"""Exact minimality audit for the constructed twelve-triangle collective identity.

Preserve the full input/output operator N, not merely its action on one vector.
The 72/73-arrow lower bounds apply to two-/three-pass linear networks with
separate auxiliary stages and all 36 original coefficient ports retained. They
are not unrestricted theorems about arbitrary recurrent or in-place circuits.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import (
    POINTS, LABELS, OMEGA, ONE, ZERO, C, mean, rotation, compose,
    transpose, zmv, zmul, zconj, zscale, znorm, zmm, zreal,
    projector, zsum, mm, mv,
)


def main():
    generators=((1,2,0,3),(3,0,2,1))
    group={(0,1,2,3)};front=list(group)
    while front:
        q=front.pop()
        for g in generators:
            p=compose(g,q)
            if p not in group: group.add(p);front.append(p)
    assert len(group)==12
    X0=transpose((mean([POINTS[k] for k in 'ABC']),POINTS['A'],POINTS['B']))
    v0=zmv(X0,(ONE,OMEGA,zmul(OMEGA,OMEGA)))
    rotations=[rotation(p) for p in sorted(group)]
    vs=[zmv(R,v0) for R in rotations]
    u=tuple(z for v in vs for z in v)
    assert len(u)==36 and all(z!=ZERO for z in u)
    norm=sum(znorm(z) for z in u)
    assert norm==80
    N=projector(u)
    local_projectors=[projector(v) for v in vs]
    L=tuple(tuple(local_projectors[i//3][i%3][j%3] if i//3==j//3 else ZERO
                  for j in range(36)) for i in range(36))
    blocks=[[mm(R,transpose(S)) for S in rotations] for R in rotations]
    G=zreal(tuple(tuple(blocks[i//3][j//3][i%3][j%3]/12 for j in range(36)) for i in range(36)))
    Id=tuple(tuple(ONE if i==j else ZERO for j in range(36)) for i in range(36))
    assert zmm(G,L)==N and zmm(N,N)==N
    assert zmm(Id,zmm(G,L))==N
    count=lambda m:sum(z!=ZERO for r in m for z in r)
    assert [count(L),count(G),count(N),count(Id)]==[108,432,1296,36]
    original_count=count(L)+count(G)+count(N)
    wire_feedback_count=count(L)+count(G)+count(Id)
    assert original_count==1836 and wire_feedback_count==576
    # Pruning-only minimality of the original graph: every closed three-step
    # cycle has strictly positive trace weight. Removing any arrow removes at
    # least one such cycle, strictly lowering trace(N)=1 when weights stay fixed.
    old=[]
    for stage,m in enumerate((L,G,N)):
        old.append({((stage,i),((stage+1)%3,j)):m[j][i]
                    for i in range(36) for j in range(36) if m[j][i]!=ZERO})
    losses={e:F(0) for stage in old for e in stage};cycle_trace=F(0)
    for closing,z in old[2].items():
        k=closing[0][1];i=closing[1][1]
        for b in range(36):
            e0=((0,i),(1,b));e1=((1,b),(2,k))
            if e0 not in old[0] or e1 not in old[1]: continue
            w=zmul(zmul(old[0][e0],old[1][e1]),z)
            assert w[1]==0 and w[0]>0
            cycle_trace+=w[0]
            for e in (e0,e1,closing): losses[e]+=w[0]
    assert cycle_trace==1 and len(losses)==1836 and min(losses.values())>0
    assert sum(losses.values())==3
    # Rank-one factorization: one shared auxiliary port Omega.
    B=(tuple(zscale(zconj(z),1/norm) for z in u),) # 1 x 36
    A=tuple((z,) for z in u)                    # 36 x 1
    assert zmm(A,B)==N
    assert zmm(B,A)==((ONE,),)
    assert sum(znorm(z) for z in B[0])==F(1,80)
    # Rescaling the hidden coordinate gives the balanced contractions
    # A'=u/sqrt(80), B'=u_dagger/sqrt(80), with identical supports.
    assert zmm(N,A)==A
    # Every input basis vector, not only the coherent vector, has the same output.
    for i in range(36):
        column=tuple((ONE if j==i else ZERO,) for j in range(36))
        assert zmm(A,zmm(B,column))==zmm(N,column)
    visible=[('coefficient',i) for i in range(36)]
    hub=('collective','Omega')
    arrows={(visible[i],hub):B[0][i] for i in range(36)}
    arrows.update({(hub,visible[i]):A[i][0] for i in range(36)})
    assert len(arrows)==72 and all(a!=b for a,b in arrows)
    assert len({v for e in arrows for v in e})==37
    # All 72 arrows occur in length-two closed identity-endpoint walks.
    used=set();weight_sum=ZERO
    for i in range(36):
        e=(visible[i],hub);back=(hub,visible[i])
        weight=zmul(arrows[e],arrows[back])
        assert weight[1]==0 and weight[0]>0
        weight_sum=(weight_sum[0]+weight[0],weight_sum[1]+weight[1])
        used.update((e,back))
    assert used==set(arrows) and weight_sum==ONE
    # Preserve the ORIGINAL three-stage clock as well: two one-dimensional
    # auxiliary ports joined by a single identity wire.
    h1=('local','Omega');h2=('aligned','Omega')
    three_pass={(visible[i],h1):B[0][i] for i in range(36)}
    three_pass[h1,h2]=ONE
    three_pass.update({(h2,visible[i]):A[i][0] for i in range(36)})
    assert len(three_pass)==73 and len({v for e in three_pass for v in e})==38
    assert zmm(A,zmm(((ONE,),),B))==N
    used3=set();weight3=ZERO
    for i in range(36):
        route=((visible[i],h1),(h1,h2),(h2,visible[i]))
        w=zmul(zmul(three_pass[route[0]],three_pass[route[1]]),three_pass[route[2]])
        assert w[1]==0 and w[0]>0
        weight3=(weight3[0]+w[0],weight3[1]+w[1]);used3.update(route)
    assert used3==set(three_pass) and weight3==ONE
    # Any deleted leg makes a nonzero column or row of N vanish.
    for i in range(36):
        cutB=(tuple(ZERO if j==i else z for j,z in enumerate(B[0])),)
        cutA=tuple((ZERO,) if j==i else row for j,row in enumerate(A))
        assert zmm(A,cutB)!=N and zmm(cutA,B)!=N
    # Tetrahedral equivariance: action permutes blocks by left multiplication
    # and rotates their coefficient coordinates. The assembled mode is invariant.
    perms=sorted(group);lookup={p:i for i,p in enumerate(perms)}
    for g,Rg in zip(perms,rotations):
        transformed=[None]*12
        for h,v in zip(perms,vs):
            transformed[lookup[compose(g,h)]]=zmv(Rg,v)
        assert transformed==vs
    # Geometry remains exactly the original twelve triangles.
    triangles=[]
    for p in perms:
        a,b,c=[LABELS[p[i]] for i in range(3)]
        triangles.append((mean([POINTS[k] for k in (a,b,c)]),POINTS[a],POINTS[b]))
    from check_twelve_triangle_positive_geometry import det
    volume=sum(det(transpose(t))/6 for t in triangles)
    assert volume==F(8,3)
    # Lower-bound witnesses: no zero input column or output row exists in N.
    nonzero_columns=sum(any(N[j][i]!=ZERO for j in range(36)) for i in range(36))
    nonzero_rows=sum(any(z!=ZERO for z in row) for row in N)
    lower_bound=nonzero_columns+nonzero_rows
    assert lower_bound==72==count(A)+count(B)
    result={'status':'passed','original_geometry_volume':str(volume),
            'same_collective_projector_on_all_inputs':True,'tetrahedral_equivariance_preserved':True,
            'implementations':{'original_dense_three_stage':1836,'identity_wire_feedback':576,
                               'one_hub_two_pass':72,'three_stage_factored_return':73},
            'original_pruning_minimality':{'established':True,'fixed_weights':True,
                                           'every_arrow_has_positive_closed_trace_contribution':True,
                                           'min_single_deletion_trace_loss':str(min(losses.values())),
                                           'max_single_deletion_trace_loss':str(max(losses.values())),
                                           'proof':'Every proper edge-deleted subgraph removes at least one positive closed-cycle contribution and creates none; its cycle trace is strictly below 1, so it cannot equal N.'},
            'minimality':{'class':'two-pass linear gather/scatter, fixed 36 visible ports, disjoint auxiliary ports, scalar weighted endpoint arrows',
                          'nonzero_input_columns':nonzero_columns,'nonzero_output_rows':nonzero_rows,
                          'lower_bound':lower_bound,'attained':True,
                          'proof':'N=AB has 36 nonzero columns so B needs at least 36 nonzero entries; N has 36 nonzero rows so A needs at least 36. Disjoint pass endpoints make these 72 different arrows. The one-hub factorization attains the bound.'},
            'three_stage_minimality':{'class':'three-pass linear network with fixed 36 visible ports, disjoint internal stages, arbitrary auxiliary dimensions, no bypasses',
                                      'lower_bound':73,'attained':True,'proof':'At least 36 first-stage arrows for the nonzero input columns, at least one middle arrow for a nonzero return, and at least 36 last-stage arrows for the nonzero output rows.',
                                      'closed_three_step_walks':36,'closed_walk_union_arrows':73,
                                      'positive_closed_weight_sum':'1'},
            'two_step_closed_walks':36,'closed_walk_union_arrows':72,'positive_closed_weight_sum':'1',
            'single_arrow_deletion_controls':72,
            'scope':'1836 is pruning-minimal at fixed weights but not implementation-size minimal. The exact collective identity and spatial carrier admit proven minima of 73/72 arrows in the stated three-/two-pass linear classes, respectively.'}
    dest=Path(__file__).resolve().parents[1]/'results'
    (dest/'twelve-triangle-net-minimality.json').write_text(json.dumps(result,indent=2)+'\n')
    manifest=[{'source':src,'target':dst,'weight_real':str(z[0]),'weight_imag_sqrt3':str(z[1])}
              for (src,dst),z in sorted(arrows.items(),key=lambda item:str(item[0]))]
    (dest/'twelve-triangle-72-arrows.json').write_text(json.dumps(manifest,indent=2)+'\n')
    manifest3=[{'source':src,'target':dst,'weight_real':str(z[0]),'weight_imag_sqrt3':str(z[1])}
               for (src,dst),z in sorted(three_pass.items(),key=lambda item:str(item[0]))]
    (dest/'twelve-triangle-73-arrows.json').write_text(json.dumps(manifest3,indent=2)+'\n')
    print('PASS: original 1836-arrow graph is pruning-minimal at fixed weights; refactoring preserves N and geometry with 73 arrows (three-stage minimum) or 72 (two-pass minimum).')

if __name__=='__main__': main()
