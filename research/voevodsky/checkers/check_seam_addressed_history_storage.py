"""Compile filled-bond storage into addressed reversible steps; test noise.

The existing coherent carrier is preserved. Global bare-energy commutation is
not assumed for seam-conditioned gates outside that sector. Quantum history
phase errors are tested independently of occupation stability.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
from check_coupled_six_piece_belt import R, Z, ONE, add, mul, norm, positive
from check_constraint_energy_accounting import identity, plus, times, compose, adjoint
from check_phase_occupation_necessity import matrix
from check_native_phase_seam_memory import scalar

BASE=Path(__file__).resolve().parents[1]


def main():
    prior_path=BASE/'results/filled_bond_history_storage.json'
    prior_raw=prior_path.read_bytes()
    prior=json.loads(prior_raw)
    memory_raw=(BASE/'results/native_phase_seam_memory.json').read_bytes()
    memory=json.loads(memory_raw)
    assert sha256(memory_raw).hexdigest()==prior['memory_receipt_sha256']
    snapshot=BASE.parent.parent/memory['source_snapshot']
    raw=snapshot.read_bytes()
    assert sha256(raw).hexdigest()==prior['source_snapshot_sha256']
    native=json.loads(raw)['records']['native']['carriers']['belt']
    N,K=matrix(native['return_entries']),matrix(native['native_energy_entries'])
    seams=[matrix(row['entries']) for row in native['seam_projectors']]
    d=tuple(map(F,native['metric_denominators']))
    m=len(seams)
    assert m==21
    eps,J,kappa=F(1,4),F(1,2),F(1)
    gap=J-eps
    full=(1<<m)-1
    I=identity(36)
    for P in seams:
        assert adjoint(P,d)==P and compose(P,P)==P and compose(P,N)=={}
        S=plus(I,times(-1,P))
        assert compose(S,N)==N
    # Pointer labels are PHYSICALLY ORTHONORMAL here. Prior nonnormalized
    # record amplitudes are re-expressed through inherited weights below.
    # copy_index is a controlled modular addition, not quantum cloning.
    def copy_index(label,inverse=False):
        mask,h,b=label
        if mask>0 and mask&(mask-1)==0:
            j=mask.bit_length()
            h=(h+(-j if inverse else j))%(m+1)
        return mask,h,b
    def fill(label,e):
        mask,h,b=label
        if h==0 or h==e+1:
            return label
        if not mask&(1<<e) and b<m-1:
            return mask|(1<<e),h,b+1
        if mask&(1<<e) and b>0:
            return mask^(1<<e),h,b-1
        return label
    def energy_label(label):
        mask,_,b=label
        number=mask.bit_count()
        return eps*number+J*(m-number)+gap*b
    def forward(label):
        label=copy_index(label)
        for e in range(m):
            label=fill(label,e)
        return label
    def backward(label):
        for e in reversed(range(m)):
            label=fill(label,e)
        return copy_index(label,inverse=True)
    label_checks=0
    for e in range(m):
        for mask in (0,1<<e,full^(1<<e),full):
            for history in range(m+1):
                for battery in range(m):
                    label=(mask,history,battery)
                    out=fill(label,e)
                    assert fill(out,e)==label
                    assert energy_label(out)==energy_label(label)
                    label_checks+=1
    for j in range(m):
        for history in range(m+1):
            x=(1<<j,history,0)
            assert copy_index(copy_index(x),inverse=True)==x
    # All 21 branches, every stage: total bare energy is constant on N.
    source=[(1<<j,0,0) for j in range(m)]
    target=[(full,j+1,m-1) for j in range(m)]
    stage_counts=[]
    for j,x in enumerate(source):
        current=copy_index(x)
        baseline=energy_label(x)
        for e in range(m):
            current=fill(current,e)
            assert energy_label(current)==baseline==F(41,4)
            assert current[2]==e+1-(j<=e)
        assert current==target[j] and forward(x)==target[j]
        assert backward(current)==x
        stage_counts.append(current[2])
    assert stage_counts==[20]*21
    assert forward((0,0,0))==(0,0,0)
    # Spectral half-swap certificate for each enabled bit/battery pair.
    X={(0,1):ONE,(1,0):ONE}
    Q=times(F(1,2),plus(identity(2),times(-1,X)))
    assert compose(Q,Q)==Q and adjoint(Q,(F(1),F(1)))==Q
    # S_e-controlled swap plus P_e identity is an involution, but need not
    # commute with the OTHER source energies outside N. Certify actual
    # off-diagonal H_before*S-S*H_after residuals on a reachable branch.
    sumP=plus(*seams)
    def carrier_block(mask,battery):
        number=mask.bit_count()
        return plus(K,times(kappa-J,sumP),
                    *(times(2*J,P) for e,P in enumerate(seams) if mask&(1<<e)),
                    times(eps*number+J*(m-number)+gap*battery,I))
    current=copy_index(source[0])
    nonzero=[]
    for e,P in enumerate(seams):
        out=fill(current,e)
        if out!=current:
            S=plus(I,times(-1,P))
            Hbefore,Hafter=carrier_block(current[0],current[2]),carrier_block(out[0],out[2])
            residual=plus(compose(Hafter,S),times(-1,compose(S,Hbefore)))
            assert compose(residual,N)=={} and compose(N,residual)=={}
            if residual:
                nonzero.append(e)
        current=out
    assert nonzero
    # Exact logical-phase error: all filled occupations and their energy
    # remain unchanged, while one retained amplitude changes sign.
    weights=[]
    for item in memory['record_frames'][18:]:
        h=item['record_metric_h']
        weights.append(R(F(h['rational']),F(h['sqrt2'])))
    amplitudes=[(R(j+1),R((-1)**j)) for j in range(m)]
    norms=[h*norm(a) for h,a in zip(weights,amplitudes)]
    total=sum(norms,R())
    overlap=total-2*norms[0]
    fidelity=overlap*overlap/(total*total)
    assert positive(R(1)-fidelity)
    # In orthonormal frames this is simply a diagonal -1 on history label 1.
    corrupted=[(-a[0],-a[1]) if j==0 else a for j,a in enumerate(amplitudes)]
    assert corrupted!=amplitudes
    assert sum((h*norm(a) for h,a in zip(weights,corrupted)),R())==total
    assert [(-a[0],-a[1]) if j==0 else a for j,a in enumerate(corrupted)]==amplitudes
    report={'status':'addressed_storage_and_history_noise_audit_checked',
            'source_seams':m,'history_dimension':m+1,
            'battery_level_count':m,'battery_spacing':str(gap),'final_battery_energy':str((m-1)*gap),
            'write_sequence':'coherently copy one-hot index into ready history; execute 21 history-controlled seam steps, skipping the initially occupied seam',
            'read_sequence':'reverse seam order, then inverse controlled index addition',
            'addressed_gate_label_cases':label_checks,'all_source_branches_checked':m,
            'every_reachable_stage_energy':'41/4 including finite battery',
            'all_steps_preserve_coherent_carrier':True,
            'finite_no_overflow_battery':True,'empty_ready_state_fixed':True,
            'gate_generator':'pi*(I-G_e)/2 for the metric-unitary seam-controlled involution; actual timing remains supplied',
            'global_energy_conservation_off_coherent_sector':False,
            'nonzero_off_sector_energy_residual_seams_on_branch_zero':nonzero,
            'history_phase_error':{'filled_occupations':21,'register_energy_unchanged':'21/4',
                 'battery_energy_unchanged':'5','recovered_state_fidelity':scalar(fidelity),
                 'fidelity_strictly_below_one':True,'known_phase_error_reversible':True,
                 'automatic_error_correction':False},
            'occupation_flip_energy_cost_on_coherent_carrier':'J-epsilon=1/4 for a single filled bit emptied, without battery compensation',
            'conclusion':'Seam-addressed controlled preparation is exact on the prepared coherent sector. Occupation energy does not protect degenerate quantum history, and off-sector noise invalidates the simple energy-matched gate guarantee.',
            'limitations':['Seam-addressed is not proved spatial or microscopic tensor-factor locality: the native carrier is a 36-coordinate direct-sum field.',
                           'History, battery, coherent-sector preparation and gate timing remain declared resources.',
                           'The modular history operation uses coherent controls and is not a measurement or cloning of arbitrary input states.',
                           'No autonomous latch, noise threshold, physical memory lifetime, mass or isotope binding prediction is claimed.'],
            'source_snapshot_sha256':snapshot.stem,'previous_storage_receipt_sha256':sha256(prior_raw).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/seam_addressed_history_storage.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
