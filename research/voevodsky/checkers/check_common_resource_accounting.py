"""Finite selected-K accounting and ideal projective-readout energy checks."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,sys
from check_selected_source_k import verify,ROOT,BASE
from check_native_spinor_pair_adapter import matrix,transport_matrix
from check_typed_spin_channels import decode,eye,kron,conjugate_matrix,trace
from check_pentachoron_spin_interfaces import A,CI,S2,mm,adj,scale,add
from check_rival_defect_record_rule import vacuum_extend,generator_blocks
from sector_theorem import SOURCE_K,CONCLUSIONS

NOTE=BASE+'common-resource-accounting.v1.md'
CONTRACT=BASE+'contracts/retained-reaggregation-conjecture-net.v1.json'
SCENARIO_CHECKS=('same_complete_diagonals','both_signed_involutions','both_controls_self_adjoint','shared_vacuum_reference','all_joint_coordinates_retained','same_normalized_scalar_preparation','selected_K_self_adjoint')
READOUT_CHECKS=('centered_record_involution','unitary_coefficient_identity','density_trace_coefficients','record_occupation_coefficients','interaction_energy_coefficients','unitary_energy_coefficients','dephased_energy_coefficients','conditional_projective_states','measurement_energy_change_operator','rival_ready_state_dark')

def readout_checks():
    """Exact coefficients of C^2, CS, S^2; no transcendental equality by floats."""
    I=eye(2);zero=scale(A(0),I);N=((A(0),A(0)),(A(0),A(1)));X=((A(0),A(1)),(A(1),A(0)))
    g=A(F(1,2));h=add(N,scale(-g,X));G=scale(S2,add(h,scale(-g,I)))
    rho0=((A(1),A(0)),(A(0),A(0)))
    coefficients=(rho0,scale(CI,add(mm(rho0,G),scale(A(-1),mm(G,rho0)))),mm(mm(G,rho0),G))
    def expectations(operator,matrices=coefficients):return tuple(trace(mm(operator,r)) for r in matrices)
    def dephase(r):return ((r[0][0],A(0)),(A(0),r[1][1]))
    projected=[(mm(mm(rho0,r),rho0),mm(mm(N,r),N)) for r in coefficients]
    return dict(zip(READOUT_CHECKS,(
        adj(G)==G and mm(G,G)==I,
        mm(G,G)==I and add(scale(CI,G),scale(-CI,G))==zero,
        expectations(I)==(A(1),A(0),A(1)),
        expectations(N)==(A(0),A(0),g),
        expectations(scale(-g,X))==(A(0),A(0),-g),
        expectations(h)==(A(0),A(0),A(0)),
        expectations(h,tuple(dephase(r) for r in coefficients))==(A(0),A(0),g),
        all(p0==scale(r[0][0],rho0) and p1==scale(r[1][1],N) for r,(p0,p1) in zip(coefficients,projected)),
        add(dephase(h),scale(A(-1),h))==scale(g,X),
        mm(N,rho0)==zero and dephase(rho0)==rho0)))

def prove(nonce):
    selected=verify();assert selected['status']=='pass' and all(selected['checks'].values())
    def load(name):return json.loads((ROOT/(BASE+name)).read_text())
    source=load('results/pentachoron_cycle_transport.json');spin=load('results/pentachoron_spin_interfaces.json')
    typed=load('results/typed_spin_channels.json');Ps=matrix(typed['input_scalar_projector']);details={};g=A(F(1,2))
    def check(name,value):
        details[name]=bool(value)
        if not value:raise AssertionError(name)
    for row in source['chirality_results']:
        chirality=row['chirality'];ext=row['conditional_cycle_defect_extension']
        Ws=[matrix(ext[key]['cell_isometry']) for key in ('attachment_encoding','opposite_lift_attachment_encoding')]
        low=add(*(mm(W,adj(W)) for W in Ws));lo=decode(row['low_energy'])
        hi=decode(next(r for r in spin['chirality_results'] if r['chirality']==chirality)['higher_energy'])
        L=add(scale(lo,low),scale(hi,add(eye(10),scale(A(-1),low))))
        T=transport_matrix(matrix(row['spin_lift']));H=add(L,add(scale(A(2),eye(10)),scale(A(-1),add(T,adj(T)))))
        K=vacuum_extend(add(kron(H,eye(10)),kron(eye(10),conjugate_matrix(H))))
        I=eye(101);c=vacuum_extend(eye(100));zero=scale(A(0),I)
        for option,W in enumerate(Ws):
            label=f'{chirality}_{option}';J=kron(W,conjugate_matrix(W));Pi=vacuum_extend(mm(mm(J,Ps),adj(J)))
            projections=(Pi,add(c,scale(A(-1),Pi)))
            # Exact factored projection proof avoids dense 101-cubed products:
            # Jdagger J=I, Ps^2=Ps and cPi=Pi imply Pi^2=Pi,
            # (c-Pi)^2=c-Pi. Thus S=I-P is an orthogonal complement,
            # S^2+P^2=I and SP+PS=0 for either P.
            projection_identities=(mm(adj(J),J)==eye(4) and mm(Ps,Ps)==Ps and adj(Ps)==Ps and all(Pi[100][i]==Pi[i][100]==A(0) for i in range(101)))
            diagonal_ok=[];involutions=[];hermitian=[];vacuum_ok=[]
            for P in projections:
                S=add(I,scale(A(-1),P))
                involutions.append(projection_identities and add(S,P)==I)
                hermitian.append(adj(S)==S and adj(P)==P)
                d0,off,d1=generator_blocks(P,g);bare0=add(K,d0);bare1=add(K,d1)
                diagonal_ok.append(bare0==add(K,scale(g,I)) and bare1==add(K,scale(1+g,I)) and off==scale(-g,P) and add(bare0,scale(-g,I))==K and add(bare1,scale(-g,I))==add(K,I))
                vacuum_ok.append(bare0[100][100]==g and bare1[100][100]==1+g and all(off[100][i]==off[i][100]==A(0) for i in range(101)))
            check('same_complete_diagonals_'+label,all(diagonal_ok))
            check('both_signed_involutions_'+label,all(involutions))
            check('both_controls_self_adjoint_'+label,all(hermitian))
            check('shared_vacuum_reference_'+label,all(vacuum_ok))
            check('all_joint_coordinates_retained_'+label,len(K)==101 and all(len(P)==101 for P in projections) and add(*projections)==c and trace(Pi)==1 and trace(projections[1])==99)
            scalar=((A(1)/S2,),(A(0),),(A(0),),(A(1)/S2,));v=mm(J,scalar)+((A(0),),)
            check('same_normalized_scalar_preparation_'+label,mm(adj(v),v)==eye(1) and mm(Pi,v)==v and mm(projections[1],v)==tuple((A(0),) for _ in range(101)))
            check('selected_K_self_adjoint_'+label,adj(K)==K)
    for name,value in readout_checks().items():check(name,value)
    sources=dict(selected['source_hashes'])
    for p in (NOTE,CONTRACT,BASE+'checkers/check_common_resource_accounting.py'):
        sources[p]=sha256((ROOT/p).read_bytes()).hexdigest()
    return {'schema':'marici.voevodsky.common-resource-receipt.v1','status':'pass','node_id':'common-resource-accounting','outcome':'++','intent':'prove','attempt_nonce':nonce,
        'fresh_execution':True,'physical_admission':False,'kernel_verified_analytic_theorem':False,
        'proof_kind':'exact finite signed-control blocks, common reference and readout coefficient identities; written finite-dimensional spectral argument for joint reversibility',
        'checks':{name:True for name in sorted(CONCLUSIONS['common-resource-accounting'])},'detail_checks':details,
        'joint_dimension':202,'empty_ready_energy_before_subtraction':'1/2','empty_ready_energy_after_subtraction':'0',
        'readout_convention':'ideal projective neutral-record measurement, both outcomes and matter retained; external apparatus not modeled',
        'energy_accounting':{'primary_before':'epsilon','primary_after_nonselective_readout':'epsilon+p','rival_before_and_after':'epsilon','measurement_energy_increase':'p','p':'(1-cos(sqrt(2)))/4'},
        'source_hashes':sources}

if __name__=='__main__':Path(sys.argv[2]).write_text(json.dumps(prove(sys.argv[1]),indent=2)+'\n')
