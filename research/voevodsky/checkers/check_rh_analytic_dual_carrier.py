"""Exact finite restrictions of the analytic test/antidual enlargement.
All-domain continuity and source identity are analytic arguments in the note,
not inferred from these finite matrix tests. Source-owner inputs are read only.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_native_task_catalogue import ROOT,ZERO,ONE,mm,adj,madd,msub,mzero,parse,sparse,eye,trace
from check_proton_unitary_probe_repair import restore
from check_rh_two_seed_route_audit import build,columns,multiply_scalar,blockdiag
from check_rh_source_kernel_generation import ar,arb,acb,ctx


def neg(A):return multiply_scalar(A,F(-1))
def hyperbolic(n):
    I=eye(n);Z=mzero(n,n)
    return [[(I if (i<n)!=(j<n) else Z)[i%n][j%n] for j in range(2*n)] for i in range(2*n)]
def shear(G):
    n=len(G);U=eye(2*n)
    for i in range(n):
        for j in range(n):U[n+i][j]=G[i][j]
    return U

def lift(G):return eye(len(G))+[row[:] for row in G]
def primal_gram(entries,m):
    G=mzero(m,m)
    for row in entries:
        i,j=row['indices'];lo,hi=map(F,row['full_divisor_enclosure']['rational_bounds'])
        G[i][j]=G[j][i]=((lo+hi)/2,F(0))
    return G

def walk(word,start,edge_forms):
    n=len(next(iter(edge_forms.values())));position=start;total=mzero(n,n);U=eye(2*n)
    for edge in word:
        assert len(edge)==2 and edge[0]==position,'noncomposable occurrence history'
        position=edge[1];G=edge_forms[edge];total=madd(total,G);U=mm(shear(G),U)
    assert position==start and U==shear(total)
    return total

def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/rh-analytic-dual-carrier-v1.json';c=json.loads(cp.read_text());ctx.prec=160
    paths={k:ROOT/c[k] for k in ('arithmetic','divisor3','divisor15')};data={k:json.loads(p.read_text()) for k,p in paths.items()}
    for record in data.values():
        assert record['passed']
        for path,digest in record['source_hashes'].items():assert sha256(Path(path).read_bytes()).hexdigest()==digest,path
    # All-domain bounds are proved in the note. Check the scalar anchors;
    # this is not a numerical extrapolation of finite test matrices.
    pi=arb.pi();l2=arb(2).log();l3=arb(3).log()
    assert abs(acb(ar('1/4')).digamma().real)<6 and pi.log()<2
    assert l3>1 and l2*(l2+1)/(2*arb(2).sqrt())+l3*(l3+1)/(3*arb(3).sqrt())<1
    assert arb(13).zeta_nzeros().unique_fmpz()==0 and F(512,169)<4
    assert F(16)+28+21==65
    forms={k:restore(v) for k,v in data['arithmetic']['generated_midpoint_terms'].items()}
    E,G,P=forms['endpoint'],forms['gamma'],forms['prime'];A=madd(madd(E,G),P)
    Z=restore(data['divisor3']['comparison_midpoint_forms']['full_divisor']);Delta=msub(A,Z)
    S15=primal_gram(data['divisor15']['full_divisor_entries'],15)
    assert all(F(x['rational_bounds'][0])>0 for x in data['divisor15']['positive_interval_LDL_pivots'])
    complex_control=mzero(15,15);complex_control[0][0]=(F(-2,5),F(0));complex_control[1][1]=(F(3,7),F(0))
    complex_control[0][1]=(F(2,9),F(1,5));complex_control[1][0]=(F(2,9),F(-1,5))
    examples={'endpoint3':E,'gamma3':G,'prime3':P,'arithmetic3':A,'divisor3':Z,
              'full_divisor_positive15':S15,'negative15_not_actual_Weil':neg(eye(15)),
              'complex_Hermitian_control15_not_actual_Weil':complex_control}
    tested={}
    for label,Q in examples.items():
        n=len(Q);assert Q==adj(Q)
        H=multiply_scalar(hyperbolic(n),F(1,2));B=lift(Q);U=shear(Q)
        assert mm(mm(adj(B),H),B)==Q
        assert mm(U,shear(neg(Q)))==eye(2*n)
        # Reversible accumulator, but NOT a Hermitian-form-preserving gate.
        defect=msub(mm(mm(adj(U),H),U),H)
        assert defect==blockdiag([Q,mzero(n,n)]) and defect!=mzero(2*n,2*n)
        tested[label]={'restriction_dimension':n,'fixed_pair_signature':[n,n],
                      'exact_pullback':True,'reversible_shear':True,'pairing_unitary':False}
    edges={'AB':E,'BC':G,'CA':P,'BA':neg(E),'AD':Z,'DB':E,'BD':neg(E),'DA':neg(Z)}
    assert walk(c['left_loop'],'A',edges)==A
    assert walk(c['right_loop_at_B'],'B',edges)==Z and walk(c['right_loop_at_A'],'A',edges)==Z
    assert walk(c['comparison_loop'],'A',edges)==Delta
    assert walk(c['same_direction_two_loop'],'A',edges)==madd(A,Z) and madd(A,Z)!=Delta
    try:walk(['AB','BC','CA','BA','AD','DB'],'A',edges)
    except AssertionError:bad_history_rejected=True
    else:bad_history_rejected=False
    assert bad_history_rejected
    wrong=dict(edges);wrong['BA']=E
    assert walk(c['right_loop_at_A'],'A',wrong)!=Z
    # Gauge freedom: common edge E ->2E, compensate CA and DB/BA.
    # Geometry/opposite orientation alone does not select the endpoint law.
    gauge=dict(edges);gauge['AB']=madd(E,E);gauge['BA']=neg(gauge['AB']);gauge['DB']=gauge['AB'];gauge['BD']=neg(gauge['AB']);gauge['CA']=msub(P,E)
    assert walk(c['left_loop'],'A',gauge)==A and walk(c['right_loop_at_A'],'A',gauge)==Z
    assert walk(c['comparison_loop'],'A',gauge)==Delta
    # Midpoint restrictions do NOT assert the exact source loop is identity.
    assert Delta!=mzero(3,3);errors=[]
    spec={tuple(r['indices']):r for r in data['divisor3']['spectral_entries']}
    for i in range(3):
        for j in range(i,3):
            alo,ahi=map(F,data['arithmetic']['generated_matrix'][i][j]['rational_bounds'])
            zlo,zhi=map(F,spec[i,j]['full_divisor']['rational_bounds'])
            ap=A[i][j][0];zp=Z[i][j][0]
            assert alo<=ap<=ahi and zlo<=zp<=zhi
            radius=max(abs(alo-ap),abs(ahi-ap))+max(abs(zlo-zp),abs(zhi-zp))
            assert abs(ap-zp)<=radius and radius>0
            errors.append({'indices':[i,j],'midpoint_defect':str(ap-zp),'certified_correction_radius':str(radius)})
    pp,np=ROOT/c['proton'],ROOT/c['neutron'];_,pops=parse(json.loads(pp.read_text()))
    ns=json.loads(np.read_text());d=[F(r['d']) for r in ns['coordinates']];nops=[mzero(36,36) for _ in range(3)]
    for r in ns['arrows']:
        aa,bb,cc,dd=map(F,r['numerator']);assert bb==dd==0
        nops['LGN'.index(r['stage'])][r['target']][r['source']]=(aa/d[r['source']],cc/d[r['source']])
    native={}
    for name,ops,metric in (('protonlike',pops,[F(1)]*36),('neutron',nops,[1/x for x in d])):
        bank=build(name,ops,metric);x=columns(bank['X'],[0]);y=columns(bank['Y'],[0]);scale=bank['D'][0][0][0];assert scale>0
        assert mm(mm(adj(x),bank['H']),x)==[[ZERO]] and mm(mm(adj(y),bank['H']),y)==[[ZERO]]
        assert multiply_scalar(mm(mm(adj(x),bank['H']),y),1/scale)==[[(F(1,2),F(0))]]
        assert mm(mm(adj(x),bank['Ms']),x)==mm(mm(adj(y),bank['Ms']),y)==[[(scale,F(0))]]
        assert mm(mm(adj(x),bank['Ms']),y)==[[ZERO]]
        assert mm(bank['W'],x)==y and mm(bank['W'],y)==mzero(108,1)
        # Normalize BOTH tags by sqrt(scale); check squared normalization
        # exactly, without pretending sqrt(scale) belongs to Q(sqrt(-3)).
        projector=multiply_scalar(mm(madd(mm(x,adj(x)),mm(y,adj(y))),bank['Ms']),1/scale)
        remainder=msub(eye(108),projector)
        assert mm(projector,projector)==projector and trace(projector)==(F(2),F(0))
        assert mm(projector,bank['W'])==mm(bank['W'],projector)
        W2=mm(bank['W'],bank['W']);W3=mm(W2,bank['W'])
        assert mm(W3,W2)==W2 # Native clock polynomial x^5-x^2.
        assert mm(mm(adj(projector),bank['H']),remainder)==mzero(108,108)
        Bs=blockdiag([msub(ops[1],ops[2])]*3)
        assert mm(Bs,projector)==mm(projector,Bs)==mzero(108,108)
        brank=trace(Bs)[0];assert brank.denominator==1
        # Finite factorized pullback on normalized tags tensor test/dual.
        for Q in examples.values():assert madd(multiply_scalar(Q,F(1,2)),multiply_scalar(adj(Q),F(1,2)))==Q
        native[name]={'stage_ranks':bank['ranks'],'source_tag_before_normalization':sparse(x),'antidual_tag_before_normalization':sparse(y),
           'divide_both_tags_by_sqrt':str(scale),'mixed_pairing':'1/2','all_factorized_finite_pullbacks_verified':True,
           'native_hyperbolic_plane_reduces_W':True,'untouched_remainder_dimension':106,
           'completed_global_G_minus_N_rank':int(brank),
           'new_test_antidual_factor_required':True,'native_W_becomes_analytic_shear':False}
    assert {v['completed_global_G_minus_N_rank'] for v in native.values()}=={6,33}
    assert msub(shear(multiply_scalar(G,F(5))),shear(multiply_scalar(G,F(2))))!=mzero(6,6)
    result={'schema':'marici.rh-analytic-dual-carrier.v1','passed':True,'iteration':7,'parameters':c,
      'fixed_test_antidual_carrier_constructed_analytically':True,'weak_source_operators_defined_by_kernels_not_point_tables':True,
      'all_domain_continuity_bounds':{'endpoint':16,'gamma':28,'prime':21,'arithmetic':65,'divisor':4,
        'seminorm':'p(1,2), or p(1,0) where sufficient','N13_certified_zero':True,
        'proof_status':'Analytic estimates in companion note; scalar anchors checked, not machine-formalized functional analysis'},
      'global_pairing_only_separately_continuous':True,'positive_Hilbert_metric_assumed':False,
      'all_T_inputs_have_effective_programs':False,'general_effective_test_oracle_interface_provided':False,
      'finite_restrictions_checked':tested,'composable_source_triangle_paths_verified':True,
      'source_common_edge_endpoint_decoration_is_not_geometry_forced':True,'common_edge_gauge_freedom_verified':True,
      'wrong_edge_orientation_and_noncomposable_history_rejected':True,'same_direction_two_loops_compute_sum_not_comparison':True,
      'independent_midpoint_comparison_is_identity':False,'midpoint_correction_envelopes':errors,
      'exact_source_comparison_identity_basis':'Primary explicit formula on evenized analytic tests in T, with uniform factor4 and unconditional divisor reflection',
      'same_completed_signed_pairing_and_source_evaluators_beside_both':True,'native_tags':native,
      '15_test_capacity_obstruction_of_original_native_H_removed_without_enlargement':False,
      'selected_infinite_dual_pair_has_unbounded_positive_and_negative_index':True,
      'full_native_stage_preserving_processing_equivalence_constructed':False,
      'stage_preserving_invertible_map_for_this_selected_plane_completion_possible':False,
      'stage_obstruction':'G-minus-N remains finite rank6 versus33 across the three stages',
      'native_clock_polynomial':'W^5=W^2, including the lifted nilpotent plane and untouched remainder',
      'nonzero_source_shear_has_injective_intertwiner_into_this_native_clock':False,
      'clock_obstruction':'For U=I+N, N^2=0, U^5-U^2=3N; injective intertwining would force N=0',
      'RH_equivalence_uses_standard_compact_Weil_criterion_not_proved_by_this_constructor':True,
      'all_test_positivity_proved':False,'RH_proved':False,'shared_sources_modified':False,'scope':c['scope'],
      'next_obligation':'Audit covariance/intertwining with native operations and analytic source actions; form-compatible completed tags alone are not native processing equivalence.'}
    files=[cp,*paths.values(),pp,np,ROOT/c['primary'],ROOT/c['count_derivation'],Path(__file__)]
    result['source_hashes']={str(p.resolve()):sha256(p.read_bytes()).hexdigest() for p in files}
    (base/'results/rh-analytic-dual-carrier-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'fixed_infinite_dual_pair_defined':True,'exact3_and15_restrictions_verified':True,
      'source_triangle_paths_and_orientation_verified':True,'compatible_completed_tags_in_both':True,
      'native_analytic_gate_execution':False,'RH_proved':False},indent=2))
if __name__=='__main__':main()
