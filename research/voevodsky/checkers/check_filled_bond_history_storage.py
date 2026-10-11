"""Retain seam amplitudes while filling bonds, with a finite energy account.

Constructive extension: a ready plus 21-label degenerate quantum history space,
and a two-level battery. On the coherent carrier a permutation swaps one-hot
records into all-filled records with the index retained in history. A control
on N extends the energy-conserving operation to the full carrier. No locality,
autonomous latch, source uniqueness or mass prediction is asserted.
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
    memory_path=BASE/'results/native_phase_seam_memory.json'
    previous_path=BASE/'results/single_seam_memory_occupation.json'
    memory_raw,previous_raw=memory_path.read_bytes(),previous_path.read_bytes()
    memory,previous=json.loads(memory_raw),json.loads(previous_raw)
    assert previous['memory_receipt_sha256']==sha256(memory_raw).hexdigest()
    path=BASE.parent.parent/memory['source_snapshot']
    raw=path.read_bytes()
    assert sha256(raw).hexdigest()==memory['source_snapshot_sha256']
    native=json.loads(raw)['records']['native']['carriers']['belt']
    metric=tuple(map(F,native['metric_denominators']))
    N,K=matrix(native['return_entries']),matrix(native['native_energy_entries'])
    seams=[matrix(record['entries']) for record in native['seam_projectors']]
    m=len(seams)
    assert m==21
    assert adjoint(N,metric)==N and compose(N,N)==N
    assert adjoint(K,metric)==K and compose(K,N)=={}
    for P in seams:
        assert adjoint(P,metric)==P and compose(P,N)=={}
    epsilon,J,kappa=F(1,4),F(1,2),F(1)
    delta=(m-1)*(J-epsilon)
    assert delta==5
    I=identity(36)
    sumP=plus(*seams)
    Hfull=plus(K,times(kappa+J,sumP),times(m*epsilon,I))
    Hfull_battery=plus(Hfull,times(delta,I))
    onehot_energy=(m-1)*J+epsilon
    # C=N tensor W +(I-N) tensor I. These block identities imply
    # [C,H_bare]=0 globally, although W alone would fail off the coherent line.
    for j,P in enumerate(seams):
        Hj=plus(K,times(kappa-J,sumP),times(2*J,P),times(onehot_energy,I))
        assert compose(Hj,N)==compose(N,Hj)==times(onehot_energy,N)
        assert compose(Hfull_battery,N)==compose(N,Hfull_battery)==times(onehot_energy,N)
        residual=plus(Hfull_battery,times(-1,Hj))
        assert residual==times(2*J,plus(*(p for k,p in enumerate(seams) if k!=j)))
        assert residual and compose(residual,N)=={}
    full=(1<<m)-1
    # Work in inherited orthogonal pointer frames. Memory directions have
    # squared norms h_j. Each paired history target receives exactly that
    # weight; this is re-encoding, not changing any physical energy gap.
    weights=[]
    for j,record in enumerate(memory['record_frames'][18:]):
        h=record['record_metric_h']
        weights.append(R(F(h['rational']),F(h['sqrt2'])))
        assert positive(weights[-1])
    assert len(weights)==m
    r0=previous['record_bit_frame_squared_norm']
    carrier_norm=weights[0]/R(F(r0['rational']),F(r0['sqrt2']))
    assert positive(carrier_norm)
    bit_weights=[h/carrier_norm for h in weights]
    full_bit_weight=R(1)
    for value in bit_weights:
        full_bit_weight=full_bit_weight*value
    history_weights=[R(1)]+[value/full_bit_weight for value in bit_weights]
    def tensor_weight(label):
        mask,history,_=label
        value=carrier_norm*history_weights[history]
        for j,r in enumerate(bit_weights):
            if mask & (1<<j):
                value=value*r
        return value
    sources=[(1<<j,0,0) for j in range(m)]
    targets=[(full,j+1,1) for j in range(m)]
    assert len(set(sources+targets))==2*m
    def swap(label):
        mask,history,battery=label
        if history==0 and battery==0 and mask>0 and mask&(mask-1)==0:
            assert mask<1<<m
            return (full,mask.bit_length(),1)
        if mask==full and 1<=history<=m and battery==1:
            return (1<<(history-1),0,0)
        return label
    def transport(state):
        result={}
        for label,amplitude in state.items():
            new=swap(label)
            result[new]=add(result.get(new,Z),amplitude)
        return {key:value for key,value in result.items() if value!=Z}
    def weight(label):
        if label in sources:
            return weights[sources.index(label)]
        if label in targets:
            return weights[targets.index(label)]
        raise AssertionError('Fixture outside retained memory sector')
    def norm_squared(state):
        return sum((weight(label)*norm(a) for label,a in state.items()),R())
    def expectation(state,observable):
        return sum((observable(label)*weight(label)*norm(a) for label,a in state.items()),R())/norm_squared(state)
    def carrier_register_energy(label):
        number=label[0].bit_count()
        return number*epsilon+(m-number)*J
    def battery_energy(label):
        return delta*label[2]
    # Exhaust the active label families with all history and battery values;
    # every other mask is fixed by the explicit definition above.
    checked=0
    for mask in [0]+[1<<j for j in range(m)]+[full]:
        for history in range(m+1):
            for battery in (0,1):
                label=(mask,history,battery)
                assert swap(swap(label))==label
                checked+=1
    for s,t,h in zip(sources,targets,weights):
        assert swap(s)==t and swap(t)==s and weight(s)==weight(t)==h
        assert tensor_weight(s)==tensor_weight(t)==h
        assert carrier_register_energy(s)+battery_energy(s)==carrier_register_energy(t)+battery_energy(t)
    # Exact coefficient-space permutation has a positive spectral generator.
    W={(j+m,j):ONE for j in range(m)}|{(j,j+m):ONE for j in range(m)}
    pointer_metric=[1/h for h in weights]*2
    assert compose(W,W)==identity(2*m) and adjoint(W,pointer_metric)==W
    Q=times(F(1,2),plus(identity(2*m),times(-1,W)))
    assert compose(Q,Q)==Q and adjoint(Q,pointer_metric)==Q
    # Arbitrary coherent superposition: every memory channel is nonzero.
    initial={s:(R(j+1),R((-1)**j)) for j,s in enumerate(sources)}
    filled=transport(initial)
    assert len(filled)==m and all(label[0]==full for label in filled)
    assert norm_squared(initial)==norm_squared(filled)
    assert transport(filled)==initial
    assert expectation(initial,lambda label:label[0].bit_count())==1
    assert expectation(filled,lambda label:label[0].bit_count())==m
    assert expectation(initial,carrier_register_energy)==onehot_energy
    assert expectation(filled,carrier_register_energy)==m*epsilon
    assert expectation(filled,battery_energy)==delta
    assert expectation(initial,lambda label:carrier_register_energy(label)+battery_energy(label))==expectation(filled,lambda label:carrier_register_energy(label)+battery_energy(label))
    # Relative amplitudes reside in orthogonal history labels, never discarded.
    for j in range(m):
        assert filled[targets[j]]==initial[sources[j]]
    assert len({(label[0],label[2]) for label in filled})==1
    # The ready empty pattern is not charged from nothing.
    assert swap((0,0,0))==(0,0,0)
    report={'status':'filled_bond_history_storage_checked',
            'source_seams':m,'added_history_dimension':m+1,'memory_history_subspace_dimension':m,
            'history_energy':'declared degenerate zero Hamiltonian; readiness and physical implementation are resources, not derived to be free',
            'battery_levels':['0',str(delta)],'battery_gap_origin':'(m-1)*(J-epsilon), inherited from the existing occupation fixture',
            'full_carrier_control':'C=N tensor W +(I-N) tensor I; global coherent-return control, not a local implementation',
            'metric_unitary_involution':True,
            'tensor_frame_check':'Inherited bit norms r_j=h_j/||w||^2; history label j has norm r_j/product(r), so paired tensor norms match exactly.','commutes_with_bare_carrier_register_battery_H':True,
            'source_operator_energy_blocks_checked':m,'pointer_label_cases_checked':checked,
            'all_nonzero_complex_amplitudes_recovered':True,
            'filled_register_occupation':m,'input_register_occupation':1,
            'initial_register_energy':str(onehot_energy),'filled_register_energy':str(m*epsilon),
            'released_energy_stored_in_finite_battery':str(delta),'total_energy':str(onehot_energy),
            'hold':'At g=0 the coherent carrier, all-filled bits and charged battery are stationary; degenerate history amplitudes acquire only a common phase.',
            'read':'Inverse swap restores all one-hot amplitudes and discharges the battery; no history erasure.',
            'pulse':'Existing uniform generator pi*(I-C)/2 commutes with bare H and implements C in unit pulse time, up to the common bare-H phase on this sector.',
            'autonomous_latch':False,
            'limitations':['A ready quantum history register and finite battery are explicit additional resources.',
                           'All-filled occupation does not encode which amplitude: the retained quantum history does. Erasing it collapses 21 distinguishable directions to one.',
                           'The pulse must be stopped for holding; leaving the exchange generator on returns amplitude. Control timing and an autonomous latch are not derived.',
                           'The occupied-memory sector is assumed prepared. An empty ready record remains empty; this does not derive spontaneous charging.',
                           'No microscopic locality, nonzero-mixing robustness, mass calibration, isotope binding or electron transport is claimed.'],
            'source_snapshot_sha256':path.stem,'memory_receipt_sha256':sha256(memory_raw).hexdigest(),
            'previous_bridge_sha256':sha256(previous_raw).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/filled_bond_history_storage.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
