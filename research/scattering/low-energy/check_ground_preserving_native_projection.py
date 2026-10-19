"""Exact native-metric endpoint projection with ground and sector preservation."""
import argparse
import hashlib
import json
from pathlib import Path
import check_three_hidden_native_interpolant as oldfit

base=oldfit.base;ROOT=oldfit.ROOT;HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/ground-preserving-native-projection.v1.json'
PROOF=HOME/'GROUND-PRESERVING-NATIVE-PROJECTION.md'
RESULT=HOME/'results/ground-preserving-native-projection.v1.json'
F,mm,eye,add,scale,inertia=oldfit.F,oldfit.mm,oldfit.eye,oldfit.add,oldfit.scale,oldfit.inertia
transpose,block,decode,invert=oldfit.transpose,oldfit.block,oldfit.decode,oldfit.invert
Span=base.algebra.lower.Span


def zeros(n,m):return [[F()]*m for _ in range(n)]
def difference(A,B):return add(A,scale(F(-1),B))
def rank(A):
    span=Span(len(A[0]))
    for i,row in enumerate(A):span.add(row,{'row':i})
    return len(span.rows)

def canonical_rows(span):
    rows=[r[:] for r in span.rows]
    for i in reversed(range(len(rows))):
        for j in range(i):
            c=rows[j][span.pivots[i]];rows[j]=[a-c*b for a,b in zip(rows[j],rows[i])]
    return rows

def cyclic(A,seeds):
    span=Span(len(A));queue=[v[:] for v in seeds];cursor=0
    while cursor<len(queue):
        v=queue[cursor];cursor+=1
        if span.add(v,{'queue':cursor}):queue.append([r[0] for r in mm(A,transpose([v]))])
    return transpose(canonical_rows(span))

def require_equal(A,B):assert A==B,'projection identity failed'

