"""One actual seam: amplitude memory -> existing occupation register.

Exact metric-isometric encoding and unitary write/read; the existing g=0
occupation Hamiltonian supplies a hold phase. Control work is explicit, not
claimed autonomous. No extension to all noncommuting seams is inferred.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
from check_coupled_six_piece_belt import R, Z, ONE, add, mul, conj, scale, norm, positive, encoded
from check_constraint_energy_accounting import identity, plus, times, compose, adjoint
from check_phase_occupation_necessity import matrix
from check_native_phase_seam_memory import budget, energy, act, scalar
from check_belt_three_by_twelve import decode

BASE=Path(__file__).resolve().parents[1]


def sharp(A,domain,codomain):
    return {(j,i):scale(domain[j]/codomain[i],conj(v)) for (i,j),v in A.items()}


def block(A,offset):
    return {(i+offset,j+offset):v for (i,j),v in A.items()}


def main():
    receipt_path=BASE/'results/native_phase_seam_memory.json'
    receipt_raw=receipt_path.read_bytes()
    receipt=json.loads(receipt_raw)
    snapshot=BASE.parent.parent/receipt['source_snapshot']
    raw=snapshot.read_bytes()
    assert sha256(raw).hexdigest()==receipt['source_snapshot_sha256']
    bundle=json.loads(raw)
    native=bundle['records']['native']['carriers']['belt']
    intrinsic_raw=(BASE/'results/belt_three_by_twelve_store.json').read_bytes()
    assert sha256(intrinsic_raw).hexdigest()==receipt['intrinsic_source_sha256']
    intrinsic=json.loads(intrinsic_raw)
    d=tuple(map(F,native['metric_denominators']))
    w=[decode(c['selected_numerator']) for c in intrinsic['coordinates']]
    b=budget(w,d)
    N=matrix(native['return_entries'])
    K=matrix(native['native_energy_entries'])
    record=native['seam_projectors'][0]
    P=matrix(record['entries'])
    descriptor=receipt['record_frames'][18]
    assert descriptor['name']==f'seam_{record["triangles"][0]}_{record["triangles"][1]}'
    u=[Z]*36
    for i,v in descriptor['direction_entries']:
        u[i]=decode(v)
    h=budget(u,d)
    assert positive(h) and act(P,u)==u and act(P,w)==[Z]*36
    assert act(N,w)==w and compose(K,N)=={}
    assert {(i,j):scale(1/(b*d[j]),mul(a,conj(v))) for i,a in enumerate(w) for j,v in enumerate(w) if a!=Z and v!=Z}==N
    # Avoid new radicals by displaying the occupied-bit coordinate in a
    # non-normalized basis of squared norm h/b. This is only a frame change.
    memory_metric=list(d)+[1/h]
    tensor_metric=list(d)+[di*b/h for di in d]
    E={(i,i):ONE for i in range(36)}
    E.update({(36+i,36):v for i,v in enumerate(w) if v!=Z})
    Es=sharp(E,memory_metric,tensor_metric)
    image=compose(E,Es)
    assert compose(Es,E)==identity(37)
    assert image==plus(identity(36),block(N,36))
    row={i:scale(1/(h*d[i]),conj(v)) for i,v in enumerate(u) if v!=Z}
    U=plus(identity(37),times(-1,P),{(36,36):scale(-1,ONE)},
           {(i,36):v for i,v in enumerate(u) if v!=Z},
           {(36,i):v for i,v in row.items()})
    assert compose(U,U)==identity(37) and adjoint(U,memory_metric)==U
    V=plus(compose(compose(E,U),Es),identity(72),times(-1,image))
    assert compose(V,V)==identity(72) and adjoint(V,tensor_metric)==V
    assert compose(V,E)==compose(E,U)
    epsilon,J,kappa=F(1,4),F(1,2),F(1)
    # Existing H=K+kappa*P+epsilon*n+J*(n-(I-P))^2, g=0.
    empty=plus(K,times(kappa,P),times(J,plus(identity(36),times(-1,P))))
    occupied=plus(K,times(kappa+J,P),times(epsilon,identity(36)))
    H=plus(empty,block(occupied,36))
    n=block(identity(36),36)
    carrier_return=plus(N,block(N,36))
    assert adjoint(H,tensor_metric)==H
    assert compose(H,n)==compose(n,H)
    assert compose(H,image)==compose(image,H)
    assert compose(H,carrier_return)==plus(times(J,N),times(epsilon,block(N,36)))
    assert compose(H,V)!=compose(V,H)
    # The inherited uniform spectral rule also implements write/read V.
    Q=times(F(1,2),plus(identity(72),times(-1,V)))
    assert compose(Q,Q)==Q and adjoint(Q,tensor_metric)==Q
    # At t=4*pi the hold phases are (+1,-1). Outside the coherent sector
    # choose identity solely for this test matrix; it is not asserted to be
    # the full exp(-itH) there. On all written states it is the exact hold.
    hold=plus(identity(72),times(-2,block(N,36)))
    assert compose(hold,hold)==identity(72) and adjoint(hold,tensor_metric)==hold
    assert compose(H,hold)==compose(hold,H)
    fixtures=[]
    for alpha,beta in ((F(0),F(1)),(F(1),F(1)),(F(2),F(1))):
        source=[add(scale(alpha,a),scale(beta,v)) for a,v in zip(w,u)]+[Z]
        # rectangular multiplication uses padded output helper explicitly
        def encode(x):
            result=[Z]*72
            for (i,j),v in E.items():
                result[i]=add(result[i],mul(v,x[j]))
            return result
        before=encode(source)
        written=act(V,before)
        expected=[scale(alpha,v) for v in w]+[scale(beta,v) for v in w]
        assert written==expected and act(carrier_return,written)==written
        total=budget(before,tensor_metric)
        assert total==alpha*alpha*b+beta*beta*h and budget(written,tensor_metric)==total
        population=energy(n,written,tensor_metric)/total
        assert population==beta*beta*h/total
        held=act(hold,written)
        assert energy(n,held,tensor_metric)==energy(n,written,tensor_metric)
        assert energy(H,held,tensor_metric)==energy(H,written,tensor_metric)
        assert act(carrier_return,held)==held
        # Known hold phase compensation then inverse write recovers all data.
        assert act(V,act(hold,held))==before
        assert act(V,held)!=before  # even the pure record differs by global sign
        initial_energy=energy(H,before,tensor_metric)
        stored_energy=energy(H,written,tensor_metric)
        assert initial_energy==alpha*alpha*J*b+beta*beta*(energy(K,u,d)+kappa*h)
        assert stored_energy==alpha*alpha*J*b+beta*beta*epsilon*h
        control_work=stored_energy-initial_energy
        assert control_work==beta*beta*((epsilon-kappa)*h-energy(K,u,d))
        assert positive(-control_work)
        # Work reservoir balance is an explicit bookkeeping account, not a
        # derived microscopic battery or an autonomous switching mechanism.
        reservoir_change=-control_work
        assert stored_energy+reservoir_change==initial_energy
        read_work=initial_energy-energy(H,held,tensor_metric)
        assert read_work+control_work==0
        fixtures.append({'coherent_amplitude':str(alpha),'mismatch_amplitude':str(beta),
                         'occupied_probability':scalar(population),
                         'initial_joint_energy_form':scalar(initial_energy),
                         'written_joint_energy_form':scalar(stored_energy),
                         'normalized_written_energy':scalar(stored_energy/total),
                         'write_control_work_into_system':scalar(control_work),
                         'reservoir_energy_gain':scalar(reservoir_change),
                         'phase_corrected_read_control_work':scalar(read_work),
                         'closed_write_hold_read_net_work':'0',
                         'hold_preserves_carrier_and_occupation':True,
                         'phase_corrected_read_recovers_input':True})
    assert fixtures[0]['occupied_probability']==scalar(R(1))
    assert fixtures[0]['normalized_written_energy']==scalar(R(epsilon))
    # Extend the SAME direct-sum encoding to 21 seam memories: record j maps
    # to w tensor the one-hot bit string j. This is an isometry into a code,
    # not an identification with all 2^21 independent occupation states.
    seams=[matrix(item['entries']) for item in native['seam_projectors']]
    m=len(seams)
    assert m==21
    code_metric=list(d)
    for p in seams:
        assert compose(p,p)==p and adjoint(p,d)==p and compose(p,N)=={}
        j=min(j for i,j in p)
        direction=[p.get((i,j),Z) for i in range(36)]
        hj=budget(direction,d)
        code_metric.append(1/hj)
    onehot_masks=[1<<j for j in range(m)]
    assert len(set(onehot_masks))==m and all(mask.bit_count()==1 for mask in onehot_masks)
    fully_occupied=(1<<m)-1
    assert fully_occupied not in [0]+onehot_masks
    H_empty=plus(K,times(kappa-J,plus(*seams)),times(m*J,identity(36)))
    onehot_energy=(m-1)*J+epsilon
    H_code=plus(H_empty,{(36+j,36+j):(R(onehot_energy),R()) for j in range(m)})
    number_code={(36+j,36+j):ONE for j in range(m)}
    assert adjoint(H_code,code_metric)==H_code
    assert compose(number_code,number_code)==number_code
    assert compose(H_code,number_code)==times(onehot_energy,number_code)
    assert compose(H_empty,N)==times(m*J,N)
    full_ground=m*epsilon
    assert onehot_energy-full_ground==(m-1)*(J-epsilon)==5
    bank={'status':'one_hot_code_extension_checked_not_full_occupation',
          'seam_memories':m,'code_dimension':36+m,
          'full_carrier_register_dimension':36*(2**m),
          'encoding':'q -> q|00...0>; z_j -> z_j*w|one_hot_j>, with inherited record metrics',
          'hold_preserves_code':True,'record_number_on_code_is_a_projection':True,
          'total_occupation_expectation_bound':'0 <= <sum n_j> <= 1 for normalized code states',
          'one_hot_memory_energy':str(onehot_energy),'fully_occupied_ground_energy':str(full_ground),
          'code_memory_energy_above_full_ground':str(onehot_energy-full_ground),
          'all_filled_pattern_in_code':False,
          'lossless_memory_into_fixed_ground_obstruction':'The 21-dimensional one-hot memory sector cannot be isometrically compressed into the rank-one fixed-carrier all-filled ground without additional retained degrees of freedom.',
          'scope':'Exact code algebra using actual noncommuting projectors; no 36*2^21 matrix enumeration or local autonomous preparation claim.'}
    result={'status':'single_seam_memory_occupation_bridge_checked',
            'twenty_one_seam_extension':bank,
            'seam':record['triangles'],'memory_dimension':37,'tensor_dimension':72,
            'code_dimension':37,'record_bit_frame_squared_norm':scalar(h/b),
            'metric_isometric_encoding_and_full_unitary_write':True,
            'existing_hold_hamiltonian':'K+kappa*P+epsilon*n+J*(n-(I-P))^2; g=0',
            'parameters':{'epsilon':'1/4','J':'1/2','kappa':'1','g':'0'},
            'K_convention':'existing stored native positive matrix (4H_native/pi), with its declared model coefficient',
            'all_time_hold_on_written_states':'alpha*exp(-i*J*t)*w|0> + beta*exp(-i*epsilon*t)*w|1>, in the declared bit frame',
            'exact_sample_hold_time':'4*pi in the declared units',
            'fixtures':fixtures,
            'limitations':['Encoding uses the full coherent return vector w, not just the local seam; it is not a proved local implementation.',
                           'Coherent amplitude becomes a superposition of empty/occupied states, not a forced classical bit or occupation in every input.',
                           'Holding preserves the written coherent carrier at g=0; relative phase must be tracked for exact recovery.',
                           'Write/read do not conserve the hold Hamiltonian; the control/reservoir work is explicitly accounted, not autonomously implemented.',
                           'The checked all-seam one-hot code is not the fully occupied bond sector; nonzero-mixing extension and calibrated mass remain unconstructed.'],
            'source_snapshot_sha256':snapshot.stem,'memory_receipt_sha256':sha256(receipt_raw).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/single_seam_memory_occupation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
