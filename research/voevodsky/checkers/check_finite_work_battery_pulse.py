"""Old hold law plus a finite coherent work battery.

Exact error-sector pairings conserve the unchanged bare hold plus work energy.
Finite shifted work states need not coincide, so logical coherence after
tracing the battery is tested rather than assumed. No noise-bath or recovery
work implementation is inferred from a conserved pulse.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import importlib.util
import json
from check_encoded_history_memory import ZERO,ONE,add,mul,conj,scale,inner

BASE=Path(__file__).resolve().parents[1]


def main():
    previous_path=BASE/'results/error_transparent_bond_pulse.json'
    previous_raw=previous_path.read_bytes();previous=json.loads(previous_raw)
    circuit_raw=(BASE/'results/history_code_circuit.json').read_bytes()
    assert sha256(circuit_raw).hexdigest()==previous['recovery_circuit_receipt_sha256']
    circuit=json.loads(circuit_raw)
    source=BASE.parent/'kitaev/checkers/check_s3_five_rail_code_freeze.py'
    assert sha256(source.read_bytes()).hexdigest()==circuit['source_code_sha256']
    spec=importlib.util.spec_from_file_location('prior_code',source)
    owner=importlib.util.module_from_spec(spec);spec.loader.exec_module(owner)
    cert=owner.certify('five_qubit_perfect_code',2,owner.QUBIT)
    errors=[(0,)*10]+owner.single_rail_errors(2)
    signs=[(-1)**owner.symplectic(e,cert['logical_z'],2) for e in errors]
    J,delta,gap=F(1,2),F(1,4),F(1,2)
    assert gap==2*delta
    outputs=[]
    for M in (1,2,4,8,16):
        # Ready wavefunction has equal amplitudes on k=1,...,M. The two
        # extra boundary levels permit a single upward or downward shift.
        levels=M+2
        dim=4*levels
        def index(logical,k): return logical*levels+k
        def e_hold(logical,sa,sb):
            return J+delta*F(sa*(1-2*(logical&1))-sb*(1-2*((logical>>1)&1)),2)
        def permutation(sa,sb):
            t=int((e_hold(3,sa,sb)-e_hold(0,sa,sb))/gap)
            assert t in (-1,0,1)
            mapping=list(range(dim))
            for k in range(levels):
                target=k-t
                if 0<=target<levels:
                    a,b=index(0,k),index(3,target)
                    mapping[a],mapping[b]=b,a
            assert sorted(mapping)==list(range(dim))
            assert all(mapping[mapping[i]]==i for i in range(dim))
            for i,j in enumerate(mapping):
                li,ki=divmod(i,levels);lj,kj=divmod(j,levels)
                assert e_hold(li,sa,sb)+gap*ki==e_hold(lj,sa,sb)+gap*kj
            return mapping
        pairings={}
        for sa in signs:
            for sb in signs:
                pairings[sa,sb]=permutation(sa,sb)
        def permute(v,p):
            out=[ZERO]*dim
            for i,a in enumerate(v): out[p[i]]=a
            return out
        def half(v,p,inverse=False):
            # exp(-i*pi*(I-F)/4), or its inverse.
            a=(F(1,2),F(1,2) if inverse else F(-1,2))
            b=(F(1,2),F(-1,2) if inverse else F(1,2))
            return [add(mul(a,x),mul(b,y)) for x,y in zip(v,permute(v,p))]
        def total_energy(v,sa,sb):
            n=inner(v,v)[0]
            assert inner(v,v)[1]==0
            return sum((mul(conj(a),a)[0]*(e_hold(i//levels,sa,sb)+gap*(i%levels)) for i,a in enumerate(v)),F(0))/n
        def target_fidelity(v,logical):
            return sum((mul(conj(v[index(logical,k)]),v[index(logical,k)])[0] for k in range(levels)),F(0))/inner(v,v)[0]
        clean=pairings[1,1];faulty=pairings[-1,1]
        # One physical Z fault halfway through: in the actual recovery frame
        # it changes syndrome, not logical amplitudes (up to a common phase).
        initial=[ZERO]*dim
        for k in range(1,M+1): initial[index(0,k)]=ONE
        mid=half(initial,clean)
        final=half(mid,faulty)
        assert inner(final,final)==inner(initial,initial)
        assert total_energy(final,-1,1)==total_energy(mid,-1,1)
        fidelity=target_fidelity(final,3)
        assert fidelity==1-F(1,2*M)
        assert half(half(final,faulty,inverse=True),clean,inverse=True)==initial
        # Fault before pulse, superposition of even logical states. The
        # conditional work shifts differ by TWO ladder spacings.
        superposed=[ZERO]*dim
        for k in range(1,M+1):
            superposed[index(0,k)]=ONE;superposed[index(3,k)]=ONE
        written=permute(superposed,faulty)
        assert permute(written,faulty)==superposed
        overlap=sum((mul(conj(written[index(0,k)]),written[index(3,k)])[0] for k in range(levels)),F(0))
        logical_fidelity=F(1,2)+overlap/inner(written,written)[0]
        assert logical_fidelity==F(1,2)*(1+F(max(M-2,0),M))
        assert total_energy(written,-1,1)==total_energy(superposed,-1,1)
        # Boundary hostile: the lower end cannot supply an upward system
        # energy step. The complete unitary remains valid by fixing it.
        assert faulty[index(0,0)]==index(0,0)
        outputs.append({'ready_support_levels':M,'physical_work_levels':levels,
            'mean_ready_work_energy':str(gap*F(M+1,2)),
            'maximum_ready_work_energy':str(gap*M),
            'midpulse_fault_target_fidelity':str(fidelity),
            'preexisting_fault_even_superposition_fidelity':str(logical_fidelity),
            'pulse_conserves_old_hold_plus_work_energy':True,
            'full_joint_inverse_recovers_all_amplitudes':True,
            'bottom_boundary_cannot_supply_energy':True})
    report={'status':'finite_work_battery_energy_and_coherence_tradeoff_checked',
            'old_error_sector_hold_unchanged':True,
            'work_level_spacing':str(gap),
            'source_error_sector_pairs_checked_per_battery':len(signs)**2,
            'pulse':'Energy-matched involutive pairings; Q_work=(I-F_work)/2 commutes with unchanged hold plus work Hamiltonian, so its spectral pulse conserves that energy for every angle.',
            'trials':outputs,
            'uniform_packet_midpulse_fidelity':'1-1/(2*M)',
            'exact_finite_battery_limit':'For unknown even logical superpositions, exact pure logical transfer requires the two oppositely shifted battery states to coincide up to phase. No nonzero finite-support ladder state is invariant under a nonzero translation; boundaries or residual correlations remain.',
            'not_erased':'Information lost from the reduced logical state remains in correlations with the work battery. The full joint inverse recovers it exactly.',
            'scope':['The pulse conserves the old hold plus work energy. The injected fault and physical syndrome correction are separate interactions whose work/bath accounting is not supplied.',
                'The work battery is an additional resource, distinct from the 21 battery bits already storing bond history.',
                'Finite coherent packets and syndrome-dependent many-body pulse couplings are declared inputs, not source-selected local hardware.',
                'These uniform-packet fidelities are exact examples, not an optimal capacity bound or a universal fault threshold.',
                'No autonomous latch, mass, isotope binding or physical memory lifetime follows.'],
            'previous_transparency_receipt_sha256':sha256(previous_raw).hexdigest(),
            'recovery_circuit_receipt_sha256':sha256(circuit_raw).hexdigest(),
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/finite_work_battery_pulse.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
