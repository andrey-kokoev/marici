"""Transport the prior reversible projection-memory lift to native belt records.

One complex scalar record per rank-one rejected direction, with its inherited
metric. Norm transfer, spectral gate energy and native constraint energy are
reported separately. No occupation law or mass normalization is added.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

from check_coupled_six_piece_belt import R, Z, ONE, add, mul, conj, scale, norm, total, positive, encoded
from check_constraint_energy_accounting import identity, plus, times, compose, adjoint, trace
from check_belt_three_by_twelve import decode
from check_phase_occupation_necessity import matrix

BASE = Path(__file__).resolve().parents[1]


def dot(x,y,denominators):
    return total(scale(1/d,mul(conj(a),b)) for a,b,d in zip(x,y,denominators))


def budget(x,denominators):
    value = dot(x,x,denominators)
    assert value[1]==0
    return value[0]


def act(A,x):
    result = [Z]*len(x)
    for (i,j),v in A.items():
        result[i] = add(result[i],mul(v,x[j]))
    return result


def energy(A,x,denominators):
    value = dot(x,act(A,x),denominators)
    assert value[1]==0
    return value[0]


def scalar(x):
    return {'rational':str(x.a),'sqrt2':str(x.b)}


def main():
    necessity = json.loads((BASE/'results/phase_occupation_necessity.json').read_text())
    snapshot = BASE.parent.parent/necessity['immutable_source_snapshot']
    raw = snapshot.read_bytes()
    assert sha256(raw).hexdigest()==necessity['snapshot_sha256']==snapshot.stem
    bundle = json.loads(raw)
    native = bundle['records']['native']['carriers']['belt']
    bridge = bundle['records']['bridge']
    assert bridge['proton_and_belt']['belt']['all_native_seam_projectors_reconstructed_exactly']
    intrinsic_path = BASE/'results/belt_three_by_twelve_store.json'
    intrinsic_raw = intrinsic_path.read_bytes()
    assert bridge['sources'][str(intrinsic_path.relative_to(BASE.parent))]==sha256(intrinsic_raw).hexdigest()
    intrinsic = json.loads(intrinsic_raw)
    d = tuple(map(F,native['metric_denominators']))
    N = matrix(native['return_entries'])
    Hnative,Hfull = matrix(native['native_energy_entries']),matrix(native['entries'])
    w = [decode(c['selected_numerator']) for c in intrinsic['coordinates']]
    wnorm = budget(w,d)
    assert {(i,j):scale(1/(wnorm*d[j]),mul(a,conj(b))) for i,a in enumerate(w) for j,b in enumerate(w) if a!=Z and b!=Z}==N
    projectors = []
    for t in range(18):
        indices = (2*t,2*t+1)
        vnorm = sum((norm(w[i])/d[i] for i in indices),R())
        local_line = {(i,j):scale(1/(vnorm*d[j]),mul(w[i],conj(w[j]))) for i in indices for j in indices}
        reject = plus({(i,i):ONE for i in indices},times(-1,local_line))
        projectors.append((f'phase_triangle_{intrinsic["triangle_order"][t]}',reject))
    projectors += [(f'seam_{record["triangles"][0]}_{record["triangles"][1]}',matrix(record['entries'])) for record in native['seam_projectors']]
    count = len(projectors)
    assert count==39
    dimension = 36+count
    gates,metric,descriptors = [],list(d),[]
    for k,(name,P) in enumerate(projectors):
        assert compose(P,P)==P and adjoint(P,d)==P and trace(P,36)==1
        assert compose(P,N)=={}
        column = min(j for i,j in P)
        u = {i:v for (i,j),v in P.items() if j==column}
        h = sum((norm(v)/d[i] for i,v in u.items()),R())
        assert positive(h)
        row = {i:scale(1/(h*d[i]),conj(v)) for i,v in u.items()}
        assert {(i,j):mul(v,row[j]) for i,v in u.items() for j in u}==P
        # q'=(I-P)q+u*z; z'=u^sharp*q/h. Record metric is h.
        slot = 36+k
        gate = plus(identity(dimension),times(-1,P),{(slot,slot):scale(-1,ONE)},
                    {(i,slot):v for i,v in u.items()}, {(slot,i):v for i,v in row.items()})
        metric.append(1/h)
        gates.append((u,row,slot,gate))
        descriptors.append({'name':name,'direction_column':column,'record_metric_h':scalar(h),
                            'direction_entries':[[i,encoded(v)] for i,v in u.items()]})
    I = identity(dimension)
    Hextended = dict(Hfull)  # carrier constraint Hamiltonian, zero record block
    nonconserving_native_energy_gates = 0
    recoded_metric = list(metric[:36])+[v/4 for v in metric[36:]]
    for u,row,slot,gate in gates:
        assert compose(gate,gate)==I and adjoint(gate,metric)==gate
        # Existing uniform spectral rule H_gate=pi*Q, Q=(I-U)/2.
        Q = times(F(1,2),plus(I,times(-1,gate)))
        assert compose(Q,Q)==Q and adjoint(Q,metric)==Q and trace(Q,dimension)==1
        assert compose(Q,gate)==compose(gate,Q)
        # Reframe every direction u -> 2u and record z -> z/2. This is
        # re-encoding, not a second resource or a different energy scale.
        recoded = {(i,j):scale((F(1,2) if i>=36 else 1)*(2 if j>=36 else 1),v)
                   for (i,j),v in gate.items()}
        assert adjoint(recoded,recoded_metric)==recoded
        assert all(recoded[i,slot]==scale(2,v) for i,v in u.items())
        assert all(recoded[slot,i]==scale(F(1,2),v) for i,v in row.items())
        nonconserving_native_energy_gates += compose(Hextended,gate)!=compose(gate,Hextended)
    assert nonconserving_native_energy_gates>0

    def step(state,k):
        u,row,slot,_ = gates[k]
        a = total(mul(coefficient,state[i]) for i,coefficient in row.items())
        difference = add(state[slot],scale(-1,a))
        result = list(state)
        for i,v in u.items():
            result[i] = add(state[i],mul(v,difference))
        result[slot] = a
        return result

    def sweep(state,reverse=False):
        result = list(state)
        for k in (reversed(range(count)) if reverse else range(count)):
            result = step(result,k)
        return result

    # Exact full-space recovery, including arbitrary initially populated records.
    for j in range(dimension):
        basis = [Z]*dimension
        basis[j] = ONE
        assert sweep(sweep(basis),reverse=True)==basis
    coherent = w+[Z]*count
    assert sweep(coherent)==coherent
    fixtures = []
    for k in (0,18):  # first local phase rejection and first actual seam
        u,_,_,_ = gates[k]
        initial = list(coherent)
        for i,v in u.items():
            initial[i] = add(initial[i],v)
        state = list(initial)
        before = budget(initial,metric)
        for j in range(count):
            old = state
            state = step(old,j)
            assert budget(state,metric)==budget(old,metric)
            carrier_loss = budget(old[:36],d)-budget(state[:36],d)
            record_gain = budget(state[36:],metric[36:])-budget(old[36:],metric[36:])
            assert carrier_loss==record_gain
        assert state[:36]==w
        assert positive(budget(state[36:],metric[36:]))
        assert budget(state,metric)==before
        encoded_state = state[:36]+[scale(F(1,2),z) for z in state[36:]]
        assert budget(encoded_state,recoded_metric)==before
        assert sweep(state,reverse=True)==initial
        reused = sweep(state)
        assert reused[:36]!=w and budget(reused,metric)==before
        assert sweep(reused,reverse=True)==state
        # The same forward order is not generally the inverse of a noncommuting sweep.
        fixture = {'input':descriptors[k]['name']+' mismatch plus coherent return',
                   'carrier_returns_exactly_to_selected_vector':True,
                   'retained_record_squared_budget':scalar(budget(state[36:],metric[36:])),
                   'initial_carrier_constraint_4H_over_pi':scalar(energy(Hfull,initial[:36],d)),
                   'final_carrier_constraint_4H_over_pi':scalar(energy(Hfull,state[:36],d)),
                   'initial_native_phase_alignment_4H_over_pi':scalar(energy(Hnative,initial[:36],d)),
                   'reverse_order_recovers_input_and_empties_records':True,
                   'forward_reuse_returns_amplitude_to_carrier':True,
                   'two_forward_sweeps_equal_identity_on_this_fixture':reused==initial}
        fixtures.append(fixture)
    assert not fixtures[1]['two_forward_sweeps_equal_identity_on_this_fixture']
    report = {'status':'exact_native_phase_seam_memory_lift_verified',
              'carrier_dimension':36,'phase_memory_registers':18,'seam_memory_registers':21,
              'total_complex_dimension':dimension,'scalar_records_are_amplitudes_not_binary_occupations':True,
              'all_local_lifts_metric_unitary_involutions':True,
              'record_frame_rescaling_preserves_dynamics_and_metric_budget':True,
              'all_local_spectral_generators_checked':'H_gate=pi*(I-U_gate)/2; positive, conserved during its own gate',
              'full_space_reverse_recovery_basis_checks':dimension,
              'coherent_return_with_empty_records_fixed':True,
              'gates_not_conserving_bare_carrier_constraint_energy':nonconserving_native_energy_gates,
              'fixtures':fixtures,'record_frames':descriptors,
              'source_snapshot':necessity['immutable_source_snapshot'], 'source_snapshot_sha256':snapshot.stem,
              'intrinsic_source_sha256':sha256(intrinsic_raw).hexdigest(),
              'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope':'Existing reversible memory construction transported to actual native phase/seam rejection projectors. The conserved norm budget, per-gate spectral energy, and native carrier constraint Hamiltonian are distinct. No common autonomous storage Hamiltonian, binary bond occupation, calibrated rest mass, or electron transport is inferred.'}
    (BASE/'results/native_phase_seam_memory.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:value for key,value in report.items() if key!='record_frames'},indent=2))


if __name__=='__main__':
    main()
