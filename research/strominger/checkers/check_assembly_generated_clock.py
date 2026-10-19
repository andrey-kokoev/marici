"""Does existing contact assembly generate a local clock from the actual input?

Existing frozen-contact operator, not a new discrete two-cycle update. Dummy
orbit coordinates are eliminated in favor of a state-read phase quadrature.
All matrices are finite numerical realizations; no supplier is executed.
"""
from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
import cmath,json
from check_native_relational_clock import scalar,eye,adj,add,scale,diff,mm,trace,norm,projector,encoded

ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/'research/scattering/high-energy/pentachoron_connected_phase_energy_bundle.zip'
FREEZE=ROOT/'research/strominger/inputs/assembly-generated-clock-freeze.json'
CONTEXT=ROOT/'research/scattering/high-energy/matched_spatial_note.md'


def block(a,b,c,d):return [r+s for r,s in zip(a,b)]+[r+s for r,s in zip(c,d)]
def zero(n):return [[0j]*n for _ in range(n)]
def generator(H,rho):return scale(-1j,diff(mm(H,rho),mm(rho,H)))
def reading(rho,Q):return trace(mm(rho,Q)).real

def coefficients(H,rho,order=20):
    out=[rho]
    for k in range(1,order+1):out.append(scale(1/k,generator(H,out[-1])))
    return out


def orbit(coeff,alpha):
    # alpha is only an auxiliary coordinate for solving the native orbit.
    out=coeff[-1]
    for term in reversed(coeff[:-1]):out=add(term,scale(alpha,out))
    return out


def clock_state(coeff,Q,target):
    lo,hi=0.0,0.016
    assert reading(orbit(coeff,lo),Q)<=target<=reading(orbit(coeff,hi),Q)
    for _ in range(48):
        middle=(lo+hi)/2
        if reading(orbit(coeff,middle),Q)<target:lo=middle
        else:hi=middle
    return orbit(coeff,(lo+hi)/2)


def clock_direction(H,rho,Q):
    direction=generator(H,rho);speed=reading(direction,Q)
    if abs(speed)<1e-10:raise ValueError('No local clock chart: zero phase derivative')
    return scale(1/speed,direction),speed


def frame(a,phases):return [[phases[i]*z*phases[j].conjugate() for j,z in enumerate(row)] for i,row in enumerate(a)]


