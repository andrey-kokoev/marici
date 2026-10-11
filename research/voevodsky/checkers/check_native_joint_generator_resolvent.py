"""Iteration 4: admit the actual stored phase/alignment/seam energy, retain
its extra modes, and verify the exact visible Schur resolvent polynomially.
The joint generator is a declared equal-weight positive-defect construction.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
from check_native_adapter_collective_closure import F,cmul,cdiv,apply,inner,indicator,unit,Span,closure,orthogonalize,restricted,same

BASE=Path(__file__).resolve().parents[1]
def zero(n,m=None):return [[F() for _ in range(n if m is None else m)] for _ in range(n)]
def identity(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def add(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(s,A):return [[s*x for x in row] for row in A]
def multiply(A,B):
    out=zero(len(A),len(B[0]))
    for i,row in enumerate(A):
        for k,a in enumerate(row):
            if a:
                for j,b in enumerate(B[k]):
                    if b:out[i][j]=out[i][j]+a*b
    return out

def equal(A,B):return len(A)==len(B) and all(same(a,b) for a,b in zip(A,B))
def sparse(A):return [{j:x for j,x in enumerate(row) if x} for row in A]
def dense(A):return [[row.get(j,F()) for j in range(len(A))] for row in A]
def block(A,rows,cols):return [[A[i][j] for j in cols] for i in rows]
def encode_matrix(A):return [[x.encoded() for x in row] for row in A]

def psd_rank(A):
    """Exact LDL elimination; zero pivots must have zero remaining row."""
    A=[list(row) for row in A];rank=0
    assert all(A[i][j]==A[j][i] for i in range(len(A)) for j in range(len(A)))
    for k in range(len(A)):
        pivot=A[k][k]
        if not pivot:
            assert all(not A[k][j] for j in range(k,len(A)));continue
        assert pivot.positive();rank+=1;inverse=pivot.inverse()
        for i in range(k+1,len(A)):
            for j in range(i,len(A)):
                A[i][j]=A[i][j]-A[i][k]*inverse*A[k][j];A[j][i]=A[i][j]
    return rank

def polynomial_product(a,b):
    out=[F() for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
    return out

def matrix_polynomial_product(a,b):
    out=[zero(len(a[0]),len(b[0][0])) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=add(out[i+j],multiply(x,y))
    return out

def characteristic_and_adjugate(A):
    """Faddeev-LeVerrier in an exact field, followed by full polynomial checks.
    Returned coefficient lists are ascending powers of z.
    """
    n=len(A);B=identity(n);coefficients=[F(1)];adjugate_desc=[]
    for k in range(1,n+1):
        adjugate_desc.append(B)
        AB=multiply(A,B);c=-sum((AB[i][i] for i in range(n)),F())*Q(1,k)
        coefficients.append(c);B=add(AB,scale(c,identity(n)))
    assert equal(B,zero(n))
    polynomial=list(reversed(coefficients));adjugate=list(reversed(adjugate_desc))
    pencil=[scale(-1,A),identity(n)]
    expected=[scale(c,identity(n)) for c in polynomial]
    assert all(equal(a,b) for a,b in zip(matrix_polynomial_product(pencil,adjugate),expected))
    assert all(equal(a,b) for a,b in zip(matrix_polynomial_product(adjugate,pencil),expected))
    return polynomial,adjugate


def main():
    paths={name:BASE/'results'/file for name,file in {
        'closure':'native_adapter_collective_closure.json','adapter':'native_rim_phase_adapter.json',
        'intrinsic':'belt_three_by_twelve_store.json','energy':'native_operation_energy_lift_store.json'}.items()}
    previous,adapter,store,energy=[json.loads(paths[k].read_text(encoding='utf-8')) for k in ('closure','adapter','intrinsic','energy')]
    for receipt in (previous,adapter):
        assert receipt['verification_passed']
        for name,digest in receipt['source_hashes'].items():assert sha256((BASE/name).read_bytes()).hexdigest()==digest
    assert energy['source_sha256']['belt']==sha256(paths['intrinsic'].read_bytes()).hexdigest()
    native=energy['carriers']['belt'];assert len(native['seam_projectors'])==21
    z=[(Q(c['selected_numerator'][0]),Q(c['selected_numerator'][2])) for c in store['coordinates']]
    assert list(map(Q,native['metric_denominators']))==[Q(c['d']) for c in store['coordinates']]
    metric=[F(*v) for v in previous['metric']];n=len(metric);assert n==48
    def convert(entries):
        out=[{} for _ in range(n)]
        for i,j,raw in entries:
            a,b,c,d=map(Q,raw);assert b==d==0
            value=cdiv(cmul((a,c),z[j]),z[i]);assert value[1]==0
            if value[0]:out[i][j]=F(value[0])
        return out
    A=convert(native['entries']);Aphase=convert(native['native_energy_entries'])
    seams=[convert(s['entries']) for s in native['seam_projectors']]
    U=[{i:F(1)} for i in range(n)]
    for port in previous['ports']:
        slots=port['carrier_slots']+port['belt_slots']
        for i,k in enumerate(slots):
            U[k]={slots[j]:F(*raw[:2]) for j,raw in enumerate(adapter['adapter_matrix'][i]) if any(Q(v) for v in raw)}
    # Native energy is zero-extended to the carrier coordinates; it is not I-L.
    # In K=4H/pi units the inherited involution gate contributes 2(I-U).
    gate=scale(2,add(identity(n),scale(-1,dense(U))))
    K=sparse(add(dense(A),gate))
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    check('actual_native_energy_contains_all_21_seams',equal(dense(A),add(dense(Aphase),scale(4,sum_matrices([dense(s) for s in seams],n)))))
    check('native_energy_zero_extended_to_carriers',all(not row for row in A[36:]) and all(j<36 for row in A for j in row))
    check('joint_generator_metric_self_adjoint',all(metric[i]*K[i].get(j,F())==metric[j]*K[j].get(i,F()) for i in range(n) for j in range(n)))
    check('native_energy_C3_covariant',all(A[(i+12)%36].get((j+12)%36,F())==A[i].get(j,F()) for i in range(36) for j in range(36)))
    seeds=[indicator(n,range(36)),indicator(n,range(36,42)),indicator(n,range(42,48))]
    old_basis=[[F(*v) for v in row] for row in previous['collective_orthogonal_basis']]
    old_span=Span(n)
    for i,v in enumerate(old_basis):old_span.add(v,{'old':i})
    leakage_columns=sum(bool(any(old_span.reduce(apply(A,v))[0])) for v in old_basis)
    check('nine_space_is_not_invariant_under_actual_energy',leakage_columns>0)
    generator_closure=closure(seeds,{'K':K},n)
    operation_closure=closure(seeds,{'U':U,'native_energy':A},n)
    check('joint_generator_and_operation_closures_are_eleven',len(generator_closure.rows)==len(operation_closure.rows)==11 and all(not any(generator_closure.reduce(v)[0]) for v in operation_closure.rows))
    check('earlier_nine_space_is_retained',all(not any(generator_closure.reduce(v)[0]) for v in old_basis))
    belt_norm=sum(metric[:36],F());sector_norm=sum(metric[:12],F())
    old_ops={key:[{} for _ in range(n)] for key in ('L','G','N')}
    for i in range(36):
        old_ops['L'][i]={j:metric[j]/sector_norm for j in range(36) if i//12==j//12}
        old_ops['G'][i]={j:F(Q(1,3)) for j in range(36) if i%12==j%12}
        old_ops['N'][i]={j:metric[j]/belt_norm for j in range(36)}
    for op in old_ops.values():
        for i in range(36,48):op[i][i]=F(1)
    check('all_earlier_L_G_N_stages_preserve_eleven_space',all(not any(generator_closure.reduce(apply(op,v))[0]) for op in old_ops.values() for v in generator_closure.rows))
    symmetric=closure([seeds[0]],{'K':K},n)
    antisymmetric=closure([[a-b for a,b in zip(seeds[1],seeds[2])]],{'K':K},n)
    check('specified_symmetric_input_closes_in_five',len(symmetric.rows)==5 and not any(symmetric.reduce([a+b for a,b in zip(seeds[1],seeds[2])])[0]))
    check('antisymmetric_input_closes_in_six',len(antisymmetric.rows)==6)
    check('symmetric_and_antisymmetric_blocks_are_orthogonal',all(inner(a,b,metric)==0 for a in symmetric.rows for b in antisymmetric.rows))
    # Use rational geometry/energy-generated vectors for a readable basis, not
    # parameter-dependent Krylov coordinates involving large nested radicals.
    geometric=[indicator(n,slots) for slots in previous['geometric_collective_supports']]
    simple=closure(seeds+geometric,{'native_energy':A},n)
    check('rational_basis_spans_full_eleven_space',len(simple.rows)==11 and all(not any(generator_closure.reduce(v)[0]) for v in simple.rows))
    basis,norms=orthogonalize(simple.rows,metric)
    smallK=restricted(K,basis,metric,norms);smallA=restricted(A,basis,metric,norms);smallU=restricted(U,basis,metric,norms)
    smallGate=scale(2,add(identity(11),scale(-1,smallU)))
    gram=lambda B:[[norms[i]*v for v in row] for i,row in enumerate(B)]
    native_rank=psd_rank(gram(smallA));gate_rank=psd_rank(gram(smallGate));joint_rank=psd_rank(gram(smallK))
    check('restricted_native_and_gate_energies_positive',native_rank>=0 and gate_rank>=0)
    check('joint_positive_energy_has_one_zero_mode',joint_rank==10)
    check('joint_is_exact_sum_of_retained_ingredients',equal(smallK,add(smallA,smallGate)))
    # Positive extension is inherited on the full space from the freshly rerun
    # native checker and U's metric-unitary involution certificate.
    check('no_interaction_without_adapter_on_selected_inputs',all(not any(apply(A,v)) for v in seeds))
    visible=range(3);hidden=range(3,11)
    Kpp=block(smallK,visible,visible);Kpq=block(smallK,visible,hidden);Kqp=block(smallK,hidden,visible);Kqq=block(smallK,hidden,hidden)
    hmetric=norms[3:]
    check('hidden_block_positive_definite',psd_rank([[hmetric[i]*v for v in row] for i,row in enumerate(Kqq)])==8)
    coupling_columns=[[Kqp[i][j] for i in range(8)] for j in range(3)]
    hidden_closure=closure(coupling_columns,{'Kqq':sparse(Kqq)},8)
    check('all_eight_hidden_coordinates_are_reachable',len(hidden_closure.rows)==8)
    # Full polynomial identities, not a resolvent check at a few sampled energies.
    print('Computing exact 11-state and 8-state polynomial resolvents...',flush=True)
    D,Adj=characteristic_and_adjugate(smallK);Dq,Adjq=characteristic_and_adjugate(Kqq)
    sigma=[multiply(multiply(Kpq,C),Kqp) for C in Adjq]
    adj_visible=[block(C,visible,visible) for C in Adj]
    effective_pencil=[zero(3) for _ in range(len(Dq)+1)]
    for i,coefficient in enumerate(Dq):
        effective_pencil[i]=add(effective_pencil[i],scale(-coefficient,Kpp))
        effective_pencil[i+1]=add(effective_pencil[i+1],scale(coefficient,identity(3)))
    for i,C in enumerate(sigma):effective_pencil[i]=add(effective_pencil[i],scale(-1,C))
    rhs=[scale(c,identity(3)) for c in polynomial_product(Dq,D)]
    check('full_visible_Schur_polynomial_identity_left',all(equal(a,b) for a,b in zip(matrix_polynomial_product(effective_pencil,adj_visible),rhs)))
    check('full_visible_Schur_polynomial_identity_right',all(equal(a,b) for a,b in zip(matrix_polynomial_product(adj_visible,effective_pencil),rhs)))
    check('full_adjugate_and_hidden_adjugate_certified',len(D)==12 and len(Dq)==9)
    check('zero_is_full_mode_not_hidden_block_pole',D[0]==0 and Dq[0]!=0)
    check('self_energy_is_not_zero',any(x for row in sigma[-1] for x in row))
    numerator_lower=[C[1][0] for C in Adj];numerator_upper=[C[2][0] for C in Adj]
    equal_outputs=all(a==b for a,b in zip(numerator_lower,numerator_upper))
    check('lower_upper_port_response_symmetry',equal_outputs and any(numerator_lower))
    check('equal_output_norms_for_flux_comparison',norms[1]==norms[2])
    # Source collective is a port excitation, not a two-particle tensor-product
    # state; equal responses here must not be relabelled as photon multiplicities.
    result={'verification_passed':all(checks.values()),'checks':checks,
        'generator_contract':'K = K_native_with_seams + 2(I-U); physical formal convention H=(pi/4)K. Equal weighting is declared, not derived.',
        'full_dimension':48,'previous_closure_dimension':9,'energy_leakage_columns':leakage_columns,
        'joint_cyclic_dimension':11,'visible_dimension':3,'hidden_dimension':8,'hidden_reachable_dimension':len(hidden_closure.rows),
        'prepared_input_cyclic_dimensions':{'native_belt_only':len(symmetric.rows),'carrier_difference':len(antisymmetric.rows)},
        'symmetric_and_antisymmetric_invariant_blocks_orthogonal':True,
        'positive_ranks':{'native':native_rank,'gate':gate_rank,'joint':joint_rank},
        'basis':[[x.encoded() for x in row] for row in basis],'gram_diagonal':[x.encoded() for x in norms],
        'joint_generator':encode_matrix(smallK),'native_generator':encode_matrix(smallA),'adapter':encode_matrix(smallU),
        'characteristic_coefficients_ascending':[x.encoded() for x in D],
        'hidden_characteristic_coefficients_ascending':[x.encoded() for x in Dq],
        'self_energy_numerator_coefficients_ascending':[encode_matrix(C) for C in sigma],
        'visible_resolvent_numerator_coefficients_ascending':[encode_matrix(C) for C in adj_visible],
        'effective_operator':'Kpp + Sigma(z), Sigma(z)=self_energy_numerator(z)/det(zI-Kqq)',
        'same_input_lower_upper_resolvent_numerators':equal_outputs,
        'qualification':['Three visible states are native belt/proton-port/electron-port characters, not survival/2gamma/3gamma states.',
            'Positivity and metric unitarity do not derive physical energies, holding, binding, or a clock.',
            'Closure is for this joint equal-weight generator and retained native-energy/adapter library, not arbitrary independently controlled seams.',
            'Full electron spinor coupling remains absent; carrier native energy is zero-extended in this interface fixture.',
            'Resolvents require spectral exclusions; the eliminated expression additionally excludes hidden-block eigenvalues.',
            'K is a stationary registered-interface fixture; a continuously moving-port implementation and its control energy are not synthesized.',
            'Open-channel self-energies, thresholds and flux normalization are not yet included.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in list(paths.values())+[Path(__file__),BASE/'checkers/check_native_adapter_collective_closure.py',BASE/'checkers/check_native_operation_energy_lift.py']}}
    (BASE/'results/native_joint_generator_resolvent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('verification_passed','checks','joint_cyclic_dimension','hidden_dimension','positive_ranks','same_input_lower_upper_resolvent_numerators')},indent=2))

def sum_matrices(matrices,n):
    out=zero(n)
    for A in matrices:out=add(out,A)
    return out

if __name__=='__main__':main()
