"""Two source-bound storage branches: interaction complexity and battery shape.

A: exact recovery-frame Pauli expansion and a truncation hostile.
B: sine-shaped finite work packets, with exact cyclotomic pulse checks and
fixed-support optimality for the specified midpoint-input fidelity only.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from collections import Counter
import importlib.util
import json
import cmath
import math
from check_history_code_circuit import raw
from evolve_relative_geometry_modes import Cyclotomic

BASE=Path(__file__).resolve().parents[1]


def multiply(a,b):
    x,z,p=a;u,v,q=b
    return [x^u,z^v,(p+q+2*(z&u).bit_count())%4]


def character(e,p): return (-1)**(((e[0]&p[1]).bit_count()+(e[1]&p[0]).bit_count())%2)


def expansion_audit(owner,cert):
    stabilizers=[raw(s) for s in owner.QUBIT]
    group=[]
    for mask in range(16):
        p=[0,0,0]
        for i,s in enumerate(stabilizers):
            if mask&(1<<i): p=multiply(p,s)
        group.append(p)
    errors=[[0,0,0]]+[raw(e) for e in owner.single_rail_errors(2)]
    logicals={'X':raw(cert['logical_x']),'Z':raw(cert['logical_z'])}
    y=multiply(logicals['X'],logicals['Z']);y[2]=(y[2]+1)%4
    logicals['Y']=y
    result={}
    for name,L in logicals.items():
        coset=[multiply(L,s) for s in group]
        weights=[(p[0]|p[1]).bit_count() for p in coset]
        coefficients=[sum(character(e,p) for e in errors)/F(16) for p in coset]
        assert coefficients==[1-F(w,4) for w in weights]
        assert Counter(weights)==Counter({3:10,5:6})
        assert sum(coefficients)==1
        responses=[sum(c*character(e,p) for c,p in zip(coefficients,coset)) for e in errors]
        assert responses==[F(1)]*16
        # Keep only weight-three terms and renormalize to act correctly on
        # the code. Even this favorable truncation must be checked on errors.
        truncated=[F(1,10) if w==3 else F(0) for w in weights]
        bad=[{'error_x_mask':e[0],'error_z_mask':e[1],
              'response':str(sum(c*character(e,p) for c,p in zip(truncated,coset)))}
             for e in errors if sum(c*character(e,p) for c,p in zip(truncated,coset))!=1]
        assert bad
        result[name]={'term_count':16,'body_weights':{'3':10,'5':6},
                      'coefficients_relative_to_signed_logical_stabilizer_coset':{'3':'1/4','5':'-1/4'},
                      'all_sixteen_error_sector_responses':'1',
                      'normalized_weight_three_truncation_failing_sectors':len(bad),
                      'first_truncation_counterexample':bad[0]}
    pair_weights=Counter()
    for _ in logicals:
        for a in [3]*10+[5]*6:
            for b in [3]*10+[5]*6: pair_weights[a+b]+=1
    assert pair_weights==Counter({6:300,8:360,10:108})
    return {'status':'exact_pauli_complexity_and_truncation_checked',
            'component_operators':result,
            'pair_pulse_projector_terms':769,
            'pair_terms_by_body_weight':{'0':1,**{str(k):v for k,v in sorted(pair_weights.items())}},
            'pair_identity_coefficient':'1/4','other_pair_coefficient_magnitude':'1/64',
            'hold_terms_by_body_weight':{'0':1,'3':20,'5':12},
            'conclusion':'No direct one- or two-body Hamiltonian on these same physical qubits equals this full error-transparent operator. Removing high-weight terms, even after fixing the on-code action, loses error transparency.',
            'scope':'Pauli-basis uniqueness for the declared operator, not a no-go for ancillary mediators, approximate gadgets or other codes.'}


def battery_audit():
    results=[]
    for M in (1,2,4,8,16):
        ring=Cyclotomic(4*(M+1))
        z=lambda k:ring.root(2*k)
        i=ring.root(M+1)
        theta_cos=ring.scale(F(1,2),ring.add(z(1),z(-1)))
        def total(vs):
            value=ring.zero
            for v in vs: value=ring.add(value,v)
            return value
        def norm(v): return ring.multiply(ring.conjugate(v),v)
        amplitudes=[ring.add(z(k),ring.scale(-1,z(-k))) for k in range(1,M+1)]
        length=total(norm(a) for a in amplitudes)
        assert length==ring.scalar(2*(M+1))
        # The real path adjacency / 2 has these M sine eigenvectors.
        eigenvalues=[]
        for mode in range(1,M+1):
            a=[ring.add(z(mode*k),ring.scale(-1,z(-mode*k))) for k in range(1,M+1)]
            lam=ring.scale(F(1,2),ring.add(z(mode),z(-mode)))
            eigenvalues.append(lam)
            for k in range(M):
                left=a[k-1] if k else ring.zero
                right=a[k+1] if k+1<M else ring.zero
                assert ring.scale(F(1,2),ring.add(left,right))==ring.multiply(lam,a[k])
        assert len(set(eigenvalues))==M
        levels=M+2;dim=4*levels
        def index(q,k):return q*levels+k
        def permutation(shift):
            p=list(range(dim))
            for k in range(levels):
                target=k-shift
                if 0<=target<levels:
                    a,b=index(0,k),index(3,target)
                    p[a],p[b]=b,a
            return p
        clean,faulty=permutation(0),permutation(1)
        # Same old hold (-,+) and half-unit work ladder as the prior branch.
        for a,b in enumerate(faulty):
            la,ka=divmod(a,levels);lb,kb=divmod(b,levels)
            hold=lambda l:F(1,2)+F(1,8)*(-(1-2*(l&1))-(1-2*((l>>1)&1)))
            assert hold(la)+F(ka,2)==hold(lb)+F(kb,2)
        def permute(v,p):
            out=[ring.zero]*dim
            for k,a in enumerate(v):out[p[k]]=a
            return out
        ca=ring.scale(F(1,2),ring.add(ring.one,ring.scale(-1,i)))
        cb=ring.scale(F(1,2),ring.add(ring.one,i))
        def half(v,p):return [ring.add(ring.multiply(ca,a),ring.multiply(cb,b)) for a,b in zip(v,permute(v,p))]
        packet_results=[]
        for name,packet,N in (('uniform',[ring.one]*M,F(M)),('sine',amplitudes,F(2*(M+1)))):
            ready=[ring.zero]*dim
            for k,a in enumerate(packet,1):ready[index(0,k)]=a
            final=half(half(ready,clean),faulty)
            # Include the actual free hold/work phases as well, at declared
            # total time T=8*pi with pulse strength 1/8. Each half lasts 4*pi.
            # All energies are quarter-integers, so these phases are exact signs.
            def free_half(v,sa,sb):
                out=[]
                for j,a in enumerate(v):
                    logical,k=divmod(j,levels)
                    energy=F(1,2)+F(1,8)*(sa*(1-2*(logical&1))-sb*(1-2*((logical>>1)&1)))+F(k,2)
                    exponent=4*energy
                    assert exponent.denominator==1
                    out.append(ring.scale((-1)**int(exponent),a))
                return out
            actual_mid=free_half(half(ready,clean),1,1)
            actual_final=free_half(half(actual_mid,faulty),-1,1)
            assert actual_final==[ring.scale(-1,a) for a in final]
            assert total(norm(a) for a in final)==ring.scalar(N)
            fidelity=ring.scale(1/N,total(norm(final[index(3,k)]) for k in range(levels)))
            expected=ring.scalar(1-F(1,2*M)) if name=='uniform' else ring.scale(F(1,2),ring.add(ring.one,theta_cos))
            assert fidelity==expected
            # Track the other objective as a control, not as optimized too.
            pre=[ring.zero]*dim
            for k,a in enumerate(packet,1):pre[index(0,k)]=pre[index(3,k)]=a
            out=permute(pre,faulty)
            pre_fidelity=ring.scale(1/(4*N),total(norm(ring.add(out[index(0,k)],out[index(3,k)])) for k in range(levels)))
            assert permute(out,faulty)==pre
            mean=ring.scale(1/N,total(ring.scale(F(k,2),norm(a)) for k,a in enumerate(packet,1)))
            assert mean==ring.scalar(F(M+1,4))
            def approximate(a):
                value=sum(float(c)*cmath.exp(2j*math.pi*k/ring.order) for k,c in enumerate(a))
                assert abs(value.imag)<1e-9
                return value.real
            packet_results.append({'packet':name,
                'midpulse_fidelity_exact_coefficients':[str(c) for c in fidelity],
                'midpulse_fidelity_approx':approximate(fidelity),
                'preexisting_fault_superposition_fidelity_approx':approximate(pre_fidelity)})
        if M==4:
            assert packet_results[1]['preexisting_fault_superposition_fidelity_approx']<packet_results[0]['preexisting_fault_superposition_fidelity_approx']
        results.append({'ready_support_levels':M,'physical_work_levels':levels,
                        'shared_mean_ready_work_energy':str(F(M+1,4)),
                        'cyclotomic_order':ring.order,'profiles':packet_results})
    return {'status':'fixed_support_midpulse_optimum_and_second_objective_checked',
            'midpulse_optimum':'(1+cos(pi/(M+1)))/2',
            'optimizer':'a_k proportional to sin(k*pi/(M+1)), k=1,...,M',
            'proof':'Midpoint target fidelity is (1+Re sum conjugate(a_k)*a_(k+1)/sum |a_k|^2)/2. The real path matrix has eigenvalues cos(j*pi/(M+1)); the first is largest. All sine recurrences and distinct eigenvalues are checked exactly.',
            'same_capacity_and_mean_energy_as_uniform':True,
            'free_hold_phase_control':'The complete half-step exp(-i*4*pi*H_hold+work) exp(-i*pi*Q/2) gives the same midpoint fidelity at total duration 8*pi and pulse strength 1/8. This declared commensurate schedule is not a physical clock calibration.',
            'trials':results,
            'controls':['This optimizes the prior midpoint-fault |00> target fidelity, not arbitrary logical inputs or all fault times.',
                        'At M=4 the sine packet improves that target but worsens the preexisting-fault even-superposition fidelity.',
                        'Preparing the coherent sine profile is a supplied resource; these are not particle-mass fits or a physical noise threshold.',
                        'The midpoint pulse benchmark is additionally checked with free hold/work phases at the declared commensurate duration 8*pi; arbitrary schedules and the injected fault/recovery bath are not thereby certified.']}


def main():
    paths=[BASE/'results/error_transparent_bond_pulse.json',BASE/'results/finite_work_battery_pulse.json']
    previous=[json.loads(p.read_bytes()) for p in paths]
    assert previous[1]['previous_transparency_receipt_sha256']==sha256(paths[0].read_bytes()).hexdigest()
    circuit=json.loads((BASE/'results/history_code_circuit.json').read_bytes())
    source=BASE.parent/'kitaev/checkers/check_s3_five_rail_code_freeze.py'
    assert sha256(source.read_bytes()).hexdigest()==circuit['source_code_sha256']
    spec=importlib.util.spec_from_file_location('prior_code',source)
    owner=importlib.util.module_from_spec(spec);spec.loader.exec_module(owner)
    cert=owner.certify('five_qubit_perfect_code',2,owner.QUBIT)
    report={'status':'both_storage_branches_advanced',
            'changed_hold_branch':expansion_audit(owner,cert),
            'finite_work_branch':battery_audit(),
            'source_hashes':{p.name:sha256(p.read_bytes()).hexdigest() for p in paths+[source]},
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Exact gate-model comparisons, not admitted microscopic couplings, physical lifetimes or isotope predictions.'}
    (BASE/'results/storage_branch_comparison.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
