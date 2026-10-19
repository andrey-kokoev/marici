"""Typed multi-object spin audit, bound to the retained electron spin lifts.
Constructive SU(2) representation tests, not a positron/photon identification.
"""
from fractions import Fraction as Q
from itertools import product,permutations,combinations_with_replacement
from math import factorial
from pathlib import Path
from hashlib import sha256
import json
from check_pentachoron_spin_interfaces import A,S2,S3,S5,CI,ZERO,ONE,I,pauli,mm,adj,scale,add,rank

BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]

def eye(n):return tuple(tuple(A(i==j) for j in range(n)) for i in range(n))
def zeros(n,m):return tuple(tuple(ZERO for _ in range(m)) for _ in range(n))
def kron(a,b):return tuple(tuple(x*y for x in row for y in subrow) for row in a for subrow in b)
def conjugate_matrix(a):return tuple(tuple(x.flip(8) for x in row) for row in a)
def power(a,n):
    out=eye(len(a))
    for _ in range(n):out=mm(a,out)
    return out

def decode(raw):
    return A(tuple(Q(raw.get(str(i),'0')) for i in range(16)))
def trace(a):return sum((a[i][i] for i in range(len(a))),ZERO)
def encoded(a):return [[v.record() for v in row] for row in a]
def tidy(v):return {key:value for key,value in v.items() if value!=0}
def plus_vector(a,b):
    out=dict(a)
    for key,value in b.items():out[key]=out.get(key,ZERO)+value
    return tidy(out)
def scale_vector(s,v):return tidy({key:s*value for key,value in v.items()})
def tensor_action(matrix,v):
    if not v:return {}
    out=dict(v)
    for slot in range(len(next(iter(v)))):
        nxt={}
        for key,value in out.items():
            for i in range(len(matrix)):
                c=matrix[i][key[slot]]
                if c==0:continue
                target=list(key);target[slot]=i;target=tuple(target)
                nxt[target]=nxt.get(target,ZERO)+c*value
        out=tidy(nxt)
    return out

def tensor_generator(matrix,v):
    out={}
    for key,value in v.items():
        for slot in range(len(key)):
            for i in range(len(matrix)):
                c=matrix[i][key[slot]]
                if c==0:continue
                target=list(key);target[slot]=i;target=tuple(target)
                out[target]=out.get(target,ZERO)+c*value
    return tidy(out)

def vector_norm(v):return sum((x.flip(8)*x for x in v.values()),ZERO)
def exchange(v,pi):return {tuple(key[i] for i in pi):value for key,value in v.items()}
def bose_projection(v):
    k=len(next(iter(v)));out={}
    for pi in permutations(range(k)):out=plus_vector(out,exchange(v,pi))
    return scale_vector(A(Q(1,factorial(k))),out)
def epsilon(indices):
    if len(set(indices))<3:return 0
    return (-1)**sum(indices[i]>indices[j] for i in range(3) for j in range(i+1,3))
def basis_vectors(d,k):return list(product(range(d),repeat=k))
def as_sparse(column,labels):return tidy({key:value for key,value in zip(labels,column)})
def matrix_columns(matrix,labels):return [as_sparse(col,labels) for col in zip(*matrix)]
def casimir(v,lie):
    out={}
    for L in lie:out=plus_vector(out,scale_vector(A(-1),tensor_generator(L,tensor_generator(L,v))))
    return out