def main():
    assert json.loads(FREEZE.read_text())['disposition']=='preregistered; not yet computed'
    with ZipFile(SOURCE) as archive:
        manifest=json.loads(archive.read('SHA256.json'))
        for name,digest in manifest.items():assert sha256(archive.read(name)).hexdigest()==digest
        raw=archive.read('pentachoron_connected_phase_energy_results.json');source=json.loads(raw)
    read=lambda name:[[scalar(v) for v in row] for row in source['matrices'][name]]
    LO,LC,X,P=map(read,('L_original','L_connected','cycle_X','matching_P'))
    HO,HC=add(LO,X),add(LC,X);n=len(HO);assert n==20
    I,Z=eye(n),zero(n)
    assert norm(diff(P,adj(P)))<2e-11 and norm(diff(mm(P,P),P))<2e-11 and abs(trace(P)-2)<2e-11
    values=source['with_retained_cycles']['original_spectrum'];groups=[]
    for E in values:
        if not groups or abs(E-groups[-1][0])>1e-8:groups.append([])
        groups[-1].append(E)
    energies=[sum(g)/len(g) for g in groups]
    Pg=projector(HO,energies,0)
    assert norm(diff(mm(HO,Pg),scale(energies[0],Pg)))<2e-9
    assert norm(diff(mm(Pg,Pg),Pg))<2e-9 and abs(trace(Pg)-4)<2e-9
    actual=scale(1/4,Pg);rho0=block(actual,Z,Z,Z)
    H=block(add(HO,scale(2,P)),scale(-2,P),scale(-2,P),add(HC,scale(2,P)))
    free=block(HO,Z,Z,HC)
    Q=block(Z,scale(-1j,P),scale(1j,P),Z)
    J=block(diff(I,P),P,P,diff(I,P))
    weight=trace(mm(actual,P)).real;assert weight>1e-6
    direction=generator(H,rho0);initial_speed=reading(direction,Q)
    residuals={'contact_hermitian':norm(diff(H,adj(H))),
        'incoming_free_stationarity':norm(generator(free,rho0)),
        'initial_phase_slope_identity':abs(initial_speed-4*weight),
        'trace_direction':abs(trace(direction)),
        'energy_direction':abs(trace(mm(direction,H))),
        'gate_involution':norm(diff(mm(J,J),eye(2*n)))}
    assert max(residuals.values())<2e-9
    assert norm(direction)>1e-3 and initial_speed>0 and reading(rho0,Q)==0
    # First-order coherence is generated from the actual mixture, no specially
    # phased initial state. Its matching formula is checked as a full block.
    cross=[r[n:] for r in direction[:n]]
    assert norm(diff(cross,scale(-2j,mm(actual,P))))<2e-9
    try:clock_direction(free,rho0,Q)
    except ValueError:pass
    else:raise AssertionError('Disabled matching gate admitted a clock')
    # Two exact applications of the bare return gate do not yield elapsed
    # phase: they restore the entire density. Assembly labels alone are no clock.
    after=mm(mm(J,rho0),adj(J));returned=mm(mm(J,after),adj(J))
    assert norm(diff(returned,rho0))<2e-9
    base_coeff=coefficients(H,rho0)
    rate=3.0;scaled_H=scale(rate,H);scaled_coeff=coefficients(scaled_H,rho0)
    initial_energy=trace(mm(rho0,H)).real;cases=[]
    for target in (weight*0.004,weight*0.008,weight*0.016):
        state=clock_state(base_coeff,Q,target);other=clock_state(scaled_coeff,Q,target)
        chart,speed=clock_direction(H,state,Q)
        other_chart,other_speed=clock_direction(scaled_H,state,Q)
        errors={'clock_readout':abs(reading(state,Q)-target),
                'trace':abs(trace(state)-1),'hermitian':norm(diff(state,adj(state))),
                'energy':abs(trace(mm(state,H)).real-initial_energy),
                'rate_independent_state':norm(diff(state,other)),
                'rate_independent_clock_direction':norm(diff(chart,other_chart))}
        assert max(errors.values())<2e-9 and speed>0
        # The reconstructed clock derivative of its own reading is exactly one.
        assert abs(reading(chart,Q)-1)<2e-9
        populations=[state[i][i].real for i in range(2*n)]
        connected=sum(populations[n:]);assert connected>0 and min(populations)>-2e-10
        full_change=norm(diff(state,rho0));assert full_change>1e-4
        phases=[1+0j]*n+[cmath.exp(0.731j)]*n
        framed_H,framed_rho,framed_Q=(frame(a,phases) for a in (H,state,Q))
        assert abs(reading(framed_rho,framed_Q)-target)<2e-9
        assert abs(reading(generator(framed_H,framed_rho),framed_Q)-speed)<2e-9
        cases.append({'state_read_clock':target,'clock_direction_denominator_model_units':speed,
            'all_forty_populations':populations,'connected_record_occupation':connected,
            'full_density':encoded(state),'density_change_norm':full_change,'residuals':errors})
    checks={'source_archive_and_matching_projector_verified':True,
        'actual_incoming_mixture_needs_no_coherent_control_preparation':True,
        'contact_creates_cross_topology_coherence':True,
        'initial_clock_slope_equals_four_matching_weight':True,
        'disabled_gate_has_no_clock_and_chart_is_rejected':True,
        'phase_clock_predicts_all_forty_record_populations':True,
        'common_generator_rate_cancels_from_relational_state_and_direction':True,
        'trace_and_full_frozen_contact_energy_retained':True,
        'consistent_branch_rephasing_does_not_change_clock':True,
        'bare_two_gate_return_does_not_accumulate_state_phase':True}
    result={'status':'passed','checks':checks,
        'scientific_disposition':'Existing contact Hamiltonian generates clock-readable coherence from the actual incoming mixture. This yields a local relational evolution chart with no external rate in its observable relations. The bare involutive two-pass gate supplies no accumulated phase; no inevitable discrete two-cycle update or global time is derived.',
        'source_matching_weight':weight,'initial_phase_slope_model_units':initial_speed,
        'initial_cross_block_formula':'generator(rho)_OC=-2i rho_original P',
        'local_relational_equation':'d rho/d chi = -i[H,rho] / Tr(-i[H,rho] Q)',
        'phase_clock_operator':encoded(Q),'existing_contact_operator':encoded(H),
        'actual_initial_density':encoded(rho0),'cases':cases,'initial_residuals':residuals,
        'source_coordinate_count':40,'maximum_initial_residual':max(residuals.values()),
        'processing_boundary':'The source already supplies this contact Hamiltonian and its Hamiltonian evolution semantics. It does not identify the bare gate or these continuous orbits with a unique two-cycle assembly schedule.',
        'clock_boundary':'Local chart only where phase derivative is nonzero. Monotone global time, clock-reset authority, winding, source-selected processing increments, seconds and GR remain separate.',
        'new_spatial_result_context':'Matched spatial refinement retains expansion-directed strain current but changes its magnitude. No strain or mode-count clock is inferred. This finite contact test does not verify the refined full scattering model.',
        'source_hashes':{SOURCE.relative_to(ROOT).as_posix():sha256(SOURCE.read_bytes()).hexdigest(),
                        FREEZE.relative_to(ROOT).as_posix():sha256(FREEZE.read_bytes()).hexdigest(),
                        CONTEXT.relative_to(ROOT).as_posix():sha256(CONTEXT.read_bytes()).hexdigest(),
                        'archived_phase_receipt':sha256(raw).hexdigest(),
                        'checker':sha256(Path(__file__).read_bytes()).hexdigest(),
                        'matrix_helpers':sha256(Path(__file__).with_name('check_native_relational_clock.py').read_bytes()).hexdigest()},
        'scope':'Standard-library numerical matrix audit and algebraic generator identities. Auxiliary orbit coordinates are eliminated, not declared physical time. No supplier rerun, continuum certificate or calibrated time.'}
    out=ROOT/'research/strominger/results/assembly-generated-clock.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'matching_weight':weight,
        'initial_phase_slope':initial_speed,'clock_generated_from_actual_input':True,
        'bare_two_pass_gate_advances_phase':False,
        'maximum_initial_residual':max(residuals.values()),
        'clock_cases':[{'chi':c['state_read_clock'],'connected_occupation':c['connected_record_occupation'],
                        'rate_rescaling_state_error':c['residuals']['rate_independent_state']} for c in cases]},indent=2))

if __name__=='__main__':main()