def validate_contract(c):
    assert c['schema']=='marici.scattering.ground-preserving-native-projection.v1'
    assert c['visible_coordinates']==[0,1,2] and c['spectral_points_in_stored_K_units']==['-1','-2']
    assert ROOT/c['native_source']==base.algebra.lower.SOURCE
    assert ROOT/c['preceding_fit']==oldfit.RESULT
    for key in ('live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    preceding=oldfit.build();assert preceding==json.loads(oldfit.RESULT.read_text(encoding='utf-8')),'stale preceding fit'
    threshold=base.algebra.lower.audit()
    src=json.loads(base.algebra.lower.SOURCE.read_text(encoding='utf-8'))
    K=decode(src['joint_generator']);h=[F(*v) for v in src['gram_diagonal']]
    H=[[h[i] if i==j else F() for j in range(11)] for i in range(11)]
    HP=[r[:3] for r in H[:3]];HQ=[r[3:] for r in H[3:]]
    PP=[r[:3] for r in K[:3]];QQ=[r[3:] for r in K[3:]]
    QP=[r[:3] for r in K[3:]];PQ=[r[3:] for r in K[:3]]
    assert inertia(mm(H,K))==(10,0,1) and inertia(mm(HQ,QQ))==(8,0,0)
    span=Span(8);snapshots={}
    for s in (1,2):
        X=mm(invert(add(QQ,scale(F(s),eye(8)))),QP);snapshots[s]=X
        for j,v in enumerate(transpose(X)):span.add(v,{'s':s,'visible_input':j})
    endpoint_rank=len(span.rows);assert endpoint_rank==5
    ground=transpose([[F(*v) for v in threshold['kernel_vector']]])
    added=span.add([r[0] for r in ground[3:]],{'native_ground':True});assert added is False
    W=transpose(canonical_rows(span));m=len(W[0]);assert m==5
    HW=mm(mm(transpose(W),HQ),W);LW=mm(mm(invert(HW),transpose(W)),HQ)
    require_equal(mm(LW,W),eye(m));assert inertia(HW)==(m,0,0)
    Ar=mm(mm(LW,QQ),W);Br=mm(LW,QP);Cr=mm(PQ,W)
    reduced=block(PP,Cr,Br,Ar);metric=block(HP,zeros(3,m),zeros(m,3),HW)
    E=block(eye(3),zeros(3,m),zeros(8,3),W)
    L=block(eye(3),zeros(3,8),zeros(m,3),LW)
    n=3+m
    require_equal(mm(L,E),eye(n));require_equal(mm(mm(transpose(E),H),E),metric)
    require_equal(mm(mm(L,K),E),reduced)
    assert inertia(metric)==(n,0,0) and inertia(mm(metric,reduced))==(n-1,0,1)
    assert inertia(mm(HW,Ar))==(m,0,0)
    Pn=[[F(int(i==j and i<3)) for j in range(11)] for i in range(11)]
    Pr=[[F(int(i==j and i<3)) for j in range(n)] for i in range(n)]
    require_equal(mm(Pn,E),mm(E,Pr))
    # Native orthogonal projector, not a fabricated whole-core intertwiner.
    projection=mm(E,L);require_equal(mm(projection,projection),projection)
    require_equal(mm(H,projection),transpose(mm(H,projection)))
    vr=mm(L,ground);require_equal(mm(E,vr),ground)
    require_equal(mm(reduced,vr),zeros(n,1));require_equal(vr[:3],ground[:3])
    require_equal(mm(mm(transpose(vr),metric),vr),mm(mm(transpose(ground),H),ground))
    v=[r[0] for r in vr[:3]];port_norm=sum((h[i]*v[i]*v[i] for i in range(3)),F());assert port_norm.positive()
    S0=[[F(int(i==j))-2*v[i]*h[j]*v[j]/port_norm for j in range(3)] for i in range(3)]
    require_equal(S0,decode(threshold['coefficient_limit']))
    evaluations=[]
    for s in (0,1,2,3):
        A=add(QQ,scale(F(s),eye(8)));X=mm(invert(A),QP)
        Y=mm(invert(add(Ar,scale(F(s),eye(m)))),Br)
        Xr=mm(W,Y);err=difference(X,Xr)
        N=mm(PQ,X);Nr=mm(Cr,Y);delta=difference(N,Nr)
        energy=mm(mm(mm(transpose(err),HQ),A),err)
        require_equal(mm(HP,delta),energy)
        counts=inertia(energy);assert counts[1]==0
        if s in (1,2):
            require_equal(X,Xr);require_equal(N,Nr)
            native_full=invert(difference(scale(F(-s),eye(11)),K))
            reduced_full=invert(difference(scale(F(-s),eye(n)),reduced))
            require_equal([r[:3] for r in native_full[:3]],[r[:3] for r in reduced_full[:3]])
        if s==3:assert counts==(1,0,2)
        evaluations.append({'z':str(-s),'self_energy_error_inertia':list(counts),
            'energy_error_identity_verified':True,'effective_operator_equal':rank(delta)==0,
            'full_visible_resolvent_equal':True if s in (1,2) else None})
    residual=difference(mm(K,E),mm(E,reduced));residual_rank=rank(residual);assert residual_rank>0
    symmetric=cyclic(K,[[F(int(i==0)) for i in range(11)],
                        [F(int(i in (1,2))) for i in range(11)]])
    assert len(symmetric[0])==5
    symmetric_r=mm(L,symmetric)
    require_equal(mm(E,symmetric_r),symmetric)
    require_equal(mm(residual,symmetric_r),zeros(11,5))
    # Port projection preserves the exact preparation sector, allowing identical leads.
    sym_span=Span(11)
    for j,vcol in enumerate(transpose(symmetric)):sym_span.add(vcol,{'symmetric_basis':j})
    assert all(not any(sym_span.reduce(col)[0]) for op in (K,Pn) for col in transpose(mm(op,symmetric)))
    assert rank(mm(Pn,symmetric))==2
    visible_cyclic=cyclic(reduced,[[F(int(i==j)) for i in range(n)] for j in range(3)])
    assert len(visible_cyclic[0])==n
    controls=[]
    for name in ('erase-native-ground','claim-global-intertwining','claim-third-point-identity','claim-global-five-hidden-minimality'):
        try:
            if name=='erase-native-ground':require_equal(ground,zeros(11,1))
            elif name=='claim-global-intertwining':require_equal(residual,zeros(11,n))
            elif name=='claim-third-point-identity':assert evaluations[-1]['effective_operator_equal'] is True
            else:assert preceding['minimal_hidden_dimension_for_exact_two_point_fit']==5
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile projection accepted: '+name)
    paths={ROOT/p for p in preceding['source_sha256']}
    paths.update((oldfit.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_ground_preserving_native_projection.py'))
    return {'schema':'marici.scattering.ground-preserving-native-projection-receipt.v1','status':'pass',
        'scope_verdict':'positive_endpoint_and_ground_preserving_native_projection',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'visible_dimension':3,'endpoint_snapshot_hidden_rank':endpoint_rank,'ground_added_hidden_dimension':int(added),
        'hidden_dimension':m,'full_core_dimension':n,'weighted_core_inertia':[n-1,0,1],
        'minimal_hidden_dimension_in_native_orthogonal_projection_class':endpoint_rank,
        'global_minimum_ground_preserving_hidden_dimension_claimed':False,
        'hidden_embedding':base.encoded(W),'embedding':base.encoded(E),'metric_adjoint':base.encoded(L),
        'reduced_core':base.encoded(reduced),'full_metric':base.encoded(metric),
        'native_ground_in_projection':True,'ground_visible_direction_and_norm_preserved':True,
        'reduced_ground_vector':base.encoded(vr),'coefficient_limit':base.encoded(S0),
        'conditional_chain_threshold_limit_matches_native':True,'coefficient_limit_norm_gap':0,
        'candidate_visible_cyclic_dimension':n,'symmetric_core_sector_dimension':5,
        'symmetric_core_sector_intertwining_verified':True,'symmetric_port_projector_invariance_verified':True,
        'symmetric_visible_lead_dimension':2,
        'global_intertwining_residual_rank':residual_rank,'evaluations':evaluations,
        'all_energy_full_response_identical':False,'explicit_positive_band_packet_error_bound_proved':False,
        'analytic_argument_machine_formalized':False,'source_operation_licensing_claimed':False,
        'native_owner_solver_replayed':False,'historical_ancestor_freshness_claimed':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,
        'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale ground-preserving projection'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    keys=('status','full_core_dimension','hidden_dimension','ground_added_hidden_dimension','weighted_core_inertia',
          'conditional_chain_threshold_limit_matches_native','symmetric_core_sector_dimension','global_intertwining_residual_rank')
    print(json.dumps({k:r[k] for k in keys}))


if __name__=='__main__':main()