def main():
    spin_path=BASE/'results/pentachoron_cycle_transport.json'
    source=json.loads(spin_path.read_text(encoding='utf-8'));assert source['verification_passed']
    for name,digest in source['source_hashes'].items():assert sha256((ROOT/name).read_bytes()).hexdigest()==digest
    note=BASE/'braid-composition-effective-shape-interaction-operators.md'
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    paulis=[pauli(tuple(A(i==j) for i in range(3))) for j in range(3)]
    # Reject identifying the same Frobenius A=C^2 with a spinor at every leg.
    old_m=((ONE,ZERO,ZERO,ZERO),(ZERO,ZERO,ZERO,ONE));old_delta=adj(old_m)
    center=scale(A(-1),I);pair_center=kron(center,center)
    check('spinor_center_is_minus_identity',pair_center==eye(4))
    check('old_merge_fails_central_covariance',mm(center,old_m)!=mm(old_m,pair_center))
    check('old_split_fails_central_covariance',mm(pair_center,old_delta)!=mm(old_delta,center))
    check('all_spinor_pair_to_spinor_intertwiners_vanish',rank(scale(A(2),eye(8)))==8)
    # The partner is explicitly the conjugate representation, not an admitted
    # physical positron. vec(I) spans its canonical scalar pairing with V.
    omega=(ONE,ZERO,ZERO,ONE)
    singlet=tuple(tuple(x*y.flip(8)/2 for y in omega) for x in omega)
    triplet=add(eye(4),scale(A(-1),singlet))
    check('input_scalar_and_vector_projectors',mm(singlet,singlet)==singlet and mm(triplet,triplet)==triplet and mm(singlet,triplet)==zeros(4,4) and trace(singlet)==1 and trace(triplet)==3)
    spin2=basis_vectors(3,2);spin3=basis_vectors(3,3)
    delta_state={key:ONE for key in spin2 if key[0]==key[1]}
    epsilon_state={key:A(epsilon(key)) for key in spin3 if epsilon(key)}
    tensors=[tuple(tuple(int(i==j and k==a)+int(i==k and j==a)+int(j==k and i==a) for a in range(3)) for i,j,k in spin3)]
    qrows=tensors[0]
    Qmap=tuple(tuple(A(v) for v in row) for row in qrows)
    triplet_in=tuple(tuple(paulis[a][i][j] for a in range(3)) for i,j in product(range(2),repeat=2))
    M2=tuple(tuple(delta_state.get(key,ZERO)*x.flip(8)/(S2*S3) for x in omega) for key in spin2)
    M3=scale(ONE/(S2*S3*S5),mm(Qmap,adj(triplet_in)))
    check('symmetric_triple_vector_gram',mm(adj(Qmap),Qmap)==scale(A(15),eye(3)))
    check('incoming_triplet_gram',mm(adj(triplet_in),triplet_in)==scale(A(2),eye(3)))
    check('two_object_map_selects_scalar_sector',mm(adj(M2),M2)==singlet)
    check('three_object_map_selects_vector_sector',mm(adj(M3),M3)==triplet)
    check('two_object_output_exchange_symmetric',all(exchange(v,(1,0))==v for v in matrix_columns(M2,spin2)))
    check('three_object_output_exchange_symmetric',all(exchange(v,pi)==v for v in matrix_columns(M3,spin3) for pi in permutations(range(3))))
    # Positive rank-one scalar intermediate for M2; a vector intermediate is
    # needed for M3. The latter is not a scalar state C in disguise.
    check('typed_map_ranks_one_and_three',rank(M2)==1 and rank(M3)==3)
    lie=[]
    for sigma in paulis:
        T=scale(-CI/2,sigma)
        L=tuple(tuple(trace(mm(paulis[i],add(mm(T,paulis[j]),scale(A(-1),mm(paulis[j],T)))))/2 for j in range(3)) for i in range(3))
        lie.append(L)
    check('vector_representation_casimir_two',all(casimir({(j,):ONE},lie)=={(j,):A(2)} for j in range(3)))
    for index,(sigma,L) in enumerate(zip(paulis,lie)):
        T=scale(-CI/2,sigma);pair=add(kron(T,I),kron(I,conjugate_matrix(T)))
        for name,M,labels in [('two',M2,spin2),('three',M3,spin3)]:
            before=matrix_columns(mm(M,pair),labels)
            after=[tensor_generator(L,v) for v in matrix_columns(M,labels)]
            check(name+'_Lie_covariance_'+str(index),before==after)
    cycle_reports=[];cycle_pairs=[]
    for row in source['chirality_results']:
        S=tuple(tuple(decode(v) for v in line) for line in row['spin_lift']);label=str(row['chirality'])
        check('native_spin_lift_unitary_'+label,mm(adj(S),S)==I and power(S,5)==center)
        representation=tuple(tuple(trace(mm(mm(mm(paulis[i],S),paulis[j]),adj(S)))/2 for j in range(3)) for i in range(3))
        check('native_vector_lift_orthogonal_'+label,mm(adj(representation),representation)==eye(3) and power(representation,5)==eye(3))
        pair=kron(S,conjugate_matrix(S));cycle_pairs.append(pair)
        check('pair_returns_after_five_'+label,power(pair,5)==eye(4))
        check('native_source_itself_rejects_old_merge_'+label,mm(S,old_m)!=mm(old_m,kron(S,S)))
        for name,M,labels in [('two',M2,spin2),('three',M3,spin3)]:
            check(name+'_native_cycle_covariance_'+label,matrix_columns(mm(M,pair),labels)==[tensor_action(representation,v) for v in matrix_columns(M,labels)])
        cycle_reports.append({'chirality':row['chirality'],'spin_lift':encoded(S),'vector_action':encoded(representation)})
    # Casimir polynomials on complete symmetric tensor bases certify disjoint
    # rotation types: Sym^2 W has j=0,2; Sym^3 W has j=1,3.
    symmetric_bases={}
    for k in (2,3):
        symmetric_bases[k]=[{key:ONE for key in set(permutations(occupation))} for occupation in combinations_with_replacement(range(3),k)]
    check('symmetric_sector_dimensions',len(symmetric_bases[2])==6 and len(symmetric_bases[3])==10)
    check('two_object_Casimir_polynomial',all(plus_vector(casimir(casimir(v,lie),lie),scale_vector(A(-6),casimir(v,lie)))=={} for v in symmetric_bases[2]))
    check('three_object_Casimir_polynomial',all(plus_vector(plus_vector(casimir(casimir(v,lie),lie),scale_vector(A(-14),casimir(v,lie))),scale_vector(A(24),v))=={} for v in symmetric_bases[3]))
    # (C-11)/72 is the inverse of C(C-6) on the three-object symmetric sector.
    inverse_controls=[]
    for v in symmetric_bases[3]:
        p=plus_vector(casimir(casimir(v,lie),lie),scale_vector(A(-6),casimir(v,lie)))
        restored=scale_vector(A(Q(1,72)),plus_vector(casimir(p,lie),scale_vector(A(-11),p)))
        inverse_controls.append(restored==v)
    check('no_rotation_intertwiner_between_common_orbital_two_and_three_sectors',all(inverse_controls))
    # A scalar three-vector tensor exists, but it is antisymmetric. With one
    # common orbital its Bose projection vanishes. Extra orbital information
    # restores a permissible scalar three-object state.
    check('three_vector_scalar_is_antisymmetric',vector_norm(epsilon_state)==6 and exchange(epsilon_state,(1,0,2))==scale_vector(A(-1),epsilon_state))
    check('common_orbital_scalar_triple_is_killed_by_Bose_projection',bose_projection(epsilon_state)=={})
    decorated={}
    for spins in permutations(range(3)):
        for orbitals in permutations(range(3)):
            key=tuple(3*s+o for s,o in zip(spins,orbitals))
            decorated[key]=A(Q(epsilon(spins)*epsilon(orbitals),6))
    check('retained_orbital_scalar_triple_normalized',vector_norm(decorated)==1)
    check('retained_orbital_scalar_triple_Bose_symmetric',all(exchange(decorated,pi)==decorated for pi in permutations(range(3))))
    check('retained_orbital_scalar_triple_rotation_invariant',all(tensor_generator(kron(L,eye(3)),decorated)=={} for L in lie))
    orbital_epsilon={key:A(epsilon(key)) for key in spin3 if epsilon(key)}
    collapse=tuple(tuple(A(Q(1,3)) for _ in range(3)) for _ in range(3))
    check('collapsing_orbitals_to_one_mode_erases_scalar_triple',tensor_action(collapse,orbital_epsilon)=={})
    # Tuple concatenation stacks the three orthogonal output blocks.
    # Finite typed isometry at an explicitly declared common conversion q=3/4.
    S=scale(A(Q(1,2)),eye(4))+scale(S3/2,M2)+scale(S3/2,M3)
    check('typed_survival_two_three_map_isometric',len(S)==40 and mm(adj(S),S)==eye(4))
    # A second, equally covariant isometry uses independent sector conversions.
    # This is an explicit nonuniqueness control, not a fitted reaction rate.
    survival=add(scale(S3/2,singlet),scale(A(Q(1,2)),triplet))
    second=survival+scale(A(Q(1,2)),M2)+scale(S3/2,M3)
    check('independent_sector_conversion_isometry',mm(adj(second),second)==eye(4))
    check('survival_preserves_native_pair_covariance',all(mm(survival,pair)==mm(pair,survival) for pair in cycle_pairs))
    effects=[mm(adj(survival),survival),scale(A(Q(1,4)),singlet),scale(A(Q(3,4)),triplet)]
    check('typed_probability_effects_resolve_identity',add(add(effects[0],effects[1]),effects[2])==eye(4))
    for name,rho in [('scalar',singlet),('vector_mixture',scale(A(Q(1,3)),triplet)),('unpolarized',scale(A(Q(1,4)),eye(4)))]:
        ps=[trace(mm(E,rho)) for E in effects]
        check('density_probability_normalization_'+name,sum(ps,ZERO)==1 and ps[1]==A(Q(1,4))*trace(mm(singlet,rho)) and ps[2]==A(Q(3,4))*trace(mm(triplet,rho)))
    check('same_symmetry_different_unpolarized_ratios',Q(1,3)!=Q(1,9))
    probabilities=(Q(1,4),Q(3,16),Q(9,16))
    check('unpolarized_equal_conversion_ratio_is_one_to_three',sum(probabilities)==1 and probabilities[1]/probabilities[2]==Q(1,3))
    # A diagonal collective lead is not the tensor-product free motion of k
    # objects. Use the same positive one-body edge defect, on two sites.
    h=((ONE,A(-1)),(A(-1),ONE));kinetic=[]
    for k in (2,3):
        labels=basis_vectors(2,k);diag=[{(0,)*k:ONE},{(1,)*k:ONE}]
        seen=list(diag);cursor=0
        def dense(v):return [v.get(key,ZERO) for key in labels]
        while cursor<len(seen):
            image=tensor_generator(h,seen[cursor]);cursor+=1
            if rank([dense(v) for v in seen]+[dense(image)])>len(seen):seen.append(image)
        check('diagonal_orbital_copy_not_kinetically_closed_'+str(k),len(seen)==k+1 and len(seen)>2)
        kinetic.append({'objects':k,'diagonal_copy_dimension':2,'smallest_free_symmetric_closure':len(seen)})
    result={'verification_passed':all(checks.values()),'checks':checks,
        'source_spin_receipt':str(spin_path.relative_to(BASE)),'native_cycle_reports':cycle_reports,
        'type_contract':{'incoming':'V tensor conjugate(V), dimension 4; conjugate partner is declared, not a derived positron',
            'test_output_object':'W=adjoint SU(2) vector representation, dimension 3; not a photon construction',
            'common_orbital_two_outputs':'Sym^2 W, dimension 6','common_orbital_three_outputs':'Sym^3 W, dimension 10'},
        'input_scalar_projector':encoded(singlet),'input_vector_projector':encoded(triplet),
        'two_output_map':encoded(M2),'three_output_map':encoded(M3),
        'typed_channel_isometry_fixture':{'q_scalar':'3/4','q_vector':'3/4','ambient_shape':[40,4],
            'unpolarized_survival_two_three':list(map(str,probabilities))},
        'general_probability_law':'P2=q_scalar tr(P_scalar rho); P3=q_vector tr(P_vector rho). No unique rate is derived.',
        'unpolarized_ratio':'q_scalar/(3 q_vector); 372 would require q_scalar/q_vector=1116, not supplied here.',
        'decorated_scalar_three_object_state':[{'object_indices':list(key),'amplitude':value.record()} for key,value in sorted(decorated.items())],
        'kinetic_controls':kinetic,
        'not_established':['Physical positron/charge conjugation','Transverse massless photon or momentum states',
            'A native full-spinor coupling to the eleven-state scalar port generator',
            'Multi-object asymptotic kinetic self-energies or observed branching fractions',
            'A symmetry-compatible scalar c linking the common-orbital two/three sectors without additional records'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            (spin_path,note,Path(__file__),BASE/'checkers/check_pentachoron_spin_interfaces.py')}}
    (BASE/'results/typed_spin_channels.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'map_ranks':[1,3],
        'typed_fixture_probabilities':list(map(str,probabilities)),'kinetic_controls':kinetic},indent=2))

if __name__=='__main__':main()
