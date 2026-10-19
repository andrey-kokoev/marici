"""Source-bound native spinor-pair adapters with full residual-space retention.
Both native doublets are audited. Conjugate partner and cross-channel couplings
remain explicit mathematical choices, not physical particle admissions.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
import json
from check_typed_spin_channels import decode,eye,kron,conjugate_matrix,power,trace,encoded,matrix_columns,tensor_action,basis_vectors
from check_pentachoron_spin_interfaces import A,CI,S2,S3,mm,adj,scale,add,pauli

ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'

def matrix(raw):return tuple(tuple(decode(x) for x in row) for row in raw)
def zero(rows,cols):return tuple(tuple(A() for _ in range(cols)) for _ in range(rows))
def act_cells(S,W):
    out=[[A() for _ in range(2)] for _ in range(10)]
    for cell in range(5):
        rows=mm(S,W[2*cell:2*cell+2]);target=(cell+1)%5
        out[2*target:2*target+2]=rows
    return tuple(tuple(row) for row in out)
def transport_matrix(S):
    out=[[A() for _ in range(10)] for _ in range(10)]
    for cell in range(5):
        for i in range(2):
            for j in range(2):out[2*((cell+1)%5)+i][2*cell+j]=S[i][j]
    return tuple(tuple(row) for row in out)
def act_faces(S,F,order):
    out=[[A() for _ in range(2)] for _ in range(len(F))];index={tuple(key):i for i,key in enumerate(order)}
    for i,(c,d) in enumerate(order):
        target=index[( (c+1)%5,(d+1)%5)]
        out[2*target:2*target+2]=mm(S,F[2*i:2*i+2])
    return tuple(tuple(row) for row in out)

def main():
    source_path=BASE/'results/pentachoron_cycle_transport.json';typed_path=BASE/'results/typed_spin_channels.json'
    source=json.loads(source_path.read_text(encoding='utf-8'));typed=json.loads(typed_path.read_text(encoding='utf-8'))
    assert source['verification_passed'] and typed['verification_passed']
    for name,digest in source['source_hashes'].items():assert sha256((ROOT/name).read_bytes()).hexdigest()==digest
    for name,digest in typed['source_hashes'].items():assert sha256((BASE/name).read_bytes()).hexdigest()==digest
    spin_path=BASE/'results/pentachoron_spin_interfaces.json';spin=json.loads(spin_path.read_text(encoding='utf-8'));assert spin['verification_passed']
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    Ps=matrix(typed['input_scalar_projector']);Pv=matrix(typed['input_vector_projector'])
    M2=matrix(typed['two_output_map']);M3=matrix(typed['three_output_map'])
    sigma=[pauli(tuple(A(i==j) for i in range(3))) for j in range(3)]
    reports=[];naive_failures=[]
    for row in source['chirality_results']:
        chirality=row['chirality'];S=matrix(row['spin_lift']);T=transport_matrix(S)
        extension=row['conditional_cycle_defect_extension']
        encodings=[extension['attachment_encoding'],extension['opposite_lift_attachment_encoding']]
        Ws=[matrix(item['cell_isometry']) for item in encodings];projections=[mm(W,adj(W)) for W in Ws]
        low=add(*projections);low_energy=decode(row['low_energy'])
        high_row=next(r for r in spin['chirality_results'] if r['chirality']==chirality);high_energy=decode(high_row['higher_energy'])
        L=add(scale(low_energy,low),scale(high_energy,add(eye(10),scale(A(-1),low))))
        X=add(scale(A(2),eye(10)),scale(A(-1),add(T,adj(T))))
        check('low_rank_four_'+str(chirality),trace(low)==4 and mm(low,low)==low)
        check('doublet_orthogonality_'+str(chirality),mm(adj(Ws[0]),Ws[1])==zero(2,2))
        check('native_mismatch_cycle_commutes_'+str(chirality),mm(L,T)==mm(T,L))
        for option,(encoding,W) in enumerate(zip(encodings,Ws)):
            key=str(chirality)+'_'+str(option);F=matrix(encoding['face_isometry'])
            check('cell_encoding_isometric_'+key,mm(adj(W),W)==eye(2))
            check('face_encoding_isometric_'+key,mm(adj(F),F)==eye(2))
            TW=act_cells(S,W);D=mm(adj(W),TW)
            check('cell_transport_intertwiner_'+key,TW==mm(W,D))
            check('face_transport_intertwiner_'+key,act_faces(S,F,encoding['face_order'])==mm(F,D))
            check('effective_doublet_transport_unitary_'+key,mm(adj(D),D)==eye(2) and power(D,5)==scale(A(-1),eye(2)))
            check('effective_doublet_det_one_'+key,D[0][0]*D[1][1]-D[0][1]*D[1][0]==1)
            check('native_mismatch_doublet_eigenvalue_'+key,mm(L,W)==scale(low_energy,W))
            # The extra cycle defect is declared, not supplied by bare geometry.
            energy=decode(extension['ground_energy'] if option==0 else next(r['total_energy'] for r in extension['complete_joint_spectrum'] if r['seam_sector']=='low' and r['dimension']==2 and r['total_energy']!=extension['ground_energy']))
            check('conditional_operation_energy_compression_'+key,mm(add(L,X),W)==scale(energy,W))
            J=kron(W,conjugate_matrix(W));pairD=kron(D,conjugate_matrix(D))
            check('native_pair_isometry_'+key,len(J)==100 and mm(adj(J),J)==eye(4))
            check('native_pair_cycle_covariance_'+key,kron(TW,conjugate_matrix(TW))==mm(J,pairD) and power(pairD,5)==eye(4))
            HW=mm(add(L,X),W)
            native_pair_on_J=add(kron(HW,conjugate_matrix(W)),kron(W,conjugate_matrix(HW)))
            check('native_pair_energy_compression_'+key,native_pair_on_J==scale(2*energy,J))
            check('native_pair_scalar_vector_covariance_'+key,mm(Ps,pairD)==mm(pairD,Ps) and mm(Pv,pairD)==mm(pairD,Pv))
            check('native_pair_scalar_is_trivial_'+key,mm(pairD,Ps)==Ps)
            R=tuple(tuple(trace(mm(mm(mm(sigma[i],D),sigma[j]),adj(D)))/2 for j in range(3)) for i in range(3))
            check('native_effective_vector_action_'+key,mm(adj(R),R)==eye(3) and power(R,5)==eye(3))
            epsilon={v:A((-1)**sum(v[i]>v[j] for i in range(3) for j in range(i+1,3)))/(S2*S3) for v in basis_vectors(3,3) if len(set(v))==3}
            check('native_scalar_record_internal_covariance_'+key,tensor_action(R,epsilon)==epsilon)
            ambientR=tuple(tuple(trace(mm(mm(mm(sigma[i],S),sigma[j]),adj(S)))/2 for j in range(3)) for i in range(3))
            original_output_covariance=matrix_columns(mm(M3,pairD),basis_vectors(3,3))==[tensor_action(ambientR,v) for v in matrix_columns(M3,basis_vectors(3,3))]
            check('ambient_output_covariance_requires_doublet_choice_'+key,original_output_covariance==(S==D))
            for name,M,k in [('two',M2,2),('vector_three',M3,3)]:
                check('native_to_output_covariance_'+name+'_'+key,matrix_columns(mm(M,pairD),basis_vectors(3,k))==[tensor_action(R,v) for v in matrix_columns(M,basis_vectors(3,k))])
                attachment=mm(M,adj(J))
                check('native_vertex_recovers_typed_map_'+name+'_'+key,mm(attachment,J)==M)
                check('native_vertex_retains_complement_as_dark_'+name+'_'+key,attachment==mm(mm(attachment,J),adj(J)))
            # No dense 100x100 projection is necessary: these identities retain
            # its complete factorization rather than deleting residual records.
            check('native_complement_not_quotiented_'+key,add(Ps,Pv)==eye(4) and len(J)-len(J[0])==96)
            naive=S==D;naive_failures.append(not naive)
            reports.append({'chirality':chirality,'doublet_option':option,'cell_encoding':encoded(W),
                'face_encoding':encoded(F),'face_order':encoding['face_order'],
                'effective_cycle_D':encoded(D),'effective_vector_R':encoded(R),
                'naive_local_spin_lift_equals_D':naive,'original_ambient_vector_output_covariant':original_output_covariance,'native_pair_encoding':'J=W tensor conjugate(W), 100x4; factored exactly',
                'single_mismatch_energy':low_energy.record(),'single_conditional_energy':energy.record(),
                'pair_conditional_core_energy':(2*energy).record(),
                'retained_space_dimensions':{'native_single':10,'native_pair':100,'selected_pair':4,'unselected_low_pair':12,'full_pair_complement':96}})
    check('naive_doublet_spin_identification_is_not_universal',any(naive_failures) and not all(naive_failures))
    result={'verification_passed':all(checks.values()),'checks':checks,'adapter_reports':reports,
        'vertex_law':'A_c=B_c J^dagger from full native pair records; Ps/Pv and orbital vertices remain typed. All 96 complementary native coordinates remain in the full Hamiltonian.',
        'source_energy_rule':'Native L reconstructed from its verified two spectral projectors/energies; optional L+(T-I)^dagger(T-I) energy uses the predecessor equal-weight convention.',
        'native_selfenergy_pullback':'Sigma_native(z)=J Sigma_encounter(z) J^dagger, finite-rank on the retained 100-state native pair space; complement is uncoupled by this explicit vertex choice.',
        'core_replacement':'For each selected option, the compressed native conditional pair energy is 2e I4, not the old freely declared 6I4 fixture.',
        'physical_coupling_admitted':False,
        'qualifications':['Conjugate native partner is a declared mathematical copy, not a derived physical positron.',
            'Both available native doublets are audited; this computation does not select one physically.',
            'Relative orbital/native energy units and every cross-channel lambda remain supplied, not source-derived.',
            'Optional cycle-defect energy is not native time evolution and supplies no physical clock.',
            'The scalar Slater-record off-center dispersive response remains a separate unresolved calculation.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            (source_path,spin_path,typed_path,Path(__file__),BASE/'checkers/check_pentachoron_cycle_transport.py',BASE/'checkers/check_typed_spin_channels.py',BASE/'checkers/check_pentachoron_spin_interfaces.py')}}
    (BASE/'results/native_spinor_pair_adapter.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'adapters':[
        {'chirality':r['chirality'],'option':r['doublet_option'],'naive_spin_identification':r['naive_local_spin_lift_equals_D'],'pair_dimensions':r['retained_space_dimensions']} for r in reports]},indent=2))

if __name__=='__main__':main()
